# Source: https://docs.startree.ai/api-reference/segment/list-all-segments-an-optional-excludereplacedsegments-parameter-is-used-to-get-the-list-of-segments-which-has-not-yet-been-replaced-determined-by-segment-lineage-entries-and-can-be-queried-from-the-table-the-value-is-false-by-default.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List all segments. An optional 'excludeReplacedSegments' parameter is used to get the list of segments which has not yet been replaced (determined by segment lineage entries) and can be queried from the table. The value is false by default

> List all segments

## OpenAPI

````yaml get /segments/{tableName}
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
  /segments/{tableName}:
    get:
      tags:
        - Segment
      summary: >-
        List all segments. An optional 'excludeReplacedSegments' parameter is
        used to get the list of segments which has not yet been replaced
        (determined by segment lineage entries) and can be queried from the
        table. The value is false by default.
      description: List all segments
      operationId: getSegments
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
        - name: excludeReplacedSegments
          in: query
          description: >-
            Whether to exclude replaced segments in the response, which have
            been replaced specified in the segment lineage entries and cannot be
            queried from the table
          schema:
            type: string
        - name: startTimestamp
          in: query
          description: Start timestamp (inclusive)
          schema:
            type: string
        - name: endTimestamp
          in: query
          description: End timestamp (exclusive)
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
