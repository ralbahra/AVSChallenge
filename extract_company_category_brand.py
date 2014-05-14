# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/Users/redaal-bahrani/.spyder2/.temp.py
"""

import numpy
import pandas

path_to_csv = '/Users/redaal-bahrani/Documents/Coursework/EECS510/Project/kaggle/Acquire Valued Shoppers Challenge/transactions_reduced.csv'
data = numpy.genfromtxt(path_to_csv, dtype=None, delimiter=',', names=True)

dataframe = pandas.DataFrame(data, columns=['id','chain','dept','category','company','brand','date','productsize','productmeasure','purchasequantity','purchaseamount'])

groupby_company_category_brand = dataframe.groupby(['company','category','brand'])


for company, category, brand in groupby_company_category_brand.groups:
    tmp = groupby_company_category_brand.get_group((company, category, brand))
    ids = list(tmp['id'])
    print company, category, brand
    ids
    print len(ids)
    del ids

