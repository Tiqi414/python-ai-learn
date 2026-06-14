"""
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
    1、添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
        1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
        1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
        1.3 验证成绩范围（0-100 分）
        1.4 创建学生对象并添加到系统
    2、修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
        2.1 输入要修改的学生姓名
        2.2 根据姓名查找该学生，显示该学生当前成绩信息
        2.3 输入新的语文、数学、英语成绩
        2.4 更新学生成绩数据
    3、删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
    4、查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
        4.1 输出格式为："姓名：张三  | 语文：85 | 数学：90 | 英语：88 | 总分：263"
    5、展示全部学生成绩：展示出系统中所有学生的成绩
"""

# 学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"姓名：{self.name}  | 语文：{self.chinese} | 数学: {self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"

    # 修改学生成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


# 教务管理系统
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = [] # 列表, 记录的是在校学生成绩信息

    # 添加学生信息
    def add_student(self):
        name = input("请输入学生姓名: ")

        # 判断学生姓名是否存在, 如果存在, 则添加失败 (不能重复添加)
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在, 添加失败!")
                return

        chinese = float (input("请输入学生语文成绩: "))
        math = float (input("请输入学生数学成绩: "))
        english = float (input("请输入学生英语成绩: "))
        #判断分数是否在 0-100 之间
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            print("学生信息添加成功~")
        else:
            print("各科成绩必须在 0-100 之间!")

    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名: ")

        # 根据学生姓名找到学生信息
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩: {s}")

                chinese = float (input("请输入修改后的语文成绩: "))
                math = float (input("请输入改后的数学成绩: "))
                english = float (input("请输入改后的英语成绩: "))

                # 判断分数是否在 0-100 之间
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese, math, english)
                    print("成绩修改成功 ~ ")
                    print(f"修改后的成绩: {s}")
                    return
                else:
                    print("各科成绩必须在 0-100 之间!")
                    return
        print("未找到该学生, 修改失败!")
    # 删除学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                return
        print("未找到该学生, 删除失败!")

    # 查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名: ")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息: {s}")
                return
        print("未找到该学生!")

    #展示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    # 运行系统
    def run(self):
        print(f"欢迎使用教务管理系统~ V{EduManagement.system_version}")

        while True:
            print()
            print("# ============================================================================  #")
            print("# 1.添加学生   2.修改学生   3.删除学生   4.查询指定学生   5.查询所有学生   6.退出系统    #")
            print("# ============================================================================= #")

            choice = input("\n请选择要执行的操作，输入1~6: ")

            match choice:
                case "1":  # 添加学生
                    self.add_student()
                case "2":  # 修改学生
                    self.update_student()
                case "3":  # 删除学生
                    self.delete_student()
                case "4":  # 查询指定学生
                    self.query_student()
                case "5":  # 查询所有学生
                    self.list_student()
                case "6":  # 退出系统
                    print("Bye ~ ")
                    break
                case _: #  其他情况
                    print("输入错误, 请输入 1-6 之间的菜单功能!")

# 测试
if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()

# 练习
"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
查询购物车：将购物车中的商品信息展示出来，格式为：商品名称：xxx，商品价格：xxx，商品数量：xxx。
退出购物车
"""

# 商品类
class Goods:
    def __init__(self, name, price, num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称：{self.name}，商品价格：{self.price}，商品数量：{self.num}"

    # 修改商品
    def update_goods(self, price=None, num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num

# 购物车管理系统
class ShoppingManagement:
    system_version = "1.0"
    system_name = "购物车管理系统"

    def __init__(self):
        self.goods_list = []

    # 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    def add_goods(self):
        name = input("请输入要添加的商品名称: ")
        for goods in self.goods_list:
            if goods.name == name:
                print("该商品已存在, 请重新输入!")
                return
        price = float (input("请输入该商品的价格: "))
        num = float (input("请输入该商品的数量: "))
        if 0 <= price and 0 <= num:
            goods = Goods(name, price, num)
            self.goods_list.append(goods)
            print("商品添加完成 ~")
        else:
            print("添加失败! 请确认数量和价格是否正确!")

    # 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    def update_goods(self):
        name = input("请输入要修改的商品名称: ")
        for goods in self.goods_list:
            if goods.name == name:
                print(f"当前商品信息: {goods}")

                price = float(input("请输入修改后的价格: "))
                num = float(input("请输入修改后的数量: "))
                if 0 <= price and 0 <= num:
                    goods.update_goods(price, num)
                    print("修改成功 ~")
                    print(f"修改后的信息为: {goods}")
                    return
                else:
                    print("修改失败! 请确认数量和价格是否正确!")
                    return
        print("为查询到该商品信息!")

    # 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    def delete_goods(self):
        name = input("请输入要删除的商品名称: ")
        for goods in self.goods_list:
            if goods.name == name:
                self.goods_list.remove(goods)
                print("该商品已删除完成 ~")
                return
        print("删除失败! 未查询到该商品!")

    # 查询购物车：将购物车中的商品信息展示出来，格式为：商品名称：xxx，商品价格：xxx，商品数量：xxx。
    def list_goods(self):
        if self.goods_list is not None:
            for goods in self.goods_list:
                print(goods)
            return
        print("购物车为空, 请添加商品!")

    # 运行系统
    def run(self):
        print(f"欢迎使用购物车管理系统~ V{ShoppingManagement.system_version}")

        while True:
            print()
            print("# ============================================================  #")
            print("#  1.添加商品   2.修改商品   3.删除商品    4.查询购物车   5.退出系统   #")
            print("# ============================================================= #")

            choice = input("\n请选择要执行的操作，输入1~5: ")

            match choice:
                case "1":  # 添加商品
                    self.add_goods()
                case "2":  # 修改商品
                    self.update_goods()
                case "3":  # 删除商品
                    self.delete_goods()
                case "4":  # 查询购物车
                    self.list_goods()
                case "5":  # 退出系统
                    print("Bye ~ ")
                    break
                case _: #  其他情况
                    print("输入错误, 请输入 1-5 之间的菜单功能!")

# 测试
if __name__ == '__main__':
    shopping_management = ShoppingManagement()
    shopping_management.run()