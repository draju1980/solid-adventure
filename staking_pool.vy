# SPDX-License-Identifier: MIT

# Staking Pool Contract

interface ERC20:
    def transferFrom(sender: address, receiver: address, amount: uint256): nonpayable
    def transfer(receiver: address, amount: uint256): nonpayable

@external
def __init__(token: address, reward_rate: uint256):
    self.staking_token: address = token
    self.reward_rate: uint256 = reward_rate  # Reward rate per second
    self.total_staked: uint256 = 0
    self.balances: HashMap[address, uint256] = HashMap()
    self.rewards: HashMap[address, uint256] = HashMap()
    self.last_update: HashMap[address, uint256] = HashMap()

def _update_rewards(account: address):
    current_time: uint256 = block.timestamp
    last_time: uint256 = self.last_update[account]
    staked_amount: uint256 = self.balances[account]
    if staked_amount > 0:
        elapsed_time: uint256 = current_time - last_time
        self.rewards[account] += elapsed_time * staked_amount * self.reward_rate / 1e18
    self.last_update[account] = current_time

@external
def stake(amount: uint256):
    assert amount > 0, "Amount must be greater than 0"
    self._update_rewards(msg.sender)
    ERC20(self.staking_token).transferFrom(msg.sender, self, amount)
    self.balances[msg.sender] += amount
    self.total_staked += amount

@external
def withdraw(amount: uint256):
    assert amount > 0, "Amount must be greater than 0"
    assert self.balances[msg.sender] >= amount, "Insufficient balance"
    self._update_rewards(msg.sender)
    self.balances[msg.sender] -= amount
    self.total_staked -= amount
    ERC20(self.staking_token).transfer(msg.sender, amount)

@external
def claim_rewards():
    self._update_rewards(msg.sender)
    reward: uint256 = self.rewards[msg.sender]
    assert reward > 0, "No rewards available"
    self.rewards[msg.sender] = 0
    ERC20(self.staking_token).transfer(msg.sender, reward)

@view
@external
def get_staked_balance(account: address) -> uint256:
    return self.balances[account]

@view
@external
def get_total_staked() -> uint256:
    return self.total_staked

@view
@external
def get_rewards(account: address) -> uint256:
    self._update_rewards(account)
    return self.rewards[account]
