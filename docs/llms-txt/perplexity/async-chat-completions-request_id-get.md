# Source: https://docs.perplexity.ai/api-reference/async-chat-completions-request_id-get.md

# Get Async Chat Completion Response

> Retrieves the status and result of a specific asynchronous chat completion job.

## OpenAPI

````yaml get /async/chat/completions/{request_id}
paths:
  path: /async/chat/completions/{request_id}
  method: get
  servers:
    - url: https://api.perplexity.ai
  request:
    security:
      - title: HTTPBearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        request_id:
          schema:
            - type: string
              required: true
              description: The ID of the asynchronous chat completion request.
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
                  - title: ID
                    type: string
                    description: Unique identifier for the asynchronous job.
              model:
                allOf:
                  - title: Model
                    type: string
                    description: The model used for the request.
              created_at:
                allOf:
                  - title: Created At
                    type: integer
                    format: int64
                    description: Unix timestamp of when the job was created.
              started_at:
                allOf:
                  - title: Started At
                    type: integer
                    format: int64
                    nullable: true
                    description: Unix timestamp of when processing started.
              completed_at:
                allOf:
                  - title: Completed At
                    type: integer
                    format: int64
                    nullable: true
                    description: Unix timestamp of when processing completed.
              response:
                allOf:
                  - $ref: '#/components/schemas/ChatCompletionsResponseJson'
                    nullable: true
                    description: >-
                      The actual chat completion response, available when status
                      is COMPLETED.
              failed_at:
                allOf:
                  - title: Failed At
                    type: integer
                    format: int64
                    nullable: true
                    description: Unix timestamp of when processing failed.
              error_message:
                allOf:
                  - title: Error Message
                    type: string
                    nullable: true
                    description: Error message if the job failed.
              status:
                allOf:
                  - $ref: '#/components/schemas/AsyncProcessingStatus'
            title: AsyncApiChatCompletionsResponse
            refIdentifier: '#/components/schemas/AsyncApiChatCompletionsResponse'
            requiredProperties:
              - id
              - model
              - created_at
              - status
        examples:
          example:
            value:
              id: <string>
              model: <string>
              created_at: 123
              started_at: 123
              completed_at: 123
              response:
                id: <string>
                model: <string>
                created: 123
                usage:
                  prompt_tokens: 123
                  completion_tokens: 123
                  total_tokens: 123
                  search_context_size: <string>
                  citation_tokens: 123
                  num_search_queries: 123
                  reasoning_tokens: 123
                object: chat.completion
                choices:
                  - index: 123
                    finish_reason: stop
                    message:
                      content: <string>
                      role: system
                search_results:
                  - title: <string>
                    url: <string>
                    date: '2023-12-25'
                videos:
                  - url: <string>
                    thumbnail_url: <string>
                    thumbnail_width: 123
                    thumbnail_height: 123
                    duration: 123
              failed_at: 123
              error_message: <string>
              status: CREATED
        description: Successfully retrieved async chat completion response.
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Async chat completion response not found.
        examples: {}
        description: Async chat completion response not found.
  deprecated: false
  type: path
