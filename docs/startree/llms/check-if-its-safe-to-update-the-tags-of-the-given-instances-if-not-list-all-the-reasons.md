# Source: https://docs.startree.ai/api-reference/instance/check-if-its-safe-to-update-the-tags-of-the-given-instances-if-not-list-all-the-reasons.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Check if it's safe to update the tags of the given instances. If not list all the reasons

## OpenAPI

````yaml post /instances/updateTags/validate
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
  /instances/updateTags/validate:
    post:
      tags:
        - Instance
      summary: >-
        Check if it's safe to update the tags of the given instances. If not
        list all the reasons.
      operationId: instanceTagUpdateSafetyCheck
      requestBody:
        content:
          '*/*':
            schema:
              type: array
              items:
                $ref: '#/components/schemas/InstanceTagUpdateRequest'
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
    InstanceTagUpdateRequest:
      type: object
      properties:
        newTags:
          type: array
          items:
            type: string
        instanceName:
          type: string
          example: Server_a.b.com_20000
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
