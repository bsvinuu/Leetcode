/* Write your T-SQL query statement below */


select distinct(num) as ConsecutiveNums 
from (
select *,
lag(num,1) over (ORDER BY (SELECT NULL)) AS lag1,
lag(num,2) over (ORDER BY (SELECT NULL)) AS lag2
from Logs) sub_query
where num=lag1 and num=lag2
-- where num=lag1 and num=lag2