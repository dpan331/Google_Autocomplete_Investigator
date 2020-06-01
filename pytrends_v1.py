import pandas as pd
from pytrends.request import TrendReq
# Github repository of pytrends
# https://github.com/GeneralMills/pytrends#suggestions

# check workaround to overpass rate limit
pytrend = TrendReq()
df = pd.read_csv('seedQueryList.csv', header=None)

# Get Interest over Time
queryList = df[0].tolist()
pytrend.build_payload(kw_list=queryList)
intoverTime = pytrend.interest_over_time()
del intoverTime['isPartial']
intoverTime.to_csv('interestOverTime.csv')

# Get Google Keyword Suggestions
for keyword in queryList:
    suggestions = pytrend.suggestions(keyword=keyword)
    keySugg = pd.DataFrame(suggestions)
    if suggestions != []:
        print(keySugg.drop(columns= 'mid'))
    else:
        continue

# Get related queries
related = pytrend.related_queries()
# Get TOP related queries
relQueries_top = pd.DataFrame(columns=['query', 'value'])
for keyword in queryList:
    df_add = pd.DataFrame(related[keyword]['top'],columns = ['query', 'value'])
    df_add['term'] = keyword
    relQueries_top = pd.concat([relQueries_top, df_add], axis=0, ignore_index=True)
# Get RISING related queries
relQueries_rising = pd.DataFrame(columns=['query', 'value'])
for keyword in queryList:
    df_add = pd.DataFrame(related[keyword]['rising'],columns = ['query', 'value'])
    df_add['term'] = keyword
    relQueries_rising = pd.concat([relQueries_rising, df_add], axis=0, ignore_index=True)
relQueries_top.to_csv('relatedTopQueries.csv')
relQueries_top.to_csv('relatedRisingQueries.csv')
