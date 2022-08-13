import sys
from win32gui import GetOpenFileNameW, GetSaveFileNameW


def getimgpath():
    img_src = ""
    img_hdl = ""

    try:
        if sys.platform.startswith('win32'):
            print("请选择待处理图片的路径")
            img_src = GetOpenFileNameW()[0]
            print("请设置处理后图片的储存路径")
            img_hdl = GetSaveFileNameW()[0]
        elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
            img_src = input("请输入待处理图片的路径：")
            img_hdl = input("请输入处理后图片的储存路径：")
        else:
            img_src = input("请输入待处理图片的路径：")
            img_hdl = input("请输入处理后图片的储存路径：")
    except:
        img_src = input("请输入待处理图片的路径：")
        img_hdl = input("请输入处理后图片的储存路径：")

    return [img_src, img_hdl]
