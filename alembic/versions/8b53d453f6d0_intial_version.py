"""intial version

Revision ID: 8b53d453f6d0
Revises: 
Create Date: 2022-07-17 12:38:53.199778

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '8b53d453f6d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('university',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('city', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('state', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('conference', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('division', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('category', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('region', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
    sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
    sa.Column('preferred_name', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
    sa.Column('bio', sqlmodel.sql.sqltypes.AutoString(length=1000), nullable=True),
    sa.Column('gender', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
    sa.Column('contact_number', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=True),
    sa.Column('current_address', sqlmodel.sql.sqltypes.AutoString(length=300), nullable=True),
    sa.Column('permanent_address', sqlmodel.sql.sqltypes.AutoString(length=300), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('experience',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(length=100), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profilephoto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('photo_url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profilephoto')
    op.drop_table('experience')
    op.drop_table('education')
    op.drop_table('user')
    op.drop_table('university')
    # ### end Alembic commands ###