# 导入模块
# import utils.my_fun
#
# utils.my_fun.log_separator1()
#
# from utils import my_fun
# my_fun.log_separator1()

# 注意: 如果要通过 from utils import * 导入包下所有模块, 需要 __init__.py 文件中添加 __all__ =[]
# from utils import *
#
# my_fun.log_separator1()
#
# print(my_var.PI)

# 导入模块中的功能
# 绝对路径: 从项目的根目录下开始查找
from 第二章.utils.my_fun import log_separator1, log_separator3
# 相对路径: 从当前文件所在目录开始查找
from utils.my_fun import log_separator1, log_separator3


log_separator1()
log_separator3()

