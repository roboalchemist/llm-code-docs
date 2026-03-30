# Source: https://docs.firehydrant.com/docs/alertmanager-event-source.md

# Alertmanager Event Source

The Alertmanager Integration for Signals allows users to create events in FireHydrant from alerts in Alertmanager. Anytime Alertmanager sends an event to FireHydrant, we evaluate the event payload to see if it matches any rules configured by one of your teams. If there's a match, we’ll alert the team. Learn more about [Alert Rules](https://docs.firehydrant.com/docs/alert-rules)  here.

### Configuring an Alertmanager Webhook

1. In FireHydrant, navigate to the Signals Sources page (Signals > Sources). Here, you’ll find a webhook URL you will use when creating a webhook in Alertmanager.

<Image alt="Copy the Alertmanager URL" align="center" width="800px" src="https://files.readme.io/c3e41ba-alertmanager-webhook.jpg">
  Copy the Alertmanager URL
</Image>

2. In your Alertmanager config YAML file, add a webhook receiver for FireHydrant and use the URL from the previous step as the webhook config URL:

```yaml
  receivers: 
      - name: 'firehydrant-signals-webhook'
        webhook_configs: 
          - url: https://signals.firehydrant.com/v1/transpose/alertmanager/{webhook_key}
```

3. In any of your routes, you can now add your named receiver as part of the route. For example:

```yaml
  route:
    receiver: firehydrant-signals-webhook
```

4. After creating alerts that match your routes, confirm that FireHydrant received your webhook by visiting Alerting > Webhook Logs in the web app. You should see a new Signal created. You can open the drawer to see the full payload from Alertmanager.

## Field Mappings

FireHydrant's Alertmanager transposer will map the following fields to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model).

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Alertmanager Parameter
      </th>

      <th>
        FireHydrant Parameter
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **md5(**`payload.groupKey`**)**
      </td>

      <td>
        `idempotency_key` - Specifically FireHydrant uses an MD5 hash of the `groupKey` parameter as the idempotency key
      </td>
    </tr>

    <tr>
      <td>
        `payload.alerts[0].annotations.summary`\
        *-OR-*\
        `payload.receiver`
      </td>

      <td>
        `summary` - FireHydrant will check if there is a summary in the annotation of the first alert, otherwise we use the receiver name
      </td>
    </tr>

    <tr>
      <td>
        `payload.alerts[0].annotations.description`
      </td>

      <td>
        `body` - FireHydrant will check to see if there is a description in the annotation of the first alert, otherwise the description will be empty
      </td>
    </tr>

    <tr>
      <td>
        `payload.status`
      </td>

      <td>
        `status` - Open when `status` is "firing", otherwise Closed
      </td>
    </tr>

    <tr>
      <td>
        `payload.alerts[0].generatorURL`\
        *-OR-*\
        `payload.externalURL`
      </td>

      <td>
        `links` - FireHydrant will check if there is a `generatorURL` parameter in the first alert, otherwise we will use the `externalURL` parameter
      </td>
    </tr>

    <tr>
      <td>
        `payload.groupKey`
      </td>

      <td>
        `annotations['alertmanager/groupKey']`
      </td>
    </tr>

    <tr>
      <td>
        `payload.commonAnnotations`
      </td>

      <td>
        `annotations['alertmanager/annotations-*']` - FireHydrant will take all the `commonAnnotations` and prepend `alertmanager/annotations-` to their keys before inserting them into the `annotations` object
      </td>
    </tr>

    <tr>
      <td>
        `payload.commonLabels`
      </td>

      <td>
        `annotations['alertmanager/labels-*']` - FireHydrant will take all the `commonLabels` and prepend `alertmanager/labels-` to their keys before inserting them into the `annotations` field
      </td>
    </tr>

    <tr>
      <td>
        `payload.groupLabels`
      </td>

      <td>
        `annotations['alertmanager/grouped-by-*']` - FireHydrant will take all the `groupLabels` and prepend `alertmanager/grouped-by-` to their keys before inserting them into the `annotations` field
      </td>
    </tr>
  </tbody>
</Table>

These mappings mean that an inbound webhook from Alertmanager with the following content

```json Alertmanager Payload
{
  "version": "4",
  "groupKey": "123456789",
  "truncatedAlerts": 0,
  "status": "firing",
  "receiver": "Receiver String",
  "groupLabels": {
    "groupLabel1": "value1",
    "groupLabel2": "value2"
  },
  "commonLabels": {
    "commonLabel1": "value1",
    "commonLabel2": "value2"
  },
  "commonAnnotations": {
    "commonAnnotation1": "value1",
    "commonAnnotation2": "value2"
  },
  "externalURL": "https://test-alermanager.io",
  "alerts": [
    {
      "status": "firing",
      "labels": {
        "label1": "value1",
        "label2": "value2"
      },
      "annotations": {
        "summary": "This is a test alertmanager alert",
        "description": "This is a longer description of a test alertmanager alert",
        "annotation1": "value1",
        "annotation2": "value2"
      },
      "startsAt": "2023-12-18T07:20:50.52Z",
      "endsAt": "2023-12-18T07:20:50.52Z",
      "generatorURL": "https://test-alermanager.io/generator",
      "fingerprint": "28295wtbgwyrgb8731"
    }
  ]
}
```

...will result in the following mapped Signal on FireHydrant:

```json Transposed Signal
{
  "summary": "This is a test alertmanager alert",
  "body": "This is a longer description of a test alertmanager alert",
  "links": [
    {
      "href": "https://test-alermanager.io/generator",
      "text": "Alertmanager Generator"
    }
  ],
  "idempotency_key": "25f9e794323b453885f5181f1b624d0b",
  "annotations": {
    "alertmanager/annotations-commonAnnotation1": "value1",
    "alertmanager/annotations-commonAnnotation2": "value2",
    "alertmanager/groupKey": "123456789",
    "alertmanager/grouped-by-groupLabel1": "value1",
    "alertmanager/grouped-by-groupLabel2": "value2",
    "alertmanager/labels-commonLabel1": "value1",
    "alertmanager/labels-commonLabel2": "value2"
  },
  "status": 0
}
```