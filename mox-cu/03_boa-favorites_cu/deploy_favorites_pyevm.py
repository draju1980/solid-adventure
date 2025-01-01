# imprting titanoboa
import boa

def main():
    print("\nLets read in the vyper contract and deploy it to the py-evm blockchain")

    # Deploying the contract using the titanoboa
    favorites_contract = boa.load('favorites.vy')

    # Print contract address after deploying
    print(f"\nThe contract name is: {favorites_contract.contract_name}")
    print(f"\nThe contract address is: {favorites_contract._address}")
    print(f"\nThe contract abi is: {favorites_contract.abi}")
    print(f"\nThe contract bytecode is: {favorites_contract.bytecode.hex()}")


    starting_favorite_number = favorites_contract.retrieve()
    print(f"\nThe starting favorite number is: {starting_favorite_number}")

    # Setting the favorite number
    favorites_contract.store(42)    # Setting the favorite number to 42 heance send the transaction
    ending_favorite_number = favorites_contract.retrieve()
    print(f"\nThe ending favorite number is: {ending_favorite_number}")



if __name__ == '__main__':
    main()