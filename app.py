import pandas as pd
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType, ChartType
from pyecharts import options as opts
from pyecharts.charts import Bar, WordCloud, Page, Pie, Geo
from pyecharts.commons.utils import JsCode


def pub_sports_place_pie():
    data = pd.read_csv('pub_sports_place.csv', encoding="gbk")
    list_name1 = []
    list_name2 = []
    new_list = []
    list_name1 = list(data.loc[:, "districtName"])
    df = pd.DataFrame(list_name1, columns=["districtName"])

    ##去除空值
    index = df["districtName"].notnull()
    df = df[index]

    ###统计去除重复项的内容
    for i in list_name1:
        if i not in list_name2:
            list_name2.append(i)

    ####统计词频
    count_times_dict = {}
    for i in list_name1:
        if list_name1.count(i) > 1:
            count_times_dict[i] = list_name1.count(i)

    ##字典排序
    count_times_list = sorted(count_times_dict.items(), key=lambda x: x[1], reverse=True)
    count_times_dict = {}
    for i, j in count_times_list:
        count_times_dict[i] = j

    list_districts = []
    list_numbers = []
    for i, j in count_times_dict.items():
        list_districts.append(i)
        list_numbers.append(j)

    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add(
            "", [list(z) for z in zip(list_districts, list_numbers)],
            # 设置圆心坐标
            center=["40%", "57%"],
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Sport Places"),
            legend_opts=opts.LegendOpts(
                type_="scroll",
                # 'scroll'：可滚动翻页的图例。当图例数量较多时可以使用。
                pos_left="80%",
                orient="vertical",
                # 图例列表的布局朝向。垂直/水平
                pos_top="15%"
                # 图例组件离容器上侧的距离。
            ),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


def pub_sports_place_items_bar():
    data = pd.read_csv('pub_sports_place_item.csv', encoding="gbk")
    list_name1 = []
    list_name2 = []
    new_list = []
    list_name1 = list(data.loc[:, "sportsPlaceItemName"])
    df = pd.DataFrame(list_name1, columns=["sportsPlaceItemName"])

    ###去除空值
    index = df["sportsPlaceItemName"].notnull()
    df = df[index]

    ###统计去除重复项的内容
    for i in list_name1:
        if i not in list_name2:
            list_name2.append(i)

    ####统计词频
    count_times_dict = {}
    for i in list_name1:
        if list_name1.count(i) > 1:
            count_times_dict[i] = list_name1.count(i)

    ##字典排序
    count_times_list = sorted(count_times_dict.items(), key=lambda x: x[1], reverse=True)
    count_times_dict = {}
    for i, j in count_times_list:
        count_times_dict[i] = j

    list_items = []
    list_numbers = []
    for i, j in count_times_dict.items():
        list_items.append(i)
        list_numbers.append(j)

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
        .add_xaxis(list_items)
        .add_yaxis("运动项目", list_numbers, color=Faker.rand_color())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider+inside）"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
    )
    return c


