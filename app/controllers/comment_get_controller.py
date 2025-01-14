from http import HTTPStatus

import sqlalchemy
from flask import current_app, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.comment_model import CommentModel


@jwt_required()
def comment_get(group_id):
    session: Session = db.session
    base_query = session.query(CommentModel)
    try:
        comments = base_query.filter_by(group_id=group_id).all()
        return jsonify(comments), HTTPStatus.OK
    except sqlalchemy.exc.ProgrammingError:
        return (
            jsonify({'message': 'Ainda não existem grupos cadastrados'}),
            HTTPStatus.OK,
        )
