# Source: https://php-enqueue.github.io/transport/mongodb/

Title: MongoDB

URL Source: https://php-enqueue.github.io/transport/mongodb/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/mongodb/#enqueue-mongodb-message-queue-transport) Enqueue Mongodb message queue transport
------------------------------------------------------------------------------------------------------------------------------------

Allows to use [MongoDB](https://www.mongodb.com/) as a message queue broker.

*   [Installation](https://php-enqueue.github.io/transport/mongodb/#installation)
*   [Create context](https://php-enqueue.github.io/transport/mongodb/#create-context)
*   [Send message to topic](https://php-enqueue.github.io/transport/mongodb/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/mongodb/#send-message-to-queue)
*   [Send priority message](https://php-enqueue.github.io/transport/mongodb/#send-priority-message)
*   [Send expiration message](https://php-enqueue.github.io/transport/mongodb/#send-expiration-message)
*   [Send delayed message](https://php-enqueue.github.io/transport/mongodb/#send-delayed-message)
*   [Consume message](https://php-enqueue.github.io/transport/mongodb/#consume-message)
*   [Subscription consumer](https://php-enqueue.github.io/transport/mongodb/#subscription-consumer)

[](https://php-enqueue.github.io/transport/mongodb/#installation) Installation
------------------------------------------------------------------------------

```
$ composer require enqueue/mongodb
```

[](https://php-enqueue.github.io/transport/mongodb/#create-context) Create context
----------------------------------------------------------------------------------

```
<?php
use Enqueue\Mongodb\MongodbConnectionFactory;

// connects to localhost
$connectionFactory = new MongodbConnectionFactory();

// same as above
$factory = new MongodbConnectionFactory('mongodb:');

// same as above
$factory = new MongodbConnectionFactory([]);

$factory = new MongodbConnectionFactory([
    'dsn' => 'mongodb://localhost:27017/db_name',
    'dbname' => 'enqueue',
    'collection_name' => 'enqueue',
    'polling_interval' => '1000',
]);

$context = $factory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('mongodb:')->createContext();
```

[](https://php-enqueue.github.io/transport/mongodb/#send-message-to-topic) Send message to topic
------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Mongodb\MongodbContext $context */
/** @var \Enqueue\Mongodb\MongodbDestination $fooTopic */

$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/mongodb/#send-message-to-queue) Send message to queue
------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Mongodb\MongodbContext $context */
/** @var \Enqueue\Mongodb\MongodbDestination $fooQueue */

$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/mongodb/#send-priority-message) Send priority message
------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Mongodb\MongodbContext $context */

$fooQueue = $context->createQueue('foo');

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setPriority(5) // the higher priority the sooner a message gets to a consumer
    //
    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/mongodb/#send-expiration-message) Send expiration message
----------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Mongodb\MongodbContext $context */
/** @var \Enqueue\Mongodb\MongodbDestination $fooQueue */

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setTimeToLive(60000) // 60 sec
    //
    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/mongodb/#send-delayed-message) Send delayed message
----------------------------------------------------------------------------------------------

```
<?php
use Enqueue\AmqpTools\RabbitMqDlxDelayStrategy;

/** @var \Enqueue\Mongodb\MongodbContext $context */
/** @var \Enqueue\Mongodb\MongodbDestination $fooQueue */

// make sure you run "composer require enqueue/amqp-tools".

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setDeliveryDelay(5000) // 5 sec

    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/mongodb/#consume-message) Consume message:
-------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Mongodb\MongodbContext $context */
/** @var \Enqueue\Mongodb\MongodbDestination $fooQueue */

$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive();

// process a message

$consumer->acknowledge($message);
// $consumer->reject($message);
```

[](https://php-enqueue.github.io/transport/mongodb/#subscription-consumer) Subscription consumer
------------------------------------------------------------------------------------------------

```
<?php
use Interop\Queue\Message;
use Interop\Queue\Consumer;

/** @var \Enqueue\Mongodb\MongodbContext $context */
/** @var \Enqueue\Mongodb\MongodbDestination $fooQueue */
/** @var \Enqueue\Mongodb\MongodbDestination $barQueue */

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

[back to index](https://php-enqueue.github.io/)
