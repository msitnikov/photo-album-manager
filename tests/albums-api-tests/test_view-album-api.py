import unittest
import pytest
import json
import requests





class TestViewAlbum(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        global BASE_URL
        global albumID
        global albumTitle

        albumTitle = "MyFirstAlbum"
        BASE_URL = "http://localhost:8080"
        requestPayload = {
            "id": 103,
            "title": albumTitle,
            "userId": 2
            }
        resp = requests.post(BASE_URL + "/api/albums", json=requestPayload)
        data = resp.json()
        assert resp.status_code ==200
        albumID = data['id']
        return albumID
    
    @classmethod
    def tearDownClass(cls):
        resp = requests.delete(BASE_URL + "/api/albums/" + str(albumID))
        assert resp.status_code ==200
 
    def test_verifyAbilityToViewAlbum(self):
        resp = requests.get(BASE_URL + "/api/albums/" + str(albumID))
        data = resp.json()
        assert resp.status_code ==200
        assert data['title'] == albumTitle
        assert data['userId'] == 2


       