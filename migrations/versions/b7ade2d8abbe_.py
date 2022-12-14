"""empty message

Revision ID: b7ade2d8abbe
Revises: 
Create Date: 2022-08-15 16:24:35.504672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7ade2d8abbe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'todolists', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
