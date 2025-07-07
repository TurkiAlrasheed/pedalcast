# 🚲 PedalCast: Forecasting Daily Bluebikes Usage

**Goal**  
Predict daily bike demand at each Bluebikes station in Boston using weather conditions, calendar context, and recent usage patterns.

---

### 📅 Data Sources
- **[Bluebikes Trip Data](https://s3.amazonaws.com/hubway-data/index.html)**  
  I gathered data from July 2023 through June 2025.
  
- **[Visual Crossing Historical Weather](https://www.visualcrossing.com/weather-data)**  
  Daily Boston weather from July 2023 to June 2025, including temperature, precipitation, humidity, windspeed, and visibility.

---

### ⚙️ Methods
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


### 📈 Results
- **Test RMSE**: **9.29 trips/day**
- **R² Score**: **0.0.9223**
- **Usage history (lag features)** was the strongest predictor of future demand, with the 7-day rolling average (`rolling_7`) contributing the most to the model’s performance.
---
