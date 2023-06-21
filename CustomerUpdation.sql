
use CIS;

CREATE TABLE Customers1 (
  Customer_Id INT,
  Store_ID INT,
  ZipCode VARCHAR(10),
  Effective_Date DATE
);

INSERT INTO Customers1 (Customer_Id, Store_ID, ZipCode, Effective_Date)
VALUES (1, 1001, '12345', '2018-06-20'),
(2, 1001, '12345', '2019-06-20'),
(1, 1003, '56789', '2020-06-20'),
(4, 1003, '56789', '2021-06-20'),
(5, 1003, '56789', '2022-06-20');


WITH cte as (
SELECT Customer_Id, store_id, zipcode,	
	CASE WHEN (LAG(effective_date) OVER(PARTITION BY Customer_Id) IS NULL AND 
               LEAD(effective_date) OVER(PARTITION BY Customer_Id) IS NULL ) THEN "New" ELSE "Existing" END AS "Status"
FROM Customers1 )

SELECT COUNT(Status) AS "Increased Customers" FROM cte WHERE Status = 'New' and store_id = '1001'