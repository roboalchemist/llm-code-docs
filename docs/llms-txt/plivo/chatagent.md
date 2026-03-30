# Source: https://plivo.com/docs/aiagent/deploy/chatagent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat Widget

> Deploy an AI Chat Agent to handle inbound conversations via chat applications

### Deploying a Chat Agent

In this guide, we’ll walk you through deploying an AI Chat Agent to handle inbound conversations on a chat application or chat widget. The Chat Agent will engage with customers by responding to messages received via chat widget.

To deploy a Chat Agent that responds to incoming chat messages:

#### Step 1: Set up the Trigger for Inbound Chat Messages

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/chatagent1.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=fa8c9cd7631eeb530da70ad48bfa0c93" width="1706" height="670" data-path="aiagent/images/chatagent1.png" />
</Frame>

In the agent flow, add the **"When a chat message is received"** trigger under **Incoming Conversations**. This trigger activates the agent when a new message is received via chat.

#### Step 2: Build and Test Your Agent Flow

Design the agent flow to handle different customer queries and scenarios, such as responding to questions or providing customer support. Add common questions as **Quick Response Questions** to help customers get started. Once you’ve built the flow, test it to ensure it performs as expected.

#### Step 3: Configure Chat Application

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/chatagent2.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=87f053b23d7af0aa9589cf731b9c5f58" width="1970" height="1242" data-path="aiagent/images/chatagent2.png" />
</Frame>

* Go to **Settings** > **Chat**.
* From the **Chat** page, you can create a new **Chat Application** by clicking on **Create Application**.

#### Step 4: Select the Agent for Your Chat Application

* Once the application is created, select the agent flow you’ve created for handling inbound chat messages.
* Configure additional settings such as the type of chat (Webchat, In-app Chat) depending on the application’s requirements.

#### Step 5: Finalize and Deploy

Once the chat application is set up and the agent is linked, your Chat Agent will be ready to handle inbound customer messages through the selected chat platform.

<Note>
  Chat Agents handle only **inbound** conversations and cannot initiate messages.
</Note>
