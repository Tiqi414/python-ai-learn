# # 列表操作
# # 定义列表 --list
# s = [56,90,88,65,90,"A","Hello",True]
# print(type(s))
#
# # 访问列表元素
# # 获取
# print(s[0]) #正向索引, 从0开始
# print(s[-8]) #反向索引, 从-1开始
#
# # 修改
# s[5] = "ABC"
# print(s)
#
# # 删除
# del s[6]
# print(s)
#
# # 循环
# for item in s:
#     print(item)



# --------------------------列表 list 切片-------------------------
# # 定义列表
# s = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
#
# # 切片操作
# print(s[0:5])
# print(type(s))
# print(s[5:1:-1])

# ----------------------列表 list 常用方法-------------------------
# 列表定义:
# s = [56,90,88,65,90,100,209,72,145]
# print(s)
#
# # append(): 列表后面追加元素
# s.append(199)
# print(s)
#
# # insert(): 在指定元素之前加入元素
# s.insert(2,80)
# print(s)
#
# # remove(): 移除列表中第一个匹配到的元素
# s.remove(90)
# print(s)
#
# # pop(): 删除列表中指定索引位置的元素并返回(如果未指定, 默认删除最后一个)
# e = s.pop(1)
# print(e)
#
# e = s.pop()
# print(e)
#
# # sort(): 排序
# s.sort()
# print(s)
#
# # reverse(): 反转
# s.reverse()
# print(s)


# 案例1: 将用户输入的10个数字, 存储到一个列表中, 并将列表中的数字进行排序,输出其中的最小值 最大值以及平均值

# # 1. 定义列表
# s_list= []
#
# # 2. 将用户输入的数字存入列表 --> 使用append()
# for i in range(10):
#     s_list.append(int (input(f"请输入第{i+1}个数字: ")))
# print(s_list)
#
# # 3. 排序
# s_list.sort()
# print(f"列表从小到大顺序为: {s_list}")
#
# # 4. 输出其中的最小值 最大值以及平均值 --> sum() 求和; len() 获取元素的个数(列表长度)
# print(f"列表中的最小值是: {min(s_list)}")
# print(f"列表中的最大值是: {s_list[-1]}")
# print(f"列表中的平均值是: {sum(s_list)/len(s_list):.2f}")


# 案例2: 合并两个列表中的元素,并对合并的结果进行去重处理(去除列表中重复的元素)
# s_list1 = [19,23,54,64,875,20,109,123,54]
# s_list2 = [55,80,72,35,60,123,54,29,91]
#
#  # 1. 合并列表
# for i in s_list2:
#     s_list1.append(i)
# print(f"合并后的列表为: {s_list1}")
#
#  # 2. 去除重复记录
# new_list = []
# for i in s_list1:
#     # 判断new_list中是否存在 i 元素, 如果不在再添加
#     if i not in new_list: # 判断元素是否存在于列表中, 如果存在,则返回True; 不存在,返回false
#         new_list.append(i)
# print(f"合并去重后的列表为: {new_list}")


# 案例2(简化版本): 合并两个列表中的元素,并对合并的结果进行去重处理(去除列表中重复的元素)
# s_list1 = [19,23,54,64,875,20,109,123,54]
# s_list2 = [55,80,72,35,60,123,54,29,91]
#
#  # 1. 合并列表
#  # 解包: 将列表这一类容器解开成一个一个独立的元素
#  # 组包: 将多个值合并到一个容器
# s_list = [*s_list1, *s_list2]               # s_list = s_list1 + s_list2
# print(f"合并后的列表为: {s_list}")
#
#  # 2. 去除重复记录
# new_list = []
# for i in s_list:
#     # 判断new_list中是否存在 i 元素, 如果不在再添加
#     if i not in new_list: # 判断元素是否存在于列表中, 如果存在,则返回True; 不存在,返回false
#         new_list.append(i)
# print(f"合并去重后的列表为: {new_list}")


# 案例3: 生成1-20的平方列表:
# 方式一: 传统方式
# s_list = []
# for i in range(1,21):
#     s_list.append(i**2)
# print(f"1-20的平方列表为: {s_list}")
#
# # 方式二: 列表推导式 --> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式1: [要插入的值 for i in 序列/列表]
# num_list2 = [i**2 for i in range(1,21)]
# print(f"1-20的平方列表为: {s_list}")
#
# # 从如下数字列表中提取所有偶数, 并计算其平方, 组成一个新的列表
# # 方式一: 传统方式
# num_list = [19,23,54,64,87,20,109,232,43,26,55,72]
# new_list = []
# for i in num_list:
#     if i % 2 == 0 :
#         new_list.append(i**2)
# print(f"新的列表为: {new_list}")
#
# # 方式二: 列表推导式 --> 就是按照一定的规则快速生成一个列表的方法 --> 语法格式2: [要插入的值 for i in 序列/列表 if 条件]
# new_list1 = [i**2 for i in num_list if i% 2 == 0]
# print(f"新的列表为: {new_list}")

# 合并如下三个列表,并对合并后的,列表进行元素去重,然后排好序后输出
# list1 = ['M','A','C','E','F','G','H','L','N','I','J','K','O']
# list2 = ['X','Z','T','Y','D','E','F','G']
# list3 = ['W','A','S','D']
# new_list1 = [*list1 , *list2, *list3]
# new_list2 = []
#
# # new_list2 = sorted(set([*list1, *list2, *list3]))
#
# for i in new_list1:
#    if i not in new_list2:
#         new_list2.append(i)
# new_list2.sort()
# print(f"新的列表为: {new_list2}")


# 将如下列表中能被 3 或 5 整除的元素提取出来 并获取这些数字对应的平方, 组成一个新的列表
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
new_list = [i**2 for i in list1 if i%3==0 or i%5==0]
print(f"新的列表为: {new_list}")


# 将如下列表中的正数提取出来, 封装成一个新的列表
list6 = [11,2,31,4,-5,15,17,28,49,10,-11,16,54,-14,36,-16,87,-39]
new_list6 = [i for i in list6 if i > 0]
print(f"新的列表为: {new_list6}")



