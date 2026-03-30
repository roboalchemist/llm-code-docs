# Source: https://docs.startree.ai/api-reference/segment/get-selected-segments-timestamps.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get selected segments timestamps

> Get the selected segments given the (inclusive) start and (exclusive) end timestamps in milliseconds. These timestamps will be compared against  minmax values of the time column in each segment. If the table is a refresh use case, the value of start and end timestamp is voided, since there is no time column for refresh use case; instead, the whole qualified segments will be returned. If no timestamps are provided, all the qualified segments will be returned. For the segments that partially belong to the time range, the boolean flag 'excludeOverlapping' is introduced in order for user to determine whether to exclude this kind of segments in the response.

## OpenAPI

````yaml get /segments/{tableName}/select
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
  /segments/{tableName}/select:
    get:
      tags:
        - Segment
      summary: Get selected segments timestamps
      description: >-
        Get the selected segments given the (inclusive) start and (exclusive)
        end timestamps in milliseconds. These timestamps will be compared
        against  minmax values of the time column in each segment. If the table
        is a refresh use case, the value of start and end timestamp is voided,
        since there is no time column for refresh use case; instead, the whole
        qualified segments will be returned. If no timestamps are provided, all
        the qualified segments will be returned. For the segments that partially
        belong to the time range, the boolean flag 'excludeOverlapping' is
        introduced in order for user to determine whether to exclude this kind
        of segments in the response.
      operationId: getSelectedSegments
      parameters:
        - name: tableName
          in: path
          description: Name of the table
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: OFFLINE|REALTIME
          schema:
            type: string
        - name: startTimestamp
          in: query
          description: Start timestamp (inclusive) in milliseconds
          schema:
            type: string
        - name: endTimestamp
          in: query
          description: End timestamp (exclusive) in milliseconds
          schema:
            type: string
        - name: excludeOverlapping
          in: query
          description: >-
            Whether to exclude the segments overlapping with the timestamps,
            false by default
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: successful operation
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  additionalProperties:
                    type: array
                    items:
                      type: string
      deprecated: true
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
