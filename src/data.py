import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import DB_PATH, SQL_QUERY_PATH, TARGET_COL, DROP_COLS, TEST_SIZE, RANDOM_STATE

def load_data_from_db() -> pd.DataFrame:
    """Выполняет SQL-скрипт и загружает витрину данных."""
    with open(SQL_QUERY_PATH, "r", encoding="utf-8") as file:
        query = file.read()
    
    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(query, conn)
    return df

def prepare_data(df: pd.DataFrame):
    """Разделяет данные на X, y и создает обучающую и тестовую выборки."""
    X = df.drop(columns=DROP_COLS)
    y = df[TARGET_COL]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    return X_train, X_test, y_train, y_test