# Source: https://docs.startree.ai/api-reference/table/delete-tables-partitions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete tables partitions

## OpenAPI

````yaml delete /tables/{tableNameWithType}/partitions
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
  /tables/{tableNameWithType}/partitions:
    delete:
      tags:
        - Table
      operationId: dropPartitionManager
      parameters:
        - name: tableNameWithType
          in: path
          description: Name of the table with type REALTIME
          required: true
          schema:
            type: string
        - name: serverIds
          in: query
          description: Comma separated server ids to be dropped
          schema:
            type: string
        - name: partitionIds
          in: query
          description: Comma separated partition ids to be dropped
          schema:
            type: string
        - name: dryRun
          in: query
          description: >-
            Run in dryRun mode initially to know the partitions that will be
            dropped on each server. No partitions will be dropped when
            dryRun=true
          required: true
          schema:
            type: boolean
            default: true
        - name: forceDelete
          in: query
          description: >-
            Run in forceDelete mode if all the partitions on the server to be
            deleted irrespective of number of primary keys. All partitions will
            be dropped when forceDelete=true
          required: true
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: successful operation
          content:
            '*/*':
              schema:
                type: string
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
