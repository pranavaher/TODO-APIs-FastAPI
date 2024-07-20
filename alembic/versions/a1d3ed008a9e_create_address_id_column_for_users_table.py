"""create address_id column for users table

Revision ID: a1d3ed008a9e
Revises: 245a34fc4778
Create Date: 2024-07-19 17:41:09.902339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1d3ed008a9e'
down_revision: Union[str, None] = '245a34fc4778'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("address_id", sa.Integer, nullable=True))
    op.create_foreign_key("address_users_fk", source_table="users", referent_table="address", local_cols=["address_id"], remote_cols=["id"], ondelete="CASCADE")

def downgrade() -> None:
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column("users", "address_id")
