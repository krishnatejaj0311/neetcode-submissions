-- Write your query below
select name from (
select id, name from customers where 
id not in (select customer_id from orders)
)