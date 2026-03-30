# Source: https://www.courier.com/docs/platform/automations/cancel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancelling An Automation

> Courier Automations can be cancelled using a dynamic cancellation token. Add the token in settings, then invoke a separate automation with a “Cancel Automation” node referencing the same token.

## Add a Cancellation Token

To allow an automation to be cancelled, add a cancellation token to the automation.

1. Navigate to the settings tab of the automation you want to cancel.
2. Add a cancellation token. This can be any value desired. Its best to use a dynamic value so
   a specific automation invocation may be cancelled, rather than all running instances. For
   example, you may use `refs.data.userId`, which would allow the automation run to be associated
   with the user the automation would send to.
3. Publish the Automation.
4. Create a new automation
5. Add the `Cancel Automation` node
6. Set the token to the same token from step 2.
7. Publish

## Canceling From the UI

An automation can also be canceled from automation logs.

1. Navigate to the [automation logs page](https://app.courier.com/logs/automations) in Courier.
2. Find your automation in the logs, you can search with a run Id or source.
3. If your automation has not finished processing, a cancel button will be shown in the run summary.
4. Clicking this button will cancel your automation.

<Frame caption="Canceling an Automation from Logs">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/cancel-button-logs.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=32e466e1fd4e839a789f636e05a61107" alt="Canceling an automation from logs" width="2880" height="1368" data-path="assets/platform/automations/cancel-button-logs.png" />
</Frame>

## Canceling Multiple Automations

When multiple automations share the same cancellation token and a cancel automation is invoked, all automations that have the same token will be simultaneously canceled.

## Templated Cancellation Token

It may be advantageous to create a compound key for your cancellation token. For example, if you want to have a cancellation token that combines two different fields, or a data field and a static string. In automations, most fields support Javascript string interpolation and the cancellation token is an example of one. The documentation above says you can use `refs`, for example `refs.data.userId` and the following would be identical in the cancellation token field, `${data.userId}`. For more advanced interpolation you can perform nested interpolations as well.

**Static Fields**

```javascript  theme={null}
${`onboarding-flow-${data.userId}`}
```

**Combining Fields**

```javascript  theme={null}
${`${data.userId}-${data.tenantId}`}
```
