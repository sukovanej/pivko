"""products: add shop column

Revision ID: edd5c035e28e
Revises: be73503fbcf5
Create Date: 2020-04-25 22:06:05.965434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edd5c035e28e'
down_revision = 'be73503fbcf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('shop', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'shop')
    # ### end Alembic commands ###
