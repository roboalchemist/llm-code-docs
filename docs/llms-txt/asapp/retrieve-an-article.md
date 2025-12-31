# Source: https://docs.asapp.com/apis/knowledge-base/retrieve-an-article.md

# Retrieve an article

> Fetch a specific article by its unique identifier. If the article has not been created because the associated submission was not approved, a 404 status will be returned.

## OpenAPI

````yaml api-specs/knowledge-base.yaml get /knowledge-base/v1/articles/{id}
paths:
  path: /knowledge-base/v1/articles/{id}
  method: get
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The unique identifier for the article to be retrieved.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The unique identifier for the article.
                    example: fddd060c-22d7-4aed-acae-8f8dcc093a88
              title:
                allOf:
                  - type: string
                    description: >-
                      The refined title of the article, resulting from the
                      cleanup process.
                    example: 5G Data Plan Overview
              content:
                allOf:
                  - type: string
                    description: >-
                      The refined content of the article, resulting from the
                      cleanup process.
                    example: >-
                      Our 5G data plans includes 75GB of data per month, while
                      the Unlimited 5G plan offers unlimited data with no speed
                      caps. Both plans include unlimited calls and texts within
                      the country. International roaming is available for an
                      additional fee.
              url:
                allOf:
                  - type: string
                    description: >-
                      The reference URL of the article. Defaults to null if not
                      provided.
                    example: https://example.com/5g-data-plans
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
                    description: >-
                      The timestamp indicating when the article was last
                      updated. This field is null if the initial submission is
                      still pending review.
                    example: '2024-12-12T00:00:00Z'
              updatedBy:
                allOf:
                  - type: string
                    description: >-
                      The email address of the user who last updated the
                      article. This field is null if the initial submission is
                      still pending review.
                    example: user@company.com
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
              originalContent:
                allOf:
                  - type: string
                    description: >-
                      The original content of the article prior to the cleanup
                      process.
                    example: >-
                      Our 5G data plans offer lightning-fast speeds and generous
                      data allowances. The Basic 5G plan now includes 75GB of
                      data per month, while our Unlimited 5G plan offers truly
                      unlimited data with no speed caps. Both plans include
                      unlimited calls and texts within the country.
                      International roaming can be added for an additional fee.
              originalTitle:
                allOf:
                  - type: string
                    description: >-
                      The original title of the article prior to the cleanup
                      process.
                    example: 5G Data Plan
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
                      - Is there a family plan for 5G?
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
                      - clarificationInstruction: >-
                          Emphasize that 5G coverage may vary by location and
                          mention the new Family Plan option
                        exampleResponse: >-
                          Our 5G plans offer great speeds and data allowances,
                          including our new Family Plan. Please note that 5G
                          coverage may vary depending on your location. You can
                          check coverage in your area on our website.
              pendingSubmissionId:
                allOf:
                  - type: string
                    description: >-
                      The unique identifier for the submission currently under
                      review for this article. This field is null if there are
                      no pending submissions.
                    example: 86ba487a-6d58-4b4c-82de-9d422f1166ae
              currentVersion:
                allOf:
                  - type: string
                    description: >-
                      The current version label of the article. This field is
                      null if the initial submission is still pending review.
                    example: v1
              deploymentStatus:
                allOf:
                  - description: The current deployment status of the article.
                    example: DRAFT
                    type: string
                    enum:
                      - NONE
                      - DRAFT
                      - SANDBOX
                      - PRODUCTION
                      - SANDBOX_AND_PRODUCTION
            description: An article stored within the Knowledge Base.
            example:
              id: fddd060c-22d7-4aed-acae-8f8dcc093a88
              updatedAt: '2024-12-12T00:00:00'
              updatedBy: user@company.com
              title: 5G Data Plan Overview
              content: >-
                Our 5G data plans includes 75GB of data per month, while the
                Unlimited 5G plan offers unlimited data with no speed caps. Both
                plans include unlimited calls and texts within the country.
                International roaming is available for an additional fee.
              url: https://example.com/5g-data-plans
              metadata:
                - key: department
                  value: Customer experience
              originalContent: >-
                Our 5G data plans offer lightning-fast speeds and generous data
                allowances. The Basic 5G plan now includes 75GB of data per
                month, while our Unlimited 5G plan offers truly unlimited data
                with no speed caps. Both plans include unlimited calls and texts
                within the country. International roaming can be added for an
                additional fee.
              originalTitle: 5G Data Plan
              queryExamples:
                - What 5G plans do you offer?
                - Is there a family plan for 5G?
              additionalInstructions:
                - clarificationInstruction: >-
                    Emphasize that 5G coverage may vary by location and mention
                    the new Family Plan option
                  exampleResponse: >-
                    Our 5G plans offer great speeds and data allowances,
                    including our new Family Plan. Please note that 5G coverage
                    may vary depending on your location. You can check coverage
                    in your area on our website.
              pendingSubmissionId: 86ba487a-6d58-4b4c-82de-9d422f1166ae
              currentVersion: v1
              deploymentStatus: DRAFT
        examples:
          example:
            value:
              id: fddd060c-22d7-4aed-acae-8f8dcc093a88
              updatedAt: '2024-12-12T00:00:00'
              updatedBy: user@company.com
              title: 5G Data Plan Overview
              content: >-
                Our 5G data plans includes 75GB of data per month, while the
                Unlimited 5G plan offers unlimited data with no speed caps. Both
                plans include unlimited calls and texts within the country.
                International roaming is available for an additional fee.
              url: https://example.com/5g-data-plans
              metadata:
                - key: department
                  value: Customer experience
              originalContent: >-
                Our 5G data plans offer lightning-fast speeds and generous data
                allowances. The Basic 5G plan now includes 75GB of data per
                month, while our Unlimited 5G plan offers truly unlimited data
                with no speed caps. Both plans include unlimited calls and texts
                within the country. International roaming can be added for an
                additional fee.
              originalTitle: 5G Data Plan
              queryExamples:
                - What 5G plans do you offer?
                - Is there a family plan for 5G?
              additionalInstructions:
                - clarificationInstruction: >-
                    Emphasize that 5G coverage may vary by location and mention
                    the new Family Plan option
                  exampleResponse: >-
                    Our 5G plans offer great speeds and data allowances,
                    including our new Family Plan. Please note that 5G coverage
                    may vary depending on your location. You can check coverage
                    in your area on our website.
              pendingSubmissionId: 86ba487a-6d58-4b4c-82de-9d422f1166ae
              currentVersion: v1
              deploymentStatus: DRAFT
        description: Article successfully retrieved
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