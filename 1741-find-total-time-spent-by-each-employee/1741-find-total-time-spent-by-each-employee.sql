/* Write your T-SQL query statement below */


with temp_table as (
select event_day,emp_id,(out_time-in_time) as stayed_duration
from Employees)

select event_day as day,emp_id, sum(stayed_duration) as total_time
from temp_table
group by event_day,emp_id