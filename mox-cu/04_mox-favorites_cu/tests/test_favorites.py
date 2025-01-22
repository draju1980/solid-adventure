# from script.deploy import deploy_favorites

# import pytest

# @pytest.fixture(scope="session")
# def favorites_contract():
#     return deploy_favorites()


def test_starting_values(favorites_contract):
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
    assert favorites_contract.retrieve() == 77

def test_can_change_values(favorites_contract):
    # Arrange
    # favorites_contract = deploy_favorites()
    # Act
    favorites_contract.store(42)
    # Assert
    assert favorites_contract.retrieve() == 42
    # Act
    favorites_contract.store(77)
    # Assert
    assert favorites_contract.retrieve() == 77

def test_to_add_person(favorites_contract):
    # Arrange
    # favorites_contract = deploy_favorites()
    name = "John"
    age = 42
    # Act
    favorites_contract.add_person(name, age)
    index0 = favorites_contract.list_of_people(0)
    # Assert
    assert index0 == (age, name)
    # Act
    name = "Tom"
    age = 77
    favorites_contract.add_person(name, age)
    index0 = favorites_contract.list_of_people(1)
    # Assert
    assert index0 == (age, name)


def test_to_name_to_favorite_number(favorites_contract):
    # Arrange
    # favorites_contract = deploy_favorites()
    name = "Mary"
    age = 27
    # Act
    favorites_contract.add_person(name, age)
    index0 = favorites_contract.list_of_numbers(0)
    # Assert
    assert index0 == age
    # Act
    name = "Tom"
    age = 77
    favorites_contract.add_person(name, age)
    index0 = favorites_contract.list_of_numbers(1)
    # Assert
    assert index0 == age
