-- This is a file for testung DELETE statments

-- 1. To delete a STUDENT, first indentify it's ID 
SELECT * 
	FROM students
    WHERE stu_first_name LIKE 'Matt%'
;

SELECT * 
	FROM students 
    WHERE stu_id = 'stdX2000001008'
;


-- 2. Delete the STUDENT itself 
DELETE 
	FROM students 
    WHERE stu_id = 'stdX2000001008'
;

-- 3. Delete all the chldren records to eliminate orphans 
SELECT * FROM attendance WHERE att_stu_id = 'stdX2000001008';
DELETE FROM attendance WHERE att_stu_id = 'stdX2000001008';
DELETE FROM transcripts WHERE trn_stu_id = 'stdX2000001008';
DELETE FROM schedules WHERE ssc_stu_id = 'stdX2000001008';

-- Let's see if there are any orphaned attendance records 

SELECT * 
	FROM students
    WHERE stu_last_name LIKE 'Le%'
    AND stu_grade_level = '12'
;

SELECT * 
	FROM students
    JOIN attendance ON stu_id = att_stu_id
    WHERE stu_last_name LIKE 'Le%'
    AND stu_grade_level = '12'
;
    
SELECT stu_id, stu_first_name, stu_last_name
	FROM students
    LEFT OUTER JOIN attendance ON stu_id = att_stu_id
    WHERE stu_last_name LIKE 'Le%'
    AND stu_grade_level = '12'
    AND att_stu_id IS NULL
;

SELECT *
	FROM attendance
    LEFT OUTER JOIN students ON stu_id = att_stu_id
    WHERE stu_id IS NULL
;

DELETE FROM students WHERE stu_last_name LIKE 'Z%'

-- This query SHOULD work but it takes way too long to execute
DElETE attendance 
	FROM attendance
    LEFT OUTER JOIN students
    ON stu_id = att_stu_id 
    WHERE stu_id IS NULL
;

-- We need another way to identify (and then delete) orphans 

-- Refresher: standard IN operator 
SELECT * 
	FROM students
    WHERE stu_grade_level IN ('01', '02')
;
-- Using in operator on a sub-select. This query finds all students in an Elementary School
SELECT *
	FROM students
    WHERE stu_skl_id NOT IN (SELECT skl_id FROM schools WHERE skl_name LIKE '%Elementary%')
;

-- Identify the orphaned attendance records using a SUB-SELECT (IN) clause 
SELECT *
	FROM attendance
    WHERE att_stu_id NOT IN (SELECT stu_id FROM students)
;

DELETE
	FROM attendance
    WHERE att_stu_id NOT IN (SELECT stu_id FROM students)
;

