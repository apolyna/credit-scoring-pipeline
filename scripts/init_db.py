import os
import pandas as pd
import sqlite3

CSV_PATH = os.path.join("data", "cs-training.csv")
DB_PATH = "credit_scoring.db"


def init_database():
    if not os.path.exists(CSV_PATH):
        print(f"Ошибка: Файл {CSV_PATH} не найден!")
        print("Пожалуйста, скачайте cs-training.csv и положите его в папку data/")
        return

    print("Чтение CSV файла...")
    df = pd.read_csv(CSV_PATH, index_col=0)
    
    # Нормализуем названия колонок для удобства в SQL
    df.columns = [c.replace("-", "_").replace(".", "_") for c in df.columns]

    print(f"Загружено записей: {len(df)}")

    conn = sqlite3.connect(DB_PATH)
    print("Сохранение данных в SQLite базу (таблица raw_clients)...")
    df.to_sql("raw_clients", conn, if_exists="replace", index_label="client_id")
    conn.close()
    print(f"База данных успешно создана: {DB_PATH}")


if __name__ == "__main__":
    init_database()