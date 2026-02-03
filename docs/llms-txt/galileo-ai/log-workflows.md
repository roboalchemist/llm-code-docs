# Source: https://docs.galileo.ai/api-reference/observe/log-workflows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Log Workflows to an Observe Project

> Log workflows to an Observe project.

Use this endpoint to log workflows to an Observe project. The request body should contain the
`workflows` to be ingested.

Additionally, specify the `project_id` or `project_name` to which the workflows should be ingested.
If the project does not exist, it will be created. If the project exists, the workflows will be logged to it.
If both `project_id` and `project_name` are provided, `project_id` will take precedence.

### WorkflowStep

A workflow step is the atomic unit of logging to Galileo. They represent a single execution of a workflow, such as a chain, agent, or a RAG execution. Workflows can have multiple steps, each of which can be a different type of node, such as an LLM, Retriever, or Tool.

You can log multiple workflows in a single request. Each workflow step must have the following fields:

* `type`: The type of the workflow.
* `input`: The input to the workflow.
* `output`: The output of the workflow.

## Examples

### LLM Step

```json  theme={null}
{
  "type": "llm",
  "input": "What is the capital of France?",
  "output": "Paris"
}
```

### Retriever Step

```json  theme={null}
{
  "type": "retriever",
  "input": "What is the capital of France?",
  "output": [{ "content": "Paris is the capital and largest city of France." }]
}
```

### Multi-Step

Workflow steps of type `workflow`, `agent` or `chain` can have sub-steps with children. A workflow with a retriver and an LLM step would look like this:

```json  theme={null}
{
  "type": "workflow",
  "input": "What is the capital of France?",
  "output": "Paris",
  "steps": [
    {
      "type": "retriever",
      "input": "What is the capital of France?",
      "output": [{ "content": "Paris is the capital and largest city of France." }]
    },
    {
      "type": "llm",
      "input": "What is the capital of France?",
      "output": "Paris"
    }
  ]
}
```


## OpenAPI

````yaml POST /v1/observe/workflows
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.staging.galileo.ai
    description: Galileo Public APIs - staging
