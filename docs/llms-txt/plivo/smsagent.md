# Source: https://plivo.com/docs/aiagent/getstarted/firstagent/smsagent.md

# Source: https://plivo.com/docs/aiagent/deploy/sms/smsagent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS Agent

> Deploy an SMS Agent to automate inbound and outbound SMS conversations

In this guide, we’ll walk you through deploying an AI SMS Agent to handle inbound and outbound SMS conversations. The SMS Agent can be used to engage with customers either by responding to inbound SMS or sending outbound SMS messages.

#### 1. Inbound SMS Agent

To deploy an SMS Agent that responds to inbound SMS messages:

Step 1: Set up the Trigger for Inbound SMS Messages

<Frame>
  <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/smsagent1.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=fe8a6b93c4ac7cd8d05cf01ba4ca86b0" width="1726" height="808" data-path="aiagent/images/smsagent1.png" />
</Frame>

In the agent flow, add the **"When an SMS is received"** trigger under **Incoming Conversations**. This trigger will activate the agent when an SMS is received on the assigned phone number.

Step 2: Build and Test Your Agent Flow

Design and customize the agent flow to handle customer queries, such as responding to questions or providing assistance. Test the agent flow to ensure that the agent responds as expected to incoming SMS messages.

Step 3: Configure SMS Agent in Settings

<Frame>
  <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/smsagent2.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=060f77488216f390a3d37c50e91480a7" width="1170" height="984" data-path="aiagent/images/smsagent2.png" />
</Frame>

Go to **Settings > Phone Numbers** to select the phone number where you want the SMS agent to respond to messages.

* In the **"Message Agent"** field, select the agent flow you’ve created for handling inbound SMS.
* Ensure that the correct phone number is mapped to this flow.

A single phone number can only have one agent flow mapped for inbound SMS, but an agent flow can be mapped to multiple numbers.

#### 2. Outbound SMS Agent

<Frame>
  <img src="https://mintcdn.com/plivo/kC7RdeaQ9U2h_t61/aiagent/images/smsagent3.png?fit=max&auto=format&n=kC7RdeaQ9U2h_t61&q=85&s=1693956c8ff0b9586fc7658fc07a9eb9" width="1874" height="1200" data-path="aiagent/images/smsagent3.png" />
</Frame>

To deploy an outbound SMS agent, follow these steps:

Step 1: Configure the "Send Message" Node

In your agent flow, add the **"Send Message"** node:

* Choose **SMS** as the channel.
* Set the **From Number** as a rented number or SID from your Plivo account.
* Enter the **To Number**, which can be either a dynamic value or a fixed number.

Step 2: Triggering the Outbound SMS

There are multiple ways to trigger the outbound SMS:

* **API Integration**: Use the **"Trigger an API Request"** node to trigger the outbound SMS via an external API.
* **Agent Flow Branching**: You can trigger the outbound SMS within your agent flow based on certain conditions or events.

### Concluding Notes:

* **Inbound SMS**: When a customer sends an SMS to your phone number, the agent flow associated with that number will be triggered automatically to respond to the incoming SMS.
* **Outbound SMS**: Outbound SMS can be triggered by API calls or initiated directly within your agent flow using the **"Send Message"** node.
* **Agent Flow Flexibility**: Your agent flow can be designed to dynamically respond based on conditions such as message received, or different scenarios like failed or successful message deliveries.
