
# coding: utf-8

# In[ ]:

#EX89
'''import sql database from database.db, which has a table of 50 country names with their populations
then excute sql code to print out names of countries with population more than 2000000 sq km. 
'''
import sqlite3
conn=sqlite3.connect('database.db')
cur=conn.cursor()
cur.execute("SELECT country FROM countries WHERE area>=2000000")
rows=cur.fetchall()
conn.close()

for i in rows:
    print(i[0])


# In[ ]:

#EX90
'''write database file to csv file using pandas data frames'''

import sqlite3
import pandas
conn=sqlite3.connect('database.db')
cur=conn.cursor()
cur.execute('SELECT * FROM countries WHERE area>=2000000')
rows=cur.fetchall()
conn.close()
#converting to df and csv
df=pandas.DataFrame.from_records(rows)
df.columns=["Rank","Country","Area","Population"]
df.to_csv('countries_by_area.txt', index=False)


# In[ ]:

df['Area']


# In[ ]:

#EX91
'''commit changes to database by adding a new csv file'''
import sqlite3
import pandas

data=pandas.read_csv('ten-more-countries.txt')
conn=sqlite3.connect('database.db')
cur=conn.cursor()

for index,row in data.iterrows():
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row['Country'], row['Area'])) 

conn.commit()
conn.close()


# In[ ]:

#EX92 
'''count number of files in a directory= using glob'''
import glob
file_list=glob.glob1('/Users/spydermac/Desktop/Python Analytics/','*.ipynb')
print(len(file_list))


# In[ ]:

#EX93 
'''Please download the attached ZIP file. Inside the ZIP file there's a directory named subdirs.
That directory contains other directories inside. Please write a script that counts the number of
.py files contained inside subdirs and all its sub-directories.'''
import glob
file_list=glob.glob('subdirs/**/*.py', recursive=True)
print (len(file_list))


# In[ ]:

# EX94
''' Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:

https:/www.google.com
https:/www.yahoo.com
https:/www.stackoverflow.com
https:/www.pythonhow.com
Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash,
so the content looks like in the expected output.'''
with open('urls.txt') as file:
    url_list=file.readlines()
with open('urls_corrected.txt','w') as f:
    for url in url_list:
        url_remove_s=url.replace('s','',1)
        print(url_remove_s)
    
        
        #to add / at the exact position
        new_url=url_remove_s[:6]+'/'+url_remove_s[6:]
        print(new_url)
        f.write(new_url)


# In[ ]:

#EX95 
'''storing comma seperate input into file'''
def storing_words():
    word =input('Enter Values with a comma between: ')
    seperated_word=word.split(',')
    with open('user_data.txt','a+') as file:#read and append
        file.seek(0)
        for word in seperated_word:
            file.write(word+'\n')
        


# In[ ]:

storing_words()


# In[ ]:

#EX96 
'''storing data in a file and keep running until the word CLOSE is entered'''
def word_file():
    while True:
        user_input=input('Enter your word, Enter CLOSE when done: ')
        with open('user_data.txt','a+') as file:
            if user_input.upper()!='CLOSE':
                file.write(user_input+'\n')
            else:
                break
            


# In[ ]:

word_file()


# In[ ]:

def save_close_file():
    file=open('save_close_file.txt','a+')
    input_list=[]
    while True:
        
        user_input=input('Enter value or SAVE to save words, CLOSE to exit: ')
        if user_input.upper()=='SAVE':
            for i in input_list:
                file.write(i+'\n')
            file.close()
            file=open('save_close_file.txt','a+')
            input_list=[]
        elif user_input.upper()=='CLOSE':
            for i in input_list:
                file.write(i+'\n')
            file.close()
            break
        else:
            input_list.append(user_input)
            for i in input_list:
                print(i)


# In[ ]:

save_close_file()


# In[ ]:

#EX98 
'''create GUI to add words to file.'''
from tkinter import *
window=Tk()
file=open('user_gui.txt','a+')
def add():
    file.write(entry.get()+'\n') #to get file from window entry
    entry.delete(0,END)
def save():
    global file
    file.close()
    file=open('user_gui.txt','a+')
def close():
    file.close
    window.destroy()
'''
Text entry field
'''
user_value = StringVar()
entry=Entry(window,textvariable=user_value)
entry.pack
entry.grid(row=0,column=0)

'''
Add line button
'''
button_add=Button(window, text='Add Line', command=add)
button_add.grid(row=0,column=1)

button_save=Button(window, text='Save Changes', command=save)
button_save.grid(row=0,column=2)

button_close=Button(window, text='Save&Close', command=close)
button_close.grid(row=0,column=3)

window.mainloop()


# In[ ]:




# In[ ]:



