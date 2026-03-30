# Source: https://docs.firehydrant.com/docs/command-extensions.md

# Command Extensions

> 📘 Note:
>
> Command Extensions are currently only available for Slack.

Command extensions allow your team to add custom functionality to the FireHydrant Slack bot. These custom commands can return templated text or hook into our webhooks to make requests to external systems.

This section provides information on how to use these extensions once they've been set up.

## Prerequisites

* You must [have Slack configured](https://docs.firehydrant.com/docs/slack-integration).
* If you want the command extension to execute API requests, you must [set up a webhook](https://docs.firehydrant.com/docs/webhooks).
* Otherwise, if you only want the custom command to return a templated reply with information, there are no prerequisites.

## Setup

<Image alt="Command Extensions under Slack integration settings" align="center" width="650px" src="https://files.readme.io/0dbc293-image.png">
  Command Extensions under Slack integration settings
</Image>

1. Go to [your integrations page](https://app.firehydrant.io/organizations/integrations), search for the Slack tile, then click the edit pencil.
2. Click on the **Command Extensions** tab then **+ Add command extension**.
3. On this page, you can configure the required fields for your command extension:

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Examples
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Command Name
      </td>

      <td>
        The name of your command. It should only contain alphanumeric, dashes, or underscores. For example, `my-example-command`.
      </td>
    </tr>

    <tr>
      <td>
        Help Description
      </td>

      <td>
        A description to help users understand what this command extension does.
      </td>
    </tr>

    <tr>
      <td>
        Command Type
      </td>

      <td>
        One of `Reply`, `Webhook`
      </td>
    </tr>

    <tr>
      <td>
        Reply Template\
        (Reply only)
      </td>

      <td>
        The templated output to return for Reply-type command extensions. This field supports both [Template Variables](https://docs.firehydrant.com/docs/template-variables) as well as Slack's specialized [mrkdwn](https://api.slack.com/reference/surfaces/formatting) language.
      </td>
    </tr>

    <tr>
      <td>
        Webhook\
        (Webhook only)
      </td>

      <td>
        Which Webhook this command extension should call for Webhook-type command extensions. Select the Webhook you configured previously.
      </td>
    </tr>

    <tr>
      <td>
        Webhook Payload
      </td>

      <td>
        The request payload to send to the Webhook. This field supports [Template Variables](https://docs.firehydrant.com/docs/template-variables), making all of the incident's data available to use in the body.
      </td>
    </tr>
  </tbody>
</Table>

Once you've configured the command extension, click "Add command" to finalize it.

## Usage

<Image alt="Example execution of a custom command extension + webhook" align="center" width="650px" src="https://files.readme.io/0daa10b-slack-webhook-example.gif">
  Example execution of a custom command extension + webhook
</Image>

To execute your command extension, just run it in your incident channel in Slack:

```julia Command Format
/fh <command-name> <arg1> <arg2> ...
```

* `/fh` is the prefix that invokes the FireHydrant bot. Note that it's the shortest alias, but you can also use `/firehydrant` and `/incident`.
* `<command-name>` is the name of the command extension that you created.
* `<arg1>` `<arg2>` ... are any arguments that your command extension requires.

For instance, if you have a command extension named `restart-deployment`, you could use it to restart an nginx deployment in a default namespace using the following command:

```julia Example Command
/fh restart-deployment default nginx-deployment
```

## Handling Webhook Payloads

When using the webhook with command extensions, your external system will receive a payload that looks like this:

```json Webhook Payload
{
  "data": {
    "callback": {
      "expiration": "2023-07-24T23:29:34Z",
      "url": "https://app.firehydrant.io/integrations/slack/webhooks/eyJhbGNiJ9.eyJpc3MiOeHRlb4LWRiYjYtNDg0Yi1hMWVmLTRlYzgwNzVmZDBjOCIsImV4cCI6MTY5MDI0MTM3NH0.GVXKsHeYhVTg7kzT5Xnba46L-GWhE"
    },
    "command_arguments": [
      "default",
      "nginx-deployment"
    ],
    "command_extension": {
      "description": "Description",
      "id": "7d5fc662-572c-45c4-bbd1-17e23830fe39",
      "name": "restart-deployment"
    },
    "firehydrant_user": {
      "email": "bobby+dalmatians@firehydrant.io",
      "id": "2af3339f-9d81-434b-a208-427d6d85c124",
      "name": "Robert Ross",
      "source": "firehydrant_user"
    },
    "payload": {},
    "payload_type": "json"
  },
  "event": {
    "operation": "CREATED",
    "resource_type": "command_extension"
  }
}
```

Note that the actual payload you configured for your webhook is located at `data.payload`. The rest of this data is provided as information so you can use it in the service receiving these webhooks.

### Responding to Webhook Callbacks

The callback URL is a unique URL that you can use to reply with incident notes on your timeline. This is useful to reply with asynchronous tasks that your operation is running.

For example, you can add notes back to your incident with:

```Text Example Callback
POST /integrations/slack/webhooks/eyJhbGNiJ9.eyJpc3MiOeHRlb4LWRiYjYtNDg0Yi1hMWVmLTRlYzgwNzVmZDBjOCIsImV4cCI6MTY5MDI0MTM3NH0.GVXKsHeYhVTg7kzT5Xnba46L-GWhE HTTP/1.1
Host: app.firehydrant.io
Content-Type: application/json
Content-Length: 120

{
  "reply_type": "actions",
  "actions": [
    {
      "action": "new_note",
      "body": "Deployment has successfully restarted"
    }
  ]
}
```