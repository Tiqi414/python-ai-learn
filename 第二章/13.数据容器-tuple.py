# 元组基本操作 - tuple ---> 元素可以被重复, 有序, 不可被修改
# 定义
# t1 = (80,95,78,50,76,80,85,20)
#
# print(t1)
# print(type(t1))
#
# # 索引访问
# print(t1[0])
# print(t1[-1])
#
# # 切片
# print(t1[0:5:1])
#
# # count() 统计元素个数
# print(t1.count(80))
#
# # index() 获取元素索引 (第一个元素位置)
# print(t1.index(80))
#
# # 注意点
# t2 = ()
# print(type(t2))
#
# # 如果定义单元素的元组, 单个元素之后需要加上都逗号, 比如(100,)
# t3 = (100,)
# print(type(t3))



# -------------------------------- 元组 tuple 组包与解包 -----------------------------------
# # 组包操作
# t1 = (5,7,9,10,2,23,12)
#
# print(t1)
#
# # 解包操作
# # 基础解包(变量数量与容器的元素个数一致)
# a,b,c,d,e,f,g = t1
# print(a,b,c,d,e,f,g)
#
# # * 扩展解包(* 收集剩余的所有元素,封装列表list中)
# first,second,*other,last = t1
# print(first,second)
# print(other)
# print(last)


# 案例1:
# a,b = 10,2
# b,a = a,b
# print(a)
# print(b)

# 案例2:
# a,b,c = 100,200,300
# c,a,b = a,b,c
# print(a,b,c)


# 根据提供的学生成绩单, 完成需求: (自己手动第一遍)
# 1.计算每个学生的总分 各科平均分, 然后一并输出出来
# t0 = []
# t = ("S001_王 林","S002_李慕婉","S003_十 三","S004_曾 牛","S005_周 轶",
#      "S006_王 卓","S007_红 蝶" ,"S008_徐立国","S009_许 木","S010_遁 天")
# t1_y = (85,92,78,88,95,76,89,75,86,66) # 语文成绩
# t2_s = (92,88,85,79,96,82,91,69,89,59) # 数学成绩
# t3_e = (78,95,82,91,89,77,94,82,98,72) # 英语成绩
# for i in range(10):
#     print(f"{t[i]}\t的总分为: {t1_y[i] + t2_s[i] + t3_e[i]}, 各科平均分为: {(t1_y[i] + t2_s[i] + t3_e[i])/3:.1f}")
#     t0.append((t1_y[i] + t2_s[i] + t3_e[i])/3)
#
# # 2.统计各科成绩的最低分 最高分 平均分, 并输出
# new_t1_y = sorted(t1_y)
# new_t2_s = sorted(t2_s)
# new_t3_e = sorted(t3_e)
# print(f"语文的最低分为: {new_t1_y[0]}, 最高分为: {new_t1_y[-1]}, 平均分为: {sum(t1_y) / len(t1_y):.1f}")
# print(f"数学的最低分为: {new_t2_s[0]}, 最高分为: {new_t2_s[-1]}, 平均分为: {sum(t2_s) / len(t2_s):.1f}")
# print(f"英语的最低分为: {new_t3_e[0]}, 最高分为: {new_t3_e[-1]}, 平均分为: {sum(t3_e) / len(t3_e):.1f}")
#
# # 3.查找成绩优秀(平均分大于90)的学生, 并输出
# for i in range(10):
#     if t0[i] > 90:
#         print(f"{t[i]}\t是成绩优秀的学生, 成绩为{t0[i]:.1f}")


#######  优化后:
students = (
    ("S001", "王 林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十 三", 78, 85, 82),
    ("S004", "曾 牛", 88, 79, 91),
    ("S005", "周 轶", 95, 96, 89),
    ("S006", "王 卓", 76, 82, 77),
    ("S007", "红 蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许 木", 86, 89, 98),
    ("S010", "遁 天", 66, 59, 72)
)
# 1计算每个学生的总分 各科平均分, 然后一并输出出来
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分\t\t")
# 方式一:
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]}\t{s[1]}\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{avg:.1f}\t")
# 方式二: 可以用 tuple 解包操作 更加直观
for s in students:
    stu_id, name, chinese, math, english = s
    total = chinese + math + english
    avg = total / 3
    print(f"{stu_id}\t{name}\t{chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{avg:.1f}\t")
print()
# 2.统计各科成绩的最低分 最高分 平均分, 并输出
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print(f"语文的最低分为: {min (chinese_scores)}, 最高分为: {max (chinese_scores)}, 平均分为: {sum (chinese_scores) / len (chinese_scores):.1f}")
print(f"数学的最低分为: {min (math_scores)}, 最高分为: {max (math_scores)}, 平均分为: {sum (math_scores) / len (math_scores):.1f}")
print(f"英语的最低分为: {min (english_scores)}, 最高分为: {max (english_scores)}, 平均分为: {sum (english_scores) / len (english_scores):.1f}")
print()
# 3.查找成绩优秀(平均分大于90)的学生, 并输出
for s in students:
    stu_id, name, chinese, math, english = s
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"{stu_id} {name}为优秀学生, 平均成绩为: {avg:.1f}")