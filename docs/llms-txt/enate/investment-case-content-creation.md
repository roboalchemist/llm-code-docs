# Source: https://docs.enate.net/enate-help/enateai/enateai/enateai-ai-analyst/ai-prompts/investment-case-content-creation.md

# Investment Case Content Creation

### Scenario Description

Create content for an investment case document which contains useful information about building a new hotel in a given location.

### Sample Files

* Hotel Performance File

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FnEJZ8MsT5CSfxQL31zHn%2FHotel-Performance%204%204.txt?alt=media&token=acc17484-addf-4466-9ef7-5f12b91ac164>" %}

### Input File Tags:

* Hotel Performance

### Output File Tags:

* AI Output Hotel File

### AI Persona Title:

* Business Analyst

### AI Persona Description:

* You are a experienced business analyst working in the hotel industry. You write detailed assessments and provide recommendations.

### Prompt Text

{% code overflow="wrap" %}

```
1- Hi, I would like you to be an expert in recommending business decisions in the leisure, particularly the hotel sector. I would like you to use this expertise to summarize and recommend investment decisions about where to build new hotels based on data that I will share with you. and i need the your recommendation in .txt file so please generate your decision in .txt file.  

2 - A good place to build a new hotel is where there is a competitor brand hotel within 3 kilometres of the location of my proposed location because this indicates that there is a market for hotel rooms within out price range. However, if there are more than 3 competitor brands of hotel within 3 kilometres of the proposed location then this is an indicator that the location may not be good for us because there is too much local competition. Please note that we are only interested in considering competitor brands as competition, unbranded hotels should not be considered competition.  

3 - In the case of too much competition, you should think about whether we should propose a different brand. If the hotel is in a location that you consider to be generally wealthy and a major city or leisure destination, then you should propose analysis of one of our more luxury brands, if it is an area you consider to be poorer then please propose one of our  less luxury brands.  

Please use the attached file {{FileTag:Hotel Performance}} and below information in your decision making. If the input file provided do not match and is not useful for analysis, please proceed with the analysis based on the data  provided within this  initial message regarding competitor hotels and provide the output file in .txt do not wait for any confirmation.  

The brand that we are proposing is Premier Inn.   

Our competitor brands to Premier Inn are Marriott, Sheraton and Hilton. Please note that brands such as ‘Double Tree by Hilton’ are not competitors to the Holiday Inn brand. 

Our own more luxury brands are Four seasons and One & Only Resorts. Our own more budget brands are Premier Inn and Wyndham Hotels.   

The town is Northampton, UK.   

The table of competitor hotels nearby is as follows.   

Competitor Brand  Distance to Proposed Location  Average Room Rate  

Hilton  		   	2  					85  

The George               	2  					90  

Delta Hotels by Marriot  	3  					70  

Beaumont House  	4  					80  

Double Tree by Hilton  	2  					70  

Ellenborough Park  	7  					300  
Please write two short paragraphs explaining the decision you recommend outlining: What decision we should make, why we should make that decision, risks that we should consider.  

5. Output -  
Give the outcome as .txt file for download and without ---- lines and correct format. 
```

{% endcode %}

### AI Creativity Level:

* Balanced
