"""criando tabelas

Revision ID: fc21ead17058
Revises:
Create Date: 2022-03-02 13:14:23.390453
"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fc21ead17058'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'cards',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('tile', sa.String(length=64), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'categories',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )
    op.create_table(
        'groups',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('title', sa.String(length=64), nullable=False),
        sa.Column('privacy', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('title'),
    )
    op.create_table(
        'images',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('image', sa.TEXT(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'activities',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('category_id', postgresql.UUID(), nullable=True),
        sa.Column('card_id', postgresql.UUID(), nullable=True),
        sa.Column('timer_total', sa.DateTime(), nullable=True),
        sa.Column('timer_init', sa.DateTime(), nullable=True),
        sa.Column('favorite', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ['card_id'],
            ['cards.id'],
        ),
        sa.ForeignKeyConstraint(
            ['category_id'],
            ['categories.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(length=64), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password_hash', sa.String, nullable=False),
        sa.Column('image_id', postgresql.UUID(), nullable=True),
        sa.Column('activity_id', postgresql.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ['activity_id'],
            ['activities.id'],
        ),
        sa.ForeignKeyConstraint(
            ['image_id'],
            ['images.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    op.create_table(
        'comments',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('group_id', postgresql.UUID(), nullable=True),
        sa.Column('user_id', postgresql.UUID(), nullable=True),
        sa.Column('comment', sa.TEXT(), nullable=False),
        sa.Column('hour', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ['group_id'],
            ['groups.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'users_groups',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('user_id', postgresql.UUID(), nullable=True),
        sa.Column('group_id', postgresql.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ['group_id'],
            ['groups.id'],
        ),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_groups')
    op.drop_table('comments')
    op.drop_table('users')
    op.drop_table('activities')
    op.drop_table('images')
    op.drop_table('groups')
    op.drop_table('categories')
    op.drop_table('cards')
    # ### end Alembic commands ###
