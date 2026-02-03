import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename_1 = "../../data/death_valley_2014.csv"
filename_2 = "../../data/sitka_weather_2014.csv"
filename_3 = "../../data/ShanghaiWeatherHistory.csv"


def read_temps(
    filename, date_index, high_index, low_index, date_format, strip_br=False
):
    with open(filename) as f:
        reader = csv.reader(f)

        dates, highs, lows = [], [], []
        for row in reader:
            if strip_br:
                row = [cell.replace("<br />", "").strip() for cell in row]
            try:
                current_date = datetime.strptime(row[date_index], date_format)
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {row[date_index]}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows


dates_1, highs_1, lows_1 = read_temps(
    filename_1,
    date_index=0,
    high_index=1,
    low_index=3,
    date_format="%Y-%m-%d",
)
dates_2, highs_2, lows_2 = read_temps(
    filename_2,
    date_index=0,
    high_index=1,
    low_index=3,
    date_format="%Y-%m-%d",
)
dates_3, highs_3, lows_3 = read_temps(
    filename_3,
    date_index=0,
    high_index=1,
    low_index=3,
    date_format="%Y-%m-%d",
    strip_br=True,
)

# Plot the first two files in one chart for comparison
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_1, highs_1, c="red", alpha=0.5, label="Death Valley highs")
plt.plot(dates_1, lows_1, c="blue", alpha=0.5, label="Death Valley lows")
plt.plot(dates_2, highs_2, c="orange", alpha=0.5, label="Sitka highs")
plt.plot(dates_2, lows_2, c="green", alpha=0.5, label="Sitka lows")
plt.fill_between(dates_1, highs_1, lows_1, facecolor="red", alpha=0.05)
plt.fill_between(dates_2, highs_2, lows_2, facecolor="green", alpha=0.05)

plt.title("Daily high and low temperatures - 2014\nDeath Valley vs Sitka", fontsize=24)
fig.autofmt_xdate()  # Rotate date labels automatically
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.legend()
plt.show()

# Plot the third file in its own chart
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_3, highs_3, c="red", alpha=0.5)
plt.plot(dates_3, lows_3, c="blue", alpha=0.5)
plt.fill_between(dates_3, highs_3, lows_3, facecolor="blue", alpha=0.1)

plt.title("Daily high and low temperatures\nShanghai", fontsize=24)
fig.autofmt_xdate()  # Rotate date labels automatically
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
