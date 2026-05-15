from psycopg.rows import dict_row

from app.db import get_connection

def load_grades(rows):

    with get_connection() as conn:

        with conn.transaction():

            with conn.cursor() as cur:

                cur.execute("TRUNCATE TABLE grades")

                cur.executemany(
                    """
                    INSERT INTO grades (
                        grade_date,
                        group_name,
                        full_name,
                        grade
                    )
                    VALUES (%s, %s, %s, %s)
                    """,
                    rows
                )

    unique_students = len(
        set((row[1], row[2]) for row in rows)
    )

    return {
        "status": "ok",
        "records_loaded": len(rows),
        "students": unique_students,
    }


def get_students_more_than_3_twos():

    with get_connection() as conn:

        with conn.cursor(row_factory=dict_row) as cur:

            cur.execute(
                """
                SELECT
                    full_name,
                    COUNT(*) AS count_twos
                FROM grades
                WHERE grade = 2
                GROUP BY full_name, group_name
                HAVING COUNT(*) > 3
                ORDER BY count_twos DESC
                """
            )

            return cur.fetchall()


def get_students_less_than_5_twos():

    with get_connection() as conn:

        with conn.cursor(row_factory=dict_row) as cur:

            cur.execute(
                """
                SELECT
                    full_name,
                    COUNT(*) AS count_twos
                FROM grades
                WHERE grade = 2
                GROUP BY full_name, group_name
                HAVING COUNT(*) < 5
                ORDER BY count_twos DESC
                """
            )

            return cur.fetchall()