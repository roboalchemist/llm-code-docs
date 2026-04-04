# Source: https://php-enqueue.github.io/transport/redis/

Title: Redis

URL Source: https://php-enqueue.github.io/transport/redis/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/transport/redis/#redis-transport) Redis transport
----------------------------------------------------------------------------------

The transport uses [Redis](https://redis.io/) as a message broker. It creates a collection (a queue or topic) there. Pushes messages to the tail of the collection and pops from the head. The transport works with [phpredis](https://github.com/phpredis/phpredis) php extension or [predis](https://github.com/nrk/predis) library. Make sure you installed either of them

Features:

*   Configure with DSN string
*   Delay strategies out of the box
*   Recovery&Redelivery support
*   Expiration support
*   Delaying support
*   Interchangeable with other Queue Interop implementations
*   Supports Subscription consumer

Parts:

*   [Installation](https://php-enqueue.github.io/transport/redis/#installation)
*   [Create context](https://php-enqueue.github.io/transport/redis/#create-context)
*   [Send message to topic](https://php-enqueue.github.io/transport/redis/#send-message-to-topic)
*   [Send message to queue](https://php-enqueue.github.io/transport/redis/#send-message-to-queue)
*   [Send expiration message](https://php-enqueue.github.io/transport/redis/#send-expiration-message)
*   [Send delayed message](https://php-enqueue.github.io/transport/redis/#send-delayed-message)
*   [Consume message](https://php-enqueue.github.io/transport/redis/#consume-message)
*   [Delete queue (purge messages)](https://php-enqueue.github.io/transport/redis/#delete-queue-purge-messages)
*   [Delete topic (purge messages)](https://php-enqueue.github.io/transport/redis/#delete-topic-purge-messages)
*   [Connect Heroku Redis](https://php-enqueue.github.io/transport/redis/#connect-heroku-redis)

[](https://php-enqueue.github.io/transport/redis/#installation) Installation
----------------------------------------------------------------------------

*   With php redis extension:

```
$ apt-get install php-redis
$ composer require enqueue/redis
```

*   With predis library:

```
$ composer require enqueue/redis predis/predis:^1
```

[](https://php-enqueue.github.io/transport/redis/#create-context) Create context
--------------------------------------------------------------------------------

*   With php redis extension:

```
<?php
use Enqueue\Redis\RedisConnectionFactory;

// connects to localhost
$factory = new RedisConnectionFactory();

// same as above
$factory = new RedisConnectionFactory('redis:');

// same as above
$factory = new RedisConnectionFactory([]);

// connect to Redis at example.com port 1000 using phpredis extension
$factory = new RedisConnectionFactory([
    'host' => 'example.com',
    'port' => 1000,
    'scheme_extensions' => ['phpredis'],
]);

// same as above but given as DSN string
$factory = new RedisConnectionFactory('redis+phpredis://example.com:1000');

$context = $factory->createContext();

// if you have enqueue/enqueue library installed you can use a factory to build context from DSN
$context = (new \Enqueue\ConnectionFactoryFactory())->create('redis:')->createContext();

// pass redis instance directly
$redis = new \Enqueue\Redis\PhpRedis([ /** redis connection options */ ]);
$redis->connect();

// Secure\TLS connection. Works only with predis library. Note second "S" in scheme.
$factory = new RedisConnectionFactory('rediss+predis://user:pass@host/0');

$factory = new RedisConnectionFactory($redis);
```

*   With predis library:

```
<?php
use Enqueue\Redis\RedisConnectionFactory;

$connectionFactory = new RedisConnectionFactory([
    'host' => 'localhost',
    'port' => 6379,
    'scheme_extensions' => ['predis'],
]);

$context = $connectionFactory->createContext();
```

*   With predis and custom [options](https://github.com/nrk/predis/wiki/Client-Options):

It gives you more control over vendor specific features.

```
<?php
use Enqueue\Redis\RedisConnectionFactory;
use Enqueue\Redis\PRedis;

$config = [
    'host' => 'localhost',
    'port' => 6379,
    'predis_options' => [
        'prefix'  => 'ns:'
    ]
];

$redis = new PRedis($config);

$factory = new RedisConnectionFactory($redis);
```

[](https://php-enqueue.github.io/transport/redis/#send-message-to-topic) Send message to topic
----------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Redis\RedisContext $context */

$fooTopic = $context->createTopic('aTopic');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooTopic, $message);
```

[](https://php-enqueue.github.io/transport/redis/#send-message-to-queue) Send message to queue
----------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Redis\RedisContext $context */

$fooQueue = $context->createQueue('aQueue');
$message = $context->createMessage('Hello world!');

$context->createProducer()->send($fooQueue, $message);
```

[](https://php-enqueue.github.io/transport/redis/#send-expiration-message) Send expiration message
--------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Redis\RedisContext $context */
/** @var \Enqueue\Redis\RedisDestination $fooQueue */

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setTimeToLive(60000) // 60 sec
    //
    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/redis/#send-delayed-message) Send delayed message
--------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Redis\RedisContext $context */
/** @var \Enqueue\Redis\RedisDestination $fooQueue */

$message = $context->createMessage('Hello world!');

$context->createProducer()
    ->setDeliveryDelay(5000) // 5 sec

    ->send($fooQueue, $message)
;
```

[](https://php-enqueue.github.io/transport/redis/#consume-message) Consume message:
-----------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Redis\RedisContext $context */

$fooQueue = $context->createQueue('aQueue');
$consumer = $context->createConsumer($fooQueue);

$message = $consumer->receive();

// process a message

$consumer->acknowledge($message);
//$consumer->reject($message);
```

[](https://php-enqueue.github.io/transport/redis/#delete-queue-purge-messages) Delete queue (purge messages):
-------------------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Redis\RedisContext $context */

$fooQueue = $context->createQueue('aQueue');

$context->deleteQueue($fooQueue);
```

[](https://php-enqueue.github.io/transport/redis/#delete-topic-purge-messages) Delete topic (purge messages):
-------------------------------------------------------------------------------------------------------------

```
<?php
/** @var \Enqueue\Redis\RedisContext $context */

$fooTopic = $context->createTopic('aTopic');

$context->deleteTopic($fooTopic);
```

[](https://php-enqueue.github.io/transport/redis/#connect-heroku-redis) Connect Heroku Redis
--------------------------------------------------------------------------------------------

[Heroku Redis](https://devcenter.heroku.com/articles/heroku-redis) describes how to setup Redis instance on Heroku. To use it with Enqueue Redis you have to pass REDIS_URL to RedisConnectionFactory constructor.

```
<?php

// REDIS_URL: redis://h:asdfqwer1234asdf@ec2-111-1-1-1.compute-1.amazonaws.com:111

$connection = new \Enqueue\Redis\RedisConnectionFactory(getenv('REDIS_URL'));
```

[back to index](https://php-enqueue.github.io/)
