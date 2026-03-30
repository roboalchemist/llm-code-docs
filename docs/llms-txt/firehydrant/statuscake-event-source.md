# Source: https://docs.firehydrant.com/docs/statuscake-event-source.md

# StatusCake Event Source

The StatusCake Event Source for Signals allows users to create events in FireHydrant from uptime monitors in StatusCake. Anytime that StatusCake sends a webhook event to FireHydrant, we’ll evaluate the event payload to see if it matches a rule set up by one of your teams. Learn more about [Alert Rules](https://docs.firehydrant.com/docs/signals-alert-rules) here.

## Configuring StatusCake Webhook

1. In FireHydrant, navigate to the [Event Sources](https://app.firehydrant.io/signals/sources/integrations) page. Here, copy the ingest URL for StatusCake.

   <Image align="center" src="https://files.readme.io/c2b4609-statuscake-webhook.jpg" />
2. In StatusCake, navigate to Alerting > Contact Groups. Click the "New Contact Group" button to create a new contact group.
3. Scroll down to the Webhook URL, and add the url you copied in step 1. Set the Webhook Method to `POST`
4. To add this webhook to any monitor, navigate to Monitors > All Monitors and select a monitor you want to connect to FireHydrant.
5. Click Edit on the Monitor and scroll to the Contact Groups. Add the contact group that you created in step 2. Click Save Now.

You can learn more about StatusCake webhooks by reading [their Webhooks documentation](https://www.statuscake.com/kb/knowledge-base/how-to-use-the-web-hook-url/).

## Field Mappings

The following StatusCake webhook parameters are transposed to FireHydrant's Signals [Events Data Model](https://docs.firehydrant.com/docs/events-data-model):

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        StatusCake Parameter
      </th>

      <th>
        Signal Parameter(s)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `URL`
      </td>

      <td>
        `idempotency_key`\
        `body`
      </td>
    </tr>

    <tr>
      <td>
        `Name`
      </td>

      <td>
        `summary`
      </td>
    </tr>

    <tr>
      <td>
        `Status`
      </td>

      <td>
        `status` - Closed on FireHydrant when Up or UP on StatusCake, otherwise Open\
        `annotations['Status']`
      </td>
    </tr>

    <tr>
      <td>
        `CheckRate`\
        `ContactGroup`\
        `IP`\
        `StatusCode`
      </td>

      <td>
        `annotations['CheckRate']`\
        `annotations['ContactGroup']`\
        `annotations['IP']`\
        `annotations['StatusCode']`
      </td>
    </tr>
  </tbody>
</Table>

Subsequently, the following webhook from StatusCake:

```json StatusCake Payload
{
  "Name": "My Website",
  "Status": "UP",
  "StatusCode": 200,
  "URL": "https://www.example.com",
  "IP": "1.2.3.4",
  "CheckRate": 300,
  "ContactGroup": "12345"
}
```

...will be transposed to the following Signal in FireHydrant:

```json Transposed Signal
{
  "idempotency_key": "https://www.example.com",
  "summary": "My Website",
  "body": "https://www.example.com",
  "status": "CLOSED",
  "annotations": {
    "CheckRate": "300",
    "ContactGroup": "12345",
    "IP": "1.2.3.4",
    "StatusCode": "200",
    "Status": "UP"
  }
}
```