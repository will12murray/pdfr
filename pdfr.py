import PyPDF2
import glob
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger


def getInfo(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        numPages = pdf.getNumPages()

    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title

    return info, author, creator, producer, subject, title


def textExtractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        # Get the first page
        page = pdf.getPage(0)
        ptype = str(type(page))
        text = page.extractText()

        return page, ptype, text


def pdfSplitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        writer = PdfFileWriter()
        writer.addPage(pdf.getPage(page))

        output_fname = f'{fname}_page_{page+1}.pdf'

        with open(output_fname, 'wb') as out:
            writer.write(out)

    print(f'Created : {output_fname}')


def merger(file1, file2):
    output = PdfFileMerger()
    output.append(file1)
    output.append(file2)
    output.write('Merged.pdf')
    # Use the append function to define the page numbers to add?


def extractor(path, pageRange, newTitle):
    """
    Page extractor.
    path = original file path (adda merge element to this?)
    pageRange = pass either a tuple of a range of pages or a list of individual pages to be in the new pdf.
    newTitle = new PDF title
    """

    # Filepath should be a user defined variable that declares where the new file will be saved.
    filePath = '/Users/willmurray/Google Drive/Coding/pdfr/res'
    pdf = PdfFileReader(path)
    writer = PdfFileWriter()

    if type(pageRange) is tuple:
        for page in range(pageRange[0]-1, pageRange[1]):
            writer.addPage(pdf.getPage(page))

            with open(filePath + "/" + newTitle, 'wb') as f:
                writer.write(f)

        print(
            f'Created {newTitle} from {os.path.basename(path)}, in {filePath}.')

    if type(pageRange) is list:
        for page in pageRange:
            page -= 1
            writer.addPage(pdf.getPage(page))

            with open(filePath + "/" + newTitle, 'wb') as f:
                writer.write(f)

        print(
            f'Created {newTitle} from {os.path.basename(path)}, in {filePath}.')


if __name__ == '__main__':
    # path1 = '/Users/willmurray/Google Drive/Coding/pdfr/res/17709-1609866376.pdf'
    # path2 = '/Users/willmurray/Google Drive/Coding/pdfr/res/SID_RNAV_RWY25_DEPS'

    m1 = '/Users/willmurray/Desktop/Ballpark method.pdf'
    m2 = '/Users/willmurray/Desktop/ETP.pdf'
    # info, author, creator, producer, subject, title = getInfo(path2)
    # print(f"Info = {info}")
    # print(f"Author = {author}")
    # print(f"Creator = {creator}")
    # print(f"Producer = {producer}")
    # print(f"Subject = {subject}")
    # print(f"Title = {title}")

    # page, ptype, text = textExtractor(path2)
    # print(f"Page = {page}")
    # print(f"Type = {ptype}")
    # print(f"text = {text}")

    # pdfSplitter(path)

    # outputfolder = '/Users/willmurray/Google Drive/Coding/pdfr/res'
    merger(m1, m2)

    # extractor(path1, [1, 2, 3], "SID_RNAV_RWY25_DEPS")
