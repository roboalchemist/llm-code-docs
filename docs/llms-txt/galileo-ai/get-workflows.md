# Source: https://docs.galileo.ai/api-reference/observe/get-workflows.md

# Get Workflows

> Get workflows for a specific run in an Observe project.

## OpenAPI

````yaml https://api.acme.rungalileo.io/public/v1/openapi.json post /v1/observe/projects/{project_id}/workflows
paths:
  path: /v1/observe/projects/{project_id}/workflows
  method: post
  servers:
    - url: https://api.acme.rungalileo.io
      description: Galileo Public APIs - acme
  request:
    security:
      - title: APIKeyHeader
        parameters:
          query: {}
          header:
            Galileo-API-Key:
              type: apiKey
          cookie: {}
      - title: OAuth2PasswordBearer
        parameters:
          query: {}
          header:
            Authorization:
              type: oauth2
          cookie: {}
      - title: HTTPBasic
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
          cookie: {}
    parameters:
      path:
        project_id:
          schema:
            - type: string
              required: true
              title: Project Id
              format: uuid4
      query:
        start_time:
          schema:
            - type: string
              required: false
              title: Start Time
              format: date-time
            - type: 'null'
              required: false
              title: Start Time
        end_time:
          schema:
            - type: string
              required: false
              title: End Time
              format: date-time
            - type: 'null'
              required: false
              title: End Time
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              starting_token:
                allOf:
                  - type: integer
                    title: Starting Token
                    default: 0
              limit:
                allOf:
                  - type: integer
                    title: Limit
                    default: 100
              filters:
                allOf:
                  - items:
                      oneOf:
                        - $ref: '#/components/schemas/UserMetadataFilter'
                      discriminator:
                        propertyName: name
                        mapping:
                          user_metadata: '#/components/schemas/UserMetadataFilter'
                    type: array
                    title: Filters
            title: GetObserveWorkflowsRequest
            refIdentifier: '#/components/schemas/GetObserveWorkflowsRequest'
        examples:
          example:
            value:
              starting_token: 0
              limit: 100
              filters:
                - name: user_metadata
                  operator: one_of
                  key: <string>
                  value: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              starting_token:
                allOf:
                  - type: integer
                    title: Starting Token
                    default: 0
              limit:
                allOf:
                  - type: integer
                    title: Limit
                    default: 100
              paginated:
                allOf:
                  - type: boolean
                    title: Paginated
                    default: false
              next_starting_token:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Next Starting Token
              workflows:
                allOf:
                  - items:
                      $ref: '#/components/schemas/BaseGalileoStep'
                    type: array
                    title: Workflows
            title: WorkflowsReadResponse
            description: Response model for workflow evaluation results
            refIdentifier: '#/components/schemas/WorkflowsReadResponse'
            requiredProperties:
              - workflows
        examples:
          example:
            value:
              starting_token: 0
              limit: 100
              paginated: false
              next_starting_token: 123
              workflows:
                - type: workflow
                  input: <string>
                  redacted_input: <string>
                  output: <string>
                  redacted_output: <string>
                  name: ''
                  created_at_ns: 123
                  duration_ns: 0
                  metadata: {}
                  status_code: 123
                  ground_truth: <string>
                  root_workflow_id: <string>
                  workflow_id: <string>
                  step_id: <string>
                  steps:
                    - {}
                  metrics:
                    - name: <string>
                      value: <any>
                      status: <string>
                      explanation: <string>
                      rationale: <string>
                      cost: 123
                      model_alias: <string>
                      num_judges: 123
                      display_value: <any>
                      data_type: unknown
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    BaseGalileoStep:
      properties:
        type:
          $ref: '#/components/schemas/NodeType'
          description: Type of the step. By default, it is set to workflow.
          default: workflow
        input:
          type: string
          title: Input
          description: Input to the step.
        redacted_input:
          type: string
          title: Redacted Input
          description: >-
            Redacted input of the step. This is used to redact sensitive
            information.
        output:
          type: string
          title: Output
          description: Output of the step.
        redacted_output:
          type: string
          title: Redacted Output
          description: >-
            Redacted output of the step. This is used to redact sensitive
            information.
        name:
          type: string
          title: Name
          description: Name of the step.
          default: ''
        created_at_ns:
          type: integer
          title: Created At Ns
          description: Timestamp of the step's creation, as nanoseconds since epoch.
        duration_ns:
          type: integer
          title: Duration Ns
          description: Duration of the step in nanoseconds.
          default: 0
        metadata:
          additionalProperties:
            type: string
          type: object
          title: Metadata
          description: Metadata associated with this step.
        status_code:
          anyOf:
            - type: integer
            - type: 'null'
          title: Status Code
          description: Status code of the step. Used for logging failed/errored steps.
        ground_truth:
          anyOf:
            - type: string
            - type: 'null'
          title: Ground Truth
          description: Ground truth expected output for the step.
        root_workflow_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Root Workflow Id
        workflow_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Workflow Id
        step_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Step Id
        steps:
          anyOf:
            - items:
                $ref: '#/components/schemas/BaseGalileoStep'
              type: array
            - type: 'null'
          title: Steps
        metrics:
          items:
            $ref: '#/components/schemas/StepMetric'
          type: array
          title: Metrics
      additionalProperties: true
      type: object
      required:
        - input
      title: BaseGalileoStep
    DataTypeOptions:
      type: string
      enum:
        - unknown
        - text
        - label
        - floating_point
        - integer
        - timestamp
        - milli_seconds
        - boolean
        - uuid
        - percentage
        - dollars
        - array
        - template_label
        - thumb_rating_percentage
        - user_id
        - text_offsets
        - segments
        - hallucination_segments
        - thumb_rating
        - score_rating
        - star_rating
        - tags_rating
        - thumb_rating_aggregate
        - score_rating_aggregate
        - star_rating_aggregate
        - tags_rating_aggregate
      title: DataTypeOptions
    NodeType:
      type: string
      enum:
        - chain
        - chat
        - llm
        - retriever
        - tool
        - agent
        - workflow
        - trace
        - session
      title: NodeType
    StepMetric:
      properties:
        name:
          type: string
          title: Name
        value:
          title: Value
        status:
          anyOf:
            - type: string
            - type: 'null'
          title: Status
        explanation:
          anyOf:
            - type: string
            - type: 'null'
          title: Explanation
        rationale:
          anyOf:
            - type: string
            - type: 'null'
          title: Rationale
        cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Cost
        model_alias:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Alias
        num_judges:
          anyOf:
            - type: integer
            - type: 'null'
          title: Num Judges
        display_value:
          anyOf:
            - {}
            - type: 'null'
          title: Display Value
        data_type:
          $ref: '#/components/schemas/DataTypeOptions'
          default: unknown
      type: object
      required:
        - name
        - value
      title: StepMetric
    UserMetadataFilter:
      properties:
        name:
          type: string
          const: user_metadata
          title: Name
          default: user_metadata
        operator:
          type: string
          enum:
            - one_of
            - not_in
            - eq
            - ne
          title: Operator
        key:
          type: string
          title: Key
        value:
          anyOf:
            - type: string
            - items:
                type: string
              type: array
          title: Value
      type: object
      required:
        - operator
        - key
        - value
      title: UserMetadataFilter
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
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````