# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message.md.txt

# pubsub.Message class

Interface representing a Google Cloud Pub/Sub message.

**Signature:**

    export declare class Message 

## Constructors

| Constructor | Modifiers | Description |
|---|---|---|
| [(constructor)(data)](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message.md#pubsubmessageconstructor) |   | Constructs a new instance of the `Message` class |

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [attributes](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message.md#pubsubmessageattributes) |   | { \[key: string\]: string; } | User-defined attributes published with the message, if any. |
| [data](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message.md#pubsubmessagedata) |   | string | The data payload of this message object as a base64-encoded string. |
| [json](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message.md#pubsubmessagejson) |   | any | The JSON data payload of this message object, if any. |

## Methods

| Method | Modifiers | Description |
|---|---|---|
| [toJSON()](https://firebase.google.com/docs/reference/functions/firebase-functions.pubsub.message.md#pubsubmessagetojson) |   | Returns a JSON-serializable representation of this object. |

## pubsub.Message.(constructor)

Constructs a new instance of the `Message` class

**Signature:**

    constructor(data: any);

### Parameters

| Parameter | Type | Description |
|---|---|---|
| data | any |   |

## pubsub.Message.attributes

User-defined attributes published with the message, if any.

**Signature:**

    readonly attributes: {
            [key: string]: string;
        };

## pubsub.Message.data

The data payload of this message object as a base64-encoded string.

**Signature:**

    readonly data: string;

## pubsub.Message.json

The JSON data payload of this message object, if any.

**Signature:**

    get json(): any;

## pubsub.Message.toJSON()

Returns a JSON-serializable representation of this object.

**Signature:**

    toJSON(): any;

**Returns:**

any

A JSON-serializable representation of this object.