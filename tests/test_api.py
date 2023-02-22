from fastapi.testclient import TestClient

from ontogpt_api import __version__
from ontogpt_api.main import app

client = TestClient(app)


def test_api_extract():
    """Test the package main function"""

    response = client.post(
        "/extract",
        data={
            # "datamodel": "",
            # "text": ""
        },
        headers={"Content-Type": "application/json"},
    )
    resp = response.json()
    assert len(resp["named_entities"]) > 1


def test_version():
    """Test the version is a string."""
    assert isinstance(__version__, str)
