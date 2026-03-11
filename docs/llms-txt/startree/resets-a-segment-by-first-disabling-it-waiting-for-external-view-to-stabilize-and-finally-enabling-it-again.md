# Source: https://docs.startree.ai/api-reference/segment/resets-a-segment-by-first-disabling-it-waiting-for-external-view-to-stabilize-and-finally-enabling-it-again.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Resets a segment by first disabling it, waiting for external view to stabilize, and finally enabling it again

> Resets a segment by disabling and then enabling it

## OpenAPI

````yaml post /segments/{tableNameWithType}/{segmentName}/reset
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
  /segments/{tableNameWithType}/{segmentName}/reset:
    post:
      tags:
        - Segment
      summary: >-
        Resets a segment by first disabling it, waiting for external view to
        stabilize, and finally enabling it again
      description: Resets a segment by disabling and then enabling it
      operationId: resetSegment
      parameters:
        - name: tableNameWithType
          in: path
          description: Name of the table with type
          required: true
          schema:
            type: string
        - name: segmentName
          in: path
          description: Name of the segment
          required: true
          schema:
            type: string
        - name: targetInstance
          in: query
          description: Name of the target instance to reset
          schema:
            type: string
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
      security:
        - oauth: []
        - database: []
components:
  schemas:
    SuccessResponse:
      type: object
      properties:
        status:
          type: string
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
