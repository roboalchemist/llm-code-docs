# Source: https://docs.firehydrant.com/docs/honeycomb-event-source.md

# Honeycomb Event Source

The Honeycomb Integration for Signals allows users to create events in FireHydrant from triggers in Honeycomb. Anytime Honeycomb sends an event to FireHydrant, FireHydrant checks to see if the event payload matches a rule set up by one of your teams. If there's a match, we’ll alert the team. Learn more about [Alert Rules](https://docs.firehydrant.com/docs/alert-rules)  here.

## Configuring Honeycomb Webhook

1. In FireHydrant, navigate to the Signals Sources page (Signals > Sources). Here, you’ll find a webhook URL you will use when creating a webhook in Honeycomb.

<Image alt="Copy the Datadog URL" align="center" width="800px" src="https://files.readme.io/875f2c4-honeycomb-webhook.jpg">
  Copy the Honeycomb URL
</Image>

2. In Honeycomb, navigate to the team settings page ([https://ui.honeycomb.io/teams](https://ui.honeycomb.io/teams)). Find the team to which you want to add the webhook and click on it. Click the Integrations tab for that team.
3. Click the “Add Integration” button towards the bottom of the page. Choose the “Webhook” option. Give the webhook a name that you can easily reference later on.
4. Add the webhook URL from FireHydrant that we copied in step one. Add a shared secret if desired (not required on the FireHydrant side).
5. Click “Add” to save your webhook.

### Adding Webhook to a Trigger

In Honeycomb, you can add a webhook as a notification recipient for a trigger.

1. Navigate to the Triggers list using the left sidebar. Find a trigger that you want to use to send Signals to FireHydrant. Click into the Trigger by clicking on the title.
2. At the bottom of the page, click “Add Recipient” to add your webhook. Select your Webhook in the Recipient dropdown in the modal and click “Add.”
3. Your trigger is now set up to create Signals in FireHydrant.

### Testing your Honeycomb Webhook

1. From the triggers list in Honeycomb, click the “Test” button.
2. Confirm that FireHydrant received your webhook by visiting **Alerting > Signals** Logs in the web app. You should see a new Signal created. You can open the drawer to see the full payload from Honeycomb.

## Field Mappings/Behaviors

The payload from Honeycomb will be directly mapped to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model). The following table explains the behavior once the payload hits our system:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Inbound Parameter
      </th>

      <th>
        FireHydrant Parameter
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `payload.id`
      </td>

      <td>
        `idempotency_key`
      </td>
    </tr>

    <tr>
      <td>
        `payload.name`
      </td>

      <td>
        `summary`
      </td>
    </tr>

    <tr>
      <td>
        `payload.description`
      </td>

      <td>
        `body`
      </td>
    </tr>

    <tr>
      <td>
        `payload.result_url`\
        `payload.slo_url`\
        `payload.sli_url`
      </td>

      <td>
        `links` - FireHydrant will add these three URL parameters to the `links` list
      </td>
    </tr>

    <tr>
      <td>
        `status`
      </td>

      <td>
        `status` - Open on FireHydrant if `triggered`, otherwise Closed
      </td>
    </tr>
  </tbody>
</Table>

These mappings mean that an inbound webhook from Grafana with the following content:

```json Honeycomb Payload
{
  "version": "v0.1.0",
  "name": "Sample Honeycomb Alert",
  "id": "IdlLjelDnWKh",
  "trigger_description": "",
  "status": "tRiGgErEd",
  "alert_type": "on_change",
  "summary": "",
  "description": "Validate Honeycomb Webhook Integration",
  "operator": "",
  "threshold": 0,
  "result_url": "https://honeycomb.io/sample/trigger",
  "slo_url": "https://ui.honeycomb.io/org-name/environments/env-name/datasets/dataset-name/slo/yo8JPUKErFE",
  "sli_url": "https://ui.honeycomb.io/org-name/environments/env-name/datasets/dataset-name/schema?dc=sli.delivery_latency.email",
  "result_groups": null,
  "result_groups_triggered": null,
  "trigger_url": "",
  "is_test": true
}
```

Will be transposed to the following FireHydrant Signal:

```json Transposed Signal
{
  "summary": "Sample Honeycomb Alert",
  "body": "Validate Honeycomb Webhook Integration",
  "links": [
    {
      "href": "https://honeycomb.io/sample/trigger",
      "text": "Honeycomb result"
    },
    {
      "href": "https://ui.honeycomb.io/org-name/environments/env-name/datasets/dataset-name/slo/yo8JPUKErFE",
      "text": "Honeycomb slo"
    },
    {
      "href": "https://ui.honeycomb.io/org-name/environments/env-name/datasets/dataset-name/schema?dc=sli.delivery_latency.email",
      "text": "Honeycomb sli"
    }
  ],
  "idempotency_key": "IdlLjelDnWKh",
  "status": 0
}
```