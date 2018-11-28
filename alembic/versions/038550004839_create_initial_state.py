"""create initial state

Revision ID: 038550004839
Revises: 
Create Date: 2018-11-27 15:40:32.924236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '038550004839'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('companies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('token', sa.String(), nullable=False)
        )
    op.create_table('daily_balances',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.id'), nullable=False),
        sa.Column('date', sa.Date),
        sa.Column('balance', sa.Float)
    )


def downgrade():
    pass
