# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.multicastmessage.md.txt

# MulticastMessage interface

Payload for the [Messaging.sendEachForMulticast()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.messaging.md#messagingsendeachformulticast) method. The payload contains all the fields in the BaseMessage type, and a list of tokens.

**Signature:**  

    export interface MulticastMessage extends BaseMessage 

**Extends:** [BaseMessage](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.basemessage.md#basemessage_interface)

## Properties

|                                                              Property                                                               |    Type    | Description |
|-------------------------------------------------------------------------------------------------------------------------------------|------------|-------------|
| [tokens](https://firebase.google.com/docs/reference/admin/node/firebase-admin.messaging.multicastmessage.md#multicastmessagetokens) | string\[\] |             |

## MulticastMessage.tokens

**Signature:**  

    tokens: string[];