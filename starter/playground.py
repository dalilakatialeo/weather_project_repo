from datetime import datetime

# # iso_string = '2021-07-02T07:00:00+08:00'

# # date_object = datetime.strptime(iso_string,'%Y-%m-%dT%H:%M:%S%z')
# # new_date = datetime.strftime(date_object, '%A %d %B %Y')

# # print(new_date)

# # # def convert_f_to_c(temp_in_farenheit):
# # #     """Converts an temperature from farenheit to celcius.

# # # #     Args:
# # # #         temp_in_farenheit: float representing a temperature.
# # # #     Returns:
# # # #         A float representing a temperature in degrees celcius, rounded to 1dp.
# # # #     """
# # # #     temp_in_celsius = ((temp_in_farenheit) - 32) * (5/9)
# # # #     return f"{temp_in_celsius:.1f}"

# # # # print(convert_f_to_c(21))

# # numbers = ["1","2","3"]

# # def calculate_mean(weather_data):
# #     """Calculates the mean value from a list of numbers.

# #     Args:
# #         weather_data: a list of numbers.
# #     Returns:
# #         A float representing the mean value.
# #     """
# #     weather_data = [int(i) for i in weather_data]

# #     return sum(weather_data) / len(weather_data)

# # print(calculate_mean(numbers))

# # # def list_mean(list):
# # #     return sum(list) / len(list)
# # # print(list_mean([10,5,6]))
# # #     return sum(weather_data) / len(weather_data)

# # weather_data = [49, 57, 56, 55, 53]
# # # def find_min(weather_data):
# #   """Calculates the minimum value in a list of numbers.

# #     Args:
# #         weather_data: A list of numbers.
# #     Returns:
# #         The minium value and it's position in the list.
# #     """
#     # if len(weather_data) == 0:
#     #     return ()
#     # counter = float(weather_data[0])
#     # min_weather = 0
#     # for index,weather in enumerate(weather_data):
#     #     if float(weather) <= counter:
#     #         min_weather = index
#     #         counter = float(weather)
#     # return counter,min_weather
# # weather_data = [49, 57, 56, 55, 53]
# # def find_min(weather_data):
# #     if weather_data == []:
# #         return ()
# #     else:
# #         min_num = weather_data[0]
# #         for number in weather_data:
# #             if number <= min_num:
# #                 min_num = number
# #             return min_num, weather_data[min_num]

# # print(find_min(weather_data))

# # numbers = [6,3,8,1]
# # min_num = numbers[0]
# # min_index = 0

# # if len(numbers) == 0:
# #     print()
# # else:
# #     for index, n in enumerate(numbers):
# #         if n <= min_num:
# #             min_num = n
# #             min_index = index
# #     print(min_num, min_index)

# # 5 Day Overview
# #   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
# #   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
# #   The average low this week is 12.2°C.
# #   The average high this week is 17.8°C.
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

# list_of_lists = [
#     ["a", 6, 2], #date as string, min as int, max as int
#     ["b", 3, 4],
#     ["c", 5, 6],
#     ["d", 7, 8],
#     ["e", 1, 10]
# ]

# if list_of_lists == []:
#     print ()

# else:
# #set min number as first encountered
#     min_num_list = []
#     min_num = float(list_of_lists[0][1])
#     max_num = float(list_of_lists[0][2])
#     min_index = 0
#     max_index = 0
#     for index, row in enumerate(list_of_lists): #iterate over the sublists
#        min_num_list.append(row[1])
#     print(find_min(min_num_list))

#     min_temp, min_pos = find_min(min_num_list)
# # print(min_num_list)
#     #    if row: #provided that they are a list
#     #         for n in row: #for each value in the sublist
#     #             # if n != row[0]: #provided that it is not the string at index 0
#     #                 if n <= min_num: #if the value is less than or equal to min
#     #                     min_num = n #new min will be that value
#     #                     min_index = index
#     print(f"The lowest temperature will be {min_temp}, and will occur on {min_pos}")

    #                 if i >= max_num:
    #                     max_num = i
    #                     max_index = index
    # print(f"The highest temperature will be {max_num}, and will occur on {list_of_lists[max_index][0]}")

    # list_of_lists = [float(x) for x in list_of_lists]

    # return sum(weather_data) / len(weather_data)

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

