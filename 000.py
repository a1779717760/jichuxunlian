from PIL import Image,ImageDraw,ImageFont

def u_main():
    im = Image.open("1.png")
    txt = "SSR"
    x , y = im.size
    wdraw = 0.8 * x
    ydraw = 0.08 * y
    draw = ImageDraw.Draw(im)
    # 网上下载的字体无效，用电脑自带字体
    #ttfront = ImageFont.truetype('./truetype.ttf',55)
    draw.text((wdraw,ydraw),txt,fill=(0,0,255))
    im.save("./2.png")

if __name__ == '__main__':
    u_main()


