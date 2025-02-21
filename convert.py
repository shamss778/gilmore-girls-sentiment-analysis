import PyPDF2
import csv
import os


def pdf_to_csv(pdf_path, csv_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Page", "Line", "Text"])

            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                lines = text.split("\n")

                for line_num, line in enumerate(lines, 1):
                    writer.writerow([page_num + 1, line_num, line.strip()])

    print(f"PDF converted to CSV: {csv_path}")


# Usage
pdf_folder = "PDF"
output_folder = "CSV"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, filename)
        csv_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.csv")
        pdf_to_csv(pdf_path, csv_path)
