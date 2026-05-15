from alembic import op
import sqlalchemy as sa

revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "grades",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("grade_date", sa.Date(), nullable=False),
        sa.Column("group_name", sa.String(length=100), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column(
            "grade",
            sa.Integer(),
            sa.CheckConstraint("grade BETWEEN 2 AND 5"),
            nullable=False,
        ),
    )

    op.create_index(
        "idx_grade",
        "grades",
        ["grade"],
    )


def downgrade():
    op.drop_index("idx_grade", table_name="grades")
    op.drop_table("grades")