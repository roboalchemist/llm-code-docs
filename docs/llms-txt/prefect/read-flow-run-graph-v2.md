# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/flow-runs/read-flow-run-graph-v2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Flow Run Graph V2

> Get a graph of the tasks and subflow runs for the given flow run



## OpenAPI

````yaml get /flow_runs/{id}/graph-v2
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /flow_runs/{id}/graph-v2:
    get:
      tags:
        - Flow Runs
        - Flow Run Graph
      summary: Read Flow Run Graph V2
      description: Get a graph of the tasks and subflow runs for the given flow run
      operationId: read_flow_run_graph_v2_flow_runs__id__graph_v2_get
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The flow run id
            title: Id
          description: The flow run id
        - name: since
          in: query
          required: false
          schema:
            type: string
            format: date-time
            description: Only include runs that start or end after this time.
            default: '0001-01-01T00:00:00+00:00'
            title: Since
          description: Only include runs that start or end after this time.
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Graph'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Graph:
      properties:
        start_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Start Time
        end_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: End Time
        root_node_ids:
          items:
            type: string
            format: uuid
          type: array
          title: Root Node Ids
        nodes:
          items:
            prefixItems:
              - type: string
                format: uuid
              - $ref: '#/components/schemas/Node'
            type: array
            maxItems: 2
            minItems: 2
          type: array
          title: Nodes
        artifacts:
          items:
            $ref: '#/components/schemas/GraphArtifact'
          type: array
          title: Artifacts
        states:
          items:
            $ref: '#/components/schemas/GraphState'
          type: array
          title: States
      type: object
      required:
        - start_time
        - end_time
        - root_node_ids
        - nodes
        - artifacts
        - states
      title: Graph
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    GraphArtifact:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          type: string
          format: date-time
          title: Created
        key:
          anyOf:
            - type: string
            - type: 'null'
          title: Key
        type:
          anyOf:
            - type: string
            - type: 'null'
          title: Type
        is_latest:
          type: boolean
          title: Is Latest
        data:
          anyOf:
            - {}
            - type: 'null'
          title: Data
      type: object
      required:
        - id
        - created
        - key
        - type
        - is_latest
        - data
      title: GraphArtifact
    GraphState:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        timestamp:
          type: string
          format: date-time
          title: Timestamp
        type:
          $ref: '#/components/schemas/StateType'
        name:
          type: string
          title: Name
      type: object
      required:
        - id
        - timestamp
        - type
        - name
      title: GraphState
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    StateType:
      type: string
      enum:
        - SCHEDULED
        - PENDING
        - RUNNING
        - COMPLETED
        - FAILED
        - CANCELLED
        - CRASHED
        - PAUSED
        - CANCELLING
      title: StateType
      description: Enumeration of state types.

````

Built with [Mintlify](https://mintlify.com).