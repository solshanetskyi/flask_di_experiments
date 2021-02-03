import pytest

from flask_.app import create_app

app = create_app()
app.config["TESTING"] = True


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_credit_card(client):
    credit_card = client.get("/credit_card")

    print(credit_card.get_data())

    assert 200 == credit_card.status_code

