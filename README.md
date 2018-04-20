# iframe-slideshow

Module rendering html file with iframe that loops thought url list and associated labels.

'''

import iframe_slideshow

# src urls
s =['https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg',
    'https://images.pexels.com/photos/356378/pexels-photo-356378.jpeg']

# Labels
l = ['Cat','Dog']

# Instantiate slidehshow
ss = iframe_slideshow.IFrameSlideshow(src_list=s, label_list=l)

# Saves to file
ss.save(filename='my_filename.html')

'''