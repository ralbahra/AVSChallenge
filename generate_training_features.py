# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 17:54:11 2014

@author: redaal-bahrani
"""

import pandas as pd

sum_by_company_1 = pd.read_csv('data/sums/sum_by_company_1.csv')
sum_by_company_2 = pd.read_csv('data/sums/sum_by_company_2.csv')
sum_by_company = sum_by_company_1.append(sum_by_company_2)

sum_by_category_1 = pd.read_csv('data/sums/sum_by_category_1.csv')
sum_by_category_2 = pd.read_csv('data/sums/sum_by_category_2.csv')
sum_by_category = sum_by_category_1.append(sum_by_category_2)

sum_by_company_category_brand_1 = pd.read_csv('data/sums/sum_by_company_category_brand_1.csv')
sum_by_company_category_brand_2 = pd.read_csv('data/sums/sum_by_company_category_brand_2.csv')
sum_by_company_category_brand = sum_by_company_category_brand_1.append(sum_by_company_category_brand_2)

train_history = pd.read_csv('data/trainHistory.csv')
test_history = pd.read_csv('data/testHistory.csv')
offer = pd.read_csv('data/offers.csv')

train_history_offer = pd.merge(train_history, offer, on = ['offer'], how = 'left')

training_data_1 = pd.merge(train_history_offer, sum_by_company, on = ['id','company'], how = 'left')
training_data_1.rename(columns={'purchasequantity': 'pq_company', 'purchaseamount': 'pa_company'},inplace=True)
training_data_2 = pd.merge(train_history_offer, sum_by_category, on = ['id','category'], how = 'left')
training_data_2.rename(columns={'purchasequantity': 'pq_category', 'purchaseamount': 'pa_category'},inplace=True)
training_data_3 = pd.merge(train_history_offer, sum_by_company_category_brand, on = ['id','company','category','brand'], how = 'left')
training_data_3.rename(columns={'purchasequantity': 'pq_company_category_brand', 'purchaseamount': 'pa_company_category_brand'},inplace=True)

training_data = pd.merge(training_data_1, training_data_2, on = ['id','company','category','brand'], how = 'left')
training_data.drop(['chain_y','offer_y','market_y','repeattrips_y','repeater_y','offerdate_y','quantity_y','offervalue_y'],inplace=True,axis=1)
training_data.rename(columns={'chain_x': 'chain','offer_x': 'offer','market_x': 'market','repeattrips_x': 'repeattrips','repeater_x': 'repeater','offerdate_x': 'offerdate','quantity_x': 'quantity','offervalue_x': 'offervalue'},inplace=True)
training_data = pd.merge(training_data, training_data_3, on = ['id','company','category','brand'], how = 'left')
training_data.drop(['chain_y','offer_y','market_y','repeattrips_y','repeater_y','offerdate_y','quantity_y','offervalue_y'],inplace=True,axis=1)
training_data.rename(columns={'chain_x': 'chain','offer_x': 'offer','market_x': 'market','repeattrips_x': 'repeattrips','repeater_x': 'repeater','offerdate_x': 'offerdate','quantity_x': 'quantity','offervalue_x': 'offervalue'},inplace=True)

#training_data = training_data.fillna(value = -999)

training_data.to_csv('data/features.csv',index=False)


