from script.deploy import deploy_favorites
from script.workshop import deploy_word

import pytest

@pytest.fixture(scope="session")
def favorites_contract():
    return deploy_favorites()

@pytest.fixture(scope="session")
def workshop_contract():
    return deploy_word()