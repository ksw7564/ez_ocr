import os
import datetime
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

input = 'input'
output = 'output'
done = 'done'
arr = os.listdir('input')
d = datetime.datetime.now()
today = str(d.year)+d.strftime("%m")+d.strftime("%d")

for folder in arr:
    files = os.listdir(input+"/"+folder)
    
    if not os.path.exists(output+"/"+today):
        os.mkdir(output+"/"+today)
        print("Directory " , output+"/"+today ,  " Created ")
        if not os.path.exists(output+"/"+today+"/"+folder):
           os.mkdir(output+"/"+today+"/"+folder)
    else:    
        print("Directory " , output+"/"+today+"/"+folder ,  " already exists")
        if not os.path.exists(output+"/"+today+"/"+folder):
            os.mkdir(output+"/"+today+"/"+folder)
        
        
    if not os.path.exists(done+"/"+today):
        os.mkdir(done+"/"+today)
        print("Directory " , done+"/"+today,  " Created ")
        if not os.path.exists(done+"/"+today+"/"+folder):
            os.mkdir(done+"/"+today+"/"+folder)
    else:    
        print("Directory " , done+"/"+today+"/"+folder ,  " already exists")
        if not os.path.exists(done+"/"+today+"/"+folder):
            os.mkdir(done+"/"+today+"/"+folder)
            
    for file in files:
        
        pdf = input+"/"+folder+"/"+file
        txt = output+"/"+today+"/"+folder+"/"+file.split('.pdf')[0]+".txt"
        backup = done+"/"+today+"/"+folder+"/"+file
        
        output_string = StringIO()
        
        print(pdf+" 변환")
        with open(pdf, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)

        with open(txt,'w', encoding='utf-8') as f:
            f.write(output_string.getvalue())
            print(txt+" 파일 생성 완료")
            
        os.rename(pdf, backup)
        print(backup+" 파일 이동 완료")
        
    os.rmdir(input+"/"+folder)

