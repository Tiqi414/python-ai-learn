# #match...case 模式匹配: 工作日程安排
# day = input("请输入星期几(1-7): ")
#
# match day:
#     case "1":
#         print("周一: 工作会议日")
#     case "2":
#         print("周二: 学习培训日")
#     case "3":
#         print("周三: 项目开发日")
#     case "4":
#         print("周四: 代码审查日")
#     case "5":
#         print("周五: 总结规划日")
#     case "6" | "7":
#         print("周末: 休息放松")
#     case _: #匹配其他所有的情况
#         print("输入有误!")


# 案例: 简单游戏指令系统
oper = input("请输入您的操作: ").lower() # 之后的case里就不用写大写了，比如只写 "w"、"esc" 即可

match oper:
    case "上" | "w" :
        print("角色向上移动")
    case "下" | "s" :
        print("角色向下移动")
    case "左" | "a" :
        print("角色向左移动")
    case "右" | "d" :
        print("角色向右移动")
    case "跳" | " ":
        print("角色跳跃")
    case "攻击" | "j" :
        print("角色发动攻击")
    case "退出" | "esc" :
        print("退出游戏")
    case _:
        print("无效操作!!")
