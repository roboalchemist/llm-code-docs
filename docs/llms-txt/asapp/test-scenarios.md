# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/test-scenarios.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Scenarios

> Learn how to create and use Test Scenarios to test conversations with GenerativeAgent.

A **Test Scenario** simulates a customer profile to test conversations with GenerativeAgent.

These scenarios help you define both the mock API responses and the customer's side of the interaction—goals, known information, and personality—so you can assess how GenerativeAgent handles different scenarios, edge cases, and potential issues.

<Note>
  Use Test Scenarios to test:

  * Key happy-flows
  * Edge cases
  * Common problems or issues
</Note>

There are two ways to use Test Scenarios:

1. **Manual:** 'Talk to GenerativeAgent' mode\
   To save and start using a test scenario to talk to GenerativeAgent, fill in the **Test Name** and **User API profile**.
2. **Automatic:** 'Simulate a customer and conversation' mode\
   To save and start using a test scenario to simulate a customer and conversation, fill in the **Test Name**, **User API profile**, **User Goals**, and **Information the user knows** sections so the customer portion of the conversation can be simulated.

### Create a Test Scenario

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioCreate.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=88af08783a5b6620ffd1e7456ba538ed" data-og-width="1950" width="1950" data-og-height="1718" height="1718" data-path="images/generativeagent/TestScenarioCreate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioCreate.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=84aff3f90200b890a383d11bbccd94f7 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioCreate.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=93d20e65637497482c85cbd8cb1027c6 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioCreate.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8306cf0c53ad233ec4bc6ceba2d21df1 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioCreate.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=1c5fed8e3a4b5aa6a0e860cd1e877655 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioCreate.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ed430eff4b22b7a101d61044a722a9f6 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioCreate.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=236129f3d552ce4022821b03a88e93f1 2500w" />
</Frame>

To create a Test Scenario:

