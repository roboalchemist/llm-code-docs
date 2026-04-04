# Source: https://pipedream.com/docs/workflows/event-history.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Event History

Monitor all workflow events and their stack traces in one centralized view under the [**Event History**](https://pipedream.com/event-history) section in the dashboard.

Within the **Event History**, you’ll be able to filter your events by workflow, execution status, within a specific time range.

<Warning>
  Workspace admins are able to view events for all workflows, but members are required to select a workflow since they might not have [access to certain projects](/projects/access-controls/#permissions).
</Warning>

## Filtering Events

The filters at the top of the screen allow you to search all events processed by your workflows.

You can filter by the event’s **Status**, **time of initiation** or by the **Workflow name**.

<Note>
  The filters are scoped to the current [workspace](/workspaces/). If you’re not seeing the events or workflow you’re expecting, try [switching workspaces](/workspaces/#switching-between-workspaces).
</Note>

### Filtering by status

* The **Status** filter controls which events are shown by their status
* For example selecting the **Success** status, you’ll see all workflow events that were successfully executed

<Frame>
  <img src="https://mintcdn.com/pipedream/xnRKrRxEtt3vxd6I/images/d3b5a53b-image.png?fit=max&auto=format&n=xnRKrRxEtt3vxd6I&q=85&s=3f5695a46b7a24d7fbcf8139b2d70056" width="640" height="549" data-path="images/d3b5a53b-image.png" />
</Frame>

#### All failed workflow executions

* You can view all failed workflow executions by applying the **Error** status filter
* This will only display the failed workflow executions in the selected time period
* This view in particular is helpful for identifying trends of errors, or workflows with persistent problems

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/045bb06a-image.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=bb31b0995253e547b0eab6dd32de2780" width="408" height="324" data-path="images/045bb06a-image.png" />
</Frame>

#### All paused workflow executions

* Workflow executions that are currently in a suspended state from `$.flow.delay` or `$.flow.suspend` will be shown when this filter is selected

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/08497233-image.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=c2a5d95436b862cd1f2fcbf250c1a667" width="381" height="302" data-path="images/08497233-image.png" />
</Frame>

<Note>
  If you’re using `setTimeout` or `sleep` in Node.js or Python steps, the event will not be considered **Paused**. Using those language native execution holding controls leaves your workflow in a **Executing** state.
</Note>

### Within a timeframe

* Filtering by time frame will include workflow events that *began* execution within the defined range
* Using this dropdown, you can select between convenient time ranges, or specify a custom range on the right side

<Frame>
  <img src="https://mintcdn.com/pipedream/anb6FA0wpd8jtdUB/images/518959a5-image.png?fit=max&auto=format&n=anb6FA0wpd8jtdUB&q=85&s=c329443aa8d663539a2ba69a21fa3b0e" width="922" height="794" data-path="images/518959a5-image.png" />
</Frame>

### Filtering by workflow

You can also filter events by a specific workflow. You can search by the workflow’s name in the search bar in the top right.

<Frame>
  <img src="https://mintcdn.com/pipedream/NF77kliJSewMqg65/images/224baa1d-CleanShot_2023-05-10_at_15.39.30_2x_yoa1k6.png?fit=max&auto=format&n=NF77kliJSewMqg65&q=85&s=8458a751a4ec5634375f7f74c2d21c7e" width="544" height="120" data-path="images/224baa1d-CleanShot_2023-05-10_at_15.39.30_2x_yoa1k6.png" />
</Frame>

Alternatively, you can filter by workflow from a specific event. First, open the menu on the far right, then select **Filter By Workflow**. Then only events processed by that workflow will appear.

<Frame>
  <img src="https://mintcdn.com/pipedream/h8oodpUDiyR1Ssvt/images/430a091d-CleanShot_2023-05-10_at_15.41.20_2x_ulvdns.png?fit=max&auto=format&n=h8oodpUDiyR1Ssvt&q=85&s=0c26b0142096492199a1a769405eeba2" width="576" height="96" data-path="images/430a091d-CleanShot_2023-05-10_at_15.41.20_2x_ulvdns.png" />
</Frame>

## Inspecting events

* Clicking on an individual event will open a panel that displays the steps executed, their individual configurations, as well as the overall performance and results of the entire workflow.
* The top of the event history details will display details including the overall status of that particular event execution and errors if any.
* If there is an error message, the link at the bottom of the error message will link to the corresponding workflow step that threw the error.
* From here you can easily **Build from event** or **Replay event**

<Frame>
  <img src="https://mintcdn.com/pipedream/Acz4Z1ch6TM7-aI8/images/a4077c02-CleanShot_2023-05-10_at_15.53.44_2x_t30gsb.png?fit=max&auto=format&n=Acz4Z1ch6TM7-aI8&q=85&s=7f4dc7763d9e2582fe4f37df4bfa2c8a" width="2592" height="1599" data-path="images/a4077c02-CleanShot_2023-05-10_at_15.53.44_2x_t30gsb.png" />
</Frame>

## Bulk actions

You can select multiple events and perform bulk actions on them.

* **Replay**: Replays the selected events. This is useful for example when you have multiple errored events that you want to execute again after fixing a bug in your workflow.
* **Delete**: Deletes the selected events. This may be useful if you have certain events you want to scrub from the event history, or when you’ve successfully replayed events that had originally errored.

<div className="relative pb-[calc(56.25%+41px)] h-0 w-full">
  <iframe
    src="https://demo.arcade.software/eLd2F3KJ1YFEj0ARi0Vq?embed"
    title="Bulk replay"
    loading="lazy"
    allowFullScreen
    allow="clipboard-write"
    className="absolute top-0 left-0 w-full h-full"
    style={{
    colorScheme: "light",
  }}
  />
</div>

<Note>
  When you replay multiple events at once, they’ll be replayed in the order they were originally executed. This means the first event that came in will be replayed first, followed by the second, and so on.
</Note>

## Limits

The number of events recorded and available for viewing in the Event History depends on your plan. [Please see the pricing page](https://pipedream.com/pricing) for more details.

## FAQ

### Is Event History available on all plans?

Yes, event history is available for all workspace plans, including free plans. However, the length of searchable or viewable history changes depending on your plan. [Please see the pricing page](https://pipedream.com/pricing) for more details.

Built with [Mintlify](https://mintlify.com).
