from mongoCon import *
from mysqlCon import *
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType

def read_turple(turple, num):
    result = []
    for t in turple:
        result.append(t[num])
    return result

def find_address(list, address):
    for l in list:
        if address in l:
            return l
    return None

# 一级行政区(名称:拼音),已验证无空值
def create_provinces():
    provinces = list(init_provinces())
    print("provinces",provinces)
    return provinces

#创建一级行政区字典{拼音：数目}，初始化数目为0
def create_provinces_dict(provinces):
    keys = read_turple(provinces, 2)
    provinces_dict = dict.fromkeys(keys,0)
    return provinces_dict

#一级行政区计数出现频次
def provinces_count(provinces_dict):
    for address in shop.find({},{"_id":0, "address": 1}):
        try:
            addressArr = str(address['address']).lower().replace(","," ").split(" ")
            for a in addressArr:
                if a in provinces_dict:
                    provinces_dict[a] += 1
                    break
        except KeyError:
            # print("地址为空！")
            pass

# print(provinces_dict)
#
# print(provinces_dict)
# print(provinces_dict['guangdong'])
# print(provinces_dict['zhejiang'])
# print(provinces_dict['hebei'])
# print(provinces_dict['anhui'])
# print(provinces_dict['shandong'])
# print(provinces_dict['chongqing'])
# print(provinces_dict['innermongolia'])

#只保留有商店记录的一级行政区数据data[省份，数量]
def provinces_data(provinces, provinces_dict):
    regions = read_turple(provinces, 1)
    values = list(provinces_dict.values())
    data = [list(z) for z in zip(regions,values)]
    data = [d for d in data if d[1] > 0]
    # print(data)
    return data


def create_provinces_geo(provinces_data):
    provinces_geo = (
        Geo()
        .add_schema(maptype="china")
        .add(
            "省份",
            provinces_data,
            type_=ChartType.EFFECT_SCATTER,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False), text_style_opts = opts.TextStyleOpts(font_weight="bold", font_family="Microsoft YaHei"))
        .set_global_opts(title_opts=opts.TitleOpts(title="省份分布图"), visualmap_opts=opts.VisualMapOpts(is_show=True,max_=150),
                         toolbox_opts=opts.ToolboxOpts(is_show=True))
        .render(r"F:\Personal\Desktop\Qoo\analysis\province.html")
    )



#二级行政区(名称：拼音)
def create_cities():
    cities = list(init_cities())
    #删除空值
    for key, value in enumerate(cities):
        if ' ' in value or '' in value:
            del cities[key]
    print("cities", cities)
    return cities

#创建二级行政区字典{(pid, 拼音):数目}，初始化数目为0,经查重发现，非重复数据有367个
def create_cities_dict(cities):
    #查重
    # for city in cities:
    #     if cities.count(city) > 1:
    #         print("重复 ",city)
    cities_dict = dict(zip(cities,[0]*len(cities)))
    # print(len(cities_dict))
    return cities_dict



#二级行政区计数出现频次
def cities_count(provinces, cities_dict):
    pid = 0
    for address in shop.find({},{"_id":0, "address": 1}):
        try:
            addressArr = str(address['address']).lower().replace(","," ").split(" ")
            for a in addressArr:
                province = find_address(provinces, a)
                if province:
                    pid = province[0]
                    break
            for a in addressArr:
                city = find_address(cities, a)
                if city and city[0] == pid:
                    temp = (pid, city[1], a)
                    cities_dict[temp] += 1
                    break
        except KeyError:
            # print("地址为空！")
            pass
    print(cities_dict)
    return cities_dict




# 只保留有商店记录的二级行政区数据data[省份，数量]
def cities_data(cities_dict):
    regions = read_turple(cities_dict.keys(), 1)
    values = list(cities_dict.values())
    data = [list(z) for z in zip(regions,values)]
    data = [d for d in data if d[1] > 0]
    print(data)
    return data



def create_cities_geo(cities_data):
    cities_geo = (
        Geo(init_opts=opts.InitOpts(width="1000px", height="700px"))
        .add_schema(maptype="china-cities")
        .add(
            "城市",
            cities_data,
            type_=ChartType.EFFECT_SCATTER,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False), text_style_opts = opts.TextStyleOpts(font_weight="bold", font_family="Microsoft YaHei"))
        .set_global_opts(title_opts=opts.TitleOpts(title="城市分布图"), visualmap_opts=opts.VisualMapOpts(is_show=True,max_=120),
                         toolbox_opts=opts.ToolboxOpts(is_show=True))
        .render(r"F:\Personal\Desktop\Qoo\analysis\cities.html")
    )



if __name__ == '__main__':
    provinces = create_provinces()
    provinces_dict = create_provinces_dict(provinces)
    provinces_count(provinces_dict)
    provinces_data = provinces_data(provinces, provinces_dict)
    create_provinces_geo(provinces_data)

    cities = create_cities()
    cities_dict = create_cities_dict(cities)
    cities_count(provinces, cities_dict)
    cities_data = cities_data(cities_dict)
    create_cities_geo(cities_data)
