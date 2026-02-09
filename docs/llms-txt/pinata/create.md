# Source: https://docs.pinata.cloud/sdk/x402/payment-instructions/create.md

# Source: https://docs.pinata.cloud/sdk/keys/create.md

# Source: https://docs.pinata.cloud/sdk/groups/public/create.md

# Source: https://docs.pinata.cloud/sdk/groups/private/create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# create

> `org:groups:write`

Create a private group

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const group = await pinata.groups.private.create({
	name: "My New Group",
});
```

## Returns

```typescript  theme={null}
type GroupResponseItem = {
    id: string;
    name: string;
    created_at: string;
};
```

## Parameters

### name

* Type: `string`

Requires a name for the group to be created

```typescript {2} theme={null}
const group = await pinata.groups.private.create({
	name: "My New Group",
});
```
