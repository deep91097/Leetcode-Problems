# Write your MySQL query statement below
WITH RECURSIVE cte AS (
    SELECT employee_id,employee_name,
    manager_id, 1 as level
    FROM Employees
    WHERE manager_id is null

    UNION
    SELECT e.employee_id,e.employee_name,
    e.manager_id
    , c.level + 1
    FROM employees e
    INNER JOIN cte c
    ON e.manager_id = c.employee_id
),
cte2 as (
    select employee_id, employee_id as manager_id 
    from Employees
    UNION
    SELECT e.employee_id, c2.manager_id
    FROM cte2 as c2
    inner join Employees as e
    on c2.employee_id = e.manager_id
)
,cte3 as(
select c1.employee_id, c1.employee_name, c1.level, c2.manager_id,
c2.employee_id as eid,
e.salary

from cte as c1
inner join cte2 as c2
on c1.employee_id = c2.manager_id
inner join Employees e on
c2.employee_id = e.employee_id
)
select employee_id,employee_name,level
,
count(distinct case when employee_id <> eid then eid else null end) as team_size,
SUM(salary) as budget
from cte3
group by employee_id,employee_name,level
order by level,budget desc,employee_name;