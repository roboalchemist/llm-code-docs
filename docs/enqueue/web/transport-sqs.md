# Source: https://php-enqueue.github.io/transport/sqs/

Title: Amazon SQS

URL Source: https://php-enqueue.github.io/transport/sqs/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/sqs/#amazon-sqs-transport) Amazon SQS transport
------------------------------------------------------------------------------------------

A transport for [Amazon SQS](https://aws.amazon.com/sqs/) broker. It uses internally official [aws sdk library](https://packagist.org/packages/aws/aws-sdk-php)

*   [Installation](https://php-enqueue.github.io/transport/sqs/#installation)
*   [Create context](https://php-enqueue.github.io/transport/sqs/#create-context)
*   [Declare queue](https://php-enqueue.github.io/transport/sqs/#decalre-queue)
*   [Send message to queue](https://php-enqueue.github.io/transport/sqs/#send-message-to-queue)
*   [Send delay message](https://php-enqueue.github.io/transport/sqs/#send-delay-message)
*   [Consume message](https://php-enqueue.github.io/transport/sqs/#consume-message)
*   [Purge queue messages](https://php-enqueue.github.io/transport/sqs/#purge-queue-messages)
*   [Queue from another AWS account](https://php-enqueue.github.io/transport/sqs/#queue-from-another-aws-account)

[](https://php-enqueue.github.io/transport/sqs/#installation) Installation
--------------------------------------------------------------------------

```
$ composer require enqueue/sqs
```

[](https://php-enqueue.github.io/transport/sqs/#create-context) Create context
------------------------------------------------------------------------------

```
<?php
use Enqueue\Sqs\SqsConnectionFactory;

$factory = new SqsConnectionFactory([
    'key' => 'aKey',
    'secret' => 'aSecret',
    'region' => 'aRegion',
]);

// same as above but given as DSN string. You may need to url encode secret if it contains special char (like +)
$factory = new SqsConnectionFactory('sqs:?key=aKey&secret=aSecret&region=aRegion');

$context = $factory->createContext();

// using a pre-configured client
$client = new Aws\Sqs\SqsClient([ /* ... */ ]);
$factory = new SqsConnectionFactory($client);

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('sqs:')->createContext();
```

[](https://php-enqueue.github.io/transport/sqs/#declare-queue) Declare queue.
-----------------------------------------------------------------------------

Declare queue operation creates a queue on a broker side.

```
<?php
/** @var \Enqueue\Sqs\SqsContext $context */

$fooQueue = $context->createQueue('foo');
$context->declareQueue($fooQueue);

// to remove queue use deleteQueue method
//$context->deleteQueue($fooQueue);
```

[](https://php-enqueue.github.io/transport/sqs/#send-message-to-queue) Send message to queue
--------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Sqs\SqsContext $context */

$fooQueue = $context->createQueue('foo');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/sqs/#send-delay-message) Send delay message
--------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Sqs\SqsContext $context */

$fooQueue = $context->createQueue('foo');
$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setDeliveryDelay(60000) // 60 sec

    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/sqs/#consume-message) Consume message:
---------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Sqs\SqsContext $context */

$fooQueue = $context->createQueue('foo');
$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive();

// process a message

$consumer->acknowledge($message);
// $consumer->reject($message);
```

[](https://php-enqueue.github.io/transport/sqs/#purge-queue-messages) Purge queue messages:
-------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Sqs\SqsContext $context */

$fooQueue = $context->createQueue('foo');

$context->purgeQueue($fooQueue);
```

[](https://php-enqueue.github.io/transport/sqs/#queue-from-another-aws-account) Queue from another AWS account
--------------------------------------------------------------------------------------------------------------

SQS allows to use queues from another account. You could set it globally for all queues via option `queue_owner_aws_account_id` or per queue using `SqsDestination::setQueueOwnerAWSAccountId` method.

```
<?php
use Enqueue\Sqs\SqsConnectionFactory;

// globally for all queues
$factory = new SqsConnectionFactory('sqs:?queue_owner_aws_account_id=awsAccountId');

$context = (new SqsConnectionFactory('sqs:'))->createContext();

// per queue.
$queue = $context->createQueue('foo');
$queue->setQueueOwnerAWSAccountId('awsAccountId');
```

[](https://php-enqueue.github.io/transport/sqs/#multi-region-examples) Multi region examples
--------------------------------------------------------------------------------------------

Enqueue SQS provides a generic multi-region support. This enables users to specify which AWS Region to send a command to by setting region on SqsDestination. You might need it to access SQS FIFO queue because they are not available for all regions. If not specified the default region is used.

```
<?php
use Enqueue\Sqs\SqsConnectionFactory;

$context = (new SqsConnectionFactory('sqs:?region=eu-west-2'))->createContext();

$queue = $context->createQueue('foo');
$queue->setRegion('us-west-2');

// the request goes to US West (Oregon) Region
$context->declareQueue($queue);
```

[back to index](https://php-enqueue.github.io/)
