# Source: https://docs.lancedb.com/storage/configuration.md

# Configuring Cloud Storage in LanceDB

> Configure LanceDB to use S3, GCS, Azure Blob, and S3-compatible object stores with environment variables or storage options.

export const TsStorageTigrisConnect = "async function storageTigrisConnect() {\n  const db = await lancedb.connect(\n    \"s3://your-bucket/path\",\n    {\n      storageOptions: {\n        endpoint: \"https://t3.storage.dev\",\n        region: \"auto\",\n      },\n    },\n  );\n  return db;\n}\n";

export const TsStorageTableTimeout = "async function storageTableTimeout() {\n  const db = await lancedb.connect(\"s3://bucket/path\");\n  const table = await db.createTable(\n    \"table\",\n    [{ a: 1, b: 2 }],\n    { storageOptions: { timeout: \"60s\" } },\n  );\n  return table;\n}\n";

export const TsStorageS3Minio = "async function storageS3Minio() {\n  const db = await lancedb.connect(\"s3://bucket/path\", {\n    storageOptions: {\n      region: \"us-east-1\",\n      endpoint: \"http://minio:9000\",\n    },\n  });\n  return db;\n}\n";

export const TsStorageS3Express = "async function storageS3Express() {\n  const db = await lancedb.connect(\n    \"s3://my-bucket--use1-az4--x-s3/path\",\n    {\n      storageOptions: {\n        region: \"us-east-1\",\n        s3Express: \"true\",\n      },\n    },\n  );\n  return db;\n}\n";

export const TsStorageS3Ddb = "async function storageS3Ddb() {\n  const db = await lancedb.connect(\n    \"s3+ddb://bucket/path?ddbTableName=my-dynamodb-table\",\n  );\n  return db;\n}\n";

export const TsStorageGcsServiceAccount = "async function storageGcsServiceAccount() {\n  const db = await lancedb.connect(\n    \"gs://my-bucket/my-database\",\n    {\n      storageOptions: {\n        serviceAccount: \"path/to/service-account.json\",\n      },\n    },\n  );\n  return db;\n}\n";

export const TsStorageConnectTimeout = "async function storageConnectTimeout() {\n  const db = await lancedb.connect(\"s3://bucket/path\", {\n    storageOptions: { timeout: \"60s\" },\n  });\n  return db;\n}\n";

export const TsStorageConnectS3 = "async function storageConnectS3() {\n  const db = await lancedb.connect(\"s3://bucket/path\");\n  return db;\n}\n";

export const TsStorageConnectGcs = "async function storageConnectGcs() {\n  const db = await lancedb.connect(\"gs://bucket/path\");\n  return db;\n}\n";

export const TsStorageConnectAzure = "async function storageConnectAzure() {\n  const db = await lancedb.connect(\"az://bucket/path\");\n  return db;\n}\n";

export const TsStorageAzureAccount = "async function storageAzureAccount() {\n  const db = await lancedb.connect(\n    \"az://my-container/my-database\",\n    {\n      storageOptions: {\n        accountName: \"some-account\",\n        accountKey: \"some-key\",\n      },\n    },\n  );\n  return db;\n}\n";

export const PyStorageTigrisConnect = "db = lancedb.connect(\n    \"s3://your-bucket/path\",\n    storage_options={\n        \"endpoint\": \"https://t3.storage.dev\",\n        \"region\": \"auto\",\n    },\n)\n";

export const PyStorageTableTimeout = "table = db.create_table(\n    \"table\",\n    [{\"a\": 1, \"b\": 2}],\n    storage_options={\"timeout\": \"60s\"},\n)\n";

export const PyStorageS3Minio = "db = lancedb.connect(\n    \"s3://bucket/path\",\n    storage_options={\n        \"region\": \"us-east-1\",\n        \"endpoint\": \"http://minio:9000\",\n    },\n)\n";

export const PyStorageS3Express = "db = lancedb.connect(\n    \"s3://my-bucket--use1-az4--x-s3/path\",\n    storage_options={\n        \"region\": \"us-east-1\",\n        \"s3_express\": \"true\",\n    },\n)\n";

export const PyStorageS3Ddb = "db = lancedb.connect(\n    \"s3+ddb://bucket/path?ddbTableName=my-dynamodb-table\",\n)\n";

export const PyStorageGcsServiceAccount = "db = lancedb.connect(\n    \"gs://my-bucket/my-database\",\n    storage_options={\n        \"service_account\": \"path/to/service-account.json\",\n    },\n)\n";

export const PyStorageConnectTimeout = "db = lancedb.connect(\n    \"s3://bucket/path\",\n    storage_options={\"timeout\": \"60s\"},\n)\n";

export const PyStorageConnectS3 = "db = lancedb.connect(\"s3://bucket/path\")\n";

export const PyStorageConnectGcs = "db = lancedb.connect(\"gs://bucket/path\")\n";

export const PyStorageConnectAzure = "db = lancedb.connect(\"az://bucket/path\")\n";

export const PyStorageAzureAccount = "db = lancedb.connect(\n    \"az://my-container/my-database\",\n    storage_options={\n        \"account_name\": \"some-account\",\n        \"account_key\": \"some-key\",\n    },\n)\n";

