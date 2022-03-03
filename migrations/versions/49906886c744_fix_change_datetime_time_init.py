"""fix: change datetime time_init

Revision ID: 49906886c744
Revises: e3a47489a3a3
Create Date: 2022-03-02 21:40:44.236536

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '49906886c744'
down_revision = 'e3a47489a3a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('activities', 'timer_init',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('activities', 'timer_init',
               existing_type=sa.String(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    # ### end Alembic commands ###
