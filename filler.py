from bs4 import BeautifulSoup 
import os
import re
htmlToAdd =''

dir = 'D:/Programme/arthurmrtl.github.io/images/pdlv'
for filename in os.listdir(dir):
    if(filename != 'icon'):
        fileCrop = filename.split('.')
        htmlToAdd = htmlToAdd + """
    <div class="col-sm-6 col-md-4 col-lg-3 col-xl-3 item" data-aos="fade" data-src=images/pdlv/"""+filename+""" ">
        <a href="#"><img src="images/pdlv/icon/"""+fileCrop[0]+'_crop.'+fileCrop[1]+""" "class="img-fluid"></a>
    </div>"""

base = os.path.dirname(os.path.abspath(__file__))

html = open(os.path.join(base, 'D:/Programme/arthurmrtl.github.io/car_pdlv.html'))

soup = BeautifulSoup(html, 'html.parser')

div = soup.find("div", {"id": "last"})
div.insert_after(htmlToAdd)

with open('D:/Programme/arthurmrtl.github.io/car_pdlv.html', "wb") as f_output:
    f_output.write(soup.prettify("utf-8",formatter=None))


