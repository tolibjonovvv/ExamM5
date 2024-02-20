import pdfkit
import threading
import os

print("PDF fayllar saqlanayotgan papka:", os.path.abspath('pdflar'))

base_url = 'http://tilshunos.com/paronims/'
path_wkpdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

config = pdfkit.configuration(wkhtmltopdf=path_wkpdf)
def web_2_jpg(i):
    pdfkit.from_url(base_url + str(i),
                 'pdflar/' + str(i) + '.pdf', configuration=config)
    print(f"page-{i} saved!")

def main():
    threads = []

    for i in range(1, 11):
        t = threading.Thread(target=web_2_jpg, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()