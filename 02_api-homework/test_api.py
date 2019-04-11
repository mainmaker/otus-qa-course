import json
import pytest


def test_dogceo_status(dog):
    """Docsting"""
    # print("\nREQUEST: ", request.config.getoption("--address"))
        # pytest.skip("unsupported configuration")
    assert dog.status_code == 200

def test_dogceo_headers(dog):
    """Docsting"""
    assert dog.headers["Content-Type"] == "application/json"

def test_dogceo_text_status(dog):
    """Docsting"""
    res = json.loads(dog.text)
    assert res["status"] == "success"

def test_dogceo_text_message(dog):
    """Docsting"""
    res = json.loads(dog.text)
    assert type(res["message"]) == str


def test_brew_status(brew):
    """Docsting"""
    assert brew.status_code == 200

def test_brew_id(brew):
    """Docsting"""
    json_text = json.loads(brew.text)
    assert json_text["id"] == 5494

def test_brew_type(brew):
    """Docsting"""
    json_text = json.loads(brew.text)
    assert type(json_text) == dict

def test_brew_name(brew):
    """Docsting"""
    json_text = json.loads(brew.text)
    assert json_text["name"] == "MadTree Brewing"


def test_cdn_status(cdn):
    """Docsting"""
    assert cdn.status_code == 200

def test_cdn_results(cdn):
    """Docsting"""
    json_text = json.loads(cdn.text)
    assert bool(json_text["results"]) == True

def test_cdn_results_name(cdn):
    """Docsting"""
    json_text = json.loads(cdn.text)
    name = json_text["results"][0]
    assert name["name"] == "1140"

def test_cdn_headers_methods(cdn):
    """Docsting"""
    assert cdn.headers['Access-Control-Allow-Methods'] == 'GET,PUT,POST,DELETE,OPTIONS'
