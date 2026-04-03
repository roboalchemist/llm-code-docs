# Source: https://firebase.google.com/docs/reference/functions/test/test.pubsub.md.txt

# Namespace: pubsub

# [test](https://firebase.google.com/docs/reference/functions/test/test).pubsub

namespace static

Namespace for testing Pubsub functions using the Cloud Functions for Firebase Test SDK.

## Methods

### exampleMessage

static

exampleMessage() returns functions.pubsub.Message

Fetch an example Message already populated with data.

Returns

:   `non-null functions.pubsub.Message`

### makeMessage

static

makeMessage(encodedString, attributes) returns functions.pubsub.Message

Function to create a Pubsub event for a message with data payload in the form of a base64-encoded string.

|                                       #### Parameter                                        ||
|---------------|------------------------------------------------------------------------------|
| encodedString | string Base64-encoded string for the content of a `pubsubMessage`.           |
| attributes    | Optional Object Attributes of `pubsubMessage` to specify. Value may be null. |

Returns

:   `non-null functions.pubsub.Message`

### makeMessage

static

makeMessage(json, attributes) returns functions.pubsub.Message

Function to create a Pubsub event for a message with JSON payload.

|                                      #### Parameter                                      ||
|------------|------------------------------------------------------------------------------|
| json       | Object Content of `pubsubMessage` as a JSON payload. Value must not be null. |
| attributes | Optional Object Attributes of `pubsubMessage` to specify. Value may be null. |

Returns

:   `non-null functions.pubsub.Message`