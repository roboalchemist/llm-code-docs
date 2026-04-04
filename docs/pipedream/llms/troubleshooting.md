# Source: https://pipedream.com/docs/troubleshooting.md

# Source: https://pipedream.com/docs/connect/managed-auth/troubleshooting.md

# Source: https://pipedream.com/docs/connect/components/troubleshooting.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting

Common issues and solutions when working with Pipedream Connect components.

## Referencing the app prop in configured props payload

If you encounter an error like `Cannot read properties of undefined (reading 'oauth_access_token')`, it's likely related to an incorrect reference to the app prop in your configuredProps payload.

For example, using `google_sheets` instead of `googleSheets`, or `stripe` instead of `app`. Always use the exact app prop name as returned by the component definition.

The app prop name can be found in the component's definition under `configurable_props`:

```javascript  theme={null}
"configurable_props": [
  {
    "name": "googleSheets", // Use this exact name in your payload
    "type": "app",
    "app": "google_sheets"
  },
  ...
]
```

## Passing dynamic props ID

When working with components that use dynamic props, you must track and pass the `dynamicPropsId` in your API calls. After calling the API to reload props as described in the [Configure dynamic props](/connect/components/actions/#configure-dynamic-props) section, you'll receive a response containing a `dynamicProps.id` value that looks like `dyp_6xUyVgQ`.

This ID must be included in subsequent API calls to `runAction` or `deployTrigger`. Failing to include it can result in errors like:

```json  theme={null}
{
  "name": "Error",
  "message": "undefined is not an array or an array-like"
}
```

or

```json  theme={null}
{
  "title": "TypeError",
  "detail": "Cannot read properties of undefined (reading 'endpoint')"
}
```

For example, after receiving the dynamic props ID from the reload props call, include it in your action execution:

```js  theme={null}
// First, reload props for a component with dynamic props
const { dynamicProps } = await client.reloadProps({ … });
 
// Then use the dynamicProps.id when running the action
const resp = await client.runAction({
  externalUserId: "abc-123",
  actionId: "google_sheets-add-single-row",
  dynamicPropsId: dynamicProps.id, // Must include this
  configuredProps: {
    googleSheets: {
      authProvisionId: account.id,
    },
    sheetId: "1BfWjFF2dTW_YDiLISj5N9nKCUErShgugPS434liyytg",
    worksheetId: "Sheet1",
    // ... other configured props
  }
});
```

Remember to maintain this ID in your application state while the user is configuring the component, and include it in all subsequent API calls related to that particular configuration.

## Checking source logs for deployed triggers

If a deployed trigger isn't emitting events as expected, you can examine the source logs to get a better sense of what's happening.

Use the following URL to access logs and view emitted events:

```html  theme={null}
https://pipedream.com/sources/{dcid}
```

Replace `{dcid}` with your deployed component ID (e.g., `dc_dAuGmW7`).

The sources UI contains three tabs:

* **Events**: Lists emitted events from the deployed trigger that will be sent to the subscribed webhook or workflow. This helps you verify that events are being properly processed and understand their structure.

* **Logs**: Displays execution history for the trigger. For polling sources, this shows each time the trigger checks for updates. For webhook-based instant sources, it shows each time the source receives an event from the upstream API. This tab is especially useful for troubleshooting when events aren't being emitted as expected.

* **Configuration**: Provides a read-only view of the deployed source's code and configuration. While you can't modify settings for deployed triggers that belong to external users here, this tab offers insight into how the trigger is configured.

<Note>
  This UI view is currently in beta and has some limitations. Some UI elements may appear unpolished, and the configuration tab has limited functionality.
</Note>

Built with [Mintlify](https://mintlify.com).
