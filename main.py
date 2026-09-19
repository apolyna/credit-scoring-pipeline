from src.data import load_data_from_db, prepare_data
from src.train import train_model
from src.evaluate import evaluate_and_save_reports

def main():
    print("Запуск ML Пайплайна Кредитного Скоринга ")
    
    # 1. Загрузка витрины из SQLite
    print("Загрузка данных из SQLite")
    df = load_data_from_db()
    
    # 2. Подготовка и разбиение выборки
    print(" Подготовка и разбиение выборки")
    X_train, X_test, y_train, y_test = prepare_data(df)
    
    # 3. Обучение модели и сохранение весов
    model = train_model(X_train, y_train, X_test, y_test)
    
    # 4. Оценка качества и сохранение графиков
    evaluate_and_save_reports(model, X_test, y_test)
    
    print("\nПайплайн успешно выполнен!")

if __name__ == "__main__":
    main()