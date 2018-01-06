# 学习文件操作
open('方.jpg')  # 相对路径打开
open('D:\\GitHub\\PyPractice\\方.jpg')  # 绝对路径打开方式1
open('D:/GitHub/PyPractice/方.jpg')  # 绝对路径打开方式2


# 图片虽然不能显示，但是已经挂载在了内存当中，如需查看需要调用模块
from PIL import Image
img = Image.open('方.jpg')
img.show()


