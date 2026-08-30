SELECT *
FROM walmart_sales
LIMIT 10;


SELECT
    MIN(Date) AS first_date,
    MAX(Date) AS last_date
FROM walmart_sales;

SELECT
    COUNT(*) AS total_rows,
    SUM(Store IS NULL) AS null_store,
    SUM(Date IS NULL) AS null_date,
    SUM(Weekly_Sales IS NULL) AS null_sales,
    SUM(Holiday_Flag IS NULL) AS null_holiday,
    SUM(Temperature IS NULL) AS null_temperature,
    SUM(Fuel_Price IS NULL) AS null_fuel,
    SUM(CPI IS NULL) AS null_cpi,
    SUM(Unemployment IS NULL) AS null_unemployment
FROM walmart_sales;

-- Basic Overview
SELECT COUNT(DISTINCT Store) AS total_stores
FROM walmart_sales;

SELECT
    MIN(Date) AS first_date,
    MAX(Date) AS last_date
FROM walmart_sales;

SELECT
    SUM(Weekly_Sales) AS total_sales
FROM walmart_sales;

SELECT
    AVG(Weekly_Sales) AS average_weekly_sales
FROM walmart_sales;

SELECT
    MAX(Weekly_Sales) AS highest_weekly_sales,
    MIN(Weekly_Sales) AS lowest_weekly_sales
FROM walmart_sales;

-- Store performance analysis

SELECT
    Store,
    SUM(Weekly_Sales) AS total_sales
FROM walmart_sales
GROUP BY Store
ORDER BY total_sales DESC;

SELECT
    Store,
    SUM(Weekly_Sales) AS total_sales
FROM walmart_sales
GROUP BY Store
ORDER BY total_sales ASC;

SELECT
    Store,
    AVG(Weekly_Sales) AS average_weekly_sales
FROM walmart_sales
GROUP BY Store
ORDER BY average_weekly_sales DESC;

SELECT
    Holiday_Flag,
    SUM(Weekly_Sales) AS total_sales
FROM walmart_sales
GROUP BY Holiday_Flag;

SELECT
    Holiday_Flag,
    AVG(Weekly_Sales) AS average_weekly_sales
FROM walmart_sales
GROUP BY Holiday_Flag;

select year(`date`) as year,
sum(weekly_sales) as total_sales
from walmart_sales
group by year(`date`)
order by year desc;

select year(`date`) as year,
month(`date`) as month,
sum(weekly_sales) as total_sales
from walmart_sales
group by year(`date`),month(`date`)
order by year,month;

-- slight differnce in both these the aboveone and the below one
SELECT
    MONTH(`Date`) AS month_number,
    MONTHNAME(`Date`) AS month_name,
    SUM(`Weekly_Sales`) AS total_sales
FROM walmart_sales
GROUP BY
    MONTH(`Date`),
    MONTHNAME(`Date`)
ORDER BY month_number;

-- top 10 store by avg weekly sales

select 
	store,
    round(avg(weekly_sales),2) as average_weekly_sales
from walmart_sales
group by store
order by average_weekly_sales desc
limit 10;

select holiday_flag,
count(*) as total_count,
round(sum(weekly_sales),2) as total_sales,
round(avg(weekly_sales),2) as avg_sales
from walmart_sales
group by holiday_flag;


select store,
round(sum(weekly_sales),2) as total_sales
from walmart_sales
where holiday_flag = 1
group by store
order by total_sales desc
limit 10;

select temperature,
round(avg(weekly_sales),2) as avg_total_sales
from walmart_sales
group by temperature
order by Temperature;


select 
case
	when temperature < 30 then 'Below 30°'
    when temperature < 50 then 'Below 50°'
    when temperature < 70 then 'Below 70°'
    when temperature < 90 then 'Below 90°'
    else '90° and above'
end as temperature_range,
count(*) as number_of_weeks,
round(avg(weekly_sales),2) as avg_sales
from walmart_sales
group by temperature_range
order by avg_sales desc;

SELECT
    CASE
        WHEN Fuel_Price < 2.5 THEN 'Below 2.5'
        WHEN Fuel_Price < 3.0 THEN '2.5-2.99'
        WHEN Fuel_Price < 3.5 THEN '3.0-3.49'
        WHEN Fuel_Price < 4.0 THEN '3.5-3.99'
        ELSE '4.0 and above'
    END AS fuel_price_range,
    COUNT(*) AS number_of_weeks,
    ROUND(AVG(Weekly_Sales), 2) AS average_weekly_sales
FROM walmart_sales
GROUP BY fuel_price_range
ORDER BY average_weekly_sales DESC;


select 
case
	when cpi < 100 then 'Below 180'
    when cpi < 200 then 'Below 200'
    when cpi < 300 then 'Below 300'
    else '300 and above'
end as cpi_range,
count(*) as total_count,
round(avg(weekly_sales),2) as avg_weekly_sales
from walmart_sales
group by cpi_range
order by avg_weekly_sales desc;

SELECT
    CASE
        WHEN Unemployment < 5 THEN 'Below 5%'
        WHEN Unemployment < 7 THEN '5-6.99%'
        WHEN Unemployment < 9 THEN '7-8.99%'
        WHEN Unemployment < 11 THEN '9-10.99%'
        ELSE '11% and above'
    END AS unemployment_range,
    COUNT(*) AS number_of_weeks,
    ROUND(AVG(Weekly_Sales), 2) AS average_weekly_sales
FROM walmart_sales
GROUP BY unemployment_range
ORDER BY average_weekly_sales DESC;

select store,
`date`,
weekly_sales,
holiday_flag
from walmart_sales
order by Weekly_Sales desc
limit 10;

SELECT
Store,
`Date`,
Weekly_Sales,
Holiday_Flag
FROM walmart_sales
ORDER BY Weekly_Sales asc
LIMIT 10;

SELECT
    YEAR(`Date`) AS year,
    ROUND(SUM(Weekly_Sales), 2) AS total_sales
FROM walmart_sales
GROUP BY YEAR(`Date`)
ORDER BY year;

-- yoy growth 

with yearly_sales as(
select YEAR(`date`) as year,
round(sum(weekly_sales),2) as total_sales
from walmart_sales
group by YEAR(`date`)
)
select 
year,
round(total_sales,2) as total_sales,
round(
	(total_sales - lag(total_sales) over (order by year))
    / lag(total_sales) over(order by year) * 100 ,2
) as yoy_growth_percent
from yearly_sales
order by year;

SELECT
    Store,
    ROUND(AVG(Weekly_Sales), 2) AS average_weekly_sales,
    ROUND(STDDEV(Weekly_Sales), 2) AS sales_stddev
FROM walmart_sales
GROUP BY Store
ORDER BY sales_stddev ASC;






    



















