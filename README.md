# Google Autocomplete Investigator
Python script (back-end) created by **Dimitrios Panourgias**
<br/> June 2020

:children_crossing: *This script is not maintained, so, in time, certain operations or even the entire script may not be functional.* 
<br/> :space_invader: *Also the script is not tested to handle all cases and exceptions (but if you follow the inpput guidelines it shall work fine).*

<br/> **Scope of the script:**
<br/> The script receives as input a list of queries and inputs each query in Google Search bar to finally retrieve the autocomplete suggestions.

## Python script (back-end) 
The script reads a csv (seedQueryList.csv) with queries. 
<br/> <img src="https://github.com/dpan331/Keyword_research_tools/blob/master/Google_Autocomplete_Investigator/goog_autoc_img/seedQueryList.JPG" height="50" width="100">

Once ran, the user must input the type of search the script will perform:
<br/> **simple**: the script inputs each query alone in the Google Search bar (as you can see from the results shown in the image below).

<br/> <img src="https://github.com/dpan331/Keyword_research_tools/blob/master/Google_Autocomplete_Investigator/goog_autoc_img/simpleSearchResults.JPG" height="300" width="150">

<br/> **extensive**: the script inputs each query along with each letter of the alphabet of your choice (as you can see from the results shown in the image below. Observe that after each query from the seedQueryList the next word begins with a letter from the alphabet in the known order). If the user chooses the extensive type of search then she/he gets asked to choose also a language (gr/en/de).

<br/> <img src="https://github.com/dpan331/Keyword_research_tools/blob/master/Google_Autocomplete_Investigator/goog_autoc_img/extensiveSearchResults.JPG" height="400" width="200">

Finally, the script exports the aggregated data in a csv (resultsAutocomplete.csv).

## Further actions
Apart from just gazing the autocomplete results to get ideas for your keywords, you can download all the keywords you have already set up in your Google Ads ad account and merging to identify gaps. 

<br/> The same can be performed for Google Search Console queries that you rank for and can retrieve from the relevant report of the UI (User Interface).

<br/> To retrieve metrics for the autocomplete search results, simply throw them in Google Ads' keyword planner (At least until the next keyword research tool that I upload here :sunglasses:).

<br/> You can also modify the script to go even deeper in your investigation by using the retrieved (first) autocomplete search results as seed queries to be refed to the script. However keep in mind that the deeper you go the more irrelevant the results will be.

<br/> <img src="https://github.com/dpan331/Keyword_research_tools/blob/master/Google_Autocomplete_Investigator/goog_autoc_img/it-crowd-moss-fire-email.JPG" height="320" width="400">


