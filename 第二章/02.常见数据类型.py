# 常见数据类型 ---> type() 获取指定的字面量或面量的类型
print("hello")
print(type("hello"))
print(type(100))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))

num = -100
print(type(num))

# 常见数据类型 ---> isinstance(数据,类型) ---> bool值 ---> 判定数据是否是指定的类型,如果是: True,否则: False
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,str))

# 定义字符串的三种方式
s1 = "Hello"
s2 = 'Python'
s3 = """
Hello: 
    欢迎大家加入Python课程的学习!
    大家记得一键三连哦 ~
"""

print(s1)
print(s2)
print(s3)

print(type(s1),type(s2),type(s3))

# 字符串拼接
s1 = "人生苦短,""我用Python"
print(s1)

msg1 = "人生苦短"
msg2 = "我用Python"
print("龟叔说: "+ msg1 + "," + msg2)

# 案列: ---> str(int数字) ---> 将int类型的数字转为字符串
name = "huhu"
age = 24
pro = "软件工程"
hobby = "Python、Java"
print("大家好 , 我是" + name + " , " + "今年" + str(age) + "岁 , 学习的专业是" + pro + " , " + "爱好是" + hobby + "。")

# 字符串格式化 ---> 方式一: %s 占位符
print("大家好,我是%s,今年%s岁,学习的专业是%s,爱好是%s。"%(name,age,pro,hobby))

# 字符串格式化 ---> 方式二: f"...{变量名/表达式}..." ---> 推荐方式
print(f"大家好,我是{name},今年{age}岁,学习的专业是{pro},爱好是{hobby}。")