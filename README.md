# Python-Visualization-
Visualization in Pyhton using Pandas, Numpy, Seaborn, and Matplotlib libraries

**Summary**

In this project, I applied visualisation and data analytics techniques on a dataset of 3,900 Data Science job postings using Python. The aim is to identify the top-hiring sectors, cities, and in-demand skills. I performed data cleaning and explored the data using charts (histogram, bar charts, and line charts) as well as  Natural Language Processing (NLP) techniques like Word clouds. These methods transformed the data into useful information for potential job seekers.

**Key Tools**: Python (Pandas, NumPy, Matplotlib, Seaborn).

**Key Skills**: Data wrangling, Exploratory Data Analysis, Data Visualisation.


**Methods**

1. **Data Cleaning**- Handled missing data in ‘City’, and ‘Easy Apply’ columns. Extracted City and State from ‘Location’ column.
   
2.  **Exploratory Data Analysis**
   
  •	**Univariate**- Visualised the distribution of Ratings with a Histogram.

  •	**Bivariate**- Comparing job count across sectors using bar charts.

  •	**Text analysis** -Identified common themes in skills and locations using Word Cloud 




**Flow chart for visualisation**


 
**Dataset**

The data set I used for this project is the Data Scientist dataset available here . It has 3900 rows and 17 columns and contains information on location, job descriptions, roles, and companies. The columns are listed below.


•	Job Title

•	Salary Estimate

•	Job Description

•	Rating

•	Company Name

•	Location

•	Headquarters

•	Size

•	Founded

•	Type of ownership

•	Industry

•	Sector

•	Revenue

•	Competitors

•	Easy Apply


**Questions**

1.	What is the range of job ratings for data science jobs?
  
2.	Which companies offer the most data science jobs?

3.	What cities have the highest number of data scientist jobs?
  
4.	Where are the headquarters of the companies hiring data scientists?
  
5.	What sectors employ the most data scientists? 

6.	What kind of companies (private, public, not-for-profit) hire data scientists?
   
7.	What job titles have the highest and lowest ratings?

**Key Insights** 

The histogram shows the frequency of the rating values.  This sets the tone for the rest of the analysis. It shows that the majority of the ratings in the data set are between 3 and 4. There is no zero-rating, and less than a hundred companies/jobs are rated between 1 and 2. Indicating that the data science field in competitive. 

<img width="665" height="320" alt="image" src="https://github.com/user-attachments/assets/e33dbf40-4ef0-4fbc-a878-ebca84bcfcb1" />



 
The bar chart below shows the top 10 companies that offer data scientist jobs. It shows that Apple, IBM, Amazon, and Facebook are the top 4. 

<img width="701" height="351" alt="image" src="https://github.com/user-attachments/assets/2e4955b7-cd01-4255-a7a3-c1883f06c3a2" />





 
In the figure below, the top ten cities that hire data scientists are Austin, Chicago, Sandiego, New York, Houston, Philadelphia, Los Angeles, Dallas, Antonia, and Phoenix 


<img width="936" height="461" alt="image" src="https://github.com/user-attachments/assets/1f970533-715b-4fd8-820d-4cc79dd7eba6" />





From the bar chart below, it can be inferred that most companies that hire data science have their headquarters located in New York, San Diego, Chicago, Austin, Los Angeles, Houston, San Antonio, Philadelphia, Armonk, and Irving. 


<img width="797" height="516" alt="image" src="https://github.com/user-attachments/assets/b9a4d92c-cbfe-4acc-8da4-882bd0ef6e66" />




 
In the pie chart below the sector popularity for data science jobs can be determined easily; Business services and information technology companies are the biggest employers of data scientists, representing 32.2% and 19.5%. This is more than half of the top 10 sectors employing data scientists while Pharmaceuticals, finance, and healthcare sectors are also top employers of data scientists, represented by 8.4, 7.7, and 5.6% respectively. 


<img width="820" height="578" alt="image" src="https://github.com/user-attachments/assets/7937cc15-f9d5-4064-8817-b424cd035a89" />




 
Nearly half of the companies that employ data scientists are privately owned companies, while 28.7% are publicly owned companies, 5.3% are not for profit organizations, 2.3% are government companies, and 0.4% are hospitals.

The bar chart shows the top seven highest-rated data science job titles in the data set. It shows that SQL Data Engineers, Data Analyst Assistants, Machine Learning Engineer, and Junior Data Analysts are scored the maximum rating of 5. Indicating that the perceived value of these jobs is high. 

<img width="881" height="277" alt="image" src="https://github.com/user-attachments/assets/dce41627-5353-4b60-8e1c-e5f44207adf8" />


 

Figure 6: Highest rated data professions

The bar chart above shows the lowest-rated job titles. Data Analyst, Research Scientist, Business Analyst and Research Scientist were among the jobs with the lowest possible ratings between zero and -1. 

<img width="728" height="249" alt="image" src="https://github.com/user-attachments/assets/d7926673-5fdc-476c-96d9-660eaffa2f88" />


 
Figure 7: Lowest-rated data jobs


The results show that the self-storage service industry is among the top-rated for data science jobs. It also shows that religious organizations and Museums are not rated highly in terms of data science jobs.


<img width="975" height="204" alt="image" src="https://github.com/user-attachments/assets/abebfc64-9652-4876-b1f2-009f8f9710f6" />

 
Figure 8 Ratings by industry

The word cloud shows the top occurring locations for the job. It shows that Austin, California, and San Francisco are the top locations for data science jobs.  
<img width="975" height="204" alt="image" src="https://github.com/user-attachments/assets/87da481d-fe57-41d1-a18c-ff64b60650c3" />

 
Figure 9 Word cloud of Data Science job Locations


Word cloud analysis reveals that the top occurring words in job descriptions for data science,among other things are experience, teamwork, ability, machine learning. 

 <img width="770" height="388" alt="image" src="https://github.com/user-attachments/assets/4c0279aa-d1a2-42d2-82ba-179645eff9aa" />

Figure 10 Word cloud of data science job description

**Recommendations**. 

•	The high company and job ratings are an indication that the data science field is lucrative since most ratings were over 3. 

•	Analysis of top locations, top employers, and headquarters shows that the United States has the highest demand for data scientists. International students have a higher chance of getting jobs after graduation. Universities in key cities such as New York, San Diego and Texas could enhance their data science programs, offer short courses, and increase enrolment. 

•	Word cloud analysis highlights the importance of soft skills, particularly teamwork and experience working on teams. Job seekers should emphasize these skills on their CV and build them through volunteering, joining clubs, and societies. 

