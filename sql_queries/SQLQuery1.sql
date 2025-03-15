use sales_data;


SELECT TOP 10 * FROM sales_data;

EXEC sp_columns sales_data;

SELECT * 
FROM sales_data
WHERE 
    [Invoice_ID] IS NULL OR
    [Branch] IS NULL OR
    [City] IS NULL OR
    [Customer_type] IS NULL OR
    [Gender] IS NULL OR
    [Product_line] IS NULL OR
    [Unit_price] IS NULL OR
    [Quantity] IS NULL OR
    [Tax_5] IS NULL OR
    [Total] IS NULL OR
    [Date] IS NULL OR
    [Time] IS NULL OR
    [Payment] IS NULL OR
    [cogs] IS NULL OR
    [gross_margin_percentage] IS NULL OR
    [gross_income] IS NULL OR
    [Rating] IS NULL;

--total sales per branch
select branch,City,round(sum(Total),0) AS Total Sales from sales_data group by branch,City;
--avg sales per branch
select branch,City,round(avg(Total),0) AS Avg Sales from sales_data group by branch,City;
--PAYMENT METHODS USED
select TOP 1 Payment,count(Payment) AS COUNTT from sales_data group by Payment order by COUNTT DESC;
select Payment,count(Payment) AS COUNTT from sales_data group by Payment;
---avg rating
select branch,round(avg(Rating),2) AS Avg Rating from sales_data group by branch;
--best selling product line in terms of revenue
select Product_line,round(sum(Total),2) AS Total revenue from sales_data group by Product_line order by Total Revenue desc;

--most qty
select Product_line,sum(Quantity) AS Total quantity sold from sales_data group by Product_line order by Total quantity sold desc;

--cust type spend
select Customer_type,round(sum(Total),2) as Total spend from sales_data group by Customer_type order by Total spend desc;

--avg unit price
select Product_line,round(avg(Unit_price),2) AS Avg unit price from sales_data group by Product_line order by Avg unit price desc;

--sales by month
select MONTH(Date),round(sum(Total),2) as total_sales from sales_data group by MONTH(Date)
