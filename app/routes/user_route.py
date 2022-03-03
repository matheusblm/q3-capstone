from flask import Blueprint

from app.controllers.user_post_controller import post_user
from app.controllers.user_login_controller import login
from app.controllers.user_patch_controller import update_user
from app.controllers.user_get_controller import user_get
from app.controllers.user_delete_controller import user_delete


bp = Blueprint("bp_user", __name__, url_prefix="/api/user")
bp.get("")(user_get)
bp.post("/register")(post_user)
bp.post("/login")(login)
bp.patch('')(update_user)
bp.delete("")(user_delete)
