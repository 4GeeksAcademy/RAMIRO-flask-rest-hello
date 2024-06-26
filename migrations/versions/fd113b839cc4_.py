"""empty message

Revision ID: fd113b839cc4
Revises: 
Create Date: 2024-03-23 09:51:42.957005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd113b839cc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('heigth', sa.Integer(), nullable=True),
    sa.Column('mass', sa.Integer(), nullable=True),
    sa.Column('hair_color', sa.String(length=250), nullable=True),
    sa.Column('sking_color', sa.String(length=250), nullable=True),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('birth_year', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('gravity', sa.Integer(), nullable=True),
    sa.Column('diamer', sa.Integer(), nullable=True),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('population', sa.Integer(), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('apellido', sa.String(length=50), nullable=True),
    sa.Column('nombre_de_usuario', sa.String(length=50), nullable=True),
    sa.Column('contraseña', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.Column('DNI', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehiculos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('modelo', sa.String(length=100), nullable=True),
    sa.Column('vehicle_class', sa.String(length=100), nullable=True),
    sa.Column('passangres', sa.Integer(), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('consumables', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('personas_id', sa.Integer(), nullable=True),
    sa.Column('planetas_id', sa.Integer(), nullable=True),
    sa.Column('vehiculos_id', sa.Integer(), nullable=True),
    sa.Column('usuarios_DNI', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['personas_id'], ['personas.id'], ),
    sa.ForeignKeyConstraint(['planetas_id'], ['planetas.id'], ),
    sa.ForeignKeyConstraint(['usuarios_DNI'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['vehiculos_id'], ['vehiculos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritos')
    op.drop_table('vehiculos')
    op.drop_table('usuarios')
    op.drop_table('planetas')
    op.drop_table('personas')
    # ### end Alembic commands ###
