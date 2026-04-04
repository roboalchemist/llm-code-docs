# Source: https://docs.pinata.cloud/sdk/x402/payment-instructions/list.md

# Source: https://docs.pinata.cloud/sdk/x402/cids/list.md

# Source: https://docs.pinata.cloud/sdk/keys/list.md

# Source: https://docs.pinata.cloud/sdk/groups/public/list.md

# Source: https://docs.pinata.cloud/sdk/groups/private/list.md

# Source: https://docs.pinata.cloud/sdk/files/public/list.md

# Source: https://docs.pinata.cloud/sdk/files/private/list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# list

> `org:files:read`

List and filter files pinned to your Pinata account

## Usage

```typescript  theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const files = await pinata.files.pivate.list()
```

## Returns

```typescript  theme={null}
type FileListResponse = {
  files: FileListItem[];
  next_page_token: string;
};

type FileListItem = {
	id: string;
	name: string | null;
	cid: "pending" | string;
	size: number;
	numberOfFiles: number;
	mimeType: string;
	groupId: string;
	updatedAt: string;
	createdAt: string;
};
```

## Parameters

Filter response with the following additional methods. All filters are optional.

### name

* Type: `string`

Filter results based on name

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .name("pinnie")
```

### group

* Type: `string`

Filter results based on group ID

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .group("5b56981c-7e5b-4dff-aeca-de784728dddb")
```

### noGroup

* Type: `boolean`

Filter results to only show files that are not part of a group

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .noGroup(true)
```

### cid

* Type: `string`

Filter results based on CID

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .cid("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
```

### keyvalues

* Type: `Record<string, string>`

Filter results based on keyvalue pairs in metadata

```typescript {3-5} theme={null}
const files = await pinata.files.private
  .list()
  .keyvalues({
    env: "prod"
  })
```

### mimeType

* Type: `string`

Filter results based on mime type

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .mimeType("image/png")
```

### order

* Type: `"ASC" | "DESC"`

Order results either ascending or descending by created date

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .order("ASC")
```

### limit

* Type: `number`

Limit the number of results

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .limit(10)
```

### cidPending

* Type: `boolean`

Filters results and only returns files where `cid` is still `pending`

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .cid(true)
```

### pageToken

* Type: `string`

Paginates through files based on a provided page token

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .pageToken("MDE5MWIzZWYtM2U0Zi03YTY5LWE3OTQtOTRhZDE5NjQxMTk0")
```

## Auto Paginate

The `list` method has an auto pagination feature that is triggered when used inside a `for await` iterator

```typescript  theme={null}
for await (const item of pinata.files.private.list()) {
  console.log(item.id);
}
```

Works like magic ✨
