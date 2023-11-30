"""Inventory bud-fix

Revision ID: 178a0b6d74eb
Revises: 929b559d5923
Create Date: 2023-11-28 16:30:09.217845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '178a0b6d74eb'
down_revision = '929b559d5923'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'in_stock')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('in_stock', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###