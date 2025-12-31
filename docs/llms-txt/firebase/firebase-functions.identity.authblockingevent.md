# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md.txt

# identity.AuthBlockingEvent interface

Defines the auth event for 2nd gen blocking events

**Signature:**  

    export interface AuthBlockingEvent extends AuthEventContext 

**Extends:** AuthEventContext

## Properties

|                                                                         Property                                                                         |                                                                                Type                                                                                | Description |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| [data](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authblockingevent.md#identityauthblockingeventdata) | [AuthUserRecord](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.identity.authuserrecord.md#identityauthuserrecord_interface) |             |

## identity.AuthBlockingEvent.data

**Signature:**  

    data?: AuthUserRecord;