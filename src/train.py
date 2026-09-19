from catboost import CatBoostClassifier
from src.config import MODEL_PARAMS, CAT_FEATURES, MODEL_SAVE_PATH

def train_model(X_train, y_train, X_test, y_test) -> CatBoostClassifier:
    """Инициализирует, обучает и сохраняет модель CatBoost."""
    model = CatBoostClassifier(
        **MODEL_PARAMS,
        cat_features=CAT_FEATURES
    )
    
    print("Начинаем обучение CatBoost")
    model.fit(
        X_train, y_train,
        eval_set=(X_test, y_test),
        early_stopping_rounds=50,
        use_best_model=True
    )
    
    # Сохраняем обученную модель
    MODEL_SAVE_PATH.parent.mkdir(parents=True, exist_ok=True)
    model.save_model(str(MODEL_SAVE_PATH))
    print(f"Модель успешно сохранена в: {MODEL_SAVE_PATH}")
    
    return model