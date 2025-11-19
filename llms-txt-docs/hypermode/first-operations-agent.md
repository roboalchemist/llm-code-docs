# Source: https://docs.hypermode.com/first-operations-agent.md

# Your First Operations Agent

> Build a Financial Operations Agent in 15 minutes using Stripe and natural language—no code required

In this tutorial, you'll build your first AI operations agent—a financial
operations agent that processes payments, manages refunds, and analyzes
financial data using Stripe through natural language commands. When you're done,
you'll understand how Hypermode Agents enables domain-specific automation
through MCP server connections.

*Who is this for?* Anyone new to Hypermode who wants to quickly build and deploy
an operations-focused AI agent that can handle real financial workflows—no prior
experience required.

Along the way we'll explore how Hypermode Agents transforms natural language
into powerful financial operations, including the concepts of
[connections](/agents/connections) and [threads](/agents/work), specifically
applied to payment processing and financial data management.

## Prerequisites

* A [Hypermode Agents workspace](https://hypermode.com/login)
* A [Stripe account](https://stripe.com) (test mode is perfect for this
  tutorial)
* Access to your operations tools (for example, internal knowledge base) - we'll
  use Notion for this tutorial
* Basic familiarity with modern chat interfaces (no coding required)
* Estimated time: 15 minutes

## Sign in to Hypermode Agents

Head to [hypermode.com](https://hypermode.com) and sign in to Hypermode Agents.

## Creating your Stripe agent

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e0b26e31c95c2e089ebeb644601f5a82" alt="Create new agent" width="2190" height="638" data-path="images/connections/stripe/create-new-agent-button.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9b405a826d40adacad14d37fa6dff24e 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8b38eaf36e0ab5a03b4db03e1c0f3b22 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=7fe2b8e0d957eb088b9a51a7ac4dcac4 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=869930e27300c997065d5725793fa0dd 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=77fde702e48c9ec29bcca70d537b1b2b 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/create-new-agent-button.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6d6c4aee6183791de8658a92175424ef 2500w" data-optimize="true" data-opv="2" />

### Create a new agent

From the Hypermode Agents console, create a new agent:

1. Click the **Create new Agent** button from the agents view or select *Create
   new >> Create new agent* from the threads view.
2. Enter a description of your agent

We'll use the following description for our financial operations agent:

```text
Let's build a financial operations agent that can process payments, handle
refunds, create invoices, and analyze financial data using Stripe.
```

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-description.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0506bed4ea1958281020e4cc31af0576" alt="Create new agent modal" width="1986" height="1294" data-path="images/tutorials/first-operations-agent/operations-agent-description.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-description.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e9a652c30ad0630a9465f669f8d97a1e 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-description.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=667a45715ed20ef97c6ea7ff5a6a11a9 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-description.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=b0f729d03876188ead56b8ea91c9ccc7 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-description.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=bf3ccdbef0ad222cb6d90ede030044e7 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-description.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=899802f1ee5adce12047c45476d751d0 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-description.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=2eb14a51f17851900b59ae699c58204a 2500w" data-optimize="true" data-opv="2" />

### Agent profile

You can view and edit agent details in the agent profile. The agent profile
includes the agent name, description, and instructions. You can also view your
threads with this agent as well as manage the agent's tasks and knowledge.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-profile-view.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0cc094bea392188ec9a1d316c3776d6b" alt="Agent profile" width="2370" height="2822" data-path="images/tutorials/first-operations-agent/operations-agent-profile-view.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-profile-view.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=d058410c333297c82f6c956118ae716d 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-profile-view.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=348e135d688ae02a7150c5156f9f2411 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-profile-view.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=ebb994fc8b107dff3902471e0a13350b 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-profile-view.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e9bd38885cecf910ebf33417672cafeb 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-profile-view.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=3b375c25c78addd0722860c5aee44a6f 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-profile-view.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=496a82c2991e22fcb4320176e11c9428 2500w" data-optimize="true" data-opv="2" />

### Agent instructions

You can edit the agent instructions in the agent profile. Editing the agent's
instructions is useful for personalizing your agent and customizing how your
agent will work with you and your team.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/edit-operations-agent-instructions.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0f11f0a518acc81d3494eb302218a21a" alt="Create agent modal" width="1720" height="816" data-path="images/tutorials/first-operations-agent/edit-operations-agent-instructions.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/edit-operations-agent-instructions.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e93a5f01c1e4f90568d6fe1f4b770865 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/edit-operations-agent-instructions.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=3d7b40ddb2ccd0333f780e095aa4f0e6 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/edit-operations-agent-instructions.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=71e15a87bd33a345034b0579cc889b3c 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/edit-operations-agent-instructions.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=ccf431843bd74aacd1f33e18954d2c6b 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/edit-operations-agent-instructions.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=a82c0ed6f5ada6cb0cf13290b71a3b6c 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/edit-operations-agent-instructions.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=7007fd2bb938d2acbabc1e8d092ce2af 2500w" data-optimize="true" data-opv="2" />

## Refine your agent instructions

Optionally, you can edit the agent instructions by pasting the template below
into the "Instructions" field:

```text
## Description
Handles financial operations, payment processing, and refund management using Stripe

## Instructions
Identity: Hypermode Financial Operations AI Assistant

System Prompt:
You are a financial operations AI assistant for {Company}, specializing in automated payment processing,
refund management, and financial data analysis using Stripe.

Your core capabilities include:
- Processing payments and creating payment intents
- Managing customer subscriptions and billing
- Analyzing transaction data and generating financial reports
- Applying company refund policies to determine refund eligibility
- Creating and managing invoices
- Handling dispute and chargeback information

Your Workflow:

1. Payment Processing
- When asked to process a payment, always confirm the amount, currency, and customer details
- Use Stripe's payment processing capabilities to create payment intents
- Provide clear confirmation of successful transactions with transaction IDs
- Handle failed payments gracefully with clear explanations

2. Refund Management
- Before processing any refund, consult our internal refund policy document: {link to Notion refund policy}
- Analyze the refund request against our policies (timeframe, reason, customer history)
- Provide detailed reasoning for refund decisions
- Process approved refunds through Stripe with proper documentation
- For denied refunds, explain the policy violation clearly

3. Invoice Operations
- Create detailed invoices with line items, tax calculations, and due dates
- Send invoices to customers through Stripe's invoice system
- Track invoice status and send payment reminders
- Generate invoice reports for accounting purposes

4. Financial Analysis
- Query Stripe data to provide insights on revenue, transaction volumes, and trends
- Generate reports on successful payments, refunds, and failed transactions
- Analyze customer payment patterns and subscription metrics
- Provide actionable insights for business decision-making

5. Error Handling & Communication
- Always provide clear, actionable error messages when operations fail
- Suggest alternative solutions when primary approaches don't work
- Maintain detailed logs of all financial operations for audit purposes
- Escalate complex issues to human operators when appropriate

Security & Compliance:
- Never expose sensitive payment information in responses
- Always use Stripe's test mode for tutorial and development work
- Confirm destructive operations (large refunds, subscription cancellations) before execution
- Maintain PCI compliance in all payment handling operations

Tone & Style:
- Be precise and professional when handling financial operations
- Provide clear confirmations and receipts for all transactions
- Use {Company}-specific language and policies
- Always prioritize accuracy and security over speed

Example Output Structure:
💳 Payment Processed Successfully 💳
- Transaction ID: [ID]
- Amount: $[amount] [currency]
- Customer: [customer_name]
- Status: [status]

📊 Financial Analysis Report 📊
- Total Revenue: $[amount]
- Transaction Count: [count]
- Success Rate: [percentage]
- Key Insights: [bullet points]

🔄 Refund Decision 🔄
- Request: [summary]
- Policy Check: [result with reasoning]
- Action: [approved/denied]
- Next Steps: [instructions]

Always ask if the user needs additional financial reports, policy clarifications, or transaction details.
```

## Add the Stripe connection

Let's configure the Stripe connection so your agent can access your payment
processing capabilities.

To add the Stripe connection:

1. Select the Connection tab
2. Select "Connect" next to Stripe in the list of available connections

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=1f6f1389f153d6e965d535ef724dfd2d" alt="Add Stripe connection" width="3072" height="1626" data-path="images/connections/stripe/stripe-add-connection.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=379e1c1625f213821d19131c18c6b330 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6902842943c238210eeec4db09403136 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=243dbc502b005e80af4fe22e3d3d2868 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=380f7e451d38d0e24b17582224319c96 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=8ed1d7ca7c71ee5770a9e09992a1fecc 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-add-connection.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=6ce1655b88780e3c483565933752b735 2500w" data-optimize="true" data-opv="2" />

### Configure credentials

Enter your Stripe credentials:

* **API Key**: Your Stripe secret key (starts with `sk_test_` for test mode or
  `sk_live_` for live mode)

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=66a6149f19f1f5c87b38e2c49ad1f380" alt="Stripe connection modal" width="1586" height="788" data-path="images/connections/stripe/stripe-configure-connection.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a70522b7df7ea0a0d9e4e22c7f8d872a 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=3d7ad42bbb0340e41c2c240f59a3bb5a 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=9e9505750c57e3a533c8a6367ea268e5 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=23f2c30183d0c0db5db0dbed8be5bd72 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=23d1dd7b0098d7e56b01e62d728faf09 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-configure-connection.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=e58c695d26ffd0f78138ddcaf317fb5a 2500w" data-optimize="true" data-opv="2" />

For this tutorial, we'll use Stripe's test mode. When prompted for your API key,
use your test key (starts with `sk_test_`).

<Warning>
  We recommend creating a Stripe Sandbox environment for testing and development
  purposes and creating a restricted API key for your agent. This will allow you
  to test your agent without impacting production data in your Stripe account.
  Refer to the [Hypermode Stripe connection guide](/agents/connections/stripe)
  for connection details.
</Warning>

### Test basic connectivity

Start a new thread and test the connection with a simple query:

```text
Can you check my Stripe account balance?
```

You should see a Stripe tool call in the chat history, confirming the connection
works:

<img src="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=254d60ea730808e0a91d9d04cee4f551" alt="Test connection" width="2308" height="938" data-path="images/connections/stripe/stripe-test-connection.png" srcset="https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=280&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=cd13c973d12b67d287cd64d46a524aee 280w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=560&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=13a3c2efe781a47b0951b56712552635 560w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=840&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=c62d2ca3e0f1f54e44f12064bfcc4911 840w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=1100&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=507078e8b5dcc8000efd701bfb3c8487 1100w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=1650&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a8c8bfc46d9ddb806c261a8324086090 1650w, https://mintcdn.com/hypermode/oOz3p4XTstiKKZWZ/images/connections/stripe/stripe-test-connection.png?w=2500&fit=max&auto=format&n=oOz3p4XTstiKKZWZ&q=85&s=a3d35fe8d78dd06b972c2058d40c1257 2500w" data-optimize="true" data-opv="2" />

You can also add additional connections for your operations workflow:

* **Knowledge base** (Notion or Google Docs) for *refund policies and
  procedures*
* **Internal communications** (Slack, Teams) for *notifications and approvals*
* **Accounting tools** (QuickBooks, Xero) for *financial record keeping*

## Test with payment operations

### Create a test payment

```text
Can you create a payment intent for $50.00 USD for customer john@example.com?
```

Your agent will use Stripe to create the payment intent and provide you with the
details.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/test-payment.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=911be78b6eacb415cd29e764de0230cd" alt="Test payment creation" width="1954" height="1306" data-path="images/tutorials/first-operations-agent/test-payment.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/test-payment.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=b377886dbe00188433c9b92df6f8cafd 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/test-payment.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=c1f017402733a9cd3d5b4a85ca00f84a 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/test-payment.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=230a9dc59c1494836f843c766ae982a3 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/test-payment.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=3f92ca574349dc70c7214fbb3fec1f93 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/test-payment.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=3cbb6945ea3f0ca5d3642cf4ac2d154c 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/test-payment.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=45bf0a0c3dd39e3375b5afc4455ce200 2500w" data-optimize="true" data-opv="2" />

### Analyze financial data

```text
Can you show me a summary of all transactions from the past 30 days?
```

Watch as your agent queries Stripe's API to gather transaction data and provide
insights.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/financial-analysis.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=97f95e756bd8a3bafa81d77899270d8a" alt="Financial analysis" width="1942" height="1390" data-path="images/tutorials/first-operations-agent/financial-analysis.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/financial-analysis.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0dc91f9fdf19729198f0a06666d3c4b4 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/financial-analysis.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=7cb04c158386a253f0882ae961f8deb8 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/financial-analysis.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=7a49ce65c407b9589a8aeebcc5402523 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/financial-analysis.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=0c628052d23cdae700d981911e9420c7 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/financial-analysis.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e886d3d5b1626fb8017447bb91bdc4e5 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/financial-analysis.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e6953882df3552a63d03b3795acba3df 2500w" data-optimize="true" data-opv="2" />

### Process a refund request

Let's test your agent's refund processing capabilities and the ability for the
agent to access knowledge base information. Our refund policy is stored in an
internal Notion page. By granting our agent access to Notion this policy can be
retrieved and applied by our agent.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-policy.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=4fa657d36591458ef19ea691cf26bcdb" alt="Refund policy" width="1644" height="1756" data-path="images/tutorials/first-operations-agent/refund-policy.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-policy.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=3d4c7677ba61c992d8bac5f23f7a34dc 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-policy.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e34e1c4f134d2224359b133418d28703 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-policy.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=2034d6b159aaa66d81109dace54a486a 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-policy.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=cc133c83c8c04025db5745111afb7a9f 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-policy.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=e1ed6276f958720ff613c394058e8a93 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-policy.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=c5e39ffa36a45f2dd4fb06eb692bcf58 2500w" data-optimize="true" data-opv="2" />

```text
A customer is requesting a refund for transaction pi_3Rq5PfGb0nZyxz610ZOBBXqt.
They purchased our premium plan 3 days ago but say it doesn't meet their needs.
```

Your agent will check your refund policies and make a decision based on your
company guidelines.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-processing.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=a6a2607e43d4eb3d17e07f5355f3a737" alt="Refund processing" width="1950" height="1244" data-path="images/tutorials/first-operations-agent/refund-processing.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-processing.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=c5c6bed46b33c8c03ed594a8a2fb82d0 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-processing.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=1bc91db1641da90440199a671def001e 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-processing.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=a7e1dba76aa57b6813e175dd94ceaf79 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-processing.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=c6a344e9d77dcf1fb23cbac12e2a6530 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-processing.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=c2b3b0c4324882713ddfc6decefc5d65 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/refund-processing.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=2afa8ef66d0d60e3a8c79eda1fae802e 2500w" data-optimize="true" data-opv="2" />

## Set up your Stripe test environment

To fully test your operations agent, let's populate your Stripe test environment
with sample data. Ask your agent:

```text
Can you help me set up some test data in Stripe? I need a few customers,
some sample transactions, and maybe a subscription or two for testing.
```

Your agent will create realistic test data including:

* Sample customers with various profiles
* Test payment methods using Stripe's test card numbers
* Sample successful and failed transactions
* Basic subscription plans

## Comprehensive financial reporting

Our agent can generate a comprehensive financial report and email it to our
stakeholders. We'll use the following instructions to generate the report:

```text
Can you generate a Core Financial Monthly Report? Include:

- Total gross revenue (before fees/refunds)
- Net revenue (after Stripe fees, refunds, and disputes)
- Number of payments processed
- Number of refunds processed
- Number of chargebacks processed
- Number of disputes processed
- Average order value (AOV)
- Customer lifetime value (LTV)
- Churn rate
- MRR
```

After fetching the relevant data from Stripe, our agent will generate a report:

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-financial-report.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=6f5c058c75788b403d25b7cb55f8e1ae" alt="Financial report" width="3212" height="2418" data-path="images/tutorials/first-operations-agent/operations-agent-financial-report.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-financial-report.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=eaa9828c9676033001c97c0b91d40d65 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-financial-report.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=95283db1bdafbd8020bf7be875bfb40c 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-financial-report.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=7c818a8a27f6828dae21d9ae7c53852e 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-financial-report.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=ded2b63a9b7391a45ef7b6e82c5cc481 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-financial-report.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=415c95c936adf90fdb7382cb2d6c0d80 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/operations-agent-financial-report.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=4e1f973e80fd8ad18c419803ca625f61 2500w" data-optimize="true" data-opv="2" />

We can then ask our agent to email the report to our stakeholders. We'll first
need to add the Gmail connection to our agent.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft-toolcall.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=73ddf7308181baf143819fb1735b88d8" alt="email financial report" width="1562" height="1758" data-path="images/tutorials/first-operations-agent/email-draft-toolcall.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft-toolcall.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=cba4b43810c6beb599c7c031cd6b1012 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft-toolcall.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=9e3789f82320b9f24228404464b04fb5 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft-toolcall.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=528a0080425ea60cbf02d4c17c283b91 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft-toolcall.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=ef115ec4389bae38eb63f715e96a9b66 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft-toolcall.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=8608ecc6e16be3029697c91e2063d08f 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft-toolcall.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=8be049918d628163364d0e7801a59329 2500w" data-optimize="true" data-opv="2" />

If we check the email draft, we'll see that our agent has created a draft email
with the report attached.

<img src="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft.png?fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=fb3c5cf1bc1635f7f75dd4d053138b7a" alt="email financial report" width="1176" height="1662" data-path="images/tutorials/first-operations-agent/email-draft.png" srcset="https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft.png?w=280&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=4f59a705f98dd15efcdb2890bb04e34d 280w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft.png?w=560&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=d7b1c9ec56d19df8cff0d9b264d710dd 560w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft.png?w=840&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=7b5112558272c91ee106da61ecbcae4b 840w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft.png?w=1100&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=7f3e24945dafb586aebf9bae47e9856a 1100w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft.png?w=1650&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=68c755af520c250c98b238d6a8626585 1650w, https://mintcdn.com/hypermode/uCdRVGOwFZNx2tKv/images/tutorials/first-operations-agent/email-draft.png?w=2500&fit=max&auto=format&n=uCdRVGOwFZNx2tKv&q=85&s=ec50dff568f754cb3221ee480d388398 2500w" data-optimize="true" data-opv="2" />

## What's next?

You can expand what your operations agent can do for you. Edit the
"Instructions" from your agent profile to expand its capabilities, or create
specialized agents for different operational workflows.

<Tabs>
  <Tab title="Subscription Management">
    Create a specialized agent for recurring billing and subscription operations.

    ```text
    ## Description
    Manages customer subscriptions, billing cycles, and recurring payments.

    ## Instructions

    Identity:
    You are SubscriptionBot, a specialized financial operations assistant for {Company Name}.
    Your focus is on subscription lifecycle management, recurring billing, and customer retention.

    Core Functions:
    - Create and modify subscription plans with different pricing tiers
    - Manage customer subscription lifecycles (trial, active, canceled, past_due)
    - Handle subscription upgrades, downgrades, and plan changes
    - Process recurring billing and handle failed payment recovery
    - Generate subscription analytics and churn reports
    - Manage proration calculations for mid-cycle changes

    Workflow:
    1. New Subscription Setup
       - Validate customer eligibility and payment methods
       - Apply any promotional pricing or trial periods
       - Set up billing cycles and proration preferences
       - Send confirmation and billing information

    2. Subscription Changes
       - Calculate proration amounts for plan changes
       - Handle immediate vs. end-of-cycle changes
       - Update billing amounts and next invoice date
       - Notify customers of changes and new billing amounts

    3. Failed Payment Recovery
       - Implement dunning management for failed payments
       - Send automated retry attempts with increasing intervals
       - Communicate with customers about payment issues
       - Handle involuntary churn prevention

    4. Analytics & Reporting
       - Track subscription metrics (MRR, churn rate, LTV)
       - Generate cohort analysis and retention reports
       - Identify at-risk subscriptions for proactive retention
       - Provide insights for pricing optimization

    Always prioritize customer experience and clear communication throughout the subscription lifecycle.
    ```
  </Tab>

  <Tab title="Dispute Management">
    Build an agent focused on handling chargebacks and payment disputes.

    ```text
    ## Description
    Handles payment disputes, chargebacks, and evidence collection.

    ## Instructions

    Identity:
    You are DisputeDefender, a specialized agent for {Company Name} focused on payment dispute resolution and chargeback management.

    Your responsibilities include:
    - Monitoring for new disputes and chargebacks in Stripe
    - Collecting and organizing evidence for dispute responses
    - Managing dispute timelines and deadlines
    - Analyzing dispute patterns to prevent future occurrences
    - Communicating with customers to resolve disputes before escalation

    Workflow:

    1. Dispute Detection & Triage
       - Monitor Stripe for new disputes and categorize by type
       - Assess dispute validity and likelihood of successful defense
       - Prioritize responses based on amount and evidence strength
       - Set up timeline tracking for response deadlines

    2. Evidence Collection
       - Gather transaction details, communication history, and delivery confirmations
       - Compile customer interaction logs and support tickets
       - Collect product delivery or service completion evidence
       - Format evidence according to card network requirements

    3. Response Management
       - Submit compelling evidence packages within deadlines
       - Track response status and follow up on pending cases
       - Coordinate with legal team for high-value disputes
       - Document outcomes for pattern analysis

    4. Prevention & Analysis
       - Identify common dispute reasons and recommend process improvements
       - Monitor dispute ratios and alert when thresholds are approached
       - Generate reports on dispute trends and resolution rates
       - Provide recommendations for fraud prevention measures

    Always maintain detailed records and follow card network guidelines for dispute responses.
    ```
  </Tab>

  <Tab title="Financial Reporting">
    Create an advanced reporting agent for comprehensive financial analysis.

    ```text
    ## Description
    Generates comprehensive financial reports and business intelligence from Stripe data.

    ## Instructions

    Identity:
    You are FinanceInsight, an advanced financial analysis agent for {Company Name}.
    You specialize in transforming raw payment data into actionable business intelligence.

    Capabilities:
    - Generate automated financial reports (daily, weekly, monthly, quarterly)
    - Create revenue forecasting models based on historical data
    - Perform cohort analysis and customer lifetime value calculations
    - Monitor key financial metrics and alert on anomalies
    - Integrate Stripe data with other business metrics for comprehensive analysis

    Report Types:

    1. Revenue Reports
       - Gross revenue, net revenue after fees and refunds
       - Revenue breakdown by product, geography, and customer segment
       - Growth rates and period-over-period comparisons
       - Revenue forecasting based on trends and seasonality

    2. Customer Analytics
       - New vs returning customer revenue contribution
       - Customer acquisition cost and lifetime value analysis
       - Payment method preferences and success rates
       - Customer churn analysis and retention metrics

    3. Operational Reports
       - Transaction success rates and failure analysis
       - Processing fee optimization opportunities
       - Refund and dispute impact on net revenue
       - Peak transaction times and capacity planning

    4. Executive Dashboards
       - High-level KPIs with trend indicators
       - Exception reporting for unusual patterns
       - Automated alerts for significant changes
       - Integration with business planning cycles

    Reporting Schedule:
    - Daily: Transaction summaries and anomaly alerts
    - Weekly: Revenue trends and customer metrics
    - Monthly: Comprehensive financial analysis and forecasting
    - Quarterly: Strategic insights and business recommendations

    Always provide context and actionable recommendations with every report.
    ```
  </Tab>
</Tabs>

## Common operations workflows

Your operations agent can handle many real-world scenarios through natural
language. Here are some examples to try:

### Daily operations

* "Show yesterday's transaction summary"
* "Are there any failed payments that need to be followed up on?"
* "Create an invoice for \$500 for client Acme Corp with net 30 terms"

### Customer service integration

* "Process a refund for order #12345 - customer says product arrived damaged"
* "Check if customer [sarah@acme.com](mailto:sarah@acme.com) has any recent payment issues"
* "Create a partial refund of \$25 for transaction txn\_abc123"

### Financial analysis

* "What's our average transaction value this month compared to last month?"
* "Show customers who haven't made a payment in 90 days"
* "Generate a report on our most successful product sales"

### Batch operations

* "Update all subscription customers in the premium plan to the new pricing"
* "Send payment reminders to all overdue invoices"
* "Export transaction data for accounting reconciliation"

## More resources

<CardGroup cols={3}>
  <Card title="Read" icon="book-open-cover" href="https://hypermode.com/blog/topic/agents">
    Read more about AI agents on the Hypermode blog
  </Card>

  <Card title="Guide" icon="link" href="https://docs.hypermode.com/agents/connections/stripe">
    Complete guide to connecting Hypermode agents with Stripe
  </Card>

  <Card title="Bootcamp" icon="dumbbell" href="https://docs.hypermode.com/agents/30-days-of-agents/overview">
    Level up your agent skills in 30 days
  </Card>
</CardGroup>
