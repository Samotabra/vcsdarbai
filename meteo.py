# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from matplotlib import pyplot as plt
#
# # define website
# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"
#
# #response from the website
# response = requests.get(url) #pasiima visa info is url
#
# #create a bs4(beautifulsoup) object (musu objektas) to parde (analizuoti) the HTML content
# soup = BeautifulSoup(response.content, 'html.parser')   # soup, kad galetum pasiimti produktu info
#
# #find all weather information in the class content city
# week_days = soup.find_all('span', class_='date')
#
# temperatures = soup.find('span', class_='big up-from-zero')[::2]
#
# night_temp = [temperature.get_text() for temperature in temperatures]
#
# week_day = [day.get_text() for day in week_days]
#
# temp_list = []
# for temperature in temperatures:
#     temp_text = temperature.get_text().replace('C', '')
#     temp_values = int(temp_text[:-1])
#     temp_list.append(temp_values)
#
# min_length = min(len(week_day), len(temp_list))
#
# reorder_weekdays = week_day[:min_length]
#
# reorder_temperature = temp_list[:min_length]
#
# week_day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print(reorder_temperature)


# #temp_values = night_temp

# # for weekdays in week_day_order:
# #     for weekday, temperature in zip(seven_days, temperatures_days):
# #         if weekdays in weekday:
# #             reorder_weekdays.append(weekday)
# #             reorder_temperatures.append(week_temp_order[week_day_order.index(weekdays)])
# #             break
# #
# data = {
#     'weekday': reorder_weekdays,
#     'temperature': reorder_temperature
# }
#
# df = pd.DataFrame(data)
#
# #print(df)
#
# # df_sorted = df.sort_values(by='temperature')
# # plt.bar(df_sorted['weekday'], df_sorted['temperature'])
# # plt.xlabel('savaites diena')
# # plt.ylabel('temperatura')
# # plt.title('Oru prognoze Vilniuje')
# # plt.ylim(0, 25)
# # plt.show()
