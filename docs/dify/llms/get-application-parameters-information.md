# Source: https://docs.dify.ai/api-reference/application/get-application-parameters-information.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Application Parameters Information

> Used at the start of entering the page to obtain information such as features, input parameter names, types, and default values.



## OpenAPI

````yaml en/api-reference/openapi_completion.json get /parameters
openapi: 3.0.1
info:
  title: Completion App API
  description: >-
    The text generation application offers non-session support and is ideal for
    translation, article writing, summarization AI, and more.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Completion App API. Replace {api_base_url} with the
      actual API base URL provided for your application (e.g., from
      props.appDetail.api_base_url).
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Completion
    description: Operations related to text generation and completion.
  - name: Files
    description: Operations related to file management.
  - name: End Users
    description: Operations related to end user information.
  - name: Feedback
    description: Operations related to user feedback.
  - name: TTS
    description: Operations related to Text-to-Speech.
  - name: Application
    description: Operations to retrieve application settings and information.
paths:
  /parameters:
    get:
      tags:
        - Application
      summary: Get Application Parameters Information
      description: >-
        Used at the start of entering the page to obtain information such as
        features, input parameter names, types, and default values.
      operationId: getAppParameters
      responses:
        '200':
          description: Application parameters information.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AppParametersResponse'
              examples:
                success:
                  value:
                    opening_statement: Hello!
                    suggested_questions_after_answer:
                      enabled: true
                    speech_to_text:
                      enabled: true
                    retriever_resource:
                      enabled: true
                    annotation_reply:
                      enabled: true
                    user_input_form:
                      - paragraph:
                          label: Query
                          variable: query
                          required: true
                          default: ''
                    file_upload:
                      image:
                        enabled: false
                        number_limits: 3
                        detail: high
                        transfer_methods:
                          - remote_url
                          - local_file
                    system_parameters:
                      file_size_limit: 15
                      image_file_size_limit: 10
                      audio_file_size_limit: 50
                      video_file_size_limit: 100
components:
  schemas:
    AppParametersResponse:
      type: object
      properties:
        opening_statement:
          type: string
          description: Opening statement.
        suggested_questions:
          type: array
          items:
            type: string
          description: List of suggested questions for the opening.
        suggested_questions_after_answer:
          type: object
          properties:
            enabled:
              type: boolean
              description: Whether suggesting questions after an answer is enabled.
        speech_to_text:
          type: object
          properties:
            enabled:
              type: boolean
              description: Whether speech to text is enabled.
        retriever_resource:
          type: object
          properties:
            enabled:
              type: boolean
              description: >-
                Whether citation and attribution (retriever resource) is
                enabled.
        annotation_reply:
          type: object
          properties:
            enabled:
              type: boolean
              description: Whether annotation reply is enabled.
        user_input_form:
          type: array
          items:
            $ref: '#/components/schemas/UserInputFormItem'
          description: User input form configuration.
        file_upload:
          type: object
          description: File upload configuration.
          properties:
            image:
              type: object
              description: >-
                Image settings. Currently only supports image types: png, jpg,
                jpeg, webp, gif.
              properties:
                enabled:
                  type: boolean
                  description: Whether image upload is enabled.
                number_limits:
                  type: integer
                  description: Image number limit, default is 3.
                detail:
                  type: string
                  description: >-
                    Detail level for image processing (e.g., 'high'). From
                    example, not in main description.
                transfer_methods:
                  type: array
                  items:
                    type: string
                    enum:
                      - remote_url
                      - local_file
                  description: >-
                    List of transfer methods, must choose at least one if
                    enabled.
        system_parameters:
          type: object
          description: System parameters.
          properties:
            file_size_limit:
              type: integer
              description: Document upload size limit (MB).
            image_file_size_limit:
              type: integer
              description: Image file upload size limit (MB).
            audio_file_size_limit:
              type: integer
              description: Audio file upload size limit (MB).
            video_file_size_limit:
              type: integer
              description: Video file upload size limit (MB).
    UserInputFormItem:
      type: object
      description: >-
        Represents a single item in the user input form. It will have one of the
        specific control type keys.
      oneOf:
        - $ref: '#/components/schemas/TextInputControlWrapper'
        - $ref: '#/components/schemas/ParagraphControlWrapper'
        - $ref: '#/components/schemas/SelectControlWrapper'
    TextInputControlWrapper:
      type: object
      properties:
        text-input:
          $ref: '#/components/schemas/TextInputControl'
      required:
        - text-input
    ParagraphControlWrapper:
      type: object
      properties:
        paragraph:
          $ref: '#/components/schemas/ParagraphControl'
      required:
        - paragraph
    SelectControlWrapper:
      type: object
      properties:
        select:
          $ref: '#/components/schemas/SelectControl'
      required:
        - select
    TextInputControl:
      type: object
      description: Text input control.
      properties:
        label:
          type: string
          description: Variable display label name.
        variable:
          type: string
          description: Variable ID.
        required:
          type: boolean
          description: Whether it is required.
        default:
          type: string
          description: Default value.
      required:
        - label
        - variable
        - required
    ParagraphControl:
      type: object
      description: Paragraph text input control.
      properties:
        label:
          type: string
          description: Variable display label name.
        variable:
          type: string
          description: Variable ID.
        required:
          type: boolean
          description: Whether it is required.
        default:
          type: string
          description: Default value.
      required:
        - label
        - variable
        - required
    SelectControl:
      type: object
      description: Dropdown control.
      properties:
        label:
          type: string
          description: Variable display label name.
        variable:
          type: string
          description: Variable ID.
        required:
          type: boolean
          description: Whether it is required.
        default:
          type: string
          description: Default value.
        options:
          type: array
          items:
            type: string
          description: Option values.
      required:
        - label
        - variable
        - required
        - options
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: >-
        API Key authentication. For all API requests, include your API Key in
        the `Authorization` HTTP Header, prefixed with 'Bearer '. Example:
        `Authorization: Bearer {API_KEY}`. **Strongly recommend storing your API
        Key on the server-side, not shared or stored on the client-side, to
        avoid possible API-Key leakage that can lead to serious consequences.**

````

Built with [Mintlify](https://mintlify.com).