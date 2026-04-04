# Source: https://docs.pinata.cloud/sdk/types/keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Keys

### KeyPermissions

```typescript  theme={null}
export type KeyPermissions = {
	admin?: boolean;
	endpoints?: Endpoints;
};
```

### Endpoints

```typescript  theme={null}
export type Endpoints = {
	data?: DataEndponts;
	pinning?: PinningEndpoints;
};
```

### DataEndponts

```typescript  theme={null}
export type DataEndponts = {
	pinList?: boolean;
	userPinnedDataTotal?: boolean;
};
```

### PinningEndpoints

```typescript  theme={null}
export type PinningEndpoints = {
	hashMetadata?: boolean;
	hashPinPolicy?: boolean;
	pinByHash?: boolean;
	pinFileToIPFS?: boolean;
	pinJSONToIPFS?: boolean;
	pinJobs?: boolean;
	unpin?: boolean;
	userPinPolicy?: boolean;
};
```

### KeyOptions

```typescript  theme={null}
export type KeyOptions = {
	keyName: string;
	permissions: KeyPermissions;
	maxUses?: number;
};
```

### KeyResponse

```typescript  theme={null}
export type KeyResponse = {
	JWT: string;
	pinata_api_key: string;
	pinata_api_secret: string;
};
```

### KeyListQuery

```typescript  theme={null}
export type KeyListQuery = {
	revoked?: boolean;
	limitedUse?: boolean;
	exhausted?: boolean;
	name?: string;
	offset?: number;
};
```

### KeyListItem

```typescript  theme={null}
export type KeyListItem = {
	id: string;
	name: string;
	key: string;
	secret: string;
	max_uses: number;
	uses: number;
	user_id: string;
	scopes: KeyScopes;
	revoked: boolean;
	createdAt: string;
	updatedAt: string;
};
```

### KeyScopes

```typescript  theme={null}
type KeyScopes = {
	endpoints: {
		pinning: {
			pinFileToIPFS: boolean;
			pinJSONToIPFS: boolean;
		};
	};
	admin: boolean;
};
```

### KeyListResponse

```typescript  theme={null}
export type KeyListResponse = {
	keys: KeyListItem[];
	count: number;
};
```

### RevokeKeyResponse

```typescript  theme={null}
export type RevokeKeyResponse = {
	key: string;
	status: string;
};
```
