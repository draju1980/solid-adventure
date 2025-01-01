import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account
import os

# Load the environment variables
load_dotenv()
RPC_URL = os.getenv("RPC_URL")
MY_ADDRESS = os.getenv("MY_ADDRESS")
PRIVATE_KEY = os.getenv("MY_PRIVATE_KEY")

def main():
    print("\nLets read in the vyper contract and deploy it to the Anvil blockchain")
    env = NetworkEnv(EthereumRPC(RPC_URL))
    boa.set_env(env)

    my_account = Account.from_key(PRIVATE_KEY)
    boa.env.add_account(my_account,force_eoa=True)


    # Deploy the contract on anvil blockchain
    favorites_contract = boa.load('favorites.vy')

        # Print contract address after deploying
    print(f"\nThe contract name is: {favorites_contract.contract_name}")
    print(f"\nThe contract address is: {favorites_contract._address}")
    print(f"\nThe contract abi is: {favorites_contract.abi}")
    print(f"\nThe contract bytecode is: {favorites_contract.bytecode.hex()}")


    starting_favorite_number = favorites_contract.retrieve()
    print(f"\nThe starting favorite number is: {starting_favorite_number}")

    # new_favorite_number = cast_to_uint256((input("Enter new favorite number: ")))

    # Setting the favorite number
    favorites_contract.store(22)    # Setting the favorite number to 42 heance send the transaction
    ending_favorite_number = favorites_contract.retrieve()
    print(f"\nThe ending favorite number is: {ending_favorite_number}")


if __name__ == '__main__':
    main()