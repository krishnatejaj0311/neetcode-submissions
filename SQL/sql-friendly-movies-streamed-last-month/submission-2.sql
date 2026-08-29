-- Write your query below
select distinct title from (
select tv_program.program_date,
tv_program.content_id,
tv_program.channel,
content.title,
content.kids_content,
content.content_type
from tv_program
inner join 
content
on (tv_program.content_id = content.content_id)
) where program_date like '2020-06-%' and kids_content = 'Y' and content_type = 'Movies'