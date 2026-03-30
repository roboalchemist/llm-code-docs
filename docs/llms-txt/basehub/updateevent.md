# updateEvent

> Method that allows modifying existing events by their ID.

```
import { updateEvent } from "basehub/events"
```

## Parameters

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Parameter

Type

Description

`key`

`EventBlock['adminKey']`

**Required.** The event key that defines the schema and scope

`id`

`string`

**Required.** The unique identifier of the event to update

`data`

`object`

**Required.** Partial object containing the fields to update

## Returns

```
{ success: true; eventId: string } | { success: false; error: string }
```