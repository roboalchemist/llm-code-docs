# Source: https://docs.startree.ai/api-reference/cluster/update-groovy-static-analysis-configuration.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Groovy static analysis configuration

## OpenAPI

````yaml post /cluster/configs/groovy/staticAnalyzerConfig
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
  /cluster/configs/groovy/staticAnalyzerConfig:
    post:
      tags:
        - Cluster
      summary: Update Groovy static analysis configuration
      operationId: setGroovyStaticAnalysisConfig
      requestBody:
        content:
          '*/*':
            schema:
              type: object
              additionalProperties:
                $ref: '#/components/schemas/GroovyStaticAnalyzerConfig'
        required: false
      responses:
        '200':
          description: Success
          content: {}
        '500':
          description: Server error updating configuration
          content: {}
      security:
        - oauth: []
components:
  schemas:
    GroovyStaticAnalyzerConfig:
      type: object
      properties:
        allowedReceivers:
          type: array
          readOnly: true
          items:
            type: string
        allowedImports:
          type: array
          readOnly: true
          items:
            type: string
        allowedStaticImports:
          type: array
          readOnly: true
          items:
            type: string
        disallowedMethodNames:
          type: array
          readOnly: true
          items:
            type: string
        methodDefinitionAllowed:
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
