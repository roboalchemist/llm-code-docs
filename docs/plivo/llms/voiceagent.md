# Source: https://plivo.com/docs/aiagent/getstarted/firstagent/voiceagent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Voice AI Agent

> Build a voice agent for inbound customer support calls

In this guide, we will walk you through building an **Inbound Voice Call Agent** that handles order-related issues for a D2C brand. The voice agent will be deployed on the company’s number, where customers can call in and get assistance with their orders.

<Steps>
  <Step title="Define the Use Case">
    Before building your agent, clearly define the use case and understand the customer’s needs. Think about all the possible issues a customer might have when calling about an order. For example:

    * The customer wants to inquire about their order status
    * The customer wants to cancel or modify their order
    * The customer asks generic questions like refund policies or delivery time.

    Make sure to also think of any edge cases or unusual situations that might come up.
  </Step>

  <Step title="Prepare a Mental Framework for the Agent’s Tasks">
    Imagine that you are hiring a human customer service agent for your brand. Prepare a guide or job description for the agent, listing what tasks they need to handle. Some tasks for your inbound voice agent could include:

    * **Identifying the customer** based on their phone number from Shopify.
    * **Providing order details** (order status, shipping details, etc.).
    * **Handling generic customer queries** like refund policies and delivery times.
    * **Escalating the conversation** to a human representative if needed.
  </Step>

  <Step title="Define the Agent’s Tasks in Detail for Vibe Agent">
    Once you have a mental framework, it’s time to define the tasks in detail. For example, the agent will:

    * Greet the customer.
    * Ask for the issue they’re calling about.
    * If the customer has an order-related issue, verify their details using Shopify API by their phone number.
    * If no matching customer is found, ask them to call from their registered mobile number.
    * For non-order-related queries, refer to the knowledge base.
    * If needed, escalate to a human representative.

    Here’s a sample prompt for the agent:

    > I want to create an Inbound Voice Agent for my D2C brand that can handle customer support calls. The agent's first step after answering the call is to automatically get the customer's mobile number from the dialer. It will then use this number to immediately check our Shopify system for a matching account. If an account is found, the agent can handle specific order-related issues like returns, refunds, or general order status. If the number doesn't match an existing customer, the agent will politely let them know and then ask if they have a generic question or if they would like to be connected with a human representative. For general questions, like our refund policy or delivery times, the agent will look up the answers in a designated knowledge base. The agent will always transfer the conversation to a live human representative if the customer specifically asks to be connected, or if the agent is unable to find the information they need.

    <Frame>
      <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/buildcallagent1.jpg?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=43cfacf950d734bc623b4b9de428aba7" width="2880" height="1760" data-path="aiagent/images/buildcallagent1.jpg" />
    </Frame>
  </Step>

  <Step title="Let Vibe Agent Work Its Magic">
    Allow [Vibe Agent](/aiagent/aistudio/vibeagent) to place nodes in the agent flow builder. It will automatically generate the flow based on the prompts you’ve provided. Be patient and let it complete the flow. Occasionally, you might need to manually intervene (e.g., authorizing [third-party applications](/aiagent/aistudio/mcptools) for tool calls like Shopify integration).

    <Frame>
      <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/buildcallagent2.jpg?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=cb5946683b480b420fe6ccd2edd44525" width="2880" height="1760" data-path="aiagent/images/buildcallagent2.jpg" />
    </Frame>
  </Step>

  <Step title="Review the Workflow and Validate the Happy Path and Edge Cases">
    Once the [Vibe Agent](/aiagent/aistudio/vibeagent) completes the first draft, review the entire workflow:

    * Verify the variables the agent has identified (e.g., customer phone number, order status).
    * Check the intent behind each [path](/aiagent/aistudio/path) or branch of the agent flow (e.g., identifying the customer, handling order inquiries).
    * Verify if the correct API calls (e.g., Shopify) have been set up to fetch or update order details.
    * Ensure the [knowledge base](/aiagent/aistudio/agentconfiguration/knowledgebase) is properly set up for answering generic queries (e.g., refund policies, delivery time).

    <Frame>
      <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/buildcallagent3.jpg?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=4247562162a2a6a6a171989cb15ed731" width="2880" height="1760" data-path="aiagent/images/buildcallagent3.jpg" />
    </Frame>
  </Step>

  <Step title="Make Adjustments Based on New Edge Cases">
    While reviewing, if you think of a new edge case or find something that doesn’t work, you can either:

    * Ask Vibe Agent to fix it automatically by providing a detailed prompt.
    * Make the necessary changes directly in the flow builder.
  </Step>

  <Step title="Make Changes Yourself (If Necessary)">
    While Vibe Agent can handle most tasks, sometimes you may want to make minor adjustments yourself. Use our [Node Reference Guide](/aiagent/aistudio/nodereference/aiconversation) to fully understand the available nodes and how to configure them for your specific use case.
  </Step>

  <Step title="Test the Agent">
    Test the agent by starting simple and expanding the complexity gradually. Use the [Playground](/aiagent/aistudio/playground) to run initial tests, verifying basic functionalities such as:

    * Is the agent correctly identifying the customer from Shopify?
    * Can the agent provide accurate order details based on the customer’s phone number?
    * Does the agent handle generic inquiries and escalate when needed?

    <Frame>
      <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/playground.gif?s=d27cf006524df4bb6359c16abe8f6d00" width="2386" height="1640" data-path="aiagent/images/playground.gif" />
    </Frame>
  </Step>

  <Step title="Make Fixes if the Agent Isn’t Performing as Expected">
    If you find that the agent isn’t performing as expected for certain scenarios:

    * Go back to Vibe Agent, provide a detailed prompt about what needs fixing, and let it update the flow.
    * Alternatively, you can make the necessary changes directly in the flow builder.
  </Step>

  <Step title="Deploy the Agent">
    Once you are satisfied with the agent's performance:

    * [Purchase a number from Plivo](/aiagent/deploy/buynumber) (if you haven’t already).
    * Link the number to your [Call Agent](/aiagent/aistudio/nodereference/callfunctions) configuration.
    * Deploy the agent to handle real customer calls.
  </Step>
</Steps>

Your inbound voice agent is now ready to assist customers, saving valuable time for human support staff by handling order-related issues and generic queries.
