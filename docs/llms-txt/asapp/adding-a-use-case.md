# Source: https://docs.asapp.com/generativeagent/build/adding-a-use-case.md

# Adding a use case to GenerativeAgent

> Learn how to add new use cases to GenerativeAgent by creating tasks and functions

Adding a use case to GenerativeAgent involves creating a **Task** that represents the business scenario you want your agent to handle, along with the **Functions** that enable it to perform the necessary actions.

<Note>
  Tasks represent use cases - they define what GenerativeAgent can accomplish for your customers. Functions are the tools that enable those tasks by connecting to your backend systems.
</Note>

## Step 1: Define Your Use Case

Start by clearly defining the business scenario you want GenerativeAgent to handle:

* **Customer goal**: What does the customer want to accomplish?
* **Business context**: What type of issue or request is this?
* **Success criteria**: How do you know when the task is complete?
* **Required actions**: What backend operations are needed?

<AccordionGroup>
  <Accordion title="Example: Order Status Inquiry">
    **Customer goal**: "I want to check where my order is"

    **Business context**: Customer service inquiry about order tracking

    **Success criteria**: Customer receives current order status and tracking information

    **Required actions**: Look up order details, retrieve tracking information, provide status update
  </Accordion>

  <Accordion title="Example: Appointment Scheduling">
    **Customer goal**: "I need to book a doctor's appointment"

    **Business context**: Healthcare appointment booking

    **Success criteria**: Customer has a confirmed appointment with details

    **Required actions**: Check availability, book appointment, send confirmation
  </Accordion>
</AccordionGroup>

## Step 2: Create the Task

Navigate to the Tasks page and create a new task that represents your use case:

<Steps>
  <Step title="Navigate to Tasks">
    Go to the Tasks page in your GenerativeAgent configuration.
  </Step>

  <Step title="Create New Task">
    Click "Create task" to start defining your use case.
  </Step>

  <Step title="Define Task Details">
    Provide the following information:

    * **Task name**: Clear, descriptive name for your use case
    * **Task selector description**: How GenerativeAgent identifies when to use this task
    * **Task message** (optional): Initial response when this task is selected
    * **General Instructions**: Detailed guidance on how to handle this use case
    * **Functions**: Select the functions this task should use

    <Frame>
      <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-91a26448-6a25-8ae7-594e-595572a8c258.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=0d4afa4d118e7f2294a1a1a4670ba04e" alt="GenerativeAgent Task creation interface" data-og-width="512" width="512" data-og-height="407" height="407" data-path="image/uuid-91a26448-6a25-8ae7-594e-595572a8c258.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-91a26448-6a25-8ae7-594e-595572a8c258.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=4166d463c150cdffb2c96075e3df56e7 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-91a26448-6a25-8ae7-594e-595572a8c258.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=5765c62bd1aeeb16d334177efcacda56 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-91a26448-6a25-8ae7-594e-595572a8c258.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=cf8e272922148c8d0654d0ac463ee280 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-91a26448-6a25-8ae7-594e-595572a8c258.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=230c50a6307ff4111e668ee8d0e25380 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-91a26448-6a25-8ae7-594e-595572a8c258.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=a2235c314c27229f541175fd7d0b0e99 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-91a26448-6a25-8ae7-594e-595572a8c258.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=1dfbd81bb18a92c5332d64d95ac0121d 2500w" />
    </Frame>
  </Step>

  <Step title="Write Task Instructions">
    **This is the most critical part of creating a successful use case.** Your task instructions determine how GenerativeAgent behaves and whether it handles your use case correctly.

    Effective task instructions should:

    * **Be specific and actionable**: Tell GenerativeAgent exactly what to do in each scenario
    * **Include examples**: Provide common customer requests and expected responses
    * **Plan for edge cases**: Define what to do when things go wrong
    * **Set clear boundaries**: Specify when to escalate to human agents

    <Note>
      **Need help writing effective instructions?** See our comprehensive guides:

      * [Task Best Practices](/generativeagent/configuring/task-best-practices) - Complete guide to writing effective task instructions
      * [Improving Tasks](/generativeagent/configuring/tasks-and-functions/improving) - Resources and tools for optimizing task performance
    </Note>
  </Step>

  <Step title="Configure Knowledge Base Filtering">
    Specify knowledge base metadata to restrict GenerativeAgent to using only articles with matching metadata for this specific use case.

    This helps ensure GenerativeAgent uses the most relevant information for each specific use case, improving accuracy and reducing irrelevant responses.

    <Note>
      If you followed the [Build your first GenerativeAgent](/generativeagent/getting-started) guide, you already have a Knowledge Base imported.

      Otherwise you can [connect your knowledge base](/generativeagent/configuring/connecting-your-knowledge-base) now.
    </Note>
  </Step>
