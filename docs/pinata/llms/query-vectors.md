# Source: https://docs.pinata.cloud/sdk/files/private/query-vectors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# queryVectors

> `org:files:write`

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud" target="_blank">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

Query file vectors for a given `groupId`

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example.mypinata.cloud",
});

const update = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World"
})
```

## Returns

```typescript  theme={null}
type VectorizeQueryResponse = {
	count: number;
	matches: VectorQueryMatch[];
};

type VectorQueryMatch = {
	file_id: string;
	cid: string;
	score: number;
};

// If using returnFile

type GetCIDResponse = {
  data?: JSON | string | Blob | null;
  contentType: ContentType;
};
```

## Parameters

### groupId

* Type: `string`

ID of the target group to query vectors

```typescript {2} theme={null}
const results = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World"
})
```

### query

* Type: `string`

Query string

```typescript {3} theme={null}
const results = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World"
})
```

### returnFile (Optional)

* Type: `boolean`

Return the top matched file itself if set to true

```typescript {4} theme={null}
const { data, contentType }  = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World",
  returnFile: true
})
```
