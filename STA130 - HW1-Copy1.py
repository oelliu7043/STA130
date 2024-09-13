#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1
import pandas as pd
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-05-05/villagers.csv"
df = pd.read_csv(url)
df


# In[14]:


# 2
rows, columns = df.shape
rows, columns


# In[ ]:


# 3
# Observations are essentially the rows of the data set, which is each instance of data, or in this case, villagers
# Variables are essentially the columns of the data set, which is each attribute that describes the villagers, such as 
# name, gender, species


# In[6]:


df.describe()


# In[7]:


df['song'].value_counts()


# In[15]:


url1 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df1 = pd.read_csv(url1)
df1


# In[28]:


df1.shape


# In[10]:


df1 = df1.dropna()
df1.describe()


# In[29]:


df1


# In[13]:


df1.columns


# In[32]:


df1 = df1.dropna()
df1.shape
df1


# In[ ]:


# 4
# (a) The columns reported in df.describe() is only 6 (survived, pclass, age, sibsp, parch, fare), as opposed to 
# the 15 given by df.shape

# (b) df.describe() counts the number of values in each column and reports it to count
# However, in the age column that has missing values, it returns a count of only 714
# Additionally, it states that count of survived is 891, which is the number of rows that have a survived value, however it 
# is not accurate to the data to say that all of the passengers survived, as 0 means that they did not survive


# In[ ]:


# 5
# An attribute, which does not require (), is a value associated to a data frame that requires no calculations to find, it
# is simply part of the object
# A method requires calculations to figure out details regarding an object or data frame's data, such as finding the mean
# The method needs to go through the data and calculate in order to return a value, unlike an attribute like number of 
# columns, which is a known value that requires no calculations to find


# In[ ]:


# 6
# Count gives the number of valid entries that is in the data frame
# Mean is the average of all the numbers in the column. This works because df.describe() only takes the columns with
# numerical values
# Std, or standard deviation, is a value that measures the spread of data. Higher std means further spread from the mean,
# lower std means smaller spread from the mean
# Min gives the smallest value that is found in the column
# 25%, 50%, 75% return the value of the data at each Quartile, which is just ordering the data from lowest to highest and
# looking at the number that is at the first quarter, half way through (median), and third quarter
# Max gives the largest value that is found in the column


# In[12]:


# 7
# 1. df.dropna() could be used in a case where there are some rows have missing values, but the rest of the rows have
# complete information. This means that most of the data can be preserved while getting rid of the few rows that have
# invalid data and will not work in the overall data analysis. For example, if a list of 100 people only has 5 people who
# have a lot of missing data, df.dropna() would remove the 5 that have insufficient data

# 2. del df['col'] could be more useful in a case where an entire column has too many missing values to the point where it
# is useless. For example, if there is a table with a list of 100 peoples names, age, gender, and alive status, but only 3
# people have their age listed, there isn't enough data on the ages for it to be useful, and deleting the entire age column 
# could be a better solution for the data analysis. On the other hand, if we were to use df.dropna() in this case, all but 3
# rows would be invalid.
# df.dropna() is better if a row is missing more data, while del df['col'] is better if a column is missing more data

# 3. If a data frame has an entire row of missing data, then applying df.dropna() will remove every single row, rendering 
# the data useless. However, if del df['col'] is used on the column before applying df.dropna(), most of the data will
# remain, except for the rows that have other missing data

# 4. Using just df.dropna(), the number of rows goes down to 182, as many rows are missing the age value, however by using
# del df['age'] first, we are able to keep 201 rows, as 19 of the rows deleted at first only had the age value missing
import pandas as pd
url1 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df1 = pd.read_csv(url1)
del df1['age']
df1 = df1.dropna()
df1.describe()


# # https://chatgpt.com/share/66e39134-4414-8012-aa77-6932467b665d

# In[16]:


