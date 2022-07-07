import pandas as pd 
import os
import sys

veg_price={
    'potato':25,
    'onion':35,
    'egg plant':55,
    'cabbage':40,
    'chilly':20
}

df_veg=pd.DataFrame(list(veg_price.items()),columns=['Vegetables','Price']) 

#print(df_veg)
os.chdir('../')
script_dir=os.path.abspath(os.path.dirname(sys.argv[0]) or '.')
file_path=os.path.join(script_dir,r'data\vegetable_prices.csv')
df_veg.to_csv(file_path,index=False)