components:
  schemas:
    ChatCompletionsMessage:
      title: Message
      type: object
      required:
        - content
        - role
      properties:
        content:
          title: Message Content
          oneOf:
            - type: string
              description: The text contents of the message.
            - type: array
              items:
                $ref: '#/components/schemas/ChatCompletionsMessageContentChunk'
              description: An array of content parts for multimodal messages.
          description: >-
            The contents of the message in this turn of conversation. Can be a
            string or an array of content parts.
        role:
          title: Role
          type: string
          enum:
            - system
            - user
            - assistant
          description: The role of the speaker in this conversation.
    ChatCompletionsMessageContentChunk:
      title: ChatCompletionsMessageContentChunk
      type: object
      properties:
        type:
          title: Content Part Type
          type: string
          enum:
            - text
            - image_url
          description: The type of the content part.
        text:
          title: Text Content
          type: string
          description: The text content of the part.
        image_url:
          title: Image URL Content
          type: object
          properties:
            url:
              title: Image URL
              type: string
              format: uri
              description: URL for the image (base64 encoded data URI or HTTPS).
          required:
            - url
          description: An object containing the URL of the image.
        file_url:
          title: File URL Content
          type: object
          properties:
            url:
              title: File URL
              type: string
              format: uri
              description: URL for the file (base64 encoded data URI or HTTPS).
          required:
            - url
          description: An object containing the URL of the file.
        file_name:
          title: File Name
          type: string
          description: The name of the file being referenced.
          example: document.pdf
      required:
        - type
      description: Represents a part of a multimodal message content.
    ChatCompletionsResponseJson:
      title: ChatCompletionsResponseJson
      type: object
      properties:
        id:
          title: ID
          type: string
          description: A unique identifier for the chat completion.
        model:
          title: Model
          type: string
          description: The model that generated the response.
        created:
          title: Created Timestamp
          type: integer
          description: >-
            The Unix timestamp (in seconds) of when the chat completion was
            created.
        usage:
          $ref: '#/components/schemas/UsageInfo'
        object:
          title: Object Type
          type: string
          default: chat.completion
          description: The type of object, which is always `chat.completion`.
        choices:
          title: Choices
          type: array
          items:
            $ref: '#/components/schemas/ChatCompletionsChoice'
          description: >-
            A list of chat completion choices. Can be more than one if `n` is
            greater than 1.
        search_results:
          title: Search Results
          type: array
          items:
            $ref: '#/components/schemas/ApiPublicSearchResult'
          nullable: true
          description: A list of search results related to the response.
        videos:
          title: Videos
          type: array
          items:
            $ref: '#/components/schemas/VideoResult'
          nullable: true
          description: >-
            A list of video results when media_response.overrides.return_videos
            is enabled. Contains video URLs and metadata.
      required:
        - id
        - model
        - created
        - usage
        - object
        - choices
    VideoResult:
      title: VideoResult
      type: object
      description: Represents a video result returned when video content is enabled.
      properties:
        url:
          title: Video URL
          type: string
          format: uri
          description: The URL of the video.
        thumbnail_url:
          title: Thumbnail URL
          type: string
          format: uri
          nullable: true
          description: The URL of the video thumbnail image.
        thumbnail_width:
          title: Thumbnail Width
          type: integer
          nullable: true
          description: The width of the thumbnail image in pixels.
        thumbnail_height:
          title: Thumbnail Height
          type: integer
          nullable: true
          description: The height of the thumbnail image in pixels.
        duration:
          title: Duration
          type: integer
          nullable: true
          description: The duration of the video in seconds.
      required:
        - url
    UsageInfo:
      title: UsageInfo
      type: object
      properties:
        prompt_tokens:
          title: Prompt Tokens
          type: integer
        completion_tokens:
          title: Completion Tokens
          type: integer
        total_tokens:
          title: Total Tokens
          type: integer
        search_context_size:
          title: Search Context Size
          type: string
          nullable: true
        citation_tokens:
          title: Citation Tokens
          type: integer
          nullable: true
        num_search_queries:
          title: Number of Search Queries
          type: integer
          nullable: true
        reasoning_tokens:
          title: Reasoning Tokens
          type: integer
          nullable: true
      required:
        - prompt_tokens
        - completion_tokens
        - total_tokens
    ChatCompletionsChoice:
      title: ChatCompletionsChoice
      type: object
      properties:
        index:
          title: Index
          type: integer
        finish_reason:
          title: Finish Reason
          type: string
          enum:
            - stop
            - length
          nullable: true
        message:
          $ref: '#/components/schemas/ChatCompletionsMessage'
      required:
        - index
        - message
    ApiPublicSearchResult:
      title: ApiPublicSearchResult
      type: object
      properties:
        title:
          title: Title
          type: string
        url:
          title: URL
          type: string
          format: uri
        date:
          title: Date
          type: string
          format: date
          nullable: true
      required:
        - title
        - url
    AsyncProcessingStatus:
      title: AsyncProcessingStatus
      type: string
      enum:
        - CREATED
        - IN_PROGRESS
        - COMPLETED
        - FAILED
      description: The status of an asynchronous processing job.

````