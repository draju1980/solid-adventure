# @version ^0.4.0
# @license MIT
# @title Calculator for Ethereum and compatible chains


# A simple calculator contract for Ethereum and compatible chains
@internal
@pure
def add(a: uint256, b: uint256) -> uint256:
    return a + b

@internal
@pure
def sub(a: uint256, b: uint256) -> uint256:
    return a - b

@internal
@pure
def mul(a: uint256, b: uint256) -> uint256:
    return a * b

@internal
@pure
def div(a: uint256, b: uint256) -> uint256:
    assert b != 0, "Division by zero"
    return a // b
