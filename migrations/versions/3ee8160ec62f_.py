"""empty message

Revision ID: 3ee8160ec62f
Revises: b0c1692627cf
Create Date: 2020-02-14 10:16:05.471740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3ee8160ec62f"
down_revision = "b0c1692627cf"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("project_customer_id_fkey", "project", type_="foreignkey")
    op.create_foreign_key(
        None, "project", "customer", ["customer_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "project", type_="foreignkey")
    op.create_foreign_key(
        "project_customer_id_fkey", "project", "customer", ["customer_id"], ["id"]
    )
    # ### end Alembic commands ###