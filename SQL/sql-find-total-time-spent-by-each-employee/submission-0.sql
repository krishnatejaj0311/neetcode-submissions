-- Write your query below
select day, emp_id, sum(total_time) as total_time from (
select emp_id, event_day as day, in_time, out_time, out_time-in_time as total_time
from employees
group by 1, 2,3,4
) group by 1, 2