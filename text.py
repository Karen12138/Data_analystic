import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('451.csv')
# info = data.info()
# print(info)
df = pd.DataFrame()

xdata = []
ydata = []

###获取特定两列值
xdata = list(data.loc[:, 'CH1 Time'])  # 将csv中列名为“列名1”的列存入xdata数组中#如果ix报错请将其改为loc
# xdata = data.iloc[:,num]   num处写要读取的列序号，0为csv文件第一列
ydata = list(data.loc[:, 'CH1 Current'])  # 将csv中列名为“列名2”的列存入ydata数组中
###合并成一个列表
xy_dict = list(zip(xdata, ydata))
xy_df = pd.DataFrame(xy_dict, columns=['CH1 Time', 'CH1 Current'])

###截取有值的行数
#''为你需要检索的一列的名称，index等于创建了一个掩码
index=xy_df['CH1 Time'].notnull()
xy_df=xy_df[index]
print(len(xy_df))
####把CH1 Time这列的值做成一个列表list_x，同理CH1 Current做成list_y
list_x = list(xy_df.loc[:, 'CH1 Time'])
list_y = list(xy_df.loc[:, 'CH1 Current'])
###这两个是存突变位置横坐标的
list_a = []
list_b = []
###这个是存相邻两个横坐标只差
list_result = []
##一个是中间位置的横坐标，一个是中间位置的纵坐标
list_x_average = []
list_y_average = []
###上半部分y的值，下半部分y的值
list_y_up_average = []
list_y_blow_average = []
###最后一个数据的横坐标
list_last_x = []
# 找到数据大小突变的位置
j_sum = 0
for j in list_y:
    j_sum += j
    j_average = j_sum / len(list_y)
print(j_average)

# target = xy_df[xy_df['CH1 Current']<j_average].index.tolist()
# print(target)
####这里是找跳跃点
for i, j in zip(range(len(list_y)), range(len(list_x))):
    try:
        if j == len(list_x) - 1:
            list_last_x.append(list_x[j])
        if list_y[i] < j_average:
            if list_y[i + 1] > j_average:
                print(f"上升第{i}个数据值的横坐标:{list_x[i]}")
                list_b.append(list_x[i])
        else:
            if list_y[j + 1] < j_average:
                print(f"下降第{j}个数据值的横坐标:{list_x[j]}")
                list_a.append(list_x[j])
    except IndexError:
        pass
##list_last_x存的是最后一个横坐标的值
# print("最后一个横坐标的值:",list_last_x)
# print("上升的横坐标：",list_b)
# print("下降的横坐标：",list_a)
###两组跳跃点相加合并成一个新的列表
list_ab = list_b + list_a
new_list_ab = sorted(list_ab)
##打印的是交点坐标的横坐标
print("突变点的横坐标:", new_list_ab)
# print(len(new_list_ab))

#####这里是找相邻跳跃点的中间横坐标
for z in range(len(new_list_ab)):
    # print(z)
    # print(new_list_ab[z] - new_list_ab[z-1])
    ####找相邻跳跃点之差
    # if new_list_ab[z] - new_list_ab[z - 1] > 1:
    #     result_minus = new_list_ab[z] - new_list_ab[z - 1]
    #     list_result.append("%.4f" % result_minus)
    if z == 0:
        x_average = new_list_ab[z] / 2
        list_x_average.append('%.4f' % x_average)
    elif z == len(new_list_ab) - 1:
        list_x_average.append(((list_last_x[0] - new_list_ab[z]) / 2) + new_list_ab[z])
    else:
        x_average = (new_list_ab[z] - new_list_ab[z - 1]) / 2
        if x_average > 1:
            list_x_average.append('%.4f' % (x_average + new_list_ab[z - 1]))
##打印相邻交点坐标的横坐标差，即每段的宽度（暂时没用）
# print(list_result)
##打印相邻交点中间坐标的横坐标，然后找到对应的y值就搞出来了
# print(list_x_average)
##将列表里的字符串转成浮点型再转成整形，好取区间
out_list = list(map(float, list_x_average))
out_list = list(map(int, out_list))
print("每段中间坐标取整之后的横坐标:", out_list)
###找每段中间横坐标对应的纵坐标
for i, j in zip(range(len(list_y)), range(len(list_x))):
    for k in range(len(out_list)):
        if (out_list[k] - 0.01) < list_x[j] < (out_list[k] + 0.01):
            list_y_average.append(list_y[j])
            for m in range(len(list_y_average)):
                if list_y_average[m] > j_average:
                    list_y_up_average.append(list_y_average[m])
                else:
                    list_y_blow_average.append(list_y_average[m])

print(list_y_average)
print("-----------------------------------------------------------------")
print("上面的y：", list_y_up_average)
print("下面的y：", list_y_blow_average)

y_up_sum = 0
y_blow_sum = 0
for m, n in zip(range(len(list_y_up_average)), range(len(list_y_blow_average))):
    y_up_sum += list_y_up_average[m]
    y_up_average = y_up_sum / len(list_y_up_average)
    y_blow_sum += list_y_blow_average[n]
    y_blow_average = y_blow_sum / len(list_y_up_average)
print("上面的均值：", y_up_average, "下面的均值：", y_blow_average)

###画图
# plot中参数的含义分别是横轴值（x），纵轴值(y)，线的形状、颜色，透明度,线的宽度和标签内容。
plt.plot(list_x, list_y, 'r-', color="blue", alpha=0.8,linewidth=0.7, label=u'图例内容')
plt.title(u"Data", size=10)  # 设置表名为“表名”
plt.legend('y',loc="best",edgecolor="blue")
# 配置默认参数：实现plt.plot中label属性显示
# labels 是图例的名称（能够覆盖在plt.plot( )中label参数值）
# loc 代表了图例在整个坐标轴平面中的位置（一般选取'best'这个参数值）
plt.xlabel('CH1 Time', size=10)  # 设置x轴名为“x轴名”
plt.ylabel('CH1 Current', size=10)  # 设置y轴名为“y轴名”
plt.show()
