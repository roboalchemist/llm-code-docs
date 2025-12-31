# Source: https://docs.pinata.cloud/sdk/files/private/vectorize.md

# vectorize

> `org:files:write`

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud" target="_blank">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

Vectorize an existing file (must be part of a group)

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example.mypinata.cloud",
});

const update = await pinata.files.private
  .vectorize("52681e41-86f4-407b-8f79-33a7e7e5df68")
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

ID of the target file to vectorize

```typescript {2} theme={null}
const update = await pinata.files.private
  .vectorize("52681e41-86f4-407b-8f79-33a7e7e5df68")
```