security: []
paths:
  /v1/observe/workflows:
    post:
      tags:
        - observe
      summary: Log Workflows
      description: >-
        Log workflows to an Observe project.


        Use this endpoint to log workflows to an Observe project. The request
        body should contain the

        `workflows` to be ingested.


        Additionally, specify the `project_id` or `project_name` to which the
        workflows should be ingested.

        If the project does not exist, it will be created. If the project
        exists, the workflows will be logged to it.

        If both `project_id` and `project_name` are provided, `project_id` will
        take precedence.
      operationId: log_workflows_v1_observe_workflows_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WorkflowsIngestRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WorkflowsIngestResponse'
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
    WorkflowsIngestRequest:
      properties:
        workflows:
          items:
            oneOf:
              - $ref: '#/components/schemas/WorkflowStep'
              - $ref: '#/components/schemas/ChainStep'
              - $ref: '#/components/schemas/LlmStep'
              - $ref: '#/components/schemas/RetrieverStep'
              - $ref: '#/components/schemas/ToolStep'
              - $ref: '#/components/schemas/AgentStep'
            discriminator:
              propertyName: type
              mapping:
                agent: '#/components/schemas/AgentStep'
                chain: '#/components/schemas/ChainStep'
                llm: '#/components/schemas/LlmStep'
                retriever: '#/components/schemas/RetrieverStep'
                tool: '#/components/schemas/ToolStep'
                workflow: '#/components/schemas/WorkflowStep'
          type: array
          minItems: 1
          title: Workflows
          description: List of workflows to log.
        project_id:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          title: Project Id
          description: Project ID for the Observe project.
        project_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Project Name
          description: Project name for the Observe project.
      type: object
      required:
        - workflows
      title: WorkflowsIngestRequest
      examples:
        - project_name: my-observe-project
          workflows:
            - created_at_ns: 1769195837805226000
              duration_ns: 0
              input: who is a smart LLM?
              metadata: {}
              name: llm
              output: I am!
              type: llm
        - project_id: 00000000-0000-0000-0000-000000000000
          workflows:
            - created_at_ns: 1769195837805279700
              duration_ns: 0
              input: who is a smart LLM?
              metadata: {}
              name: llm
              output: I am!
              type: llm
    WorkflowsIngestResponse:
      properties:
        message:
          type: string
          title: Message
        project_id:
          type: string
          format: uuid4
          title: Project Id
        project_name:
          type: string
          title: Project Name
        workflows_count:
          type: integer
          title: Workflows Count
        records_count:
          type: integer
          title: Records Count
      type: object
      required:
        - message
        - project_id
        - project_name
        - workflows_count
        - records_count
      title: WorkflowsIngestResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    WorkflowStep:
      properties:
        type:
          type: string
          const: workflow
          title: Type
          description: Type of the step. By default, it is set to workflow.
          default: workflow
        input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Input
          description: Input to the step.
        redacted_input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Redacted Input
          description: >-
            Redacted input of the step. This is used to redact sensitive
            information.
        output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Output
          description: Output of the step.
          default: ''
        redacted_output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
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
        steps:
          items:
            oneOf:
              - $ref: '#/components/schemas/WorkflowStep'
              - $ref: '#/components/schemas/ChainStep'
              - $ref: '#/components/schemas/LlmStep'
              - $ref: '#/components/schemas/RetrieverStep'
              - $ref: '#/components/schemas/ToolStep'
              - $ref: '#/components/schemas/AgentStep'
            discriminator:
              propertyName: type
              mapping:
                agent: '#/components/schemas/AgentStep'
                chain: '#/components/schemas/ChainStep'
                llm: '#/components/schemas/LlmStep'
                retriever: '#/components/schemas/RetrieverStep'
                tool: '#/components/schemas/ToolStep'
                workflow: '#/components/schemas/WorkflowStep'
          type: array
          title: Steps
          description: Steps in the workflow.
        parent:
          anyOf:
            - $ref: '#/components/schemas/StepWithChildren'
            - type: 'null'
          description: Parent node of the current node. For internal use only.
      type: object
      required:
        - input
      title: WorkflowStep
    ChainStep:
      properties:
        type:
          type: string
          const: chain
          title: Type
          description: Type of the step. By default, it is set to chain.
          default: chain
        input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Input
          description: Input to the step.
        redacted_input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Redacted Input
          description: >-
            Redacted input of the step. This is used to redact sensitive
            information.
        output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Output
          description: Output of the step.
          default: ''
        redacted_output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
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
        steps:
          items:
            oneOf:
              - $ref: '#/components/schemas/WorkflowStep'
              - $ref: '#/components/schemas/ChainStep'
              - $ref: '#/components/schemas/LlmStep'
              - $ref: '#/components/schemas/RetrieverStep'
              - $ref: '#/components/schemas/ToolStep'
              - $ref: '#/components/schemas/AgentStep'
            discriminator:
              propertyName: type
              mapping:
                agent: '#/components/schemas/AgentStep'
                chain: '#/components/schemas/ChainStep'
                llm: '#/components/schemas/LlmStep'
                retriever: '#/components/schemas/RetrieverStep'
                tool: '#/components/schemas/ToolStep'
                workflow: '#/components/schemas/WorkflowStep'
          type: array
          title: Steps
          description: Steps in the workflow.
        parent:
          anyOf:
            - $ref: '#/components/schemas/StepWithChildren'
            - type: 'null'
          description: Parent node of the current node. For internal use only.
      type: object
      required:
        - input
      title: ChainStep
    LlmStep:
      properties:
        type:
          type: string
          const: llm
          title: Type
          description: Type of the step. By default, it is set to llm.
          default: llm
        input:
          anyOf:
            - type: string
            - additionalProperties:
                type: string
              type: object
            - $ref: '#/components/schemas/Message'
            - items:
                type: string
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
          title: Input
          description: Input to the LLM step.
        redacted_input:
          anyOf:
            - type: string
            - additionalProperties:
                type: string
              type: object
            - $ref: '#/components/schemas/Message'
            - items:
                type: string
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - type: 'null'
          title: Redacted Input
          description: >-
            Redacted input of the LLM step. This is used to redact sensitive
            information.
        output:
          anyOf:
            - type: string
            - additionalProperties:
                type: string
              type: object
            - $ref: '#/components/schemas/Message'
            - items:
                type: string
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
          title: Output
          description: Output of the LLM step.
          default: ''
        redacted_output:
          anyOf:
            - type: string
            - additionalProperties:
                type: string
              type: object
            - $ref: '#/components/schemas/Message'
            - items:
                type: string
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - type: 'null'
          title: Redacted Output
          description: >-
            Redacted output of the LLM step. This is used to redact sensitive
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
        tools:
          anyOf:
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Tools
          description: List of available tools passed to the LLM on invocation.
        model:
          anyOf:
            - type: string
            - type: 'null'
          title: Model
          description: Model used for this step.
        input_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Input Tokens
          description: Number of input tokens.
        output_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Output Tokens
          description: Number of output tokens.
        total_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Total Tokens
          description: Total number of tokens.
        temperature:
          anyOf:
            - type: number
            - type: 'null'
          title: Temperature
          description: Temperature used for generation.
        time_to_first_token_ms:
          anyOf:
            - type: number
            - type: 'null'
          title: Time To First Token Ms
          description: Time to first token in milliseconds.
      type: object
      required:
        - input
      title: LlmStep
    RetrieverStep:
      properties:
        type:
          type: string
          const: retriever
          title: Type
          description: Type of the step. By default, it is set to retriever.
          default: retriever
        input:
          type: string
          title: Input
          description: Input query to the retriever.
        redacted_input:
          anyOf:
            - type: string
            - type: 'null'
          title: Redacted Input
          description: >-
            Redacted input of the retriever step. This is used to redact
            sensitive information.
        output:
          items:
            $ref: '#/components/schemas/Document-Input'
          type: array
          title: Output
          description: >-
            Documents retrieved from the retriever. This can be a list of
            strings or `Document`s.
        redacted_output:
          anyOf:
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - type: 'null'
          title: Redacted Output
          description: >-
            Redacted output of the retriever step. This is used to redact
            sensitive information.
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
      type: object
      required:
        - input
      title: RetrieverStep
    ToolStep:
      properties:
        type:
          type: string
          const: tool
          title: Type
          description: Type of the step. By default, it is set to tool.
          default: tool
        input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Input
          description: Input to the step.
        redacted_input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Redacted Input
          description: >-
            Redacted input of the step. This is used to redact sensitive
            information.
        output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Output
          description: Output of the step.
          default: ''
        redacted_output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
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
      type: object
      required:
        - input
      title: ToolStep
    AgentStep:
      properties:
        type:
          type: string
          const: agent
          title: Type
          description: Type of the step. By default, it is set to agent.
          default: agent
        input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Input
          description: Input to the step.
        redacted_input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Redacted Input
          description: >-
            Redacted input of the step. This is used to redact sensitive
            information.
        output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Output
          description: Output of the step.
          default: ''
        redacted_output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
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
        steps:
          items:
            oneOf:
              - $ref: '#/components/schemas/WorkflowStep'
              - $ref: '#/components/schemas/ChainStep'
              - $ref: '#/components/schemas/LlmStep'
              - $ref: '#/components/schemas/RetrieverStep'
              - $ref: '#/components/schemas/ToolStep'
              - $ref: '#/components/schemas/AgentStep'
            discriminator:
              propertyName: type
              mapping:
                agent: '#/components/schemas/AgentStep'
                chain: '#/components/schemas/ChainStep'
                llm: '#/components/schemas/LlmStep'
                retriever: '#/components/schemas/RetrieverStep'
                tool: '#/components/schemas/ToolStep'
                workflow: '#/components/schemas/WorkflowStep'
          type: array
          title: Steps
          description: Steps in the workflow.
        parent:
          anyOf:
            - $ref: '#/components/schemas/StepWithChildren'
            - type: 'null'
          description: Parent node of the current node. For internal use only.
      type: object
      required:
        - input
      title: AgentStep
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
    Document-Input:
      properties:
        page_content:
          type: string
          title: Page Content
          description: Content of the document.
        metadata:
          additionalProperties:
            anyOf:
              - type: boolean
              - type: string
              - type: integer
              - type: number
          type: object
          title: Metadata
      additionalProperties: false
      type: object
      required:
        - page_content
      title: Document
    Message:
      properties:
        content:
          type: string
          title: Content
        role:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/MessageRole'
          title: Role
      additionalProperties: true
      type: object
      required:
        - content
        - role
      title: Message
    StepWithChildren:
      properties:
        type:
          $ref: '#/components/schemas/NodeType'
          description: Type of the step. By default, it is set to workflow.
          default: workflow
        input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Input
          description: Input to the step.
        redacted_input:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
          title: Redacted Input
          description: >-
            Redacted input of the step. This is used to redact sensitive
            information.
        output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
          title: Output
          description: Output of the step.
          default: ''
        redacted_output:
          anyOf:
            - type: string
            - $ref: '#/components/schemas/Document-Input'
            - $ref: '#/components/schemas/Message'
            - additionalProperties: true
              type: object
            - items:
                type: string
              type: array
            - items:
                $ref: '#/components/schemas/Document-Input'
              type: array
            - items:
                $ref: '#/components/schemas/Message'
              type: array
            - items:
                additionalProperties:
                  type: string
                type: object
              type: array
            - items:
                additionalProperties: true
                type: object
              type: array
            - type: 'null'
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
        steps:
          items:
            oneOf:
              - $ref: '#/components/schemas/WorkflowStep'
              - $ref: '#/components/schemas/ChainStep'
              - $ref: '#/components/schemas/LlmStep'
              - $ref: '#/components/schemas/RetrieverStep'
              - $ref: '#/components/schemas/ToolStep'
              - $ref: '#/components/schemas/AgentStep'
            discriminator:
              propertyName: type
              mapping:
                agent: '#/components/schemas/AgentStep'
                chain: '#/components/schemas/ChainStep'
                llm: '#/components/schemas/LlmStep'
                retriever: '#/components/schemas/RetrieverStep'
                tool: '#/components/schemas/ToolStep'
                workflow: '#/components/schemas/WorkflowStep'
          type: array
          title: Steps
          description: Steps in the workflow.
        parent:
          anyOf:
            - $ref: '#/components/schemas/StepWithChildren'
            - type: 'null'
          description: Parent node of the current node. For internal use only.
      type: object
      required:
        - input
      title: StepWithChildren
    MessageRole:
      type: string
      enum:
        - agent
        - assistant
        - function
        - system
        - tool
        - user
      title: MessageRole
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