import os
import PyPDF2

def convert_pdf_to_txt(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

def convert_all_pdfs_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(directory, txt_filename)
            convert_pdf_to_txt(pdf_path, txt_path)
            print(f"Converted {filename} to {txt_filename}")


directory_path = 'PDF'
convert_all_pdfs_in_directory(directory_path)
print("All PDF files have been converted to TXT files.")
