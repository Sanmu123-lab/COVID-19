# 导入数据
import pandas as pd 
df=pd.read_excel('C:Users\\zhou\\Desktop\\Korea1.xlsx')
df.info()
date = df["天数"].to_list()
confirm = df["累计确诊"].to_list()
print(date)
print(confirm)
# 绘制散点图
import matplotlib.pyplot as  plt
print("数据行数:" , len(df))
plt.scatter(date,confirm)
#标签
plt.title('Korea')
plt.xlabel("day")
plt.ylabel("confirm")
plt.show()