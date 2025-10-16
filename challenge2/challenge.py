import datetime


right_now = datetime.datetime.now()
print(f"Current Date and Time: {right_now}")

print(f"Year: {right_now.year}")
print(f"Month: {right_now.month}")
print(f"Day: {right_now.day}")
print(f"Hour: {right_now.hour}")
print(f"Minute: {right_now.minute}")
print(f"Second: {right_now.second}")
print(f"Microsecond: {right_now.microsecond}")


days_difference = datetime.timedelta(days=100)
next_hundred = right_now + days_difference
previous_hundred = right_now - days_difference

print("\n Date 100 Days in the Future:", next_hundred)
print(" Date 100 Days in the Past:", previous_hundred)


special_day = datetime.datetime(2024, 9, 1, 8, 0, 0)
formatted_special = special_day.strftime("%Y-%m-%d %H:%M:%S")


filename = "formatted_dates.txt"
with open(filename, "w") as file_out:
    file_out.write(f"Special Date: {formatted_special}")

print(f"\n The formatted date has been saved to '{filename}'")
print(f"Date Written: {formatted_special}")
