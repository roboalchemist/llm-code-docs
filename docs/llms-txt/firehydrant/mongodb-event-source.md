# Source: https://docs.firehydrant.com/docs/mongodb-event-source.md

# MongoDB Atlas Event Source

The MongoDB Atlas Event Source for Signals allows users to create events in FireHydrant from alerts sent from MongoDB Atlas. [Alert Rules](https://docs.firehydrant.com/docs/alert-rules) can be configured to scan the payload body of events and ensure the right teams are notified of events they care about.

## Basic Configuration

1. In FireHydrant, go to **Signals > Event Sources** and copy the ingest URL for MongoDB Atlas.
2. Follow [MongoDB's instructions](https://www.mongodb.com/docs/atlas/configure-alerts/) for setting up alerts. You'll want to select **Webhook** for **Add Notifier** and use the URL copied above as the **Webhook URL**.

## Field Mappings/Behaviors

The payload from MongoDB will be directly mapped to FireHydrant's [Events Data Model](https://docs.firehydrant.com/docs/events-data-model). The following table explains the behavior once the payload hits our system:

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
        `id`
      </td>

      <td>
        `idempotency_key`
      </td>
    </tr>

    <tr>
      <td>
        `eventTypeName`
      </td>

      <td>
        `summary`
      </td>
    </tr>

    <tr>
      <td>
        `processorErrorMsg`OR\
        `metricName` + `currentValue`
      </td>

      <td>
        `body` - FireHydrant will check to see if the alert from MongoDB Atlas has a `processorErrorMsg`. If not, it will default to printing information about the triggering metric and value in the following format:

        `metricName` current value is `currentValue.number` `currentValue.units`
      </td>
    </tr>

    <tr>
      <td>
        `status`
      </td>

      <td>
        `status` - Open when `status` is "OPEN" or "TRACKING" otherwise Closed
      </td>
    </tr>

    <tr>
      <td>
        `links`
      </td>

      <td>
        `links`
      </td>
    </tr>
  </tbody>
</Table>

These mappings mean that an inbound webhook from MongoDB with the following content:

```json MongoDB Atlas Payload
{
  "acknowledgedUntil": "2019-08-24T14:15:22Z",
  "acknowledgementComment": "Expiration on 3/19.  Silencing for 7days.",
  "acknowledgingUsername": "user@example.com",
  "alertConfigId": "32b6e34b3d91647abb20e7b8",
  "created": "2019-08-24T14:15:22Z",
  "eventTypeName": "HOST_DOWN",
  "groupId": "32b6e34b3d91647abb20e7b8",
  "id": "32b6e34b3d91647abb20e7b8",
  "instanceName": "foobar",
  "lastNotified": "2019-08-24T14:15:22Z",
  "links": [
    {
      "href": "https://cloud.mongodb.com/api/atlas",
      "rel": "self"
    }
  ],
  "orgId": "32b6e34b3d91647abb20e7b8",
  "processorErrorMsg": "MongoServerError: Failed to start stream processor: (Location77175) Could not connect to the Kafka topic with kafka error code: -195, message: Local: Broker transport failure.: (Location77175)",
  "processorName": "foobar",
  "processorState": "STARTED",
  "resolved": "2019-08-24T14:15:22Z",
  "status": "OPEN",
  "updated": "2019-08-24T14:15:22Z"
}
```

Will be transposed to the following FireHydrant Signal:

```json Transposed Signal
{
  "summary": "HOST_DOWN",
  "body": "MongoServerError: Failed to start stream processor: (Location77175) Could not connect to the Kafka topic with kafka error code: -195, message: Local: Broker transport failure.: (Location77175)",
  "links": [
    {
      "href": "https://cloud.mongodb.com/api/atlas"
    }
  ],
  "idempotency_key": "32b6e34b3d91647abb20e7b8",
  "status": 0
}
```