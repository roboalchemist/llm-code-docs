# Source: https://www.courier.com/docs/platform/automations/designer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# The Automations Designer

> Courier’s Automations Designer is a visual builder for creating notification workflows. Add trigger and action nodes, configure logic, and invoke automations via API, triggers, or in-app testing.

## Creating an Automation

Start by navigating to the [automations page within the Courier
app](https://app.courier.com/automations). From there, a new automation template can be created by
clicking the `New Automation` Button.

<Frame caption="Automations Home Page">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/automations-list-page.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=8b1551dc96bf415e0c3c5b5c24683a87" alt="Automations Home Page" width="2860" height="696" data-path="assets/platform/automations/automations-list-page.png" />
</Frame>

## Renaming an Automation

To rename a template, click the name in the upper left hand corner of the designer. By default, the
name is "Untitled Automation". The name is automatically saved after being updated.

<Frame caption="Renaming an Automation Template">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/renaming.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=aa21dc21c767d5bd34e4b23927dba84c" alt="Renaming an automation template" width="1124" height="320" data-path="assets/platform/automations/renaming.png" />
</Frame>

## Working with Automation Nodes

A new template starts with a placeholder trigger node. A trigger node defines what starts an automation run. The trigger is optional; you can always invoke a template directly via `POST /automations/:template_id/invoke`.

To add nodes, expand from the list on the left and then click and drag a node onto the right. The first trigger and action node will snap into their respective placeholders:

Nodes are executed sequentially through their connections, from top to bottom. To connect two nodes, click and drag from the white dot at the bottom of the source node to the top of the target node:

## Automation Invocation

<Warning>
  Be sure to publish the template before invoking (using the publish button on the upper right).
</Warning>

There are a few ways to invoke a template, either directly in the automation template, through a trigger node, or through an api call.

See [Scheduling automations](/platform/automations/scheduling) or [Triggering With Segment](/platform/automations/segment) to get
an understanding of how trigger nodes work.

### Difference View

When publishing a template, the automation designer will prompt the user with a difference view confirmation showing the changes between versions. You can confirm the changes on this window.

<Frame caption="Difference Modal">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/diff-view.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=9a46984a0a41863f702ec7667c067d29" alt="Difference Modal" width="2794" height="1476" data-path="assets/platform/automations/diff-view.png" />
</Frame>

### Invoking an Automation using the API

To run an automation by api call, grab the automation template id or the alias from the settings section of
the designer and invoke it by calling POST `api/automations/:template_id_here/invoke`. View
[Automations API docs](/api-reference/automations/invoke-an-automation) for
more details.

<Frame caption="Template ID Location, Settings Tab">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/template-id-location.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=8f76335a0228791cf3c92a03e9cb5ef9" alt="Template ID location, settings tab" width="2560" height="796" data-path="assets/platform/automations/template-id-location.png" />
</Frame>

### Invoking an Automation from the Designer

You can invoke the automation template directly from the designer in the **Invoke** tab. This can be a good way to test the automation or to invoke very simple automation templates.
*Note:* Invoking from the designer will pass an empty data payload `{}` to the automation run

<Frame caption="Template Invoke Tab">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/template-invoke.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=aaa89968437e36dd9ee51d33a4e639b9" alt="Template invoke tab" width="2862" height="992" data-path="assets/platform/automations/template-invoke.png" />
</Frame>

## Related Resources

<CardGroup cols={2}>
  <Card title="Steps Reference" href="/platform/automations/steps" icon="list">
    All automation action types
  </Card>

  <Card title="Debugger" href="/platform/automations/debugger" icon="bug">
    Test automations before production
  </Card>

  <Card title="Scheduling" href="/platform/automations/scheduling" icon="clock">
    Schedule automations with cron, recurrence, or one-time triggers
  </Card>

  <Card title="Automations API" href="/api-reference/automations/invoke-an-automation" icon="code">
    Invoke automations via API
  </Card>
</CardGroup>
