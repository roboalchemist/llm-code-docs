# Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions

Title: Subscriptions - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions

Markdown Content:
GraphQL subscriptions provide real-time functionality to applications by allowing clients to subscribe to specific events. When these events trigger, the server immediately sends updates to the subscribed clients.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#transport-mechanisms-for-graphql-subscriptions)Transport Mechanisms for GraphQL Subscriptions
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The method of how these updates are delivered is determined by the transport mechanism. In this section, we will discuss two popular transport mechanisms: GraphQL over WebSockets and GraphQL over Server-Sent Events (SSE).

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#graphql-over-websockets)GraphQL over WebSockets
--------------------------------------------------------------------------------------------------------------------------------

WebSockets provide a full-duplex communication channel over a single TCP connection. This means data can be sent and received simultaneously. With GraphQL, this means both queries/mutations and subscription operations can be sent over the same connection.

WebSockets are widely supported in browsers and have been the de facto standard for real-time data transport in GraphQL. There are two popular protocols for GraphQL over WebSockets: [graphql-ws](https://github.com/enisdenjo/graphql-ws) and [subscription-transport-ws](https://github.com/apollographql/subscriptions-transport-ws). Hot Chocolate, supports both protocols.

In terms of specific protocols, the recommendation is to use graphql-ws or graphql-sse over the legacy subscription-transport-ws.

**Key Features:**

*   Full-duplex: Both the client and server can initiate communication, allowing real-time bidirectional communication.
*   Persistent connection: The connection between client and server remains open, allowing for real-time data transfer.
*   Well-supported: There are several libraries available for managing WebSocket connections and GraphQL subscriptions.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#graphql-over-server-sent-events-sse)GraphQL over Server-Sent Events (SSE)
----------------------------------------------------------------------------------------------------------------------------------------------------------

Server-Sent Events (SSE) is a standard that allows a server to push real-time updates to clients over HTTP. Unlike WebSockets, SSE is a half-duplex communication channel, which means the server can send messages to the client, but not the other way around. This makes it a good fit for one-way real-time data like updates or notifications.

With GraphQL, you can send regular queries and mutations over HTTP/2 and subscription updates over SSE. This combination leverages the strengths of both HTTP/2 (efficient for request-response communication) and SSE (efficient for server-to-client streaming).

Another advantage of SSE is its better compatibility with firewalls compared to WebSockets. However, if you're using HTTP/1, keep in mind that SSE inherits its limitations, such as supporting no more than 7 parallel requests in the browser.

[graphql-sse](https://github.com/enisdenjo/graphql-sse) is a popular library for GraphQL over SSE.

**Key Features:**

*   Efficient for one-way real-time data: The server can push updates to the client as soon as they occur.
*   Built on HTTP: SSE is built on HTTP, simplifying handling and compatibility. It benefits from HTTP features such as automatic reconnection, HTTP/2 multiplexing, and headers/cookies support.
*   Less Complex: SSE is less complex than WebSockets as it only allows for one-way communication.
*   Better Firewall Compatibility: SSE generally encounters fewer issues with firewalls.

Choosing between GraphQL over WebSockets and GraphQL over SSE depends on the specific needs of your application. If you need full-duplex, real-time communication, WebSockets may be the best choice. If you only need server-to-client real-time communication and want to take advantage of existing HTTP infrastructure, SSE could be a better option.

Special thanks to Denis Badurina, @enisdenjo on [Twitter](https://twitter.com/enisdenjo) and [GitHub](https://github.com/enisdenjo). He is the creator of [graphql-http](https://github.com/enisdenjo/graphql-http), [graphql-ws](https://github.com/enisdenjo/graphql-ws) and [graphql-sse](https://github.com/enisdenjo/graphql-sse).

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#usage)Usage
--------------------------------------------------------------------------------------------

Subscribing to an event is like writing a standard query. The only difference is the operation keyword and that we are only allowed to have one root field.

SDL

type Subscription {

bookAdded: Book!

bookPublished(author: String!): Book!

}

GraphQL

subscription {

bookAdded {

title

}

}

A subscription type can be defined like the following.

C#

public class Subscription

{

[Subscribe]

public Book BookAdded([EventMessage] Book book) => book;

}

C#

builder.Services

.AddGraphQLServer()

.AddSubscriptionType<Subscription>();

Warning

Only **one** subscription type can be registered using `AddSubscriptionType()`. If we want to split up our subscription type into multiple classes, we can do so using type extensions.

[Learn more about extending types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types)

A subscription type is just a regular object type, so everything that applies to an object type also applies to the subscription type (this is true for all all root types).

[Learn more about object types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types)

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#transport)Transport
----------------------------------------------------------------------------------------------------

After defining the subscription type, we need to add the WebSockets middleware to our request pipeline.

C#

app.UseRouting();

app.UseWebSockets();

app.UseEndpoints(endpoints =>

{

endpoints.MapGraphQL();

});

To make pub/sub work, we also have to register a subscription provider. A subscription provider represents a pub/sub implementation used to handle events. Out of the box we support two subscription providers.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#in-memory-provider)In-Memory Provider
----------------------------------------------------------------------------------------------------------------------

The In-Memory subscription provider does not need any configuration and is easily setup.

C#

builder.Services

.AddGraphQLServer()

.AddInMemorySubscriptions();

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#redis-provider)Redis Provider
--------------------------------------------------------------------------------------------------------------

The Redis subscription provider enables us to run multiple instances of our Hot Chocolate GraphQL server and handle subscription events reliably.

In order to use the Redis provider we have to add the `HotChocolate.Subscriptions.Redis` package.

Bash

dotnet add package HotChocolate.Subscriptions.Redis

Warning

All `HotChocolate.*` packages need to have the same version.

After we have added the package we can setup the Redis subscription provider.

C#

builder.Services

.AddGraphQLServer()

.AddRedisSubscriptions((sp) => ConnectionMultiplexer.Connect("host:port"));

Our Redis subscription provider uses the [StackExchange.Redis](https://github.com/StackExchange/StackExchange.Redis) Redis client underneath.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#postgres-provider)Postgres Provider
--------------------------------------------------------------------------------------------------------------------

The PostgreSQL Subscription Provider enables your GraphQL server to provide real-time updates to your clients using PostgreSQL's native `LISTEN/NOTIFY` mechanism. This provider is ideal for applications that already use PostgreSQL and want to avoid the overhead of running a separate pub/sub service.

In order to use the PostgreSQL provider we have to add the `HotChocolate.Subscriptions.Postgres` package.

Bash

dotnet add package HotChocolate.Subscriptions.Postgres

To enable Postgres subscriptions with your HotChocolate server, add `AddPostgresSubscriptions` to your GraphQL server configuration:

C#

builder.Services

.AddGraphQLServer()

.AddQueryType<Query>()

.AddSubscriptionType<Subscriptions>()

.AddPostgresSubscriptions((sp, options) => options.ConnectionFactory = ct => );

### [](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#options)Options

`PostgresSubscriptionOptions` encapsulates options for configuring the Postgres subscription provider. The properties included in this class are:

1.   `ConnectionFactory`: A function used to create a new, long-lived connection. The connection should have the following configuration to work optimally:

    *   `KeepAlive=30`: Sets a keep alive interval to keep the connection alive
    *   `Pooling=false`: Disables pooling as it is not needed
    *   `Enlist=false`: Ensures subscriptions run in the background and are not enlisted into any transaction

2.   `ChannelName`: Specifies the name of the Postgres channel used to send/receive messages. The default value is "hotchocolate_subscriptions".

3.   `MaxSendBatchSize`: Sets the maximum number of messages sent in one batch. The default value is 256.

4.   `MaxSendQueueSize`: Determines the maximum number of messages that can be queued for sending. If the queue is full, the subscription will wait until there is available space. The default value is 2048.

5.   `SubscriptionOptions`: Options used to configure the subscriptions.

Here's an example of creating a connection factory suitable for long-lived connections:

C#

var builder = new NpgsqlDataSourceBuilder(connectionString);

builder.ConnectionStringBuilder.Pooling = false;

builder.ConnectionStringBuilder.KeepAlive = 30;

builder.ConnectionStringBuilder.Enlist = false;

var dataSource = builder.Build();

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#publishing-events)Publishing Events
--------------------------------------------------------------------------------------------------------------------

To publish events and trigger subscriptions, we can use the `ITopicEventSender`. The `ITopicEventSender` is an abstraction for the registered event publishing provider. Using this abstraction allows us to seamlessly switch between subscription providers, when necessary.

Most of the time we will be publishing events for successful mutations. Therefore we can simply inject the `ITopicEventSender` into our mutations like we would with every other `Service`. Of course we can not only publish events from mutations, but everywhere we have access to the `ITopicEventSender` through the DI Container.

C#

public class Mutation

{

public async Book AddBook(Book book, ITopicEventSender sender)

{

await sender.SendAsync("BookAdded", book);

}

}

In the example the `"BookAdded"` is the topic we want to publish to, and `book` is our payload. Even though we have used a string as the topic, we do not have to. Any other type works just fine.

But where is the connection between `"BookAdded"` as a topic and the subscription type? By default, Hot Chocolate will try to map the topic to a field of the subscription type. If we want to make this binding less error-prone, we could do the following.

C#

await sender.SendAsync(nameof(Subscription.BookAdded), book);

If we do not want to use the method name, we could use the `Topic` attribute.

C#

public class Subscription

{

[Subscribe]

[Topic("ExampleTopic")]

public Book BookAdded([EventMessage] Book book) => book;

}

public async Book AddBook(Book book, ITopicEventSender sender)

{

await sender.SendAsync("ExampleTopic", book);

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#dynamic-topics)Dynamic Topics
--------------------------------------------------------------------------------------------------------------

We can even use the `Topic` attribute on dynamic arguments of the subscription field.

C#

public class Subscription

{

[Subscribe]

[Topic($"{{{nameof(author)}}}")]

public Book BookPublished(string author, [EventMessage] Book book)

=> book;

}

public async Book PublishBook(Book book, ITopicEventSender sender)

{

await sender.SendAsync(book.Author, book);

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#itopiceventreceiver)ITopicEventReceiver
------------------------------------------------------------------------------------------------------------------------

If more complex topics are required, we can use the `ITopicEventReceiver`.

C#

public class Subscription

{

public ValueTask<ISourceStream<Book>> SubscribeToBooks(ITopicEventReceiver receiver)

=> receiver.SubscribeAsync<Book>("ExampleTopic");

[Subscribe(With = nameof(SubscribeToBooks))]

public Book BookAdded([EventMessage] Book book)

=> book;

}

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#websocket-authentication)Websocket Authentication
----------------------------------------------------------------------------------------------------------------------------------

When working with GraphQL subscriptions over WebSockets, you may want to authenticate incoming WebSocket connections using JSON Web Tokens. Normally, HTTP headers are sent with each request for standard APIs, but WebSockets behave differently. After a successful HTTP handshake, the protocol is "upgraded" to WebSockets, and additional headers cannot be easily injected for subsequent messages.

Instead, the recommended approach is to send your token via the `connection_init` message when the WebSocket connection is first established. Hot Chocolate allows you to intercept this initial message, extract the token, and then authenticate the user in a way similar to standard HTTP requests.

An example implementation of this approach can be found in the [Hot Chocolate Examples repository](https://github.com/ChilliCream/hotchocolate-examples/tree/master/misc/WebsocketAuthentication).

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#why-a-special-approach-for-websockets)Why a Special Approach for WebSockets
------------------------------------------------------------------------------------------------------------------------------------------------------------

*   **Single HTTP Handshake**: A WebSocket connection is established once. After that, you cannot update HTTP headers on the same connection.
*   **`connection_init` Payload**: GraphQL subscription clients send a `connection_init` message when establishing the subscription. This payload can include extra properties (e.g., `authorization`), which Hot Chocolate can use for authentication.
*   **Long-Lived Connections**: Because WebSockets are persistent, tokens might remain valid for the entire duration of the connection. It is advisable to ensure that you handle token expiration appropriately—often by closing the connection if security policies require it.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#core-concepts)Core Concepts
------------------------------------------------------------------------------------------------------------

1.   **Stub (or "Skip") Authentication Scheme**

The initial WebSocket upgrade request is directed to a "stub" authentication scheme that simply indicates "no authentication result" for upgrade requests. This prevents the request from failing before you can intercept and handle the token manually.

2.   **Forwarding the Default Scheme**

In standard HTTP scenarios, the default scheme (e.g., JWT bearer) is used to authenticate. However, if the request is recognized as a WebSocket upgrade, the framework forwards it to the "stub" scheme first. That way, you don’t attempt to validate a token at the moment of the upgrade handshake.

3.   **Intercepting `connection_init`**

Once the WebSocket is established, the client sends `connection_init` containing authentication data. A custom `SocketSessionInterceptor` (or similar) reads the token from `connection_init` (e.g., under a key like `authorization`), stores it in the `HttpContext`, and triggers a fresh authentication attempt—this time using the real JWT bearer scheme.

4.   **Hot Chocolate Integration**

Hot Chocolate's subscription middleware allows you to plug into the subscription lifecycle. By customizing the session interceptor (`OnConnectAsync`), you can decide whether to accept or reject the connection based on successful authentication.

[](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions#testing-the-flow)Testing the Flow
------------------------------------------------------------------------------------------------------------------

1.   **Open Nitro**

Use a local instance of Nitro (e.g., `https://localhost:5095/graphql`) to send GraphQL queries and subscriptions.

2.   **Retrieve an Access Token**

Request a token from your `/token` endpoint. This endpoint should return a valid JWT that is trusted by your API.

3.   **Configure Nitro**

    *   In Nitro, open the **Settings** of your document / API.
    *   Under **Authentication**, choose **Bearer Token** and paste your JWT.
    *   Nitro will automatically include the token in the `connection_init` message under an `authorization` parameter when opening a WebSocket connection.

4.   **Run Your Subscription**

Execute the subscription query of your choice. For example:

GraphQL

subscription {

onTimedEvent {

count

isAuthenticated

}

} 
The server-side resolver can check `isAuthenticated` to demonstrate whether the current user is authenticated (based on the token you provided).

Last updated on **2026-02-17** by**Tobias Tengler**
