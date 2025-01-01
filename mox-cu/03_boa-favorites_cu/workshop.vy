# pragma version 0.4.0
# @license MIT

my_bool: bool

@deploy
def __init__():
    self.my_bool = True

@external
def set_bool(new_bool: bool):
    self.my_bool = new_bool

@external
@view
def get_bool() -> bool:
    return self.my_bool