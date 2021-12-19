import twint
import nest_asyncio
import pandas as pd

nest_asyncio.apply()

c = twint.Config()
c.Until = '2021-12-02'
c.Search = 'ethereum'
c.Store_csv = True
c.Output = "ethereum_12_01_2.csv"
c.Limit = 1000
#c.Hide_output = True

twint.run.Search(c)
