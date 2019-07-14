"""empty message

Revision ID: 720d5f4c4cbf
Revises: e00711b0b021
Create Date: 2019-07-14 09:13:02.007856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '720d5f4c4cbf'
down_revision = 'e00711b0b021'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=True))
    op.execute('UPDATE users SET admin=False')
    op.alter_column('users', 'admin', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###
