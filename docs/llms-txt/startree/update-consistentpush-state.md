# Source: https://docs.startree.ai/api-reference/consistentpush/update-consistentpush-state.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update consistentPush state

## OpenAPI

````yaml post /segments/{tableNameWithType}/consistentPushRequest
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
  /segments/{tableNameWithType}/consistentPushRequest:
    post:
      tags:
        - ConsistentPush
      summary: Update consistentPush state
      operationId: updateConsistentPushState
      parameters:
        - name: tableNameWithType
          in: path
          description: Table Name with type
          required: true
          schema:
            type: string
        - name: taskType
          in: query
          description: task type, required
          required: true
          schema:
            type: string
      requestBody:
        description: Consistent Push Record
        content:
          '*/*':
            schema:
              $ref: '#/components/schemas/ConsistentPushExecutionRestRequest'
        required: true
      responses:
        default:
          description: successful operation
          content: {}
      security:
        - oauth: []
components:
  schemas:
    ConsistentPushExecutionRestRequest:
      type: object
      properties:
        consistentPushId:
          type: string
          readOnly: true
        checkpointId:
          type: string
          readOnly: true
        consistentPushSegmentMetadataList:
          type: array
          readOnly: true
          items:
            $ref: '#/components/schemas/ConsistentPushSegmentMetadata'
        segmentsFrom:
          type: array
          readOnly: true
          items:
            type: string
    ConsistentPushSegmentMetadata:
      type: object
      properties:
        segmentToName:
          type: string
          readOnly: true
        outputSegmentTarURI:
          type: string
          readOnly: true
  securitySchemes:
    oauth:
      type: apiKey
      description: The format of the key is  ```"Basic <token>" or "Bearer <token>"```
      name: Authorization
      in: header

````

Built with [Mintlify](https://mintlify.com).
