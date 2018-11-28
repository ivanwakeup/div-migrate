"""update model to reference multiple cust accounts

Revision ID: bc6272e06a0f
Revises: 038550004839
Create Date: 2018-11-27 17:36:32.054591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc6272e06a0f'
down_revision = '038550004839'
branch_labels = None
depends_on = None

Session = sa.orm.sessionmaker()

def upgrade():
    op.create_table('accounts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.id'), nullable=True)
        )

    bind = op.get_bind()
    session = Session(bind=bind)
    
    session.execute('INSERT INTO accounts(company_id) select id from companies;')
    
    op.add_column('daily_balances', sa.Column('account_id', sa.Integer, sa.ForeignKey('accounts.id', nullable=True))
    session.execute('INSERT INTO daily_balances(account_id) select id from accounts where daily_balances.company_id = accounts.company_id;')
    op.drop_constraint('daily_balances_company_id_fkey', 'daily_balances')
    op.drop_column('daily_balances', 'company_id')

def downgrade():
    pass
