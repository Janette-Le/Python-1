# Unemployment statistics by ethnicity, gender and regions in the UK from 2004 to 2018

### Link blog post:
Click here to be transfered to my Data Analyst **[Porfolio](https://janette-le.github.io/)**

### Official notebook
**[Official notebook](https://nbviewer.jupyter.org/github/Janette-Le/Python1/blob/main/ABC.ipynb)**

### Data source:
Data source: https://data.gov.uk/dataset/fe6c83aa-62aa-4a8c-94cc-225f47287225/unemployment-by-ethnicity

### Libraries used
- Random forest & Gradient boosting
- Pandas
- Numpy
- Plotly

### Where my idea come from?

<p align="justify">As we may all know, by the end of January 2020, Britain officially exited Europe. Thousands of politicians, economists and socialist forecasted that this event will create tremendous effects (positive and negative) on the society, labor market and the economy for both Britain and Europe.
There are many factors that affect the unemployment rate; on macroeconomic perspectives, it may be the volatility of the economy or the intervention of the government; on microeconomic perspectives, it may depend on age, gender, education level of the employee and local regional economy. This project aims to study which demographic elements have affected the unemployment trend in the UK in the last 15 years.</p>

This project is my personal final work for my Python class. As requests by my professor, he asked everyone to look for a raw dataset that is not available on Kaggle's, so I picked a dataset on data.gov.uk to execute my assignment. To prevent me from manually cleansing data columns by columns, I defined some functions in the Module file. These functions are alternative ways to save time when cleaning raw datasets, as well as sharpen algorithm logical sense. All directions and details are officially expressed on [Report](https://github.com/Janette-Le/Python-1/blob/main/Report.pdf) while executing code is in [Python scripts](https://github.com/Janette-Le/Python-1/blob/main/HoangUyen_Le_CapstoneProject.ipynb) file. For visualization supports, you can open my presentation on the [Slide](https://github.com/Janette-Le/Python-1/blob/main/Slide.pptx) file to have a more comprehensive view about my work.

### Elements
- ABC files: functions that were created and used in the projects
- HoangUyen_Le_CapstoneProject: Python notebook contains the Data analysis of the project
- Report: the official report of my project
- Slide: file can be used for presentation 

### Brief results
Random forest regression model performs better, since all its the accuracy scores (R2, MAE, MSE, RMSE) are higher than those of Gradient boosting.

About which predictor variables have the largest effect on the tendency of being unemployed among UK labor force, I create a plot of variable importance. As evidently observed, some variables which are expected to affect unemployment rate the most are year, age range and regions. Ethnicity is ranked lower in the list; this means that the ethnicity group individuals belong to does not affect their chance of getting a job offer.

Moreover, it is worthwhile to note that in this dataset, only basic personal information of employee is mentioned. Unemployment rate is also affected by academic qualifications, as well as macroeconomic factors such as the condition of global and domestic economy. The ‘Year ‘ variable is ranked at the first place in the variable importance list indicating that labor force indicators (employment/unemployment rates, etc) are highly dependent on global economy changes.

