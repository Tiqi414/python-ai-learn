"""
    案例:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
        1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5. 列出所有学生：遍历所有学生信息并输出。
        6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        7. 退出系统。
"""
# 遇到的问题:
#          加了一些没必要的循环,可以用 input() 直接返回主界面; 成绩数据类型一开始为设置 int 整数型;
#          统计成绩时将存储各科成绩的列表放到的循环外, 会导致每次操作都会增加, 造成冗余;
#          分别统计各成绩学员的时候, elif 和 if 选择错误, 选了 elif 造成结果只会打印一个, 同时有会更优方案, 如下:
#             找出最高分和最低分的学生
#             chinese_max_students = [name for name, scores in student_scores.items() if scores['chinese'] == chinese_max]
#             chinese_min_students = [name for name, scores in student_scores.items() if scores['chinese'] == chinese_min]
#
#             math_max_students = [name for name, scores in student_scores.items() if scores['math'] == math_max]
#             math_min_students = [name for name, scores in student_scores.items() if scores['math'] == math_min]
#
#             english_max_students = [name for name, scores in student_scores.items() if scores['english'] == english_max]
#             english_min_students = [name for name, scores in student_scores.items() if scores['english'] == english_min]

e = """
======================================================================
===                                                                ===      
===  1.添加学生信息    2.修改学生信息    3.删除学生信息    4.查询学生信息  ===        
===       5.列出所有学生   6.统计班级成绩    7.退出系统                  ===   
===                                                                ===  
======================================================================
"""
print("欢迎使用教务管理系统~~")
stu_info = {}

while True:
    print(e)
    function = input("请选择您需要进行的操作(1-7): ")
    match function:
# 1.添加学生信息: 根据录入学生姓名 语文 数学 英语成绩, 录入完成保存到系统中
        case "1":
            while True:
                stu_name = input("请输入学生姓名: ")
                if stu_name not in stu_info:
                    chinese_score = int (input("请输入语文成绩: "))
                    math_score = int (input("请输入数学成绩: "))
                    english_score = int (input("请输入英语成绩: "))
                    stu_info[stu_name] = {"chinese_score": chinese_score, "math_score": math_score,
                                          "english_score": english_score}
                    print(f"学生{stu_name}信息已添加完成!")
                    print(stu_info)
                    if input("是否继续添加(选择 '是' 或者 '否'): ") == "否":
                        break
                else:
                    print("该学生信息已存在, 请重新输入!")
                    break
# 2.修改学生信息: 要求输入要修改的学生姓名, 然后再提示输入语文 数学 英语成绩, 输入完成后修改学院信息
        case "2":
            while True:
                stu_name = input("请输入要选择修改的学生姓名: ")
                if stu_name  in stu_info:
                    chinese_score = int (input("请输入要修改的语文成绩: "))
                    math_score = int (input("请输入要修改的数学成绩: "))
                    english_score = int (input("请输入要修改的英语成绩: "))
                    stu_info[stu_name] = {"chinese_score": chinese_score, "math_score": math_score,
                                          "english_score": english_score}
                    print(f"学生{stu_name}的信息已修改完成!")
                    if input("是否继续修改(选择 '是' 或者 '否'): ") == "否":
                        break
                else:
                    print("未查询到该学生信息, 请重新输入!")
                    break
# 3.删除学生信息: 要求输入要删除的学生姓名, 根据姓名删除学生信息
        case "3":
            while True:
                stu_name = input("请输入要删除的学生姓名: ")
                if stu_name in stu_info:
                    stu_info.pop(stu_name)
                    print(f"已成功删除学生{stu_name}的信息")
                    if input("是否继续删除(选择 '是' 或者 '否'): ") == "否":
                        break
                else:
                    print("未查询到该学生信息, 请重新输入!")
                    break
# 4.查询学生信息: 要求输入要查询的学生姓名,根据姓名查询学生信息并输出
        case "4":
            while True:
                stu_name = input("请输入要查询的学生姓名: ")
                if stu_name  in stu_info:
                    stu_score = stu_info[stu_name]
                    print(f"学生姓名: {stu_name}, 语文成绩: {stu_score['chinese_score']}, 数学成绩: {stu_score['math_score']}, 英语成绩: {stu_score['english_score']}")
                    if input("是否继续查询(选择 '是' 或者 '否'): ") == "否":
                        break
                else:
                    print("未查询到该学生信息, 请重新输入!")
                    break
# 5.列出所有学生: 遍历所有学生信息并输出
        case "5":
            if len(stu_info) != 0:
                for stu_name in stu_info:
                    stu_score = stu_info[stu_name]
                    print(f"学生姓名: {stu_name}, 语文成绩: {stu_score['chinese_score']}, 数学成绩: {stu_score['math_score']}, 英语成绩: {stu_score['english_score']}")
            else:
                print("未查询到任何学生信息, 请添加~")
            input("\n回车返回主菜单")
# 6.统计班级成绩: 统计班级语文 数学 英语成绩的最高分 最低分 平均分, 以及语文 数学 英语最高分和最低分的学员姓名
        case "6":
            chinese_score_list = []
            math_score_list = []
            english_score_list = []
            if len(stu_info) != 0:
                for stu_name in stu_info.keys():
                    stu_score = stu_info[stu_name]
                    chinese_score_list.append(stu_score['chinese_score'])
                    math_score_list.append(stu_score['math_score'])
                    english_score_list.append(stu_score['english_score'])
                chinese_score_avg = sum(chinese_score_list) / len(chinese_score_list)
                math_score_avg = sum(math_score_list) / len(math_score_list)
                english_score_avg = sum(english_score_list) / len(english_score_list)
                print(f"班级语文成绩的最高分为: {max(chinese_score_list)}, 最低分为: {min(chinese_score_list)}, 平均分为: {chinese_score_avg:.1f}")
                print(f"班级数学成绩的最高分为: {max(math_score_list)}, 最低分为: {min(math_score_list)}, 平均分为: {math_score_avg:.1f}")
                print(f"班级英语成绩的最高分为: {max(english_score_list)}, 最低分为: {min(english_score_list)}, 平均分为: {english_score_avg:.1f}")
                for stu_name in stu_info.keys():
                    stu_score = stu_info[stu_name]
                    if stu_score['chinese_score'] == max(chinese_score_list):
                        print(f"语文成绩最高分的学员: {stu_name}")
                    if stu_score['math_score'] == max(math_score_list):
                        print(f"数学成绩最高分的学员: {stu_name}")
                    if stu_score['english_score'] == max(english_score_list):
                        print(f"英语成绩最高分的学员: {stu_name}")
                    if stu_score['chinese_score'] == min(chinese_score_list):
                        print(f"语文成绩最低分的学员: {stu_name}")
                    if stu_score['math_score'] == min(math_score_list):
                        print(f"数学成绩最低分的学员: {stu_name}")
                    if stu_score['english_score'] == min(english_score_list):
                        print(f"英语成绩最低分的学员: {stu_name}")
            else:
                print("未查询到任何学生信息, 请添加~")
            input("\n回车返回主菜单")
# 7.退出系统
        case "7":
            print("欢迎下次使用~")
            break
        case _:
            print("非法操作, 不支持!!!")
