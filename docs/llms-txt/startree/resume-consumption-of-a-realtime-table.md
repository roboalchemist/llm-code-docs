# Source: https://docs.startree.ai/api-reference/table/resume-consumption-of-a-realtime-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Resume consumption of a realtime table

> Resume the consumption for a realtime table. ConsumeFrom parameter indicates from which offsets consumption should resume. Recommended value is 'lastConsumed', which indicates consumption should continue based on the offsets in segment ZK metadata, and in case the offsets are already gone, the first available offsets are picked to minimize the data loss.

## OpenAPI

````yaml post /tables/{tableName}/resumeConsumption
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
  /tables/{tableName}/resumeConsumption:
    post:
      tags:
        - Table
      summary: Resume consumption of a realtime table
      description: >-
        Resume the consumption for a realtime table. ConsumeFrom parameter
        indicates from which offsets consumption should resume. Recommended
        value is 'lastConsumed', which indicates consumption should continue
        based on the offsets in segment ZK metadata, and in case the offsets are
        already gone, the first available offsets are picked to minimize the
        data loss.
      operationId: resumeConsumption
      parameters:
        - name: tableName
          in: path
          description: Name of the table
          required: true
          schema:
            type: string
        - name: comment
          in: query
          description: Comment on pausing the consumption
          schema:
            type: string
        - name: consumeFrom
          in: query
          description: lastConsumed (safer) | smallest (repeat rows) | largest (miss rows)
          schema:
            type: string
            default: lastConsumed
            enum:
              - lastConsumed
              - smallest
              - largest
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
