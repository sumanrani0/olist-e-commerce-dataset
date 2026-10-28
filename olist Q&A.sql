-- 1) Which sellers generate the highest revenue?

select s.seller_id ,round( sum(i.price)::numeric , 2) as revenue
from olist_sellers s
join olist_order_items i
on s.seller_id = i.seller_id
group by s.seller_id
order by revenue desc 
limit 1;

-- 2) What is the total product revenue, and how does it change month by month?

--A) TOTAL REVENUE
select round(sum(price)::numeric,2)
from olist_order_items;

--B)REVENUE AS MONTH
select to_char(
				date_trunc(
					'month',
						to_timestamp
				(o.order_purchase_timestamp,'yyyy-mm-dd hh24:mi:ss') ),
				'mon yyyy'),
				round(sum(i.price)::numeric,2) as revenue
from olist_orders o
join olist_order_items i
on o.order_id=i.order_id
group by date_trunc(
	'month',
		to_timestamp(o.order_purchase_timestamp,'yyyy-mm-dd hh24:mi:ss')
)
order by date_trunc(
	'month',
		to_timestamp(o.order_purchase_timestamp,'yyyy-mm-dd hh24:mi:ss')
		) ;

-- 3) What is the total freight cost, and which product categories have the highest shipping costs?

--A)  TOTAL FREIGHT VALUE
select round(sum(freight_value)::numeric, 2 )as total_freight_value
from olist_order_items;

--B) HIGHEST FREIGHT VALUE PRODUCT
select p.product_category_name,round(sum(i.freight_value)::numeric, 2) as shipping_value
from olist_products p
	join olist_order_items i
		on i.product_id = p.product_id
group by (p.product_category_name)
order by shipping_value desc
	limit 1;
	
-- 4) What is the average delivery time, and which orders were delivered late?

--A) AVG DELIVERY TIME
SELECT    
       AVG(
    		(
               order_delivered_customer_date -                             
                TO_TIMESTAMP(
            order_purchase_timestamp
			'YYYY-MM-DD HH24:MI:SS')
          ) 
        ) AS avg_delivery_days
FROM olist_orders
WHERE order_purchase_timestamp IS NOT NULL
  AND order_delivered_customer_date IS NOT NULL;

--  B) LATE DELIVERED OREDRS

SELECT
    order_id,
		TO_TIMESTAMP(
        order_estimated_delivery_date,
        'YYYY-MM-DD HH24:MI:SS'
    )::date AS estimated_delivery_date,
        order_delivered_customer_date::date,
                (order_delivered_customer_date::date
            -
            TO_TIMESTAMP(
                order_estimated_delivery_date,
                'YYYY-MM-DD HH24:MI:SS')::date
    ) AS days_late
FROM olist_orders
WHERE order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL
  AND order_delivered_customer_date::date >
      TO_TIMESTAMP(
        order_estimated_delivery_date,
        'YYYY-MM-DD HH24:MI:SS'
      )::date
ORDER BY days_late desc;

-- 5) Which payment methods are most popular, and what is the average number of installments?

--A) POPULAR PAYMENT METHODE
select payment_type,count(payment_value) as  no_of_payments
from olist_order_payments
group by payment_type
order by count(payment_value) desc;

--B) AVG NO. OF INSTALLMENT
select round(avg(payment_installments)::numeric,2) as avg_payment_installments
from olist_order_payments;

-- 6) Which customer cities or states have the highest number of orders?

--A) STATE WISE ORDERS
SELECT c.customer_state,count(DISTINCT o.order_id) as no_of_order
from olist_customers c
join olist_orders o
on c.customer_id = o.customer_id
group by c.customer_state
order by count(o.order_id) desc ;

--B) CITIES WISE ORDERS
SELECT c.customer_city,count(DISTINCT o.order_id) as no_of_order
from olist_customers c
join olist_orders o
on c.customer_id = o.customer_id
group by c.customer_city
order by count(o.order_id) desc ;

-- 7) Which product categories receive the highest average review scores?

SELECT p.product_category_name,round(avg(r.review_score)::numeric,2) as avg_review_score,count(*) as total_reviews
from olist_order_reviews r
join olist_order_items i
on r.order_id=i.order_id
join olist_products p
on p.product_id = i.product_id
group by p.product_category_name
order by avg(r.review_score) desc;

-- 8) Which customer states generate the highest total payment value?

select c.customer_state,round(sum(p.payment_value)::numeric , 2) as total_payment_value
from olist_customers c
join olist_orders o
on o.customer_id= c.customer_id
join olist_order_payments p
on p.order_id = o.order_id
group by c.customer_state
order by total_payment_value desc;

-- 9) Which product categories generate the most revenue?

select p.product_category_name,round(sum(i.price)::numeric,2) as revenue
from olist_order_items i
join olist_products p
on i.product_id = p.product_id
group by p.product_category_name
order by  revenue desc;

-- 10) How do monthly orders, delivered orders, and product sales change over time?

select date_trunc('month',to_timestamp(o.order_purchase_timestamp,'yyyy-mm-dd hh24:mi:ss')) as month,
		count(distinct o.order_id) as total_orders,
		count(distinct o.order_id ) filter(
	where o.order_status = 'delivered')as delivered_order,
round(sum(i.price)::numeric,2) as product_sales
from olist_order_items i
join olist_orders o
on i.order_id = o.order_id
group by date_trunc('month',to_timestamp(o.order_purchase_timestamp,'yyyy-mm-dd hh24:mi:ss'))
order by month;
		
