# I'm a comment!

# pragma version 0.4.0
# @license MIT


my_word: String[100]


@deploy
def __init__():
    self.my_word = "hello world"

@external
def store(_my_word: String[100]):
    self.my_word = _my_word

@external
@view
def retrieve() -> String[100]:
    return self.my_word
