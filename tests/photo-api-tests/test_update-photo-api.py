import unittest
import pytest
import json
import requests

class TestGetUpdatePhoto(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        global BASE_URL
        global photoID
        global albumID
        global id
        global albumId
        global title
        global url
        global thumbnailUrl
        global albumTitle
        title = "veni vidi vici"
        url = "http://placehold.it/600/92bfbf"
        thumbnailUrl = "http://placehold.it/150/92bfbf"
        albumTitle = "MyFirstAlbum"
        BASE_URL = "http://localhost:8080"
        id = 44
        #create album    
        requestPayload = {
            "id": id,
            "title": albumTitle,
            "userId": 2
            }
        resp = requests.post(BASE_URL + "/api/albums", json=requestPayload)
        data = resp.json()
        assert resp.status_code ==200
        assert data['title'] == albumTitle
        assert data['userId'] ==2
        albumID = data['id']
        #create/assign photo to album
        requestPayload = {
            "id": id,
            "albumId": albumID,
            "title": title,
            "url": url,
            "thumbnailUrl": thumbnailUrl
        }
        resp = requests.post(BASE_URL + "/api/photos", json=requestPayload)
        data = resp.json()
        photoID = data['id']
        assert resp.status_code ==200
        assert data['albumId'] == albumID
        assert data['title'] == title
        assert data['url'] == url
        assert data['thumbnailUrl'] == thumbnailUrl

    def test_verifyAbilityToUpdatePhotoByID(self):
        requestPayload = {
            "id": id,
            "albumId": albumID,
            "title": "UpdatedTitle",
            "url": "Updated URI",
            "thumbnailUrl": "Updated thumbnailUrl"
        }
        resp = requests.put(BASE_URL + "/api/photos", json=requestPayload)
        data = resp.json()
        photoID = data['id']
        assert resp.status_code == 200
        assert data['albumId'] == albumID
        assert data['title'] == "UpdatedTitle"
        assert data['url'] == "Updated URI"
        assert data['thumbnailUrl'] == "Updated thumbnailUrl"
 
 