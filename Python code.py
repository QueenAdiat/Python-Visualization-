
#### Importing necessary librabries ########### 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


# Reading data into the Pandas Dataframe

data=pd.read_csv(DataScientist.csv")  #depending on the location in the user's system ##########


# Understanding the data ######

print(data.head(15))
print(data.shape)
print(data.describe)
print(data.isnull)
print(data.isnull() .sum(). sum())  # looking for missing values 

# # Taking out unecessary columns

new_data= data.drop(columns=["Easy Apply", 'Competitors']) 

# #  Plotting Histogram of Rating and salary estimate  

new_data['Rating'].plot.hist()
plt.show()


# # Plotting pie charts #######################

# ########## Sectors ###############
Company_pie_data =new_data['Sector']
Company_pie_data.value_counts().sort_values(ascending=False).head(10).plot.pie(y="Count", autopct="%0.1f%%")
plt.axis("off")
plt.show()

# ############ Type of Ownership ######### 
Ownership_data =new_data['Type of ownership']
Ownership_data.value_counts().sort_values(ascending=False).head(10).plot.pie(y="Count", autopct="%0.1f%%")
plt.axis('off')
plt.show()

# # Plotting Word cloud  #########

# # # Word cloud for Location column ########

Location_text= " ".join(review for review in new_data['Location'].astype(str))
Location_stopwords=set(STOPWORDS)
wordcloud= WordCloud(stopwords=Location_stopwords, background_color="white").generate(Location_text)
plt.axis('off')
plt.imshow(wordcloud, interpolation='bilinear') 
plt.show()
# # ## Word cloud for description column #######

Description_text= " ".join(review for review in new_data['Job Description'].astype(str))
Description_stopwords=set(STOPWORDS)
wordcloud= WordCloud(stopwords=Description_stopwords, background_color="black").generate(Description_text)
plt.axis('off')
plt.imshow(wordcloud, interpolation='bilinear') 
plt.show()


# #  Plotting Bar charts  ##########

#  ### Bar chart for top 10 Highest rated data science jobs #### 

Lower_rating = data[data['Rating'] != "-1"]                                        # Takes out missing values 
Lower_rating = new_data.sort_values(by='Rating', ascending=False).head(10)         # Highest rated job title 
Lower_rating.drop_duplicates(subset= "Job Title", keep=False, inplace=True)        # Takes out duplicates in the column 
Lower_rating.plot(kind='bar', orientation="vertical", x= 'Job Title', y= 'Rating', figsize=[5,2], fontsize=7)
plt.show()

# # ##### Bar chart for the top 10 Lowest rated data science jobs ########

Higher_rating = data[data['Rating'] != "-1"]                                        # Takes out missing values 
Higher_rating = new_data.sort_values(by='Rating', ascending=True).head(10)         # Lowest Rated Job titles 
Higher_rating.drop_duplicates(subset= "Job Title", keep=False, inplace=True)        # Takes out duplicates in the column 
Higher_rating.plot(kind='bar', orientation="vertical", x= 'Job Title', y= 'Rating', figsize=[5,2], fontsize=7)
plt.show()

########### Top 10  companies ###########
Top_company= new_data["Company Name"].value_counts().sort_values(ascending=False).head(10)   
plt.rcParams["figure.figsize"] = (10,7)
Top_company.plot.bar(color='green')
plt.xlabel("Company Name")
plt.ylabel("Count")
plt.show()


# ####### Top locations ###########

Top_cities= new_data[new_data['Location'] != "-1"]    
plt.rcParams["figure.figsize"] = (10,7)
Top_cities["Location"].value_counts().sort_values(ascending=False).head(10).plot.bar(color='orange')
plt.xlabel("Location")
plt.ylabel("Count")
plt.show()


# ####### Plotting the company Headquaters ############
Top_hq= new_data[new_data['Headquarters'] != "-1"]  
plt.rcParams["figure.figsize"] = (10,7)
Top_hq["Headquarters"].value_counts().sort_values(ascending=False).head(10).plot.bar(color='black')
plt.xlabel("Headquarters")
plt.ylabel("Count")
plt.show()

# ##########  Plotting line graph ##############

# ## Line graph for top rated Industries  #### 

Lower_Companies = data[data['Industry'] != "-1"]                                       
Lower_companies = new_data.sort_values(by='Industry', ascending=False).head(1000)      
Lower_companies.drop_duplicates(subset= "Industry", keep=False, inplace=True)        
Lower_companies.plot(kind='line', x= 'Industry', y= 'Rating')
plt.show()

# ##### Comparing companies and industry ratings ####


Other_companies = new_data.sort_values(by='Industry',  ascending=False).head(500)      
Other_companies.drop_duplicates(subset= "Industry", keep=False, inplace=True)  
Other_companies.drop_duplicates(subset= "Sector", keep=False, inplace=True)     
Other_companies.plot(kind='line', x= 'Industry',y= 'Rating')
plt.show()


