# Google Autocomplete Investigator
Python script (back-end) created by **Dimitrios Panourgias**
<br/> June 2020

:children_crossing: *This script is not maintained, so, in time, certain operations or even the entire script may not be functional.* 

<br/> **Scope of the script:**
<br/> The script receives as input a list of queries and inputs each query in Google Search bar to finally retrieve the autocomplete suggestions.

## Python script (back-end) 
The script reads a csv (seedQueryList.csv) with queries. 
<img src="https://github.com/dpan331/Skr0utz_scraper/blob/master/skrtz_img/productsList.JPG" height="150" width="600">

Once ran, the user must input the type of search the script will perform:
<br/> **simple**: the script inputs each query alone in the Google Search bar.
<br/> **extensive**: the script inputs each query along with each letter of the alphabet of your choice (see next).

If the user chooses the extensive type of search then she/he gets asked to choose also a language (gr/en/de).

Finally, the script exports the aggregated data in a csv (resultsAutocomplete.csv).


