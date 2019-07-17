import os
import glob
from PIL import Image

# iphone5分辨率：1136×640
# 图片是可以旋转的，也就是长和宽可以互换。1136×640以下和640×1136以下图片都符合要求
# 因此获取图片的长边和1136比，短边和640比，哪个比值大说明要按哪个比值来缩放

# 图片输入目录、输出目录
input_dir = './0005/input_img'
output_dir = './0005/output_img'
#遍历图片，并修改保存
for file in glob.glob(input_dir + '/*.jpg'):
    img = Image.open(file)
    h , w = img.size[0] , img.size[1]
    scale = max( max(h , w) / 1136 , min(h , w) / 640)
    if scale > 1:
        try:
            img = img.resize((int(h/scale),int(w/scale)),Image.BILINEAR)
            img.save(os.path.join(output_dir,os.path.basename(file)))
        except Exception as e:
            print(e)
