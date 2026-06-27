/* Write your T-SQL query statement below */

Select p.product_name,sum(o.unit) as unit
from Orders o inner join Products p on o.product_id=p.product_id    
where year(o.order_date)=2020 and month(o.order_date)=2
group by p.product_name
HAVING SUM(o.unit) >= 100





