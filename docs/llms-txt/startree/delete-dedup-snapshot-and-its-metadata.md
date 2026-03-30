# Source: https://docs.startree.ai/api-reference/dedupsnapshot/delete-dedup-snapshot-and-its-metadata.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete dedup snapshot and its metadata

## OpenAPI

````yaml delete /dedupSnapshots/{tableNameWithType}/snapshotAndMetadata
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
  /dedupSnapshots/{tableNameWithType}/snapshotAndMetadata:
    delete:
      tags:
        - DedupSnapshot
      summary: Delete dedup snapshot and its metadata
      operationId: deleteDedupSnapshotAndMetadata
      parameters:
        - name: tableNameWithType
          in: path
          description: Name of the table with type REALTIME
          required: true
          schema:
            type: string
        - name: snapshotName
          in: query
          description: >-
            Name of dedup snapshot to delete. If omit, all snapshots and their
            metadata are deleted
          schema:
            type: string
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
