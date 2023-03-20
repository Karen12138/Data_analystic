# -*- coding: utf-8 -*-
import itertools
import pandas as pd
import pyecharts
from pyecharts.charts import Pie
from pyecharts import options as opts

data = pd.read_csv('pub_sports_place.csv', encoding="gbk")
list_name1 = []
list_name2 = []
new_list = []
list_name1 = list(data.loc[:, "districtName"])
df = pd.DataFrame(list_name1, columns=["districtName"])

index = df["districtName"].notnull()
df = df[index]
# print(df)

###统计去除重复项的内容
for i in list_name1:
    if i not in list_name2:
        list_name2.append(i)
# print(list_name2)

####统计词频
count_times_dict = {}
for i in list_name1:
    if list_name1.count(i) > 1:
        count_times_dict[i] = list_name1.count(i)
# print(count_times_dict)

##字典排序
count_times_list=sorted(count_times_dict.items(),key=lambda x:x[1],reverse=True)
count_times_dict = {}
for i ,j  in count_times_list:
    count_times_dict[i] = j
print(count_times_dict)


list_districts=[]
list_numbers=[]
for i, j in count_times_dict.items():
    list_districts.append(i)
    list_numbers.append(j)
# print(list_districts,list_numbers)

dist_df=pd.DataFrame(list(count_times_dict.items()),columns=['Districts', 'Numbers'])
print(dist_df)


c = (
    Pie()
    .add("", [list(z) for z in zip(list_districts,list_numbers)])
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_set_color.html")
)