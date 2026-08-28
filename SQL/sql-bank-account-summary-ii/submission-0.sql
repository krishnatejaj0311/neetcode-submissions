-- Write your query below
select name, balance from (
select name, account, SUM(amount) as balance from (
select users.name, 
users.account,
transactions.trans_id,
transactions.amount,
transactions.transacted_on
from users
inner join 
transactions
on (users.account = transactions.account)
) group by 1, 2 
) where balance > 10000