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
    bool_contract = boa.load('workshop.vy')

    # Print contract address after deploying
    print(f"\nThe contract name is: {bool_contract.contract_name}")
    print(f"\nThe contract address is: {bool_contract._address}")
    print(f"\nThe contract abi is: {bool_contract.abi}")
    print(f"\nThe contract bytecode is: {bool_contract.bytecode.hex()}")

    bool_status = bool_contract.get_bool()
    print(f"\nmy_bool status is: {bool_status}")


if __name__ == '__main__':
    main()

