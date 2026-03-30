# Source: https://php-enqueue.github.io/concepts/

Title: Key concepts

URL Source: https://php-enqueue.github.io/concepts/

Markdown Content:
If you are new to queuing system, there are some key concepts to understand to make the most of this lib.

The library consist of several components. The components could be used independently or as integral part.

[](https://php-enqueue.github.io/concepts/#components) Components
-----------------------------------------------------------------

### [](https://php-enqueue.github.io/concepts/#transport) Transport

The transport is the underlying vendor-specific library that provides the queuing features: a way for programs to create, send, read messages. Based on [queue interop](https://github.com/queue-interop/queue-interop) interfaces. Use transport directly if you need full control or access to vendor specific features.

The most famous transports are [RabbitMQ](https://php-enqueue.github.io/transport/amqp_lib/), [Amazon SQS](https://php-enqueue.github.io/transport/sqs/), [Redis](https://php-enqueue.github.io/transport/redis/), [Filesystem](https://php-enqueue.github.io/transport/filesystem/).

*   _connection factory_ creates a connection to the vendor service with vendor-specific config.
*   _context_ provides the Producer, the Consumer and helps create Messages. It is the most commonly used object and an implementation of [abstract factory](https://en.wikipedia.org/wiki/Abstract_factory_pattern) pattern.
*   _destination_ is a concept of a destination to which messages can be sent. Choose queue or topic. Destination represents broker state so expect to see same names at broker side.
*   _queue_ is a named destination to which messages can be sent to. Messages accumulate on queues until they are retrieved by programs (called consumers) that service those queues.
*   _topic_ implements [publish and subscribe](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) semantics. When you publish a message it goes to all the subscribers that are interested - so zero to many subscribers will receive a copy of the message. Some brokers do not support Pub\Sub.
*   _message_ describes data sent to (or received from) a destination. It has a body, headers and properties.
*   _producer_ sends a message to the destination. The producer implements vendor-specific logic and is in charge of converting messages between Enqueue and vendor-specific message format.
*   _consumer_ fetches a message from a destination. The consumer implements vendor-specific logic and is in charge of converting messages between vendor-specific message format and Enqueue.
*   _subscription consumer_ provides a way to consume messages from several destinations simultaneously. Some brokers do not support this feature.
*   _processor_ is an optional concept useful for sharing message processing logic. Vendor independent. Implements your business logic.

Additional terms we might refer to:

*   _receive and delete delivery_: the queue deletes the message when it’s fetched by consumer. If processing fails, then the message is lost and won’t be processed again. This is called _at most once_ processing.
*   _peek and lock delivery_: the queue locks for a short amount of time a message when it’s fetched by consumer, making it invisible to other consumers, in order to prevent duplicate processing and message lost. If there is no acknowledgment before the lock times out, failure is assumed and then the message is made visible again in the queue for another try. This is called _at least once_ processing.
*   _an explicit acknowledgement_: the queue locks a message when it’s fetched by consumer, making it invisible to other consumers, in order to prevent duplicate processing and message lost. If there is no explicit acknowledgment received before the connection is closed, failure is assumed and then the message is made visible again in the queue for another try. This is called _at least once_ processing.
*   _message delivery delay_: messages are sent to the queue but won’t be visible right away to consumers to fetch them. You may need it to plan an action at a specific time.
*   _message expiration_: messages could be dropped of a queue within some period of time without processing. You may need it to not process stale messages. Some transports do not support the feature.
*   _message priority_: message could be sent with higher priority, therefor being consumed faster. It violates first in first out concept and should be used with precautions. Some transports do not support the feature.
*   _first in first out_: messages are processed in the same order than they have entered the queue.

Lifecycle

A queuing system is divided in two main parts: producing and consuming. The [transport section of the Quick Start](https://php-enqueue.github.io/quick_tour/#transport) shows some code example for both parts.

Producing part

1.   The application creates a Context with a Connection factory
2.   The Context helps the application to create a Message
3.   The application gets a Producer from the Context
4.   The application uses the Producer to send the Message to the queue

Consuming part

1.   The application gets a Consumer from the Context
2.   The Consumer receives Messages from the queue
3.   The Consumer uses a Processor to process a Message
4.   The Processor returns a status (like `Interop\Queue\Processor::ACK`) to the Consumer
5.   The Consumer requeues or removes the Message from the queue depending on the Processor returned status

### [](https://php-enqueue.github.io/concepts/#consumption) Consumption

The consumption component is based on top of transport. The most important class is [QueueConsumer](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue/Consumption/QueueConsumer.php). Could be used with any queue interop compatible transport. It provides extension points which could be ad-hoc into processing flow. You can register [existing extensions](https://php-enqueue.github.io/consumption/extensions/) or write a custom one.

### [](https://php-enqueue.github.io/concepts/#client) Client

Enqueue Client is designed for as simple as possible developer experience. It provides high-level, very opinionated API. It manages all transport differences internally and even emulate missing features (like publish-subscribe). Please note: Client has own logic for naming transport destinations. Expect a different transport queue\topic name from the Client topic, command name. The prefix behavior could be disabled.

*   _Topic:_ Send a message to the topic when you want to notify several subscribers that something has happened. There is no way to get subscriber results. Uses the router internally to deliver messages.
*   _Command:_ guarantees that there is exactly one command processor\subscriber. Optionally, you can get a result. If there is no command subscriber an exception is thrown.
*   _Router:_ copy a message sent to the topic and duplicate it for every subscriber and send.
*   _Driver_ contains vendor specific logic.
*   _Producer_ is responsible for sending messages to the topic or command. It has nothing to do with transport’s producer.
*   _Message_ contains data to be sent. Please note that on consumer side you have to deal with transport message.
*   _Consumption:_ rely on consumption component.

[](https://php-enqueue.github.io/concepts/#how-to-use-enqueue) How to use Enqueue?
----------------------------------------------------------------------------------

There are different ways to use Enqueue: both reduce the boiler plate code you have to write to start using the Enqueue feature.

*   as a [Client](https://php-enqueue.github.io/client/quick_tour/): relies on a [DSN](https://php-enqueue.github.io/client/supported_brokers/) to connect
*   as a [Symfony Bundle](https://php-enqueue.github.io/symfony): recommended if you are using the Symfony framework

[back to index](https://php-enqueue.github.io/)
