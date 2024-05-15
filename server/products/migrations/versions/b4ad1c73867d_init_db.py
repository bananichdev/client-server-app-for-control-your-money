"""init_db

Revision ID: b4ad1c73867d
Revises: 
Create Date: 2024-05-16 00:55:17.864498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4ad1c73867d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.Date(), nullable=False),
    sa.Column('updated_date', sa.Date(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='products'
    )
    op.create_index(op.f('ix_products_category_id'), 'category', ['id'], unique=False, schema='products')
    op.create_index(op.f('ix_products_category_owner_id'), 'category', ['owner_id'], unique=False, schema='products')
    op.create_table('product',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.Date(), nullable=False),
    sa.Column('updated_date', sa.Date(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['products.category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='products'
    )
    op.create_index(op.f('ix_products_product_id'), 'product', ['id'], unique=False, schema='products')
    op.create_index(op.f('ix_products_product_owner_id'), 'product', ['owner_id'], unique=False, schema='products')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_product_owner_id'), table_name='product', schema='products')
    op.drop_index(op.f('ix_products_product_id'), table_name='product', schema='products')
    op.drop_table('product', schema='products')
    op.drop_index(op.f('ix_products_category_owner_id'), table_name='category', schema='products')
    op.drop_index(op.f('ix_products_category_id'), table_name='category', schema='products')
    op.drop_table('category', schema='products')
    # ### end Alembic commands ###
