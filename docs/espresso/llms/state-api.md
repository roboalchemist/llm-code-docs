# Source: https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions/espresso-api/state-api.md

# Source: https://docs.espressosys.com/network/api-reference/espresso-api/state-api.md

# State API

All state derived from block data is represented in the form of Merkle trees or Merkle tries, so this API is able to provide select segments of the state with a proof that will convince the client that the returned segment is accurate, as long as they know the corresponding state *commitment* (part of each block header).

## Endpoints

### GET `/fee-state`

Get a Merkle proof proving the balance of a certain fee account in a given snapshot of the state. The element in the returned Merkle proof contains the balance of the requested account, or `null` if the account has no balance.

#### Paths

* `/fee-state/:height/:account`
* `/fee-state/commit/:commit/:account`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>account</code></td><td><code>hex</code></td><td>Fee account to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/fee-state/block-height`

The latest block height for which fee state is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the fee state storage is updated asynchronously.

#### Returns `integer`

## GET `/fee-state/fee-balance/latest/:account`

Convenience endpoint to get the current balance of an account from a trusted node.

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>account</code></td><td><code>hex</code></td><td>Fee account to look up</td></tr></tbody></table>

**Returns** the balance as a plain integer, without proof.

### GET `/block-state`

Get a Merkle proof proving the inclusion of a certain block at a position in the history. The element in the returned Merkle proof contains the commitment of the block at the requested position in history.

#### Paths

* `/block-state/:height/:index`
* `/block-state/commit/:commit/:index`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>index</code></td><td><code>integer</code></td><td>Height of the block to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/block-state/block-height`

The latest block height for which block state is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the block state storage is updated asynchronously.

#### Returns `integer`

## Reward State

The reward state API has two versions:

* **Protocol V3**: Uses reward state v1 with SHA3 hashing (`RewardMerkleTreeV1`)
* **Protocol V4+**: Uses reward state v2 with Keccak256 hashing (`RewardMerkleTreeV2`)

### GET `/reward-state`

Get a Merkle proof proving the balance of a certain reward account in a given snapshot of the state. The element in the returned Merkle proof contains the balance of the requested account, or `null` if the account has no balance.

This endpoint returns a V1 Merkle tree proof.

#### Paths

* `/reward-state/:height/:account`
* `/reward-state/commit/:commit/:account`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>account</code></td><td><code>hex</code></td><td>Reward account to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/reward-state/block-height`

The latest block height for which reward state is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the reward state storage is updated asynchronously.

#### Returns `integer`

### GET `/reward-state/proof/:height/:address`

Get the Merkle proof for a reward account at a given block height. Returns a `RewardAccountQueryDataV1` type, containing the balance and a `RewardAccountProofV1`. This proof is based on `RewardMerkleTreeV1`, which uses the SHA3 hashing algorithm.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height to get proof for</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>Account address to get proof for</td></tr></tbody></table>

#### Returns `RewardAccountQueryDataV1`

```json
{
  "balance": "0x...",
  "proof": {
    "account": "0x...",
    "proof": { /* merkle proof */ }
  }
}
```

**`RewardAccountQueryDataV1`** fields:

<table><thead><tr><th width="135">Field</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>balance</code></td><td><code>U256</code></td><td>The reward account balance</td></tr><tr><td><code>proof</code></td><td><code>RewardAccountProofV1</code></td><td>Merkle proof for the account</td></tr></tbody></table>

**`RewardAccountProofV1`** fields:

<table><thead><tr><th width="135">Field</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>account</code></td><td><code>Address</code></td><td>The reward account address</td></tr><tr><td><code>proof</code></td><td><code>RewardMerkleProofV1</code></td><td>Merkle proof using SHA3 hashing</td></tr></tbody></table>

## Reward State V2

Reward state v2 is used by consensus protocol V4 and above which uses Keccak256 based Merkle proofs for improved compatibility with Ethereum smart contracts.

### GET `/reward-state-v2`

Get a Merkle proof proving the balance of a certain reward account in a given snapshot of the state. The element in the returned Merkle proof contains the balance of the requested account, or `null` if the account has no balance.

#### Paths

* `/reward-state-v2/:height/:account`
* `/reward-state-v2/commit/:commit/:account`

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of the state snapshot to read from</td></tr><tr><td><code>commit</code></td><td><code>tagged&#x3C;MERKLE_COMM></code></td><td>Commitment of the state snapshot to read from</td></tr><tr><td><code>account</code></td><td><code>hex</code></td><td>Reward account to look up</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/reward-state-v2/block-height`

