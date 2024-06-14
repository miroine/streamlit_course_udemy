from ucimlrepo import fetch_ucirepo
import pandas as pd 
import numpy as np


def get_data_from_uci(id=529, tag ='original'):  
# fetch dataset 
    s = fetch_ucirepo(id=529)  
    return pd.DataFrame(s['data'] [tag])



  


