# Source: https://docs.galileo.ai/api-reference/protect/invoke.md

# Invoke

## OpenAPI

````yaml https://api.acme.rungalileo.io/public/v1/openapi.json post /v1/protect/invoke
paths:
  path: /v1/protect/invoke
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
              prioritized_rulesets:
                allOf:
                  - items:
                      $ref: '#/components/schemas/Ruleset'
                    type: array
                    title: Prioritized Rulesets
                    description: Rulesets to be applied to the payload.
              payload:
                allOf:
                  - $ref: '#/components/schemas/Payload'
                    description: Payload to be processed.
              project_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Project Name
                    description: Project name.
              project_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid4
                      - type: 'null'
                    title: Project Id
                    description: Project ID.
              stage_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Stage Name
                    description: Stage name.
              stage_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid4
                      - type: 'null'
                    title: Stage Id
                    description: Stage ID.
              stage_version:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Stage Version
                    description: >-
                      Stage version to use for the request, if it's a central
                      stage with a previously registered version.
              timeout:
                allOf:
                  - type: number
                    title: Timeout
                    description: >-
                      Optional timeout for the guardrail execution in seconds.
                      This is not the timeout for the request. If not set, a
                      default timeout of 5 minutes will be used.
                    default: 300
              metadata:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: string
                        type: object
                      - type: 'null'
                    title: Metadata
                    description: >-
                      Optional additional metadata. This will be echoed back in
                      the response.
              headers:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: string
                        type: object
                      - type: 'null'
                    title: Headers
                    description: >-
                      Optional additional HTTP headers that should be included
                      in the response.
            required: true
            title: ProtectRequest
            description: Protect request schema with custom OpenAPI title.
            refIdentifier: '#/components/schemas/ProtectRequest'
            requiredProperties:
              - payload
        examples:
          example:
            value:
              prioritized_rulesets:
                - rules:
                    - metric: <string>
                      operator: gt
                      target_value: <string>
                  action:
                    type: OVERRIDE
                    subscriptions:
                      - statuses:
                          - triggered
                        url: <string>
                    choices:
                      - <string>
                  description: <string>
              payload:
                input: <string>
                output: <string>
              project_name: <string>
              project_id: <string>
              stage_name: <string>
              stage_id: <string>
              stage_version: 123
              timeout: 300
              metadata: {}
              headers: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: string
                    description: Status of the request after processing the rules.
              text:
                allOf:
                  - type: string
                    title: Text
                    description: Text from the request after processing the rules.
              trace_metadata:
                allOf:
                  - $ref: '#/components/schemas/TraceMetadata'
            title: ProtectResponse
            description: Protect response schema with custom OpenAPI title.
            refIdentifier: '#/components/schemas/ProtectResponse'
            requiredProperties:
              - text
              - trace_metadata
          - type: object
            properties:
              status:
                allOf:
                  - type: string
                    description: Status of the execution.
              api_version:
                allOf:
                  - type: string
                    title: Api Version
                    default: 1.0.0
              text:
                allOf:
                  - type: string
                    title: Text
                    description: Text from the request after processing the rules.
              trace_metadata:
                allOf:
                  - $ref: '#/components/schemas/TraceMetadata'
              stage_metadata:
                allOf:
                  - $ref: '#/components/schemas/StageMetadata'
              ruleset_results:
                allOf:
                  - items:
                      $ref: '#/components/schemas/RulesetResult'
                    type: array
                    title: Ruleset Results
                    description: Results of the rule execution.
              metric_results:
                allOf:
                  - additionalProperties:
                      $ref: '#/components/schemas/MetricComputation'
                    type: object
                    title: Metric Results
                    description: Results of the metric computation.
              action_result:
                allOf:
                  - $ref: '#/components/schemas/ActionResult'
              metadata:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: string
                        type: object
                      - type: 'null'
                    title: Metadata
                    description: >-
                      Optional additional metadata. This being echoed back from
                      the request.
              headers:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: string
                        type: object
                      - type: 'null'
                    title: Headers
                    description: >-
                      Optional additional HTTP headers that should be included
                      in the response.
            title: InvokeResponse
            refIdentifier: '#/components/schemas/InvokeResponse'
            requiredProperties:
              - text
              - trace_metadata
              - stage_metadata
              - action_result
        examples:
          example:
            value:
              status: <string>
              text: <string>
              trace_metadata:
                id: <string>
                received_at: 123
                response_at: 123
                execution_time: 123
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
    ActionResult:
      properties:
        type:
          $ref: '#/components/schemas/ActionType'
          description: Type of action that was taken.
        value:
          type: string
          title: Value
          description: Value of the action that was taken.
      type: object
      required:
        - type
        - value
      title: ActionResult
    ActionType:
      type: string
      enum:
        - OVERRIDE
        - PASSTHROUGH
      title: ActionType
    ExecutionStatus:
      type: string
      enum:
        - triggered
        - failed
        - error
        - timeout
        - paused
        - not_triggered
        - skipped
      title: ExecutionStatus
      description: Status of the execution.
    MetricComputation:
      properties:
        value:
          anyOf:
            - type: number
            - type: integer
            - type: string
            - items:
                anyOf:
                  - type: number
                  - type: integer
                  - type: string
                  - type: 'null'
              type: array
            - additionalProperties:
                anyOf:
                  - type: number
                  - type: integer
                  - type: string
                  - type: 'null'
              type: object
            - type: 'null'
          title: Value
        execution_time:
          anyOf:
            - type: number
            - type: 'null'
          title: Execution Time
        status:
          type: string
        error_message:
          anyOf:
            - type: string
            - type: 'null'
          title: Error Message
      type: object
      title: MetricComputation
    OverrideAction-Input:
      properties:
        type:
          type: string
          const: OVERRIDE
          title: Type
          default: OVERRIDE
        subscriptions:
          items:
            $ref: '#/components/schemas/SubscriptionConfig'
          type: array
          title: Subscriptions
          description: >-
            List of subscriptions to send a notification to when this action is
            applied and the ruleset status matches any of the configured
            statuses.
        choices:
          items:
            type: string
          type: array
          minItems: 1
          title: Choices
          description: >-
            List of choices to override the response with. If there are multiple
            choices, one will be chosen at random when applying this action.
      type: object
      required:
        - choices
      title: OverrideAction
    OverrideAction-Output:
      properties:
        type:
          type: string
          const: OVERRIDE
          title: Type
          default: OVERRIDE
        subscriptions:
          items:
            $ref: '#/components/schemas/SubscriptionConfig'
          type: array
          title: Subscriptions
          description: >-
            List of subscriptions to send a notification to when this action is
            applied and the ruleset status matches any of the configured
            statuses.
        choices:
          items:
            type: string
          type: array
          minItems: 1
          title: Choices
          description: >-
            List of choices to override the response with. If there are multiple
            choices, one will be chosen at random when applying this action.
      type: object
      required:
        - choices
      title: OverrideAction
    PassthroughAction-Input:
      properties:
        type:
          type: string
          const: PASSTHROUGH
          title: Type
          default: PASSTHROUGH
        subscriptions:
          items:
            $ref: '#/components/schemas/SubscriptionConfig'
          type: array
          title: Subscriptions
          description: >-
            List of subscriptions to send a notification to when this action is
            applied and the ruleset status matches any of the configured
            statuses.
      type: object
      title: PassthroughAction
    PassthroughAction-Output:
      properties:
        type:
          type: string
          const: PASSTHROUGH
          title: Type
          default: PASSTHROUGH
        subscriptions:
          items:
            $ref: '#/components/schemas/SubscriptionConfig'
          type: array
          title: Subscriptions
          description: >-
            List of subscriptions to send a notification to when this action is
            applied and the ruleset status matches any of the configured
            statuses.
      type: object
      title: PassthroughAction
    Payload:
      properties:
        input:
          anyOf:
            - type: string
            - type: 'null'
          title: Input
          description: Input text to be processed.
        output:
          anyOf:
            - type: string
            - type: 'null'
          title: Output
          description: Output text to be processed.
      type: object
      title: Payload
    Rule:
      properties:
        metric:
          type: string
          title: Metric
          description: Name of the metric.
        operator:
          $ref: '#/components/schemas/RuleOperator'
          description: Operator to use for comparison.
        target_value:
          anyOf:
            - type: string
            - type: number
            - type: integer
            - items: {}
              type: array
            - type: 'null'
          title: Target Value
          description: Value to compare with for this metric (right hand side).
      type: object
      required:
        - metric
        - operator
        - target_value
      title: Rule
    RuleOperator:
      type: string
      enum:
        - gt
        - lt
        - gte
        - lte
        - eq
        - neq
        - contains
        - all
        - any
        - empty
        - not_empty
      title: RuleOperator
    RuleResult:
      properties:
        status:
          type: string
          description: Status of the execution.
        metric:
          type: string
          title: Metric
          description: Name of the metric.
        operator:
          $ref: '#/components/schemas/RuleOperator'
          description: Operator to use for comparison.
        target_value:
          anyOf:
            - type: string
            - type: number
            - type: integer
            - items: {}
              type: array
            - type: 'null'
          title: Target Value
          description: Value to compare with for this metric (right hand side).
        value:
          anyOf:
            - {}
            - type: 'null'
          title: Value
          description: Result of the metric computation.
        execution_time:
          anyOf:
            - type: number
            - type: 'null'
          title: Execution Time
          description: Execution time for the rule in seconds.
      type: object
      required:
        - metric
        - operator
        - target_value
      title: RuleResult
    Ruleset:
      properties:
        rules:
          items:
            $ref: '#/components/schemas/Rule'
          type: array
          minItems: 1
          title: Rules
          description: List of rules to evaluate. Atleast 1 rule is required.
        action:
          oneOf:
            - $ref: '#/components/schemas/OverrideAction-Input'
            - $ref: '#/components/schemas/PassthroughAction-Input'
          title: Action
          description: Action to take if all the rules are met.
          discriminator:
            propertyName: type
            mapping:
              OVERRIDE: '#/components/schemas/OverrideAction-Input'
              PASSTHROUGH: '#/components/schemas/PassthroughAction-Input'
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: Description of the ruleset.
      type: object
      title: Ruleset
    RulesetResult:
      properties:
        status:
          type: string
          description: Status of the execution.
        rules:
          items:
            $ref: '#/components/schemas/Rule'
          type: array
          minItems: 1
          title: Rules
          description: List of rules to evaluate. Atleast 1 rule is required.
        action:
          oneOf:
            - $ref: '#/components/schemas/OverrideAction-Output'
            - $ref: '#/components/schemas/PassthroughAction-Output'
          title: Action
          description: Action to take if all the rules are met.
          discriminator:
            propertyName: type
            mapping:
              OVERRIDE: '#/components/schemas/OverrideAction-Output'
              PASSTHROUGH: '#/components/schemas/PassthroughAction-Output'
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: Description of the ruleset.
        rule_results:
          items:
            $ref: '#/components/schemas/RuleResult'
          type: array
          title: Rule Results
          description: Results of the rule execution.
      type: object
      title: RulesetResult
    StageMetadata:
      properties:
        project_id:
          type: string
          format: uuid4
          title: Project Id
        stage_id:
          type: string
          format: uuid4
          title: Stage Id
        stage_name:
          type: string
          title: Stage Name
        stage_version:
          type: integer
          title: Stage Version
        stage_type:
          $ref: '#/components/schemas/StageType'
      type: object
      required:
        - project_id
        - stage_id
        - stage_name
        - stage_version
        - stage_type
      title: StageMetadata
    StageType:
      type: string
      enum:
        - local
        - central
      title: StageType
    SubscriptionConfig:
      properties:
        statuses:
          items:
            $ref: '#/components/schemas/ExecutionStatus'
          type: array
          title: Statuses
          description: >-
            List of statuses that will cause a notification to be sent to the
            configured URL.
          default:
            - triggered
        url:
          type: string
          minLength: 1
          format: uri
          title: Url
          description: >-
            URL to send the event to. This can be a webhook URL, a message queue
            URL, an event bus or a custom endpoint that can receive an HTTP POST
            request.
      type: object
      required:
        - url
      title: SubscriptionConfig
    TraceMetadata:
      properties:
        id:
          type: string
          format: uuid4
          title: Id
          description: Unique identifier for the request.
        received_at:
          type: integer
          title: Received At
          description: Time the request was received by the server in nanoseconds.
        response_at:
          type: integer
          title: Response At
          description: Time the response was sent by the server in nanoseconds.
        execution_time:
          type: number
          title: Execution Time
          description: Execution time for the request (in seconds).
          default: -1
      type: object
      title: TraceMetadata
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