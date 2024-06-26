"""empty message

Revision ID: 9254eae2416e
Revises: 76b163f581c8
Create Date: 2024-03-23 10:48:46.336397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9254eae2416e'
down_revision = '76b163f581c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuarios_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('favoritos_usuarios_DNI_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'usuarios', ['usuarios_id'], ['id'])
        batch_op.drop_column('usuarios_DNI')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuarios_DNI', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('favoritos_usuarios_DNI_fkey', 'usuarios', ['usuarios_DNI'], ['id'])
        batch_op.drop_column('usuarios_id')

    # ### end Alembic commands ###
