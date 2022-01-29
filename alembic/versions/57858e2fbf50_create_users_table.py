"""create users table

Revision ID: 57858e2fbf50
Revises: 
Create Date: 2022-01-28 21:06:13.250163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57858e2fbf50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('uuid', sa.String(50), primary_key=True),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('name', sa.String(200)),
    )


def downgrade():
    op.drop_table('users')
