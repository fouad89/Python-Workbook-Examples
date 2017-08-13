
# coding: utf-8

# In[ ]:

#EX81
'''generate a file of genric usernames, check if username exists already or not,
then ask for a password with a certain criteria'''
'''with open ('usernames2.txt','w') as f:
    for i in range(10):
        user=('user%s\n'%i)
        f.write(user)'''
with open('usernames1.txt','r') as file:
    lines=file.readlines()
    correct_line=[line.rstrip(' \n') for line in lines]# to strip lines from \n and append to new list
while True:
    user_name=input('Enter your username: ')
    if not user_name in correct_line:
        print('good')
        break
    else:
        print('please try again:')
while True:
    password=input('Enter your password: ')
    error_list=[]
    if not any(i.isdigit() for i in password):
        error_list.append('No numbers, please try again')
    if not any(i.isupper() for i in password):
        error_list.append('No upper case, please try again')
    if len(password)<5:
        error_list.append('too short')
    if len(error_list)==0:
        print('successful')
        break
    else:
        for error in error_list:
            print(error)


# In[ ]:

#EX85 data cleaning. 
'''
retrieve a file with country names inside it. clean the data inside that file and return a list of all countries.
'''
with open('countries-raw.txt','r') as file:
    content=file.readlines()
content=[i.strip('\n') for i in content if '\n' in i]
content=[i for i in content if i!='']
content=[i for i in content if i!='Top of Page']
content=[i for i in content if len(i)!=1]
#print (content)

with open('countries-raw2.txt','w') as f:
    for i in content:
        f.write(i+'\n')
    


# In[ ]:

#EX85 method 2
with open('countries-raw.txt','r') as file:
    content=file.readlines()
    content=[i.strip('\n') for i in content if '\n' in i]
    content=[i for i in content if i!='' and len(i)!=1 and i!='Top of Page']
print (content)


# In[ ]:

#EX86 
'''Data Checker: check if user input is a country in file or not '''
#1 take user input
#2 open file to check with. 
#3 check result

with open('countries-clean.txt','r') as file:
    country_list=file.readlines()
    country_list=[i.strip('\n') for i in country_list]
while True:
    user_input=input('enter a country to check: ')
    if user_input.title() not in country_list: #to capitalise first letter as all countries in file start with capital letter
        print('not a country')
    else:
        print(user_input.title()+' is a country')
        break


# In[ ]:

#EX87 
'''adding missing data and sorting '''
#1 open file
#2 amend list to match format before adding
#3 sorting the product
checklist=['Portugal','Germany','Spain']
checklist=[i+'\n' for i in checklist]# amend list to file format

with open('countries-missing.txt','r') as file:
    content=file.readlines()
    added_countries=sorted(content+checklist)
with open('added_countries.txt','w') as f:
    for i in added_countries:
        f.write(i)


# In[ ]:

#EX88 
'''Create a script that uses the attached countries_by_area.txt
file as data source and prints out the top 5 most densely populated countries.'''

import pandas
data=pandas.read_csv('countries-by-area.txt')
data['density']=data['population_2013'] /data['area_sqkm'] # finding density from csv file
data=data.sort_values(by='density', ascending=False) # sorting countries by density
data=data.drop('rank',axis=1)
print(data[:5])
data.to_csv('new_countries-by-area.txt')
for index, row in data[:5].iterrows():
    print(row['country'])


# In[ ]:



