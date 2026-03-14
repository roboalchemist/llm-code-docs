# Source: https://docs.startree.ai/api-reference/segment/revert-segments-replacement.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Revert segments replacement

> Revert segments replacement

## OpenAPI

````yaml post /segments/{tableName}/revertReplaceSegments
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
  /segments/{tableName}/revertReplaceSegments:
    post:
      tags:
        - Segment
      summary: Revert segments replacement
      description: Revert segments replacement
      operationId: revertReplaceSegments
      parameters:
        - name: tableName
          in: path
          description: Name of the table
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: OFFLINE|REALTIME
          required: true
          schema:
            type: string
        - name: segmentLineageEntryId
          in: query
          description: Segment lineage entry id to revert
          required: true
          schema:
            type: string
        - name: forceRevert
          in: query
          description: >-
            Force revert in case the user knows that the lineage entry is
            interrupted
          schema:
            type: boolean
            default: false
      requestBody:
        description: Fields belonging to revert replace segment request
        content:
          '*/*':
            schema:
              $ref: '#/components/schemas/RevertReplaceSegmentsRequest'
        required: false
      responses:
        default:
          description: successful operation
          content: {}
      security:
        - oauth: []
        - database: []
components:
  schemas:
    RevertReplaceSegmentsRequest:
      type: object
      properties:
        customMap:
          type: object
          additionalProperties:
            type: string
          readOnly: true
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