<Steps>
  <Step title="Navigate to Test Scenarios">
    Go to the **Test Scenarios** page in GenerativeAgent and click **"Create Scenario"** to begin creating a new test scenario.
  </Step>

  <Step title="Define Basic Information">
    Start by providing the essential details that identify and describe your test scenario:

    * **Test name**: A clear, descriptive name for your scenario
    * **Description**: (Optional) A brief explanation of what you're testing and what you expect to achieve
  </Step>

  <Step title="Configure API Profile">
    Set up the [User API Profile](#configure-user-api-profile) to define the mock responses for your test case.
  </Step>

  <Step title="(Optional) Set Input Context">
    Add optional settings like [Starting Task](#starting-task-optional) or [Input Variables](#input-variables-optional) to define how the test conversation begins.
  </Step>

  <Step title="(Optional) Define Simulation Profile">
    If you are using the automatic mode, you can configure the customer's behavior and goals by filling in the [Simulation Details](#define-simulation-details) section. Toggle evaluations **on**.
  </Step>

  <Step title="(Optional) Add Evaluations">
    Toggle evaluations **on** and optionally add [Applicability Criteria](#applicability-criteria) and [Evaluation Criteria](#evaluation-criteria) to assess the conversation outcomes.
  </Step>

  <Step title="Save your Test Scenario">
    After completing these steps, save your Test Scenario and [start running it](#run-a-test-scenario) in either manual or automatic simulation mode.
  </Step>
</Steps>

<Note>
  You can now preview the test scenario directly from the test file **after saving** your changes.
</Note>

## Configure User API Profile

The data that GenerativeAgent uses plays a critical role in how it behaves. The User API Profile defines the mock data that will be provided to GenerativeAgent when using this test scenario.

You have two options to mock data:

1. [Auto-generate mock data](#auto-generate-mock-data).
2. [Manually define functions](#manually-define-functions)

### Auto-generate mock data

Auto-generate mock data creates function mocks using the scenario you describe and the schema of the functions in the main branch of the draft environment.

To auto-generate mock data:

1. Click **Generate**.
2. Describe your scenario in a few sentences.
3. Wait up to one minute for the profile to be created (you can close the dialog while you wait).

<Note>
  The system pulls mocked data schemas from the main branch of the draft environment. To test a new function, it needs to have been added to the main branch of the draft environment.
</Note>

<Note>
  Adding details about what information the customer will have to share with GenerativeAgent and what GenerativeAgent will have to do will significantly improve the ability to auto-mock the appropriate APIs.
</Note>

### Manually define functions

If you know the specific data you want to mock for a scenario, you can manually define the functions and mock data.

1. Click **+ Select functions**.
2. Choose the API calls you want to mock (e.g. `getAccountInfo`, `confirmCode`).
3. For each function, provide the mocked **request** and **response** in JSON.

#### Add variants to mocked data

To simulate different API responses under the same function:

1. Click **+ Add variants** at the bottom of a function.
2. Define alternative request parameters and corresponding response schema.
3. Save to include the variant in your scenario.

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserMockedDataVariants.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=69bdbd5e31f22359c641235eeafc961e" data-og-width="989" width="989" data-og-height="255" height="255" data-path="images/generativeagent/TestUserMockedDataVariants.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserMockedDataVariants.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d6436c3816972166d1bf5d6d355b35db 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserMockedDataVariants.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=671176bacd74ea8706a1f937a319b037 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserMockedDataVariants.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=4a1e2e5c1455314abbb9bab3fb424a84 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserMockedDataVariants.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=16462bf79d436187d7888b71dc895082 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserMockedDataVariants.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ce45f702e221ca8c979425a6dc7af9f3 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestUserMockedDataVariants.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7a908a823bbc2897d313909893648c98 2500w" />
</Frame>

### Updating Mock data

You may need to update the mock data after creating a Test Scenario. After creating a Test Scenario, ensure your mock data aligns with your testing needs.

This can be done by updating your scenario when auto-generating the mock data or manually adding the functions and mock data.

### Date & time override (optional)

Often APIs have an implicit or explicit date and time when the system performs them. By default, GenerativeAgent assumes the customer interaction is happening at the date and time the scenario is run and updates timestamps in the API profile accordingly.

You can override the assumed timestamp of the interaction.

## Set Input Context

The **Input Context** defines the initial data and configuration that your system provides to GenerativeAgent when a conversation begins. This ensures your test scenarios accurately simulate real-world interactions.

The input context consists of two main components:

1. **[Input Variables](/generativeagent/configuring/tasks-and-functions/input-variables)**: JSON data that provides context about the customer, conversation, or session
2. **[Starting Task](/generativeagent/configuring/tasks-and-functions/enter-specific-task)**: The specific task or flow that GenerativeAgent should begin with

<Note>
  Ensure your input context matches exactly how your production system passes data to GenerativeAgent. This guarantees your test scenarios will match real conversations identically.
</Note>

## Define Simulation Details

When using automatic mode, define how the simulated customer will behave. Describe what the simulated customer brings to the conversation.

These fields drive the customer's interactions with GenerativeAgent

* The [User Goals](#user-goals).
* The [Information the user knows](#information-the-user-knows).
* The [User personality](#user-personality-optional).

Additionally you can set the **max number of turns** the simulation can run. By default, it is set to **15** turns.

### User goals

Describe the motivations of the simulated customer (e.g. "You want to change your billing address", "You want a refund").

<Note>
  The customer will attempt each goal in sequence; if it fails, it may escalate or skip.
</Note>

### Information the user knows

List identity or account data the customer can provide (e.g., Name, address, confirmation code, account number). The customer will relay this information when prompted; omit some to simulate forgotten details.

<Note>
  To test how GenerativeAgent will handle a customer who *does not* have their account number or a critical piece of information, just leave it off the list.
</Note>

### User personality (optional)

Define the tone and style for your simulated customer (rude, insistent, confused, etc.).\
By default:

> Slightly frustrated but polite. Speaks in short, direct sentences. Only say one sentence at a time, of no more than 8 words.

<Note>
  Click **Revert to default personality** to restore.
</Note>

## Add Evaluations

When evaluations are toggled on, the system runs evaluation logic after the conversation ends.

### Applicability Criteria (optional)

Define preconditions or milestones that must be met in the conversation for the evaluation to run. This is useful to disqualify cases where the conversation didn't reach the part you're testing.

If left blank, the evaluation runs by default.

Example:

> "Customer asked for their bill amount"

### Evaluation Criteria

Define one or more evaluation checks to apply to the conversation.

Examples:

> "The Agent provided the current month's bill amount of \$144.72"
> "The Agent did NOT offer a discount"

Evaluation results appear in the **Previewer**, side-by-side with the conversation after clicking on the **Results** button.

If you update your evaluation or applicability criteria later, you can return to the same conversation in the Previewer and click **Run Eval Again** to re-run against the updated test.

## Run a Test Scenario

Test scenarios are run in the **Previewer** on the side-panel.

To run a Test Scenario:

1. Navigate to the **Previewer** (play-button) on the side-panel.
2. Click **Simulate a customer and conversation**.
3. Select your test scenario from the dropdown.
4. Optionally:
   * Override the starting task by selecting one from the dropdown.
   * Override input variables by pasting JSON into the field.
5. Click **Start Conversation** to begin the test.

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=0f1049b2d1f2f707bb0052d49ba8fb64" data-og-width="1892" width="1892" data-og-height="1114" height="1114" data-path="images/generativeagent/EvaluationsResultsPanel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=f91575a650cbf2245812c91e7463ad81 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=872257a5336ec50d1ebb209924d60a72 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=013a7ce07d9fef850f3c08cd3aca4c66 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=d0fb1113bf79b41daae155307c87acaa 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3aa307719a0b6b106ca7383ad9c099ee 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/EvaluationsResultsPanel.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=a76d877f2d656e20c8a9bdb5ee409e7f 2500w" />
</Frame>

Once the conversation ends:

* Click **Results** to open detailed evaluation outcomes.
* Click **Run Eval Again** to re-run evaluations on the conversation in the previewer.

## Migration of Test Users

The system has migrated all existing Test Users to Test Scenarios and retains their functionality:

* Your Test Users became Test Scenarios automatically. You can still talk to GenerativeAgent with your old test users by selecting them in the dropdown in the previewer.
* The system converted the original default Test User into a default Test Scenario—do not delete it unless you no longer need it.
