# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md.txt

# EventHandlerOptions interface

Additional fields that can be set on any event-handling function.

**Signature:**  

    export interface EventHandlerOptions extends Omit<GlobalOptions, "enforceAppCheck"> 

**Extends:** Omit\<[GlobalOptions](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.globaloptions.md#globaloptions_interface), "enforceAppCheck"\>

## Properties

|                                                                                     Property                                                                                      |                                                                                         Type                                                                                         |                                                                                                                                           Description                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [channel](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptionschannel)                                 | string                                                                                                                                                                               | The name of the channel where the function receives events.                                                                                                                                                                                                                                     |
| [eventFilterPathPatterns](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptionseventfilterpathpatterns) | Record\<string, string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\>\> | Filters events based on path pattern matching on the CloudEvents attributes.Similar to eventFilters, but supports wildcard patterns for flexible matching where *matches any single path segment,* `*` matches zero or more path segments, and `{param}` captures a path segment as a parameter |
| [eventFilters](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptionseventfilters)                       | Record\<string, string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\>\> | Filters events based on exact matches on the CloudEvents attributes.Each key-value pair represents an attribute name and its required value for exact matching. Events must match all specified filters to trigger the function.                                                                |
| [eventType](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptionseventtype)                             | string                                                                                                                                                                               | Type of the event.                                                                                                                                                                                                                                                                              |
| [region](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptionsregion)                                   | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue     | Region of the EventArc trigger.                                                                                                                                                                                                                                                                 |
| [retry](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptionsretry)                                     | boolean \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<boolean\> \| ResetValue   | Whether failed executions should be delivered again.                                                                                                                                                                                                                                            |
| [serviceAccount](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.eventhandleroptions.md#eventhandleroptionsserviceaccount)                   | string \| [Expression](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md#paramsexpression_class)\<string\> \| ResetValue     | The service account that EventArc should use to invoke this function. Requires the P4SA to have ActAs permission on this service account.                                                                                                                                                       |

## EventHandlerOptions.channel

The name of the channel where the function receives events.

**Signature:**  

    channel?: string;

## EventHandlerOptions.eventFilterPathPatterns

Filters events based on path pattern matching on the CloudEvents attributes.

Similar to eventFilters, but supports wildcard patterns for flexible matching where `*` matches any single path segment, `**` matches zero or more path segments, and `{param}` captures a path segment as a parameter

**Signature:**  

    eventFilterPathPatterns?: Record<string, string | Expression<string>>;

## EventHandlerOptions.eventFilters

Filters events based on exact matches on the CloudEvents attributes.

Each key-value pair represents an attribute name and its required value for exact matching. Events must match all specified filters to trigger the function.

**Signature:**  

    eventFilters?: Record<string, string | Expression<string>>;

## EventHandlerOptions.eventType

Type of the event.

**Signature:**  

    eventType?: string;

## EventHandlerOptions.region

Region of the EventArc trigger.

**Signature:**  

    region?: string | Expression<string> | ResetValue;

## EventHandlerOptions.retry

Whether failed executions should be delivered again.

**Signature:**  

    retry?: boolean | Expression<boolean> | ResetValue;

## EventHandlerOptions.serviceAccount

The service account that EventArc should use to invoke this function. Requires the P4SA to have ActAs permission on this service account.

**Signature:**  

    serviceAccount?: string | Expression<string> | ResetValue;