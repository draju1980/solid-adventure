# Moccasin Project

🐍 Welcome to your Moccasin project!

## Quickstart

1. Deploy to a fake local network that titanoboa automatically spins up!

```bash
mox run deploy
```

2. Run tests

```
mox test
```

3. There are the Moccasin wallet command

a. Wallet commands to import the private key in local keystore, during the import process it will prompt you for password.
```wallet
✗ mox wallet import Anvil1
Running wallet command...
Importing private key...
Enter your private key: 
Enter a password to encrypt your key: 
Confirm your password: 
Saved account Anvil1 to keystores!
```

b. Wallet command to list the private keys
```wallet
✗ mox wallet list         
Running wallet command...
Found 1 account:
Anvil1
```

c. Wallet command to view any key on local keystores 
```wallet
✗ mox wallet view Anvil1
Running wallet command...
Keystore JSON for account Anvil1:
{
    "address": "f39Fd6e51aad88F6F4ce6aB8827279cffFb92266",
    "crypto": {
        "cipher": "aes-128-ctr",
        "cipherparams": {
            "iv": "5eee1481002bdc0c797c33ae5c8a213f"
        },
        "ciphertext": "15768dd4e55259b8d49493c9a1f2ac32f107182b457665c5377175095f1ab891",
        "kdf": "scrypt",
        "kdfparams": {
            "dklen": 32,
            "n": 262144,
            "r": 8,
            "p": 1,
            "salt": "3efb707f7b3aef28b508f85364073fc5"
        },
        "mac": "961ca6b33b610e2fabc489543f5ba2779f18840ec2a926db405308d3fba63489"
    },
    "id": "fd64151c-eaf2-4571-87a0-72666329679d",
    "version": 3
}
```

c. wallet command to delete the private key from local keystores.
```wallet
✗ mox wallet delete Anvil1
Running wallet command...
Successfully deleted account Anvil1 from keystores
```

4. Testing the contract using test case script,
below command will run all the test
```test
✗ mox test
Running test command...
========================================================================================= test session starts =========================================================================================
platform darwin -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/draju1980/lab/solid-adventure/mox-cu/04_mox-favorites_cu
configfile: pyproject.toml
plugins: titanoboa-0.2.5, cov-6.0.0, hypothesis-6.123.2, xdist-3.6.1
collected 4 items                                                                                                                                                                                     

tests/test_favorites.py ....                                                                                                                                                                    [100%]

========================================================================================== 4 passed in 0.07s ==========================================================================================
 ```

 To test only one case we need to use -k option and pass the test name, as example below

 ```test
mox test -k test_to_name_to_favorite_number
Running test command...
========================================================================================= test session starts =========================================================================================
platform darwin -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/draju1980/lab/solid-adventure/mox-cu/04_mox-favorites_cu
configfile: pyproject.toml
plugins: titanoboa-0.2.5, cov-6.0.0, hypothesis-6.123.2, xdist-3.6.1
collected 4 items / 3 deselected / 1 selected                                                                                                                                                         

tests/test_favorites.py .                                                                                                                                                                       [100%]

=================================================================================== 1 passed, 3 deselected in 0.06s ===================================================================================
 ```
_For documentation, please run `mox --help` or visit [the Moccasin documentation](https://cyfrin.github.io/moccasin)_
