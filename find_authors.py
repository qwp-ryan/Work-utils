import csv
import os

with open('authors.csv', 'r') as csvfile:
    with open('result.csv','a') as writer:
        reader = [each for each in csv.reader(csvfile, delimiter = ';')]
        line = 1
        
        for row in  reader:
            be = False
            for authors in row:
                with open('target.csv','r') as targ_csv_file:
                    target = csv.reader(targ_csv_file, delimiter= "\n")
                    for name in target:
                        _name=''.join(name)
                        _authors=''.join(authors)
                        if _name in _authors: be=True
            #if be: print("有文章的%d"%line)
            if be: 
                writer.write('1\n')
                print("有文章的%d"%line)
            else:
                writer.write("0\n")
            line=line+1
