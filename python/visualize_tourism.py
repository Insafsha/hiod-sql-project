import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns

"""
Визуализация ключевых метрик туристической компании на основе PostgreSQL.

Графики:
1. Количество заказов по месяцам.
2. Средняя стоимость туров по типу.
3. Количество туров по странам.
4. Распределение стоимости заказов.
"""

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "tourism_db",
    "user": "your_user",
    "password": "your_password",
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def fetch_dataframe(sql: str) -> pd.DataFrame:
    with get_connection() as conn:
        df = pd.read_sql(sql, conn)
    return df

def plot_orders_by_month():
    sql = """
        SELECT TO_CHAR(order_date, 'YYYY-MM') AS month,
               COUNT(*) AS order_count
        FROM orders
        GROUP BY month
        ORDER BY month;
    """
    df = fetch_dataframe(sql)
    plt.figure()
    sns.barplot(x="month", y="order_count", data=df)
    plt.xticks(rotation=45)
    plt.title("Количество заказов по месяцам")
    plt.tight_layout()
    plt.savefig("../plots/orders_by_month.png", bbox_inches="tight")

def plot_avg_price_by_tour_type():
    sql = """
        SELECT tour_type,
               AVG(price)::int AS avg_price
        FROM tours
        GROUP BY tour_type
        ORDER BY avg_price DESC;
    """
    df = fetch_dataframe(sql)
    plt.figure()
    sns.barplot(x="tour_type", y="avg_price", data=df)
    plt.xticks(rotation=45)
    plt.title("Средняя стоимость туров по типу")
    plt.tight_layout()
    plt.savefig("../plots/avg_price_by_tour_type.png", bbox_inches="tight")

def plot_tours_by_country():
    sql = """
        SELECT country,
               COUNT(*) AS tour_count
        FROM tours
        GROUP BY country
        ORDER BY tour_count DESC;
    """
    df = fetch_dataframe(sql)
    plt.figure()
    sns.barplot(x="country", y="tour_count", data=df)
    plt.xticks(rotation=45)
    plt.title("Количество туров по странам")
    plt.tight_layout()
    plt.savefig("../plots/tours_by_country.png", bbox_inches="tight")

def plot_total_cost_distribution():
    sql = """
        SELECT total_cost
        FROM orders;
    """
    df = fetch_dataframe(sql)
    plt.figure()
    sns.histplot(df["total_cost"], bins=20, kde=True)
    plt.title("Распределение стоимости заказов")
    plt.tight_layout()
    plt.savefig("../plots/total_cost_distribution.png", bbox_inches="tight")

def main():
    plot_orders_by_month()
    plot_avg_price_by_tour_type()
    plot_tours_by_country()
    plot_total_cost_distribution()
    print("Графики сохранены в папку plots/")

if __name__ == "__main__":
    main()