When using LanceDB OSS, you can choose where to store your data. The tradeoffs between storage options are covered in the [storage architecture guide](/storage). This page shows how to configure each backend.

## Object stores

LanceDB supports AWS S3 (and compatible stores), Azure Blob Storage, and Google Cloud Storage. The URI scheme in your `connect` call selects the backend.

<CodeGroup>
  <CodeBlock language="Python" title="AWS S3" icon="python">
    {PyStorageConnectS3}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="AWS S3" icon="square-js">
    {TsStorageConnectS3}
  </CodeBlock>
</CodeGroup>

<CodeGroup>
  <CodeBlock language="Python" title="Google Cloud Storage" icon="python">
    {PyStorageConnectGcs}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Google Cloud Storage" icon="square-js">
    {TsStorageConnectGcs}
  </CodeBlock>
</CodeGroup>

<CodeGroup>
  <CodeBlock language="Python" title="Azure Blob Storage" icon="python">
    {PyStorageConnectAzure}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Azure Blob Storage" icon="square-js">
    {TsStorageConnectAzure}
  </CodeBlock>
</CodeGroup>

### Configuration options

When running inside the target cloud with correct IAM bindings, LanceDB often needs no extra configuration. When running elsewhere, provide credentials via environment variables or `storage_options`.

<CodeGroup>
  <CodeBlock language="Python" title="Set a request timeout" icon="python">
    {PyStorageConnectTimeout}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Set a request timeout" icon="square-js">
    {TsStorageConnectTimeout}
  </CodeBlock>
</CodeGroup>

<Info title="Storage option casing">
  Keys are case-insensitive. Use lowercase in `storage_options` and uppercase in environment variables.
</Info>

If you need the option to apply only to a specific table:

<CodeGroup>
  <CodeBlock language="Python" title="Table-level storage options" icon="python">
    {PyStorageTableTimeout}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Table-level storage options" icon="square-js">
    {TsStorageTableTimeout}
  </CodeBlock>
</CodeGroup>

#### General object store options

| Key                          | Description                                                    |
| :--------------------------- | :------------------------------------------------------------- |
| `allow_http`                 | Allow non-TLS connections. Default: `false`.                   |
| `allow_invalid_certificates` | Skip certificate validation. Default: `false`.                 |
| `connect_timeout`            | Timeout for the connect phase. Default: `5s`.                  |
| `timeout`                    | Timeout for the full request. Default: `30s`.                  |
| `user_agent`                 | User agent string to send with requests.                       |
| `proxy_url`                  | Proxy URL to route requests through.                           |
| `proxy_ca_certificate`       | PEM-formatted CA certificate for proxy connections.            |
| `proxy_excludes`             | Comma-separated hosts that bypass the proxy (domains or CIDR). |

## AWS S3

<img src="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/aws.jpg?fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=e5ca36574c5c78fb379e1ffb0a6836bc" alt="" data-og-width="1560" width="1560" data-og-height="390" height="390" data-path="static/assets/images/storage/aws.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/aws.jpg?w=280&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=9bb03dfbcbfe030eb67558fe6799aed2 280w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/aws.jpg?w=560&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=002d8618e8de3026570b566a39d623c5 560w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/aws.jpg?w=840&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=5f65c8974785c09b723c64173d40088b 840w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/aws.jpg?w=1100&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=7a2b94edad05bb06a72c63de5c8a8b9d 1100w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/aws.jpg?w=1650&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=6b93d57505c690b6a3cea0562b46d94a 1650w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/aws.jpg?w=2500&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=b9a37023076f45b2a352617faa71165f 2500w" />

Set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and optionally `AWS_SESSION_TOKEN` as environment variables or pass them in `storage_options`. Region is optional for AWS but required for most S3-compatible stores.

Minimum permissions usually include `s3:PutObject`, `s3:GetObject`, `s3:DeleteObject`, `s3:ListBucket`, and `s3:GetBucketLocation` scoped to the relevant bucket/prefix.

### S3-compatible stores

<CodeGroup>
  <CodeBlock language="Python" title="Connect to an S3-compatible endpoint" icon="python">
    {PyStorageS3Minio}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Connect to an S3-compatible endpoint" icon="square-js">
    {TsStorageS3Minio}
  </CodeBlock>
</CodeGroup>

If the endpoint is `http://` (common in local development), also set `ALLOW_HTTP=true` or pass `allow_http=True` in `storage_options`.

### S3 Express

<CodeGroup>
  <CodeBlock language="Python" title="Use an S3 Express One Zone bucket" icon="python">
    {PyStorageS3Express}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Use an S3 Express One Zone bucket" icon="square-js">
    {TsStorageS3Express}
  </CodeBlock>
</CodeGroup>

Consult AWS networking requirements for S3 Express before enabling.

### DynamoDB commit store for concurrent writes

S3 lacks atomic writes. To enable safe concurrent writers, use DynamoDB as a commit store by switching to the `s3+ddb` scheme and specifying the table name.

