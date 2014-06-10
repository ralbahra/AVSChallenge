# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 17:54:11 2014

@author: redaal-bahrani
"""

import pandas as pd

sum_by_company_1 = pd.read_csv('data/testing_sums/test_sum_by_company_1.csv')
sum_by_company_2 = pd.read_csv('data/testing_sums/test_sum_by_company_2.csv')
sum_by_company = sum_by_company_1.append(sum_by_company_2)

sum_by_category_1 = pd.read_csv('data/testing_sums/test_sum_by_category_1.csv')
sum_by_category_2 = pd.read_csv('data/testing_sums/test_sum_by_category_2.csv')
sum_by_category = sum_by_category_1.append(sum_by_category_2)

sum_by_company_category_brand_1 = pd.read_csv('data/testing_sums/test_sum_by_company_category_brand_1.csv')
sum_by_company_category_brand_2 = pd.read_csv('data/testing_sums/test_sum_by_company_category_brand_2.csv')
sum_by_company_category_brand = sum_by_company_category_brand_1.append(sum_by_company_category_brand_2)

test_history = pd.read_csv('data/testHistory.csv')
offer = pd.read_csv('data/offers.csv')

test_history_offer = pd.merge(test_history, offer, on = ['offer'], how = 'left')

testing_data_1 = pd.merge(test_history_offer, sum_by_company, on = ['id','company'], how = 'left')
testing_data_1.rename(columns={'purchasequantity': 'pq_company', 'purchaseamount': 'pa_company'},inplace=True)
testing_data_2 = pd.merge(test_history_offer, sum_by_category, on = ['id','category'], how = 'left')
testing_data_2.rename(columns={'purchasequantity': 'pq_category', 'purchaseamount': 'pa_category'},inplace=True)
testing_data_3 = pd.merge(test_history_offer, sum_by_company_category_brand, on = ['id','company','category','brand'], how = 'left')
testing_data_3.rename(columns={'purchasequantity': 'pq_company_category_brand', 'purchaseamount': 'pa_company_category_brand'},inplace=True)

testing_data = pd.merge(testing_data_1, testing_data_2, on = ['id','company','category','brand'], how = 'left')
testing_data.drop(['chain_y','offer_y','market_y','offerdate_y','quantity_y','offervalue_y'],inplace=True,axis=1)
testing_data.rename(columns={'chain_x': 'chain','offer_x': 'offer','market_x': 'market','offerdate_x': 'offerdate','quantity_x': 'quantity','offervalue_x': 'offervalue'},inplace=True)
testing_data = pd.merge(testing_data, testing_data_3, on = ['id','company','category','brand'], how = 'left')
testing_data.drop(['chain_y','offer_y','market_y','offerdate_y','quantity_y','offervalue_y'],inplace=True,axis=1)
testing_data.rename(columns={'chain_x': 'chain','offer_x': 'offer','market_x': 'market','offerdate_x': 'offerdate','quantity_x': 'quantity','offervalue_x': 'offervalue'},inplace=True)

#training_data = training_data.fillna(value = -999)

testing_data.to_csv('data/testing_features.csv',index=False)


