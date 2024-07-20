"""create address table

Revision ID: e575df1e3150
Revises: e5d223416a97
Create Date: 2024-07-19 17:10:00.477142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e575df1e3150'
down_revision: Union[str, None] = 'e5d223416a97'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'address',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('street', sa.String),
        sa.Column('city', sa.String),
        sa.Column('state', sa.String),
        sa.Column('zip', sa.String),
    )


def downgrade() -> None:
    op.drop_table('address')