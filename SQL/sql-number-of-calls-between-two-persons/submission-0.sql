-- Write your query below
select LEAST(from_id, to_id) as person1,
GREATEST(from_id, to_id) as person2,
COUNT(*) as call_count,
SUM(duration) as total_duration
from calls
GROUP BY person1, person2