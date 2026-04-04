# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channeloptions.md.txt

# ChannelOptions interface

Channel options interface.

**Signature:**  

    export interface ChannelOptions 

## Properties

|                                                                       Property                                                                       |               Type                |                                                                    Description                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [allowedEventTypes](https://firebase.google.com/docs/reference/admin/node/firebase-admin.eventarc.channeloptions.md#channeloptionsallowedeventtypes) | string\[\] \| string \| undefined | An array of allowed event types. If specified, publishing events of unknown types is a no op. When not provided, no event filtering is performed. |

## ChannelOptions.allowedEventTypes

An array of allowed event types. If specified, publishing events of unknown types is a no op. When not provided, no event filtering is performed.

**Signature:**  

    allowedEventTypes?: string[] | string | undefined;