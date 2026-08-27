-- Write your query below
select name as warehouse_name, sum(units*volume) as volume from (
select name, product_id, units, product_name, width, length, height,
height*length*width as volume from (
select warehouse.name,
warehouse.product_id,
warehouse.units,
products.product_name,
products.width,
products.length,
products.height
from warehouse
inner join 
products
on (warehouse.product_id = products.product_id)
) 
group by 1, 2, 3, 4, 5, 6, 7
)
group by 1