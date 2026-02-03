# Source: https://docs.asapp.com/generativeagent/build-overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Building a GenerativeAgent

> Learn how GenerativeAgent works and the key components you'll configure.

Building a GenerativeAgent means configuring an agent that can handle customer conversations by understanding their needs, accessing relevant information, and taking appropriate actions.

## How GenerativeAgent Works

Unlike traditional bots with predefined flows, GenerativeAgent uses natural language processing to understand and respond to a wide range of customer queries and issues.

<Frame>
  <img src="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/ga-intra-task-breakdown.png?fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=c4d576d6ea72246809e82bfcb7a36a19" alt="GenerativeAgent detailed flow" data-og-width="2176" width="2176" data-og-height="1075" height="1075" data-path="images/generativeagent/ga-intra-task-breakdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/ga-intra-task-breakdown.png?w=280&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=866f8d037c1628256852470ded2c5943 280w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/ga-intra-task-breakdown.png?w=560&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=9254c0aa3a9cd3ddb9ba80cbba07e334 560w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/ga-intra-task-breakdown.png?w=840&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=7e64fea6c2455ef951a836ff009d550d 840w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/ga-intra-task-breakdown.png?w=1100&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=b3c2484c5e4d1382eea62e6412fd9609 1100w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/ga-intra-task-breakdown.png?w=1650&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=37122f69d21dfbad68bb2aedc2b92dc5 1650w, https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/ga-intra-task-breakdown.png?w=2500&fit=max&auto=format&n=c-LDHupSgFxlqz3x&q=85&s=8e66bd7c13c92511ad23fb387ed98c9a 2500w" />
</Frame>

<Steps>
  <Step title="Customer Input">
    When a customer sends a message or speaks, it reaches GenerativeAgent through a connector or API integration.
  </Step>

  <Step title="Knowledge Base Retrieval">
    GenerativeAgent searches its local copy of your knowledge base for relevant information and adds it to the conversation context.

    At every conversation turn, our Knowledge Base service selects the most relevant articles and adds them to the conversation context.

    The system syncs to your knowledge base at regular intervals, according to your configuration.
  </Step>

  <Step title="Task Selection and Execution">
    GenerativeAgent identifies the appropriate task based on the customer's needs and executes the task instructions by choosing one of several actions:

    * **Use a Function**: Call your APIs to retrieve data or perform actions (may make multiple function calls). Functions can also perform local logic, data manipulation, and variable setting.
    * **Request Human Help**: Escalate to a human agent when needed
    * **Change Task**: Switch to a different task if the conversation direction changes
  </Step>

  <Step title="Response Generation">
    GenerativeAgent generates a human-like response to communicate with the customer.
  </Step>
</Steps>

This process continues in a loop until either:

* **GenerativeAgent resolves the conversation** and hands control back to your system
* GenerativeAgent cannot help further and **escalates to a human agent**

## Key Components You'll Configure

### Tasks

Define the specific issues or actions you want GenerativeAgent to handle. Each task includes:

* Clear instructions in human language
* Associated functions for performing actions
* Knowledge base filtering for relevant information

### Functions

Connect GenerativeAgent to your APIs so it can:

* Retrieve customer data
* Perform actions (refunds, account updates, etc.)
* Store conversation variables
* Transfer control to other systems

<Note>
  As part of function configuration, you will create [Backend System Integrations](/generativeagent/integrate) to connect to your APIs.
</Note>

### Knowledge Base

Filter and connect your existing knowledge base so GenerativeAgent can:

* Access relevant articles for each task
* Use metadata to find the right information
* Provide accurate, up-to-date responses

## Understanding Environments

GenerativeAgent operates across three environments to ensure safe testing and deployment. As you refine your tasks, functions, and knowledge base, you'll deploy them through this progression:

* **Draft**: Test and configure your agent components before deployment
* **Sandbox**: Staging environment to validate agent behavior and responses
* **Production**: Live environment where your agent handles real customer conversations

You'll typically start by configuring and testing in Draft, then deploy to Sandbox for validation, and finally promote to Production once everything is working correctly.

<Note>
  Learn more about [deploying to GenerativeAgent](/generativeagent/configuring/deploying-to-generativeagent) for detailed deployment procedures.
</Note>

## Next Steps

<CardGroup>
  <Card title="Adding a use case" href="/generativeagent/build/adding-a-use-case">
    Learn how to add and configure use cases for your GenerativeAgent
  </Card>

  <Card title="Building your first GenerativeAgent" href="/generativeagent/getting-started">
    Learn how to build your first GenerativeAgent that can use your KnowledgeBase to start answering your users' questions.
  </Card>
</CardGroup>
