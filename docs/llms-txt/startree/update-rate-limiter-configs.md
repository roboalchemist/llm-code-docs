# Source: https://docs.startree.ai/api-reference/ratelimiter/update-rate-limiter-configs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update rate limiter configs

> Update all the rate limiter configs

## OpenAPI

````yaml post /upsertRateLimitConfigs
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
  /upsertRateLimitConfigs:
    post:
      tags:
        - RateLimiter
      summary: Update rate limiter configs
      description: Update all the rate limiter configs
      operationId: updateUpsertRateLimiter
      parameters:
        - name: kvStoreFactoryName
          in: query
          description: KvStore factory scheme
          schema:
            type: string
            default: rocksdb
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties:
                type: string
        required: false
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RateLimiterResponse'
        '500':
          description: Server initialization error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorInfo'
      security:
        - oauth: []
components:
  schemas:
    RateLimiterResponse:
      type: object
      properties:
        updatedConfigs:
          type: object
          additionalProperties:
            type: string
          readOnly: true
    ErrorInfo:
      type: object
      properties:
        status:
          type: integer
          format: int32
        message:
          type: string
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
