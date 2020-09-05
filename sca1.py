# 提取数据
import pandas as pd 
df=pd.read_excel('C:Users\\zhou\\Desktop\\Korea1.xlsx')
df.info()
# 绘制散点图
date = df["天数"].to_list()
confirm = df["累计确诊"].to_list()
print(date)
print(confirm)
import pyecharts.options as opts 
from pyecharts.charts import Scatter
scatter= (
	Scatter()
	.add_xaxis(
		xaxis_data=date
		)
	.add_yaxis(
		series_name="",
		y_axis=confirm,
		symbol_size=4,
		label_opts=opts.LabelOpts (is_show=False)
		)
	.set_global_opts(
		xaxis_opts=opts.AxisOpts(type_="value"),
		yaxis_opts=opts.AxisOpts(type_="value"),
		title_opts=opts.TitleOpts(title="韩国实际疫情图")
		)
	)
scatter.render_notebook()