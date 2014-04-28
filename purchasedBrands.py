# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 12:19:10 2014

@author: redaal-bahrani
"""


from mrjob.job import MRJob

class CommaValueProtocol(object):

    def write(self, key, values):
        return ','.join(str(v) for v in values)


class PurchasedBrands(MRJob):

    OUTPUT_PROTOCOL = CommaValueProtocol

    def mapper(self, key, line):
        """
        Emit the id and brands purchased

        86246  15343
        86246  55172
        86246  3830

        """
        user_id,chain,dept,category,company,brand,sdate,productsize,productmeasure,purchasequantity,purchaseamount = line.split(',')
        yield  user_id, brand

    def reducer(self, user_id, values):
        """
        For each user_id, emit a row containing their purchased brands
        user_id, brands

        86246,15343,55172,3830
        
        """
        purchased_brands = []
        for brand in values:
            purchased_brands.append(brand)

        purchased_brands = list(sorted(set(purchased_brands)))
        purchased_brands.insert(0,user_id)
        yield None, (purchased_brands)


if __name__ == '__main__':
    PurchasedBrands.run()