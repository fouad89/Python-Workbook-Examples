
# coding: utf-8

# ### The Python Workbook: Solve 100 Exercises
# ### EX 50-69
# #### A Udemy course to practice python with the given ex.

# In[1]:

#EX52
'''The code is supposed to ask the user to enter their name and surname and
then it prints out those user submitted values.  Instead, the code throws a
TypeError.Please fix it so that the expected output is printed out.'''

first_name=input('Enter your first name: ')
second_name=input('Enter your second name')
print ('your first name is %s and your last name is %s ' %(first_name,second_name))


# In[2]:

#EX53 
'''print out the last name of the second employee'''

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
print(d['employees'][1]['lastName'])


# In[3]:

#EX54 
'''Modify the last name of the second employee'''
d['employees'][1]['lastName']='Smooth'


# In[5]:

#EX55  
'''Adding to Multilevel Dictionaries'''

d['employees'].append({'firstName': 'Albert','lastName': 'Bert'})


# In[7]:

#EX56 
'''Store the dictionary in a json file.'''
import json
from pprint import pprint
with open('jsonfile.json','w') as f: #open a file with the json extentions
    json.dump(d,f,indent=4, sort_keys=True) #dump dictionary d into file f with indentation



# In[ ]:

#EX57 
'''
json to dictionary
'''
with open('jsonfile.json','r') as f:
    new_dict=json.loads(f.read())
pprint(new_dict)


# In[8]:

#EX58 
'''adding a new employ to the file'''
with open('jsonfile.json','r+') as file:#read and write with r+
    new_dictionary=json.loads(file.read())
    new_dictionary['employees'].append({'firstName': 'new', 'lastName':'employee'})
    file.seek(0) #putting the cursor into the first line, so to overwrite previous dictionary
    json.dump(new_dictionary,file, indent=4, sort_keys=True)


# In[9]:

#EX59 
'''Enumerator'''
#Method 1
a=[1,2,3]
for i in range(len(a)):
    print('Item %s has index %s' %(a[i],i))
    
#Method 2 using enumerate
for index,item in enumerate(a):
    print('Item %s has index %s'%(item,index))


# In[11]:

#EX61 
'''Printing hello every two seconds'''
import time

while True:
    print ('hello')
    time.sleep(2)


# In[12]:

#EX 63
'''Create a program that once executed the programs prints Hello
instantly first, then it prints it after 1 second, then after 2, 3,
and then the program prints out the message
"End of the Loop" and stops.'''
import time
i=0
while True:
    print('hello')
    i+=1
    if i>3:
        print('End of Loop')
        break
    time.sleep(i)


# In[13]:

#EX 66+67 translator {First Method}
d= dict(weather='clima',earth='terra',rain='chuva')
def translator(word):
    if word in d:
        return d[word]
    else:
        return 'Sorry'
word=input('What is your word? ')
print(translator(word.lower()))

#Method 2
def translator2(word):
    try:
        return d[word]
    except KeyError:
        return 'Doesnt exist'
word=input(' enter word: ').lower()
print(translator2(word))


# In[ ]:



