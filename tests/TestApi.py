import requests
import random

BASE_URL = "https://automationexercise.com/"

def  test_get_products():
    response = requests.get(f"{BASE_URL}api/productsList")
    assert response.status_code == 200
    body = response.json()
    assert len(body) > 0
    assert "products" in body

def test_post_products():
    response = requests.post(f"{BASE_URL}api/productsList")
    assert response.status_code == 200

    body = response.json()

    assert body["responseCode"] == 405
    assert body["message"] == "This request method is not supported."

def test_create_account():
    payload = {
    "name": "Nika",
    "email": f"nika{random.randint(1,999999)}@mail.com",
    "password": f"r{random.randint(1,999999)}",
    "title": "Mr",
    "birth_date": "1",
    "birth_month": "January",
    "birth_year": "2000",
    "firstname": "Nika",
    "lastname": "Test",
    "company": "QA",
    "address1": "Street 1",
    "country": "Canada",
    "zipcode": "12345",
    "state": "Ontario",
    "city": "Toronto",
    "mobile_number": "123456789"
}
    response = requests.post(f"{BASE_URL}api/createAccount", data=payload)
    assert response.status_code == 200

    body = response.json()

    assert body["responseCode"] == 201
    assert body["message"] == "User created!"
