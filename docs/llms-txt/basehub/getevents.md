# getEvents

> A query method to retrieve your events stored in BaseHub.

```
import { getEvents } from 'basehub/events'
```

## Parameters

### Table Query

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Parameter

Type

Description

`key`

`EventBlock['adminKey']`

**Required.** The event key that defines the schema and scope of the query

`options`

`object`

**Required.** Query configuration:

`options.type`

`"table"`

Specifies table view format

`options.first`

`number`

Number of items to retrieve

`options.skip`

`number`

Number of items to skip

`options.filter?`

`object`

Optional filters for the query

`options.orderBy?`

`object`

Optional sorting configuration

`options.select?`

`object`

Optional fields selection

### Time-series Query

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Parameter

Type

Description

`key`

`${EventKeys}:${string}`

**Required.** The event key that defines the schema and scope of the query

`options`

`object`

**Required.** Query configuration:

`options.type`

`"time-series"`

Specifies time-series format

`options.range?`

`"day"` | `"week"` | `"month"` | `"year"` | `"all-time"`

Optional time range for aggregation

warning:

Be wary of exposing the `adminKey` in the client. Anyone with this key will be able to read and update existing events from that specific block.

## Examples

```
import { getEvents } from "basehub/events"

// Table query
const tableData = await getEvents("analytics:pageviews", {
  type: "table",
  first: 10,
  skip: 0,
})

// Time-series query
const timeSeriesData = await getEvents("analytics:pageviews", {
  type: "time-series",
  range: "month",
})
```

```
import { getEvents } from "basehub/events"
import { IncrementViews } from "./increment-views"
import { unstable_noStore } from "next/cache"
import { draftMode } from "next/headers"
import type { PageViews } from "~/.basehub/schema"

export const ViewsFragment = async ({
  adminKey,
  ingestKey,
  increment,
}: {
  adminKey: PageViews["adminKey"]
  ingestKey: PageViews["ingestKey"]
  increment?: boolean
}) => {
  unstable_noStore()
  const { isEnabled: isDraftMode } = draftMode()

  const { data: views } = await getEvents(adminKey, { 
    type: "time-series",
    range: "all-time",
  }) 

  return (
    <>
      {views || "0"}
      {increment && !isDraftMode && (
        <IncrementViews ingestKey={ingestKey} />
      )}
    </>
  )
}
```