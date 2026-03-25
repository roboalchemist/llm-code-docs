# Source: https://www.courier.com/docs/tutorials/journeys/how-to-build-a-multi-step-onboarding-journey.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Build a Multi-Step Onboarding Journey

> Build an onboarding sequence with delays, a fetch node, branching, and multiple send nodes to guide new users through setup.

This tutorial builds a real onboarding journey: welcome email on signup, wait 24 hours, check if the user completed setup, then send a congratulations email or a reminder nudge depending on the result.

## Prerequisites

* Familiarity with [Create Your First Journey](/tutorials/journeys/how-to-create-your-first-journey) (or comfortable creating a journey from scratch)
* An email provider configured in your Courier workspace
* An internal endpoint that returns whether a user completed onboarding (e.g., `GET /users/:id/onboarding-status` returning JSON with a `completed` boolean)

## What You'll Build

```
Trigger (API)
  → Send: Welcome email
  → Delay: 24 hours
  → Fetch: GET /users/{{user_id}}/onboarding-status
  → Branch:
      ├─ Completed          → Send: Onboarding Complete
      └─ Default            → Send: Reminder Email
```

## Build the Journey

<Steps>
  <Step title="Create a new journey with an API trigger">
    Navigate to [Journeys](https://app.courier.com/journeys), click **New Journey**, and select **API** as the trigger type.

    Add the following schema fields:

    | Field         | Type   |
    | ------------- | ------ |
    | `user_name`   | String |
    | `signup_plan` | String |
  </Step>

  <Step title="Add the welcome email">
    Drag a **Send** node onto the canvas below the trigger. Select **Email** as the channel and click **+ Create** to build the template.

    Design a welcome message. Set the **Subject** to `Welcome to Courier, {{user_name}}!` and add a text block in the body: `You're on the {{signup_plan}} plan. Here's how to get the most out of your account...`

    Click the pencil icon next to the template title at the top left and rename it to "Welcome Email." Close the designer when you're done.
  </Step>

  <Step title="Add a 24-hour delay">
    Drag a **Delay** node below the send node. Set the type to **Duration** and enter `24 hours`.

    This gives the user a day to explore before you check on their progress.
  </Step>

  <Step title="Add a fetch node to check onboarding status">
    Drag a **Fetch Data** node below the delay. Configure it:

    | Field              | Value                                                         |
    | ------------------ | ------------------------------------------------------------- |
    | **URL**            | `https://api.yourapp.com/users/{{user_id}}/onboarding-status` |
    | **Method**         | GET                                                           |
    | **Merge Strategy** | Soft Merge                                                    |

    The `user_id` variable comes from the invocation request, not the trigger schema. If you need it in a fetch URL, add `user_id` as a String schema field on the trigger and pass it in the `data` object when invoking.

    The response should include a boolean field (e.g., `{ "completed": true }`). With Soft Merge, the response fields are added to the journey context without overwriting existing data. Downstream nodes can reference them with the `data.` prefix.
  </Step>

  <Step title="Add a branch node">
    Drag a **Branch** node below the fetch node. Configure two paths:

    **Path 1: Completed**

    * Field: `data.completed`
    * Operator: is equal
    * Value: `true`

    **Default** (automatic fallback)
  </Step>

  <Step title="Add the congratulations email">
    On the "Completed" path, add a **Send** node for email. Create a template named "Onboarding Complete" with **Subject** `You're all set, {{user_name}}!` and a body congratulating them on completing setup.
  </Step>

  <Step title="Add the reminder email">
    On the "Default" path, add a **Send** node for email. Create a template named "Reminder Email" with **Subject** `Need a hand, {{user_name}}?` and a body nudging them to finish setup.
  </Step>

  <Step title="Publish and test">
    Click **Publish**. Then invoke the journey:

    <CodeGroup>
      ```bash cURL icon="terminal" wrap theme={null}
      curl -X POST https://api.courier.com/journeys/YOUR_JOURNEY_ID/invoke \
        -H "Authorization: Bearer $COURIER_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "user_id": "user_123",
          "data": {
            "user_name": "Jane",
            "signup_plan": "pro"
          }
        }'
      ```

      ```javascript Node.js icon="node-js" theme={null}
      const { runId } = await client.journeys.invoke("YOUR_JOURNEY_ID", {
        userId: "user_123",
        data: {
          user_name: "Jane",
          signup_plan: "pro",
        },
      });
      ```

      ```python Python icon="python" theme={null}
      response = client.journeys.invoke(
          "YOUR_JOURNEY_ID",
          user_id="user_123",
          data={
              "user_name": "Jane",
              "signup_plan": "pro",
          },
      )
      ```
    </CodeGroup>

    The welcome email sends immediately. After 24 hours, the fetch node checks onboarding status and the branch routes to the appropriate follow-up.

    <Frame caption="The completed onboarding journey: API trigger, welcome email, 24-hour delay, fetch, branch, and two send nodes">
      <img src="https://mintcdn.com/courier-4f1f25dc/US23xPO8q7EoK5r0/assets/tutorials/journeys/onboarding-canvas.png?fit=max&auto=format&n=US23xPO8q7EoK5r0&q=85&s=4012b68d6f322e650910b8a09a6eaa9a" width="1956" height="1786" data-path="assets/tutorials/journeys/onboarding-canvas.png" />
    </Frame>
  </Step>
</Steps>

## Testing Without the Delay

During development, set the delay to 1 minute instead of 24 hours so you can test the full flow quickly. Remember to change it back before publishing.

## Inspecting the Run

Open the **Logs** tab to see the run. Since this journey has a 24-hour delay, the run will show as "Waiting" until the delay expires. After the delay, you can click through each node to see the fetch response, branch decision, and send outcome.

See [Run Inspection](/platform/journeys/run-inspection) for a full guide on debugging runs.

## What's Next

<CardGroup cols={2}>
  <Card title="Create Your First Journey" href="/tutorials/journeys/how-to-create-your-first-journey" icon="circle-play">
    Start with the basics: trigger, send, publish, invoke
  </Card>

  <Card title="Building Your Journey" href="/platform/journeys/building-journeys" icon="arrow-progress">
    Reference for all node types
  </Card>

  <Card title="Fetch Data" href="/platform/journeys/nodes/fetch-data" icon="download">
    Full reference for HTTP requests and merge strategies
  </Card>

  <Card title="Run Inspection" href="/platform/journeys/run-inspection" icon="magnifying-glass">
    Step through runs to debug delivery issues
  </Card>
</CardGroup>
