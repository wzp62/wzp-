import matplotlib.pyplot as plt

names = ["欢迎来龙餐馆","蜘蛛侠：崭新之日","八仙!","奥德赛","空枪",
         "功夫女足","给阿嬷的情书","去你的岛","年会不能停！2","小黄人与大怪兽"]
money = [19.49,7.2,6.4,6.03,4.21,3.8,3.2,2.1,1.3,1.1]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10,7))
plt.barh(names, money,color='#ff6666')
plt.gca().invert_yaxis()

plt.title("2026年9月内地电影票房前10柱状图")
plt.xlabel("票房（亿元）")
plt.ylabel("影片名称")

plt.tight_layout()
plt.savefig('票房柱状图.png')
print("图片已经保存到桌面！")
