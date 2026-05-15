CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    grade_date DATE NOT NULL,
    group_name VARCHAR(100) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    grade INTEGER NOT NULL CHECK (grade BETWEEN 2 AND 5)
);

CREATE INDEX idx_grade
ON grades(grade);