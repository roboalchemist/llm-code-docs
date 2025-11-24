# Source: https://docs.chatling.ai/api-reference/v2/conversations/list-conversation-messages.md

# List conversation messages

> Get a list of all the messages for a conversation

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

<ParamField path="conversationId" type="string" required>
  The conversation ID.
</ParamField>

### Query

<ParamField query="page" type="integer" default="1">
  The page number for pagination.
</ParamField>

<ParamField query="sort" type="string" default="date_desc">
  The sort order. Possible values:

  * `date_desc`: Sort by date in descending order.
  * `date_asc`: Sort by date in ascending order.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="pages" type="object">
      <Expandable title="properties">
        <ResponseField name="current_page" type="integer">
          The current page number.
        </ResponseField>

        <ResponseField name="last_page" type="integer">
          The last page number.
        </ResponseField>

        <ResponseField name="per_page" type="integer">
          The number of items per page.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="messages" type="array">
      <Expandable title="properties">
        <ResponseField name="text" type="string">
          The text content of the message.
        </ResponseField>

        <ResponseField name="role" type="string">
          The role of the sender of the message (bot, user, or system).
        </ResponseField>

        <ResponseField name="is_ai_kb_response" type="boolean">
          Whether the message is AI generated and uses the knowledge base.
        </ResponseField>

        <ResponseField name="data" type="object">
          The data of the message. Varies depending on the message type.
        </ResponseField>

        <ResponseField name="created_at" type="string">
          The date and time when the message was created.
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
          "pages": {
              "current_page": 1,
              "last_page": 1,
              "per_page": 15
          },
          "messages": [
              {
                  "text": "System variables are predefined variables that contain system information or can be used to perform specific actions. These variables are automatically created by the Builder.",
                  "role": "bot",
                  "is_ai_kb_response": true,
                  "data": {
                      "helpful_value": null,
                      "sources": [
                          {
                              "type": "webpage",
                              "title": "Types of variables - Chatling Documentation",
                              "url": "https://docs.chatling.ai/builder/variables/variable-types"
                          },
                          {
                              "type": "webpage",
                              "title": "Sidebar - Chatling Documentation",
                              "url": "https://docs.chatling.ai/builder/sidebar"
                          },
                          {
                              "type": "webpage",
                              "title": "What are variables? - Chatling Documentation",
                              "url": "https://docs.chatling.ai/builder/variables/what-are-variables"
                          }
                      ]
                  },
                  "created_at": "2024-06-17T16:09:52+00:00"
              },
              {
                  "text": "What are system variables",
                  "role": "user",
                  "created_at": "2024-06-17T16:09:45+00:00"
              },
              {
                  "text": "**Hello! How can I assist you today?**\n\nIf you have any questions related to our chatbot or services, please feel free to ask. I'm here to help!",
                  "role": "bot",
                  "is_ai_kb_response": true,
                  "data": {
                      "helpful_value": null,
                      "sources": []
                  },
                  "created_at": "2024-06-14T15:45:39+00:00"
              },
              {
                  "text": "Hello!",
                  "role": "user",
                  "created_at": "2024-06-14T15:45:34+00:00"
              }
          ]
      }
  }
  ```
</ResponseExample>