</Steps>

## Step 3: Create Required Functions

Functions enable GenerativeAgent to perform actions similar to a live agent. For each action your use case requires, create the appropriate function.

### Available Function Types

<CardGroup cols={2}>
  <Card title="API Functions" icon="link" href="/generativeagent/configuring/tasks-and-functions/api-functions">
    Connect to your existing APIs to fetch data or perform actions. Most common function type for integrating with backend systems.
  </Card>

  <Card title="Mock API Functions" icon="code" href="/generativeagent/configuring/tasks-and-functions/mock-api">
    Define ideal API interactions before connecting to real systems. Perfect for testing and development.
  </Card>

  <Card title="Set Variable Functions" icon="floppy-disk" href="/generativeagent/configuring/tasks-and-functions/set-variable">
    Store conversation data as reference variables for future use. Useful for tracking customer information across the conversation.
  </Card>

  <Card title="System Transfer Functions" icon="arrow-right" href="/generativeagent/configuring/tasks-and-functions/system-transfer">
    Signal that control should be transferred to an external system or end the conversation with relevant data.
  </Card>
</CardGroup>

### Creating Functions

<Steps>
  <Step title="Navigate to Functions">
    Go to the Functions page in your GenerativeAgent configuration.
  </Step>

  <Step title="Create New Function">
    Click "Create Function" to start defining your function.
  </Step>

  <Step title="Define Function Details">
    Provide the following information:

    * **Function name**: Clear, descriptive name for the function
    * **Description**: How GenerativeAgent should use this function
    * **API Connection**: The backend system this function connects to
  </Step>

  <Step title="Choose Function Type">
    Select the appropriate function type based on your use case needs:

    <Tabs>
      <Tab title="Connect to an API">
        For functions that need to interact with your live backend systems.

        1. Select an existing [API connection](/generativeagent/configuring/connect-apis)
        2. Choose the API version if multiple are available
        3. Save the function

        GenerativeAgent will call the real API during customer interactions.
      </Tab>

      <Tab title="Create a Mock API Function">
        For testing or when you want to define the ideal API interaction first.

        1. Click "Integrate later"
        2. Define request parameters in JSON schema format
        3. Save the function

        You can replace the Mock call with a real API connection at any time.
      </Tab>

      <Tab title="Set Variable Functions">
        For storing conversation data as reference variables.

        1. Select "Set variable" function type
        2. Define the input GenerativeAgent should use
        3. Add the variables you want to set
        4. Save the function

        Useful for tracking customer information across the conversation.
      </Tab>

      <Tab title="System Transfer Functions">
        For signaling control transfer or conversation ending.

        1. Select "System transfer" function type
        2. Define the input GenerativeAgent should use
        3. Optionally add variables to pass along
        4. Save the function

        Helpful for ending conversations or handing control back to external systems.
      </Tab>
    </Tabs>
  </Step>
</Steps>

## Step 4: Connect Functions to Your Task

Once you've created the necessary functions, connect them to your task:

1. Return to your task configuration
2. Select the functions this task should use
3. Ensure the functions align with the actions your use case requires
4. Test the task with the Previewer to verify everything works correctly

## Step 5: Test Your Use Case

Use the [Previewer](/generativeagent/configuring/previewer) tool to test your new use case:

<Steps>
  <Step title="Access the Previewer">
    Navigate to the [Previewer](/generativeagent/configuring/previewer) in your GenerativeAgent configuration.
  </Step>

  <Step title="Test Realistic Scenarios">
    Create test conversations that represent how customers would interact with your use case. Use [Test Scenarios](/generativeagent/configuring/tasks-and-functions/test-scenarios) to define customer profiles and test different edge cases.
  </Step>

  <Step title="Verify Function Execution">
    Ensure all functions are called correctly and return expected results.
  </Step>

  <Step title="Refine as Needed">
    Make adjustments to task instructions or function configurations based on test results.
  </Step>
</Steps>

## Next Steps

<CardGroup>
  <Card title="Test Your Use Case" href="/generativeagent/configuring/previewer">
    Use the Previewer to test your new use case with realistic scenarios.
  </Card>

  <Card title="Connect Your Knowledge Base" href="/generativeagent/configuring/connecting-your-knowledge-base">
    Learn how to connect your knowledge base for better context and responses.
  </Card>

  <Card title="Integrations" href="/generativeagent/integrate">
    Explore integration options for connecting GenerativeAgent to your existing systems.
  </Card>

  <Card title="Deploy to GenerativeAgent" href="/generativeagent/configuring/deploying-to-generativeagent">
    Learn how to deploy your configured GenerativeAgent to production.
  </Card>
</CardGroup>
