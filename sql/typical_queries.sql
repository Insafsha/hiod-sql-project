-- 1. Количество заказов по статусам

SELECT status, COUNT(*) AS count FROM orders GROUP BY status;

-- 2. Средняя стоимость туров по типу

SELECT tour_type, AVG(price)::int AS avg_price FROM tours GROUP BY tour_type;

-- 3. Топ-5 клиентов по количеству заказов

SELECT c.full_name, COUNT(o.order_id) AS order_count
       FROM clients c
       JOIN orders o ON c.client_id = o.client_id
       GROUP BY c.full_name
       ORDER BY order_count DESC
       LIMIT 5;

-- 4. Количество туров в каждой стране

SELECT country, COUNT(*) AS tour_count FROM tours GROUP BY country ORDER BY tour_count DESC;

-- 5. Самые дорогие туры (ТОП-5)

SELECT country, region, hotel_name, price FROM tours ORDER BY price DESC LIMIT 5;

-- 6. Заказы клиентов с чёрного списка

SELECT o.order_id, c.full_name, o.status
       FROM orders o
       JOIN clients c ON o.client_id = c.client_id
       WHERE c.is_blacklisted = TRUE;

-- 7. Клиенты со скидками

SELECT c.full_name, d.percentage, d.reason
       FROM discounts d
       JOIN clients c ON d.client_id = c.client_id;

-- 8. Средняя длительность туров по типу

SELECT tour_type, AVG(duration_days)::int AS avg_days FROM tours GROUP BY tour_type;

-- 9. Количество заказов по месяцам

SELECT TO_CHAR(order_date, 'YYYY-MM') AS month, COUNT(*) AS order_count
       FROM orders
       GROUP BY month
       ORDER BY month;

-- 10. Топ-5 самых дорогих заказов

SELECT o.order_id, c.full_name, o.total_cost
       FROM orders o
       JOIN clients c ON o.client_id = c.client_id
       ORDER BY total_cost DESC
       LIMIT 5;