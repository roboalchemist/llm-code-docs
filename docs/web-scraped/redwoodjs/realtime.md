# Source: https://docs.redwoodjs.com/docs/realtime

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Realtime]

[Version: 8.8]

On this page

<div>

# Realtime

</div>

One of the most often-asked questions of Redwood before and after the launch of V1 was, "When will Redwood support a realtime solution?"

The answer is: **now**.

## What is Realtime?[​](#what-is-realtime "Direct link to What is Realtime?") 

Redwood\'s initial realtime solution leverages GraphQL and relies on a serverful deployment to maintain a long-running connection between the client and server.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

This means that your cannot use Realtime when deploying to Netlify or Vercel.

See one of Redwood\'s many [other Deploy providers](/docs/deploy/introduction), and the [Docker setup](/docs/docker) for good measure.

Redwood\'s GraphQL server uses the [GraphQL over Server-Sent Events](https://github.com/enisdenjo/graphql-sse/blob/master/PROTOCOL.md#distinct-connections-mode) spec\'s \"distinct connections mode\" for subscriptions.

Advantages of SSE over WebSockets include:

-   Transported over simple HTTP instead of a custom protocol
-   Built in support for re-connection and event-id
-   Simpler protocol
-   No trouble with corporate firewalls doing packet inspection

### Subscriptions and Live Queries[​](#subscriptions-and-live-queries "Direct link to Subscriptions and Live Queries") 

In GraphQL, there are two options for real-time updates: **live queries** and **subscriptions**.

Subscriptions are part of the GraphQL specification, whereas live queries are not.

There are times where subscriptions are well-suited for a realtime problem and in some cases live queries may be a better fit. Later we'll explore the pros and cons of each approach and how best to decide which to use and when.

### Defer and Stream[​](#defer-and-stream "Direct link to Defer and Stream") 

