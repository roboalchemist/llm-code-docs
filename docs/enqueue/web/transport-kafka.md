# Source: https://php-enqueue.github.io/transport/kafka/

Title: Kafka

URL Source: https://php-enqueue.github.io/transport/kafka/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/kafka/#kafka-transport) Kafka transport
----------------------------------------------------------------------------------

The transport uses [Kafka](https://kafka.apache.org/) streaming platform as a MQ broker.

*   [Installation](https://php-enqueue.github.io/transport/kafka/#installation)
*   [Create context](https://php-enqueue.github.io/transport/kafka/#create-context)
*   [Send message to topic](https://php-enqueue.github.io/transport/kafka/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/kafka/#send-message-to-queue)
*   [Consume message](https://php-enqueue.github.io/transport/kafka/#consume-message)
*   [Serialize message](https://php-enqueue.github.io/transport/kafka/#serialize-message)
*   [Change offset](https://php-enqueue.github.io/transport/kafka/#change-offset)

[](https://php-enqueue.github.io/transport/kafka/#installation) Installation
----------------------------------------------------------------------------

```
$ composer require enqueue/rdkafka
```

[](https://php-enqueue.github.io/transport/kafka/#create-context) Create context
--------------------------------------------------------------------------------

```
<?php
use Enqueue\RdKafka\RdKafkaConnectionFactory;

// connects to localhost:9092
$connectionFactory = new RdKafkaConnectionFactory();

// same as above
$connectionFactory = new RdKafkaConnectionFactory('kafka:');

// same as above
$connectionFactory = new RdKafkaConnectionFactory([]);

// connect to Kafka broker at example.com:1000 plus custom options
$connectionFactory = new RdKafkaConnectionFactory([
    'global' => [
        'group.id' => uniqid('', true),
        'metadata.broker.list' => 'example.com:1000',
        'enable.auto.commit' => 'false',
    ],
    'topic' => [
        'auto.offset.reset' => 'beginning',
    ],
]);

$context = $connectionFactory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('kafka:')->createContext();
```

[](https://php-enqueue.github.io/transport/kafka/#send-message-to-topic) Send message to topic
----------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\RdKafka\RdKafkaContext $context */

$message = $context->createMessage('Hello world!');

$fooTopic = $context->createTopic('foo');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/kafka/#send-message-to-queue) Send message to queue
----------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\RdKafka\RdKafkaContext $context */

$message = $context->createMessage('Hello world!');

$fooQueue = $context->createQueue('foo');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/kafka/#consume-message) Consume message:
-----------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\RdKafka\RdKafkaContext $context */

$fooQueue = $context->createQueue('foo');

$consumer = $context->createConsumer($fooQueue);

// Enable async commit to gain better performance (true by default since version 0.9.9).
//$consumer->setCommitAsync(true);

$message = $consumer->receive();

// process a message

$consumer->acknowledge($message);
// $consumer->reject($message);
```

[](https://php-enqueue.github.io/transport/kafka/#serialize-message) Serialize message
--------------------------------------------------------------------------------------

By default the transport serializes messages to json format but you might want to use another format such as [Apache Avro](https://avro.apache.org/docs/1.2.0/). For that you have to implement Serializer interface and set it to the context, producer or consumer. If a serializer set to context it will be injected to all consumers and producers created by the context.

```
<?php
use Enqueue\RdKafka\Serializer;
use Enqueue\RdKafka\RdKafkaMessage;

class FooSerializer implements Serializer
{
    public function toMessage($string) {}

    public function toString(RdKafkaMessage $message) {}
}

/** @var \Enqueue\RdKafka\RdKafkaContext $context */

$context->setSerializer(new FooSerializer());
```

[](https://php-enqueue.github.io/transport/kafka/#change-offset) Change offset
------------------------------------------------------------------------------

By default consumers starts from the beginning of the topic and updates the offset while you are processing messages. There is an ability to change the current offset.

```
<?php
/** @var \Enqueue\RdKafka\RdKafkaContext $context */

$fooQueue = $context->createQueue('foo');

$consumer = $context->createConsumer($fooQueue);
$consumer->setOffset(123);

$message = $consumer->receive(2000);
```

[](https://php-enqueue.github.io/transport/kafka/#usage-with-symfony-bundle) Usage with Symfony bundle
------------------------------------------------------------------------------------------------------

Set your enqueue to use rdkafka as your transport

```
# app/config/config.yml

enqueue:
    default:
        transport: "rdkafka:"
        client: ~
```

You can also you extended configuration to pass additional options, if you don’t want to pass them via DSN string or need to pass specific options. Since rdkafka uses librdkafka (being basically a wrapper around it) most configuration options are identical to those found at https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md.

```
# app/config/config.yml

enqueue:
    default:
        transport:
            dsn: "rdkafka://"
            global:
                ### Make sure this is unique for each application / consumer group and does not change
                ### Otherwise, Kafka won't be able to track your last offset and will always start according to
                ### `auto.offset.reset` setting.
                ### See Kafka documentation regarding `group.id` property if you want to know more
                group.id: 'foo-app'
                metadata.broker.list: 'example.com:1000'
            topic:
                auto.offset.reset: beginning
            ### Commit async is true by default since version 0.9.9.
            ### It is suggested to set it to true in earlier versions since otherwise consumers become extremely slow,
            ### waiting for offset to be stored on Kafka before continuing.
            commit_async: true
        client: ~
```

[back to index](https://php-enqueue.github.io/transport)
