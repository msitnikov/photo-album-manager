import unittest
import pytest
import json
import requests





class TestUpdateAlbum(unittest.TestCase):
    
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
        assert data['title'] == albumTitle
        assert data['userId'] ==2        
        albumID = data['id']
    
    @classmethod
    def tearDownClass(cls):
        resp = requests.delete(BASE_URL + "/api/albums/" + str(albumID))
        assert resp.status_code ==200

    def test_verifyAbilityToUpdateAlbum(self):
        requestPayload = {
            "id": albumID,
            "title": "MyFirstAlbumUPDATEDTitle",
            "userId": 1
            }
        resp = requests.post(BASE_URL + "/api/albums", json=requestPayload)
        data = resp.json()
        assert resp.status_code ==200
        assert data['title'] =='MyFirstAlbumUPDATEDTitle'
        assert data['userId'] ==1
        assert data['id'] ==albumID