# Source: https://docs.asapp.com/apis/knowledge-base/retrieve-a-submission.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve a submission

> Obtain the details of a specific submission using its unique identifier.



## OpenAPI

````yaml api-specs/knowledge-base.yaml get /knowledge-base/v1/submissions/{id}
openapi: 3.0.1
info:
  title: Knowledge Base API
  description: >
    This API allows for the programmatic addition and modification of articles
    in the Knowledge Base. It is particularly useful when data sources are not
    suitable for scraping or when manual article creation via the ASAPP
    AI-Console UI is not preferred. The Submission API facilitates the creation
    and updating of articles, with each submission representing a specific
    change to an article.


    All submissions require human review and approval through the ASAPP
    AI-Console UI before they are published in the Knowledge Base.


    To create a new article, submit the article details without an `articleId`.
    Omitting the `articleId` signals the creation of a new article upon
    submission approval.


    To update an existing article, include the `articleId` of the article you
    wish to modify along with the updates in your submission.
  contact:
    email: api-info@asapp.com
  license:
    name: ASAPP Software License
    url: https://api.asapp.com/LICENSE
  version: '1.0'
servers:
  - url: https://api.test.asapp.com
security:
  - API-ID: []
    API-Secret: []
paths:
  /knowledge-base/v1/submissions/{id}:
    get:
      summary: Retrieve a submission
      description: Obtain the details of a specific submission using its unique identifier.
      operationId: getSubmission
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: The unique identifier for the submission to be retrieved.
          example: fddd060c-22d7-4aed-acae-8f8dcc093a88
      responses:
        '200':
          description: Submission successfully retrieved
          content:
            application/json:
              schema:
                description: >-
                  Information about a successfully submitted proposal to update
                  an article in the Knowledge Base.
                type: object
                properties:
                  id:
                    type: string
                    description: The unique identifier for the submission.
                    example: fddd060c-22d7-4aed-acae-8f8dcc093a88
                  articleId:
                    type: string
                    description: >-
                      The unique identifier for the article related to the
                      submission.
                    example: 8f8dcc09-22d7-4aed-acae-fddd060c3a88
                  submittedAt:
                    type: string
                    format: date-time
                    description: The timestamp when the submission was created.
                    example: '2024-12-12T00:00:00Z'
                  title:
                    type: string
                    description: The article title, either original or refined.
                    example: 5G Data Plan
                  content:
                    type: string
                    description: The article content, either original or refined.
                    example: >-
                      Our 5G data plans offer lightning-fast speeds and generous
                      data allowances. The Basic 5G plan includes 50GB of data
                      per month, while our Unlimited 5G plan offers truly
                      unlimited data with no speed caps. Both plans include
                      unlimited calls and texts within the country.
                      International roaming can be added for an additional fee.
                  url:
                    type: string
                    description: >-
                      The reference URL of the article. Defaults to an empty
                      string if not provided.
                    example: https://example.com/5g-data-plans
                  metadata:
                    type: array
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
                    type: array
                    items:
                      type: string
                    description: >-
                      Examples of customer questions related to the article.
                      Defaults to an empty array if not provided.
                    example:
                      - What 5G plans do you offer?
                      - Is there an unlimited 5G plan?
                  additionalInstructions:
                    type: array
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
                    description: The current status of the submission.
                    type: string
                    enum:
                      - PENDING_REVIEW
                      - ACCEPTED
                      - REJECTED
                    example: PENDING_REVIEW
        '400':
          description: 400 - Bad request
          content:
            application/json:
              schema:
                description: Bad request response
                type: object
                properties:
                  error:
                    example:
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
        '401':
          description: 401 - Unauthorized
          content:
            application/json:
              schema:
                description: Unauthorized response
                type: object
                properties:
                  error:
                    example:
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
        '403':
          description: 403 - Forbidden
          content:
            application/json:
              schema:
                description: Forbidden response
                type: object
                properties:
                  error:
                    example:
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
        '404':
          description: 404 - Not Found
          content:
            application/json:
              schema:
                description: Not Found response
                type: object
                properties:
                  error:
                    example:
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
        '429':
          description: 429 - Too Many Requests
          content:
            application/json:
              schema:
                description: Too Many Requests response
                type: object
                properties:
                  error:
                    example:
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
        '503':
          description: 503 - Service Unavailable
          content:
            application/json:
              schema:
                description: Service Unavailable response
                type: object
                properties:
                  error:
                    example:
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
        default:
          description: 500 - Internal Server Error
          content:
            application/json:
              schema:
                description: Default error response
                type: object
                properties:
                  error:
                    example:
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
components:
  securitySchemes:
    API-ID:
      type: apiKey
      in: header
      name: asapp-api-id
    API-Secret:
      type: apiKey
      in: header
      name: asapp-api-secret

````