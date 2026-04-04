# Source: https://docs.pinata.cloud/sdk/types/groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Groups

### GroupOptions

```typescript  theme={null}
export type GroupOptions = {
	name: string;
	isPublic?: boolean;
};
```

### UpdateGroupOptions

```typescript  theme={null}
export type UpdateGroupOptions = {
	groupId: string;
	name?: string;
	isPublic?: boolean;
};
```

### GetGroupOptions

```typescript  theme={null}
export type GetGroupOptions = {
	groupId: string;
};
```

### GroupListResponse

```typescript  theme={null}
export type GroupListResponse = {
	groups: GroupResponseItem[];
	next_page_token: string;
};
```

### GroupResponseItem

```typescript  theme={null}
export type GroupResponseItem = {
	id: string;
	is_public: boolean;
	name: string;
	createdAt: string;
};
```

### GroupQueryOptions

```typescript  theme={null}
export type GroupQueryOptions = {
	name?: string;
	limit?: number;
	pageToken?: string;
	isPublic?: boolean;
};
```

### GroupCIDOptions

```typescript  theme={null}
export type GroupCIDOptions = {
	groupId: string;
	files: string[];
};
```

### UpdateGroupFilesResponse

```typescript  theme={null}
export type UpdateGroupFilesResponse = {
	id: string;
	status: string;
};
```
