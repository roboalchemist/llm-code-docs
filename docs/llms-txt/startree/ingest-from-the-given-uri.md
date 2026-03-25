# Source: https://docs.startree.ai/api-reference/table/ingest-from-the-given-uri.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Ingest from the given URI

> Creates a segment using file at the given URI and pushes it to Pinot.
 All steps happen on the controller. This API is NOT meant for production environments/large input files.
Example usage (query params need encoding):

```
curl -X POST "http://localhost:9000/ingestFromURI?tableNameWithType=foo_OFFLINE
&batchConfigMapStr={
  "inputFormat":"json",
  "input.fs.className":"org.apache.pinot.plugin.filesystem.S3PinotFS",
  "input.fs.prop.region":"us-central",
  "input.fs.prop.accessKey":"foo",
  "input.fs.prop.secretKey":"bar"
}
&sourceURIStr=s3://test.bucket/path/to/json/data/data.json"
```

## OpenAPI

````yaml post /ingestFromURI
openapi: 3.0.1
info:
  title: Pinot Controller API
  description: APIs for accessing Pinot Controller information
  contact:
    name: https://github.com/apache/pinot
  version: '1.0'
servers:
  - url: https://dev.startree.ai/
security: []
tags:
  - name: AtomicIngestion
  - name: BatchRestart
  - name: ClusterHealth
  - name: Connection
  - name: ConsistentPush
  - name: DedupSnapshot
  - name: PerfAdvisor
  - name: RateLimiter
  - name: Table
  - name: Restream
  - name: Tuner
  - name: AlterTable
  - name: UpsertSnapshot
  - name: Cluster
  - name: User
  - name: Application
  - name: Broker
  - name: AppConfigs
  - name: Auth
  - name: Health
  - name: Logger
  - name: PeriodicTask
  - name: Database
  - name: Instance
  - name: Leader
  - name: Query
  - name: Schema
  - name: Segment
  - name: Tenant
  - name: Task
  - name: Upsert
  - name: Version
  - name: Zookeeper
paths:
  /ingestFromURI:
    post:
      tags:
        - Table
      summary: Ingest from the given URI
      description: >-
        Creates a segment using file at the given URI and pushes it to Pinot. 
         All steps happen on the controller. This API is NOT meant for production environments/large input files. 
        Example usage (query params need encoding):

        ```

        curl -X POST
        "http://localhost:9000/ingestFromURI?tableNameWithType=foo_OFFLINE

        &batchConfigMapStr={
          "inputFormat":"json",
          "input.fs.className":"org.apache.pinot.plugin.filesystem.S3PinotFS",
          "input.fs.prop.region":"us-central",
          "input.fs.prop.accessKey":"foo",
          "input.fs.prop.secretKey":"bar"
        }

        &sourceURIStr=s3://test.bucket/path/to/json/data/data.json"

        ```
      operationId: ingestFromURI
      parameters:
        - name: tableNameWithType
          in: query
          description: Name of the table to upload the file to
          required: true
          schema:
            type: string
        - name: batchConfigMapStr
          in: query
          description: >-
            Batch config Map as json string. Must pass inputFormat, and
            optionally input FS properties. e.g. {"inputFormat":"json"}
          required: true
          schema:
            type: string
        - name: sourceURIStr
          in: query
          description: URI of file to upload
          required: true
          schema:
            type: string
      responses:
        default:
          description: successful operation
          content: {}
      security:
        - oauth: []
        - database: []
components:
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header
    database:
      type: apiKey
      description: >-
        Database context passed through http header. If no context is provided
        'default' database context will be considered.
      name: database
      in: header

````

Built with [Mintlify](https://mintlify.com).
