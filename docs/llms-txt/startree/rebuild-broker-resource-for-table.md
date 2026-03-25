# Source: https://docs.startree.ai/api-reference/table/rebuild-broker-resource-for-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rebuild broker resource for table

> when new brokers are added

## OpenAPI

````yaml post /tables/{tableName}/rebuildBrokerResourceFromHelixTags
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
  /tables/{tableName}/rebuildBrokerResourceFromHelixTags:
    post:
      tags:
        - Table
        - Tenant
      summary: Rebuild broker resource for table
      description: when new brokers are added
      operationId: rebuildBrokerResource
      parameters:
        - name: tableName
          in: path
          description: Table name (with type)
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Success
          content: {}
        '400':
          description: 'Bad request: table name has to be with table type'
          content: {}
        '500':
          description: Internal error rebuilding broker resource or serializing response
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
