SELECT *
	FROM teachers
    WHERE tch_last_name = 'Bennett'
    AND tch_first_name = 'Catherine'
;

SELECT * FROM teachers WHERE tch_id = 'stfX2000001634';

UPDATE teachers 
	SET tch_last_name = 'Polk', tch_home_phone = '(617) 555-1234'
    WHERE tch_id = 'stfX2000001634'
;

SELECT * 
	FROM schools
;

UPDATE schools
	SET skl_level = 'K-4'
    WHERE skl_name LIKE '%Elementary'
;