[Defer and stream](https://the-guild.dev/graphql/yoga-server/docs/features/defer-stream) are directives that allow you to improve latency for clients by sending the most important data as soon as it\'s ready.

As applications grow, the GraphQL operation documents can get bigger. The server will only send the response back once all the data requested in the query is ready. But not all requested data is of equal importance, and the client may not need all of the data at once.

#### Using Defer[​](#using-defer "Direct link to Using Defer") 

The `@defer` directive allows you to postpone the delivery of one or more (slow) fields grouped in an inlined or spread fragment.

#### Using Stream[​](#using-stream "Direct link to Using Stream") 

The `@stream` directive allows you to stream the individual items of a field of the list type as the items are available.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

The `@stream` directive is currently **not** supported by Apollo GraphQL client.

## Features[​](#features "Direct link to Features") 

Realtime handles the hard parts of a GraphQL realtime implementation by automatically:

-   allowing GraphQL Subscription operations to be handled
-   merging in your subscriptions types and mapping their handler functions (subscribe and resolve) to your GraphQL schema letting you keep your subscription logic organized and apart from services (your subscription may use a service to respond to an event)
-   authenticating subscription requests using the same `@requireAuth` directives already protecting other queries and mutations (or you can implement your own validator directive)
-   adding in the `@live` query directive to your GraphQL schema and setting up the `useLiveQuery` envelop plugin to handle requests, invalidation, and managing the storage mechanism needed
-   creating and configuring in-memory and persisted Redis stores used by the PubSub transport for subscriptions and Live Queries (and letting you switch between them in development and production)
-   placing the pubSub transport and stores into the GraphQL context so you can use them in services, subscription resolvers, or elsewhere (like a webhook, function, or job) to publish an event or invalidate data
-   typing your subscription channel event payloads
-   support `@defer` and `@stream` directives

It provides a first-class developer experience for real-time updates with GraphQL so you can easily

-   respond to an event (e.g. NewPost, NewUserNotification)
-   respond to a data change (e.g. Post 123\'s title updated)

and have the latest data reflected in your app.

Lastly, the Redwood CLI has commands to generate a boilerplate implementation and sample code needed to create your custom subscriptions and Live Queries.

Regardless of the implementation chosen, **a stateful server and store are needed** to track changes, invalidation, and who wants to be informed about changes.

### What can I build with Realtime?[​](#what-can-i-build-with-realtime "Direct link to What can I build with Realtime?") 

-   Application alerts and messages
-   User notifications
-   Live charts
-   Location updates
-   Auction bid updates
-   Messaging
-   OpenAI streaming responses

## Redwood Realtime Setup[​](#redwood-realtime-setup "Direct link to Redwood Realtime Setup") 

To setup realtime in an existing Redwood project, run the following commands:

-   `yarn rw setup server-file`
-   `yarn rw setup realtime`

You\'ll get:

-   `api/server.ts` where you can configure your Fastify server
-   `api/lib/realtime.ts` where you consume your subscriptions and configure realtime with an in-memory or Redis store
-   Usage examples for live queries, subscriptions, defer, and stream. You\'ll get sdl, services/subscriptions for each
-   The [`auction` live query](#auction-live-query-example) example
-   The [`countdown timer` subscription](#countdown-timer-example) example
-   The [`chat` subscription](#chatnew-message-example) examples
-   The [`alphabet` stream](#alphabet-stream-example) example
-   The [`slow and fast` field defer](#slow-and-fast-field-defer-example) example

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

There is no UI set up for these examples. You can find information on how to try them out using the GraphiQL playground.

Just add the realtime configuration to your GraphQL handler in `api/src/functions/graphql.ts` and you\'re good to go:

api/src/functions/graphql.ts

``` 
+ import  from 'src/lib/realtime'

  export const handler = createGraphQLHandler()
```

### Realtime Configuration[​](#realtime-configuration "Direct link to Realtime Configuration") 

By default, Redwood\'s realtime configures an in-memory store for the Pub Sub client used with subscriptions and live query invalidation.

Realtime supports in-memory and Redis stores:

-   In-memory stores are useful for development and testing.
-   Redis stores are useful for production.

To enable defer and streaming, set `enableDeferStream` to true.

Configure a Redis store and defer and stream in:

api/lib/realtime.ts

``` 
import  from '@redwoodjs/realtime'

import subscriptions from 'src/subscriptions/**/*.'

// if using a Redis store
// import  from 'ioredis'
// const publishClient = new Redis()
// const subscribeClient = new Redis()

/**
 * Configure RedwoodJS Realtime
 *
 * See https://redwoodjs.com/docs/realtime
 *
 * Realtime supports Live Queries and Subscriptions over GraphQL SSE.
 *
 * Live Queries are GraphQL queries that are automatically re-run when the data they depend on changes.
 *
 * Subscriptions are GraphQL queries that are run when a client subscribes to a channel.
 *
 * Redwood Realtime
 *  - uses a publish/subscribe model to broadcast data to clients.
 *  - uses a store to persist Live Query and Subscription data.
 *
 * Redwood Realtime supports in-memory and Redis stores:
 * - In-memory stores are useful for development and testing.
 * - Redis stores are useful for production.
 */
export const realtime: RedwoodRealtimeOptions =  },
  },
  liveQueries:  },
  },
  // To enable defer and streaming, set to true.
  // enableDeferStream: true,
}
```

#### PubSub and LiveQueryStore[​](#pubsub-and-livequerystore "Direct link to PubSub and LiveQueryStore") 

By setting up realtime, the GraphQL server adds two helpers on the context:

-   pubSub
-   liveQueryStore

With `context.pubSub` you can subscribe to and publish messages via `context.pubSub.publish('the-topic', id, id2)`.

With `context.liveQueryStore.` you can `context.liveQueryStore.invalidate(key)` where your key may be a reference or schema coordinate:

##### Reference[​](#reference "Direct link to Reference") 

Where the query is: `auction(id: ID!): Auction @requireAuth`:

-   `"Auction:123"`

##### Schema Coordinate[​](#schema-coordinate "Direct link to Schema Coordinate") 

When the query is: `auctions: [Auction!]! @requireAuth`:

-   `"Query.auctions"`

## Subscriptions[​](#subscriptions "Direct link to Subscriptions") 

Redwood has a first-class developer experience for GraphQL subscriptions.

#### Subscribe to Events[​](#subscribe-to-events "Direct link to Subscribe to Events") 

-   Granular information on what data changed
-   Why has the data changed?
-   Spec compliant

### Chat/New Message Example[​](#chatnew-message-example "Direct link to Chat/New Message Example") 

``` 
type Subscription 
```

1.  I subscribed to a \"newMessage" in room "2"
2.  Someone added a message to room "2" with a from and body
3.  A \"NewMessage\" event to Room 2 gets published
4.  I find out and see who the message is from and what they messaged (the body)

### Countdown Timer Example[​](#countdown-timer-example "Direct link to Countdown Timer Example") 

Counts down from a starting values by an interval.

``` 
subscription CountdownFromInterval 
```

This example showcases how a subscription yields its own response.

## Live Queries[​](#live-queries "Direct link to Live Queries") 

Redwood has made it super easy to add live queries to your GraphQL server! You can push new data to your clients automatically once the data selected by a GraphQL operation becomes stale by annotating your query operation with the `@live` directive.

The invalidation mechanism is based on GraphQL ID fields and schema coordinates. Once a query operation has been invalidated, the query is re-executed, and the result is pushed to the client.

##### Listen for Data Changes[​](#listen-for-data-changes "Direct link to Listen for Data Changes") 

-   I\'m not interested in what exactly changed it.
-   Just give me the data.
-   This is not part of the GraphQL specification.
-   There can be multiple root fields.

### Auction Live Query Example[​](#auction-live-query-example "Direct link to Auction Live Query Example") 

``` 
query GetCurrentAuctionBids @live 
    highestBid 
    id
    title
  }
}

mutation MakeBid ) 
}
```

1.  I listen for changes to Auction 1 by querying the auction.
2.  A bid was placed on Auction 1.
3.  The information for Auction 1 is no longer valid.
4.  My query automatically refetches the latest Auction and Bid details.

## Defer Directive[​](#defer-directive "Direct link to Defer Directive") 

The `@defer` directive allows you to postpone the delivery of one or more (slow) fields grouped in an inlined or spread fragment.

### Slow and Fast Field Defer Example[​](#slow-and-fast-field-defer-example "Direct link to Slow and Fast Field Defer Example") 

Here, the GraphQL schema defines two queries for a \"fast\" and a \"slow\" (i.e., delayed) information.

``` 
export const schema = gql`
  type Query 
`
```

The Redwood services for these queries return the `fastField` immediately and the `showField` after some delay.

``` 
import  from 'src/lib/logger'

const wait = (time: number) =>
  new Promise((resolve) => setTimeout(resolve, time))

export const fastField = async () => 

export const slowField = async (_, ) => 
```

When making the query:

``` 
query SlowAndFastFieldWithDefer 
  fastField
}
```

The response returns:

``` 

}
```

and will await the deferred field to then present:

``` 

}
```

## Stream Directive[​](#stream-directive "Direct link to Stream Directive") 

The `@stream` directive allows you to stream the individual items of a field of the list type as the items are available.

### Alphabet Stream Example[​](#alphabet-stream-example "Direct link to Alphabet Stream Example") 

Here, the GraphQL schema defines a query to return the letters of the alphabet:

``` 
export const schema = gql`
  type Query info

[AsyncGenerators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncGenerator) as declared via the `async *` keywords are prone to memory leaks and leaking timers. For real-world usage, use Repeater.

``` 
import  from '@redwoodjs/realtime'

import  from 'src/lib/logger'

export const alphabet = async () => , 'publishing')

        push(value)
      }

      if (values.length === 0) 
    }

    const interval = setInterval(publish, 1000)

    stop.then(() => )

    publish()
  })
}
```

### What does the incremental stream look like?[​](#what-does-the-incremental-stream-look-like "Direct link to What does the incremental stream look like?") 

Since Apollo Client does not yet support the `@stream` directive, you can use them in the GraphiQL Playground or see them in action via CURL.

When making the request with the `@stream` directive:

``` 
curl -g -X POST \
  -H "accept:multipart/mixed" \
  -H "content-type: application/json" \
  -d '"}' \
  http://localhost:8911/graphql
```

Here you see the initial response has `[]` for alphabet data. Then on each push to the Repeater, an incremental update to the list of letters is sent. The stream ends when `hasNext` is false:

``` 
* Connected to localhost (127.0.0.1) port 8911 (#0)
> POST /graphql HTTP/1.1
> Host: localhost:8911
> User-Agent: curl/8.1.2
> accept:multipart/mixed
> content-type: application/json
> Content-Length: 53
>
< HTTP/1.1 200 OK
< connection: keep-alive
< content-type: multipart/mixed; boundary="-"
< transfer-encoding: chunked
<
---
Content-Type: application/json; charset=utf-8
Content-Length: 39

,"hasNext":true}
---
Content-Type: application/json; charset=utf-8
Content-Length: 70

],"hasNext":true}
---
Content-Type: application/json; charset=utf-8
Content-Length: 70

],"hasNext":true}
---
Content-Type: application/json; charset=utf-8
Content-Length: 70

],"hasNext":true}
---
Content-Type: application/json; charset=utf-8
Content-Length: 70

],"hasNext":true}
---
Content-Type: application/json; charset=utf-8
Content-Length: 70

],"hasNext":true}
---
Content-Type: application/json; charset=utf-8
Content-Length: 70

],"hasNext":true}
---
Content-Type: application/json; charset=utf-8
Content-Length: 70

],"hasNext":true}
---
...

---
Content-Type: application/json; charset=utf-8
Content-Length: 17

-----
```

## How do I choose Subscriptions or Live Queries?[​](#how-do-i-choose-subscriptions-or-live-queries "Direct link to How do I choose Subscriptions or Live Queries?") 

![image](https://github.com/ahaywood/redwoodjs-streaming-realtime-demos/assets/1051633/e3c51908-434c-4396-856a-8bee7329bcdd)

When deciding on how to offer realtime data updates, you'll want to consider:

-   How frequently do your users require information updates?
    -   Determine the value of \"real-time\" versus \"near real-time\" to your users. Do they need to know in less than 1-2 seconds, or is 10, 30, or 60 seconds acceptable for them to receive updates?
    -   Consider the criticality of the data update. Is it low, such as a change in shipment status, or higher, such as a change in stock price for an investment app?
    -   Consider the cost of maintaining connections and tracking updates across your user base. Is the infrastructure cost justifiable?
    -   If you don\'t require \"real\" real-time, consider polling for data updates on a reasonable interval. According to Apollo, [in most cases](https://www.apollographql.com/docs/react/data/subscriptions/), your client should not use subscriptions to stay up to date with your backend. Instead, you should poll intermittently with queries or re-execute queries on demand when a user performs a relevant action, such as clicking a button.
-   How are you deploying? Serverless or serverful?
    -   Real-time options depend on your deployment method.
    -   If you are using a serverless architecture, your application cannot maintain a stateful connection to your users\' applications. Therefore, it\'s not easy to \"push,\" \"publish,\" or \"stream\" data updates to the web client.
        -   In this case, you may need to look for third-party solutions that manage the infrastructure to maintain such stateful connections to your web client, such as [Supabase Realtime](https://supabase.com/realtime), [SendBird](https://sendbird.com/), [Pusher](https://pusher.com/), or consider creating your own [AWS SNS-based](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) functionality.

## Showcase Demos[​](#showcase-demos "Direct link to Showcase Demos") 

Please see our [showcase realtime app](https://realtime-demo.fly.dev) for examples of subscriptions and live queries. It also demonstrates how you can handle streaming responses, like those used by OpenAI chat completions.

### Chat Room (Subscription)[​](#chat-room-subscription "Direct link to Chat Room (Subscription)") 

Sends a message to one of four Chat Rooms.

Each room subscribes to its new messages via the `NewMessage` channel aka topic.

``` 
context.pubSub.publish('newMessage', roomId, )
```

#### Simulate[​](#simulate "Direct link to Simulate") 

``` 
./scripts/simulate_chat.sh -h
Usage: ./scripts/simulate_chat.sh -r [roomId] -n [num_messages]
       ./scripts/simulate_chat.sh -h

Options:
  -r roomId       Specify the room ID (1-4) for sending chat messages.
  -n num_messages Specify the number of chat messages to send. If not provided, the script will run with a random number of messages.
```

#### Test[​](#test "Direct link to Test") 

``` 
/**
 * To test this NewMessage subscription, run the following in one GraphQL Playground to subscribe:
 *
 * subscription ListenForNewMessagesInRoom 
 * }
 *
 *
 * And run the following in another GraphQL Playground to publish and send a message to the room:
 *
 * mutation SendMessageToRoom ) 
 * }
 */
```

### Auction Bids (Live Query)[​](#auction-bids-live-query "Direct link to Auction Bids (Live Query)") 

Bid on a fancy pair of new sneaks!

When a bid is made, the auction updates via a Live Query due to the invalidation of the auction key.

``` 
const key = `Auction:$`
context.liveQueryStore.invalidate(key)
```

#### Simulate[​](#simulate-1 "Direct link to Simulate") 

``` 
./scripts/simulate_bids.sh -h
Usage: ./scripts/simulate_bids.sh [options]

Options:
  -a <auctionId>  Specify the auction ID (1-5) for which to send bids (optional).
  -n <num_bids>   Specify the number of bids to send (optional).
  -h, --help      Display this help message.
```

#### Test[​](#test-1 "Direct link to Test") 

``` 
/**
 * To test this live query, run the following in the GraphQL Playground:
 *
 * query GetCurrentAuctionBids @live 
 *    highestBid 
 *    id
 *    title
 *   }
 * }
 *
 * And then make a bid with the following mutation:
 *
 * mutation MakeBid ) 
 * }
 */
```

### Countdown (Streaming Subscription)[​](#countdown-streaming-subscription "Direct link to Countdown (Streaming Subscription)") 

> It started slowly and I thought it was my heart But then I realised that this time it was for real

Counts down from a starting values by an interval.

This example showcases how a subscription can yields its own response.

#### Test[​](#test-2 "Direct link to Test") 

``` 
/**
 * To test this Countdown subscription, run the following in the GraphQL Playground:
 *
 * subscription CountdownFromInterval 
 */
```

### Bedtime Story (Subscription with OpenAI Streaming)[​](#bedtime-story-subscription-with-openai-streaming "Direct link to Bedtime Story (Subscription with OpenAI Streaming)") 

> Tell me a story about a happy, purple penguin that goes to a concert.

Showcases how to use OpenAI to stream a chat completion via a prompt that writes a bedtime story:

``` 
const PROMPT = `Write a short children's bedtime story about an Animal that is a given Color and that does a given Activity.

Give the animal a cute descriptive and memorable name.

The story should teach a lesson.

The story should be told in a quality, style and feeling of the given Adjective.

The story should be no longer than 3 paragraphs.

Format the story using Markdown.`
```

The story updates on each stream content delta via a `newStory` subscription topic event.

``` 
context.pubSub.publish('newStory', id, story)
```

### Movie Mashup (Live Query with OpenAI Streaming)[​](#movie-mashup-live-query-with-openai-streaming "Direct link to Movie Mashup (Live Query with OpenAI Streaming)") 

> It\'s Out of Africa meets Pretty Woman.

> So it\'s a psychic, political, thriller comedy with a heart With a heart, not unlike Ghost meets Manchurian Candidate.

\-- The Player, 1992

Mashup some of your favorite movies to create something new and Netflix-worthy to watch.

Powered by OpenAI, this movie tagline and treatment updates on each stream content delta via a Live Query by invalidating the \`MovieMashup key.

``` 
context.liveQueryStore.invalidate(`MovieMashup:$`)
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/realtime.md)