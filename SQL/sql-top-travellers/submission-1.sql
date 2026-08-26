-- Write your query below
select name, sum(case when distance is null then 0 else distance end) as travelled_distance from (
select users.name,
users.id,
rides.distance
from users
left join
rides
on (users.id = rides.user_id)
)
group by 1 order by travelled_distance desc