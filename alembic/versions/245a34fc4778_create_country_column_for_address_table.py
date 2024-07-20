"""create country column for address table

Revision ID: 245a34fc4778
Revises: e575df1e3150
Create Date: 2024-07-19 17:39:01.112827

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '245a34fc4778'
down_revision: Union[str, None] = 'e575df1e3150'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("address", sa.Column("country", sa.String(), nullable=True))


def downgrade() -> None:
    pass
