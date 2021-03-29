# Program to split and merge PDFs via a GUI.

import PyPDF2
import glob
import os
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger, pdf
from tkinter import *
from tkinter import ttk


def splitter(path):
    """
    This function splits a pdf at the desired point.

    Currently this splits every page. Need to add a function to choose specifc pages/page range.
    """

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
    """
    This function merges one file with another.

    Need to add a functionality to elect the order, and save location.
    """
    output = PdfFileMerger()
    output.append(file1)
    output.append(file2)
    output.write('Merged.pdf')
    # Use the append function to define the page numbers to add?

if __name__ == "__main__":
    # This sets up the main application window.
    root = Tk()
    root.title("PDF Splitter / Merger")

    # Creating a content frame via a frame widget.
    mainframe = ttk.Frame(root, padding = " 3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe['borderwidth'] = 2
    mainframe['relief'] = 'sunken'
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Merge:").grid(column=2, row=1, sticky=(N,W))

    merge_file_1 = StringVar()
    merge_file_2 = StringVar()

    merge1_entry = ttk.Entry(mainframe, width=20, textvariable=merge_file_1)
    merge2_entry = ttk.Entry(mainframe, width=20,textvariable=merge_file_2)

    merge1_entry.grid(column=2, row=2, sticky=(W, E))
    merge2_entry.grid(column=2, row=3, sticky=(W, E))



    root.mainloop()



    # merger(merge_file_1, merge_file_2)

    # file_to_split = ""

    # splitter(file_to_split)
