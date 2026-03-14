# Source: https://php-enqueue.github.io/transport/pheanstalk/

Title: Pheanstalk

URL Source: https://php-enqueue.github.io/transport/pheanstalk/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/pheanstalk/#beanstalk-pheanstalk-transport) Beanstalk (Pheanstalk) transport
-----------------------------------------------------------------------------------------------------------------------

The transport uses [Beanstalkd](http://kr.github.io/beanstalkd/) job manager. The transport uses [Pheanstalk](https://github.com/pda/pheanstalk) library internally.

*   [Installation](https://php-enqueue.github.io/transport/pheanstalk/#installation)
*   [Create context](https://php-enqueue.github.io/transport/pheanstalk/#create-context)
*   [Send message to topic](https://php-enqueue.github.io/transport/pheanstalk/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/pheanstalk/#send-message-to-queue)
*   [Consume message](https://php-enqueue.github.io/transport/pheanstalk/#consume-message)

[](https://php-enqueue.github.io/transport/pheanstalk/#installation) Installation
---------------------------------------------------------------------------------

```
$ composer require enqueue/pheanstalk
```

[](https://php-enqueue.github.io/transport/pheanstalk/#create-context) Create context
-------------------------------------------------------------------------------------

```
<?php
use Enqueue\Pheanstalk\PheanstalkConnectionFactory;

// connects to localhost:11300
$factory = new PheanstalkConnectionFactory();

// same as above
$factory = new PheanstalkConnectionFactory('beanstalk:');

// connects to example host and port 5555
$factory = new PheanstalkConnectionFactory('beanstalk://example:5555');

// same as above but configured by array
$factory = new PheanstalkConnectionFactory([
    'host' => 'example',
    'port' => 5555
]);

$context = $factory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('beanstalk:')->createContext();
```

[](https://php-enqueue.github.io/transport/pheanstalk/#send-message-to-topic) Send message to topic
---------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Pheanstalk\PheanstalkContext $context */

$fooTopic = $context->createTopic('aTopic');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/pheanstalk/#send-message-to-queue) Send message to queue
---------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Pheanstalk\PheanstalkContext $context */

$fooQueue = $context->createQueue('aQueue');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/pheanstalk/#consume-message) Consume message:
----------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Pheanstalk\PheanstalkContext $context */

$fooQueue = $context->createQueue('aQueue');
$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive(2000); // wait for 2 seconds

$message = $consumer->receiveNoWait(); // fetch message or return null immediately

// process a message

$consumer->acknowledge($message);
// $consumer->reject($message);
```

[back to index](https://php-enqueue.github.io/)
