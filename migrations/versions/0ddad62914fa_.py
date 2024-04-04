"""empty message

Revision ID: 0ddad62914fa
Revises: fe3ebfc6b60a
Create Date: 2024-03-23 10:41:11.905269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ddad62914fa'
down_revision = 'fe3ebfc6b60a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=50), nullable=True))
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.drop_column('name')

    # ### end Alembic commands ###