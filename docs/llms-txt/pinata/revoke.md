# Source: https://docs.pinata.cloud/sdk/keys/revoke.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# revoke

> `org:write`

Revoke an API Key

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const revoke = await pinata.keys.revoke([
 "94566af5e63833e260be"
]);
```

## Returns

```typescript  theme={null}
type RevokeKeyResponse[] = {
  key: string;
  status: string;
};
```

## Parameters

### keys

* Type: `string[]`

An array of API Keys to revoke. This is the `key` found in the response of `keys.list`

```typescript  theme={null}
const revoke = await pinata.keys.revoke([
 "94566af5e63833e260be"
]);
```
