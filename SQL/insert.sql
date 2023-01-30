-- Inserting records into a table 

INSERT INTO students (stu_id, stu_first_name, stu_last_name, stu_grade_level)
			VALUES  ('cjxs001', 'Cole',			'Spencer',     '11')
;


SELECT * 
	FROM students 
    WHERE stu_id = 'cjxs001'
;