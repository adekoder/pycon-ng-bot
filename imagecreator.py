from PIL import Image, ImageDraw, ImageFont

day = 1

arialFont = ImageFont.truetype('fonts/arial.ttf',150)

class MakeImage():
    def __init__(self, *, day, dimension=(), bgcolor, banner ):
        self.day = day
        self.width = dimension[0]
        self.height = dimension[1]
        self.bgcolor = bgcolor
        self.banner = banner
    
    def __create_tag(self):
        image = Image.new('RGBA', (self.width, self.height), self.bgcolor)
        if self.day > 1:
            text = '%sdays to go'% self.day
        else:
            text = '%sday to go'% self.day
        draw = ImageDraw.Draw(image)
        draw.text((50, 100), text , fill='green', font=arialFont)
        path = 'images/%s.png' % self.day
        image.save(path)
        return path

    def __place_message_on_banner(self, tag):
        count_tag = Image.open(tag)
        banner =  Image.open(self.banner)
        banner.paste(count_tag, (40, 300 ))
        file_path = 'images/banner/%s.jpg' % self.day
        banner.save(file_path)
        return file_path

    def __call__(self):
        path = self.__create_tag()
        return self.__place_message_on_banner(path)

if __name__ == "__main__":
    image = MakeImage(day=457, dimension=[1000, 500], bgcolor='white', banner='images/banner.jpg')
    print(image())
            