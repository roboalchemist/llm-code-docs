# Source: https://docs.startree.ai/api-reference/broker/enabledisable-the-query-rate-limiting-for-a-broker-instance.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Enable/disable the query rate limiting for a broker instance

> Enable/disable the query rate limiting for a broker instance

## OpenAPI

````yaml post /brokers/instances/{instanceName}/qps
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
  /brokers/instances/{instanceName}/qps:
    post:
      tags:
        - Broker
      summary: Enable/disable the query rate limiting for a broker instance
      description: Enable/disable the query rate limiting for a broker instance
      operationId: toggleQueryRateLimiting
      parameters:
        - name: instanceName
          in: path
          description: Broker instance name
          required: true
          schema:
            type: string
          example: Broker_my.broker.com_30000
        - name: state
          in: query
          description: ENABLE|DISABLE
          required: true
          schema:
            type: string
            enum:
              - ENABLE
              - DISABLE
      responses:
        '200':
          description: Success
          content: {}
        '400':
          description: Bad Request
          content: {}
        '404':
          description: Instance not found
          content: {}
        '500':
          description: Internal error
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
