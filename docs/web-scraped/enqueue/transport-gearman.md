# Source: https://php-enqueue.github.io/transport/gearman/

Title: Gearman

URL Source: https://php-enqueue.github.io/transport/gearman/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/gearman/#gearman-transport) Gearman transport
----------------------------------------------------------------------------------------

The transport uses [Gearman](http://gearman.org/) job manager. The transport uses [Gearman PHP extension](http://php.net/manual/en/book.gearman.php) internally.

*   [Installation](https://php-enqueue.github.io/transport/gearman/#installation)
*   [Create context](https://php-enqueue.github.io/transport/gearman/#create-context)
*   [Send message to topic](https://php-enqueue.github.io/transport/gearman/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/gearman/#send-message-to-queue)
*   [Consume message](https://php-enqueue.github.io/transport/gearman/#consume-message)

[](https://php-enqueue.github.io/transport/gearman/#installation) Installation
------------------------------------------------------------------------------

```
$ composer require enqueue/gearman
```

[](https://php-enqueue.github.io/transport/gearman/#create-context) Create context
----------------------------------------------------------------------------------

```
<?php
use Enqueue\Gearman\GearmanConnectionFactory;

// connects to localhost:4730
$factory = new GearmanConnectionFactory();

// same as above
$factory = new GearmanConnectionFactory('gearman:');

// connects to example host and port 5555
$factory = new GearmanConnectionFactory('gearman://example:5555');

// same as above but configured by array
$factory = new GearmanConnectionFactory([
    'host' => 'example',
    'port' => 5555
]);

$context = $factory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('gearman:')->createContext();
```

[](https://php-enqueue.github.io/transport/gearman/#send-message-to-topic) Send message to topic
------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Gearman\GearmanContext $context */

$fooTopic = $context->createTopic('aTopic');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/gearman/#send-message-to-queue) Send message to queue
------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Gearman\GearmanContext $context */

$fooQueue = $context->createQueue('aQueue');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/gearman/#consume-message) Consume message:
-------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Gearman\GearmanContext $context */

$fooQueue = $context->createQueue('aQueue');
$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive(2000); // wait for 2 seconds

$message = $consumer->receiveNoWait(); // fetch message or return null immediately

// process a message

$consumer->acknowledge($message);
// $consumer->reject($message);
```

[back to index](https://php-enqueue.github.io/)
