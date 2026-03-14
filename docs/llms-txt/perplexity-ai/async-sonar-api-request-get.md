# Source: https://docs.perplexity.ai/api-reference/async-sonar-api-request-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Async Chat Completion

> Retrieve the response for a given asynchronous chat completion request.



## OpenAPI

````yaml get /v1/async/sonar/{api_request}
openapi: 3.1.0
info:
  title: Perplexity AI API
  description: Perplexity AI API
  version: 1.0.0
servers:
  - url: https://api.perplexity.ai
    description: Perplexity AI API
security: []
paths:
  /v1/async/sonar/{api_request}:
    get:
      summary: Get Async Chat Completion
      description: Retrieve the response for a given asynchronous chat completion request.
      operationId: >-
        get_async_chat_completion_response_async_chat_completions__api_request__get
      parameters:
        - name: api_request
          in: path
          required: true
          schema:
            type: string
            title: Api Request
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AsyncApiChatCompletionsResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBearer: []
components:
  schemas:
    AsyncApiChatCompletionsResponse:
      properties:
        id:
          type: string
          title: Id
          description: Unique identifier for the async request
        model:
          type: string
          title: Model
          description: Model used for the request
        created_at:
          type: integer
          title: Created At
          description: Unix timestamp when the request was created
        started_at:
          anyOf:
            - type: integer
            - type: 'null'
          title: Started At
          description: Unix timestamp when processing started
        completed_at:
          anyOf:
            - type: integer
            - type: 'null'
          title: Completed At
          description: Unix timestamp when processing completed
        response:
          anyOf:
            - $ref: '#/components/schemas/CompletionResponse'
            - type: 'null'
        failed_at:
          anyOf:
            - type: integer
            - type: 'null'
          title: Failed At
          description: Unix timestamp when the request failed (if applicable)
        error_message:
          anyOf:
            - type: string
            - type: 'null'
          title: Error Message
          description: Error message if the request failed
        status:
          $ref: '#/components/schemas/AsyncProcessingStatus'
          description: Current processing status of the request
      type: object
      required:
        - id
        - model
        - created_at
        - status
      title: AsyncApiChatCompletionsResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    CompletionResponse:
      properties:
        id:
          type: string
          title: Id
          description: Unique identifier for the completion
        model:
          type: string
          title: Model
          description: Model used for generation
        created:
          type: integer
          title: Created
          description: Unix timestamp when the completion was created
        usage:
          anyOf:
            - $ref: '#/components/schemas/UsageInfo'
            - type: 'null'
        object:
          type: string
          title: Object
          description: Object type identifier
          default: chat.completion
        choices:
          items:
            $ref: '#/components/schemas/Choice'
          type: array
          title: Choices
          description: Array of completion choices
        citations:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Citations
          description: URLs of sources used to generate the response
        search_results:
          anyOf:
            - items:
                $ref: '#/components/schemas/ApiPublicSearchResult'
              type: array
            - type: 'null'
          title: Search Results
          description: Search results used for context in the response
        images:
          anyOf:
            - items:
                $ref: '#/components/schemas/ImageResult'
              type: array
            - type: 'null'
          title: Images
          description: Array of images returned when return_images is true
        related_questions:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Related Questions
          description: >-
            Array of related questions returned when return_related_questions is
            true
      type: object
      required:
        - id
        - model
        - created
        - choices
      title: CompletionResponse
    AsyncProcessingStatus:
      type: string
      enum:
        - CREATED
        - IN_PROGRESS
        - COMPLETED
        - FAILED
      title: AsyncProcessingStatus
      description: Status enum for async processing.
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
    UsageInfo:
      description: Token usage and cost information for a request
      properties:
        prompt_tokens:
          type: integer
          title: Prompt Tokens
          description: Number of tokens in the prompt/input
        completion_tokens:
          type: integer
          title: Completion Tokens
          description: Number of tokens in the completion/output
        total_tokens:
          type: integer
          title: Total Tokens
          description: Total tokens used (prompt + completion)
        search_context_size:
          anyOf:
            - type: string
            - type: 'null'
          title: Search Context Size
          description: Size of search context used
        citation_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Citation Tokens
          description: Number of tokens used for citations
        num_search_queries:
          anyOf:
            - type: integer
            - type: 'null'
          title: Num Search Queries
          description: Number of search queries executed
        reasoning_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Reasoning Tokens
          description: Number of tokens used for reasoning
        cost:
          $ref: '#/components/schemas/Cost'
          description: Cost breakdown for the request
      type: object
      required:
        - prompt_tokens
        - completion_tokens
        - total_tokens
        - cost
      title: UsageInfo
    Choice:
      description: A single completion choice
      properties:
        index:
          type: integer
          title: Index
          description: Index of the choice in the array
        finish_reason:
          anyOf:
            - type: string
              enum:
                - stop
                - length
            - type: 'null'
          title: Finish Reason
          description: Reason generation stopped (stop or length)
        message:
          $ref: '#/components/schemas/ChatMessage-Output'
          description: Complete message (non-streaming)
        delta:
          $ref: '#/components/schemas/ChatMessage-Output'
          description: Incremental message delta (streaming)
      type: object
      required:
        - index
        - message
        - delta
      title: Choice
    ApiPublicSearchResult:
      description: A single search result from the web
      properties:
        title:
          type: string
          title: Title
          description: Title of the search result page
        url:
          type: string
          title: Url
          description: URL of the search result page
        date:
          anyOf:
            - type: string
            - type: 'null'
          title: Date
          description: Publication date of the result
        last_updated:
          anyOf:
            - type: string
            - type: 'null'
          title: Last Updated
          description: Date the result was last updated
        snippet:
          type: string
          title: Snippet
          description: Text snippet from the search result
          default: ''
        source:
          type: string
          enum:
            - web
            - attachment
          title: Source
          description: Source type of the result (web or attachment)
          default: web
      type: object
      required:
        - title
        - url
      title: ApiPublicSearchResult
    ImageResult:
      properties:
        image_url:
          type: string
          title: Image Url
          description: URL of the image
        origin_url:
          type: string
          title: Origin Url
          description: Original URL where the image was found
        title:
          type: string
          title: Title
          description: Title or description of the image
        width:
          type: integer
          title: Width
          description: Width of the image in pixels
        height:
          type: integer
          title: Height
          description: Height of the image in pixels
      type: object
      required:
        - image_url
        - origin_url
        - title
        - width
        - height
      title: ImageResult
    Cost:
      description: Cost breakdown for a chat completion request
      properties:
        input_tokens_cost:
          type: number
          title: Input Tokens Cost
          description: Cost for input tokens in USD
        output_tokens_cost:
          type: number
          title: Output Tokens Cost
          description: Cost for output tokens in USD
        reasoning_tokens_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Reasoning Tokens Cost
          description: Cost for reasoning tokens in USD
        request_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Request Cost
          description: >-
            Cost for web search requests in USD (includes pro search cost if
            applicable)
        citation_tokens_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Citation Tokens Cost
          description: Cost for citation tokens in USD
        search_queries_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Search Queries Cost
          description: Cost for search queries in USD
        total_cost:
          type: number
          title: Total Cost
          description: Total cost for the request in USD
      type: object
      required:
        - input_tokens_cost
        - output_tokens_cost
        - total_cost
      title: Cost
    ChatMessage-Output:
      properties:
        role:
          $ref: '#/components/schemas/ChatMessageRole'
        content:
          anyOf:
            - type: string
            - items:
                anyOf:
                  - $ref: '#/components/schemas/ChatMessageContentTextChunk'
                  - $ref: '#/components/schemas/ChatMessageContentImageChunk'
                  - $ref: '#/components/schemas/ChatMessageContentFileChunk'
                  - $ref: '#/components/schemas/ChatMessageContentPDFChunk'
                  - $ref: '#/components/schemas/ChatMessageContentVideoChunk'
              type: array
              title: Structured Content
            - type: 'null'
          title: Content
      type: object
      required:
        - role
        - content
      title: ChatMessage
    ChatMessageRole:
      type: string
      enum:
        - system
        - user
        - assistant
        - tool
      title: ChatMessageRole
      description: Chat roles enum
    ChatMessageContentTextChunk:
      properties:
        type:
          type: string
          const: text
          title: Type
        text:
          type: string
          title: Text
      type: object
      required:
        - type
        - text
      title: ChatMessageContentTextChunk
    ChatMessageContentImageChunk:
      properties:
        type:
          type: string
          const: image_url
          title: Type
        image_url:
          anyOf:
            - $ref: '#/components/schemas/URL'
            - type: string
          title: Image Url
      type: object
      required:
        - type
        - image_url
      title: ChatMessageContentImageChunk
    ChatMessageContentFileChunk:
      properties:
        type:
          type: string
          const: file_url
          title: Type
        file_url:
          anyOf:
            - $ref: '#/components/schemas/URL'
            - type: string
          title: File Url
        file_name:
          anyOf:
            - type: string
            - type: 'null'
          title: File Name
      type: object
      required:
        - type
        - file_url
      title: ChatMessageContentFileChunk
    ChatMessageContentPDFChunk:
      properties:
        type:
          type: string
          const: pdf_url
          title: Type
        pdf_url:
          anyOf:
            - $ref: '#/components/schemas/URL'
            - type: string
          title: Pdf Url
      type: object
      required:
        - type
        - pdf_url
      title: ChatMessageContentPDFChunk
    ChatMessageContentVideoChunk:
      properties:
        type:
          type: string
          const: video_url
          title: Type
        video_url:
          anyOf:
            - $ref: '#/components/schemas/VideoURL'
            - type: string
          title: Video Url
      type: object
      required:
        - type
        - video_url
      title: ChatMessageContentVideoChunk
    URL:
      properties:
        url:
          type: string
          title: Url
      type: object
      required:
        - url
      title: URL
    VideoURL:
      properties:
        url:
          type: string
          title: Url
        frame_interval:
          anyOf:
            - type: string
            - type: integer
          title: Frame Interval
          default: 25
      type: object
      required:
        - url
      title: VideoURL
  securitySchemes:
    HTTPBearer:
      type: http
      scheme: bearer

````

Built with [Mintlify](https://mintlify.com).