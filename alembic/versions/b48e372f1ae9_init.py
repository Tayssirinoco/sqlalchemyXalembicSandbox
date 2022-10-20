"""init

Revision ID: b48e372f1ae9
Revises: 
Create Date: 2022-10-20 22:02:00.468077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b48e372f1ae9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'jobs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('jobs')
