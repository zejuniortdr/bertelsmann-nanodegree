# QUESTION SET 1

## Question 1

We want to understand more about the movies that families are watching. The following categories are considered family movies: Animation, Children, Classics, Comedy, Family and Music.

Based on question 1, create a query that shows for each category, the number of movies it contains and the total number of rentals made

```sql
WITH films_per_category AS(
    SELECT
        c.name as category_name,
        COUNT(fc.film_id) as films_quantity
    FROM 
        film f
            JOIN film_category fc ON fc.film_id = f.film_id
            JOIN category c ON c.category_id = fc.category_id
    WHERE
        c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
    GROUP BY 1
    ORDER BY 2 DESC
)
SELECT
	fpc.category_name,
    fpc.films_quantity,
    COUNT(*) as total_rental
FROM rental r
	join inventory i on i.inventory_id = r.inventory_id
    join film f on f.film_id = i.film_id
    join film_category fc on fc.film_id = f.film_id
    join category c on c.category_id = fc.category_id
    join films_per_category fpc on fpc.category_name = c.name
GROUP BY 1, 2
ORDER BY 3 DESC
```


## Question 2
Based on Question 2, now we need to know many rentals occured per family-friendly category and day of week.

```sql

SELECT 
    to_char(rental_date, 'Day') as day_of_week,
    c.name as category_name,
    count(*) as total_rentals
FROM rental r
	JOIN inventory i ON i.inventory_id = r.inventory_id
    JOIN film f ON i.film_id = f.film_id
    JOIN film_category fc ON fc.film_id = f.film_id
    JOIN category c ON c.category_id = fc.category_id
WHERE
  c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
GROUP BY 1, 2
ORDER BY 3 desc
```

## Question 3
Finally, provide a table with the family-friendly film category, each of the quartiles, and the corresponding count of movies within each combination of film category for each corresponding rental duration category. The resulting table should have three columns:

- Category
- Rental length category
- Count

```sql
WITH temp_table AS (
    SELECT
        f.title AS film_title,
        c.name AS category_name,
        rental_duration,
        NTILE(4) OVER(ORDER BY rental_duration) AS standard_quartile
    FROM 
        film f
            JOIN film_category fc ON fc.film_id = f.film_id
            JOIN category c ON c.category_id = fc.category_id
            JOIN inventory i ON i.film_id = f.film_id
            JOIN rental r ON r.inventory_id = i.inventory_id
    WHERE
        c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
    GROUP BY 1, 2, 3
    ORDER BY 2
)
SELECT 
    category_name, 
    standard_quartile,
    COUNT(*) AS count
FROM 
    temp_table
GROUP BY 1, 2
ORDER BY 1, 2
```

# QUESTION SET 2

## Question 1
Question 1:
We want to find out how the two stores compare in their count of rental orders during every month for all the years we have data for. Write a query that returns the store ID for the store, the year and month and the number of rental orders each store has fulfilled for that month. Your table should include a column for each of the following: year, month, store ID and count of rental orders fulfilled during that month.

```sql
SELECT 
    EXTRACT(MONTH FROM rental_date) AS rental_month,
    EXTRACT(YEAR FROM rental_date) AS rental_year,
    store.store_id AS store_id,
    COUNT(*) AS count_rentals
FROM 
	store
    	JOIN staff ON staff.store_id = store.store_id
        JOIN rental ON rental.staff_id = staff.staff_id
GROUP BY 1, 2, 3
ORDER BY 2, 1 ASC, 4 DESC
```

## Question 2
Question 2
We would like to know who were our top 10 paying customers, how many payments they made on a monthly basis during 2007, and what was the amount of the monthly payments. Can you write a query to capture the customer name, month and year of payment, and total payment amount for each month by these top 10 paying customers?

```sql
WITH top10 AS (
    SELECT 
        customer_id,
        sum(amount)
    FROM payment
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
) 
SELECT 
    DATE_TRUNC('month', payment_date) AS pay_mon,
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    COUNT(*) AS pay_countpermon,
    SUM(amount) AS pay_amount
FROM payment p
    JOIN top10 ON top10.customer_id = p.customer_id AND EXTRACT(YEAR FROM payment_date) = 2007
    JOIN customer c ON c.customer_id = p.customer_id
GROUP BY 1, 2
ORDER BY 2
```