# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.event.md.txt

# Event interface

Wire format for an event.

**Signature:**  

    export interface Event 

## Properties

|                                                 Property                                                 |                                                                                                                                        Type                                                                                                                                         |            Description            |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| [context](https://firebase.google.com/docs/reference/functions/firebase-functions.event.md#eventcontext) | { eventId: string; timestamp: string; eventType: string; resource: [Resource](https://firebase.google.com/docs/reference/functions/firebase-functions.resource.md#resource_interface); domain?: string; auth?: { variable?: { uid?: string; token?: string; }; admin: boolean; }; } | Wire format for an event context. |
| [data](https://firebase.google.com/docs/reference/functions/firebase-functions.event.md#eventdata)       | any                                                                                                                                                                                                                                                                                 | Event data over wire.             |

## Event.context

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

## Event.data

Event data over wire.

**Signature:**  

    data: any;