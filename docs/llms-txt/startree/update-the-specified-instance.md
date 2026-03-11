# Source: https://docs.startree.ai/api-reference/instance/update-the-specified-instance.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update the specified instance

> Update specified instance with given instance config

## OpenAPI

````yaml put /instances/{instanceName}
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
  /instances/{instanceName}:
    put:
      tags:
        - Instance
      summary: Update the specified instance
      description: Update specified instance with given instance config
      operationId: updateInstance
      parameters:
        - name: instanceName
          in: path
          description: Instance name
          required: true
          schema:
            type: string
          example: Server_a.b.com_20000 | Broker_my.broker.com_30000
        - name: updateBrokerResource
          in: query
          description: Whether to update broker resource for broker instance
          schema:
            type: boolean
            default: false
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Instance'
        required: false
      responses:
        '200':
          description: Success
          content: {}
        '500':
          description: Internal error
          content: {}
      security:
        - oauth: []
components:
  schemas:
    Instance:
      required:
        - host
        - port
        - type
      type: object
      properties:
        host:
          type: string
          readOnly: true
        port:
          type: integer
          format: int32
          readOnly: true
        type:
          type: string
          readOnly: true
          enum:
            - CONTROLLER
            - BROKER
            - SERVER
            - MINION
        tags:
          type: array
          readOnly: true
          items:
            type: string
        pools:
          type: object
          additionalProperties:
            type: integer
            format: int32
          readOnly: true
        grpcPort:
          type: integer
          format: int32
          readOnly: true
        adminPort:
          type: integer
          format: int32
          readOnly: true
        queryServicePort:
          type: integer
          format: int32
          readOnly: true
        queryMailboxPort:
          type: integer
          format: int32
          readOnly: true
        queriesDisabled:
          type: boolean
          readOnly: true
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
