import json
import requests # pip install requests  requests 库是用来在Python中发出标准的HTTP请求
import jsonpath # pip install jsonpath
from pyecharts.charts import Map,Geo ## pip install pyecharts 
from pyecharts import options as opts 
from pyecharts.globals import GeoType,RenderType


# 1.目标网站
url='https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
# 2.请求资源，获取响应内容
resp=requests.post(url)
print(resp.text)
# 3.提取数据
# 类型转换  json--->dict
data=json.loads(resp.text)
# print(data['data'][0]['name'])
name=jsonpath.jsonpath(data,"$..name")
print(name)
confirm=jsonpath.jsonpath(data,"$..confirm")
print(confirm)

# 数据处理
data_list=list(zip(name,confirm))
# list 序列解包
print(list(data_list))

# 4.保存数据、可视化  matplotlib(静态) 和 pyecharts(动态)

map=Map().add(series_name="世界疫情分布",  
			  data_pair=data_list, # 输入数据
			  maptype="world",
			  is_map_symbol_show=False

)
# 设置系列配置项
map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 不显示国家名称
map.render('世界疫情分布情况.html')