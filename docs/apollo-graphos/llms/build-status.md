# Source: https://www.apollographql.com/docs/graphos/platform/insights/notifications/build-status.md

# Build Status Notifications

Configure GraphOS to send notifications to a webhook whenever GraphOS attempts to build a new supergraph schema for your federated graph.
Notifications indicate whether the build succeeded. Successful build notifications include a temporary URL to the new supergraph schema.

## Setup

## Configure webhook

Custom webhooks require you to set up an HTTPS endpoint accessible via
the public internet. GraphOS sends webhook notifications to this
endpoint as `POST` requests. Notification details are
provided as JSON in the request body, as described in the next section.

1. Specify a name for this notification channel in the **Channel Name** field. This name must be unique among
   all your graph's notification channels, including Slack channels.

2. In the **Webhook URL** input, provide the URL of your HTTP(S) endpoint.

3. Click **Next** and complete any remaining steps in the dialog.

### Webhook format

Custom webhook notification details are provided as a JSON object in the request body.

The JSON object conforms to the structure of the `ResponseShape` interface:

```javascript
interface BuildError {
  message: string;
  locations: ReadonlyArray<Location>;
}

interface Location {
  line: number;
  column: number;
}

interface ResponseShape {
  eventType: 'BUILD_PUBLISH_EVENT';
  eventID: string;
  supergraphSchemaURL: string | undefined;
  buildSucceeded: boolean;
  buildErrors: BuildError[] | undefined;
  graphID: string;
  variantID: string;
  timestamp: string;
}
```

#### Field descriptions

Field
Description

##### `eventType`

The build status event name; currently, always `BUILD_PUBLISH_EVENT`

##### `eventId`

A unique event ID

##### `supergraphSchemaURL`

If the build succeeded, a short-lived (24-hour) URL that enables you to fetch the supergraph
schema without authenticating (such as with an API key).

If the build fails, this field isn't present.

##### `buildSucceeded`

Whether or not the build succeeded

##### `buildErrors`

If the build failed, an array of `builderError` objects that describe the errors that occurred during the build.

If the build succeeded, this field isn't present.

##### `graphID`

A unique graph ID

##### `variantID`

An unique ID in the graph ref format `graphID@variantName`

##### `timestamp`

An ISO 8601 Date string indicating when the event occurred
