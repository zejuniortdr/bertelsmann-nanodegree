# QUESTION SET 1

## Question 1

We want to understand more about the movies that families are watching. The following categories are considered family movies: Animation, Children, Classics, Comedy, Family and Music.

Create a query that lists each movie, the film category it is classified in, and the number of times it has been rented out.

```sql
SELECT
    f.title as film_title,
    c.name as category_name,
    COUNT(*) as rental_count
FROM 
    film f
        JOIN film_category fc ON fc.film_id = f.film_id
        JOIN category c ON c.category_id = fc.category_id
        JOIN inventory i ON i.film_id = f.film_id
        JOIN rental r ON r.inventory_id = i.inventory_id
WHERE
    c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
GROUP BY 1, 2
```


## Question 2
Now we need to know how the length of rental duration of these family-friendly movies compares to the duration that all movies are rented for. Can you provide a table with the movie titles and divide them into 4 levels (first_quarter, second_quarter, third_quarter, and final_quarter) based on the quartiles (25%, 50%, 75%) of the rental duration for movies across all categories? Make sure to also indicate the category that these family-friendly movies fall into.

```sql
SELECT
    f.title AS film_title,
    c.name AS category_name,
    rental_duration,
    NTILE(4) OVER(ORDER BY sum(rental_duration)) AS standard_quartile
FROM 
    film f
        JOIN film_category fc ON fc.film_id = f.film_id
        JOIN category c ON c.category_id = fc.category_id
        JOIN inventory i ON i.film_id = f.film_id
        JOIN rental r ON r.inventory_id = i.inventory_id
WHERE
    c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
GROUP BY 1, 2, 3
ORDER BY 4, 3
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
    count(*) AS count_rentals
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
    concat(c.first_name, ' ', c.last_name) AS full_name,
    count(*) AS pay_countpermon,
    sum(amount) AS pay_amount
FROM payment p
    JOIN top10 ON top10.customer_id = p.customer_id AND EXTRACT(YEAR FROM payment_date) = 2007
    JOIN customer c ON c.customer_id = p.customer_id
GROUP BY 1, 2
ORDER BY 2
```