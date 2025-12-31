# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/python/firebase_functions.core.md.txt

# firebase_functions.core module

Public code that is shared across modules.

## Classes

|                                                                            ### Change *class* firebase_functions.core.Change(*before: T* , *after: T* )                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: Generic\[T\] The Cloud Functions interface for events that change state, such as Realtime Database on_value_written. after*: T* :   The state of data after the change. before*: T* :   The state of data before the change. |

|                                                                                                                                                                                                                      ### CloudEvent *class* firebase_functions.core.CloudEvent(*specversion: str* , *id: str* , *source: str* , *type: str* , *time: datetime* , *data: T* , *subject: str \| None* )                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bases: Generic\[T\] A CloudEvent is the base of a cross-platform format for encoding a serverless event. More information can be found at <https://github.com/cloudevents/spec>. data*: T* :   Information about this specific event. id*: str* :   A globally unique ID for this event. source*: str* :   The resource which published this event. specversion*: str* :   Version of the CloudEvents spec for this event. subject*: str \| None* :   The resource, provided by source, that this event relates to. time*: datetime* :   When this event occurred. type*: str* :   The type of event that this represents. |

## Functions

|                                                 ### init firebase_functions.core.init(*callback: Callable\[\[\], Any\]* ) â None                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Registers a function that should be run when in a production environment before executing any functions code. Calling this decorator more than once leads to undefined behavior. |