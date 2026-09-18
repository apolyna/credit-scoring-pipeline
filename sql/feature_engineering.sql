WITH client_base AS (
    SELECT 
        client_id,
        SeriousDlqin2yrs AS target,
        age,
        COALESCE(MonthlyIncome, 0) AS monthly_income,
        COALESCE(NumberOfDependents, 0) AS dependents,
        DebtRatio AS debt_ratio,
        RevolvingUtilizationOfUnsecuredLines AS credit_utilization,
        
        (NumberOfTime30_59DaysPastDueNotWorse + 
         NumberOfTime60_89DaysPastDueNotWorse + 
         NumberOfTimes90DaysLate) AS total_past_due_events,
         
        CASE 
            WHEN NumberOfTimes90DaysLate > 0 THEN 1 
            ELSE 0 
        END AS has_severe_default,
        
        (NumberOfOpenCreditLinesAndLoans + NumberRealEstateLoansOrLines) AS total_credit_lines,

        CASE 
            WHEN age < 30 THEN 'Under 30'
            WHEN age BETWEEN 30 AND 50 THEN '30-50'
            ELSE 'Over 50'
        END AS age_group

    FROM raw_clients
)

SELECT 
    c.client_id,
    c.target,
    c.age,
    c.monthly_income,
    c.dependents,
    c.debt_ratio,
    c.credit_utilization,
    c.total_past_due_events,
    c.has_severe_default,
    c.total_credit_lines,
    c.age_group,
    
    --Оконная функция 1: Средний доход по возрастной группе
    AVG(c.monthly_income) OVER (
        PARTITION BY c.age_group
    ) AS avg_income_by_age_group,

    --Оконная функция 2: Среднее использование кредита по числу иждивенцев
    AVG(c.credit_utilization) OVER (
        PARTITION BY c.dependents
    ) AS avg_utilization_by_dependents

FROM client_base c;