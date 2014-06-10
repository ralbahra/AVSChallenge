# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 11:52:50 2014

@author: redaal-bahrani
"""

import pandas as pd
transactions = pd.read_csv('test_transactions_reduced_2.csv')
transactions.loc[(transactions.purchasequantity > 0) & (transactions.purchaseamount < 0), 'purchasequantity'] = transactions.purchasequantity * -1
transactions.loc[(transactions.purchasequantity < 0) & (transactions.purchaseamount > 0), 'purchaseamount'] = transactions.purchaseamount * -1

sum_by_company = transactions[['id','company','purchasequantity','purchaseamount']]
sum_by_company = sum_by_company.groupby(['id','company']).sum().reset_index()
sum_by_company.to_csv('test_sum_by_company_2.csv',index=False)
del sum_by_company

sum_by_category = transactions[['id','category','purchasequantity','purchaseamount']]
sum_by_category = sum_by_category.groupby(['id','category']).sum().reset_index()
sum_by_category.to_csv('test_sum_by_category_2.csv',index=False)
del sum_by_category

sum_by_company_category = transactions[['id','company','category','purchasequantity','purchaseamount']]
sum_by_company_category = sum_by_company_category.groupby(['id','company','category']).sum().reset_index()
sum_by_company_category.to_csv('test_sum_by_company_category_2.csv',index=False)
del sum_by_company_category

sum_by_company_category_brand = transactions[['id','company','category','brand','purchasequantity','purchaseamount']]
sum_by_company_category_brand = sum_by_company_category_brand.groupby(['id','company','category','brand']).sum().reset_index()
sum_by_company_category_brand.to_csv('test_sum_by_company_category_brand_2.csv',index=False)
del sum_by_company_category_brand

sum_by_dept = transactions[['id','dept','purchasequantity','purchaseamount']]
sum_by_dept = sum_by_dept.groupby(['id','dept']).sum().reset_index()
sum_by_dept.to_csv('test_sum_by_dept_2.csv',index=False)
del sum_by_dept
del transactions