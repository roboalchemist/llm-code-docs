# Source: https://docs.pinata.cloud/sdk/signatures/public/delete.md

# Source: https://docs.pinata.cloud/sdk/signatures/private/delete.md

# Source: https://docs.pinata.cloud/sdk/groups/public/delete.md

# Source: https://docs.pinata.cloud/sdk/groups/private/delete.md

# Source: https://docs.pinata.cloud/sdk/files/public/delete.md

# Source: https://docs.pinata.cloud/sdk/files/private/delete.md

# delete

> `org:files:write`

Delte an array of files from your account

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const deletedFiles = await pinata.files.private.delete([
  "4ad9d3d1-4ab4-464c-a42a-3027fc39a546"
])
```

## Returns

```typescript  theme={null}
type DeleteResponse[] = {
  id: string;
  status: string;
};
```

## Parameters

### files

* Type: `string[]`

An array of file IDs you want to delete

```typescript  theme={null}
const unpin = await pinata.files.private
  .delete([
    "5e3011c0-f242-46b8-ad8d-2141bba23096",
    "e4cb100d-9065-4a08-80a3-f195f35de336"
  ])
```
