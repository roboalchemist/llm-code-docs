# Source: https://docs.asapp.com/apis/knowledge-base/create-a-submission.md

# Create a submission

> Initiate a request to add a new article or update an existing one. The provided title and content will be processed to create the final version of the submission.

## OpenAPI

````yaml api-specs/knowledge-base.yaml post /knowledge-base/v1/submissions
paths:
  path: /knowledge-base/v1/submissions
  method: post
  servers:
    - url: https://api.test.asapp.com
  request:
    security:
      - title: API ID & API Secret
        parameters:
          query: {}
          header:
            asapp-api-id:
              type: apiKey
            asapp-api-secret:
              type: apiKey
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
              articleId:
                allOf:
                  - type: string
                    description: The unique identifier for the article being updated.
                    example: 8f8dcc09-22d7-4aed-acae-fddd060c3a88
              title:
                allOf:
                  - type: string
                    description: >-
                      The proposed title of the article, which will be refined
                      automatically. This is required for new articles.
                    minLength: 1
                    maxLength: 256
                    example: 5G Data Plan
              content:
                allOf:
                  - type: string
                    description: >-
                      The article content in plain text, expected to be in
                      English and limited to 200,000 Unicode characters. This
                      will be refined during submission. Required for new
                      articles.
                    minLength: 1
                    maxLength: 200000
                    example: >-
                      Our 5G data plans offer lightning-fast speeds and generous
                      data allowances. The Basic 5G plan includes 50GB of data
                      per month, while our Unlimited 5G plan offers truly
                      unlimited data with no speed caps. Both plans include
                      unlimited calls and texts within the country.
                      International roaming can be added for an additional fee.
              url:
                allOf:
                  - type: string
                    description: >-
                      A reference URL for the article, used for informational
                      purposes only.
                    example: https://example.com/5g-data-plans
              metadata:
                allOf:
                  - type: array
                    items:
                      description: >-
                        A key-value pair providing additional information about
                        the article.
                      type: object
                      required:
                        - key
                        - value
                      properties:
                        key:
                          type: string
                          minLength: 1
                          description: The key for the metadata entry.
                          example: department
                        value:
                          type: string
                          minLength: 1
                          description: The value for the metadata entry.
                          example: Customer experience
                    description: Additional key-value pairs related to the article.
                    example:
                      - key: department
                        value: Customer experience
              queryExamples:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: >-
                      Examples of customer questions related to the article,
                      such as "Why is my bill so high?". Defaults to an empty
                      list if not provided.
                    example:
                      - What 5G plans do you offer?
                      - Is there an unlimited 5G plan?
              additionalInstructions:
                allOf:
                  - type: array
                    items:
                      description: Guidelines and responses to enhance the article.
                      type: object
                      properties:
                        clarificationInstruction:
                          type: string
                          description: A guideline to improve the article's content.
                          example: Emphasize that 5G coverage may vary by location
                        exampleResponse:
                          type: string
                          description: >-
                            A sample response applicable if the clarification
                            instruction is followed.
                          example: >-
                            Our 5G plans offer great speeds and data allowances,
                            but please note that 5G coverage may vary depending
                            on your location. You can check coverage in your
                            area on our website.
                    description: >-
                      Specific instructions to ensure responses are relevant and
                      address exceptions.
                    example:
                      - clarificationInstruction: Emphasize that 5G coverage may vary by location
                        exampleResponse: >-
                          Our 5G plans offer great speeds and data allowances,
                          but please note that 5G coverage may vary depending on
                          your location. You can check coverage in your area on
                          our website.
            required: true
            description: >-
              A proposal for creating a new article or updating an existing one
              in the Knowledge Base.
            example:
              title: 5G Data Plan
              content: >-
                Our 5G data plans offer lightning-fast speeds and generous data
                allowances. The Basic 5G plan includes 50GB of data per month,
                while our Unlimited 5G plan offers truly unlimited data with no
                speed caps. Both plans include unlimited calls and texts within
                the country. International roaming can be added for an
                additional fee.
              url: https://example.com/5g-data-plans
              metadata:
                - key: department
                  value: Customer experience
              queryExamples:
                - What 5G plans do you offer?
                - Is there an unlimited 5G plan?
              additionalInstructions:
                - clarificationInstruction: Emphasize that 5G coverage may vary by location
                  exampleResponse: >-
                    Our 5G plans offer great speeds and data allowances, but
                    please note that 5G coverage may vary depending on your
                    location. You can check coverage in your area on our
                    website.
        examples:
          example:
            value:
              title: 5G Data Plan
              content: >-
                Our 5G data plans offer lightning-fast speeds and generous data
                allowances. The Basic 5G plan includes 50GB of data per month,
                while our Unlimited 5G plan offers truly unlimited data with no
                speed caps. Both plans include unlimited calls and texts within
                the country. International roaming can be added for an
                additional fee.
              url: https://example.com/5g-data-plans
              metadata:
                - key: department
                  value: Customer experience
              queryExamples:
                - What 5G plans do you offer?
                - Is there an unlimited 5G plan?
              additionalInstructions:
                - clarificationInstruction: Emphasize that 5G coverage may vary by location
                  exampleResponse: >-
                    Our 5G plans offer great speeds and data allowances, but
                    please note that 5G coverage may vary depending on your
                    location. You can check coverage in your area on our
                    website.
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The unique identifier for the submission.
                    example: fddd060c-22d7-4aed-acae-8f8dcc093a88
              articleId:
                allOf:
                  - type: string
                    description: >-
                      The unique identifier for the article related to the
                      submission.
                    example: 8f8dcc09-22d7-4aed-acae-fddd060c3a88
              submittedAt:
                allOf:
                  - type: string
                    format: date-time
                    description: The timestamp when the submission was created.
                    example: '2024-12-12T00:00:00Z'
              title:
                allOf:
                  - type: string
                    description: The article title, either original or refined.
                    example: 5G Data Plan
              content:
                allOf:
                  - type: string
                    description: The article content, either original or refined.
                    example: >-
                      Our 5G data plans offer lightning-fast speeds and generous
                      data allowances. The Basic 5G plan includes 50GB of data
                      per month, while our Unlimited 5G plan offers truly
                      unlimited data with no speed caps. Both plans include
                      unlimited calls and texts within the country.
                      International roaming can be added for an additional fee.
              url:
                allOf:
                  - type: string
                    description: >-
                      The reference URL of the article. Defaults to an empty
                      string if not provided.
                    example: https://example.com/5g-data-plans
              metadata:
                allOf:
                  - type: array
                    items:
                      description: >-
                        A key-value pair providing additional information about
                        the article.
                      type: object
                      required:
                        - key
                        - value
                      properties:
                        key:
                          type: string
                          minLength: 1
                          description: The key for the metadata entry.
                          example: department
                        value:
                          type: string
                          minLength: 1
                          description: The value for the metadata entry.
                          example: Customer experience
                    description: Additional key-value pairs related to the article.
                    example:
                      - key: department
                        value: Customer experience
              queryExamples:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: >-
                      Examples of customer questions related to the article.
                      Defaults to an empty array if not provided.
                    example:
                      - What 5G plans do you offer?
                      - Is there an unlimited 5G plan?
              additionalInstructions:
                allOf:
                  - type: array
                    items:
                      description: Guidelines and responses to enhance the article.
                      type: object
                      properties:
                        clarificationInstruction:
                          type: string
                          description: A guideline to improve the article's content.
                          example: Emphasize that 5G coverage may vary by location
                        exampleResponse:
                          type: string
                          description: >-
                            A sample response applicable if the clarification
                            instruction is followed.
                          example: >-
                            Our 5G plans offer great speeds and data allowances,
                            but please note that 5G coverage may vary depending
                            on your location. You can check coverage in your
                            area on our website.
                    description: >-
                      Specific instructions to ensure responses are relevant and
                      address exceptions.
                    example:
                      - clarificationInstruction: Emphasize that 5G coverage may vary by location
                        exampleResponse: >-
                          Our 5G plans offer great speeds and data allowances,
                          but please note that 5G coverage may vary depending on
                          your location. You can check coverage in your area on
                          our website.
              status:
                allOf:
                  - description: The current status of the submission.
                    example: PENDING_REVIEW
                    type: string
                    enum:
                      - PENDING_REVIEW
                      - ACCEPTED
                      - REJECTED
            description: >-
              Information about a successfully submitted proposal to update an
              article in the Knowledge Base.
        examples:
          example:
            value:
              id: fddd060c-22d7-4aed-acae-8f8dcc093a88
              articleId: 8f8dcc09-22d7-4aed-acae-fddd060c3a88
              submittedAt: '2024-12-12T00:00:00'
              title: 5G Data Plan
              content: >-
                Our 5G data plans offer lightning-fast speeds and generous data
                allowances. The Basic 5G plan includes 50GB of data per month,
                while our Unlimited 5G plan offers truly unlimited data with no
                speed caps. Both plans include unlimited calls and texts within
                the country. International roaming can be added for an
                additional fee.
              url: https://example.com/5g-data-plans
              metadata:
                - key: department
                  value: Customer experience
              queryExamples:
                - What 5G plans do you offer?
                - Is there an unlimited 5G plan?
              additionalInstructions:
                - clarificationInstruction: Emphasize that 5G coverage may vary by location
                  exampleResponse: >-
                    Our 5G plans offer great speeds and data allowances, but
                    please note that 5G coverage may vary depending on your
                    location. You can check coverage in your area on our
                    website.
              status: PENDING_REVIEW
        description: Submission successfully created
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 400-01
                      message: Bad request
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Bad request response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 400-01
                message: Bad request
        description: 400 - Bad request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 401-01
                      message: Unauthorized
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Unauthorized response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 401-01
                message: Unauthorized
        description: 401 - Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 403-01
                      message: Forbidden Response
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Forbidden response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 403-01
                message: Forbidden Response
        description: 403 - Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 404-01
                      message: Not Found
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Not Found response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 404-01
                message: Not Found
        description: 404 - Not Found
    '413':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 413-01
                      message: Request Entity Too Large
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Request Entity Too Large response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 413-01
                message: Request Entity Too Large
        description: 413 - Request Entity Too Large
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 429-01
                      message: Too Many Requests
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Too Many Requests response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 429-01
                message: Too Many Requests
        description: 429 - Too Many Requests
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 503-01
                      message: Service Unavailable
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Service Unavailable response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 503-01
                message: Service Unavailable
        description: 503 - Service Unavailable
    default:
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 500-01
                      message: Internal server error
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Default error response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 500-01
                message: Internal server error
        description: 500 - Internal Server Error
  deprecated: false
  type: path
components:
  schemas: {}

````