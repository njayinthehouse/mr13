# To convert a list of images into a pdf
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image, PageBreak
from reportlab.lib.units import inch

# PathList * Path * String -> Path
def convert(images, path, filename):
    filepath = os.path.join(path, filename)
    doc = SimpleDocTemplate(filepath, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    width = 7.5 * inch
    height = 9.5 * inch

    def story(images, acc):
        if images == []:
            return acc
        else:
            pic = Image(images[0], width, height)
            acc.append(pic)
            acc.append(PageBreak())
            return story(images[1:], acc)

    doc.build(story(images, []))
    return filepath
