"""empty message

Revision ID: 854592b405c1
Revises: d51e0d171164
Create Date: 2024-03-07 01:08:08.678233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '854592b405c1'
down_revision = 'd51e0d171164'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
