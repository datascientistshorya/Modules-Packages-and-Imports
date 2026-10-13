def convert_celsius_to_fahrenheit(celsius):
     return (celsius * 9/5) + 32


def calculate_average_temperature(temperatures):
    return sum(temperatures)/len(temperatures)

def find_hottest_day(temperatures):
    return max(temperatures)