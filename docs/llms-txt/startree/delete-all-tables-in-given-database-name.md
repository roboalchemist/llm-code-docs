# Source: https://docs.startree.ai/api-reference/database/delete-all-tables-in-given-database-name.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete all tables in given database name

> Delete all tables in given database name

## OpenAPI

````yaml delete /databases/{databaseName}
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
  /databases/{databaseName}:
    delete:
      tags:
        - Database
      summary: Delete all tables in given database name
      description: Delete all tables in given database name
      operationId: deleteTablesInDatabase
      parameters:
        - name: databaseName
          in: path
          description: Database name
          required: true
          schema:
            type: string
        - name: dryRun
          in: query
          description: >-
            Run in dryRun mode initially to know the list of tables that will be
            deleted in actual run. No tables will be deleted when dryRun=true
          required: true
          schema:
            type: boolean
            default: true
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteDatabaseResponse'
      security:
        - oauth: []
components:
  schemas:
    DeleteDatabaseResponse:
      type: object
      properties:
        deletedTables:
          type: array
          readOnly: true
          items:
            type: string
        failedTables:
          type: array
          readOnly: true
          items:
            $ref: '#/components/schemas/DeletionFailureWrapper'
        dryRun:
          type: boolean
          readOnly: true
    DeletionFailureWrapper:
      type: object
      properties:
        tableName:
          type: string
          readOnly: true
        errorMessage:
          type: string
          readOnly: true
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
