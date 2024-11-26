# Import Module
from bs4 import BeautifulSoup
import os

f=open("questions.xml",errors="ignore")
HTML_DOC =f.read()
f.close()

# Function to remove tags
def remove_tags(html):

    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()

    # return data by retrieving the tag content
    ss=' '.join(soup.stripped_strings)
    f=open('sk.html','w')
    f.write(ss)
    f.close()
    #---------------------------------------
    os.system('sk.html')
    
# Print the extracted data
remove_tags(HTML_DOC)


