from PIL import Image
import os

def create_icon(path, filname,):
    image = Image.open(path+'/'+filename)
    new_size = (2613, 3934)
    image.thumbnail(new_size, Image.ANTIALIAS)
    image = image.convert("RGB")
    name = filname.split('.')
    image.save(path+'/icon/'+name[0]+'_crop.'+name[1], "JPEG", quality=30)
    
def compresor(path, filname,):
    image = Image.open(path+'/'+filename)
    image = image.convert("RGB")
    image.save(path+'/'+filname, "JPEG", quality=70)


dir = 'D:/Programme/arthurmrtl.github.io/images/plane'
for filename in os.listdir(dir):
    if(filename != 'icon'):
        compresor(dir,filename)
        create_icon(dir,filename)
        
