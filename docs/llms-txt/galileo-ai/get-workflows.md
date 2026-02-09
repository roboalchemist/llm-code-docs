# Source: https://docs.galileo.ai/api-reference/observe/get-workflows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Workflows

> Get workflows for a specific run in an Observe project.



## OpenAPI

````yaml https://api.staging.galileo.ai/public/v1/openapi.json post /v1/observe/projects/{project_id}/workflows
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.staging.galileo.ai
    description: Galileo Public APIs - staging
security: []
paths:
  /v1/observe/projects/{project_id}/workflows:
    post:
      tags:
        - observe
      summary: Get Workflows
      description: Get workflows for a specific run in an Observe project.
      operationId: get_workflows_v1_observe_projects__project_id__workflows_post
      parameters:
        - name: project_id
          in: path
          required: true
          schema:
            type: string
            format: uuid4
            title: Project Id
        - name: start_time
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: date-time
              - type: 'null'
            title: Start Time
        - name: end_time
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: date-time
              - type: 'null'
            title: End Time
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetObserveWorkflowsRequest'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WorkflowsReadResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - APIKeyHeader: []
        - OAuth2PasswordBearer: []
        - HTTPBasic: []
components:
  schemas:
    GetObserveWorkflowsRequest:
      properties:
        starting_token:
          type: integer
          title: Starting Token
          default: 0
        limit:
          type: integer
          title: Limit
          default: 100
        filters:
          items:
            oneOf:
              - $ref: '#/components/schemas/UserMetadataFilter'
            discriminator:
              propertyName: name
              mapping:
                user_metadata: '#/components/schemas/UserMetadataFilter'
          type: array
          title: Filters
      type: object
      title: GetObserveWorkflowsRequest
    WorkflowsReadResponse:
      properties:
        starting_token:
          type: integer
          title: Starting Token
          default: 0
        limit:
          type: integer
          title: Limit
          default: 100
        paginated:
          type: boolean
          title: Paginated
          default: false
        next_starting_token:
          anyOf:
            - type: integer
            - type: 'null'
          title: Next Starting Token
        workflows:
          items:
            $ref: '#/components/schemas/BaseGalileoStep'
          type: array
          title: Workflows
      type: object
      required:
        - workflows
      title: WorkflowsReadResponse
      description: Response model for workflow evaluation results
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: Galileo-API-Key
    OAuth2PasswordBearer:
      type: oauth2
      flows:
        password:
          scopes: {}
          tokenUrl: https://api.staging.galileo.ai/login
    HTTPBasic:
      type: http
      scheme: basic

````