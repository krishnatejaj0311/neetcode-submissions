-- Write your query below

select expressions.left_operand,
expressions.operator,
expressions.right_operand,
case 
when expressions.operator = '>' and left_value.value > right_value.value then 'true'
when expressions.operator = '<' and left_value.value < right_value.value then 
'true'
when expressions.operator = '=' and left_value.value = right_value.value then 'true'
else 'false'
end as value
from expressions

join variables as left_value on left_value.name = expressions.left_operand
join variables as right_value on right_value.name = expressions.right_operand
