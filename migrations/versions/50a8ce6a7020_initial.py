"""initial

Revision ID: 50a8ce6a7020
Revises: 
Create Date: 2023-06-05 16:13:47.698289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50a8ce6a7020'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Numeric(precision=8, scale=2), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favorite_cakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cake_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cake_id'], ['cakes.id'], name=op.f('fk_favorite_cakes_cake_id_cakes')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_favorite_cakes_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('_total_price', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_orders_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('cake_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cake_id'], ['cakes.id'], name=op.f('fk_reviews_cake_id_cakes')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_reviews_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_cakes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('cake_id', sa.Integer(), nullable=True),
    sa.Column('_price', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['cake_id'], ['cakes.id'], name=op.f('fk_order_cakes_cake_id_cakes')),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name=op.f('fk_order_cakes_order_id_orders')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_cakes')
    op.drop_table('reviews')
    op.drop_table('orders')
    op.drop_table('favorite_cakes')
    op.drop_table('users')
    op.drop_table('cakes')
    # ### end Alembic commands ###
