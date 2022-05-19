import unittest

import requests


class ApiTest(unittest.TestCase):
    URL = "http://127.0.0.1:5000/NFT"


    
    NFT_post_data ={    
    'asset_id': 10,
    'name':"Himanshu",
    'picture':"picture65464.html",
    'external_link':"heyhimanshu.com",
    'description':"this is a wallet",
    "collection":1,
    'supply': 56555,
    'royalties': 5555,
    "date_of_creation":"2022-01-31",
    'buyer': 646416, 
    }
    
    def test_1_NFT_USER(self):
        response = requests.post(ApiTest.URL , data= ApiTest.NFT_post_data)
        self.assertEqual(response.status_code, 201)
        
        
    def test_2_get_all_users(self):
        response = requests.get(ApiTest.URL)
        self.assertEqual(response.status_code , 200)
        
    
    def test_3_get_USER1(self):

        response = requests.get(ApiTest.URL +"/1")
        self.assertEqual(response.status_code, 200)
            



    
    


if __name__ == '__main__':
    
    
    unittest.main()