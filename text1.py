import json
import requests # pip install requests  requests 库是用来在Python中发出标准的HTTP请求
import jsonpath # pip install jsonpath
import xlwt
# import csv
# import pandas as pd
# from pyecharts.charts import Map,Geo ## pip install pyecharts 
# from pyecharts import options as opts 
# from pyecharts.globals import GeoType,RenderType


# 1.目标网站
# url='https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
# 2.请求资源，获取响应内容
# resp=requests.post(url)
# print(resp.text)
# 3.提取数据
# 类型转换  json--->dict
# data=json.loads(resp.text)
# print(data['data'][0]['name'])
# name=jsonpath.jsonpath(data,"$..name")
# print(name)
# confirm=jsonpath.jsonpath(data,"$..confirm")
# print(confirm)


url='https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryMerge'
resp_1=requests.post(url)
# print(resp_1.text)
data=json.loads(resp_1.text)
# print(data['data'][0]['name'])
date=jsonpath.jsonpath(data,"$..date")
# print (date)
confirm=jsonpath.jsonpath(data,"$..confirm")
# print(confirm)

# 保存数据
def save_to_excel():
	try:
		workbook=xlwt.Workbook(encoding='utf-8')
		sheet=workbook.add_sheet('yiqing')
		head=['日期','确诊人数']
		for h in range(len(head)):
			sheet.write(0,h,head[h])

		i=1
		for product in all_products:
			sheet.write(i,0,product['date'])
			sheet.write(i,1,product['confirm'])

			i+=1
		workbook.save('F:/Cov/yiqing.xlsx')
		print ('写入excle成功')
	except Exception:
		print('写入excle失败')











# with open('xiaoshuaib.csv', mode='w') as csv_file:
    #fieldnames = ['日期', '确诊人数']
    #writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #writer.writeheader()
    #writer.writerow({'日期':print (date), '确诊人数':print(confirm)})
   

# x=pandas.read_csv('xiaoshuaib.csv') # 注释
# print(x)




# 数据处理
# date_list=list(zip(date,confirm))
# list 序列解包
# print(list(date_list))

# 4.保存数据、可视化  matplotlib(静态) 和 pyecharts(动态)

#map=Map().add(series_name="世界疫情分布",  
			#  data_pair=data_list, # 输入数据
			# maptype="world",
			 # is_map_symbol_show=False)
# 设置系列配置项
#map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))  # 不显示国家名称
#map.render('世界疫情分布情况.html')