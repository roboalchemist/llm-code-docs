# Source: https://php-enqueue.github.io/transport/amqp_lib/

Title: AMQP Lib

URL Source: https://php-enqueue.github.io/transport/amqp_lib/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/amqp_lib/#amqp-transport) AMQP transport
-----------------------------------------------------------------------------------

Implements [AMQP specifications](https://www.rabbitmq.com/specification.html) and implements [amqp interop](https://github.com/queue-interop/amqp-interop) interfaces. Build on top of [php amqp lib](https://github.com/php-amqplib/php-amqplib).

Features:

*   Configure with DSN string
*   Delay strategies out of the box
*   Interchangeable with other AMQP Interop implementations
*   Fixes AMQPIOWaitException when signal is sent.
*   More reliable heartbeat implementations.
*   Supports Subscription consumer

Parts:

*   [Installation](https://php-enqueue.github.io/transport/amqp_lib/#installation)
*   [Create context](https://php-enqueue.github.io/transport/amqp_lib/#create-context)
*   [Declare topic](https://php-enqueue.github.io/transport/amqp_lib/#declare-topic)
*   [Declare queue](https://php-enqueue.github.io/transport/amqp_lib/#decalre-queue)
*   [Bind queue to topic](https://php-enqueue.github.io/transport/amqp_lib/#bind-queue-to-topic)
*   [Send message to topic](https://php-enqueue.github.io/transport/amqp_lib/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/amqp_lib/#send-message-to-queue)
*   [Send priority message](https://php-enqueue.github.io/transport/amqp_lib/#send-priority-message)
*   [Send expiration message](https://php-enqueue.github.io/transport/amqp_lib/#send-expiration-message)
*   [Send delayed message](https://php-enqueue.github.io/transport/amqp_lib/#send-delayed-message)
*   [Consume message](https://php-enqueue.github.io/transport/amqp_lib/#consume-message)
*   [Subscription consumer](https://php-enqueue.github.io/transport/amqp_lib/#subscription-consumer)
*   [Purge queue messages](https://php-enqueue.github.io/transport/amqp_lib/#purge-queue-messages)
*   [Long running task and heartbeat and timeouts](https://php-enqueue.github.io/transport/amqp_lib/#long-running-task-and-heartbeat-and-timeouts)

[](https://php-enqueue.github.io/transport/amqp_lib/#installation) Installation
-------------------------------------------------------------------------------

```
$ composer require enqueue/amqp-lib
```

[](https://php-enqueue.github.io/transport/amqp_lib/#create-context) Create context
-----------------------------------------------------------------------------------

```
<?php
use Enqueue\AmqpLib\AmqpConnectionFactory;

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

// SSL or secure connection
$factory = new AmqpConnectionFactory([
    'dsn' => 'amqps:',
    'ssl_cacert' => '/path/to/cacert.pem',
    'ssl_cert' => '/path/to/cert.pem',
    'ssl_key' => '/path/to/key.pem',
]);

$context = $factory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('amqp:')->createContext();
$context = (new \Enqueue\ConnectionFactoryFactory())->create('amqp+lib:')->createContext();
```

[](https://php-enqueue.github.io/transport/amqp_lib/#declare-topic) Declare topic.
----------------------------------------------------------------------------------

Declare topic operation creates a topic on a broker side.

```
<?php
use Interop\Amqp\AmqpTopic;

/** @var \Enqueue\AmqpLib\AmqpContext $context */

$fooTopic = $context->createTopic('foo');
$fooTopic->setType(AmqpTopic::TYPE_FANOUT);
$context->declareTopic($fooTopic);

// to remove topic use delete topic method
//$context->deleteTopic($fooTopic);
```

[](https://php-enqueue.github.io/transport/amqp_lib/#declare-queue) Declare queue.
----------------------------------------------------------------------------------

Declare queue operation creates a queue on a broker side.

```
<?php
use Interop\Amqp\AmqpQueue;

/** @var \Enqueue\AmqpLib\AmqpContext $context */

$fooQueue = $context->createQueue('foo');
$fooQueue->addFlag(AmqpQueue::FLAG_DURABLE);
$context->declareQueue($fooQueue);

// to remove topic use delete queue method
//$context->deleteQueue($fooQueue);
```

[](https://php-enqueue.github.io/transport/amqp_lib/#bind-queue-to-topic) Bind queue to topic
---------------------------------------------------------------------------------------------

Connects a queue to the topic. So messages from that topic comes to the queue and could be processed.

```
<?php
use Interop\Amqp\Impl\AmqpBind;

/** @var \Enqueue\AmqpLib\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */
/** @var \Interop\Amqp\Impl\AmqpTopic $fooTopic */

$context->bind(new AmqpBind($fooTopic, $fooQueue));
```

[](https://php-enqueue.github.io/transport/amqp_lib/#send-message-to-topic) Send message to topic
-------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpLib\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpTopic $fooTopic */

$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/amqp_lib/#send-message-to-queue) Send message to queue
-------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpLib\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/amqp_lib/#send-priority-message) Send priority message
-------------------------------------------------------------------------------------------------

```
<?php
use Interop\Amqp\AmqpQueue;

/** @var \Enqueue\AmqpLib\AmqpContext $context */

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

[](https://php-enqueue.github.io/transport/amqp_lib/#send-expiration-message) Send expiration message
-----------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpLib\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setTimeToLive(60000) // 60 sec
    //
    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/amqp_lib/#send-delayed-message) Send delayed message
-----------------------------------------------------------------------------------------------

AMQP specification says nothing about message delaying hence the producer throws `DeliveryDelayNotSupportedException`. Though the producer (and the context) accepts a delivery delay strategy and if it is set it uses it to send delayed message. The `enqueue/amqp-tools` package provides two RabbitMQ delay strategies, to use them you have to install that package

```
<?php
use Enqueue\AmqpTools\RabbitMqDlxDelayStrategy;

/** @var \Enqueue\AmqpLib\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

// make sure you run "composer require enqueue/amqp-tools".

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setDelayStrategy(new RabbitMqDlxDelayStrategy())
    ->setDeliveryDelay(5000) // 5 sec

    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/amqp_lib/#consume-message) Consume message:
--------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpLib\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive();

// process a message

$consumer->acknowledge($message);
// $consumer->reject($message);
```

[](https://php-enqueue.github.io/transport/amqp_lib/#subscription-consumer) Subscription consumer
-------------------------------------------------------------------------------------------------

```
<?php
use Interop\Queue\Message;
use Interop\Queue\Consumer;

/** @var \Enqueue\AmqpLib\AmqpContext $context */
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

[](https://php-enqueue.github.io/transport/amqp_lib/#purge-queue-messages) Purge queue messages:
------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\AmqpLib\AmqpContext $context */
/** @var \Interop\Amqp\Impl\AmqpQueue $fooQueue */

$queue = $context->createQueue('aQueue');

$context->purgeQueue($queue);
```

[](https://php-enqueue.github.io/transport/amqp_lib/#long-running-task-and-heartbeat-and-timeouts) Long running task and heartbeat and timeouts
-----------------------------------------------------------------------------------------------------------------------------------------------

AMQP relies on heartbeat feature to make sure consumer is still there. Basically consumer is expected to send heartbeat frames from time to time to RabbitMQ broker so the broker does not close the connection. It is not possible to implement heartbeat feature in PHP, due to its synchronous nature. You could read more about the issues in post: [Keeping RabbitMQ connections alive in PHP](https://blog.mollie.com/keeping-rabbitmq-connections-alive-in-php-b11cb657d5fb).

`enqueue/amqp-lib` address the issue by registering heartbeat call as a [tick callbacks](http://php.net/manual/en/function.register-tick-function.php). To make it work you have to wrapp your long running task by `declare(ticks=1) {}`. The number of ticks could be adjusted to your needs. Calling it at every tick is not good.

Please note that it does not fix heartbeat issue if you spent most of the time on IO operation.

Example:

```
<?php

use Enqueue\AmqpLib\AmqpConnectionFactory;
use Interop\Amqp\AmqpConsumer;
use Interop\Amqp\AmqpMessage;

$context = (new AmqpConnectionFactory('amqp:?heartbeat_on_tick=1'))->createContext();

$queue = $context->createQueue('a_queue');
$consumer = $context->createConsumer($queue);

$subscriptionConsumer = $context->createSubscriptionConsumer();
$subscriptionConsumer->subscribe($consumer, function(AmqpMessage $message, AmqpConsumer $consumer) {
    // ticks number should be adjusted.
    declare(ticks=1) {
        foreach (fetchHugeSet() as $item) {
            // cycle does something for a long time, much longer than amqp heartbeat.
        }
    }

    $consumer->acknowledge($message);

    return true;
});

$subscriptionConsumer->consume(10000);

function fetchHugeSet(): array {};
```

Fixes partly `Invalid frame type 65` issue.

```
Error: Uncaught PhpAmqpLib\Exception\AMQPRuntimeException: Invalid frame type 65 in /some/path/vendor/php-amqplib/php-amqplib/PhpAmqpLib/Connection/AbstractConnection.php:528
```

Fixes partly `Broken pipe or closed connection` issue.

```
PHP Fatal error: Uncaught exception 'PhpAmqpLib\Exception\AMQPRuntimeException' with message 'Broken pipe or closed connection' in /some/path/vendor/php-amqplib/php-amqplib/PhpAmqpLib/Wire/IO/StreamIO.php:190
```

[back to index](https://php-enqueue.github.io/)
