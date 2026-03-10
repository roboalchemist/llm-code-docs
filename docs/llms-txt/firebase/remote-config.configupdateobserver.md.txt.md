# Source: https://firebase.google.com/docs/reference/js/remote-config.configupdateobserver.md.txt

# ConfigUpdateObserver interface

Observer interface for receiving real-time Remote Config update notifications.

NOTE: Although an `complete` callback can be provided, it will never be called because the ConfigUpdate stream is never-ending.

**Signature:**

    export interface ConfigUpdateObserver 

## Properties

| Property | Type | Description |
|---|---|---|
| [complete](https://firebase.google.com/docs/reference/js/remote-config.configupdateobserver.md#configupdateobservercomplete) | () =\> void | Called when the stream is gracefully terminated. |
| [error](https://firebase.google.com/docs/reference/js/remote-config.configupdateobserver.md#configupdateobservererror) | (error: [FirebaseError](https://firebase.google.com/docs/reference/js/util.firebaseerror.md#firebaseerror_class)) =\> void | Called if an error occurs during the stream. |
| [next](https://firebase.google.com/docs/reference/js/remote-config.configupdateobserver.md#configupdateobservernext) | (configUpdate: [ConfigUpdate](https://firebase.google.com/docs/reference/js/remote-config.configupdate.md#configupdate_interface)) =\> void | Called when a new ConfigUpdate is available. |

## ConfigUpdateObserver.complete

Called when the stream is gracefully terminated.

**Signature:**

    complete: () => void;

## ConfigUpdateObserver.error

Called if an error occurs during the stream.

**Signature:**

    error: (error: FirebaseError) => void;

## ConfigUpdateObserver.next

Called when a new ConfigUpdate is available.

**Signature:**

    next: (configUpdate: ConfigUpdate) => void;