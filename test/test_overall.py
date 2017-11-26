'''
Created on Nov 3, 2017

@author: ckubudi
'''
import unittest
import load_factors as lf
import factor_portfolio as fp
import tools

class Test(unittest.TestCase):


    def test_factor_portfolios(self):
        factors = ['price_to_book']
        assets_list=lf.load_assets(factors, '..\\data\\')
        factor_df=lf.create_factor_df(assets_list,'price_to_book',True)
        returns_df=lf.create_factor_df(assets_list,'return',False)
        (data,data_portfolios)=fp.create_factor_portfolio(factor_df, returns_df, 10, 1)
        
        print('end')
        
        tools.plot_cumulative_returns(data)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()