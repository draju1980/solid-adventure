# I'm a comment!

# pragma version 0.4.0
# @license MIT

my_word: public(String[100])


@deploy
def __init__():
    self.my_word = "Welcome to the world of Vyper!"

@external
def set(_my_word: String[100]):
    self.my_word = _my_word

@external
@view
def get() -> String[100]:
    return self.my_word
