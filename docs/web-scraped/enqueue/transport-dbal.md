# Source: https://php-enqueue.github.io/transport/dbal/

Title: DBAL

URL Source: https://php-enqueue.github.io/transport/dbal/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/dbal/#doctrine-dbal-transport) Doctrine DBAL transport
-------------------------------------------------------------------------------------------------

The transport uses [Doctrine DBAL](http://docs.doctrine-project.org/projects/doctrine-dbal/en/latest/) library and SQL like server as a broker. It creates a table there. Pushes and pops messages to\from that table.

*   [Installation](https://php-enqueue.github.io/transport/dbal/#installation)
*   [Init database](https://php-enqueue.github.io/transport/dbal/#init-database)
*   [Create context](https://php-enqueue.github.io/transport/dbal/#create-context)
*   [Send message to topic](https://php-enqueue.github.io/transport/dbal/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/dbal/#send-message-to-queue)
*   [Send expiration message](https://php-enqueue.github.io/transport/dbal/#send-expiration-message)
*   [Send delayed message](https://php-enqueue.github.io/transport/dbal/#send-delayed-message)
*   [Consume message](https://php-enqueue.github.io/transport/dbal/#consume-message)
*   [Subscription consumer](https://php-enqueue.github.io/transport/dbal/#subscription-consumer)

[](https://php-enqueue.github.io/transport/dbal/#installation) Installation
---------------------------------------------------------------------------

```
$ composer require enqueue/dbal
```

[](https://php-enqueue.github.io/transport/dbal/#create-context) Create context
-------------------------------------------------------------------------------

*   With config (a connection is created internally):

```
<?php
use Enqueue\Dbal\DbalConnectionFactory;

$factory = new DbalConnectionFactory('mysql://user:pass@localhost:3306/mqdev');

// connects to localhost
$factory = new DbalConnectionFactory('mysql:');

$context = $factory->createContext();
```

*   With existing connection:

```
<?php
use Enqueue\Dbal\ManagerRegistryConnectionFactory;
use Doctrine\Persistence\ManagerRegistry;

/** @var ManagerRegistry $registry */

$factory = new ManagerRegistryConnectionFactory($registry, [
    'connection_name' => 'default',
]);

$context = $factory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('mysql:')->createContext();
```

[](https://php-enqueue.github.io/transport/dbal/#init-database) Init database
-----------------------------------------------------------------------------

At first time you have to create a table where your message will live. There is a handy methods for this `createDataBaseTable` on the context. Please pay attention to that the database has to be created manually.

```
<?php
/** @var \Enqueue\Dbal\DbalContext $context */

$context->createDataBaseTable();
```

[](https://php-enqueue.github.io/transport/dbal/#send-message-to-topic) Send message to topic
---------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Dbal\DbalContext $context */

$fooTopic = $context->createTopic('aTopic');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/dbal/#send-message-to-queue) Send message to queue
---------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Dbal\DbalContext $context */

$fooQueue = $context->createQueue('aQueue');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/dbal/#send-expiration-message) Send expiration message
-------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Dbal\DbalContext $psrContext */
/** @var \Enqueue\Dbal\DbalDestination $fooQueue */

$message = $psrContext->createMessage('Hello world!');

$psrContext->createProducer()
    ->setTimeToLive(60000) // 60 sec
    //
    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/dbal/#send-delayed-message) Send delayed message
-------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Dbal\DbalContext $psrContext */
/** @var \Enqueue\Dbal\DbalDestination $fooQueue */

$message = $psrContext->createMessage('Hello world!');

$psrContext->createProducer()
    ->setDeliveryDelay(5000) // 5 sec
    //
    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/dbal/#consume-message) Consume message:
----------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Dbal\DbalContext $context */

$fooQueue = $context->createQueue('aQueue');
$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive();

// process a message

$consumer->acknowledge($message);
//$consumer->reject($message);
```

[](https://php-enqueue.github.io/transport/dbal/#subscription-consumer) Subscription consumer
---------------------------------------------------------------------------------------------

```
<?php
use Interop\Queue\Message;
use Interop\Queue\Consumer;

/** @var \Enqueue\Dbal\DbalContext $context */
/** @var \Enqueue\Dbal\DbalDestination $fooQueue */
/** @var \Enqueue\Dbal\DbalDestination $barQueue */

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
