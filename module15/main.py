import pandas as pd
import plotly.express as px

file_path = "temperature_data.csv"
df = pd.read_csv(file_path, parse_dates=['Date'])

if 'Date' not in df.columns or 'Temperature' not in df.columns:
    raise ValueError("CSV must contain 'Date' and 'Temperature' columns")

avg_temp = df['Temperature'].mean()
print("Temperature Overview")
print(f"Average Temperature (Overall): {avg_temp:.2f}°C\n")

df['Month'] = df['Date'].dt.month_name()

monthly_avg = (
    df.groupby('Month')['Temperature']
    .mean()
    .reindex([
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
)

print(" Average Temperature per Month:")
print(monthly_avg.round(2), "\n")

fig_monthly = px.bar(
    monthly_avg,
    x=monthly_avg.index,
    y=monthly_avg.values,
    title="Average Monthly Temperature",
    labels={'x': 'Month', 'y': 'Temperature (°C)'},
    color=monthly_avg.values,
    color_continuous_scale='Blues'
)
fig_monthly.show()

hottest = df.loc[df['Temperature'].idxmax()]
coldest = df.loc[df['Temperature'].idxmin()]

print("Hottest and Coldest Days:")
print(f"Hottest Day: {hottest['Date'].strftime('%Y-%m-%d')} ({hottest['Temperature']}°C)")
print(f"Coldest Day: {coldest['Date'].strftime('%Y-%m-%d')} ({coldest['Temperature']}°C)\n")

fig_trend = px.line(
    df,
    x='Date',
    y='Temperature',
    title="Temperature Over Time",
    labels={'Date': 'Date', 'Temperature': 'Temperature (°C)'},
    line_shape='spline'
)
fig_trend.show()


def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

df['Season'] = df['Date'].dt.month.apply(get_season)
seasonal_avg = df.groupby('Season')['Temperature'].mean().reindex(['Winter', 'Spring', 'Summer', 'Autumn'])

print("️ Average Temperature per Season:")
print(seasonal_avg.round(2), "\n")


fig_seasonal = px.bar(
    seasonal_avg,
    x=seasonal_avg.index,
    y=seasonal_avg.values,
    title="Seasonal Average Temperature",
    labels={'x': 'Season', 'y': 'Temperature (°C)'},
    color=seasonal_avg.values,
    color_continuous_scale='Oranges'
)
fig_seasonal.show()
