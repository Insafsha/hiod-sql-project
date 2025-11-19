-- Схема БД туристической компании

DROP TABLE IF EXISTS discounts;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS tours;
DROP TABLE IF EXISTS clients;

-- Таблица клиентов
CREATE TABLE clients (
    client_id      SERIAL PRIMARY KEY,
    full_name      VARCHAR(255) NOT NULL,
    email          VARCHAR(255) NOT NULL,
    phone          VARCHAR(50)  NOT NULL,
    is_regular     BOOLEAN      NOT NULL DEFAULT FALSE,
    is_blacklisted BOOLEAN      NOT NULL DEFAULT FALSE
);

-- Таблица туров
CREATE TABLE tours (
    tour_id       SERIAL PRIMARY KEY,
    country       VARCHAR(100) NOT NULL,
    region        VARCHAR(100) NOT NULL,
    hotel_name    VARCHAR(255) NOT NULL,
    tour_type     VARCHAR(50)  NOT NULL,
    duration_days INTEGER      NOT NULL,
    price         INTEGER      NOT NULL
);

-- Таблица заказов
CREATE TABLE orders (
    order_id   SERIAL PRIMARY KEY,
    client_id  INTEGER     NOT NULL REFERENCES clients(client_id),
    tour_id    INTEGER     NOT NULL REFERENCES tours(tour_id),
    order_date DATE        NOT NULL,
    status     VARCHAR(50) NOT NULL,
    total_cost INTEGER     NOT NULL
);

-- Таблица скидок
CREATE TABLE discounts (
    discount_id SERIAL PRIMARY KEY,
    client_id   INTEGER      NOT NULL REFERENCES clients(client_id),
    percentage  INTEGER      NOT NULL,
    reason      VARCHAR(100)
);

-- Индексы для ускорения аналитики

CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_order_date ON orders(order_date);
CREATE INDEX idx_clients_regular_blacklist
    ON clients(is_regular, is_blacklisted);
CREATE INDEX idx_discounts_client_id ON discounts(client_id);
CREATE INDEX idx_tours_country_type ON tours(country, tour_type);
