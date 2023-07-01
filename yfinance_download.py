import pandas as pd
import numpy as np

import yfinance as yf

data=yf.download("^NSEI",period="5d",interval="5m")

print(data.iloc[-1])

print(data.head(5))

