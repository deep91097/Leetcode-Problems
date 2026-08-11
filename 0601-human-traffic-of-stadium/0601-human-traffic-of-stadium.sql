# Write your MySQL query statement below


with cte1 as (
Select *, (id - ROW_NUMBER() OVER(ORDER BY id)) as rnk
from Stadium 
where people >= 100
)

select id, visit_date, people
from cte1 where rnk in (
select rnk 
from cte1 group by rnk
having count(*) >=3) 
order by visit_date;

