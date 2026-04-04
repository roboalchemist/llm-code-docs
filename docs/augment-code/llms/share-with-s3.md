# Source: https://docs.augmentcode.com/context-services/context-connectors/quickstart/share-with-s3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Store Indexes in S3

> Store indexes in S3 for team sharing or application data management in 5 minutes

<Warning>
  **Experimental API** - Context Connectors is experimental and subject to breaking changes.
</Warning>

S3 storage enables two key use cases:

* **Team Sharing**: Multiple team members can search the same index
* **Application Data**: Build apps that manage per-user indexes in S3

## Prerequisites

* Node.js 18+
* Augment API credentials
* AWS credentials with S3 read/write access
* An S3 bucket

## Steps

### 1. Install

```bash  theme={null}
npm install @augmentcode/context-connectors @aws-sdk/client-s3
```

### 2. Set credentials

```bash  theme={null}
export AUGMENT_API_TOKEN='your-token'
export AUGMENT_API_URL='https://your-tenant.api.augmentcode.com/'
export AWS_ACCESS_KEY_ID='your-key'
export AWS_SECRET_ACCESS_KEY='your-secret'
```

### 3. Index to S3

```bash  theme={null}
export CC_S3_BUCKET='my-team-bucket'
npx ctxc index github --owner myorg --repo myrepo -i my-project \
  --store s3
```

You should see:

```
Fetching file tree from myorg/myrepo...
Indexing complete: 142 files indexed, 0 skipped
Stored to s3://my-team-bucket/context-connectors/my-project/
```

### 4. Search from S3

Anyone with AWS credentials can now search:

```bash  theme={null}
npx ctxc search "How does authentication work?" \
  -i s3://my-team-bucket/context-connectors/my-project
```

<Note>
  Indexes are stored under a `context-connectors/` prefix in your bucket. Include this prefix when searching.
</Note>

## Done!

Your index is stored in S3 at `s3://my-team-bucket/context-connectors/my-project/`. Share the S3 URL with your team.

## Also Works With

| Instead of...   | Try...                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| AWS S3          | MinIO: set `CC_S3_ENDPOINT` and `CC_S3_FORCE_PATH_STYLE=true`                                                 |
| AWS S3          | DigitalOcean Spaces, Backblaze B2, Cloudflare R2 (use `CC_S3_ENDPOINT`)                                       |
| Manual indexing | [Auto-index on push](/context-services/context-connectors/quickstart/auto-index-webhook) with GitHub webhooks |
