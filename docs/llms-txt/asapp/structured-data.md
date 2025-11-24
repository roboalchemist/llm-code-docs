# Source: https://docs.asapp.com/ai-productivity/ai-summary/structured-data.md

# Structured Data

> Extract entities and targeted data from your conversations

Structured data is specific, customizable data points extracted from a conversation. This feature encompasses to main components:

* **Entity extraction**: Automatically identifies and extracts specific pieces of information.
* **Question extraction (Targeted Structured Data)**: Answers predefined questions based on the conversation content.

Entity and Question structured data comes out of the box with entities and questions based per industry, but can be [customized](#customization) to match your unique use cases.

The dynamic nature of structure data makes them capable of solving an endless list of challenges, but may help you with:

* Automating data collection for analytics and reporting
* Facilitating compliance monitoring and quality assurance
* Rapid population of CRMs and other business tools
* Supporting data-driven decision making and process improvement

## How it works

To illustrate how Structured Data works, let's use an example conversation:

> **Agent**: Hello, thank you for contacting XYZ Insurance. How can I assist you today?\
> **Customer**: Hi, I want to check the status of my payout for my claim.\
> **Agent**: Sure, can you please provide me with the claim number?\
> **Customer**: It's H123456789.\
> **Agent**: Thank you. Could you also provide the last 4 digits of your account number?\
> **Customer**: 6789\
> **Agent**: Let me check the details for you. One moment, please.\
> **Agent**: I see that your claim was approved on June 10, 2024, for \$5000. The payout has been processed.\
> **Customer**: Great! When will I receive the money?\
> **Agent**: The payout will be credited to your account within 3-5 business days.\
> **Customer**: Perfect, thank you so much for your help.\
> **Agent**: You’re welcome! Is there anything else I can assist you with?\
> **Customer**: No, that's all. Have a nice day.\
> **Agent**: You too. Goodbye!

AI Summary analyzes this conversation and extracts structured data in two ways:

<Tabs>
  <Tab title="Entity">
    Entity Extraction automatically identifies and extracts specific pieces of information from the conversation. These entities can include things like claim numbers, account details, dates, monetary amounts, and more.

    For our example conversation, the extracted entities might look like this:

    ```javascript  theme={null}
    [
        {
          "name": "Claim Number",
          "value": "H123456789"
        },
        {
          "name": "Account Number Last 4",
          "value": "5678"
        },
        {
          "name": "Approval Date",
          "value": "2024-06-10"
        },
        {
          "name": "Payout Amount",
          "value": 5000
        }
    ]
    ```
  </Tab>

  <Tab title="Question">
    Targeted Structured Data, or Questions, allows you to get answers to predefined queries based on the conversation content. These questions can be customized to address specific aspects of customer interactions, compliance requirements, or any other relevant factors.

    For our example conversation, some predefined questions and their answers might look like this:

    ```javascript  theme={null}
    [
        {
          "name": "Customer Satisfied",
          "answer": "Yes"
        },
        {
          "Name": "Payout Information Provided",
          "answer": "Yes"
        },
        {
          "name": "Verification Completed",
          "answer": "Yes"
        }
    ]
    ```
  </Tab>
</Tabs>

## Generate Structured Data

To generate Structured Data, you first need to provide the conversation transcript to ASAPP.

This example uses our **Conversation API** to provide the transcript, but you have options to use [AI Transcribe](/ai-productivity/ai-transcribe) integration if you have voice conversations you want to send to ASAPP.

<Steps>
  <Step title="Step 1: Configure your structured data fields">
    You need to configure your structured data fields first.

    Work with your ASAPP account team to determine whether one of our out-of-the-box configurations work for you, or if you need to create custom structured data.

    <Note>
      You can also use our APIs to [customize your structured data fields](#customization).
    </Note>
  </Step>

  <Step title="Step 2: Create a conversation">
    To create a [`conversation`](/apis/conversations/create-or-update-a-conversation), provide your IDs for the conversation and customer.

    ```javascript  theme={null}
    curl -X POST 'https://api.sandbox.asapp.com/conversation/v1/conversations' \
    --header 'asapp-api-id: <API KEY ID>' \
    --header 'asapp-api-secret: <API TOKEN>' \
    --header 'Content-Type: application/json' \
    --data '{
      "externalId": "[Your id for the conversation]",
      "customer": {
        "externalId": "[Your id for the customer]",
        "name": "customer name"
      },
      "timestamp": "2024-01-23T11:42:42Z"
    }'
    ```

    A successfully created conversation returns a status code of 200 and a conversation ID.
  </Step>

  <Step title="Step 3: Add messages">
    You need to add the messages for the conversation. You have the choice to add a **single message** for each turn of the conversation, or can upload a **batch of messages** a conversation.

    <Tabs>
      <Tab title="Single message">
        To add a message to a conversation, create a [`message`](/apis/messages/create-a-message) for each turn of the conversation.

        ```bash  theme={null}
        curl -X POST 'https://api.sandbox.asapp.com/conversation/v1/conversations/01HNE48VMKNZ0B0SG3CEFV24WM/messages' \
        --header 'asapp-api-id: \<API KEY ID\>' \
        --header 'asapp-api-secret: \<API TOKEN\>' \
        --header 'Content-Type: application/json' \
        --data '{ 
          "text": "Hello, I would like to upgrade my internet plan to GOLD.",
          "sender": {   
            "role": "customer",
            "externalId": "\[Your id for the customer\]" 
          },
          "timestamp": "2024-01-23T11:42:42Z"
        }'
        ```

        A successfully created message returns a status code of 200 and the id of the message.

        <Warning>We only show one message as an example, though you would create many messages over the source of the conversation.</Warning>
      </Tab>

      <Tab title="Batched messages">
        To add multiple messages to a conversation, call [`/messages/batch`](/apis/messages/create-multiple-messages) with an array of messages for the conversation.

        ```javascript  theme={null}
        curl -X POST 'https://api.sandbox.asapp.com/conversation/v1/conversations/5544332211/messages/batch' \
        --header 'asapp-api-id: <API KEY ID>' \
        --header 'asapp-api-secret: <API TOKEN>' \
        --header 'Content-Type: application/json' \
        --data '{
          "messages": [
            {
              "text": "Hello, thank you for contacting XYZ Insurance. How can I assist you today?",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:00:00Z"
            },
            {
              "text": "Hi, I want to check the status of my payout for my claim.",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:01:00Z"
            },
            {
              "text": "Sure, can you please provide me with the claim number?",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:02:00Z"
            },
            {
              "text": "It\'s H123456789.",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:03:00Z"
            },
            {
              "text": "Thank you. Could you also provide the last 4 digits of your account number?",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:04:00Z"
            },
            {
              "text": "****",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:05:00Z"
            },
            {
              "text": "Let me check the details for you. One moment, please.",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:06:00Z"
            },
            {
              "text": "I see that your claim was approved on June 10, ****, for ****. The payout has been processed.",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:07:00Z"
            },
            {
              "text": "Great! When will I receive the money?",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:08:00Z"
            },
            {
              "text": "The payout will be credited to your account within 3-5 business days.",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:09:00Z"
            },
            {
              "text": "Perfect, thank you so much for your help.",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:10:00Z"
            },
            {
              "text": "You\'re welcome! Is there anything else I can assist you with?",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:11:00Z"
            },
            {
              "text": "No, that\'s all. Have a nice day.",
              "sender": {"role": "customer", "externalId": "cust_1234"},
              "timestamp": "2024-09-09T10:12:00Z"
            },
            {
              "text": "You too. Goodbye!",
              "sender": {"role": "agent", "externalId": "agent_1234"},
              "timestamp": "2024-09-09T10:13:00Z"
            }
          ]
        }'
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Step 4: Generate Structured Data">
    With a conversation containing messages, you can generate Structured Data.

    To generate the Structured Data, create a [`structured-data`](/apis/autosummary/create-structured-data) using the ID of the conversation:

    ```javascript  theme={null}
    curl -X GET 'https://api.sandbox.asapp.com/autosummary/v1/structured-data/5544332211' \
    --header 'asapp-api-id: <API KEY ID>' \
    --header 'asapp-api-secret: <API TOKEN>'
    ```

    A successfully created Structured Data returns a status code of 200 and the extracted data:

    ```javascript  theme={null}
    {
      "conversationId": "01GCS2XA9447BCQANJF2SXXVA0",
      "id": "0083d936-ff70-49fc-ac19-74f1246d8b27",
      "structuredDataMetrics": [
        {
          "name": "Claim Number",
          "value": "H123456789"
        },
        {
          "name": "Account Number Last 4",
          "value": "5678"
        },
        {
          "name": "Approval Date",
          "value": "2024-06-10"
        },
        {
          "name": "Payout Amount",
          "value": 5000
        },
        {
          "name": "Customer Satisfied",
          "answer": "Yes"
        },
        {
          "name": "Payout Information Provided",
          "answer": "Yes"
        },
        {
          "name": "Verification Completed",
          "answer": "Yes"
        }
      ]
    }
    ```

    The structured data represents both the entities and answered questions you have configured.
  </Step>
</Steps>

## Customization

Structured Data questions and entities are fully customizable according to your business needs.

We have a list of potential questions and entities per industry that you can start with. Work with your ASAPP account team to determine whether one of our out-of-the-box configurations work for you, or if you need to create custom structured data.

We offer [APIs to self-serve custom structured data fields](/ai-productivity/ai-summary/structured-data/segments-and-customization).
