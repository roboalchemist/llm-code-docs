# deleteEvent

> Method that removes one or more events by their IDs.

```
import { deleteEvent } from "basehub/events"
```

## Parameters

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Parameter

Type

Description

`key`

`EventBlock['adminKey']`

**Required.** The event key that defines the schema and scope

`ids`

`[string, ...string[]]`

**Required.** Array with at least one event ID to delete

## Returns

```
{ success: true } | { success: false; error: string }
```