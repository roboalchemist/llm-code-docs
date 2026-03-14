# Source: https://docs.startree.ai/api-reference/tenant/update-an-instance-partition-for-a-server-type-in-a-tenant.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update an instance partition for a server type in a tenant

## OpenAPI

````yaml put /tenants/{tenantName}/instancePartitions
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
  /tenants/{tenantName}/instancePartitions:
    put:
      tags:
        - Tenant
      summary: Update an instance partition for a server type in a tenant
      operationId: assignInstancesPartitionMap
      parameters:
        - name: tenantName
          in: path
          description: 'Tenant name '
          required: true
          schema:
            type: string
        - name: instancePartitionType
          in: query
          description: instancePartitionType (OFFLINE|CONSUMING|COMPLETED)
          required: true
          schema:
            type: string
            enum:
              - OFFLINE
              - CONSUMING
              - COMPLETED
      requestBody:
        content:
          application/json:
            schema:
              type: string
        required: false
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InstancePartitions'
        '400':
          description: Failed to deserialize/validate the instance partitions
          content: {}
        '500':
          description: Error updating the tenant
          content: {}
      security:
        - oauth: []
        - database: []
components:
  schemas:
    InstancePartitions:
      type: object
      properties:
        instancePartitionsName:
          type: string
          readOnly: true
        partitionToInstancesMap:
          type: object
          additionalProperties:
            type: array
            items:
              type: string
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
