# Source: https://docs.startree.ai/api-reference/table/lists-all-tables-in-cluster.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Lists all tables in cluster

> Lists all tables in cluster

## OpenAPI

````yaml get /mytables
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
  /mytables:
    get:
      tags:
        - Table
      summary: Lists all tables in cluster
      description: Lists all tables in cluster
      operationId: listTables
      parameters:
        - name: type
          in: query
          description: realtime|offline|dimension
          schema:
            type: string
        - name: taskType
          in: query
          description: Task type
          schema:
            type: string
        - name: sortType
          in: query
          description: name|creationTime|lastModifiedTime
          schema:
            type: string
        - name: sortAsc
          in: query
          description: true|false
          schema:
            type: boolean
            default: true
      responses:
        '200':
          description: successful operation
          content:
            application/json:
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
