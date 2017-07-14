========
Overview
========

The user is required to enter the article ID and processed term(s).
The API fetches the article corresponding to the Article ID that contains the processed terms entered. It then runs our
Sentiment code on the article, returning the Sentiment Score of the article with respect to each processed term.

----------------
Input and output
----------------
Input from user: article ID, processed term(s)
Output from API: Sentiment score

-----------------------
Sentiment code overview
-----------------------
Our sentiment analysis implementation takes place in two steps:

1. Feature extraction - This code takes in the article as a string and returns a dictionary. It will be in a python file
called feature_extraction.py and shall be called after the article text is extracted based on the article ID and processed terms.

2. Prediction - This code takes in the dictionary that is returned from step 1 and returns the numerical sentiment score. It
will be in a python file called predictions.py and shall be called after feature_extraction.py.

-------
Summary
-------
