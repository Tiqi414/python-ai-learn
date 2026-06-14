# 变量定义 - 未指定类型注解 ---> 类型推断
from random import random

a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "C", "E"]
phones = {"13309091111", "15209101902", "18809019201"}
options = {"count": 2, "total": 10}
goods = ("手机", 6999, 1)

names.append(1)
print(names)

# 变量定义 - 指定类型注解
a2: int = 596
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int] = ["A", "C", "E"]
phones2: set[str] = {"13309091111", "15209101902", "18809019201"}
options2: dict[str, int] = {"count": 2, "total": 10}
goods2: tuple[str, int, int] = ("手机", 6999, 1)

names2.append("A")
names2.append(10010)


# 函数类型注解
def circle_area_len(r):
    return round(3.14 * r ** 2, 1), round(2 * 3.14 * r, 1)
print(circle_area_len(10))


def circle_area_len(r: float | int) -> tuple[float, float]:
    return 3.14 * r ** 2, 2 * 3.14 * r
print(circle_area_len(10))

import random
nums = [1,345,6,1,3,4,6,7]
print(random.choice(nums))