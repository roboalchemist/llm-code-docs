# Source: https://www.courier.com/docs/platform/automations/debugger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Debugger

> Courier’s Automation Debugger simulates test events through automation workflows. It allows inspecting node-level data, verifying run context, and debugging errors before triggering automations via API or production events.

# Automation Debugger

Courier's automation debugging tool can be used to run a test event through your automation template and debug any errors you may come across.

## Creating a Test Run Context

Similar to notification templates, automations can now be tested with test run contexts passed in and saved as test events. These tests can mimic an incoming payload passed through [Segment](/platform/automations/segment), [inbound events](/platform/automations/inbound-events), or an [adhoc automation call](/platform/automations/steps). You can create a test event from the `Debug` tab in your automation template.

<Frame caption="Automation Test Event">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/debugger.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=fb8ce99f2619ef29b59478d09a824569" alt="Automation Test Event" width="2860" height="1418" data-path="assets/platform/automations/debugger.png" />
</Frame>

## Running The Test Run Context

With your automation test event configured, you can execute a test run through the debugging tool to simulate the event passed through the automation workflow. When ready, click on the `Run Again` button and select each node to see the data being passed.

<Frame caption="Test Event Trigger">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/debug-trigger.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=5f1eaa92ee45e147420dc3935158d4f0" alt="Test Event Trigger" width="2036" height="1078" data-path="assets/platform/automations/debug-trigger.png" />
</Frame>

### Verifying Test Data

After running your simulated run, you can select each node in your workflow to verify that the data is passed through to each consecutive node. This can be helpful if you have several nodes that rely on incoming data payloads.

<Frame caption="Data Passed to Each Node">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/debug-check.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=4336dfc95f4afb1d833ec1ee9878bac2" alt="Data Passed to Each Node" width="2018" height="1044" data-path="assets/platform/automations/debug-check.png" />
</Frame>

## Run your Automation

After testing with the debugger, invoke your automation via API with the data payload you want to pass.

`POST https://api.courier.com/automations/:template_id/invoke`

```json  theme={null}
{
  "data": {
    "order_id": "ORD-12345",
    "status": "shipped"
  },
  "profile": {
    "email": "user@example.com",
    "phone_number": "+12345678910",
    "name": "Jane"
  }
}
```

The automation run context shows a successful run with the data you passed.

<Frame caption="Successful Run Context">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/debug-success.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=05a80cd6752db862f59a76d300ecb518" alt="Successful Run Context" width="1830" height="1140" data-path="assets/platform/automations/debug-success.png" />
</Frame>

## Testing GET Profile Nodes

Use the debugger to test a [GET Profile](/platform/automations/get-profile) node before promoting your template to production. The debugger shows the run context passed down your automation after fetching a profile.

<Frame caption="GET Profile Node">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/get-profile-node.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=a32ec4020d914b988eed9eae6fd0b47f" alt="GET Profile Node" width="1894" height="858" data-path="assets/platform/automations/get-profile-node.png" />
</Frame>

## Related Resources

<CardGroup cols={2}>
  <Card title="Automation Designer" href="/platform/automations/designer" icon="pen-ruler">
    Build workflows visually
  </Card>

  <Card title="Dynamic Data" href="/platform/automations/dynamic" icon="database">
    Access and map data in automations
  </Card>
</CardGroup>
