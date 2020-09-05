import pandas as pd
import matplotlib.pyplot as  plt
 
def main():
    df = pd.read_excel('C:Users\\zhou\\Desktop\\Korea1.xlsx')
    df.info()
    
    day = df['天数']
    confirm = df['累计确诊']
    
    print("数据行数:" , len(df))
    
    #设置 x ，y 轴的取值范围
    plt.scatter(day,confirm)
    #标签
    plt.title('Korea')
    plt.xlabel("day")
    plt.ylabel("confirm")
    plt.show()
    
#if __name__ == '__main__': #程序入口的问题
    # main()