-- Lists all records of the 2nd table  having a name value in my MySQL 
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
