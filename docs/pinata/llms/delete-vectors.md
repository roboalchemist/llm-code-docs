# Source: https://docs.pinata.cloud/sdk/files/private/delete-vectors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# deleteVectors

> `org:files:write`

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud" target="_blank">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

Delete vectors for a given `fileId`

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example.mypinata.cloud",
});

const update = await pinata.files.private
  .deleteVectors("52681e41-86f4-407b-8f79-33a7e7e5df68")
```

## Returns

```typescript  theme={null}
type VectorizeFileResponse = {
	status: boolean;
};
```

## Parameters

### fileId

* Type: `string`

ID of the target file to delete vectors

```typescript {2} theme={null}
const update = await pinata.files.private
  .deleteVectors("52681e41-86f4-407b-8f79-33a7e7e5df68")
```
