# Source: https://docs.pinata.cloud/sdk/files/public/delete-swap.md

# Source: https://docs.pinata.cloud/sdk/files/private/delete-swap.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# deleteSwap

> `org:files:write`

Remove a CID swap for [Hot Swaps](/gateways/plugins/hot-swaps) plugin

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const deleteSwap = await pinata.files.private.deleteSwap(
  "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske"
)
```

## Returns

```typescript  theme={null}
OK
```

## Parameters

Pass in the required parameters below to remove a CID swap

### cid

* Type: `string`

This would be the original CID that was swapped

```typescript  theme={null}
const deleteSwap = await pinata.files.private.deleteSwap(
  "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske"
)
```
