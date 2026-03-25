# Source: https://docs.meson.fi/implementation/smart-contracts/solidity.md

# Meson in Solidity

We have implemented the Meson protocol with Solidity smart contracts, and deployed to the following EVM-compatible public chains:

* Ethereum
* BNB Chain (formerly BSC)
* Polygon
* Evmos Mainnet
* Arbitrum
* Optimism
* Aurora (on NEAR)
* Conflux eSpace
* Avalanche C-chain
* Fantom
* Tron
* Harmony
* Moonriver
* Moonbeam

### Chain-specific System Invariates

The chain-specific invariants are given in the `MesonConfig.sol` file. The [compile and deploy script](https://github.com/MesonFi/meson-contracts-solidity#deployment) will automatically set this config file.

* `SHORT_COIN_TYPE` (uint16): The identifier of the chain. We use the last 2 bytes of [SLIP-44](https://github.com/satoshilabs/slips/blob/master/slip-0044.md) as the unique ID of a chain:

  | Chain     | Short Coin Type |
  | --------- | --------------- |
  | Ethereum  | 0x003c          |
  | Tron      | 0x00c3          |
  | Conflux   | 0x01f7          |
  | Optimism  | 0x0266          |
  | BNB Chain | 0x02ca          |
  | Polygon   | 0x03c6          |
  | Fantom    | 0x03ef          |
  | Harmony   | 0x03ff          |
  | Moonbeam  | 0x0504          |
  | Moonriver | 0x0505          |
  | Aurora    | 0x0a0a          |
  | Evmos     | 0x11bc          |
  | Avalanche | 0x2328          |
  | Arbitrum  | 0x2329          |
* `MIN_BOND_TIME_PERIOD` (uint256) & `MAX_BOND_TIME_PERIOD` (uint256): The minimal and maximum expire time when bonding a swap, set to 1 hour and 2 hours, respectively. The swap encoding will include a timestamp `expireTs` before which the user's assets will be locked on the initial chain. The LP should call `executeSwap` before `expireTs` to take away the swapping fund. The `expireTs` needs to satisfy `ts_bonded_tx + MIN_BOND_TIME_PERIOD < expireTs < ts_bonded_tx + MAX_BOND_TIME_PERIOD`, where `ts_bonded_tx` is the block time for the executed `postSwap` transaction.
* `LOCK_TIME_PERIOD` (uint256): The time length when an LP locks a swap, sets to 40 minutes. The initiator should sign the release signature to get swapped assets on the target chain before the time `ts_locked_tx + LOCK_TIME_PERIOD`, where `ts_locked_tx` is the block time for the executed `lock` transaction.
* `REQUEST_TYPE_HASH` (bytes32): Equals to `keccak256(bytes32 "Sign to request a swap on Meson")` or `keccak256(bytes32 "Sign to request a swap on Meson (Testnet)")`. It's used when checking the request signature.
* `RELEASE_TYPE_HASH` (bytes32): Equals to `keccak256(bytes32 "Sign to release a swap on Meson" + bytes32 [Recipient])` or `keccak256(bytes32 "Sign to release a swap on Meson (Testnet)" + bytes32 "[Recipient]")`. It's used when checking the release signature.

### Source Code

{% embed url="<https://github.com/MesonFi/meson-contracts-solidity>" %}
Meson Smart Contracts
{% endembed %}