def shanghai_map():
    data = pd.read_csv('pub_sports_place.csv', encoding="gbk")
    list_name1 = []
    list_name2 = []
    new_list = []
    list_name1 = list(data.loc[:, "districtName"])
    df = pd.DataFrame(list_name1, columns=["districtName"])

    ##去除空值
    index = df["districtName"].notnull()
    df = df[index]

    ###统计去除重复项的内容
    for i in list_name1:
        if i not in list_name2:
            list_name2.append(i)

    ####统计词频
    count_times_dict = {}
    for i in list_name1:
        if list_name1.count(i) > 1:
            count_times_dict[i] = list_name1.count(i)

    ##清除域外
    del count_times_dict["域外"]

    ##字典排序
    count_times_list = sorted(count_times_dict.items(), key=lambda x: x[1], reverse=True)
    count_times_dict = {}
    for i, j in count_times_list:
        count_times_dict[i] = j

    list_districts = []
    list_numbers = []
    for i, j in count_times_dict.items():
        list_districts.append(i)
        list_numbers.append(j)

    c = (
        Geo(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_schema(maptype="上海")
        .add("用户分布", [list(z) for z in zip(list_districts, list_numbers)], type_=ChartType.EFFECT_SCATTER, )
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=200,max_=1900,type_="color"), title_opts=opts.TitleOpts(title="上海"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )
    return c


def contents_wordcloud():
    words = [('完好', 350),
             ('正常', 201),
             ('球场', 186),
             ('开放', 162),
             ('篮球', 126),
             ('开门', 110),
             ('篮球场', 104),
             ('器材', 102),
             ('健身', 67),
             ('没有', 57),
             ('运转', 50),
             ('现在', 48),
             ('请问', 41),
             ('时间', 41),
             ('希望', 35),
             ('使用', 35),
             ('运动', 34),
             ('场地', 33),
             ('设备', 32),
             ('已经', 26),
             ('无法', 25),
             ('收费', 25),
             ('改造', 24),
             ('建议', 23),
             ('谢谢', 23),
             ('维修', 21),
             ('需要', 21),
             ('打球', 21),
             ('一下', 20),
             ('不能', 20),
             ('签到', 20),
             ('上肢', 19),
             ('小区', 19),
             ('牵引', 18),
             ('牵引器', 18),
             ('居民', 17),
             ('地方', 17),
             ('设施', 17),
             ('太极', 17),
             ('修好', 17),
             ('疫情', 16),
             ('锻炼', 16),
             ('健身器', 16),
             ('健身器材', 15),
             ('市民', 15),
             ('公园', 15),
             ('损坏', 15),
             ('八点', 15),
             ('上海', 15),
             ('社区', 14),
             ('完好无损', 14),
             ('漫步', 14),
             ('无损', 14),
             ('报修', 13),
             ('人员', 13),
             ('活动', 13),
             ('不是', 12),
             ('电话', 12),
             ('体育', 12),
             ('八点半', 12),
             ('不到', 12),
             ('增加', 12),
             ('联系', 11),
             ('单杠', 11),
             ('你好', 11),
             ('不开', 11),
             ('管理', 11),
             ('免费', 10),
             ('进入', 10),
             ('网球', 10),
             ('巡查', 10),
             ('工作', 10),
             ('预约', 10),
             ('公共', 10),
             ('尽快', 9),
             ('足球', 9),
             ('健身房', 9),
             ('腰背', 9),
             ('球架', 9),
             ('全天', 9),
             ('安装', 9),
             ('显示', 9),
             ('nan', 9),
             ('不了', 9),
             ('修复', 9),
             ('双杠', 9),
             ('应该', 8),
             ('修理', 8),
             ('篮球架', 8),
             ('规定', 8),
             ('小时', 8),
             ('影响', 8),
             ('向上', 7),
             ('引体向上', 7),
             ('为啥', 7),
             ('测试', 7),
             ('重新', 7),
             ('根本', 7),
             ('问题', 7),
             ('器械', 7),
             ('扭腰', 7),
             ('允许', 7),
             ('图片', 7),
             ('旁边', 7),
             ('里面', 7),
             ('方便', 7),
             ('一切', 7),
             ('附近', 7),
             ('一切正常', 7),
             ('早上', 7),
             ('场所', 7),
             ('目前', 7),
             ('不错', 7),
             ('预定', 6),
             ('作人', 6),
             ('海市', 6),
             ('身体', 6),
             ('须知', 6),
             ('关门', 6),
             ('知道', 6),
             ('安全', 6),
             ('上海市', 6),
             ('物业', 6),
             ('有人', 6),
             ('工作人员', 6),
             ('全民', 6),
             ('推手', 6),
             ('进去', 6),
             ('巡视', 6),
             ('网球场', 6),
             ('关闭', 6),
             ('手机', 6),
             ('周末', 6),
             ('松动', 6),
             ('晚上', 6),
             ('进不去', 6),
             ('钥匙', 6),
             ('以前', 6),
             ('中心', 6),
             ('之前', 6),
             ('拆除', 5),
             ('建设', 5),
             ('几个', 5),
             ('防控', 5),
             ('政府', 5),
             ('今天', 5),
             ('上面', 5),
             ('室外', 5),
             ('年轻人', 5),
             ('按摩', 5),
             ('锁门', 5),
             ('室内', 5),
             ('打篮球', 5),
             ('投诉', 5),
             ('意义', 5),
             ('昨天', 5),
             ('螺丝', 5),
             ('没人', 5),
             ('下午', 5),
             ('上锁', 5),
             ('包场', 5),
             ('注销', 5),
             ('家园', 5),
             ('按摩器', 5),
             ('全部', 5),
             ('很多', 5),
             ('公众', 5),
             ('个人', 5),
             ('不行', 5),
             ('调换', 5),
             ('实际', 5),
             ('年轻', 5),
             ('打卡', 5),
             ('过去', 5),
             ('场馆', 5),
             ('骑车', 5),
             ('能否', 5),
             ('领导', 5),
             ('进行', 5),
             ('起来', 5),
             ('足球场', 5),
             ('羽毛', 4),
             ('门球', 4),
             ('平时', 4),
             ('标准', 4),
             ('才能', 4),
             ('忽略', 4),
             ('地面', 4),
             ('合理', 4),
             ('原因', 4),
             ('不好', 4),
             ('大家', 4),
             ('周边', 4),
             ('正在', 4),
             ('孩子', 4),
             ('更换', 4),
             ('健康', 4),
             ('数据', 4),
             ('及时', 4),
             ('羽毛球场', 4),
             ('完全', 4),
             ('错误', 4),
             ('大门', 4),
             ('名字', 4),
             ('理由', 4),
             ('出来', 4),
             ('运动场', 4),
             ('打扮', 4),
             ('老人', 4),
             ('羽毛球', 4),
             ('单双杠', 4),
             ('限制', 4),
             ('晾晒', 4),
             ('恶劣', 4),
             ('号码', 4),
             ('运动器材', 4),
             ('警示牌', 4),
             ('麻烦', 4),
             ('训练', 4),
             ('看到', 4),
             ('恢复', 4),
             ('无人', 4),
             ('加入', 4),
             ('没开', 4),
             ('测试数据', 4),
             ('发现', 4),
             ('停车', 4),
             ('建造', 4),
             ('公示', 4),
             ('五点', 4),
             ('管理员', 4),
             ('态度', 4),
             ('美丽', 4),
             ('警示', 4),
             ('严重', 4),
             ('拉绳', 4),
             ('隐患', 4),
             ('练习', 3),
             ('手机号', 3),
             ('img', 3),
             ('块钱', 3),
             ('期间', 3),
             ('低龄', 3),
             ('此条', 3),
             ('下班', 3),
             ('src', 3),
             ('非常', 3),
             ('地板', 3),
             ('处理', 3),
             ('乒乓', 3),
             ('小孩', 3),
             ('成年', 3),
             ('街道', 3),
             ('费用', 3),
             ('开发', 3),
             ('游乐', 3),
             ('对外', 3),
             ('门锁', 3),
             ('时段', 3),
             ('门口', 3),
             ('您好', 3),
             ('onerror', 3),
             ('区域', 3),
             ('更新', 3),
             ('缺少', 3),
             ('今日', 3),
             ('难道', 3),
             ('大哥', 3),
             ('造成', 3),
             ('铁架', 3),
             ('二维码', 3),
             ('是否', 3),
             ('护栏', 3),
             ('一个', 3),
             ('行不行', 3),
             ('需求', 3),
             ('满足', 3),
             ('春节', 3),
             ('文化', 3),
             ('不合', 3),
             ('形同虚设', 3),
             ('天天', 3),
             ('反馈', 3),
             ('服务', 3),
             ('想不到', 3),
             ('风险', 3),
             ('打扰', 3),
             ('环境', 3),
             ('ok', 3),
             ('快点', 3),
             ('一年', 3),
             ('低龄化', 3),
             ('时间段', 3),
             ('老化', 3),
             ('体育设施', 3),
             ('形同', 3),
             ('有效', 3),
             ('大爷', 3),
             ('双位', 3),
             ('施工', 3),
             ]

    c = (
        WordCloud()
        .add(series_name="网友评论", data_pair=words, word_size_range=[20, 55],
             textstyle_opts=opts.TextStyleOpts(font_family="cursive"))
        .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud"), tooltip_opts=opts.TooltipOpts(is_show=True))
    )
    return c


def page_draggable_layout():
    page = Page(page_title="用户画像统计数据可视化", layout=Page.DraggablePageLayout)
    page.add(pub_sports_place_pie(),
             pub_sports_place_items_bar(),
             contents_wordcloud(),
             shanghai_map())
    # page.render("page.html")


if __name__ == "__main__":
    page_draggable_layout()

Page.save_resize_html("page.html",
                      cfg_file="chart_config328.json",
                      dest="page.html")
