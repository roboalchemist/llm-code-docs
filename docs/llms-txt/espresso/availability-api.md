# Source: https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions/espresso-api/availability-api.md

# Source: https://docs.espressosys.com/network/api-reference/espresso-api/availability-api.md

# Availability API

The availability API is the place to get onchain data, like blocks and transactions. It is the primary interface for downstream components like rollups and end users.

The API is designed to be *robust* and *pure*. Robust means that if the node hosting the API misses some data, for example from being offline when a certain block was finalized, it will automatically fetch the missing data from a peer, and will eventually fetch and store all finalized data. Pure means that each endpoint is a pure function -- with the exception of occasionally returning 404 for missing data, each endpoint will always give the same response given the same parameters.

Due to purity, this API provides no aggregate queries, like block or transaction counts, which might change as missing data is fetched. Likewise, every endpoint takes some specification of the exact point in the chain the client is looking for, like a block height or hash. There is no "latest block" query. Thus, most real-world use cases will need to complement the availability API with use of the [node API](https://docs.espressosys.com/network/api-reference/espresso-api/node-api).

## Organization

While this API has many endpoints, don't be intimidated -- there is a method to the madness. The API is organized around collections of different resources, each of which corresponds to blocks and can be indexed by block height or hash.

### Resources

* Leaves
* Headers
* Blocks
* Block summaries
* Payloads
* VID common

### Indices

Each of these resources can be addressed in the following ways:

* `<resource>/:height`
* `<resource>/hash/:hash`
* `<resource>/payload-hash/:payload-hash`

{% hint style="warning" %}
Not all of the indices are implemented for all resources, although in principle they can be. The supported indices are documented below for each endpoint. Future releases will fill in the missing functionality.
{% endhint %}

{% hint style="warning" %}
Leaves are currently indexed slightly differently from other resources. See documentation on leaf endpoints. Future versions of this API will merge the concept of a leaf and a header, resolving this discrepancy.
{% endhint %}

In addition, there are endpoints to fetch a range of each resource (`<resource>/:form/:until`) and to subscribe to a WebSockets stream (`/stream/<resource>/:from`).

## Types

### `BlockSummary`

```json
{
    "header": Header,
    "hash": tagged<BLOCK>,
    "size": integer,
    "num_transactions": integer
}
```

### `BlockResponse`

```json
{
    "header": Header,
    "payload": Payload,
    "hash": tagged<BLOCK>,
    "size": integer,
    "num_transactions": integer
}
```

### `LeafResponse`

```json
{
    "leaf": Leaf,
    "qc": QC,
}
```

### `PayloadResponse`

```json
{
    "data": Payload,
    "height": integer,
    "size": integer,
    "block_hash": tagged<BLOCK>,
    "hash": tagged<HASH>
}
```

### `VidCommonResponse`

```json
{
    "common": VidCommon,
    "block_hash": tagged<BLOCK>,
    "payload_hash": tagged<HASH>
}
```

## Endpoints

### GET `/availability/leaf`

#### Paths

* `/availability/leaf/:height`
* `/availability/leaf/hash/:hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the leaf to fetch</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;COMMIT></code></td><td>Hash of the leaf to fetch</td></tr></tbody></table>

#### Returns `LeafResponse`

### GET `/availability/leaf/:from/:until`

Retrieve a range of consecutive leaves.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first leaf to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last leaf to fetch</td></tr></tbody></table>

#### Returns `[LeafResponse]`

### GET `/availability/stream/leaves/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of leaves, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first leaf to yield</td></tr></tbody></table>

#### Yields `LeafResponse`

### GET `/availability/header`

#### Paths

* `/availability/header/:height`
* `/availability/header/hash/:hash`
* `/availability/header/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the header to fetch</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the header to fetch</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the header to fetch. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `Header`

### GET `/availability/header/:from/:until`

Retrieve a range of consecutive headers.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first header to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last header to fetch</td></tr></tbody></table>

#### Returns `[Header]`

### GET `/availability/stream/headers/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of headers, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first header to yield</td></tr></tbody></table>

#### Yields `Header`

### GET `/availability/block`

#### Paths

* `/availability/block/:height`
* `/availability/block/hash/:hash`
* `/availability/block/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block to fetch</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block to fetch</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the block to fetch. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `BlockResponse`

### GET `/availability/block/:from/:until`

Retrieve a range of consecutive blocks.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first block to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last block to fetch</td></tr></tbody></table>

#### Returns `[BlockResponse]`

### GET `/availability/stream/blocks/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of blocks, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first block to yield</td></tr></tbody></table>

#### Yields `BlockResponse`

### GET `/availability/block/summary`

#### Paths

* `/availability/block/summary/:height`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block to fetch</td></tr></tbody></table>

#### Returns `BlockSummary`

### GET `/availability/block/summaries/:from/:until`

Retrieve a range of consecutive block summaries.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first block summary to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last block summary to fetch</td></tr></tbody></table>

#### Returns `[BlockSummary]`

### GET `/availability/payload`

#### Paths

* `/availability/payload/:height`
* `/availability/payload/block-hash/:block-hash`
* `/availability/payload/hash/:hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block whose payload should be fetched</td></tr><tr><td><code>block-hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block whose payload should be fetched</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload to fetch. Note that block payloads are not necessarily unique. If there are multiple payloads matching this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `PayloadResponse`

### GET `/availability/payload/:from/:until`

Retrieve a range of consecutive payloads.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>from</code></td><td><code>integer</code></td><td>Height of the first payload to fetch</td></tr><tr><td><code>until</code></td><td><code>integer</code></td><td>Height just after the last payload to fetch</td></tr></tbody></table>

#### Returns `[PayloadResponse]`

### GET `/availability/stream/payloads/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of payloads, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first payload to yield</td></tr></tbody></table>

#### Yields `PayloadResponse`

### GET `/availability/vid/common`

#### Paths

* `/availability/vid/common/:height`
* `/availability/vid/common/hash/:hash`
* `/availability/vid/common/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="171">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block whose VID common data should be fetched</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block whose VID common data should be fetched</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the block whose VID common data should be fetched. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns `VidCommonResponse`

### GET `/availability/stream/vid/common/:height`

{% hint style="info" %}
This is a WebSockets endpoint. The client must be prepared to upgrade the connection to a WebSockets connection, including the proper headers.
{% endhint %}

Subscribe to a stream of VID common objects, in order, starting from the given height.

#### Parameters

<table><thead><tr><th width="223">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the first VID common to yield</td></tr></tbody></table>

#### Yields `VidCommonResponse`

### GET `/availability/block/:height/namespace/:namespace`

Get the list of transactions in a block from a given namespace, along with a proof that these are only and all such transactions from that block. Note that the proof may be `null` if `transactions` is empty, in which case the caller should check the namespace table for the specified block to confirm that `:namespace` is not present.

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block containing the desired namespace</td></tr><tr><td><code>namespace</code></td><td><code>integer</code></td><td>ID of the desired namespace</td></tr></tbody></table>

#### Returns

```json
{
    "transactions": [Transaction],
    "proof": NsProof | null
}
```

### GET `/availability/transaction`

#### Paths

* `/availability/transaction/:height/:index`
* `/availability/transaction/hash/:hash`

#### Parameters

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block containing the desired transaction</td></tr><tr><td><code>index</code></td><td><code>integer</code></td><td>0-based position of the desired transaction in its block</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;TX></code></td><td>Hash of the desired transaction. Note that transactions are not necessarily unique. If there are multiple transactions matching this hash, <a data-footnote-ref href="#user-content-fn-1">it is unspecified which one is returned</a>.</td></tr></tbody></table>

#### Returns

```json
{
    "transaction": Transaction,
    "hash": tagged<TX>,
    "index": integer,
    "proof": TransactionInclusionProof,
    "block_hash": tagged<BLOCK>,
    "block_height": integer
}
```

The response contains the hash of the transaction, the hash and height of the block that contains it, and its index within that block. It also contains a `TransactionInclusionProof`, which proves inclusion of this transaction in the block with `block_hash`. The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`TxInclusionProof`](https://github.com/EspressoSystems/espresso-sequencer/blob/8ff3c9200b6bdefa9fa6f30b46b16a1b69cea5a1/sequencer/src/block/queryable.rs#L174) type.

### GET `/availability/limits`

Get implementation-defined limits restricting certain requests.

* `small_object_range_limit`: the maximum number of small objects which can be loaded in a single range query. Currently small objects include leaves only. In the future this limit will also apply to headers, block summaries, and VID common, however
  * loading of headers and block summaries is currently implemented by loading the entire block
  * imperfect VID parameter tuning means that VID common can be much larger than it should
* `large_object_range_limit`: the maximum number of large objects which can be loaded in a single range query. Large objects include anything that *might* contain a full payload or an object proportional in size to a payload. Note that this limit applies to the entire class of objects: we do not check the size of objects while loading to determine which limit to apply. If an object belongs to a class which might contain a large payload, the large object limit always applies.

**Returns**

```json
{
    "large_object_range_limit": integer,
    "small_object_range_limit": integer
}
```

### GET `/state-cert/epoch`

Get the light client state update certificate for the given epoch.

The light client state update certificate consists of the list of Schnorr signatures of the light client state at the end of the epoch. This is used to update light client state in the contract so that it have the new stake table information for the next epoch.

<table><thead><tr><th width="193">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>epoch</code></td><td><code>integer</code></td><td>Epoch number containing the desired state cert</td></tr></tbody></table>

**Returns**

```json
{
    "epoch": integer,
    "light_client_state": {
        "viewNum": integer,
        "blockHeight": integer,
        "blockCommRoot": BN256.ScalarField
    },
    "next_stake_table_state": tagged<STAKE_TABLE_STATE>,
    "signatures": [[tagged<SCHNORR_VER_KEY>, tagged<SCHNORR_SIG>]]
}
```

[^1]: This breaks purity. This will be addressed in a future version of the API.
