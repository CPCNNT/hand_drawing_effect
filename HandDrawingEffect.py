from GetImgPath import getimgpath
from ImgConverter import imgconverter

image_source = ""
image_handled = ""

[image_source, image_handled] = getimgpath()
img = imgconverter(image_source)

img.save(image_handled)

print("处理完成，请至 {} 查看！".format(image_handled))
