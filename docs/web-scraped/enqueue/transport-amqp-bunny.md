# Source: https://php-enqueue.github.io/transport/amqp_bunny/

Title: AMQP Bunny

URL Source: https://php-enqueue.github.io/transport/amqp_bunny/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/amqp_bunny/#amqp-transport) AMQP transport
-------------------------------------------------------------------------------------

Implements [AMQP specifications](https://www.rabbitmq.com/specification.html) and implements [amqp interop](https://github.com/queue-interop/amqp-interop) interfaces. Build on top of [bunny lib](https://github.com/jakubkulhan/bunny).

*   [Installation](https://php-enqueue.github.io/transport/amqp_bunny/#installation)
*   [Create context](https://php-enqueue.github.io/transport/amqp_bunny/#create-context)
*   [Declare topic](https://php-enqueue.github.io/transport/amqp_bunny/#declare-topic)
*   [Declare queue](https://php-enqueue.github.io/transport/amqp_bunny/#declare-queue)
*   [Bind queue to topic](https://php-enqueue.github.io/transport/amqp_bunny/#bind-queue-to-topic)
*   [Send message to topic](https://php-enqueue.github.io/transport/amqp_bunny/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/amqp_bunny/#send-message-to-queue)
*   [Send priority message](https://php-enqueue.github.io/transport/amqp_bunny/#send-priority-message)
*   [Send expiration message](https://php-enqueue.github.io/transport/amqp_bunny/#send-expiration-message)
*   [Send delayed message](https://php-enqueue.github.io/transport/amqp_bunny/#send-delayed-message)
*   [Consume message](https://php-enqueue.github.io/transport/amqp_bunny/#consume-message)
*   [Subscription consumer](https://php-enqueue.github.io/transport/amqp_bunny/#subscription-consumer)
*   [Purge queue messages](https://php-enqueue.github.io/transport/amqp_bunny/#purge-queue-messages)

[](https://php-enqueue.github.io/transport/amqp_bunny/#installation) Installation
---------------------------------------------------------------------------------

```
$ composer require enqueue/amqp-bunny
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#create-context) Create context
-------------------------------------------------------------------------------------

```
<?php
use Enqueue\AmqpBunny\AmqpConnectionFactory;

// connects to localhost
$factory = new AmqpConnectionFactory();

// same as above
$factory = new AmqpConnectionFactory('amqp:');

// same as above
$factory = new AmqpConnectionFactory([]);

// connect to AMQP broker at example.com
$factory = new AmqpConnectionFactory([
    'host' => 'example.com',
    'port' => 1000,
    'vhost' => '/',
    'user' => 'user',
    'pass' => 'pass',
    'persisted' => false,
]);

// same as above but given as DSN string
$factory = new AmqpConnectionFactory('amqp://user:pass@example.com:10000/%2f');

$context = $factory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('amqp:')->createContext();
$context = (new \Enqueue\ConnectionFactoryFactory())->create('amqp+bunny:')->createContext();
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#declare-topic) Declare topic.
------------------------------------------------------------------------------------

Declare topic operation creates a topic on a broker side.

```
<?php
use Interop\Amqp\AmqpTopic;

/** @var \Enqueue\AmqpBunny\AmqpContext $context */

$fooTopic = $context->createTopic('foo');
$fooTopic->setType(AmqpTopic::TYPE_FANOUT);
$context->declareTopic($fooTopic);

// to remove topic use delete topic method
//$context->deleteTopic($fooTopic);
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#declare-queue) Declare queue.
------------------------------------------------------------------------------------

Declare queue operation creates a queue on a broker side.

```
<?php
use Interop\Amqp\AmqpQueue;

/** @var \Enqueue\AmqpBunny\AmqpContext $context */

$fooQueue = $context->createQueue('foo');
$fooQueue->addFlag(AmqpQueue::FLAG_DURABLE);
$context->declareQueue($fooQueue);

// to remove topic use delete queue method
//$context->deleteQueue($fooQueue);
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#bind-queue-to-topic) Bind queue to topic
-----------------------------------------------------------------------------------------------

Connects a queue to the topic. So messages from that topic comes to the queue and could be processed.

```
<?php
use Interop\Amqp\Impl\AmqpBind;

/** @var \Enqueue\AmqpBunny\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */
/** @var \Interop\Amqp\Impl\AmqpTopic $fooTopic */

$context->bind(new AmqpBind($fooTopic, $fooQueue));
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#send-message-to-topic) Send message to topic
---------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpBunny\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpTopic $fooTopic */

$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#send-message-to-queue) Send message to queue
---------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpBunny\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#send-priority-message) Send priority message
---------------------------------------------------------------------------------------------------

```
<?php
use Interop\Amqp\AmqpQueue;

/** @var \Enqueue\AmqpBunny\AmqpContext $context */

$fooQueue = $context->createQueue('foo');
$fooQueue->addFlag(AmqpQueue::FLAG_DURABLE);
$fooQueue->setArguments(['x-max-priority' => 10]);
$context->declareQueue($fooQueue);

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setPriority(5) // the higher priority the sooner a message gets to a consumer
    //
    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#send-expiration-message) Send expiration message
-------------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpBunny\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setTimeToLive(60000) // 60 sec
    //
    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#send-delayed-message) Send delayed message
-------------------------------------------------------------------------------------------------

AMQP specification says nothing about message delaying hence the producer throws `DeliveryDelayNotSupportedException`. Though the producer (and the context) accepts a delivery delay strategy and if it is set it uses it to send delayed message. The `enqueue/amqp-tools` package provides two RabbitMQ delay strategies, to use them you have to install that package

```
<?php
use Enqueue\AmqpTools\RabbitMqDlxDelayStrategy;

/** @var \Enqueue\AmqpBunny\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

// make sure you run "composer require enqueue/amqp-tools".

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setDelayStrategy(new RabbitMqDlxDelayStrategy())
    ->setDeliveryDelay(5000) // 5 sec

    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#consume-message) Consume message:
----------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpBunny\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive();

// process a message

$consumer->acknowledge($message);
// $consumer->reject($message);
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#subscription-consumer) Subscription consumer
---------------------------------------------------------------------------------------------------

```
<?php
use Interop\Queue\Message;
use Interop\Queue\Consumer;

/** @var \Enqueue\AmqpBunny\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */
/** @var \Interop\Amqp\Impl\AmqpQueue $barQueue */

$fooConsumer = $context->createConsumer($fooQueue);
$barConsumer = $context->createConsumer($barQueue);

$subscriptionConsumer = $context->createSubscriptionConsumer();
$subscriptionConsumer->subscribe($fooConsumer, function(Message $message, Consumer $consumer) {
    // process message

    $consumer->acknowledge($message);

    return true;
});
$subscriptionConsumer->subscribe($barConsumer, function(Message $message, Consumer $consumer) {
    // process message

    $consumer->acknowledge($message);

    return true;
});

$subscriptionConsumer->consume(2000); // 2 sec
```

[](https://php-enqueue.github.io/transport/amqp_bunny/#purge-queue-messages) Purge queue messages:
--------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpBunny\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

$queue = $context->createQueue('aQueue');

$context->purgeQueue($queue);
```

[back to index](https://php-enqueue.github.io/)
