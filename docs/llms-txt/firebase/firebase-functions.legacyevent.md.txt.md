# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.legacyevent.md.txt

# LegacyEvent interface

Wire format for an event.

**Signature:**

    export interface LegacyEvent 

## Properties

| Property | Type | Description |
|---|---|---|
| [context](https://firebase.google.com/docs/reference/functions/firebase-functions.legacyevent.md#legacyeventcontext) | { eventId: string; timestamp: string; eventType: string; resource: [Resource](https://firebase.google.com/docs/reference/functions/firebase-functions.resource.md#resource_interface); domain?: string; auth?: { variable?: { uid?: string; token?: string; }; admin: boolean; }; } | Wire format for an event context. |
| [data](https://firebase.google.com/docs/reference/functions/firebase-functions.legacyevent.md#legacyeventdata) | any | Event data over wire. |

## LegacyEvent.context

Wire format for an event context.

**Signature:**

    context: {
            eventId: string;
            timestamp: string;
            eventType: string;
            resource: Resource;
            domain?: string;
            auth?: {
                variable?: {
                    uid?: string;
                    token?: string;
                };
                admin: boolean;
            };
        };

## LegacyEvent.data

Event data over wire.

**Signature:**

    data: any;