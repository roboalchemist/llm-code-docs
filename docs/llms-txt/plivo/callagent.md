# Source: https://plivo.com/docs/aiagent/deploy/callagent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Agent

> Deploy an AI Voice Agent to handle both inbound and outbound calls

In this guide, we'll walk you through deploying an **AI Voice Agent** to handle inbound and outbound calls. The AI agent can be used to engage with customers on a call, either by answering an incoming call or initiating an outbound call.

## **1. Inbound Call Agent**

To deploy a Call Agent that answers inbound calls:

### **Step 1: Set up the Trigger for Inbound Calls**

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/callagent1.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=bf6bf3b084b1151036f8da6114a8a13a" width="1784" height="534" data-path="aiagent/images/callagent1.png" />
</Frame>

* In the Agent flow, add the **"When a call is received"** trigger under **Incoming Conversations**. This trigger will activate the agent when an incoming call is received on the assigned phone number.

### **Step 2: Build and Test Your Agent Flow**

* Customize the agent flow for the incoming conversation, where you can handle various scenarios (e.g., if the call is answered or not).
* Test the agent flow to ensure it responds appropriately to the incoming call and carries out the expected actions.

### **Step 3: Configure Phone Numbers**

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/callagent2.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=1804e177dd9fe5a1efb2124031da229d" width="2340" height="788" data-path="aiagent/images/callagent2.png" />
</Frame>

* Go to **Settings > Phone Numbers** to select the phone number where you want the Call Agent to answer incoming calls.
* In the **"Call Agent"** field, select the agent flow you've created for handling inbound calls. This links your agent to the phone number to handle conversations.

<Note>A single phone number can only have one agent flow mapped for inbound conversations, but a single agent flow can be mapped to multiple numbers.</Note>

## **2. Outbound Call Agent**

Outbound Call Agents can be triggered by an **API request** or an **initiated call within the agent flow**. Follow the steps below to configure your outbound call agent.

### **Step 1: Configure the "Initiate Call" Node**

* To initiate an outbound call, use the **"Initiate call"** node in your agent flow.
* Set the **From number** to a rented phone number in your account and the **To number** to the recipient's phone number.

### **Step 2: Build the Agent Flow for Outbound Calls**

Once the outbound call is initiated, your agent will follow the flow you've designed. This could involve interacting with the customer after the call is answered or handling other scenarios (such as busy or unanswered calls).

### **Step 3: Triggering the Outbound Call**

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/callagent3.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=f523f86bb7cf1646ce1c25dc4ede3eb3" width="1792" height="1010" data-path="aiagent/images/callagent3.png" />
</Frame>

There are multiple ways to trigger an outbound call:

#### **Option 1: API Integration**

* Use the **"Trigger an API Request"** node to trigger the outbound call via an external API. This is useful when you need to integrate outbound call functionality with your CRM or any other external application.

#### **Option 2: Conditional Trigger**

* Set a different trigger to initiate the call based on specific customer actions. For example, if a customer sends a WhatsApp message saying, "Can someone call me to assist?", you can create an inbound WhatsApp trigger, and then use a branch in the flow to initiate the outbound call using the "Initiate call" node.

## Concluding Notes:

* **Inbound Calls**: When a customer calls your number, the agent flow associated with that number will automatically be triggered.
* **Outbound Calls**: You can either trigger outbound calls through API calls or initiate them directly within the agent flow using the "Initiate call" node.
* **Agent Flow Flexibility**: Your agent flow can be designed to respond dynamically based on conditions like call answered, no answer, busy, or rejected.