<CodeGroup>
  <CodeBlock language="Python" title="Enable DynamoDB-backed commits" icon="python">
    {PyStorageS3Ddb}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Enable DynamoDB-backed commits" icon="square-js">
    {TsStorageS3Ddb}
  </CodeBlock>
</CodeGroup>

Create the DynamoDB table with hash key `base_uri` (string) and range key `version` (number). Small provisioned throughput (for example `ReadCapacityUnits=1`, `WriteCapacityUnits=1`) is sufficient for coordination.

<Tip title="Clean up failed multipart uploads">
  LanceDB aborts multipart uploads on graceful shutdown, but crashes can leave incomplete uploads. Add an S3 lifecycle rule to delete in-progress uploads after a few days.
</Tip>

## Google Cloud Storage

<img src="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/gcp.jpg?fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=c6e235e8dc41623579d507a8dd7d60ef" alt="" data-og-width="2920" width="2920" data-og-height="730" height="730" data-path="static/assets/images/storage/gcp.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/gcp.jpg?w=280&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=8d3f2ef82010242b45b095af18494c71 280w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/gcp.jpg?w=560&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=e5e9d48c064171b3f7cf353b1693f802 560w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/gcp.jpg?w=840&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=13029691b5d54eba67859ea8814517ab 840w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/gcp.jpg?w=1100&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=2ac9445521d0dd39ef02c98c9f8f1cc5 1100w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/gcp.jpg?w=1650&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=09f131fe81b125509f1d2195a0eb2626 1650w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/gcp.jpg?w=2500&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=1f2526ca3d95762cf41669371285377b 2500w" />

Provide credentials via `GOOGLE_SERVICE_ACCOUNT` (path to JSON) or include the path in `storage_options`. GCS defaults to HTTP/1; set `HTTP1_ONLY=false` if you need HTTP/2.

<CodeGroup>
  <CodeBlock language="Python" title="Connect with a service account" icon="python">
    {PyStorageGcsServiceAccount}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Connect with a service account" icon="square-js">
    {TsStorageGcsServiceAccount}
  </CodeBlock>
</CodeGroup>

## Azure Blob Storage

<img src="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/azure.jpg?fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=2ab2a9af6d996eb0cd0ca1273738f360" alt="" data-og-width="1202" width="1202" data-og-height="301" height="301" data-path="static/assets/images/storage/azure.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/azure.jpg?w=280&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=26a4fbd1d4a6646242907dd020453250 280w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/azure.jpg?w=560&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=4f5a506fb9123c986ba7161b5533059a 560w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/azure.jpg?w=840&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=484828fb1ddac405809853b23866fa6a 840w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/azure.jpg?w=1100&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=89df7139906fd0cca5a5a886d63bb059 1100w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/azure.jpg?w=1650&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=f208a55ba53e80fc0364f2225bb25df3 1650w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/azure.jpg?w=2500&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=06142dfedf9da16604d67f4ce01437be 2500w" />

Set `AZURE_STORAGE_ACCOUNT_NAME` and `AZURE_STORAGE_ACCOUNT_KEY` as environment variables, or pass them via `storage_options`.

<CodeGroup>
  <CodeBlock language="Python" title="Connect to Azure Blob Storage" icon="python">
    {PyStorageAzureAccount}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Connect to Azure Blob Storage" icon="square-js">
    {TsStorageAzureAccount}
  </CodeBlock>
</CodeGroup>

Other supported keys include service principal credentials (`azure_client_id`, `azure_client_secret`, `azure_tenant_id`), SAS tokens, managed identities, and custom endpoints.

## Tigris Object Storage

<img src="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/tigris.jpg?fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=572dbfe7dd0a3e125b36f73b33df5fda" alt="" data-og-width="2920" width="2920" data-og-height="730" height="730" data-path="static/assets/images/storage/tigris.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/tigris.jpg?w=280&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=90d80728fef13928015bbb09170bb9b8 280w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/tigris.jpg?w=560&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=f5ecca932948e015b218a6e8dbcc92d9 560w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/tigris.jpg?w=840&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=5bebd78eab3071e833acf3efbdb26f63 840w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/tigris.jpg?w=1100&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=9c4d45570acc84eb26bcb6f9ae64c01d 1100w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/tigris.jpg?w=1650&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=dfbab4509182a99d738700b27abe4881 1650w, https://mintcdn.com/lancedb-bcbb4faf/0sS6vrpmM3KSVyss/static/assets/images/storage/tigris.jpg?w=2500&fit=max&auto=format&n=0sS6vrpmM3KSVyss&q=85&s=87a45f95ce95b18f583403e108987480 2500w" />

Tigris exposes an S3-compatible API. Configure the endpoint and region:

<CodeGroup>
  <CodeBlock language="Python" title="Connect to Tigris Object Storage" icon="python">
    {PyStorageTigrisConnect}
  </CodeBlock>

  <CodeBlock language="TypeScript" title="Connect to Tigris Object Storage" icon="square-js">
    {TsStorageTigrisConnect}
  </CodeBlock>
</CodeGroup>

Environment variables `AWS_ENDPOINT=https://t3.storage.dev` and `AWS_DEFAULT_REGION=auto` achieve the same configuration.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lancedb.com/llms.txt