The latest block height for which reward state v2 is available.

Note that this may be less than the block height indicated by other APIs, such as [status](https://docs.espressosys.com/network/api-reference/espresso-api/status-api) or [node](https://docs.espressosys.com/network/api-reference/espresso-api/node-api), since the reward state storage is updated asynchronously.

#### Returns `integer`

### GET `/reward-state-v2/reward-balance/latest/:address`

Get current balance in reward state.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>address</code></td><td><code>hex</code></td><td>Ethereum address in hex format</td></tr></tbody></table>

#### Returns

The current reward balance as an integer.

### GET `/reward-state-v2/reward-balance/:height/:address`

Get balance in reward state at a specific height.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height to query</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>Ethereum address in hex format</td></tr></tbody></table>

#### Returns

The reward balance at the specified height as an integer.

### GET `/reward-state-v2/proof/:height/:address`

Get the Merkle proof for a reward account at a given block height. Returns a `RewardAccountQueryDataV2` type, containing the balance and a `RewardAccountProofV2`. This proof is based on `RewardMerkleTreeV2`, which uses the Keccak256 hashing algorithm.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height of proof for</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>Account address to get proof for</td></tr></tbody></table>

#### Returns `RewardAccountQueryDataV2`

```json
{
  "balance": "0x...",
  "proof": {
    "account": "0x...",
    "proof": {
      "Presence": { /* membership proof */ }
    }
  }
}
```

**`RewardAccountQueryDataV2`** fields:

<table><thead><tr><th width="135">Field</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>balance</code></td><td><code>U256</code></td><td>The reward account balance</td></tr><tr><td><code>proof</code></td><td><code>RewardAccountProofV2</code></td><td>Merkle proof for the account</td></tr></tbody></table>

**`RewardAccountProofV2`** fields:

<table><thead><tr><th width="135">Field</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>account</code></td><td><code>Address</code></td><td>The reward account address</td></tr><tr><td><code>proof</code></td><td><code>RewardMerkleProofV2</code></td><td>Merkle proof</td></tr></tbody></table>

**`RewardMerkleProofV2`** is an enum with two variants:

* **`Presence`**: Merkle proof demonstrating account membership in the tree
* **`Absence`**: Merkle proof demonstrating account non-membership in the tree

### GET `/reward-state-v2/reward-claim-input/:height/:address`

Get the reward claim input data formatted for use with Solidity reward claim contracts. This endpoint is only available for consensus protocol V4+.

#### Parameters

<table><thead><tr><th width="135">Name</th><th width="225">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Espresso block height (must match Light Client finalized height)</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>Account address to generate claim input for</td></tr></tbody></table>

#### Returns `RewardClaimInput`

```json
{
  "lifetime_rewards": "0x...",
  "auth_data": {
    // Authentication data including Merkle proof
  }
}
```

<table><thead><tr><th width="180">Field</th><th width="180">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>lifetime_rewards</code></td><td><code>U256</code></td><td>Total lifetime rewards for the account</td></tr><tr><td><code>auth_data</code></td><td><code>RewardAuthData</code></td><td>Merkle proof and authentication data for on-chain verification</td></tr></tbody></table>

* The `height` parameter **must match** the finalized block height in the Light Client contract
* Returns error if the account has zero rewards
* The returned data is formatted to be passed directly to reward claim contract functions

#### Error

* **`ZeroRewardError`**: Account has no rewards to claim
* **Conversion Error**: Failed to convert proof to claim input format
