import boa
from dotenv import load_dotenv
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account
import os


# During the deployment of the contract, we will get the contract address, please find the example below,
# ¢python deploy_workshop.py  
# Lets read in the vyper contract and deploy it to the Anvil blockchain
# tx broadcasted: 0xa98fedc4a457b411f330a0f9a8b602bac8c775a03fb4e461b05031ece9a5d432
# 0xa98fedc4a457b411f330a0f9a8b602bac8c775a03fb4e461b05031ece9a5d432 mined in block 0x20ae2d37a9378e9ade4907905d894b9dfe3bb5e162d25f1504a7bddb68c9c9f0!
# contract deployed at 0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512

MY_CONTRACT = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"


# Load the environment variables
load_dotenv()
RPC_URL = os.getenv("RPC_URL")
MY_ADDRESS = os.getenv("MY_ADDRESS")
PRIVATE_KEY = os.getenv("MY_PRIVATE_KEY")

def main():
    print("\nLets read in the vyper contract and deploy it to the Anvil blockchain")


    # Set the environment
    env = NetworkEnv(EthereumRPC(RPC_URL))
    boa.set_env(env)

    my_account = Account.from_key(PRIVATE_KEY)
    boa.env.add_account(my_account,force_eoa=True)


    # Interratt with favorites contract on anvil blockchain
    my_bool_deployer = boa.load_partial('workshop.vy')
    bool_contract = my_bool_deployer.at(MY_CONTRACT)

    bool_status = bool_contract.get_bool()
    print(f"\nmy_bool status after contract deployment: {bool_status}")

    bool_contract.set_bool(False)
    bool_status = bool_contract.get_bool()
    print(f"\nmy_bool status after my_bool variable update: {bool_status}")



    # # Retrieve the favorite number from  anvil blockchain
    # favorite_number = favorites_contract.retrieve()
    # print(f"\nThe favorite number is: {favorite_number}")

    # # Set the favorite number on anvil blockchain

    # favorites_contract.store(NEW_NUMBER)   # Setting the favorite number to 42 heance send the transaction
    # new_favorite_number = favorites_contract.retrieve()
    # print(f"\nThe new favorite number is: {new_favorite_number}")


    # # Storing the person details on the anvil blockchain
    # print("\nLets store the person details on the anvil blockchain")
    # favorites_contract.add_person(fake.name(), NEW_NUMBER)

    # # Added the person details on list of people array on the anvil blockchain
    # person_data = favorites_contract.list_of_people(0)
    # print(f"\nThe person data is: {person_data}")







if __name__ == '__main__':
    main()