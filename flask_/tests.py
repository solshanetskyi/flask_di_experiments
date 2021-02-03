import pytest

from flask_.app import create_app

app = create_app()
app.config["TESTING"] = True


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_credit_card(client):
    payment_options_response = client.get("/")

    assert 200 == payment_options_response.status_code

    print(payment_options_response.get_data())
