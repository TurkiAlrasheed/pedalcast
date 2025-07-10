import holidays

def create_features(df):
    out = df.copy()
    
    out['dayofweek'] = out['date'].dt.dayofweek
    out['is_weekend'] = out['dayofweek'] >= 5
    out['quarter'] = out['date'].dt.quarter 
    out['year'] = out['date'].dt.year 
    out['month'] = out['date'].dt.month 
    out['dayofyear'] = out['date'].dt.dayofyear 
    out['dayofmonth'] = out['date'].dt.day 
    out['weekofyear'] = out['date'].dt.isocalendar().week 

    def assign_season(month):
        if month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        elif month in [9, 10, 11]:
            return 'Fall'
        else:
            return 'Winter'

    out['season'] = out['month'].apply(assign_season)
    
    out = out.sort_values(['start_station_id', 'date'])
    out['lag_1'] = out.groupby('start_station_id')['trip_count'].shift(1)
    out['lag_7'] = out.groupby('start_station_id')['trip_count'].shift(7)
    
    out['rolling_7'] = (
        out.groupby('start_station_id')['trip_count']
           .shift(1)
           .rolling(window=7)
           .mean()
           .reset_index(level=0, drop=True)
    )

    us_holidays = holidays.UnitedStates()
    out['is_holiday'] = out['date'].isin(us_holidays)
    
    return out