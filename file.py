import urllib.request

url="http://che.org.il/wp-content/uploads/2016/12/pdf-sample.pdf"

def download_file(furl):
    response = urllib.request.urlopen(furl)
    pdf=response.read()
    pdf_str=str(pdf)
    lines=pdf_str.split("\\n")
    dest=r'file1.doc'
    fx=open(dest,'w')
    for line in lines:
        fx.write(line)
    fx.close()

download_file(url)
##Github

