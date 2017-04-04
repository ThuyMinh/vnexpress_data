import csv
import re
import string

def authorNameRemove(s):
    '''(str) -> str'''
    lastDot = s.rfind('.')    
    return s[:lastDot]

def htmlTagRemove(s):
    '''(str) -> str'''
    s = re.sub('''/<("[^"]*"|'[^']*'|[^'">])*>/''', ' ', s)
    return s

def specialCharRemove(s):
    '''(str) -> str'''
    s = re.sub(r'[^\w\s]',' ', s)
    s = re.sub('  ',' ', s)
    return s

with open('vnexpress_data.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for i,row in enumerate(reader):
        content = row['content']        
        title = row['title']        

        content = authorNameRemove(content)
        content = htmlTagRemove(content)
        content = specialCharRemove(content)        

        print(content)
        if(i >1): break
        
                        
