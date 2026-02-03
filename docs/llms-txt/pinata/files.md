# Source: https://docs.pinata.cloud/sdk/types/files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Files

### FileObject

```typescript  theme={null}
export type FileObject = {
	name: string;
	size: number;
	type: string;
	lastModified: number;
	arrayBuffer: () => Promise<ArrayBuffer>;
};
```

### JsonBody

```typescript  theme={null}
export type JsonBody = Record<string, unknown>;
```

### PinataMetadata

```typescript  theme={null}
export type PinataMetadata = {
	name?: string;
	keyvalues?: Record<string, string>;
};
```

### UpdateFileOptions

```typescript  theme={null}
export type UpdateFileOptions = {
	id: string;
	name?: string;
	keyvalues?: Record<string, string>;
};
```

### DeleteResponse

```typescript  theme={null}
export type DeleteResponse = {
	id: string;
	status: string;
};
```

### FileListItem

```typescript  theme={null}
export type FileListItem = {
	id: string;
	name: string | null;
	cid: "pending" | string;
	size: number;
	number_of_files: number;
	mime_type: string;
	keyvalues: Record<string, string>;
	group_id: string | null;
	created_at: string;
};
```

### FileListResponse

```typescript  theme={null}
export type FileListResponse = {
	files: FileListItem[];
	next_page_token: string;
};
```

### FileListQuery

```typescript  theme={null}
export type FileListQuery = {
	name?: string;
	group?: string;
	noGroup?: boolean;
	mimeType?: string;
	cid?: string;
	cidPending?: boolean;
	metadata?: Record<string, string>;
	order?: "ASC" | "DESC";
	limit?: number;
	pageToken?: string;
};
```

### PinQueueQuery

```typescript  theme={null}
export type PinQueueQuery = {
	sort?: "ASC" | "DSC";
	status?:
		| "prechecking"
		| "retrieving"
		| "expired"
		| "backfilled
		| "over_free_limit"
		| "over_max_size"
		| "invalid_object"
		| "bad_host_node";
	ipfs_pin_hash?: string;
	limit?: number;
	pageToken?: string;
};
```

### PinQueueItem

```typescript  theme={null}
export type PinQueueItem = {
	id: string;
	cid?: string;
	ipfs_pin_hash?: string;
	date_queued: string;
	name: string;
	status: string;
	keyvalues: any;
	host_nodes: string[];
	pin_policy: {
		regions: {
			id: string;
			desiredReplicationCount: number;
		}[];
		version: number;
	};
};
```

### PinQueueResponse

```typescript  theme={null}
export type PinQueueResponse = {
	rows: PinQueueItem[];
	next_page_token: string;
};
```

### SwapCidOptions

```typescript  theme={null}
export type SwapCidOptions = {
	cid: string;
	swapCid: string;
};
```

### SwapHistoryOptions

```typescript  theme={null}
export type SwapHistoryOptions = {
	cid: string;
	domain: string;
};
```

### SwapCidResponse

```typescript  theme={null}
export type SwapCidResponse = {
	mapped_cid: string;
	created_at: string;
};
```

### VectorizeFileResponse

```typescript  theme={null}
export type VectorizeFileResponse = {
	status: boolean;
};
```

### VectorizeQuery

```typescript  theme={null}
export type VectorizeQuery = {
	groupId: string;
	query: string;
	returnFile?: boolean;
};
```

### VectorQueryMatch

```typescript  theme={null}
export type VectorQueryMatch = {
	file_id: string;
	cid: string;
	score: number;
};
```

### VectorizeQueryResponse

```typescript  theme={null}
export type VectorizeQueryResponse = {
	count: number;
	matches: VectorQueryMatch[];
};
```

***
