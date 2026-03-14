# Source: https://plivo.com/docs/aiagent/getstarted/firstagent/whatsappagent.md

# Source: https://plivo.com/docs/aiagent/deploy/whatsapp/whatsappagent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# WhatsApp Agent

> Deploy AI WhatsApp Agent for handling inbound and outbound conversations

In this guide, we’ll walk you through deploying an AI WhatsApp Agent for inbound and outbound conversations. The AI agent can be used to handle customer interactions on WhatsApp either by responding to incoming messages or initiating an outbound conversation using a pre-approved template.

### 1. Inbound WhatsApp Agent

To deploy a WhatsApp Agent that responds to incoming WhatsApp messages:

#### Step 1: Set up the Trigger for Inbound WhatsApp Messages

<Frame>
  <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/whatsappagent1.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=cd1095c0ca96eb95a9a2cd2165281cd0" width="1726" height="950" data-path="aiagent/images/whatsappagent1.png" />
</Frame>

In the agent flow, add the **"When a WhatsApp message is received"** trigger under **Incoming Conversations**. This trigger activates the mapped agent when a new WhatsApp message is received on the selected WhatsApp number profile.

#### Step 2: Build and Test Your Agent Flow

Design the agent flow to handle different scenarios based on your use case (e.g., responding to customer queries, handling FAQs, etc.). Afterward, test the agent flow to ensure it works as expected.

#### Step 3: Configure Your WhatsApp Number

1. Go to **Settings** > **WhatsApp Configuration**.
2. Select the WhatsApp profile you want to deploy the agent on.
3. In the **"WhatsApp Agent"** field, select the agent flow you have created for handling inbound WhatsApp messages.

<Note>
  A single WhatsApp number can only have one agent flow mapped for inbound conversations, but an agent flow can be mapped to multiple WhatsApp numbers.
</Note>

### 2. Outbound WhatsApp Agent

<Frame>
  <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/whatsappagent2.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=80e92af8ceba7ab761d73e24dd960cb3" width="1800" height="986" data-path="aiagent/images/whatsappagent2.png" />
</Frame>

Outbound WhatsApp Agents are initiated by an API request trigger or by Send Message node within the agent flow.

<Info>
  Meta (WhatsApp) mandates that the first message sent by a Business must be a **template message**. Once the customer responds to this template, the AI agent can take over and handle the conversation in free-form within a 24-hour window.
</Info>

#### Step 1: Configure the "Send Message" Node

1. Use the **"Trigger an API Request"** node to initiate the WhatsApp message via an external API (e.g., a CRM system).
2. Add the **"Send Message"** node to your flow.
3. Set **WhatsApp** as the channel, **Template** as the message type and configure the remaining parameters.

#### Step 2: Conversation only after Customer Responds

Once the customer responds to the WhatsApp template message, the AI agent can carry on with the conversation freely, utilising the designed flow to handle further interactions.

### Concluding Notes

* **Inbound WhatsApp:** When a customer sends a WhatsApp message to your number, the associated agent flow will automatically be triggered.
* **Outbound WhatsApp:** You can either trigger outbound WhatsApp messages via API integration or initiate them directly in your agent flow. Ensure the first message follows Meta's template policy before the agent can take over the conversation.
* **Agent Flow Flexibility:** Your agent flow can be designed to dynamically respond based on conditions such as a message received, message type (template or free form), or customer response.
