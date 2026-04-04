# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/api-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# API Functions

> Connect to your existing APIs to fetch data or perform actions with API Functions.

API Functions enable GenerativeAgent to call your existing APIs to fetch data or perform actions. They are the most common function type for integrating with backend systems and allow your agent to interact with your existing infrastructure without requiring additional development work.

By using an API Function, you can:

* Connect to your existing APIs without creating new simplified interfaces
* Fetch real-time data from your backend systems
* Perform actions like creating records, updating accounts, or processing transactions
* Leverage your current infrastructure without additional development

To create an API function:

1. [Create a function](#step-1-create-a-new-function)
2. [Select an API connection](#step-2-select-an-api-connection)
3. [Specify name and purpose](#step-3-specify-the-name-and-purpose-of-the-function)
4. [Configure optional settings](#step-4-configure-optional-settings)
5. [Use the function in a task](#step-5-using-the-api-function-in-a-task)

## Step 1: Create a New Function

Navigate to the Functions page and click "Create Function."

1. Select "Connect to an API" and click "Next: Choose an API"
   <Frame>
     <img src="https://mintcdn.com/asapp/NUR2s8D32alf_Gg3/images/generativeagent/ConnectToAPIFunction.png?fit=max&auto=format&n=NUR2s8D32alf_Gg3&q=85&s=04adca38d00823d84d845537d7cedd68" data-og-width="1012" width="1012" data-og-height="599" height="599" data-path="images/generativeagent/ConnectToAPIFunction.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/NUR2s8D32alf_Gg3/images/generativeagent/ConnectToAPIFunction.png?w=280&fit=max&auto=format&n=NUR2s8D32alf_Gg3&q=85&s=b6961fb03b8932738b71ec917411c047 280w, https://mintcdn.com/asapp/NUR2s8D32alf_Gg3/images/generativeagent/ConnectToAPIFunction.png?w=560&fit=max&auto=format&n=NUR2s8D32alf_Gg3&q=85&s=82047fca8dd663c44423994f4d065209 560w, https://mintcdn.com/asapp/NUR2s8D32alf_Gg3/images/generativeagent/ConnectToAPIFunction.png?w=840&fit=max&auto=format&n=NUR2s8D32alf_Gg3&q=85&s=7edd1e6188a6d8aba9943a13dbb86fe2 840w, https://mintcdn.com/asapp/NUR2s8D32alf_Gg3/images/generativeagent/ConnectToAPIFunction.png?w=1100&fit=max&auto=format&n=NUR2s8D32alf_Gg3&q=85&s=3af899f0507bd1fa59e4db891cf33dab 1100w, https://mintcdn.com/asapp/NUR2s8D32alf_Gg3/images/generativeagent/ConnectToAPIFunction.png?w=1650&fit=max&auto=format&n=NUR2s8D32alf_Gg3&q=85&s=7a148b11a576c5a1c5348d32aa6ac516 1650w, https://mintcdn.com/asapp/NUR2s8D32alf_Gg3/images/generativeagent/ConnectToAPIFunction.png?w=2500&fit=max&auto=format&n=NUR2s8D32alf_Gg3&q=85&s=e00f13fa137f55e08ad867dfdaaad04d 2500w" />
   </Frame>

## Step 2: Select an API Connection

Under "Choose an API":

1. Select one of your existing [API connections](/generativeagent/configuring/connect-apis)
2. Click "Next: Function details"

<Note>
  If you don't have any API connections yet, you'll need to [create one](/generativeagent/configuring/connect-apis) first or create a [Mock API Function](/generativeagent/configuring/tasks-and-functions/mock-api).
</Note>

## Step 3: Specify the Name and Purpose of the Function

* **Function Name**: Provide a concise, unique name, using underscores (e.g., `get_account_balance`). By default, the function name will be the same as the API connection name.
* **Function Purpose**: Briefly describe what the function does (e.g., "Retrieves the current account balance for a customer").
  * GenerativeAgent uses this description to determine if/when it should call the function.

Click "Create Function" to create the function. You'll be taken to the function detail page where you can configure additional settings.

## Step 4: Configure Optional Settings

After creating the function, you can configure additional fields to enhance the function's behavior:

* **Message before sending**: Display a message to the user before calling the API
* **Confirmation message**: Show confirmation after successful API calls
* **Reference variables**: The API function response will be part of the conversation context for GenerativeAgent to reference, but you can optionally specify a specific field as a reference variable to either reference it in a [Conditional Template](/generativeagent/configuring/tasks-and-functions/conditional-templates), or to include it when you call a [System Transfer Function](/generativeagent/configuring/tasks-and-functions/system-transfer).

The function detail page shows the function configuration and any available API endpoints.

<Note>
  The function will call the real API during interactions. Make sure your API connection is properly configured and accessible.
</Note>

## Step 5: Using the API Function in a Task

Once you have created your API function, you must add the function to the task's list of available functions for GenerativeAgent to use it.

GenerativeAgent will call the function when it determines the API call is needed to complete the task.

Here's how the function works within a task and conversation flow:

1. GenerativeAgent analyzes the user's request and determines if it needs an API call
2. (Optional) The system can display a "Message before Sending" to the user
3. GenerativeAgent calls the API function with the appropriate parameters
4. The system processes the API response and can use it to generate a response to the user
5. (Optional) The system can display a "Confirmation Message" after successful API calls

<Accordion title="Example scenario using an API Function">
  ```jinja  theme={null}
  # Objective
  Help a customer check their account balance and recent transactions.

  # Context
  - Customer wants to know their current balance
  - They may also want to see recent transactions

  # Instructions
  1. **Gather Account Information:**
     - Ask for the customer's account number or phone number
     - Store "account_number" once provided

  2. **Check Account Balance:**
     - Call the `get_account_balance` function with the account number
     - Display the current balance to the customer

  3. **Show Recent Transactions (if requested):**
     - If the customer asks about recent activity, call the `get_recent_transactions` function
     - Display the transaction history in a user-friendly format

  ```
</Accordion>

## Next Steps

<CardGroup>
  <Card title="API Connections" href="/generativeagent/configuring/connect-apis">
    Learn how to create and configure API connections for your functions.
  </Card>

  <Card title="Mock API Functions" href="/generativeagent/configuring/tasks-and-functions/mock-api">
    Start with mock APIs for testing before connecting to real systems.
  </Card>

  <Card title="Set Variable Functions" href="/generativeagent/configuring/tasks-and-functions/set-variable">
    Learn how to store and manipulate conversation data with Set Variable Functions.
  </Card>

  <Card title="Previewer" href="/generativeagent/configuring/previewer">
    Test your API functions in real-time with the Previewer tool.
  </Card>
</CardGroup>
