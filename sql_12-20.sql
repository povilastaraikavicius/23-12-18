

-- Get all unique Ford models in range F250 - F500 using Betwen/AND syntax

SELECT * FROM cars WHERE model BETWEEN "F150" and "F600"

SELECT distinct model FROM cars where make = 'Ford' and cast(substr(model, 2) as integer) between 250 and 500 order by model desc;


SELECT * FROM cars order by model

SELECT * FROM cars WHERE price BETWEEN 1500 AND 5000;


INSERT INTO cars 
	(make, model, color, year, price)
VALUES
	("Ford", "F500", "White", 2020, 50000),
	("Ford", "F650", "Black", 2020, 500000);
	
	
	
SELECT * FROM cars WHERE year IN (1995, 2000, 2010);

SELECT * FROM cars WHERE color in ("Red", "Yellow") AND year >2000


SELECT * FROM cars WHERE make LIKE'__n%';

SELECT * FROM cars WHERE color IS NULL;


SELECT "GAMINTOJAS: " || make as gamintojas, model FROM cars;

SELECT make||" "||model AS "full_name", year, color FROM cars;

SELECT * FROM(
SELECT make, model, 2023 - year AS "age" FROM cars)
WHERE age <10

SELECT make, model, price, ROUND(price / 121.0 * 100, 2) AS "be PVM" FROM cars;

SELECT make, model, min(price) FROM cars WHERE make="Ford" GROUP BY make,model;
 
SELECT make, count(*) FROM cars GROUP BY make ORDER BY count(*) DESC;

SELECT color, max(price), make, model FROM cars GROUP BY color ORDER BY price DESC;


