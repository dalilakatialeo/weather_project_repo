import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp): #done
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}" 



def convert_date(iso_string): #done
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_object = datetime.strptime(iso_string,'%Y-%m-%dT%H:%M:%S%z')
    new_date = datetime.strftime(date_object, '%A %d %B %Y')

    return new_date

def convert_f_to_c(temp_in_farenheit): #done
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celsius = (float(temp_in_farenheit) - 32) * (5/9)

    return float(f"{temp_in_celsius:.1f}")


def calculate_mean(weather_data): #done
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data = [float(i) for i in weather_data]

    return sum(weather_data) / len(weather_data)


def load_data_from_csv(csv_file): #done
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    rows = []
    with open (csv_file) as grid:
        data_list = list(csv.reader(grid))
        data_list.pop(0)
        for row in data_list:
            if row:
                rows.append([row[0], int(row[1]), int(row[2])])

    return rows

def find_min(weather_data): #done
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data == []:
        return ()
    min_num = float(weather_data[0])
    min_index = 0
    for index, n in enumerate(weather_data):
        if float(n) <= min_num:
            min_num = float(n)
            min_index = index

    return min_num, min_index

def find_max(weather_data): #done
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return ()
    max_num = float(weather_data[0])
    max_index = 0
    for index, n in enumerate(weather_data):
        if float(n) >= max_num:
            max_num = float(n)
            max_index = index

    return max_num, max_index

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
        print(f"The lowest temperature will be {min_temp}, and will occur on {min_pos}")
    """
    min_list = []
    max_list = []

    if weather_data == []:
        return ("")
    else:
        for day in weather_data:
            min_list.append(day[1])
            max_list.append(day[2])
    min_temp, min_pos= (find_min(min_list))
    max_temp, max_pos= (find_max(max_list))

    min_date = weather_data[min_pos][0]
    max_date = weather_data[max_pos][0]   
    min_conv_date = convert_date(min_date)
    max_conv_date = convert_date(max_date)
    min_celsius = convert_f_to_c(min_temp)
    max_celsius = convert_f_to_c(max_temp)
    avg_min = calculate_mean(min_list)
    avg_max = calculate_mean(max_list)
    avg_min_celsius = convert_f_to_c(avg_min)
    avg_max_celsius = convert_f_to_c(avg_max)\
    
    summary = (f"{len(weather_data)} Day Overview\n")
    summary += (f"  The lowest temperature will be {min_celsius}°C, and will occur on {min_conv_date}.\n")
    summary += (f"  The highest temperature will be {max_celsius}°C, and will occur on {max_conv_date}.\n")
    summary += (f"  The average low this week is {avg_min_celsius}°C.\n")
    summary += (f"  The average high this week is {avg_max_celsius}°C.\n")

    return summary


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    new_weather_data = []
    if weather_data == []:
        return ("")
    else:
        for day in weather_data:
            date = convert_date(day[0])
            daily_min = convert_f_to_c(day[1])
            daily_max = convert_f_to_c(day[2])
            new_weather_data.append([date, daily_min, daily_max])
    # print(new_weather_data)
    daily_summary = ""
    for row in new_weather_data:
        summary = f"---- {row[0]} ----\n  Minimum Temperature: {row[1]}°C\n  Maximum Temperature: {row[2]}°C\n\n"
        daily_summary += summary 
    return daily_summary
        

# for row in new_weather_data:
#     print (f"---- {row[0]} ----")    
#     print(f"  Minimum Temperature: {row[1]}°C")
#     print(f"  Maximum Temperature: {row[2]}°C")
#     print(f"\n")
