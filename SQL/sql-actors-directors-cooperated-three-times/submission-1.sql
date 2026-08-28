-- Write your query below
select actor_id, director_id from (
select actor_id, director_id, COUNT(*) count1 from 
actor_director 
group by 1, 2
) where count1 >= 3