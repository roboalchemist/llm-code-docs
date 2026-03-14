# Source: https://php-enqueue.github.io/transport/wamp/

Title: WAMP

URL Source: https://php-enqueue.github.io/transport/wamp/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/wamp/#web-application-messaging-protocol-wamp-transport) Web Application Messaging Protocol (WAMP) Transport
-------------------------------------------------------------------------------------------------------------------------------------------------------

A transport for [Web Application Messaging Protocol](https://wamp-proto.org/). WAMP is an open standard WebSocket subprotocol. It uses internally Thruway PHP library [thruway/client](https://github.com/thruway/client)

*   [Installation](https://php-enqueue.github.io/transport/wamp/#installation)
*   [Start the WAMP router](https://php-enqueue.github.io/transport/wamp/#start-the-wamp-router)
*   [Create context](https://php-enqueue.github.io/transport/wamp/#create-context)
*   [Consume message](https://php-enqueue.github.io/transport/wamp/#consume-message)
*   [Subscription consumer](https://php-enqueue.github.io/transport/wamp/#subscription-consumer)
*   [Send message to topic](https://php-enqueue.github.io/transport/wamp/#send-message-to-topic)

[](https://php-enqueue.github.io/transport/wamp/#installation) Installation
---------------------------------------------------------------------------

```
$ composer require enqueue/wamp
```

[](https://php-enqueue.github.io/transport/wamp/#start-the-wamp-router) Start the WAMP router
---------------------------------------------------------------------------------------------

You can get a WAMP router with [Thruway](https://github.com/voryx/Thruway):

```
$ composer require voryx/thruway
$ php vendor/voryx/thruway/Examples/SimpleWsRouter.php
```

Thruway is now running on 127.0.0.1 port 9090

[](https://php-enqueue.github.io/transport/wamp/#create-context) Create context
-------------------------------------------------------------------------------

```
<?php
use Enqueue\Wamp\WampConnectionFactory;

$connectionFactory = new WampConnectionFactory();

// same as above
$connectionFactory = new WampConnectionFactory('wamp:');
$connectionFactory = new WampConnectionFactory('ws:');
$connectionFactory = new WampConnectionFactory('wamp://127.0.0.1:9090');

$context = $connectionFactory->createContext();
```

[](https://php-enqueue.github.io/transport/wamp/#consume-message) Consume message:
----------------------------------------------------------------------------------

Start message consumer before send message to the topic

```
<?php
/** @var \Enqueue\Wamp\WampContext $context */

$fooTopic = $context->createTopic('foo');

$consumer = $context->createConsumer($fooQueue);

while (true) {
    if ($message = $consumer->receive()) {
        // process a message
    }
}
```

[](https://php-enqueue.github.io/transport/wamp/#subscription-consumer) Subscription consumer
---------------------------------------------------------------------------------------------

```
<?php
use Interop\Queue\Message;
use Interop\Queue\Consumer;

/** @var \Enqueue\Wamp\WampContext $context */
/** @var \Enqueue\Wamp\WampDestination $fooQueue */
/** @var \Enqueue\Wamp\WampDestination $barQueue */

$fooConsumer = $context->createConsumer($fooQueue);
$barConsumer = $context->createConsumer($barQueue);

$subscriptionConsumer = $context->createSubscriptionConsumer();
$subscriptionConsumer->subscribe($fooConsumer, function(Message $message, Consumer $consumer) {
    // process message

    return true;
});
$subscriptionConsumer->subscribe($barConsumer, function(Message $message, Consumer $consumer) {
    // process message

    return true;
});

$subscriptionConsumer->consume(2000); // 2 sec
```

[](https://php-enqueue.github.io/transport/wamp/#send-message-to-topic) Send message to topic
---------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Wamp\WampContext $context */

$fooTopic = $context->createTopic('foo');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooTopic, $message);
```

[back to index](https://php-enqueue.github.io/)
