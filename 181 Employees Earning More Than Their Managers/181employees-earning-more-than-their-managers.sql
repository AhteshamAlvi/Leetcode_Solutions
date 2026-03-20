# Write your MySQL query statement below
SELECT e.name AS Employee FROM Employee e, Employee m WHERE e.managerid = m.id AND e.salary > m.salary;