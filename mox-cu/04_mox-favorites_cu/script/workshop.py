# import the favorites contract
from src import workshop
from moccasin.boa_tools import VyperContract    
from moccasin.config import get_active_network
from eth_account import Account


def deploy_word() -> VyperContract:
    # deploy the favorites contract
    workshop_contract: VyperContract = workshop.deploy()

    # favorites contract details  in blockchain network
    print(f"\nThe contract name is: {workshop_contract.contract_name}")
    print(f"\nThe contract address is: {workshop_contract._address}")
    print(f"\nThe contract abi is: {workshop_contract.abi}")
    print(f"\nThe contract bytecode is: {workshop_contract.bytecode.hex()}")
  

    # Get the starting word
    starting_string = workshop_contract.retrieve()
    print(f'\nThe starting word is: {starting_string}\n')

    # Set the starting word
    workshop_contract.store("Welcome to the workshop!")
    ending_string = workshop_contract.retrieve()
    print(f'\nThe ending word is: {ending_string}\n')        

    # return the contract
    return workshop_contract

def moccasin_main() -> VyperContract:
    return deploy_word()