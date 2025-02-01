# @version ^0.4.0
# @license MIT

# Import and declare module
import calculator as calc  # Alias for simplicity

# # Initialize the module
# initializes: calculator

# Use the module
# uses: calc


# Initialize with default values
@deploy
def __init__():
    pass


@external
@pure
def import_add(x: uint256, y: uint256) -> uint256:
    return calc.add(x, y)
    

@external
@pure
def import_subtract(x: uint256, y: uint256) -> uint256:
    return calc.sub(x, y)

@external
@pure
def import_multiply(x: uint256, y: uint256) -> uint256:
    return calc.mul(x, y)

@external
@pure
def import_divide(x: uint256, y: uint256) -> uint256:
    return calc.div(x, y)
