# Source: https://docs.startree.ai/api-reference/clusterhealth/get-cached-cluster-health-details-for-all-pinot-entities.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get cached cluster health details for all pinot entities

## OpenAPI

````yaml get /clusterHealth
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
  /clusterHealth:
    get:
      tags:
        - ClusterHealth
      summary: Get cached cluster health details for all pinot entities
      operationId: getClusterHealthStatus
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClusterHealthCheckResult'
      security:
        - oauth: []
components:
  schemas:
    ClusterHealthCheckResult:
      type: object
      properties:
        runTimestamp:
          type: integer
          format: int64
        healthCheckResult:
          type: object
          additionalProperties:
            type: object
            additionalProperties:
              type: object
              additionalProperties:
                $ref: '#/components/schemas/HealthCheckResult'
    HealthCheckResult:
      type: object
      properties:
        pass:
          type: boolean
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
