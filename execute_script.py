import subprocess
import os
import sys

vegetable_script_dir=os.path.join(os.path.abspath(os.path.dirname(sys.argv[0]) or '.'),r'data\vegetable_Prices.csv')
subprocess.call(vegetable_script_dir, shell=True)
flask_app=os.path.join(os.path.abspath(os.path.dirname(sys.argv[0]) or '.'),r'app.py')
subprocess.call(flask_app, shell=True)