"""empty message

Revision ID: 5e5c57ed6627
Revises: 
Create Date: 2020-12-08 15:53:42.947404

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5e5c57ed6627'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('performance_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inventory_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('performance_record', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('performance_score', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('report_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('inventory_id'),
    sa.UniqueConstraint('inventory_id', 'report_date')
    )
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('c1', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('c2', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('c3', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.UniqueConstraint('c2', 'c3', name='test_c2_c3_key')
    )
    op.drop_table('performance_profile')
    # ### end Alembic commands ###