# Source: https://www.mintlify.com/docs/api/assistant/create-assistant-message-v2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Assistant message v2

> Generates a response message from the assistant for the specified domain. Compatible with AI SDK v5+.

<Info>
  The assistant message v2 endpoint is compatible with **AI SDK v5+**. If you
  use AI SDK v4, use the [assistant message v1
  endpoint](/api-reference/assistant/create-assistant-message) instead.
</Info>

## Integration with `useChat`

The `useChat` hook from Vercel's AI SDK is the recommended way to integrate the assistant API into your application.

<Steps>
  <Step title="Install AI SDK">
    ```bash  theme={null}
    npm i ai@^6 @ai-sdk/react
    ```
  </Step>

  <Step title="Use the hook">
    ```tsx  theme={null}
    import { useState } from "react";
    import { useChat } from "@ai-sdk/react";
    import { DefaultChatTransport } from "ai";

    function MyComponent({ domain }) {
      const [input, setInput] = useState("");

      const { messages, sendMessage } = useChat({
        transport: new DefaultChatTransport({
          api: `https://api.mintlify.com/discovery/v2/assistant/${domain}/message`,
          headers: {
            Authorization: `Bearer ${process.env.PUBLIC_MINTLIFY_ASSISTANT_KEY}`,
          },
          body: {
            fp: "anonymous",
            retrievalPageSize: 5,
            context: [
              {
                type: "code",
                value: 'const example = "code snippet";',
                elementId: "code-block-1",
              },
            ],
          },
        }),
      });

      return (
        <div>
          {messages.map((message) => (
            <div key={message.id}>
              {message.role === "user" ? "User: " : "Assistant: "}
              {message.parts
                .filter((part) => part.type === "text")
                .map((part) => part.text)
                .join("")}
            </div>
          ))}
          <form
            onSubmit={(e) => {
              e.preventDefault();
              if (input.trim()) {
                sendMessage({ text: input });
                setInput("");
              }
            }}
          >
            <input value={input} onChange={(e) => setInput(e.target.value)} />
            <button type="submit">Send</button>
          </form>
        </div>
      );
    }
    ```

    **Required configuration:**

    * `transport` - Use `DefaultChatTransport` to configure the API connection.
    * `body.fp` - Fingerprint identifier (use `'anonymous'` or a unique user identifier).
    * `body.retrievalPageSize` - Number of search results to use (recommended: 5).

    **Optional configuration:**

    * `body.context` - Array of contextual information to provide to the assistant. Each context object contains:
      * `type` - Either `'code'` or `'textSelection'`.
      * `value` - The code snippet or selected text content.
      * `path` (optional) - Path to the source file or page.
      * `elementId` (optional) - Identifier for the UI element containing the context.
  </Step>
</Steps>

See [useChat](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat) and [Transport](https://ai-sdk.dev/docs/ai-sdk-ui/transport) in the AI SDK documentation for more details.

## Rate limits

The assistant API has the following limits:

* 10,000 uses per key per month
* 10,000 requests per Mintlify organization per hour
* 10,000 requests per IP per day


## OpenAPI

````yaml discovery-openapi.json post /v2/assistant/{domain}/message
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
  /v2/assistant/{domain}/message:
    post:
      summary: Assistant message v2
      description: >-
        Generates a response message from the assistant for the specified
        domain. Compatible with AI SDK v5+.
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
                    Use `anonymous` for anonymous users or provide a unique user
                    identifier.
                threadId:
                  default: null
                  type: string
                  description: >-
                    An optional identifier used to maintain conversation
                    continuity across multiple messages. When provided, it
                    allows the system to associate follow-up messages with the
                    same conversation thread. The `threadId` is returned in the
                    response as `event.threadId` when `event.type === 'finish'`.
                messages:
                  type: array
                  default:
                    - id: foobar
                      role: user
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
                          - user
                        description: The role of the message sender.
                      createdAt:
                        type: string
                        format: date-time
                        description: Timestamp when the message was created.
                      parts:
                        type: array
                        items:
                          oneOf:
                            - type: object
                              description: Text content part.
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
                              description: >-
                                Reasoning content part with optional provider
                                metadata.
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - reasoning
                                text:
                                  type: string
                                providerMetadata:
                                  type: object
                                  description: Optional provider-specific metadata.
                              required:
                                - type
                                - text
                            - type: object
                              description: Source URL reference part.
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - source-url
                                sourceId:
                                  type: string
                                url:
                                  type: string
                                title:
                                  type: string
                                providerMetadata:
                                  type: object
                                  description: Optional provider-specific metadata.
                              required:
                                - type
                                - sourceId
                                - url
                            - type: object
                              description: File attachment part.
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - file
                                mediaType:
                                  type: string
                                url:
                                  type: string
                                filename:
                                  type: string
                              required:
                                - type
                                - mediaType
                                - url
                            - type: object
                              description: Marks the start of a new step.
                              properties:
                                type:
                                  type: string
                                  enum:
                                    - step-start
                              required:
                                - type
                        description: >-
                          Array of message parts. Each part has a type and
                          type-specific fields.
                      metadata:
                        type: object
                        description: Optional metadata associated with the message.
                    required:
                      - id
                      - role
                      - parts
                  description: >-
                    Array of messages in the conversation. Use the handleSubmit
                    function from the @ai-sdk/react package's useChat hook to
                    manage messages and streaming responses.
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
                    groups:
                      type: array
                      items:
                        type: string
                      description: Optional array of group identifiers to filter results.
                  description: Optional filter criteria for the search.
                context:
                  type: array
                  items:
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - code
                          - textSelection
                        description: The type of context being provided.
                      value:
                        type: string
                        description: The code snippet or selected text content.
                      path:
                        type: string
                        description: Optional path to the source file or page.
                      elementId:
                        type: string
                        description: >-
                          Optional identifier for the UI element containing the
                          context.
                    required:
                      - type
                      - value
                  description: >-
                    Optional array of contextual information to provide to the
                    assistant.
      responses:
        '200':
          description: Message generated successfully
          content:
            application/json:
              schema:
                type: object
                description: >-
                  Streaming response compatible with AI SDK v5. Use the [useChat
                  hook from
                  @ai-sdk/react](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat#usechat)
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