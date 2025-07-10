# 🚲 PedalCast: Forecasting Daily Bluebikes Usage

**Goal**  
Predict daily bike demand at each Bluebikes station in Greater Boston using weather conditions, calendar context, and recent usage patterns.

---

### Data Sources
- **[Bluebikes Trip Data](https://s3.amazonaws.com/hubway-data/index.html)**  
  I gathered data from July 2023 through June 2025.
  
- **[Visual Crossing Historical Weather](https://www.visualcrossing.com/weather-data)**  
  Daily Boston weather from July 2023 to June 2025, including temperature, precipitation, humidity, windspeed, and visibility.

---

### Methods
- **Feature Engineering**
  - Lag features: previous day's trips (`lag_1`), weekly cycle (`lag_7`)
  - Rolling 7-day average: `rolling_7`
  - Calendar variables: day of week, weekend flag, season, etc.
  - Weather variables: temperature, precipitation, snow, humidity, visibility
  
- **Model**  
  - `XGBRegressor`
  - Training with `TimeSeriesSplit` cross-validation and Hyperparameter tuning with `GridSearchCV`
  - Preprocessing handled via scikit-learn `Pipeline` and `ColumnTransformer`

---


### Results
- **Test RMSE**: **9.27 trips/day**
- **R² Score**: **0.9228**
- **Usage history** was the strongest predictor of future demand, with the 7-day rolling average (`rolling_7`) contributing the most to the model’s performance.
---

### Forecasting

A recursive forecasting function was implemented to predict bike demand for any future date range. This function:
- Builds a grid of all stations × dates to predict (if stations not specified), taking into account stations that have seasonal inactivitiy (e.g. Nov 14 to Mar 14).
- Uses the trained model to generate forecasts day by day, recursively using prior predictions as inputs to get lag features.

Example usage:
```python
forecast = forecast_bike_demand(
    start_date='2025-07-01',
    end_date='2025-07-07',
    full_data=daily_counts,
    model_pipeline=loaded_model
)
```

To explore the full workflow, follow the notebooks in this order:

1. **`cleaning-eda.ipynb`**  
2. **`modeling.ipynb`**  
3. **`forecasting.ipynb`**  
  

