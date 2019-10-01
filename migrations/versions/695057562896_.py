"""empty message

Revision ID: 695057562896
Revises: d2730425161f
Create Date: 2019-10-01 20:48:30.347346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '695057562896'
down_revision = 'd2730425161f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player', sa.Column('score', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('player', 'score')
    # ### end Alembic commands ###
