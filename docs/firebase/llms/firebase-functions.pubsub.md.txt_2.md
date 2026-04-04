# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.md.txt

# pubsub namespace

## Functions

| Function | Description |
|---|---|
| [schedule(schedule)](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.md#pubsubschedule) | Registers a Cloud Function to run at specified times. |
| [topic(topic)](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.md#pubsubtopic) | Registers a Cloud Function triggered when a Google Cloud Pub/Sub message is sent to a specified topic. |

## Classes

| Class | Description |
|---|---|
| [Message](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message.md#pubsubmessage_class) | Interface representing a Google Cloud Pub/Sub message. |
| [ScheduleBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md#pubsubschedulebuilder_class) | The builder for scheduled functions, which are powered by Google Pub/Sub and Cloud Scheduler. Describes the Cloud Scheduler job that is deployed to trigger a scheduled function at the provided frequency. For more information, see \[Schedule functions\](/docs/functions/schedule-functions).Access via `functions.pubsub.schedule()`. |
| [TopicBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.topicbuilder.md#pubsubtopicbuilder_class) | The Google Cloud Pub/Sub topic builder.Access via `functions.pubsub.topic()`. |

## pubsub.schedule()

Registers a Cloud Function to run at specified times.

**Signature:**

    export declare function schedule(schedule: string): ScheduleBuilder;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| schedule | string | The schedule, in Unix Crontab or AppEngine syntax. |

**Returns:**

[ScheduleBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.schedulebuilder.md#pubsubschedulebuilder_class)

ScheduleBuilder interface.

## pubsub.topic()

Registers a Cloud Function triggered when a Google Cloud Pub/Sub message is sent to a specified topic.

**Signature:**

    export declare function topic(topic: string): TopicBuilder;

### Parameters

| Parameter | Type | Description |
|---|---|---|
| topic | string | The Pub/Sub topic to watch for message events. |

**Returns:**

[TopicBuilder](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.topicbuilder.md#pubsubtopicbuilder_class)

Pub/Sub topic builder interface.