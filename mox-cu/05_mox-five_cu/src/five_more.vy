# EVM: Ethereum Virtual Machine
# Ethereum, Arbitrum, Optimism, ZKsync

# pragma version 0.4.0
# @license MIT

# importing the favorites contract
import favorites
# import workshop

# initializing the favorites contract
initializes: favorites
# # importing the workshop contract
# initializes: workshop

# export retrieve and add_person functions from the favorites contract || get and set functions from the workshop contract
exports: (
    favorites.retrieve,
    favorites.add_person,
    # workshop.get,
    # workshop.set,
)


# # to export all the state variables and functions from the favorites contract
# exports: (
#     favorites.__interface__,
# )

# deploy and initialize the favorites and workshop contracts
@deploy
def __init__():
    favorites.__init__()
    # workshop.__init__()

@external
def store(new_number: uint256):
    favorites.my_favorite_number = new_number + 5
