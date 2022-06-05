
Part 1. Question1:
##Write a regex to extract all the numbers with orange color background from the below text in italics.
{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

         CODE:
	   import re
	   s = r'{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'
	   s = re.sub(r"\:\d+", ":", s)
	   print(s)

         OUTPUT:
	  {"orders":[{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":},{"id":}],"errors":[{"code":,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}



Part1. Question2: 
##Project: Semantic analysis of chrome review that dont match with ratings.

# GOAL:
The goal of the project is to identify such ratings where review is good, but the rating is poor. So that the support team can point to this users.

# 🔗 Links
https://nextlabschrome.herokuapp.com/


# Roles and Responsibilities

* Data collection and Data processing done on the dataset 'chrome_reviews'.
* Exploratory Data Analysis done on the feature 'Text' to get cleaned such as removing extra special characters, converting to lower case, split the words and lemmatize.
* Applied sentiment polarity to find the sentiment emotion of the 'Text'.
* Classified the 'Text' into positive, neutral and negative sentiments.
* Corpus was applied with vectorization and trained the model with various classification algorithms.
* Predicted accuracy using metrics like confusion matrix and accuracy score.
* Finally the dataset is set to filter the 'Text' with positive sentiment and 'ratings' as poor. 
* Considered poor rating as ratings lesser than 3.  
* Deployed using Streamlit on 'Heroku' the cloud platform which is Platform As A Service. 

# Deployment

The Project "Semantic analysis of chrome review that dont match with ratings" is deployed using streamlit on the cloud platform "Heroku".
File uploader in streamlit is used to upload a file which has internal condition check as file uploaded must in the type of csv file only. On uploading it checks for the chrome review that is not matched with the ratings. It extracts only those mismatched records and displays on the web page.

# 🔗 Links
https://nextlabschrome.herokuapp.com/



## Part 1 Question 3

Ranking Data - Understanding the co-relation between keyword rankings with description or any other attribute.  

Suggested questions:

i)Is there any co-relation between short description, long description and ranking? Does the placement of keyword (for example - using a keyword in the first 10 words - have any co-relation with the ranking)?

        * Yes, there is co-relation between hort description, long description and ranking.
        * Yes certainly, placement of keyword with first 10 words have effect on ranking. 


ii) Does APP ID (Also known as package name) play any role in ranking?
        * Yes, having unique name will highly affect the app store ranking.

iii) Any other pattern or good questions that you can think of and answer?
        * If the app has higher rating then it has more chances for higher ranking aswell. 
        * So the app quality has to be improved.
        * Having email address, web support allows users to reach for complaints and this prevents bad reviews.
        * App uninstalls: app store tracks the app uninstallation rates inorder to assess the quality of the application.



## Part 2 

1. Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution). 


    * Being in the stream of data science, i face many challenges day by day. But i turn those challenges into my learning face which makes me a quick learner and every day am learning a new things which improves my skill sets. As am strong in my analytic thinking and logical thinking, i can solve many difficult problems.  Thinking and Linking capability makes to think on the problems and link with the possiblities and methodologies, makes me a smart Data Scientist. 


2.  Formally, a vector space V' is a subspace of a vector space V if
V' is a vector space
every element of V′ is also an element of V.
Note that ordered pairs of real numbers (a,b) a,b∈R form a vector space V. Which of the following is a subspace of V?
The set of pairs (a, a + 1) for all real a
The set of pairs (a, b) for all real a ≥ b
The set of pairs (a, 2a) for all real a
The set of pairs (a, b) for all non-negative real a,b

        * All the above properties are subspace of V
