-- Write your query below
select sale_date, 
SUM(case when fruit = 'apples' then sold_num else 0 end) - 
SUM(case when fruit = 'oranges' then sold_num else 0 end) as diff
from sales
group by 1