# 8
# 1. df.groupby("col1")["col2"].describe() does 3 things
# Firstly, it groups the data frame by whatever "col1" is.
# Secondly, after grouping the data by "col1", it looks at the values associated with "col1" in "col2"
# Lastly, the describe funtion does the same as it would to a standard data frame, giving the statistics of this smaller section
# For example, if there was a giant list of names and ages, making col1 the names and col2 the ages, it would group all the
# people with the same name into a group, and display the statistics of all their ages
# Let's say that there are 3 Johns aged 11, 14, and 78
# the ("col1") takes their names a groups them into one group, as they share the same name
# the ["col2"] looks at their ages, rather than other attributes that may be in the data frame
# the describe outputs the statistics of their ages, such as the mean (34.33), min (11), max (78), and so on
import pandas as pd
url2 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df2 = pd.read_csv(url2)
df2.groupby("survived")["age"].describe()
# in this case, we are sorting the people into survived and not survived, and then looking at their ages and displaying those
# statistics

# 2. df.describe() and df.groupby("col1")["col2"].describe() may have different values in their count value depending on the
# missingness present in the original data because of the order in which they operate
# df.describe() removes all data that has missing values, and then looks at the remaining data, while
# df.groupby("col1")["col2"].describe() first groups the data by "col1", looks at their associated "col2", and only removes 
# data points that have missing "col2" data. This leads to more data being potentially lost in df.describe as opposed to
# df.groupby("col1")["col2"].describe()


# In[1]:


# 3A. 
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
df
# ChatGPT was able to find the problem immdediately and give a straight answer, while Google brought me to stackoverflow, in
# which I had to look around at other peoples' code and answers before finding the solution


# In[2]:


# 3B. 
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanics.csv"
df = pd.read_csv(url)
df
# ChatGPT tells me that the url string I pasted in was wrong, and that it should be titanic.csv, not titanics
# However, when I paste my code and error message into Google, it doesn't give me any answers, and if I only paste my error
# message, Google brings me back to stackoverflow, in which I am shown other peoples' code, problems, and solutions, which are
# not entirely related to my issue
# Even with other typos in variable names and whatnot, ChatGPT is able to accurately find the problem and give me the correct
# code that runs properly


# In[4]:


# 3C. 
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
DF.describe()
# Just like 3B, ChatGPT is able to immediately find the issue while Google brings me to the same stackoverflow page


# In[5]:


# 3D. 
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url
df
# This problem is immediately found by the compiler, telling me that the ( was never closed. 
# ChatGPT is able to give me the correct code along with finding the issue, and Google gives me the solution to the problem 
# of "SyntaxError: '(' was never closed"


# In[6]:


# 3E. 
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
df.describle()
# This problem is immediately found by the compiler, telling me that the "'DataFrame' object has no attribute 'describle'"
# ChatGPT is able to give me the correct code along with finding the issue, and Google brings me to a page similar to my issue,
# but not exactly what I'm looking for


# In[9]:


# 3F. 
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
df.groupby("Sex")["age"].describe()
# ChatGPT tells me what I did wrong and gives me the correct code, while Google isn't able to help me with this case


# In[10]:


# 3G. 
import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
df.groupby("sex")[age].describe()
# The compiler instantly tells me that the name age is not defined, as without the "" the compiler reads it as a variable that 
# has not been defined. ChatGPT finds the problem and fixes it, but Google brings me to a stackoverflow forum with the same
# error message but completely different context, which isn't useful in this case for fixing the issue


# In[ ]:


# 3. Overall, ChatGPT is much better at finding and fixing problems in my code as it can look at my exact code and give me a
# more personalized response, while Google can only use the error message that is given by the terminal. Google definitely
# helps you get used to the language and learn about it, but ChatGPT is able to give working code that is needed for your
# specific problems and uses.


# # https://chatgpt.com/share/66e3a3d2-79f8-8012-964b-e1e247903786

# In[ ]:


# 9. No

