import os
import sys
import argparse
import pandas as pd

ls=[]
with open("Emp details.txt",'r+') as rf:
    for x in rf:
        st=x.strip('\n')
        ls.append(st.split(','))
    print (ls[1])    
        
