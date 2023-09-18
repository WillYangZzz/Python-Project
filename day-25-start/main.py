import csv
import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
#
# data["temp"].mean()
# max_temp = data["temp"].max()
# data[data.temp == max_temp]
#
# monday = data[data.day == "Monday"]

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
