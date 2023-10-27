# from PIL import ImageGrab

# msg_file = '/Users/zhuangyuhao/Downloads/picture.msg'  # msg文件路径

# # 读取msg文件内容
# with open(msg_file, 'r', encoding='gbk') as file:
#     msg_content = file.read()

# # 根据回复信息的标识符进行分割
# reply_sections = msg_content.split('发件人: ')

# # 忽略第一个分割后的部分（原始消息）
# reply_sections = reply_sections[1:]

# # 循环处理每个回复信息
# for i, section in enumerate(reply_sections):
#     # 设置截图区域的坐标
#     x = 100  # 截图区域左上角的x坐标
#     y = 100 + i * 200  # 截图区域左上角的y坐标（每个回复信息之间间隔200像素）
#     width = 800  # 截图区域的宽度
#     height = 100  # 截图区域的高度

#     # 执行截图
#     screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

#     # 保存截图
#     output_file = f'reply_{i + 1}.png'
#     screenshot.save(output_file)


import chardet

msg_file = '/Users/zhuangyuhao/Downloads/picture.msg'  # msg文件路径

# 读取msg文件内容并检测编码
with open(msg_file, 'rb') as file:
    content = file.read()
    result = chardet.detect(content)

file_encoding = result['encoding']
confidence = result['confidence']

# 输出编码信息
print(f"文件编码：{file_encoding}")
print(f"可信度：{confidence}")
