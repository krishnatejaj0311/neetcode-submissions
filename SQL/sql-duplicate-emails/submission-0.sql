-- Write your query below
select email from (
select email, count(email) as email_count from person
group by 1 )
where email_count > 1