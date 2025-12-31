# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md.txt

The context in which an event occurred.

An EventContext describes: - The time an event occurred. - A unique identifier of the event. - The resource on which the event occurred, if applicable. - Authorization of the request that triggered the event, if applicable and available.

**Signature:**  

    export interface EventContext<Params = Record<string, string>> 

## Properties

|                                                          Property                                                          |                                                                                                 Type                                                                                                 |                                                          Description                                                           |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| [auth](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontextauth)           | { uid: string; token:[EventContextAuthToken](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontextauthtoken.md#eventcontextauthtoken_interface); rawToken?: string; } | Authentication information for the user that triggered the function.                                                           |
| [authType](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontextauthtype)   | "ADMIN" \| "USER" \| "UNAUTHENTICATED"                                                                                                                                                               | The level of permissions for a user.                                                                                           |
| [eventId](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontexteventid)     | string                                                                                                                                                                                               | The event's unique identifier.                                                                                                 |
| [eventType](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontexteventtype) | string                                                                                                                                                                                               | Type of event.                                                                                                                 |
| [params](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontextparams)       | Params                                                                                                                                                                                               | An object containing the values of the wildcards in the`path`parameter provided to the method for a Realtime Database trigger. |
| [resource](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontextresource)   | [Resource](https://firebase.google.com/docs/reference/functions/firebase-functions.resource.md#resource_interface)                                                                                   | The resource that emitted the event.                                                                                           |
| [timestamp](https://firebase.google.com/docs/reference/functions/firebase-functions.eventcontext.md#eventcontexttimestamp) | string                                                                                                                                                                                               | Timestamp for the event as an[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt)string.                                           |

## EventContext.auth

Authentication information for the user that triggered the function.

This object contains`uid`and`token`properties for authenticated users. For more detail including token keys, see the[security rules reference](https://firebase.google.com/docs/reference/rules/rules#properties).

This field is only populated for Realtime Database triggers and Callable functions. For an unauthenticated user, this field is null. For Firebase admin users and event types that do not provide user information, this field does not exist.

**Signature:**  

    auth?: {
            uid: string;
            token: EventContextAuthToken;
            rawToken?: string;
        };

## EventContext.authType

The level of permissions for a user.

Valid values are:

- `ADMIN`: Developer user or user authenticated via a service account.

- `USER`: Known user.

- `UNAUTHENTICATED`: Unauthenticated action

- `null`: For event types that do not provide user information (all except Realtime Database).

**Signature:**  

    authType?: "ADMIN" | "USER" | "UNAUTHENTICATED";

## EventContext.eventId

The event's unique identifier.

**Signature:**  

    eventId: string;

## EventContext.eventType

Type of event.

Possible values are:

- `google.analytics.event.log`

- `google.firebase.auth.user.create`

- `google.firebase.auth.user.delete`

- `google.firebase.database.ref.write`

- `google.firebase.database.ref.create`

- `google.firebase.database.ref.update`

- `google.firebase.database.ref.delete`

- `google.firestore.document.write`

- `google.firestore.document.create`

- `google.firestore.document.update`

- `google.firestore.document.delete`

- `google.pubsub.topic.publish`

- `google.firebase.remoteconfig.update`

- `google.storage.object.finalize`

- `google.storage.object.archive`

- `google.storage.object.delete`

- `google.storage.object.metadataUpdate`

- `google.testing.testMatrix.complete`

**Signature:**  

    eventType: string;

## EventContext.params

An object containing the values of the wildcards in the`path`parameter provided to the method for a Realtime Database trigger.

**Signature:**  

    params: Params;

## EventContext.resource

The resource that emitted the event.

Valid values are:

Analytics:`projects/<projectId>/events/<analyticsEventType>`

Realtime Database:`projects/_/instances/<databaseInstance>/refs/<databasePath>`

Storage:`projects/_/buckets/<bucketName>/objects/<fileName>#<generation>`

Authentication:`projects/<projectId>`

Pub/Sub:`projects/<projectId>/topics/<topicName>`

Because Realtime Database instances and Cloud Storage buckets are globally unique and not tied to the project, their resources start with`projects/_`. Underscore is not a valid project name.

**Signature:**  

    resource: Resource;

## EventContext.timestamp

Timestamp for the event as an[RFC 3339](https://www.ietf.org/rfc/rfc3339.txt)string.

**Signature:**  

    timestamp: string;