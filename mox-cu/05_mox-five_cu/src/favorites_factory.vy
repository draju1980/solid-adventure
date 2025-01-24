# pragma version 0.4.0
# @license MIT

# EVM: Ethereum Virtual Machine
# Ethereum, Arbitrum, Optimism, ZKsync

# imprting the interface
from interfaces import i_favorites

# # Option 1
# # List of favorite contract addresses
# list_of_favorite_contracts: public(DynArray[address, 100])

# List of favorite contract addresses
list_of_favorite_contracts: public(DynArray[i_favorites, 100])

# State variable of type address for the original favorite contract address
original_favorite_contract: address


@deploy
def __init__(original_favorite_contract: address):
    self.original_favorite_contract = original_favorite_contract

# # Option 1
# @external
# def create_favorite_contract():
#     new_favorite_contract: address = create_copy_of(self.original_favorite_contract)
#     self.list_of_favorite_contracts.append(new_favorite_contract)

# @external
# def store_from_factory(favorites_index: uint256, new_number: uint256):
#     favorites_address: address = self.list_of_favorite_contracts[favorites_index]
#     favorites_contract: i_favorites = i_favorites(favorites_address)
#     extcall favorites_contract.store(new_number)

# Option 2
@external
def create_favorite_contract():
    new_favorite_contract: address = create_copy_of(self.original_favorite_contract)
    self.list_of_favorite_contracts.append(i_favorites(new_favorite_contract))

@external
def store_from_factory(favorites_index: uint256, new_number: uint256):
    favorites_contract: i_favorites = self.list_of_favorite_contracts[favorites_index]
    extcall favorites_contract.store(new_number)

@external
@view
def view_from_factory(favorites_index: uint256) -> uint256:
    return staticcall self.list_of_favorite_contracts[favorites_index].retrieve()
    # favorites_contract: i_favorites = self.list_of_favorite_contracts[favorites_index]
    # value: uint256 = staticcall favorites_contract.retrieve()
    # return value