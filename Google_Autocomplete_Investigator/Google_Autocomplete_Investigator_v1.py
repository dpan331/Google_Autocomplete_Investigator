"""
Google AutoComplete Investigator

created by Dimitrios Panourgias
June 2020
"""

import requests
import pandas as pd
import xml.etree.ElementTree as ET

# Read the list of queries you want to investigate via autocomplete
df = pd.read_csv('seedQueryList.csv', header=None)
queryList = df[0].tolist()

# Choose simple or extensive search
# Simple tests only the query in the Google Search bar and retrieves autocomplete suggestions
# while extensive tests the query along with each letter of the alphabet of your choice (gr/en/de)
search_type = input('Please choose type of search (input: simple/extensive): ')
if search_type == 'extensive':
    lang = input('Please choose a language for extensive search (input: gr/en/de): ')

list_0 = queryList
list_gr = [" ", "α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ρ", "σ", "τ", "υ",
          "φ", "χ", "ψ", "ω"]
list_en = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
          "u", "v", "w", "x", "y", "z"]
list_de = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "z",
          "ü", "ä", "ö", "y", "w", "x"]
list_0_gr = [f"{i} {j}" for i in list_0 for j in list_gr]
list_0_en = [f"{i} {j}" for i in list_0 for j in list_en]
list_0_de = [f"{i} {j}" for i in list_0 for j in list_de]

resultsList = []
if search_type == 'simple':
    for x in list_0:
        apiurl = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=de&q=" + x
        r = requests.get(apiurl)
        tree = ET.fromstring(r.text)

        for child in tree.iter('suggestion'):
            x = child.attrib['data']
            resultsList.append(x)
else:
    if lang == 'gr':
        for x in list_0_gr:
            apiurl = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=de&q=" + x
            r = requests.get(apiurl)
            tree = ET.fromstring(r.text)

            for child in tree.iter('suggestion'):
                x = child.attrib['data']
                resultsList.append(x)
    elif lang == 'en':
        for x in list_0_en:
            apiurl = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=de&q=" + x
            r = requests.get(apiurl)
            tree = ET.fromstring(r.text)

            for child in tree.iter('suggestion'):
                x = child.attrib['data']
                resultsList.append(x)
    else:
        for x in list_0_de:
            apiurl = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=de&q=" + x
            r = requests.get(apiurl)
            tree = ET.fromstring(r.text)

            for child in tree.iter('suggestion'):
                x = child.attrib['data']
                resultsList.append(x)

results = pd.DataFrame(resultsList)
results.to_csv('resultsAutocomplete.csv')