# Source: https://docs.startree.ai/api-reference/zookeeper/create-a-node-at-a-given-path.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a node at a given path

## OpenAPI

````yaml post /zk/create
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
  /zk/create:
    post:
      tags:
        - Zookeeper
      summary: Create a node at a given path
      operationId: createNode
      parameters:
        - name: path
          in: query
          description: Zookeeper Path, must start with /
          required: true
          schema:
            type: string
        - name: ttl
          in: query
          description: >-
            TTL of the node. TTL are only honoured for persistent znodes (access
            option = 0x40 or 0x80), in which case TTL should be > 0. If access
            option is not 0x40 or 0x80, it will be ignored, and we can set it to
            any value, or just ignore it
          schema:
            type: integer
            format: int32
            default: -1
        - name: accessOption
          in: query
          description: accessOption
          schema:
            type: integer
            format: int32
            default: 1
      requestBody:
        content:
          application/json:
            schema:
              type: string
        required: false
      responses:
        '200':
          description: Success
          content: {}
        '204':
          description: No Content
          content: {}
        '400':
          description: Bad Request
          content: {}
        '500':
          description: Internal server error
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
