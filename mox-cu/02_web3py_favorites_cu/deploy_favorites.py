# importing vyper compiler
from vyper import compile_code
from web3 import Web3
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()
RPC_URL = os.getenv("RPC_URL")
MY_ADDRESS = os.getenv("MY_ADDRESS")
PRIVATE_KEY = os.getenv("MY_PRIVATE_KEY")


# Function to deploy the vyper contract
def main():
    print("\nLets read in the vyper code and deploy the contract...*..*.\n")

    # breackpoint() used for interract with python shell
    # breakpoint()

    # Read in favorites.vy contarct
    with open("favorites.vy", "r") as favorites_file:
        # forword the code to favorites_code variable
        favorites_code = favorites_file.read()
        # to compile the code and pass it to the variable 
        # vyper_compiler(favorites_code, output_formats=["abi", "bytecode"], code_format="vyper")
        compliation_details = compile_code(favorites_code, output_formats=["bytecode", "abi"])
        # print the compliation details
        print("\n", compliation_details)
    # connecting to Blockchain network using tenderly
    # w3 = Web3(Web3.HTTPProvider("https://virtual.sepolia.rpc.tenderly.co/d8376854-1b54-4d65-89b8-15c12cd1bd37"))
    
    # coneecting to the local blockchain network usinf anvil
    w3 = Web3(Web3.HTTPProvider(RPC_URL))

    # Ensure connection is successful
    if not w3.is_connected():
        raise Exception("Failed to connect to the blockchain")

    # using favorites_contract variable as placeholder for the vyper smart contract
    favorites_contract = w3.eth.contract(bytecode=compliation_details["bytecode"], abi=compliation_details["abi"])
    # print("\n",favorites_contract)


    # To build the transaction
    print("\nBuilding the transaction...*..*.\n")
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    transaction = favorites_contract.constructor().build_transaction(
        {
            "nonce": nonce,
            "from": MY_ADDRESS,
            "chainId": w3.eth.chain_id,
            "gasPrice": w3.eth.gas_price
        }
    )
    print("\n",transaction)


    # Signing the transaction
    print("\nSigning the transaction...*\n")
    # signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=MY_PRIVATE_KEY)
    MY_PRIVATE_KEY = w3.eth.account._parse_private_key(PRIVATE_KEY)
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=MY_PRIVATE_KEY)
    print("\n", signed_transaction)

    # Sending the transaction
    print("\nSending the transaction...*\n")
    tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    print("\n transaction hash:\t", tx_hash.hex())
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash.hex())
    print("\n transaction receipt:\t", tx_receipt.values)
    print(f"\n Done! Contract deployed at {tx_receipt.contractAddress}")


if __name__ == "__main__":
    main()