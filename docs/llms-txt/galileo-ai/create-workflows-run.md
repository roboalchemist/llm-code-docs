# Source: https://docs.galileo.ai/api-reference/evaluate/create-workflows-run.md

# Create Workflows Run

> Create a new Evaluate run with workflows.

Use this endpoint to create a new Evaluate run with workflows. The request body should contain the `workflows` to be ingested and evaluated.

Additionally, specify the `project_id` or `project_name` to which the workflows should be ingested. If the project does not exist, it will be created. If the project exists, the workflows will be logged to it. If both `project_id` and `project_name` are provided, `project_id` will take precedence. The `run_name` is optional and will be auto-generated (timestamp-based) if not provided.

The body is also expected to include the configuration for the scorers to be used in the evaluation. This configuration will be used to evaluate the workflows and generate the results.

## OpenAPI

````yaml https://api.acme.rungalileo.io/public/v1/openapi.json post /v1/evaluate/runs
paths:
  path: /v1/evaluate/runs
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              scorers:
                allOf:
                  - items:
                      oneOf:
                        - $ref: '#/components/schemas/AgenticWorkflowSuccessScorer'
                        - $ref: '#/components/schemas/AgenticSessionSuccessScorer'
                        - $ref: '#/components/schemas/BleuScorer'
                        - $ref: >-
                            #/components/schemas/ChunkAttributionUtilizationScorer
                        - $ref: '#/components/schemas/CompletenessScorer'
                        - $ref: '#/components/schemas/ContextAdherenceScorer'
                        - $ref: '#/components/schemas/ContextRelevanceScorer'
                        - $ref: '#/components/schemas/CorrectnessScorer'
                        - $ref: '#/components/schemas/GroundTruthAdherenceScorer'
                        - $ref: '#/components/schemas/InputPIIScorer'
                        - $ref: '#/components/schemas/InputSexistScorer'
                        - $ref: '#/components/schemas/InputToneScorer'
                        - $ref: '#/components/schemas/InputToxicityScorer'
                        - $ref: '#/components/schemas/InstructionAdherenceScorer'
                        - $ref: '#/components/schemas/OutputPIIScorer'
                        - $ref: '#/components/schemas/OutputSexistScorer'
                        - $ref: '#/components/schemas/OutputToneScorer'
                        - $ref: '#/components/schemas/OutputToxicityScorer'
                        - $ref: '#/components/schemas/PromptInjectionScorer'
                        - $ref: '#/components/schemas/PromptPerplexityScorer'
                        - $ref: '#/components/schemas/RougeScorer'
                        - $ref: '#/components/schemas/ToolErrorRateScorer'
                        - $ref: '#/components/schemas/ToolSelectionQualityScorer'
                        - $ref: '#/components/schemas/UncertaintyScorer'
                      discriminator:
                        propertyName: name
                        mapping:
                          agentic_session_success: '#/components/schemas/AgenticSessionSuccessScorer'
                          agentic_workflow_success: '#/components/schemas/AgenticWorkflowSuccessScorer'
                          bleu: '#/components/schemas/BleuScorer'
                          chunk_attribution_utilization: >-
                            #/components/schemas/ChunkAttributionUtilizationScorer
                          completeness: '#/components/schemas/CompletenessScorer'
                          context_adherence: '#/components/schemas/ContextAdherenceScorer'
                          context_relevance: '#/components/schemas/ContextRelevanceScorer'
                          correctness: '#/components/schemas/CorrectnessScorer'
                          ground_truth_adherence: '#/components/schemas/GroundTruthAdherenceScorer'
                          input_pii: '#/components/schemas/InputPIIScorer'
                          input_sexist: '#/components/schemas/InputSexistScorer'
                          input_tone: '#/components/schemas/InputToneScorer'
                          input_toxicity: '#/components/schemas/InputToxicityScorer'
                          instruction_adherence: '#/components/schemas/InstructionAdherenceScorer'
                          output_pii: '#/components/schemas/OutputPIIScorer'
                          output_sexist: '#/components/schemas/OutputSexistScorer'
                          output_tone: '#/components/schemas/OutputToneScorer'
                          output_toxicity: '#/components/schemas/OutputToxicityScorer'
                          prompt_injection: '#/components/schemas/PromptInjectionScorer'
                          prompt_perplexity: '#/components/schemas/PromptPerplexityScorer'
                          rouge: '#/components/schemas/RougeScorer'
                          tool_error_rate: '#/components/schemas/ToolErrorRateScorer'
                          tool_selection_quality: '#/components/schemas/ToolSelectionQualityScorer'
                          uncertainty: '#/components/schemas/UncertaintyScorer'
                    type: array
                    title: Scorers
                    description: List of Galileo scorers to enable.
              registered_scorers:
                allOf:
                  - items:
                      $ref: '#/components/schemas/RegisteredScorerConfig'
                    type: array
                    title: Registered Scorers
                    description: List of registered scorers to enable.
              generated_scorers:
                allOf:
                  - items:
                      $ref: '#/components/schemas/GeneratedScorerConfig'
                    type: array
                    title: Generated Scorers
                    description: List of generated scorers to enable.
              finetuned_scorers:
                allOf:
                  - items:
                      $ref: '#/components/schemas/FinetunedScorerConfig'
                    type: array
                    title: Finetuned Scorers
                    description: List of finetuned scorers to enable.
              workflows:
                allOf:
                  - items:
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
                    description: List of workflows to include in the run.
              project_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid4
                      - type: 'null'
                    title: Project Id
                    description: Evaluate Project ID to which the run should be associated.
              project_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Project Name
                    description: >-
                      Evaluate Project name to which the run should be
                      associated. If the project does not exist, it will be
                      created.
              run_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Run Name
                    description: >-
                      Name of the run. If no name is provided, a timestamp-based
                      name will be generated.
            required: true
            title: EvaluateRunRequest
            refIdentifier: '#/components/schemas/EvaluateRunRequest'
            examples:
              - project_name: my-evaluate-project
                run_name: my-evaluate-run
                scorers: &ref_0
                  - name: correctness
                  - name: output_pii
                workflows: &ref_1
                  - created_at_ns: 1760464815248918500
                    duration_ns: 0
                    input: who is a smart LLM?
                    metadata: {}
                    name: llm
                    output: I am!
                    type: llm
              - project_id: 00000000-0000-0000-0000-000000000000
                registered_scorers:
                  - name: my_registered_scorer
                run_name: my-evaluate-run
                workflows:
                  - created_at_ns: 1760464815248974600
                    duration_ns: 0
                    input: who is a smart LLM?
                    metadata: {}
                    name: llm
                    output: I am!
                    type: llm
            requiredProperties:
              - workflows
            example:
              project_name: my-evaluate-project
              run_name: my-evaluate-run
              scorers: *ref_0
              workflows: *ref_1
        examples:
          example:
            value:
              project_name: my-evaluate-project
              run_name: my-evaluate-run
              scorers:
                - name: correctness
                - name: output_pii
              workflows:
                - created_at_ns: 1760464815248918500
                  duration_ns: 0
                  input: who is a smart LLM?
                  metadata: {}
                  name: llm
                  output: I am!
                  type: llm
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    title: Message
              project_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Project Id
              project_name:
                allOf:
                  - type: string
                    title: Project Name
              run_id:
                allOf:
                  - type: string
                    format: uuid4
                    title: Run Id
              run_name:
                allOf:
                  - type: string
                    title: Run Name
              workflows_count:
                allOf:
                  - type: integer
                    title: Workflows Count
              records_count:
                allOf:
                  - type: integer
                    title: Records Count
            title: EvaluateRunResponse
            refIdentifier: '#/components/schemas/EvaluateRunResponse'
            requiredProperties:
              - message
              - project_id
              - project_name
              - run_id
              - run_name
              - workflows_count
              - records_count
        examples:
          example:
            value:
              message: <string>
              project_id: <string>
              project_name: <string>
              run_id: <string>
              run_name: <string>
              workflows_count: 123
              records_count: 123
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
    AgenticSessionSuccessScorer:
      properties:
        name:
          type: string
          const: agentic_session_success
          title: Name
          default: agentic_session_success
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: plus
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: AgenticSessionSuccessScorer
    AgenticWorkflowSuccessScorer:
      properties:
        name:
          type: string
          const: agentic_workflow_success
          title: Name
          default: agentic_workflow_success
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: plus
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: AgenticWorkflowSuccessScorer
    BleuScorer:
      properties:
        name:
          type: string
          const: bleu
          title: Name
          default: bleu
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      title: BleuScorer
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
    ChunkAttributionUtilizationScorer:
      properties:
        name:
          type: string
          const: chunk_attribution_utilization
          title: Name
          default: chunk_attribution_utilization
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: luna
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
      type: object
      title: ChunkAttributionUtilizationScorer
    CompletenessScorer:
      properties:
        name:
          type: string
          const: completeness
          title: Name
          default: completeness
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: luna
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: CompletenessScorer
    ContextAdherenceScorer:
      properties:
        name:
          type: string
          const: context_adherence
          title: Name
          default: context_adherence
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: luna
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: ContextAdherenceScorer
    ContextRelevanceScorer:
      properties:
        name:
          type: string
          const: context_relevance
          title: Name
          default: context_relevance
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      title: ContextRelevanceScorer
    CorrectnessScorer:
      properties:
        name:
          type: string
          const: correctness
          title: Name
          default: correctness
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          const: plus
          title: Type
          default: plus
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: CorrectnessScorer
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
    FinetunedScorerConfig:
      properties:
        name:
          type: string
          title: Name
          description: Name of the scorer to enable.
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      required:
        - name
      title: FinetunedScorerConfig
    GeneratedScorerConfig:
      properties:
        name:
          type: string
          title: Name
          description: Name of the scorer to enable.
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      required:
        - name
      title: GeneratedScorerConfig
    GroundTruthAdherenceScorer:
      properties:
        name:
          type: string
          const: ground_truth_adherence
          title: Name
          default: ground_truth_adherence
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          const: plus
          title: Type
          default: plus
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: GroundTruthAdherenceScorer
    InputPIIScorer:
      properties:
        name:
          type: string
          const: input_pii
          title: Name
          default: input_pii
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      title: InputPIIScorer
    InputSexistScorer:
      properties:
        name:
          type: string
          const: input_sexist
          title: Name
          default: input_sexist
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: luna
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: InputSexistScorer
    InputToneScorer:
      properties:
        name:
          type: string
          const: input_tone
          title: Name
          default: input_tone
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      title: InputToneScorer
    InputToxicityScorer:
      properties:
        name:
          type: string
          const: input_toxicity
          title: Name
          default: input_toxicity
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: luna
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: InputToxicityScorer
    InstructionAdherenceScorer:
      properties:
        name:
          type: string
          const: instruction_adherence
          title: Name
          default: instruction_adherence
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          const: plus
          title: Type
          default: plus
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: InstructionAdherenceScorer
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
    MetadataFilter:
      properties:
        name:
          type: string
          const: metadata
          title: Name
          default: metadata
        filter_type:
          type: string
          const: map
          title: Filter Type
          default: map
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
      title: MetadataFilter
      description: Filters on metadata key-value pairs in scorer jobs.
    NodeNameFilter:
      properties:
        name:
          type: string
          const: node_name
          title: Name
          default: node_name
        filter_type:
          type: string
          const: string
          title: Filter Type
          default: string
        value:
          type: string
          title: Value
        operator:
          type: string
          enum:
            - eq
            - ne
            - contains
          title: Operator
        case_sensitive:
          type: boolean
          title: Case Sensitive
          default: true
      type: object
      required:
        - value
        - operator
      title: NodeNameFilter
      description: Filters on node names in scorer jobs.
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
    OutputPIIScorer:
      properties:
        name:
          type: string
          const: output_pii
          title: Name
          default: output_pii
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      title: OutputPIIScorer
    OutputSexistScorer:
      properties:
        name:
          type: string
          const: output_sexist
          title: Name
          default: output_sexist
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: luna
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: OutputSexistScorer
    OutputToneScorer:
      properties:
        name:
          type: string
          const: output_tone
          title: Name
          default: output_tone
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      title: OutputToneScorer
    OutputToxicityScorer:
      properties:
        name:
          type: string
          const: output_toxicity
          title: Name
          default: output_toxicity
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: luna
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: OutputToxicityScorer
    PromptInjectionScorer:
      properties:
        name:
          type: string
          const: prompt_injection
          title: Name
          default: prompt_injection
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: luna
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: PromptInjectionScorer
    PromptPerplexityScorer:
      properties:
        name:
          type: string
          const: prompt_perplexity
          title: Name
          default: prompt_perplexity
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      title: PromptPerplexityScorer
    RegisteredScorerConfig:
      properties:
        name:
          type: string
          title: Name
          description: Name of the scorer to enable.
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      required:
        - name
      title: RegisteredScorerConfig
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
    RougeScorer:
      properties:
        name:
          type: string
          const: rouge
          title: Name
          default: rouge
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      title: RougeScorer
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
    ToolErrorRateScorer:
      properties:
        name:
          type: string
          const: tool_error_rate
          title: Name
          default: tool_error_rate
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: plus
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
      type: object
      title: ToolErrorRateScorer
    ToolSelectionQualityScorer:
      properties:
        name:
          type: string
          const: tool_selection_quality
          title: Name
          default: tool_selection_quality
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
        type:
          type: string
          enum:
            - luna
            - plus
          title: Type
          default: plus
        model_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Model Name
          description: Alias of the model to use for the scorer.
        num_judges:
          anyOf:
            - type: integer
              maximum: 10
              minimum: 1
            - type: 'null'
          title: Num Judges
          description: Number of judges for the scorer.
      type: object
      title: ToolSelectionQualityScorer
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
    UncertaintyScorer:
      properties:
        name:
          type: string
          const: uncertainty
          title: Name
          default: uncertainty
        filters:
          anyOf:
            - items:
                oneOf:
                  - $ref: '#/components/schemas/NodeNameFilter'
                  - $ref: '#/components/schemas/MetadataFilter'
                discriminator:
                  propertyName: name
                  mapping:
                    metadata: '#/components/schemas/MetadataFilter'
                    node_name: '#/components/schemas/NodeNameFilter'
              type: array
            - type: 'null'
          title: Filters
          description: List of filters to apply to the scorer.
      type: object
      title: UncertaintyScorer
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

````