# Source: https://docs.espressosys.com/network/concepts/the-espresso-network/internal-functionality/fee-token.md

# Fee Token Contract

{% hint style="info" %}
The source code for the fee token contract can be found on [GitHub](https://github.com/EspressoSystems/espresso-sequencer/blob/b1884c4bea3246a86cbd430853a5a69e4def0f0a/contracts/src/FeeContract.sol).
{% endhint %}

The fee token contract enables builders to deposit ETH which allows them to pay for a data processing fee associated with HotShot. While the fee token contract facilitates deposits, HotShot itself manages and tracks the working balance of builder deposits. Initially, the fee token contract only supports deposits. Withdrawals are planned to be enabled in a future release.

```solidity
function deposit(address user) public payable {
    //...
}
```

The contract defines a minimum and maximum amount for deposits to avoid errors and prevent the fee table from being filled with dust.

```solidity
uint256 public immutable MAX_DEPOSIT_AMOUNT = 1 ether;
uint256 public immutable MIN_DEPOSIT_AMOUNT = 0.001 ether;
```

{% hint style="warning" %}
In the Mainnet 0 release, withdrawals are not enabled and thus the `MAX_DEPOSIT_AMOUNT` aims to minimize how much ETH is locked by a builder.
{% endhint %}

## Public Write Methods

### deposit

Allows anyone to deposit an ETH balance for any user

*the deposit amount is less than a specified threshold to prevent accidental errors*

```solidity
function deposit(address user) public payable;
```

## Fee Token Contract UML

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-b6381b695569d6c399a02de0220106e58e55a2d7%2FFeeTokenUML.png?alt=media" alt=""><figcaption></figcaption></figure>

## Fee Token Contract Dependency Graph

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-28fab38c3e6d1b7d76874a7592cb641694107dbb%2FFeeTokenGraph.png?alt=media" alt=""><figcaption></figcaption></figure>
