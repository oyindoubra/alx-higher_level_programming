-- Lists all records in the table  with a score >= 10 
-- Record descending in order
SELECT `score`, `name`0
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
