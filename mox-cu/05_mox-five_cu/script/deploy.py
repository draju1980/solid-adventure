from src import favorites, favorites_factory, five_more, word, calc
from moccasin.boa_tools import VyperContract

def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    return favorites_contract

def deploy_factory(favorites_contract: VyperContract):
    factory_contract: VyperContract = favorites_factory.deploy(favorites_contract.address)
    factory_contract.create_favorite_contract()

    new_favorites_address: str = factory_contract.list_of_favorite_contracts(0)
    new_favorites_contract: VyperContract = favorites.at(new_favorites_address)
    new_favorites_contract.store(123)
    print(f"Stored value in new favorites contract: {new_favorites_contract.retrieve()}")

def deploy_five_more():
    five_more_contract: VyperContract = five_more.deploy()
    print(f"Default Stored value in factory contract: {five_more_contract.retrieve()}")
    five_more_contract.store(90)
    print(f"Stored value in workshop contract after store call: {five_more_contract.retrieve()}")

def word_contract():
    word_contract: VyperContract = word.deploy()
    print(f"Default Stored string in workshop contract: {word_contract.get()}")
    word_contract.set("hello world")
    print(f"Stored string on workshop contract: {word_contract.get()}")

def calculator_contract():
    calculator_contract: VyperContract = calc.deploy()
    print(f"Addition: {calculator_contract.import_add(11, 22)}")
    print(f"Subtraction: {calculator_contract.import_subtract(11, 7)}")
    print(f"Multiplication: {calculator_contract.import_multiply(11, 21)}")
    print(f"Division: {calculator_contract.import_divide(111, 21)}")

def moccasin_main():
    favorites_contract = deploy_favorites()
    deploy_factory(favorites_contract)
    deploy_five_more()
    word_contract()
    calculator_contract()
