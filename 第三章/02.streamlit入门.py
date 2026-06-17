import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    # 布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",

    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("布偶猫：温柔优雅的'人间天使'")
st.write("布偶猫，因其独特的气质和迷人的外表，被誉为“猫中仙女”。它们体型较大，肌肉发达，是现存体型最大、最重的猫种之一，却拥有与之完全不匹配的温顺性格。")
st.write("布偶猫最引人注目的是那双湛蓝色的眼睛，清澈深邃。它们的被毛属于中长毛，丝滑柔顺，且不易打结，方便打理。其标志性的重点色和白色手套构成了优雅的“双色”或“手套”等经典花色，十分美丽。")
st.write("正如其名，布偶猫极度亲人。它们喜欢被人拥抱，甚至在主人怀抱中会像布偶一样全身放松、瘫软，这是它们表达信任和舒适的方式。它们性格沉稳安静，很少发脾气，对小孩和其他宠物也极具包容心，非常适合作为家庭伴侣宠物。")
st.write("需要注意的是，布偶猫是典型的“室内猫”，需要主人的大量关注和陪伴。此外，它们的一些健康问题（如肥厚性心肌病）也值得留意，定期的兽医检查是确保它们长久健康快乐的关键。")

# 图片
# st.image("./resources/cat.jpg")
st.image("resources/cat.jpg")

# 音频
st.audio("resources/news.mp3")

# 视频
st.video("resources/news.mp4")

# Logo
st.logo("resources/logo.png")

# 表格
students_data = {
    "姓名": ["王林", "李慕婉", "贝罗", "魔礼海", "石萧"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 80],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 181]
}
st.table(students_data)

# 输入框
# 普通输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名为: {name}")

# 密码输入框
password = st.text_input("请输入密码", type="password")
st.write(f"您输入的密码为: {password}")

#单选按钮
gender = st.radio("请输入您的性别", ["男", "女", "未知"], index=2)
st.write(f"您的性别为: {gender}")
