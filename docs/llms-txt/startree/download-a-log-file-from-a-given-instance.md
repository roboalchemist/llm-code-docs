# Source: https://docs.startree.ai/api-reference/logger/download-a-log-file-from-a-given-instance.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Download a log file from a given instance

## OpenAPI

````yaml get /loggers/instances/{instanceName}/download
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
  /loggers/instances/{instanceName}/download:
    get:
      tags:
        - Logger
      summary: Download a log file from a given instance
      operationId: downloadLogFileFromInstance
      parameters:
        - name: Authorization
          in: header
          schema:
            type: string
        - name: instanceName
          in: path
          description: Instance Name
          required: true
          schema:
            type: string
        - name: filePath
          in: query
          description: Log file path
          required: true
          schema:
            type: string
      responses:
        default:
          description: successful operation
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