# def generate_summary(weather_data):
"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
#     """
# min_list = []
# max_list = []

# weather_data = [
#         ["2021-07-02T07:00:00+08:00",49,67],
#         ["2021-07-03T07:00:00+08:00",57,68],
#         ["2021-07-04T07:00:00+08:00",56,62],
#         ["2021-07-05T07:00:00+08:00",55,61],
#         ["2021-07-06T07:00:00+08:00",53,62]
# ]

# if weather_data == []:
#     print ()

# else:
#     for day in weather_data:
#         min_list.append(day[1])
#         max_list.append(day[2])
# min_temp, min_pos= (find_min(min_list))
# max_temp, max_pos= (find_max(max_list))

# min_date = weather_data[min_pos][0]
# max_date = weather_data[max_pos][0]   
# min_conv_date = convert_date(min_date)
# max_conv_date = convert_date(max_date)
# min_celsius = convert_f_to_c(min_temp)
# max_celsius = convert_f_to_c(max_temp)
# avg_min = calculate_mean(min_list)
# avg_max = calculate_mean(max_list)
# avg_min_celsius = convert_f_to_c(avg_min)
# avg_max_celsius = convert_f_to_c(avg_max)


# print (f"{len(weather_data)} Day Overview")
# print (f"The lowest temperature will be {min_celsius}°C, and will occur on {min_conv_date}.")
# print (f"The highest temperature will be {max_celsius}°C, and will occur on {max_conv_date}.")
# print (f"The average low this week is {avg_min_celsius}°C.")
# print (f"The average high this week is {avg_max_celsius}°C.")

# 5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.


# print (f"The lowest temperature will be {min_temp}, and will occur on {min_pos}")
# The average low this week is 12.2°C.
# ---- Friday 02 July 2021 ----
#   Minimum Temperature: 9.4°C
#   Maximum Temperature: 19.4°C


weather_data = [
        ["2021-07-02T07:00:00+08:00",49,67],
        ["2021-07-03T07:00:00+08:00",57,68],
        ["2021-07-04T07:00:00+08:00",56,62],
        ["2021-07-05T07:00:00+08:00",55,61],
        ["2021-07-06T07:00:00+08:00",53,62]
]
# print(weather_data)

new_weather_data = [
    ['Friday 02 July 2021', 9.4, 19.4],
    ['Saturday 03 July 2021', 13.9, 20.0],
    ['Sunday 04 July 2021', 13.3, 16.7],
    ['Monday 05 July 2021', 12.8, 16.1],
    ['Tuesday 06 July 2021', 11.7, 16.7],
]


if weather_data == []:
    print () #print --> return
else:
    for day in weather_data:
        date = convert_date(day[0])
        daily_min = convert_f_to_c(day[1])
        daily_max = convert_f_to_c(day[2])
        # new_weather_data.extend([date, daily_min, daily_max])
        new_weather_data.append([date, daily_min, daily_max])

# print(new_weather_data)  #only shows the last!

# ['Friday 02 July 2021', 9.4, 19.4]
# ['Saturday 03 July 2021', 13.9, 20.0]
# ['Sunday 04 July 2021', 13.3, 16.7]
# ['Monday 05 July 2021', 12.8, 16.1]
# ['Tuesday 06 July 2021', 11.7, 16.7]

# new_weather_data = [
#     ['Friday 02 July 2021', 9.4, 19.4]
#     ['Saturday 03 July 2021', 13.9, 20.0]
#     ['Sunday 04 July 2021', 13.3, 16.7]
#     ['Monday 05 July 2021', 12.8, 16.1]
#     ['Tuesday 06 July 2021', 11.7, 16.7]
# ]


for row in new_weather_data:
    print (f"---- {row[0]} ----")    
    print(f"  Minimum Temperature: {row[1]}°C")
    print(f"  Maximum Temperature: {row[2]}°C")
    print(f"\n")
