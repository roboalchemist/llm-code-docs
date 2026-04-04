# Source: https://docs.startree.ai/api-reference/auth/check-whether-authentication-is-enabled.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Check whether authentication is enabled

## OpenAPI

````yaml get /auth/verify
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
  /auth/verify:
    get:
      tags:
        - Auth
      summary: Check whether authentication is enabled
      operationId: verify
      parameters:
        - name: tableName
          in: query
          description: Table name without type
          schema:
            type: string
        - name: accessType
          in: query
          description: API access type
          schema:
            type: string
            default: READ
            enum:
              - CREATE
              - READ
              - UPDATE
              - DELETE
        - name: endpointUrl
          in: query
          description: Endpoint URL
          schema:
            type: string
      responses:
        '200':
          description: Verification result provided
          content: {}
        '500':
          description: Verification error
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
