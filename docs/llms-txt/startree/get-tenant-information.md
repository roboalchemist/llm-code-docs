# Source: https://docs.startree.ai/api-reference/tenant/get-tenant-information.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get tenant information

## OpenAPI

````yaml get /tenants/{tenantName}/metadata
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
  /tenants/{tenantName}/metadata:
    get:
      tags:
        - Tenant
      summary: Get tenant information
      operationId: getTenantMetadata
      parameters:
        - name: tenantName
          in: path
          description: Tenant name
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: tenant type
          schema:
            type: string
            enum:
              - SERVER
              - BROKER
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TenantMetadata'
        '404':
          description: Tenant not found
          content: {}
        '500':
          description: Server error reading tenant information
          content: {}
      security:
        - oauth: []
        - database: []
components:
  schemas:
    TenantMetadata:
      type: object
      properties:
        ServerInstances:
          uniqueItems: true
          type: array
          items:
            type: string
        OfflineServerInstances:
          uniqueItems: true
          type: array
          items:
            type: string
        RealtimeServerInstances:
          uniqueItems: true
          type: array
          items:
            type: string
        BrokerInstances:
          uniqueItems: true
          type: array
          items:
            type: string
        tenantName:
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
