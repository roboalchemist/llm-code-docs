# Source: https://www.courier.com/docs/tutorials/automations/how-to-automate-message-sequences.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build and Send Your First Automation

> Create a multi-step notification workflow in the visual Automations Designer with sends, delays, data fetching, and conditional branching.

Build a user onboarding automation that sends a welcome message, waits a day, checks whether the user completed setup, and branches to either a follow-up nudge or a silent exit. You'll build the entire workflow visually in the Automations Designer, then invoke it via API.

By the end you'll know how to add and connect nodes, configure conditional logic, pass dynamic data, test with the debugger, and publish.

## Prerequisites

* A [Courier account](https://app.courier.com/) with at least one configured provider (e.g. SendGrid)
* Two published notification templates:
  * **WELCOME\_EMAIL** - the welcome message sent immediately
  * **ONBOARDING\_NUDGE** - the follow-up sent to users who haven't completed setup
* Your Courier API key (found in [Settings > API Keys](https://app.courier.com/settings/api-keys))
* An endpoint that returns onboarding status for a user (e.g. `GET https://api.example.com/users/:id/onboarding`)

<Tip>
  New to Courier templates? Follow [Design and Send Your First Notification](/tutorials/content/how-to-design-your-first-notification) to create and publish a template before starting this tutorial.
</Tip>

## What You'll Build

The finished automation looks like this:

1. **API Invoke** trigger - starts the workflow when you call the API
2. **Send** node - delivers the welcome email
3. **Delay** node - waits 1 day
4. **Fetch Data** node - calls your API to check onboarding status
5. **If** node - branches on `data.onboarding_complete`
   * **True** branch - user finished setup, automation ends
   * **False** branch - **Send** node delivers the follow-up nudge

<Frame caption="The completed onboarding automation in the Automations Designer">
  <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/onboarding-automation-full.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=992e71a62e41c21c48ef0f8d4611946a" alt="Complete onboarding automation flow" width="2062" height="1524" data-path="assets/tutorials/automations/onboarding-automation-full.png" />
</Frame>

## Build the Automation

<Steps>
  <Step title="Create a new automation">
    Navigate to **Orchestration > [Automations](https://app.courier.com/assets/automations)** and click **+ New**. Rename it from "Untitled Automation" to something descriptive like "User Onboarding".

    <Frame caption="Create a new automation from the Automations list page">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/new-automation-button.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=442b3704f13a5848e9742043151c68c1" alt="Automations list page with New Automation button" width="2744" height="1672" data-path="assets/tutorials/automations/new-automation-button.png" />
    </Frame>

    The canvas starts with a placeholder trigger node and an empty action slot.
  </Step>

  <Step title="Configure the API Invoke trigger">
    The default trigger is **API Invoke**, which is what we want. This means the automation runs when you call `POST /automations/:template_id/invoke`.

    Click the trigger node to open its configuration. No changes are needed for the default API invoke; just confirm it's selected.

    <Frame caption="API Invoke trigger configuration">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/trigger-api-invoke.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=68c5c08225bd2754916c1d17445942c2" alt="API Invoke trigger configuration" width="2984" height="1758" data-path="assets/tutorials/automations/trigger-api-invoke.png" />
    </Frame>
  </Step>

  <Step title="Add a Send node for the welcome email">
    From the node palette on the left, drag a **Send** node onto the canvas. Then connect it to the trigger node by clicking and dragging from the dot on the side of the Invoke node to the dot on the side of the Send node.

    Click the Send node to configure it:

    * **Template**: Select your `WELCOME_EMAIL` templated
    * **To**: Set the recipient to `refs.data.user_id` (this references the `user_id` passed in the API call)
    * **Ref**: Set to `welcome` (optional; lets later nodes reference this send's status)

    <Frame caption="Send node configured with the welcome email template">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/send-node-welcome.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=4a0ec469d2ed08726eec7a3ce9d94126" alt="Send node configuration for welcome email" width="2982" height="1694" data-path="assets/tutorials/automations/send-node-welcome.png" />
    </Frame>
  </Step>

  <Step title="Add a Delay node">
    Drag a **Delay** node onto the canvas and connect it to the Send node by clicking and dragging between the dots on the sides of each node.

    Click the Delay node and set:

    * **Duration**: `1 day`

    <Frame caption="Delay node set to wait 1 day">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/delay-node-1day.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=f635999f65c64f68d51a094e87f00eb7" alt="Delay node configured for 1 day" width="2990" height="1758" data-path="assets/tutorials/automations/delay-node-1day.png" />
    </Frame>

    <Note>
      Delay steps have a 5-15 minute variance in processing time. For precise scheduling, you can use the `until` field with an ISO 8601 timestamp instead.
    </Note>
  </Step>

  <Step title="Add a Fetch Data node to check onboarding status">
    Drag a **Fetch Data** node below the Delay node and connect them.

    Click the Fetch Data node and configure:

    * **URL**: Your API endpoint with the user ID interpolated from run context, e.g. `https://api.example.com/users/USER_ID/onboarding`. Use Courier's interpolation syntax to inject `refs.data.user_id` into the URL.
    * **Method**: `GET`
    * **Merge Strategy**: `overwrite` (writes the API response into the automation's data context)

    If your API requires authentication, expand the **Headers** section and add an `Authorization` header (e.g. `Bearer YOUR_API_KEY`). See [Fetch Data authentication patterns](/platform/automations/fetch-data#authentication-patterns) for options.

    <Frame caption="Fetch Data node calling the onboarding status API">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/fetch-data-onboarding.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=c59abd7bc4a1bd4dd71d5799486eb00a" alt="Fetch Data node configuration" width="2984" height="1756" data-path="assets/tutorials/automations/fetch-data-onboarding.png" />
    </Frame>

    Your API should return an object like:

    ```json  theme={null}
    {
      "onboarding_complete": true
    }
    ```

    After this node runs, `data.onboarding_complete` is available to subsequent nodes.
  </Step>

  <Step title="Add an If node to branch on onboarding status">
    Drag an **If** node below the Fetch Data node and connect them.

    Click the If node and configure the condition:

    * **Source**: Data
    * **Field**: `onboarding_complete`
    * **Comparison**: `is`
    * **Value**: `true`

    The If node creates two branches: **True** (user completed onboarding) and **False** (user hasn't completed onboarding).

    <Frame caption="If node branching on the onboarding status">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/if-node-onboarding.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=666cffc58978d6ac4b1988d4885c6fe0" alt="If node condition configuration" width="2986" height="1752" data-path="assets/tutorials/automations/if-node-onboarding.png" />
    </Frame>
  </Step>

  <Step title="Add a Send node to the False branch">
    Drag another **Send** node onto the canvas and connect it to the **False** output of the If node.

    Configure this Send node:

    * **Template**: Select your `ONBOARDING_NUDGE` template
    * **To**: `refs.data.user_id`

    The True branch has no nodes connected to it; the automation simply ends if the user has already completed onboarding.

    <Frame caption="Follow-up Send node connected to the False branch">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/false-branch-send.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=34bb42d2fe8ba1b203e0491a02042082" alt="Send node on the False branch of the If node" width="2982" height="1696" data-path="assets/tutorials/automations/false-branch-send.png" />
    </Frame>
  </Step>
</Steps>

## Test with the Debugger

Before publishing, test the automation with the built-in debugger. The debugger executes a real run, so the Fetch Data node will actually call your URL; make sure your onboarding status endpoint is running before testing.

<Steps>
  <Step title="Create a test event">
    Click the **Debug** tab in the designer. Create a test event with data for an existing user:

    ```json  theme={null}
    {
      "data": {
        "user_id": "user_123",
        "user_name": "Jane"
      },
      "profile": {
        "email": "jane@example.com"
      }
    }
    ```

    <Frame caption="Debug tab with test event data">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/debug-test-event.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=b3dcdd8c12ff3ebb5643ae877e25d383" alt="Debugger test event configuration" width="2026" height="1438" data-path="assets/tutorials/automations/debug-test-event.png" />
    </Frame>
  </Step>

  <Step title="Run and inspect">
    Click **Run** to simulate the automation. Click each node to inspect the data flowing through it. After the Fetch Data node, you should see `onboarding_complete` in the run context, and the If node should follow the expected branch.

    <Frame caption="Inspecting run data at each node in the debugger">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/debugger-inspect-nodes.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=98c27032eff2feb473256a57219a9619" alt="Debugger showing node-level data inspection" width="2986" height="1760" data-path="assets/tutorials/automations/debugger-inspect-nodes.png" />
    </Frame>
  </Step>
</Steps>

## Publish and Invoke

<Steps>
  <Step title="Publish the automation">
    Click the **Publish** button in the upper-right corner. Review the changes in the diff view and confirm.

    <Frame caption="Reviewing changes before publishing">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/publish-diff-view.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=8edc2dbe28f4352ed1ff59ba23e7ddb5" alt="Publish diff view" width="2028" height="1274" data-path="assets/tutorials/automations/publish-diff-view.png" />
    </Frame>
  </Step>

  <Step title="Invoke from the Invoke tab">
    Click the **Invoke** tab. Courier generates a ready-to-use curl command with your template ID already filled in. You can copy this and add your data payload, or click **Invoke** to run it directly with an empty payload.

    To pass runtime data, use the generated curl as a starting point and add your `data` and `profile` objects to the `--data` body:

    ```json  theme={null}
    {
      "data": {
        "user_id": "user_123",
        "user_name": "Jane"
      },
      "profile": {
        "email": "jane@example.com"
      },
      "recipient": "user_123"
    }
    ```

    <Frame caption="Invoke tab with the generated curl command">
      <img src="https://mintcdn.com/courier-4f1f25dc/O3vynfI0MrCDSdSd/assets/tutorials/automations/invoke-tab-curl.png?fit=max&auto=format&n=O3vynfI0MrCDSdSd&q=85&s=f4c1e8321e7b9857d4843a3238675c91" alt="Invoke tab showing generated curl command" width="1742" height="924" data-path="assets/tutorials/automations/invoke-tab-curl.png" />
    </Frame>

    The `data` and `profile` objects become the automation's run context, accessible in every node via `refs.data.*` and `refs.profile.*`.

    In production, call the same endpoint from your application code when a user signs up. The template ID in the curl command is the one you'll use in your SDK calls. See the [Automations API reference](/api-reference/automations/invoke-an-automation) for SDK examples.
  </Step>
</Steps>

## Extending the Workflow

Once you're comfortable with the basics, try adding:

* **A schedule trigger** instead of API Invoke to run the automation daily for new signups. See [Scheduling](/platform/automations/scheduling).
* **A Switch node** instead of If to branch on multiple onboarding stages (e.g. "not started", "in progress", "completed"). See [If / Switch](/platform/automations/control-flow).
* **A Get Profile node** to load the user's full Courier profile before sending, so your templates can reference profile attributes. See [Get Profile](/platform/automations/get-profile).
* **Data mapping** in send nodes to reshape fetched data into clean template variables. See [Dynamic Data](/platform/automations/dynamic).

## What's Next

<CardGroup cols={2}>
  <Card title="How to Cancel an Automation" icon="ban" href="/tutorials/automations/how-to-cancel-an-automation">
    Stop in-flight automations with cancellation tokens
  </Card>

  <Card title="Send Automations via API" icon="robot" href="/tutorials/automations/how-to-send-an-automation">
    Invoke ad-hoc and template-based automations programmatically
  </Card>

  <Card title="Automations With Tenants" icon="building" href="/tutorials/automations/how-to-send-automations-with-tenants">
    Apply tenant-specific branding and data to automation runs
  </Card>

  <Card title="Automations Overview" icon="gear" href="/platform/automations/automations-overview">
    Full reference for all node types and capabilities
  </Card>
</CardGroup>
