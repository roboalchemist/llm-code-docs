# Interface

[https://github.com/0gfoundation/0g-chain/blob/dev/precompiles/interfaces/contracts/IWrappedA0GIBase.sol](https://github.com/0gfoundation/0g-chain/blob/dev/precompiles/interfaces/contracts/IWrappedA0GIBase.sol)

## Structs

### `Supply`
```solidity
struct Supply {
    uint256 cap;
    uint256 initialSupply;
    uint256 supply;
}
```
- **Description**: Defines the supply details of a minter, including the cap, initial supply, and the current supply.
  
- **Fields**:
  - `cap`: The maximum allowed mint supply for the minter.
  - `initialSupply`: The initial mint supply to the minter, equivalent to the initial allowed burn amount.
  - `supply`: The current mint supply used by the minter, set to `initialSupply` at beginning.

---

## Functions

### `getWA0GI()`
```solidity
function getWA0GI() external view returns (address);
```
- **Description**: Retrieves the address of the wrapped 0G token from the wrapped 0G precompile.
- **Returns**: `address` of the W0G contract.

---

### `minterSupply(address minter)`
```solidity
function minterSupply(address minter) external view returns (Supply memory);
```
- **Description**: Retrieves the mint supply details for a given minter.
- **Parameters**: 
  - `minter`: The address of the minter.
- **Returns**: A `Supply` structure containing the mint cap, initial supply, and current supply of the specified minter.

---

### `mint(address minter, uint256 amount)`
```solidity
function mint(address minter, uint256 amount) external;
```
- **Description**: Mints 0G to WA0GI contract and adds the corresponding amount to the minter's mint supply. If the minter's final mint supply exceeds their mint cap, the transaction will revert.
- **Parameters**: 
  - `minter`: The address of the minter.
  - `amount`: The amount of 0G to mint.
- **Restrictions**: Can only be called by the WA0GI contract.

---

### `burn(address minter, uint256 amount)`
```solidity
function burn(address minter, uint256 amount) external;
```
- **Description**: Burns the specified amount of 0G in WA0GI contract on behalf of the minter and reduces the corresponding amount from the minter's mint supply.
- **Parameters**: 
  - `minter`: The address of the minter.
  - `amount`: The amount of 0G to burn.
- **Restrictions**: Can only be called by the W0G contract.

---

---

## Staking Interfaces


Welcome to the 0G Chain Staking Interfaces documentation. This guide provides comprehensive information about interacting with the 0G Chain staking system through smart contracts, enabling you to build applications that leverage validator operations and delegations.

:::tip **Running a Validator?**
If you want to set up and initialize a validator, see the [Validator Initialization Guide](#validator-initialization) below.
:::

## Quick Navigation

- **[Validator Initialization Guide](#validator-initialization)** - Complete step-by-step setup for becoming a validator
- **[Contract Interfaces](#contract-interfaces)** - Smart contract reference documentation
- **[Examples](#examples)** - Smart contract code examples

---

## Overview

The 0G Chain staking system enables 0G token holders to participate in network consensus and earn rewards through two primary mechanisms:

1. **Becoming a Validator**: Run infrastructure to validate transactions and produce blocks
2. **Delegating to Validators**: Stake tokens with existing validators to earn rewards without running infrastructure

The staking system is built on two core smart contract interfaces:

- **`IStakingContract`**: Central registry managing validators and global staking parameters
- **`IValidatorContract`**: Individual validator operations including delegations and reward distribution

## Prerequisites

Before working with the staking interfaces:

- Familiarity with Solidity and smart contract development
- Basic knowledge of consensus mechanisms and staking concepts

## Quick Start

```solidity
// Create a validator
IStakingContract staking = IStakingContract(0xea224dBB52F57752044c0C86aD50930091F561B9);
address validator = staking.createAndInitializeValidatorIfNecessary{value: msg.value}(
    description, commissionRate, withdrawalFee, pubkey, signature
);

// Delegate to validator
IValidatorContract(validator).delegate{value: msg.value}(msg.sender);
```

## Core Concepts

### Validators
Validators process transactions and produce blocks:
- **Unique Identity**: Identified by 48-byte consensus public key
- **Operator Control**: Managed by an Ethereum address
- **Commission**: Set their own reward commission rates
- **Self-Delegation**: Required minimum stake from operator

### Delegations
Token holders earn rewards by delegating to validators:
- **Share-Based**: Delegations represented as shares in validator pool
- **Proportional Rewards**: Earnings based on share percentage
- **Withdrawal Delay**: Undelegation subject to network delay period

### Reward Distribution
Rewards flow through multiple layers:
1. **Community Tax**: Applied to all rewards first
2. **Validator Commission**: Taken from remaining rewards
3. **Delegator Distribution**: Proportional to shares held

## Contract Interfaces

### IStakingContract
`0xea224dBB52F57752044c0C86aD50930091F561B9` (Mainnet)

Central registry for validators and global parameters.

#### Validator Management
```solidity
// Create validator contract
function createValidator(bytes calldata pubkey) external returns (address);

// Initialize validator with self-delegation
function initializeValidator(
    Description calldata description,
    uint32 commissionRate,
    uint96 withdrawalFeeInGwei,
    bytes calldata pubkey,
    bytes calldata signature
) external payable;

// Create and initialize in one call
function createAndInitializeValidatorIfNecessary(
    Description calldata description,
    uint32 commissionRate, 
    uint96 withdrawalFeeInGwei,
    bytes calldata pubkey,
    bytes calldata signature
) external payable;
```

#### Query Functions
```solidity
function getValidator(bytes memory pubkey) external view returns (address);
function computeValidatorAddress(bytes calldata pubkey) external view returns (address);
function validatorCount() external view returns (uint32);
function maxValidatorCount() external view returns (uint32);
```

### IValidatorContract
Individual validator operations and delegation management.

#### Delegation Management
```solidity
// Delegate tokens (msg.value = amount)
function delegate(address delegatorAddress) external payable returns (uint);

// Undelegate shares (msg.value = withdrawal fee)
function undelegate(address withdrawalAddress, uint shares) external payable returns (uint);

// Withdraw validator commission (only validator operator)
function withdrawCommission(address withdrawalAddress) external returns (uint);
```

:::info **Access Control**
The `withdrawCommission` function is restricted to the validator operator only - the address that originally created and manages the validator.
:::

#### Information Queries
```solidity
function tokens() external view returns (uint);           // Total tokens (delegated + rewards)
function delegatorShares() external view returns (uint);  // Total shares issued
function getDelegation(address delegator) external view returns (address, uint);
function commissionRate() external view returns (uint32);
function withdrawalFeeInGwei() external view returns (uint96);
```

:::tip **Understanding tokens()**
The `tokens()` function returns the complete validator balance, including both the original delegated amounts and any accumulated rewards that haven't been distributed yet.
:::

## Examples

### Creating a Validator

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./IStakingContract.sol";

contract ValidatorExample {
    IStakingContract constant STAKING = IStakingContract(0xea224dBB52F57752044c0C86aD50930091F561B9);
    
    function createValidator(
        bytes calldata pubkey, 
        bytes calldata signature
    ) external payable {
        Description memory desc = Description({
            moniker: "My Validator",
            identity: "keybase-id", 
            website: "https://validator.example.com",
            securityContact: "security@example.com",
            details: "A reliable 0G Chain validator"
        });
        
        STAKING.createAndInitializeValidatorIfNecessary{value: msg.value}(
            desc,
            50000,  // 5% commission
            1,      // 1 Gwei withdrawal fee
            pubkey,
            signature
        );
    }
}
```

### Delegation Management

```solidity
contract DelegationHelper {
    IStakingContract constant STAKING = IStakingContract(0xea224dBB52F57752044c0C86aD50930091F561B9);
    
    function delegateToValidator(bytes calldata pubkey) external payable {
        address validator = STAKING.getValidator(pubkey);
        require(validator != address(0), "Validator not found");
        
        IValidatorContract(validator).delegate{value: msg.value}(msg.sender);
    }
    
    function getDelegationInfo(
        bytes calldata pubkey,
        address delegator
    ) external view returns (uint shares, uint estimatedTokens) {
        address validator = STAKING.getValidator(pubkey);
        IValidatorContract v = IValidatorContract(validator);
        
        (, shares) = v.getDelegation(delegator);
        
        uint totalTokens = v.tokens();
        uint totalShares = v.delegatorShares();
        
        if (totalShares > 0) {
            estimatedTokens = (shares * totalTokens) / totalShares;
        }
    }
}
```

## Validator Initialization

This section covers the complete workflow for setting up and initializing a validator on the 0G Chain.

### Step 1: Generate Validator Signature

The validator signature creation process is simplified with a single command:

```bash