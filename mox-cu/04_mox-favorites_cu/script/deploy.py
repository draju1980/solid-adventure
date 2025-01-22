# import the favorites contract
from src import favorites
from moccasin.boa_tools import VyperContract    
from moccasin.config import get_active_network
from eth_account import Account


def deploy_favorites() -> VyperContract:
    # deploy the favorites contract
    favorites_contract: VyperContract = favorites.deploy()

    # favorites contract details  in blockchain network
    print(f"\nThe contract name is: {favorites_contract.contract_name}")
    print(f"\nThe contract address is: {favorites_contract._address}")
    print(f"\nThe contract abi is: {favorites_contract.abi}")
    print(f"\nThe contract bytecode is: {favorites_contract.bytecode.hex()}")
  

    # Get the starting number
    starting_number: int  = favorites_contract.retrieve()
    print(f'\nThe starting number is: {starting_number}\n')

    # Set the starting number
    favorites_contract.store(77)
    ending_number: int  = favorites_contract.retrieve()
    print(f'\nThe ending number is: {ending_number}\n')

    # Verify the contract with blockscout
    active_network = get_active_network()
    if active_network.has_explorer():
        result = active_network.moccasin_verify(favorites_contract)
        result.wait_for_verification()
        print(f'\nContract verified: {result.is_verified()}\n')
    # return the contract
    return favorites_contract

def moccasin_main() -> VyperContract:
    return deploy_favorites()