Project: Meme Generator
========================

## 1. Goals:

1. The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes that's an image with a quote.
2. We'll be doing this projevt in a way that demonstrates the ability to build large-scale codebases. Ensduring that all of our systems are broken out into specific modules.

## 2. Implementation details:

### 2.1 Quote Engine

The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:

```text
"This is a quote body" - Author
```

This module will be composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

### 2.1.1 Quote Format

Example quotes are provided in a variety of files. Take a moment to review the file formats in ./_data/SimpleLines and ./_data/DogQuotes. Your task is to design a system to extract each quote line-by-line from these files.

The abstrat class ImporterInterface implements the can_ingest class method which decides if a file is compatible with the importer.

A parse abstract class method signature, fully complete in the children classes that implement the ImporterInterface.

The Importer class encapsulates the CSVImporter, XlsImporter, XlsxImporter, DocxImporter, TxtImporter, and the PDFImporter classes.

In Figure 1 is presented the class diagrams that describes the implementation of the strategy objects. 

<img src="./imgs/classDiagram_ImporterInterface.png">

The DocxImporter class is responsible for loading data from Docx (Microsoft Word Document) files, the CSVImporter class is responsible for loading data from CSV (Comma Separated Value) files, and the same idea applies for the file types xls, xlsx, txt, pdf.

### Dependencies: 

1. Before implementing our code, we need to install the python-docx library to work with word documents in Python. This library requires a new version of a Python helper module called setuptools. To install the updated helper and the docx library, run:
```sh
pip install -U setuptools
pip install python-docx
```
2. Before explore the code prepare a virtual environment using Python3.6+. Then proceed to install all the dependencies specified in the file requirements.txt.
3. pdftotext: Converts pdf to text (.pdf to .txt):
    - installation:
        - sudo apt install poppler-utils (Linux)
        - brew install poppler           (MacOS)
    - converts .pdf to .txt:
    ```sh
    $ pdftotext cats.pdf cats.txt
    ```