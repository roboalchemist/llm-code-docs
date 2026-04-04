# Source: https://www.mintlify.com/docs/api/assistant/create-assistant-message.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Assistant message v1

> Generates a response message from the assistant for the specified domain. Compatible with AI SDK v4.

<Badge color="orange">Deprecated</Badge>

<Info>
  The assistant message v1 endpoint is compatible with **AI SDK v4**. If you use AI SDK v5 or later, use the [assistant message v2 endpoint](/api-reference/assistant/create-assistant-message-v2) instead.
</Info>

## Integration with `useChat`

The `useChat` hook from Vercel's AI SDK is the recommended way to integrate the assistant API into your application.

<Steps>
  <Step title="Install AI SDK v4">
    ```bash  theme={null}
    npm i ai@^4.1.15
    ```
  </Step>

  <Step title="Use the hook">
    ```tsx  theme={null}
    import { useChat } from 'ai/react';

    function MyComponent({ domain }) {
      const { messages, input, handleInputChange, handleSubmit, isLoading } = useChat({
        api: `https://api.mintlify.com/discovery/v1/assistant/${domain}/message`,
        headers: {
          'Authorization': `Bearer ${process.env.PUBLIC_MINTLIFY_ASSISTANT_KEY}`,
        },
        body: {
          fp: 'anonymous',
          retrievalPageSize: 5,
          context: [
            {
              type: 'code',
              value: 'const example = "code snippet";',
              elementId: 'code-block-1',
            },
          ],
        },
        streamProtocol: 'data',
        sendExtraMessageFields: true,
      });

      return (
        <div>
          {messages.map((message) => (
            <div key={message.id}>
              {message.role === 'user' ? 'User: ' : 'Assistant: '}
              {message.content}
            </div>
          ))}
          <form onSubmit={handleSubmit}>
            <input value={input} onChange={handleInputChange} />
            <button type="submit">Send</button>
          </form>
        </div>
      );
    }
    ```

    **Required configuration for Mintlify:**

    * `streamProtocol: 'data'` - Required for streaming responses.
    * `sendExtraMessageFields: true` - Required to send message metadata.
    * `body.fp` - Fingerprint identifier (use 'anonymous' or a user identifier).
    * `body.retrievalPageSize` - Number of search results to use (recommended: 5).

    **Optional configuration:**

    * `body.context` - Array of contextual information to provide to the assistant. Each context object contains:
      * `type` - Either `'code'` or `'textSelection'`.
      * `value` - The code snippet or selected text content.
      * `elementId` (optional) - Identifier for the UI element containing the context.
  </Step>
</Steps>

See [useChat](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat) in the AI SDK documentation for more details.

## Rate limits

The assistant API has the following limits:

* 10,000 uses per key per month
* 10,000 requests per Mintlify organization per hour
* 10,000 requests per IP per day


## OpenAPI

````yaml discovery-openapi.json post /v1/assistant/{domain}/message
openapi: 3.0.1
info:
  title: Mintlify Assistant API
  description: An API to integrate Mintlify discovery features into your product.
  version: 1.0.0
servers:
  - url: https://api.mintlify.com/discovery
security:
  - bearerAuth: []
paths:
  /v1/assistant/{domain}/message:
    post:
      summary: Assistant message v1
      description: >-
        Generates a response message from the assistant for the specified
        domain. Compatible with AI SDK v4.
      parameters:
        - name: domain
          in: path
          required: true
          schema:
            type: string
          description: >-
            The domain identifier from your `domain.mintlify.app` URL. Can be
            found at the end of your dashboard URL. For example,
            `dashboard.mintlify.com/organization/domain` has a domain identifier
            of `domain`.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - fp
                - messages
              properties:
                fp:
                  type: string
                  description: >-
                    Fingerprint identifier for tracking conversation sessions.
                    Use 'anonymous' for anonymous users or provide a unique user
                    identifier.
                threadId:
                  default: null
                  type: string
                  description: >-
                    An optional identifier used to maintain conversation
                    continuity across multiple messages. When provided, it
                    allows the system to associate follow-up messages with the
                    same conversation thread. The threadId is returned in the
                    response as event.threadId when event.type === 'finish'.
                messages:
                  type: array
                  default:
                    - id: foobar
                      role: user
                      content: how do i get started
                      parts:
                        - type: text
                          text: How do I get started
                  items:
                    type: object
                    properties:
                      id:
                        type: string
                        description: Unique identifier for the message.
                      role:
                        type: string
                        enum:
                          - system
                          - assistant
                          - data
                          - user
                        description: The role of the message sender.
                      createdAt:
                        type: string
                        format: date-time
                        description: Timestamp when the message was created.
                      content:
                        type: string
                        description: The content of the message.
                      annotations:
                        type: array
                        items: {}
                        description: Optional array of annotations for the message.
                      parts:
                        type: array
                        items:
                          oneOf:
                            - type: object
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - text
                                text:
                                  type: string
                              required:
                                - type
                                - text
                            - type: object
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - reasoning
                                reasoning:
                                  type: string
                                details:
                                  type: array
                                  items:
                                    oneOf:
                                      - type: object
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - text
                                          text:
                                            type: string
                                          signature:
                                            type: string
                                        required:
                                          - type
                                          - text
                                      - type: object
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - redacted
                                          data:
                                            type: string
                                        required:
                                          - type
                                          - data
                              required:
                                - type
                                - reasoning
                                - details
                            - type: object
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - step-start
                              required:
                                - type
                            - type: object
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - source
                                source:
                                  type: object
                                  properties:
                                    sourceType:
                                      type: string
                                      enum:
                                        - url
                                    id:
                                      type: string
                                    url:
                                      type: string
                                    title:
                                      type: string
                                  required:
                                    - sourceType
                                    - id
                                    - url
                              required:
                                - type
                                - source
                            - type: object
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - tool-invocation
                                toolInvocation:
                                  oneOf:
                                    - type: object
                                      properties:
                                        state:
                                          type: string
                                          enum:
                                            - partial-call
                                        step:
                                          type: number
                                        toolCallId:
                                          type: string
                                        toolName:
                                          type: string
                                        args: {}
                                      required:
                                        - state
                                        - toolCallId
                                        - toolName
                                        - args
                                    - type: object
                                      properties:
                                        state:
                                          type: string
                                          enum:
                                            - call
                                        step:
                                          type: number
                                        toolCallId:
                                          type: string
                                        toolName:
                                          type: string
                                        args: {}
                                      required:
                                        - state
                                        - toolCallId
                                        - toolName
                                        - args
                                    - type: object
                                      properties:
                                        state:
                                          type: string
                                          enum:
                                            - result
                                        step:
                                          type: number
                                        toolCallId:
                                          type: string
                                        toolName:
                                          type: string
                                        args: {}
                                        result: {}
                                      required:
                                        - state
                                        - toolCallId
                                        - toolName
                                        - args
                                        - result
                              required:
                                - type
                                - toolInvocation
                        description: >-
                          Array of message parts with different types including
                          text, reasoning, sources, and tool invocations.
                      experimental_attachments:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                            contentType:
                              type: string
                            url:
                              type: string
                          required:
                            - url
                        description: >-
                          Optional array of experimental attachments for the
                          message.
                    required:
                      - id
                      - role
                      - content
                      - parts
                  description: >-
                    Array of messages in the conversation. On the frontend, you
                    will likely want to use the handleSubmit function from the
                    @ai-sdk package's useChat hook to append user messages and
                    handle streaming responses, rather than manually defining
                    the objects in this array as they have so many parameters.
                retrievalPageSize:
                  type: number
                  default: 5
                  description: >-
                    Number of documentation search results to use for generating
                    the response. Higher values provide more context but may
                    increase response time. Recommended: 5.
                filter:
                  type: object
                  default: null
                  properties:
                    version:
                      type: string
                      description: Optional version filter.
                    language:
                      type: string
                      description: Optional language filter.
                  description: Optional filter criteria for the search.
      responses:
        '200':
          description: Message generated successfully
          content:
            application/json:
              schema:
                type: object
                description: >-
                  Response object with data stream parts formatted with the
                  specified status, headers, and content. For more information,
                  see the AI SDK documentation at
                  [ai-sdk.dev/docs/ai-sdk-ui/streaming-data](https://ai-sdk.dev/docs/ai-sdk-ui/streaming-data).
                  Use the [useChat hook from
                  ai-sdk](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat#usechat)
                  to handle the response stream.
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        The Authorization header expects a Bearer token. Use an assistant API
        key (prefixed with `mint_dsc_`). This is a public key safe for use in
        client-side code. Generate one on the [API keys
        page](https://dashboard.mintlify.com/settings/organization/api-keys) in
        your dashboard.

````