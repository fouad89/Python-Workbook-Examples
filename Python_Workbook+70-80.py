
# coding: utf-8

# In[ ]:

#EX73 
'''Create a script that reads this file, multiplies its values by two and saves the output in a new text file.'''
import pandas as pd
data=pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2=data*2
data2.to_csv("sampledata_x_2.txt", index=None)


# In[ ]:

#EX74 
'''concatinate two files'''
import pandas as pd
#first step: read data as csv
#2nd: concatinate both files
#3rd: write to csv file
data=pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data1=pd.read_csv("sampledata_x_2.txt")
concat_data=pd.concat([data,data1])
concat_data.to_csv('concat_file.txt', index=None)# to stop index from writing to file. Otherwise the index arg is not needed


# In[ ]:

#EX75 
'''Plot the data'''
#to show graph in notebook

get_ipython().magic('matplotlib inline')
#Steps:
##1. read data file
##2. using matplotlib to add the plot
import pandas as pd
import matplotlib.pylab as plt
my_data=pd.read_csv('concat_file.txt')
my_data.plot(x='x',y='y',kind='scatter')


# In[ ]:

#EX75 
'''Plot using bokeh'''
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
output_file("bokeh_plot.html")
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
f = figure()
f.circle(x=data["x"], y=data["y"])
show(f)


# In[ ]:

#EX76 
'''print out todays date'''
from datetime import datetime
# %A  would extract the day, %B  the month, %d  the date, and %Y
print(datetime.now().strftime("Today is %A, %B, %d, %Y")) 


# In[ ]:

#EX77 
"""Create a script that asks the user to enter their 
age and the script calculates the user's year of birth and prints it out in
a string like in the expected output. Please make sure you generate the current year dynamically."""
#1. user input: age
#2. calculate years and output the year of birthh
from datetime import datetime
user_input=input('How old are you? ')
current_date=datetime.now().strftime('%Y') # or datetime.now().year, which will give an int straight away, no need to convert
year_of_birth=int(current_date)-int(user_input) 
print ('You were born in %s' %year_of_birth)


# In[ ]:

#EX78 
'''genereate a password of length 6'''
import random
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
random_letters=random.sample(characters, 6)
password=''.join(random_letters)
print(password)


# In[ ]:

#EX79
'''generate a password with specific criteria'''
'''CreatZero <I>t least 5 characters. If the conditions are generated,
print out "Password is fine", otherwise keep prompting the user for a password.'''
#1. user input
#2. set criteria
#3. check if criteria is satisfied

while True:
    user_input=input('Enter your password: ')
    #investigate any function
    if any(i.isdigit() for i in user_input) and any(i.isupper() for i in user_input) and len(user_input)>=5:
        print('Password accepted! ')
        break # end of while loop 
    else:
        print('please try again... ')
        


# In[ ]:

# EX 80 generate password with one capital letter
'''Create a program asks the user to enter a new password and check that the
submitted password should contain at least one number, one uppercase letter and at least 5 characters.
If the conditions are generated, 
print out the reason why pointing to the specific condition/s that has not been satisfied.
'''
#1. request input
#2. generate feedback if missing any of the criteria
#3. list the feedbacks.
#4. keep running until achieved
while True:
    notes_list=[]
    user_input=input('Enter Your Password: ') # user input
    if not any(i.isdigit() for i in user_input): #check if it has at least one number
        notes_list.append('You need at least one number! ')
    if not any(i.isupper() for i in user_input):#check if it has at least one upper case
        notes_list.append('Upper case missing')
    if len(user_input)<5:# longer than 5
        notes_list.append('at least five letters')
    if len(notes_list)==0:# by checking the list, if the user_input generated in of the above msgs, this will be skipped
        #program ends here if notes_list is empty
        print('Successful password')
        break
    else:
        print('Reasons: ')
        for note in notes_list:
            print(note)


# In[ ]:



