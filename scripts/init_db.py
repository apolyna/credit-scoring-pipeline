from pathlib import Path
import pandas as pd
import sqlite3

# Автоматически определяем корень проекта и правильные пути
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "cs-training.csv"
DB_PATH = BASE_DIR / "data" / "credit_scoring.db"


def init_database():
    if not CSV_PATH.exists():
        print(f"Ошибка: Файл {CSV_PATH} не найден!")
        print("Пожалуйста, скачайте cs-training.csv и положите его в папку data/")
        return

    print("Чтение CSV файла")
    df = pd.read_csv(CSV_PATH, index_col=0)
    
    # Нормализуем названия колонок для удобства в SQL
    df.columns = [c.replace("-", "_").replace(".", "_") for c in df.columns]

    print(f"Загружено записей: {len(df)}")

    # Убеждаемся, что папка data/ существует
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    print("Сохранение данных в SQLite базу (таблица raw_clients)")
    df.to_sql("raw_clients", conn, if_exists="replace", index_label="client_id")
    conn.close()
    print(f" База данных успешно создана по пути: {DB_PATH}")


if __name__ == "__main__":
    init_database()