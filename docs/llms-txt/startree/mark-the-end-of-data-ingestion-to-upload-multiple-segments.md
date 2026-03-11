# Source: https://docs.startree.ai/api-reference/atomicingestion/mark-the-end-of-data-ingestion-to-upload-multiple-segments.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Mark the end of data ingestion to upload multiple segments

## OpenAPI

````yaml post /segments/{tableName}/endDataIngestRequest
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
  /segments/{tableName}/endDataIngestRequest:
    post:
      tags:
        - AtomicIngestion
      summary: Mark the end of data ingestion to upload multiple segments
      operationId: endDataIngestRequest
      parameters:
        - name: tableName
          in: path
          description: Name of the table
          required: true
          schema:
            type: string
        - name: tableType
          in: query
          description: OFFLINE|REALTIME
          required: true
          schema:
            type: string
        - name: taskType
          in: query
          description: Task type
          required: true
          schema:
            type: string
        - name: checkpointEntryKey
          in: query
          description: Key of checkpoint entry
          required: true
          schema:
            type: string
      requestBody:
        content:
          '*/*':
            schema:
              type: string
        required: false
      responses:
        default:
          description: successful operation
          content: {}
      security:
        - oauth: []
components:
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
