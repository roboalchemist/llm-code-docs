# Source: https://docs.startree.ai/api-reference/tenant/create-a-tenant.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a tenant

## OpenAPI

````yaml post /tenants
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
  /tenants:
    post:
      tags:
        - Tenant
      summary: ' Create a tenant'
      operationId: createTenant
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Tenant'
        required: false
      responses:
        '200':
          description: Success
          content: {}
        '500':
          description: Error creating tenant
          content: {}
      security:
        - oauth: []
        - database: []
components:
  schemas:
    Tenant:
      required:
        - tenantName
        - tenantRole
      type: object
      properties:
        tenantRole:
          type: string
          readOnly: true
          enum:
            - SERVER
            - BROKER
            - MINION
        tenantName:
          type: string
          readOnly: true
        numberOfInstances:
          type: integer
          format: int32
          readOnly: true
        offlineInstances:
          type: integer
          format: int32
          readOnly: true
        realtimeInstances:
          type: integer
          format: int32
          readOnly: true
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
