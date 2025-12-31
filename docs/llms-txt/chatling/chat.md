# Source: https://docs.chatling.ai/api-reference/v2/ai-kb/chat.md

# Chat with Knowledge Base AI

> Chat with the AI using the knowledge base as the response source.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

### Body

<ParamField body="message" type="string" required>
  The message to send to the AI.
</ParamField>

<ParamField body="ai_model_id" type="integer" required>
  The ID of the AI model to use for the response. To get a list of available AI models, use the [List AI models](./list-ai-models) endpoint.
</ParamField>

<ParamField body="conversation_id" type="string">
  The ID of the conversation. This allows the AI to remember the context of the conversation.

  If left blank, a new conversation will be created.
</ParamField>

<ParamField body="contact_id" type="string">
  The ID of the contact to associate with the conversation.
</ParamField>

<ParamField body="language_id" type="integer" default="1">
  The ID of the language to use for the AI response. To get a list of available languages, use the [List languages](./list-ai-languages) endpoint.
</ParamField>

<ParamField body="temperature" type="float" default="0">
  The temperature to be used by the AI. The temperature controls the randomness of the response. A lower temperature value, such as 0, will make the outputs more focused and deterministic, whereas a higher temperature, such as 1, will make the responses more diverse and unpredictable.
</ParamField>

<ParamField body="instructions" type="array">
  List of [instructions](/chatbot/ai/instructions) to tailor the AI's response. It can be used to provide additional context to the AI, such as the desired tone or style of the response.

  Must be an array of strings.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="conversation_id" type="string">
      The unique identifier of the conversation.
    </ResponseField>

    <ResponseField name="response" type="string">
      The response from the AI.
    </ResponseField>

    <ResponseField name="sources" type="array">
      <Expandable title="properties">
        <ResponseField name="type" type="string">
          The type of the source, such as `webpage` or `document`.
        </ResponseField>

        <ResponseField name="title" type="string">
          The title of the source.
        </ResponseField>

        <ResponseField name="url" type="string">
          The URL of the source if it's a webpage.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "conversation_id": "3154224116",
          "response": "We offer a variety of AI models to power your chatbot. Here are the models available:\n\n- **GPT-4o**\n- **GPT-4 Turbo**\n- **GPT-3.5 Turbo**\n- **Claude 3.5 Sonnet**\n- **Claude 3 Opus**\n- **Claude 3 Sonnet**\n- **Claude 3 Haiku**\n\nThese models ensure that you can select the best fit for your specific needs and use cases.",
          "sources": [
              {
                  "type": "webpage",
                  "title": "Supported AI Models - Chatling Documentation",
                  "url": "https://docs.chatling.ai/ai/supported-ai-models"
              },
              {
                  "type": "webpage",
                  "title": "Pricing | Chatling",
                  "url": "https://chatling.ai/pricing"
              },
          ]
      }
  }
  ```
</ResponseExample>
