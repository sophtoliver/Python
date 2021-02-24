# Sophia M. Toliver, CIS 345 10:30 T TH, Project

from PIL import Image

# filename = 'images/question_mark.png'
# img = Image.open(filename)
# icon_pic = img.resize((16, 16))
# icon_pic.show()
# icon_pic.save('icon_pic.ico')
#
# file = 'images/brain_img.jpg'
# img = Image.open(file)
# icon_pic = img.resize((950, 750))
# icon_pic.show()
# icon_pic.save('brain_resize.png')
#
# file = 'images/seal_of_approval_img.png'
# img = Image.open(file)
# icon_pic = img.resize((101, 76))
# icon_pic.show()
# icon_pic.save('seal_of_approval_img_resize.png')
#
# file = 'images/good_job.jpg'
# img = Image.open(file)
# icon_pic = img.resize((101, 76))
# icon_pic.show()
# icon_pic.save('good_job_resize.jpg')

file = 'images/incorrect.jpg'
img = Image.open(file)
icon_pic = img.resize((101, 76))
icon_pic.show()
icon_pic.save('incorrect_resize.jpg')
