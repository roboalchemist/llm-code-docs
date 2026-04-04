# Analytics

> Learn how to send analytics events from your website.

BaseHub’s [Event Block](https://docs.basehub.com/blocks/primitives/event) provides a powerful way to know more about how your content is performing. The unique thing about it is that Events that occur throughout your website can be tied directly to a Block—therefore keeping it in context.

info:

While this article focuses on analytics, the Event block is versatile and offers much more functionality, including two different layouts and multiple use cases. For a more complex use case, check out [Forms](https://docs.basehub.com/extras/forms).

The Event Block time-series can be used for tracking things like:

*   Page views (internal and user facing)
    
*   Button/Link Clicks
    
*   Feedback forms
    

Or anything you want, really.

## Set up an Event Block and start receiving events

First of all, you’ll need to add a new Event Block to your repo.

1.  Create a new event block
    
2.  Switch to Time-series layout
    
3.  Commit your changes (not necessary if you’re working on draft mode)
    
4.  Get your event’s `ingestKey`
    

note:

### `ingestKey` vs `adminKey`

Keep in mind that the Event block exposes two different keys for different type of actions.

Since sending data is the most common, and at the same time the most safe, action in events, it has a distinctive `ingestKey` that can be safely used client side.

On the other side, update and read access is reserved for the `adminKey` and could be the case that the data stored being sensitive enough to protect that key and only use it server-side.

## Send an Event

In order to send an event, you’ll need to first get the `ingestKey` of an Event Block from the GraphQL API. Let's look at an example that tracks page views on the homepage. Once we get the page data and its `ingestKey`, we’ll `import { sendEvent } from "basehub/events"` and run it on mount:

Get page data

```
import { Pump } from "basehub/react-pump"
import { draftMode } from "next/headers"

const Homepage = () => {
  return (
    <Pump
      next={{ revalidate: 30 }}
      draft={draftMode().isEnabled}
      queries={[
        {
          homepage: {
            _title: true,
            pageViews: {
              ingestKey: true,
            }
          },
        },
      ]}
    >
      {async ([{ homepage }]) => {
        "use server"

        return (
          <div>
            <PageView ingestKey={homepage.pageViews.ingestKey} />
            <h1>{homepage._title}</h1>
          </div>
        )
      }}
    </Pump>
  )
}
```

## Get an Event count

In case you want to show the Event Count in your website—for example, to render a “view count”—, well, you can! Following up from the `<PageView />` component we built previously, we can update it so that it runs `getEvents` and renders it:

```
"use client"
import * as React from "react"
import type { PageViews as PageViewsType } from "~/.basehub/schema"
import { sendEvent, getEvents } from "basehub/events"

export const PageView = ({
  ingestKey,
  adminKey,
}: {
  ingestKey: PageViewsType["ingestKey"],
  adminKey: PageViewsType["adminKey"]
}) => {
  const [count, setCount] = React.useState() 

  // On mount, send the event
  React.useEffect(() => {
    sendEvent({ ingestKey, name: "page_view" })
  }, [])

  // We also get the event count so we can render it
  React.useEffect(() => { 
    getEvents(key, { 
      type: 'time-series',
      range: 'all-time'
    }).then( 
      (response) => { 
        if (response.success) { 
          setCount(response.data) 
        } 
      },
    ) 
  }, []) 

  return <div>Views: {count ?? "Loading..."}</div> 
}
```