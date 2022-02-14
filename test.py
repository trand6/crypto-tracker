import pandas as pd
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()
data =cg.get_exchanges_list()
print(data)
df = pd.DataFrame(data, columns=['name', 'trust_score','trust_score_rank'])
df.set_index('name',inplace=True)
ranking = df.head(5)

print(ranking )



#while(tru)