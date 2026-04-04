# Source: https://mastra.ai/reference/workspace/s3-filesystem

# S3Filesystem

Stores files in Amazon S3 or S3-compatible storage services like Cloudflare R2, MinIO, and DigitalOcean Spaces.

> **Info:** For interface details, see [WorkspaceFilesystem Interface](https://mastra.ai/reference/workspace/filesystem).

## Installation

```bash
npm install @mastra/s3
```

## Usage

Add an `S3Filesystem` to a workspace and assign it to an agent:

```typescript
import { Agent } from '@mastra/core/agent'
import { Workspace } from '@mastra/core/workspace'
import { S3Filesystem } from '@mastra/s3'

const workspace = new Workspace({
  filesystem: new S3Filesystem({
    bucket: 'my-bucket',
    region: 'us-east-1',
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
  }),
})

const agent = new Agent({
  name: 'file-agent',
  model: 'anthropic/claude-opus-4-5',
  workspace,
})
```

### Cloudflare R2

```typescript
import { S3Filesystem } from '@mastra/s3'

const filesystem = new S3Filesystem({
  bucket: 'my-r2-bucket',
  region: 'auto',
  endpoint: `https://${process.env.R2_ACCOUNT_ID}.r2.cloudflarestorage.com`,
  accessKeyId: process.env.R2_ACCESS_KEY_ID,
  secretAccessKey: process.env.R2_SECRET_ACCESS_KEY,
})
```

### MinIO

```typescript
import { S3Filesystem } from '@mastra/s3'

const filesystem = new S3Filesystem({
  bucket: 'my-bucket',
  region: 'us-east-1',
  endpoint: 'http://localhost:9000',
  accessKeyId: 'minioadmin',
  secretAccessKey: 'minioadmin',
})
```

## Constructor parameters

**bucket** (`string`): S3 bucket name

**region** (`string`): AWS region (use 'auto' for R2)

**accessKeyId** (`string`): AWS access key ID. Optional for public buckets (read-only access).

**secretAccessKey** (`string`): AWS secret access key. Optional for public buckets (read-only access).

**sessionToken** (`string`): AWS session token for temporary credentials. Required when using SSO, AssumeRole, container credentials, or any other temporary credential provider.

**endpoint** (`string`): Custom endpoint URL for S3-compatible storage (R2, MinIO, etc.)

**forcePathStyle** (`boolean`): Force path-style URLs instead of virtual-hosted-style. Required for some S3-compatible services like MinIO. Defaults to true when a custom endpoint is provided. (Default: `true (when endpoint is set)`)

**prefix** (`string`): Optional prefix for all keys (acts like a subdirectory)

**id** (`string`): Unique identifier for this filesystem instance (Default: `Auto-generated`)

**displayName** (`string`): Human-friendly display name for the UI

**icon** (`FilesystemIcon`): Icon identifier for the UI

**description** (`string`): Short description of this filesystem for the UI

**readOnly** (`boolean`): When true, all write operations are blocked (Default: `false`)

## Properties

**id** (`string`): Filesystem instance identifier

**name** (`string`): Provider name ('S3Filesystem')

**provider** (`string`): Provider identifier ('s3')

**bucket** (`string`): The S3 bucket name

**readOnly** (`boolean | undefined`): Whether the filesystem is in read-only mode

## Methods

S3Filesystem implements the [WorkspaceFilesystem interface](https://mastra.ai/reference/workspace/filesystem), providing all standard filesystem methods:

- `readFile(path, options?)` - Read file contents
- `writeFile(path, content, options?)` - Write content to a file
- `appendFile(path, content)` - Append content to a file
- `deleteFile(path, options?)` - Delete a file
- `copyFile(src, dest, options?)` - Copy a file
- `moveFile(src, dest, options?)` - Move or rename a file
- `mkdir(path, options?)` - Create a directory
- `rmdir(path, options?)` - Remove a directory
- `readdir(path, options?)` - List directory contents
- `exists(path)` - Check if a path exists
- `stat(path)` - Get file or directory metadata

### `init()`

Initialize the filesystem. Verifies bucket access and credentials.

```typescript
await filesystem.init()
```

### `getInfo()`

Returns metadata about this filesystem instance.

```typescript
const info = filesystem.getInfo()
// { id: '...', name: 'S3Filesystem', provider: 's3', status: 'ready' }
```

### `getMountConfig()`

Returns the mount configuration for sandboxes that support mounting this filesystem type.

```typescript
const config = filesystem.getMountConfig()
// { type: 's3', bucket: 'my-bucket', region: 'us-east-1', ... }
```

## Mounting in E2B Sandboxes

S3Filesystem can be mounted into E2B sandboxes, making the bucket accessible as a local directory:

```typescript
import { Workspace } from '@mastra/core/workspace'
import { S3Filesystem } from '@mastra/s3'
import { E2BSandbox } from '@mastra/e2b'

const workspace = new Workspace({
  mounts: {
    '/data': new S3Filesystem({
      bucket: 'my-bucket',
      region: 'us-east-1',
      accessKeyId: process.env.AWS_ACCESS_KEY_ID,
      secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
    }),
  },
  sandbox: new E2BSandbox({ id: 'dev-sandbox' }),
})
```

See [E2BSandbox reference](https://mastra.ai/reference/workspace/e2b-sandbox) for more details on mounting.

## Related

- [WorkspaceFilesystem interface](https://mastra.ai/reference/workspace/filesystem)
- [GCSFilesystem reference](https://mastra.ai/reference/workspace/gcs-filesystem)
- [E2BSandbox reference](https://mastra.ai/reference/workspace/e2b-sandbox)
- [Workspace overview](https://mastra.ai/docs/workspace/overview)