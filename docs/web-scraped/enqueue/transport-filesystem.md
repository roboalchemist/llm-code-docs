# Source: https://php-enqueue.github.io/transport/filesystem/

Title: Filesystem

URL Source: https://php-enqueue.github.io/transport/filesystem/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/filesystem/#filesystem-transport) Filesystem transport
-------------------------------------------------------------------------------------------------

Use files on local filesystem as queues. It creates a file per queue\topic. A message is a line inside the file. **Limitations** It works only in auto ack mode hence If consumer crashes the message is lost. Local by nature therefor messages are not visible on other servers.

*   [Installation](https://php-enqueue.github.io/transport/filesystem/#installation)
*   [Create context](https://php-enqueue.github.io/transport/filesystem/#create-context)
*   [Send message to topic](https://php-enqueue.github.io/transport/filesystem/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/filesystem/#send-message-to-queue)
*   [Send expiration message](https://php-enqueue.github.io/transport/filesystem/#send-expiration-message)
*   [Consume message](https://php-enqueue.github.io/transport/filesystem/#consume-message)
*   [Purge queue messages](https://php-enqueue.github.io/transport/filesystem/#purge-queue-messages)

[](https://php-enqueue.github.io/transport/filesystem/#installation) Installation
---------------------------------------------------------------------------------

```
$ composer require enqueue/fs
```

[](https://php-enqueue.github.io/transport/filesystem/#create-context) Create context
-------------------------------------------------------------------------------------

```
<?php
use Enqueue\Fs\FsConnectionFactory;

// stores messages in /tmp/enqueue folder
$connectionFactory = new FsConnectionFactory();

// same as above
$connectionFactory = new FsConnectionFactory('file:');

// stores in custom folder
$connectionFactory = new FsConnectionFactory('/path/to/queue/dir');

// same as above
$connectionFactory = new FsConnectionFactory('file:///path/to/queue/dir');

// with options
$connectionFactory = new FsConnectionFactory('file:///path/to/queue/dir?pre_fetch_count=1');

// as an array
$connectionFactory = new FsConnectionFactory([
    'path' => '/path/to/queue/dir',
    'pre_fetch_count' => 1,
]);

$context = $connectionFactory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('file:')->createContext();
```

[](https://php-enqueue.github.io/transport/filesystem/#send-message-to-topic) Send message to topic
---------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Fs\FsContext $context */

$fooTopic = $context->createTopic('aTopic');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/filesystem/#send-message-to-queue) Send message to queue
---------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Fs\FsContext $context */

$fooQueue = $context->createQueue('aQueue');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/filesystem/#send-expiration-message) Send expiration message
-------------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Fs\FsContext $context */

$fooQueue = $context->createQueue('aQueue');
$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setTimeToLive(60000) // 60 sec
    //
    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/filesystem/#consume-message) Consume message:
----------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Fs\FsContext $context */

$fooQueue = $context->createQueue('aQueue');
$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive();

// process a message

$consumer->acknowledge($message);
// $consumer->reject($message);
```

[](https://php-enqueue.github.io/transport/filesystem/#purge-queue-messages) Purge queue messages:
--------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Fs\FsContext $context */

$fooQueue = $context->createQueue('aQueue');

$context->purge($fooQueue);
```

[back to index](https://php-enqueue.github.io/)
