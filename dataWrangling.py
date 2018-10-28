#INFO3401-Kexin Zhai
import pandas as pd
import numpy as np
import csv
import re

def generateCleanFile(filename, new_file):
    spam = ["app","free", "%20"]
    cleanr = re.compile('<.*?>')
    with open(filename, encoding = "ISO-8859-1") as csv_file, open(new_file, 'w') as newCSV:
        data = csv.reader(csv_file, delimiter=',')
        writer = csv.writer(newCSV, delimiter=",")
        header = next(data, None)
        writer.writerow(header)
        for row in data:
            content = row[3]
            respace = re.sub(' +', ' ',content)#remove extra space
            cleantext = re.sub(cleanr, '', respace)#remove HTML tags
            cleantext = re.sub(r'^https?:\/\/.*[\r\n]*', '', cleantext, flags=re.MULTILINE)
            result1 = cleantext.split("Check out my page")#remove Check out my page
            result1Join = ' '.join(result1)
            words = result1Join.split()
            resultwords  = [word for word in words if word.lower() not in spam] #remove spam

            result_content = ' '.join(resultwords)#content after cleaning spam
            if result_content == '':
                continue
            writer.writerow([row[0], row[1],row[2], result_content, row[4], row[5]])
            
    csv_file.close()
    newCSV.close()
    return newCSV
generateCleanFile("./dd-comment-profile.csv", "new_dd.csv")
#Notes!: GitHub desktop said the file "dd-comment-progile.csv" is too large and it caused the problem. So I removed this file.