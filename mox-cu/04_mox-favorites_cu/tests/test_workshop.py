# from script.deploy import deploy_favorites

# import pytest

# @pytest.fixture(scope="session")
# def favorites_contract():
#     return deploy_favorites()


def test_starting_word(workshop_contract):
    # # Arrange
    # starting_number = 7
    # ending_number = 77
    # # Act
    # favorites_contract = deploy_favorites()
    # # Assert
    # assert favorites_contract.retrieve() == starting_number
    # favorites_contract.store(ending_number)
    # assert favorites_contract.retrieve() == ending_number
    # favorites_contract = deploy_favorites()
    assert workshop_contract.retrieve() == 'Welcome to the workshop!'



def test_can_change_word(workshop_contract):
    # Arrange
    # favorites_contract = deploy_favorites()
    # Act
    name1 = "Donald Trump"
    workshop_contract.store(name1)
    # Assert
    assert workshop_contract.retrieve() == name1
    # Act
    name2 = "Melania Trump"
    workshop_contract.store(name2)
    # Assert
    assert workshop_contract.retrieve() == name2
