USE CIS;

drop table customer;
create table customer(c_id int, dates date);

insert into customer values
(1111,'2022-12-01'),
(1111,'2022-10-01'),
(1111,'2022-09-01'),
(1111,'2023-01-01'),
(2222,'2022-01-01'),
(2222,'2022-05-01'),
(2222,'2022-04-01');

select * from customer;

SELECT c_id, Round(DATEDIFF(dates, MIN(dates) OVER (PARTITION BY c_id)) / 30) AS month_difference
FROM customer;
 

SELECT c.c_id, Round(datediff(c.dates, min_dates.min_date)/30) AS date_difference
FROM customer c
JOIN (
  SELECT c_id, MIN(dates) AS min_date
  FROM customer
  GROUP BY c_id
) min_dates ON c.c_id = min_dates.c_id;