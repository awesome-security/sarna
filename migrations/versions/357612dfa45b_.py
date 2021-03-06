"""empty message

Revision ID: 357612dfa45b
Revises: 49bab253b4ee
Create Date: 2018-07-04 23:07:54.313302

"""
from alembic import op
import sqlalchemy as sa
import sarna


# revision identifiers, used by Alembic.
revision = '357612dfa45b'
down_revision = '49bab253b4ee'
branch_labels = None
depends_on = None


def upgrade():
# ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('login_try', sa.SmallInteger(), nullable=False, server_default='0'))
    # ### end Alembic commands ###


def downgrade():
# ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'login_try')
    # ### end Alembic commands ###
