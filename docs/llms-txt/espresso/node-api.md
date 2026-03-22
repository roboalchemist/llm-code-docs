# Source: https://docs.espressosys.com/network/api-reference/espresso-api/earlier-versions/espresso-api/node-api.md

# Source: https://docs.espressosys.com/network/api-reference/espresso-api/node-api.md

# Node API

The [availability API](https://docs.espressosys.com/network/api-reference/espresso-api/availability-api) provides a pure view of snapshots of the Espresso blockchain at various points in time. Because it strives for robustness and purity, it does not include aggregate statistics like block or transaction counts, which may briefly return incorrect results and will gradually correct themselves as missing data is fetched. The node API does provide this data, making it a useful complement to the availability API.

In other words, while the availability API is a view of the blockchain abstractly, the node API provides information about *this node's* view of the chain, at the present moment in time.

## Endpoints

### GET `/node/block-height`

Get the height of the chain as known to this node. This is equal to one more than the height of the latest known block. It is *not* a count of the blocks in this node's database, as blocks earlier than the latest known block could be missing.

#### Returns `integer`

### GET `/node/transactions/count`

Get the number of finalized transactions. This count may be too low if blocks are missing from the database.

#### Returns `integer`

### GET `/node/payloads/total-size`

Get the total size, in bytes, of all finalized block payloads. This count may be too low if blocks are missing from the database.

#### Returns `integer`

### GET `/node/vid/share`

Get the VID share belonging to this node for a given block.

#### Paths

* `/node/vid/share/:height`
* `/node/vid/share/hash/:hash`
* `/node/vid/share/payload-hash/:payload-hash`

#### Parameters

<table><thead><tr><th width="183">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>height</code></td><td><code>integer</code></td><td>Height of the block whose VID share should be fetched</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Hash of the block whose VID share should be fetched</td></tr><tr><td><code>payload-hash</code></td><td><code>tagged&#x3C;HASH></code></td><td>Hash of the payload of the block whose VID share should be fetched. Note that block payloads are not necessarily unique. If there are multiple blocks whose payload matches this hash, it is unspecified which one is returned.</td></tr></tbody></table>

#### Returns `VidShare`

The specific format of this type is not currently specified, but it can be deserialized and interpreted in Rust using the [`VidShare`](https://hotshot.docs.espressosys.com/hotshot_types/vid/type.VidShare.html) type.

### GET `/node/sync-status`

Get the node's progress in syncing with the latest state of blockchain.

If the node is fully synced (that is, all the `missing` counts are 0 and `pruned_height` is `null` or 0) other endpoints in this API should give accurate results.

#### Returns

```json
{
    "missing_blocks": integer,
    "missing_leaves": integer,
    "missing_vid_common": integer,
    "missing_vid_shares": integer,
    "pruned_height": null | integer,
}
```

### GET `/node/header/window`

Get a range of consecutive headers by timestamp window.

Returns all available headers, in order, whose timestamps fall between `:start` (inclusive) and `:end` (exclusive), or between the block indicated by `:height` or `:hash` (inclusive) and `:end` (exclusive). The response also includes one block before the desired window (unless the window includes the genesis block) and one block after the window. This proves to the client that the server has not omitted any blocks whose timestamps fall within the desired window.

It is possible that not all blocks in the desired window are available when this endpoint is called. In that case, whichever blocks are available are included in the response, and `next` is `null` to indicate that the response is not complete. The client can then use one of the `/from/` forms of this endpoint to fetch the remaining blocks from where the first response left off, once they become available. If no blocks are available, not even `prev`, this endpoint will return an error.

#### Paths

* `/node/header/window/:start/:end`
* `/node/header/window/from/:height/:end`
* `/node/header/window/from/hash/:hash/:end`

#### Parameters

<table><thead><tr><th width="184">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>start</code></td><td><code>integer</code></td><td>Timestamp in seconds where the window should start</td></tr><tr><td><code>end</code></td><td><code>integer</code></td><td>Timestamp in seconds where the window should end</td></tr><tr><td><code>height</code></td><td><code>integer</code></td><td>Block height where the window should start</td></tr><tr><td><code>hash</code></td><td><code>tagged&#x3C;BLOCK></code></td><td>Block hash where the window should start</td></tr></tbody></table>

#### Returns

```json
{
    "window": Header,
    "prev": null | Header,
    "next": null | Header
}
```

### GET `/node/stake-table/current` , `/node/stake-table/:epoch`

Get the active stake table for the current epoch or the specified one.

<table><thead><tr><th width="184">Name</th><th width="193">Type</th><th>Description</th></tr></thead><tbody><tr><td><code>epoch</code></td><td><code>integer</code></td><td>The epoch number for which to get the stake table.</td></tr></tbody></table>

**Returns**

```json
{
    hex /* address */: {
        "account": hex, // address used to pay fees and collect rewards
        "stake_table_key": tagged<BLS_VER_KEY>,
        "state_ver_key": tagged<SCHNORR_VER_KEY>,
        "stake": integer,
        "commission" integer,
        "delegators": {
            hex /* address */: integer
        }
    }
}
```
