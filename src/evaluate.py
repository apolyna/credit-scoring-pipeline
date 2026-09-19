import matplotlib.pyplot as plt
import shap
from sklearn.metrics import roc_auc_score, roc_curve
from src.config import FIGURES_DIR

def evaluate_and_save_reports(model, X_test, y_test):
    """Рассчитывает метрики, сохраняет ROC-кривую и SHAP-график."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Расчет вероятностей и ROC-AUC
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    auc_score = roc_auc_score(y_test, y_pred_proba)
    print(f"\nИтоговый ROC-AUC на тестовой выборке: {auc_score:.4f}")
    
    # 2. Построение и сохранение ROC-кривой
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    plt.figure(figsize=(7, 5))
    plt.plot(fpr, tpr, label=f"CatBoost (AUC = {auc_score:.4f})", color="darkorange", lw=2)
    plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC-кривая скоринговой модели")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    roc_path = FIGURES_DIR / "roc_curve.png"
    plt.savefig(roc_path, bbox_inches="tight", dpi=300)
    plt.close()
    print(f" ROC-кривая сохранена в: {roc_path}")
    
    # 3. Расчет и сохранение SHAP summary plot
    print("Расчет SHAP-значений")
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(X_test)
    
    plt.figure(figsize=(10, 6))
    shap.summary_plot(shap_values, X_test, max_display=12, show=False)
    
    shap_path = FIGURES_DIR / "shap_summary.png"
    plt.savefig(shap_path, bbox_inches="tight", dpi=300)
    plt.close()
    print(f" SHAP-график сохранен в: {shap_path}")