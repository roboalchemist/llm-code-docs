# Source: https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions/espresso-api.md

# Source: https://docs.espressosys.com/network/api-reference/espresso-api.md

# Espresso API

## Modularity

The Espresso API comprises several independent modules serving different purposes and requiring different resources. A given node may serve one, or all, or any combination of these modules, depending on its role in the system and the resources available to it. To see a list of the modules available from a particular node, navigate to the root URL of that node's API.

In brief, the available API modules are:

* [status-api](https://docs.espressosys.com/network/api-reference/espresso-api/status-api "mention"): node-specific state and consensus metrics
* [catchup-api](https://docs.espressosys.com/network/api-reference/espresso-api/catchup-api "mention"): serves recent consensus state to allow peers to catch up with the network
* [availability-api](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api "mention"): serves data recorded by the [Tiramisu DA layer](https://github.com/EspressoSystems/gitbook/blob/main/learn/the-espresso-network/properties-of-hotshot/espresso-data-availability-layer/README.md), such as committed blocks
* [node-api](https://docs.espressosys.com/network/api-reference/espresso-api/node-api "mention"): complements the availability API by serving eventually consistent data that is not (yet) necessarily agreed upon by all nodes
* [state-api](https://docs.espressosys.com/network/api-reference/espresso-api/state-api "mention"): serves consensus state derived from finalized blocks
* [events-api](https://docs.espressosys.com/network/api-reference/espresso-api/events-api "mention"): streams events from HotShot
* [submit-api](https://docs.espressosys.com/network/api-reference/espresso-api/submit-api "mention"): allows users to submit transactions to the public mempool

## Content Types

All APIs support JSON and binary formats in both request and response bodies.

* The JSON format is a straightforward serialization of the data types used internally by consensus nodes. In the future, a formal specification will be published, and the API will conform to that specification.
* The binary format is the [bincode](https://docs.rs/bincode/latest/bincode/) serialization of consensus data types, prefixed with an 8-byte version header. In the future, this will be replaced with a binary format with better cross-language support, and the data types will be defined by a published schema, rather than generated from code.

In requests and responses, the JSON format is denoted by the MIME type `application/json`, and the binary format by `application/octet-stream`. For requests with a body, the content type of the body must be set via the `Content-Type` header. The desired content type of the response can be controlled via the `Accept` header of the request. If the `Accept` header does not preference either format, JSON will be used by default.

## Server-Hosted Documentation

All Espresso API servers provide self-hosted API documentation, which makes it easy to see exactly what APIs the server supports, and can be easier to browse than these docs. The root URL of an application, e.g. `my-server.xyz`, lists the supported API modules and versions. Clicking on any API module, or navigating to the root of that API, e.g. `my-server.xyz/status`, documents the endpoints available in that module.

## Versioning and Stability

A node may serve multiple major versions of a given API at the same time. The desired version can be selected via a URL prefix. For example, `my-server.xyz/v0/status/metrics` and `my-server.xyz/v1/status/metrics` both hit the same endpoint, but in different API versions. A URL with no version segment will get a permanent redirect response to the latest supported version. In this case, `/status/metrics` would redirect to `/v1/status/metrics`.

Whenever a breaking change is made to an API, a new major version will be created, and the old version will continue to be served for some time, giving clients time to upgrade to the new version whenever it is convenient for them. Note that non-breaking changes, such as adding new endpoints, may be made in place to existing versions.

To see a list of versions of an API supported by a server, visit the root URL of that server.

### Version Support

<table><thead><tr><th width="79.67578125">Version</th><th width="277.54296875">Status</th><th>Comment</th></tr></thead><tbody><tr><td>v1</td><td>available on testnet April 15, 2025</td><td>Some APIs are changed and some endpoints added to support proof of stake</td></tr><tr><td>v0</td><td>latest version</td><td></td></tr></tbody></table>

This guide documents the most recent version `v1`, but archive API references are available for [earlier supported versions](https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions).

## Types

These types are used in requests and responses across many of the API modules.

### Primitives

#### Integer

We use `integer` to represent any JSON integer, with a maximum size of at least `2^63 - 1`. Of special note, byte arrays are sometimes represented as arrays of integers (`[integer]`). When the type `[integer]` is used as a byte array, each integer therein is restricted to the range `[0, 255]`.

#### Hex

In the following, we use the type `hex` to indicate a hex-encoded binary string, with `0x` prefix.

#### Base 64

In the following, we use the type `base64` to indicate a base64-encoded binary string, using the standard base 64 alphabet with padding.

#### Tagged Base 64

Some types use an enhanced [tagged base 64](https://docs.rs/tagged-base64/latest/tagged_base64/) encoding, which consists of a prefix identifying the type of the encoded object, a `~`, and then a base 64 string using the URL-safe base 64 alphabet without padding. The base 64 string encodes the binary representation of a typed object, plus a checksum. Because the encoding is URL-safe, these strings can be used not only in request and response bodies, but also in URL paths. The checksum allows the server to provide useful errors if a tagged base 64 string is mistyped or corrupted. The tag makes it easy for a human to tell different types of objects apart.

For example, a transaction hash might be encoded like `TX~QDuwVkmexu1fWgJbjxshXcGqXku838Pa9cTn0d-v3hZ-`, while a block hash could look like `BLOCK~00ISpu2jHbXD6z-BwMkwR4ijGdgUSoXLp_2jIStmqBrD`.

We use the type `tagged<TAG>` to indicate a tagged base 64 object with the given tag, as in `tagged<TX>` or `tagged<BLOCK>`.

### `NamespaceTable`

```json
{
    "bytes": base64
}
```

### `ChainConfig`

A chain config determines properties of consensus, such as the base fee for sequencing and the chain ID. To save space, it can be represented either as the full config object (`Left` variant below) or as a commitment to the chain config (`Right` variant). The genesis header will always contain the full config, so clients can fetch the full config from genesis and then compare its commitment against any other header.

```json
{
    "chain_config": 
        { "Left": { "chain_id": hex, "max_block_size": integer, "base_fee": hex } }
        | { "Right": tagged<CHAIN_CONFIG> }
}
```

### `Header`

```json
{
    "version": {
        "Version": {
            "major": integer,
            "minor": integer
        }
    },
    "fields": {
        "height": integer,
        "timestamp": integer,
        "l1_head": integer,
        "l1_finalized": null | {
            "number": integer,
            "timestamp": hex,
            "hash": hex
        },
        "payload_commitment": tagged<HASH>,
        "builder_commitment": tagged<BUILDER_COMMITMENT>,
        "ns_table": NamespaceTable,
        "block_merkle_tree_root": tagged<MERKLE_COMM>,
        "fee_merkle_tree_root": tagged<MERKLE_COMM>,
        "reward_merkle_tree_root": tagged<MERKLE_COMM>,
        "fee_info": { "account": hex, "amount": hex },
        "chain_config": ChainConfig
    }
}

```

### `Payload`

```json
{
    "raw_payload": base64,
    "ns_table": NamespaceTable
}
```

### `VidCommon`

```json
{
    "V0": {
        "poly_commits": tagged<FIELD>,
        "all_evals_digest": tagged<FIELD>,
        "payload_byte_len": integer,
        "num_storage_nodes": integer,
        "multiplicity": integer
    }
} | {
    "V1": {
        "total_weights": integer,
        "recovery_threshold": integer
    }  
}
```

### `Leaf`

```json
{
    "view_number": integer,
    "justify_qc": QC,
    "next_epoch_justify_qc": null | NextEpochQC,
    "parent_commitment": string,
    "block_header": Header,
    "upgrade_certificate": null | UpgradeCertificate,
    "view_change_evidence": null | ViewChangeEvidence,
    "next_drb_result": null | DrbResult,
    "with_epoch": bool
}
```

### `Transaction`

```json
{
    "namespace": integer,
    "payload": base64
}
```

{% hint style="warning" %}
If using the Rust API, you may notice that [`namespace`](https://github.com/EspressoSystems/espresso-sequencer/blob/main/types/src/v0/v0_1/transaction.rs#L41) is represented by a `u64`. However, some internal sub-protocols represent the namespace as a `u32`, and thus the maximum allowable namespace ID is `4294967295` (2^32 - 1). Larger namespace IDs will be rejected on transaction submission.
{% endhint %}

### `MerkleProof`

The low-level proof type for a Merklized data structure. The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`MerkleProof`](https://jellyfish.docs.espressosys.com/jf_primitives/merkle_tree/prelude/struct.MerkleProof.html) type.

### `NsIndex`

The 0-based position of a namespace in a [`NamespaceTable`](#namespacetable). The index is a little-endian byte-encoded 4-byte integer, as in `[3, 2, 1, 255]` (`0xff010203`).

### `NsProof`

A proof that a certain list of transactions corresponds to a certain namespace in a block.

```json
{
    "V0": {
        "ns_index": NsIndex,
        "ns_payload": base64, // binary encoding of the namespace data
        "ns_proof": {
            "prefix_elems": tagged<FIELD>,
            "suffix_elems": tagged<FIELD>,
            "prefix_bytes": [integer],
            "suffix_bytes": [integer]
        }
    }
} | {
    "V1": {
        "ns_index": NsIndex,
        "ns_payload": [integer],
        "ns_proof": MerkleProof
    }   
}
```

`V0.ns_proof` is a low-level range proof in the Espresso ADVZ VID scheme. The details of this proof are out of scope of this document, but this JSON object corresponds to the [`LargeRangeProofType`](https://hotshot.docs.espressosys.com/hotshot_types/vid/struct.LargeRangeProofType.html), and can be manipulated in Rust using that type.
