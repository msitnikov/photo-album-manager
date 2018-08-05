    
import unittest
import pytest
import json
import requests

class TestCreateAlbum(unittest.TestCase):  
 
    @classmethod
    def setUpClass(cls):
        global BASE_URL
        BASE_URL = "http://localhost:8080"

    def test_verifyAbilityToCreateAlbum(self):
        requestPayload = {
            "title": "MyFirstAlbum",
            "userId": 2
            }
        resp = requests.post(BASE_URL + "/api/albums", json=requestPayload)
        data = resp.json()
        assert resp.status_code ==200
        assert data['title'] =='MyFirstAlbum'
        assert data['userId'] ==2
        albumID = data['id']
