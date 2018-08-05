import unittest
import pytest
import json
import requests

class TestDeleteAlbum(unittest.TestCase):
    
    
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
        id = 101
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

    def test_verifyAlbumsCannotBeDeletedIfAssociatedPhotosExist(self):
        requestPayload = {
            "id": id,
            "albumId": albumID,
            "title": "veni vidi vici",
            "url": url,
            "thumbnailUrl": thumbnailUrl
        }
        resp = requests.post(BASE_URL + "/api/photos", json=requestPayload)
        data = resp.json()
        photoID = data['id'] 
        assert resp.status_code ==200
        assert data['albumId'] == albumID
        assert data['title'] == "veni vidi vici"
        assert data['url'] == url
        assert data['thumbnailUrl'] == thumbnailUrl
         
        resp = requests.get(BASE_URL + "/api/albums/" + str(id) + "/photos")
        data = resp.json()
        photoID = data[0]['thumbnailUrl'] 
        assert resp.status_code ==200
        assert data[0]['albumId'] == albumID
        assert data[0]['title'] == title
        assert data[0]['url'] == url
        assert data[0]['thumbnailUrl'] == thumbnailUrl
        resp = requests.delete(BASE_URL + "/api/albums/" + str(id))
        assert resp.status_code ==500
        data = resp.json() 
        assert resp.status_code ==500
        assert data['status'] == 500
        assert data['error'] == "Internal Server Error"
 
    def test_verifyAbilityToDeleteAlbumThatHasNoPhotosAssociated(self):
        id = 102
        requestPayload = {
            "id": id,
            "title": albumTitle,
            "userId": 2
            }
        resp = requests.post(BASE_URL + "/api/albums", json=requestPayload)
        data = resp.json()
        assert resp.status_code ==200
        assert data['title'] ==albumTitle
        assert data['userId'] ==2
        albumID = data['id']
        resp = requests.delete(BASE_URL + "/api/albums/" + str(albumID))
        assert resp.status_code ==200
        requestPayload = {
            "id": 44,
            "albumId": albumID,
            "title": title,
            "url": url,
            "thumbnailUrl": thumbnailUrl
        }
        resp = requests.post(BASE_URL + "/api/photos", json=requestPayload)
        data = resp.json()
        assert resp.status_code ==500
        assert data['status'] == 500
        assert data['error'] == "Internal Server Error"
 
 

 