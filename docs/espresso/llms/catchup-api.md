# Source: https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions/espresso-api/catchup-api.md

# Source: https://docs.espressosys.com/network/api-reference/espresso-api/catchup-api.md

# Catchup API

The primary customer of this API is peer consensus nodes who may have recently joined the network or were temporarily disconnected. These nodes need the very latest state, one which hasn't even been finalized yet, in order to start voting and proposing in consensus.

In HotShot, all state required to participate is represented in the form of Merkle trees or Merkle tries, so this API is able to provide select segments of the state with a proof that will convince the client that the returned segment is accurate, as long as they know the corresponding state *commitment*.

## Types

### `Account`

```json
{
    // Account balance in WEI. Serialized as a hex string so as not to exceed the
    // range of JSON integers.
    "balance": hex,
    // Merkle proof justifying "balance" relative to the state commitment.
    "proof": {
        "account": hex,
        "proof":
            { "Presence": MerkleProof },
          | { "Absence": MerkleProof }
        }
    }       
}
```

## Endpoints

### GET `/catchup/:height/:view/account/:address`

Get the balance of the requested fee account in the state from the requested consensus height and view. This is used to fetch the state for *unfinalized* views, to facilitate rapid catchup. If `:view` has already been finalized, this endpoint may fail with error 404.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>The account (Ethereum address) to look up</td></tr></tbody></table>

#### Returns `Account`

### POST `/catchup/:height/:view/accounts`

Bulk version of `/catchup/:height/:view/account`. The request body should be a JSON array consisting of `TaggedBase64`-encoded fee accounts.

The response is a `FeeMerkleTree` containing sub-trees for each of the requested accounts, which is\
a more condensed way to represent the union of account proofs for each requested account. Individual\
Merkle proofs for each account can be extracted from this tree.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr></tbody></table>

#### Returns `FeeMerkleTree`

### GET `/catchup/:height/:view/blocks`

Get the Merkle frontier (path to most recently inserted element) of the accumulator of blocks, from the requested consensus view. This is used to fetch the state for *unfinalized* views, to facilitate rapid catchup. If `:view` has already been finalized, this endpoint may fail with error 404.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the frontier</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the frontier</td></tr></tbody></table>

#### Returns `MerkleProof`

### GET `/catchup/chain-config/:commitment`

Get the chain config with the given hash.

#### Parameters

<table><thead><tr><th width="126.4453125">Name</th><th width="215.55859375">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>commitment</code></td><td><code>tagged&#x3C;CHAIN_CONFIG></code></td><td>The hash of the chain config to look up</td></tr></tbody></table>

**Returns** `ChainConfig`

### GET `/catchup/:height/leafchain`

Get a leaf chain which decides a specified block height. This endpoint can be used for catching up the stake table, where `:height` is the block height of the epoch root you want to catch up to.

#### Parameters

<table><thead><tr><th width="126.4453125">Name</th><th width="215.55859375">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height decided by the desired leaf chain</td></tr></tbody></table>

**Returns** `[Leaf]`

### GET `/catchup/:height/:view/reward-account/:address`

Get the balance of the requested reward account in the state from the requested consensus height and view. This is used to fetch the state for *unfinalized* views, to facilitate rapid catchup. If `:view` has already been finalized, this endpoint may fail with error 404.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr><tr><td><code>address</code></td><td><code>hex</code></td><td>The account (Ethereum address) to look up</td></tr></tbody></table>

#### Returns `Account`

### POST `/catchup/:height/:view/reward-accounts`

Bulk version of `/catchup/:height/:view/reward-account`. The request body should be a JSON array consisting of `TaggedBase64`-encoded fee accounts.

The response is a `RewardsMerkleTree` containing sub-trees for each of the requested accounts, which is a more condensed way to represent the union of account proofs for each requested account. Individual Merkle proofs for each account can be extracted from this tree.

{% hint style="warning" %}
`:height` and `:view` *must* correspond! `:height` is provided to simplify lookups for backends where data is not indexed by view.
{% endhint %}

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>The block height at which to look up the account balance</td></tr><tr><td><code>view</code></td><td><code>integer</code></td><td>The view from which to look up the account balance</td></tr></tbody></table>

#### Returns `RewardsMerkleTree`
