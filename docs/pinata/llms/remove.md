# Source: https://docs.pinata.cloud/sdk/x402/cids/remove.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# remove

Remove a CID association from a payment instruction

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const result = await pinata.x402.removeCid(
  "01234567-89ab-cdef-0123-456789abcdef",
  "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
);
```

## Returns

```typescript  theme={null}
type CidRemoveResponse = {
  data: {};
};
```

## Parameters

### paymentInstructionId (required)

* Type: `string`

The unique identifier of the payment instruction

```typescript  theme={null}
const result = await pinata.x402.removeCid(
  "01234567-89ab-cdef-0123-456789abcdef",
  "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
);
```

### cid (required)

* Type: `string`

The IPFS CID to remove from the payment instruction. Once removed, the content will no longer require payment for access through this instruction.

```typescript  theme={null}
const result = await pinata.x402.removeCid(
  "01234567-89ab-cdef-0123-456789abcdef",
  "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
);
```
