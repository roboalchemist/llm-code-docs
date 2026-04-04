# Source: https://docs.meson.fi/protocol/system-design/relayer/apis.md

# Relayer APIs

The relayer provides the following APIs to receive swap request and release, and to query recent swaps.

The current Meson relayer is running at <https://relayer.meson.fi>.

### Submit a Swap Request

Receives an incoming swap request submitted by Meson app. Calling this API requires the swap request data and a valid user signature. The relayer will perform preliminary checks and broadcast the data to connected LP services if deemed valid.

```
POST https://relayer.meson.fi
```

**Request Body**

Example:

```json
// TODO give an example
{
  "encoded": ""
}
```

### Submit a Swap Release

Receives an incoming swap release submitted by Meson app. Calling this API requires the swap release data and a valid user signature. The relayer will perform preliminary checks and broadcast the data to connected LP services if deemed valid.

```
PUT https://relayer.meson.fi
```

**Request Body**

Example:

```json
// TODO give an example
{
  "encoded": ""
}
```

### Query Recent Swaps

Returns swaps form the pending pool, which are swaps that were submitted to the relayer recently but have not completed the entire swap process.

```
GET https://relayer.meson.fi
```

**Returns**

Example:

```json
// TODO give an example
[
  {
    "encoded": ""
  },
  ...
]
```
