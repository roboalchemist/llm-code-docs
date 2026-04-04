# Source: https://docs.pinata.cloud/sdk/types/gateways.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# Gateways

### ContentType

```typescript  theme={null}
export type ContentType =
	| "application/json"
	| "application/xml"
	| "text/plain"
	| "text/html"
	| "text/css"
	| "text/javascript"
	| "application/javascript"
	| "image/jpeg"
	| "image/png"
	| "image/gif"
	| "image/svg+xml"
	| "audio/mpeg"
	| "audio/ogg"
	| "video/mp4"
	| "application/pdf"
	| "application/octet-stream"
	| string
	| null; // Allow for other MIME types
```

### GetCIDResponse

```typescript  theme={null}
export type GetCIDResponse = {
	data?: JSON | string | Blob | null;
	contentType: ContentType;
};
```

### OptimizeImageOptions

```typescript  theme={null}
export type OptimizeImageOptions = {
	width?: number;
	height?: number;
	dpr?: number;
	fit?: "scaleDown" | "contain" | "cover" | "crop" | "pad";
	gravity?: "auto" | "side" | string;
	quality?: number;
	format?: "auto" | "webp";
	animation?: boolean;
	sharpen?: number;
	onError?: boolean;
	metadata?: "keep" | "copyright" | "none";
};
```

### AccessLinkOptions

```typescript  theme={null}
export type AccessLinkOptions = {
	cid: string;
	date?: number;
	expires: number;
	gateway?: string;
};
```

### ContainsCIDResponse

```typescript  theme={null}
export type ContainsCIDResponse = {
	containsCid: boolean;
	cid: string | null;
};
```
