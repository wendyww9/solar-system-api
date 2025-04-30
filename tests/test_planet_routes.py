import pytest

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Take-a-Nap",
        "description": "Do It Tomorrow",
        "habitable": 'true'
    }

def test_get_one_planet_no_data(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        'message': 'planet with 1 does not exist'
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Very New Planet",
        "description": "Very-very new planet",
        "habitable": 'false'
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Very New Planet",
        "description": "Very-very new planet",
        "habitable": 'false'
    }