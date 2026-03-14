# Source: https://docs.startree.ai/api-reference/table/validate-table-config-for-a-table.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Validate table config for a table

> This API returns the table config that matches the one you get from 'GET /tables/{tableName}'. This allows us to validate table config before apply.

## OpenAPI

````yaml post /tables/validate
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
  /tables/validate:
    post:
      tags:
        - Table
      summary: Validate table config for a table
      description: >-
        This API returns the table config that matches the one you get from 'GET
        /tables/{tableName}'. This allows us to validate table config before
        apply.
      operationId: checkTableConfig
      parameters:
        - name: validationTypesToSkip
          in: query
          description: >-
            comma separated list of validation type(s) to skip. supported types:
            (ALL|TASK|UPSERT)
          schema:
            type: string
      requestBody:
        content:
          '*/*':
            schema:
              type: string
        required: false
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ObjectNode'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    ObjectNode:
      type: object
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
