# Source: https://docs.galileo.ai/api-reference/evaluate-alerts/list-evaluate-alerts.md

# List Evaluate Alerts

## OpenAPI

````yaml https://api.acme.rungalileo.io/public/v1/openapi.json get /v1/projects/{project_id}/runs/{run_id}/prompts/alerts
paths:
  path: /v1/projects/{project_id}/runs/{run_id}/prompts/alerts
  method: get
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
        run_id:
          schema:
            - type: string
              required: true
              title: Run Id
              format: uuid4
        project_id:
          schema:
            - type: string
              required: true
              title: Project Id
              format: uuid4
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/EvaluateAlertDB'
            title: >-
              Response List Evaluate Alerts V1 Projects  Project Id  Runs  Run
              Id  Prompts Alerts Get
        examples:
          example:
            value:
              - project_id: <string>
                run_id: <string>
                alert_name: <string>
                filter:
                  column: <string>
                  filter_type: <string>
                  low: 123
                  high: 123
                field_name: <string>
                description: <string>
                extra: {}
                id: <string>
                created_at: '2023-11-07T05:31:56Z'
                updated_at: '2023-11-07T05:31:56Z'
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
    CategoricalPromptFilterParam:
      properties:
        column:
          type: string
          title: Column
        filter_type:
          type: string
          const: category
          title: Filter Type
        categories:
          items:
            type: string
          type: array
          title: Categories
        operator:
          $ref: '#/components/schemas/CategoryFilterOperator'
          description: >-
            Operator to use when checking if the value is in the categories. If
            None, we default to 'or'.
          default: any
      type: object
      required:
        - column
        - filter_type
        - categories
      title: CategoricalPromptFilterParam
    CategoryFilterOperator:
      type: string
      enum:
        - any
        - all
        - exact
        - none
      title: CategoryFilterOperator
    EvaluateAlertDB:
      properties:
        project_id:
          type: string
          format: uuid4
          title: Project Id
        run_id:
          type: string
          format: uuid4
          title: Run Id
        alert_name:
          type: string
          title: Alert Name
        filter:
          oneOf:
            - $ref: '#/components/schemas/RangePromptFilterParam'
            - $ref: '#/components/schemas/ValuePromptFilterParam'
            - $ref: '#/components/schemas/CategoricalPromptFilterParam'
          title: Filter
          discriminator:
            propertyName: filter_type
            mapping:
              category: '#/components/schemas/CategoricalPromptFilterParam'
              range: '#/components/schemas/RangePromptFilterParam'
              value: '#/components/schemas/ValuePromptFilterParam'
        field_name:
          type: string
          title: Field Name
        description:
          type: string
          title: Description
        extra:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Extra
        id:
          type: string
          format: uuid4
          title: Id
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          type: string
          format: date-time
          title: Updated At
      type: object
      required:
        - project_id
        - run_id
        - alert_name
        - filter
        - field_name
        - description
        - id
        - created_at
        - updated_at
      title: EvaluateAlertDB
    Operator:
      type: string
      enum:
        - eq
        - ne
        - gt
        - gte
        - lt
        - lte
        - in
        - not_in
        - contains
        - has_all
        - between
        - like
      title: Operator
    RangePromptFilterParam:
      properties:
        column:
          type: string
          title: Column
        filter_type:
          type: string
          const: range
          title: Filter Type
        low:
          type: number
          title: Low
        high:
          type: number
          title: High
      type: object
      required:
        - column
        - filter_type
        - low
        - high
      title: RangePromptFilterParam
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
    ValuePromptFilterParam:
      properties:
        column:
          type: string
          title: Column
        filter_type:
          type: string
          const: value
          title: Filter Type
        value:
          anyOf:
            - type: integer
            - type: number
            - type: boolean
            - type: string
          title: Value
        relation:
          $ref: '#/components/schemas/Operator'
      type: object
      required:
        - column
        - filter_type
        - value
        - relation
      title: ValuePromptFilterParam

````