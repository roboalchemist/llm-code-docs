# Source: https://php-enqueue.github.io/transport/stomp/

Title: STOMP

URL Source: https://php-enqueue.github.io/transport/stomp/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/stomp/#stomp-transport) STOMP transport
----------------------------------------------------------------------------------

*   [Installation](https://php-enqueue.github.io/transport/stomp/#installation)
*   [Create context](https://php-enqueue.github.io/transport/stomp/#create-context)
*   [Send message to topic](https://php-enqueue.github.io/transport/stomp/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/stomp/#send-message-to-queue)
*   [Consume message](https://php-enqueue.github.io/transport/stomp/#consume-message)

[](https://php-enqueue.github.io/transport/stomp/#installation) Installation
----------------------------------------------------------------------------

```
$ composer require enqueue/stomp
```

[](https://php-enqueue.github.io/transport/stomp/#create-context) Create context
--------------------------------------------------------------------------------

```
<?php
use Enqueue\Stomp\StompConnectionFactory;

// connects to localhost
$factory = new StompConnectionFactory();

// same as above
$factory = new StompConnectionFactory('stomp:');

// same as above
$factory = new StompConnectionFactory([]);

// connect via stomp to RabbitMQ (default) - the topic names are prefixed with /exchange
$factory = new StompConnectionFactory('stomp+rabbitmq:');

// connect via stomp to ActiveMQ - the topic names are prefixed with /topic
$factory = new StompConnectionFactory('stomp+activemq:');

// connect to stomp broker at example.com port 1000 using
$factory = new StompConnectionFactory([
    'host' => 'example.com',
    'port' => 1000,
    'login' => 'theLogin',
]);

// same as above but given as DSN string
$factory = new StompConnectionFactory('stomp://example.com:1000?login=theLogin');

$context = $factory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('stomp:')->createContext();
```

[](https://php-enqueue.github.io/transport/stomp/#send-message-to-topic) Send message to topic
----------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Stomp\StompContext $context */

$message = $context->createMessage('Hello world!');

$fooTopic = $context->createTopic('foo');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/stomp/#send-message-to-queue) Send message to queue
----------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Stomp\StompContext $context */

$message = $context->createMessage('Hello world!');

$fooQueue = $context->createQueue('foo');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/stomp/#consume-message) Consume message:
-----------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Stomp\StompContext $context */

$fooQueue = $context->createQueue('foo');

$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive();

// process a message

$consumer->acknowledge($message);
// $consumer->reject($message);
```

[back to index](https://php-enqueue.github.io/transport)
