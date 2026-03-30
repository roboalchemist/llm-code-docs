# Source: https://docs.startree.ai/api-reference/user/update-user-config-for-a-user.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update user config for a user

> Update user config for user

## OpenAPI

````yaml put /users/{username}
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
  /users/{username}:
    put:
      tags:
        - User
      summary: Update user config for a user
      description: Update user config for user
      operationId: updateUserConfig
      parameters:
        - name: username
          in: path
          required: true
          schema:
            type: string
        - name: component
          in: query
          description: CONTROLLER|SERVER|BROKER
          schema:
            type: string
        - name: passwordChanged
          in: query
          schema:
            type: boolean
      requestBody:
        content:
          '*/*':
            schema:
              type: string
        required: false
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
