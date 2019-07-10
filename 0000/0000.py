from PIL import Image, ImageDraw, ImageFont

# 打开图片
# 对于彩色图像，不管其图像格式是PNG，还是BMP，或者JPG，在PIL中，使用Image模块的
# open()函数打开后，返回的图像对象的模式都是“RGB”
# 将图像由RGB模式转换为RGBA模式
# 模式“RGBA”为32位彩色图像，它的每个像素用32个bit表示，其中24bit表示红色、绿色
# 和蓝色三个通道，另外8bit表示alpha通道，即透明通道。
img = Image.open('./1.jpg').convert('RGBA')

# 创建文字空白图,作为画布
txt = Image.new('RGBA', img.size, (255, 255, 255, 0))

# 选择一个字体
fnt = ImageFont.truetype('./source-sans-pro-regular.ttf', 100)

# get a drawing context
d = ImageDraw.Draw(txt)

# 画圆，参数依次是[a,b](以a、b两点作为矩阵的左上角和右下角，在中间画圆），颜色
d.ellipse([(img.size[0]-120, 0), (img.size[0], 120)], fill=(255, 0, 0))

# 第一个参数为左上角坐标
d.text((img.size[0]-85, 0), '3', font=fnt, fill=(255, 255, 255, 128))

# 把原始图片和操作后的画布，拼在一起
out = Image.alpha_composite(img, txt)
out.show()
out.save('./1_1.png')