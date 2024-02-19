
from pdf2image import convert_from_path

for f in range(17):
    pages = convert_from_path('./assets/certficates/certificate'+str(f)+'.pdf')
    print("Converting", f, "file ...",'./assets/certficates/certificate'+str(f)+'.pdf')

    for i in range(len(pages)):
        pages[i].save('./assets/certficates/certificateimg/page'+ str(f) +'.jpg', 'JPEG')
        print("Converted", f, "file ...")