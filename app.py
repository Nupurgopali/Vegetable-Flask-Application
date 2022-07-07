# Flask application that provides prices for certain vegetables

from flask import Flask
import pandas as pd
import os
import sys

app = Flask(__name__)

#os.chdir('../')
script_dir=os.path.abspath(os.path.dirname(sys.argv[0]) or '.')

vegetable_name=input('The name of the vegetable ')

@app.route('/')
def get_vegetable_price():
    veg_table=pd.read_csv(os.path.join(script_dir,r'data\vegetable_Prices.csv'))
    #print('dir',os.path.join(script_dir,r'data\vegetable.csv'))
    s=veg_table.loc[veg_table['Vegetables']==vegetable_name]['Price'].values[0]
    #print(s)
    return 'Cost of '+vegetable_name+' is '+str(s)
    
 
# main driver function
if __name__ == '__main__':
 
    app.run(debug=True)