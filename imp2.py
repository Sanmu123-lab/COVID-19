import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
# N为人群总数
N = 51709098
# β为传染率系数
beta = 0.2
# gamma为恢复率系数
gamma = 0.1
# Te为疾病潜伏期
Te = 10
# I_0为感染者的初始人数
I_0 = 4
# E_0为潜伏者的初始人数
E_0 = 0
# R_0为治愈者的初始人数
R_0 = 0
# S_0为易感者的初始人数
S_0 = N - I_0 - E_0 - R_0
# 累计感染者的初始人数
T_0 = 4
# T为传播时间
T = 59

# INI为初始状态下的数组
INI = (S_0,E_0,I_0,R_0,T_0)

def funcSEIR(inivalue,_):
 Y = np.zeros(5)
 X = inivalue
 # 易感个体变化
 Y[0] = - (beta * X[0] *( X[2]+X[1])) / N
 # 潜伏个体变化
 Y[1] = (beta * X[0] *( X[2]+X[1])) / N - X[1] / Te
 # 感染个体变化
 Y[2] = X[1] / Te - gamma * X[2]
 # 治愈个体变化
 Y[3] = gamma * X[2]
 # 累计人数变化
 Y[4] = Y[2]+Y[3]
 return Y

T_range = np.arange(0,T + 1)

RES = spi.odeint(funcSEIR,INI,T_range)

#plt.plot(RES[:,0],color = 'darkblue',label = 'Susceptible',marker = '.')
#plt.plot(RES[:,1],color = 'orange',label = 'Exposed',marker = '.')
#plt.plot(RES[:,2],color = 'red',label = 'Infection',marker = '.')
#plt.plot(RES[:,3],color = 'green',label = 'Recovery',marker = '.')
plt.plot(RES[:,4],color = 'yellow',label = 'Sum',marker = '.')

df=pd.read_excel('C:Users\\zhou\\Desktop\\Korea1.xlsx')
df.info()
date = df["天数"].to_list()
confirm = df["累计确诊"].to_list()
#print(date)
#print(confirm)
# 绘制散点图
#import matplotlib.pyplot as  plt
print("数据行数:" , len(df))
plt.scatter(date,confirm)
plt.legend('x1')

plt.title('Korea SEIR Model')
plt.legend()
plt.xlabel('Day')
plt.ylabel('Number')
plt.show()
