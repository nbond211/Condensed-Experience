from PIL import Image


def get_colors(infile, numcolors=5, resize=150):
    image = Image.open(infile)
    image = image.resize((resize, resize))
    result = image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
    result.putalpha(0)
    colors = result.getcolors(resize * resize)

    return colors
