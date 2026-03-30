# Source: https://docs.startree.ai/api-reference/clusterhealth/enable-disable-the-periodic-cluster-health-check-task-note-that-this-setting-isnt-persisted-across-controller-restarts-and-clusterconfigs-should-be-used-to-disable-it-permanently.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Enable / disable the periodic cluster health check task. Note that this setting isn't persisted across controller restarts and /cluster/configs should be used to disable it permanently

## OpenAPI

````yaml put /clusterHealth
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
    put:
      tags:
        - ClusterHealth
      summary: >-
        Enable / disable the periodic cluster health check task. Note that this
        setting isn't persisted across controller restarts and /cluster/configs
        should be used to disable it permanently
      operationId: toggleClusterHealthCheck
      parameters:
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
          description: successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
      security:
        - oauth: []
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

````

Built with [Mintlify](https://mintlify.com).
