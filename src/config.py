from pathlib import Path

# Корневая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Пути к данным и ресурсам
DB_PATH = BASE_DIR / "data" / "credit_scoring.db"
SQL_QUERY_PATH = BASE_DIR / "sql" / "feature_engineering.sql"
MODEL_SAVE_PATH = BASE_DIR / "models" / "catboost_model.cbm"
FIGURES_DIR = BASE_DIR / "reports" / "figures"

# Конфигурация признаков
TARGET_COL = "target"
DROP_COLS = ["client_id", TARGET_COL]
CAT_FEATURES = ["age_group"]

# Параметры модели
MODEL_PARAMS = {
    "iterations": 500,
    "learning_rate": 0.05,
    "depth": 6,
    "eval_metric": "AUC",
    "random_seed": 42,
    "verbose": 100
}

# Параметры разделения выборки
TEST_SIZE = 0.2
RANDOM_STATE = 42