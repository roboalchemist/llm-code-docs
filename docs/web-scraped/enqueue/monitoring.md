# Source: https://php-enqueue.github.io/monitoring/

Title: Monitoring

URL Source: https://php-enqueue.github.io/monitoring/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

Enqueue provides a tool for monitoring message queues. With it, you can control how many messages were sent, how many processed successfully or failed. How many consumers are working, their up time, processed messages stats, memory usage and system load. The tool could be integrated with virtually any analytics and monitoring platform. There are several integration:

*   [Datadog StatsD](https://datadoghq.com/)
*   [InfluxDB](https://www.influxdata.com/) and [Grafana](https://grafana.com/)
*   [WAMP (Web Application Messaging Protocol)](https://wamp-proto.org/) We are working on a JS\WAMP based real-time UI tool, for more information please [contact us](https://php-enqueue.github.io/monitoring/opensource@forma-pro.com).

![Image 1: Grafana Monitoring](https://php-enqueue.github.io/images/grafana_monitoring.jpg)

[contact us](mailto:opensource@forma-pro.com) if need a Grafana template such as on the picture.

*   [Installation](https://php-enqueue.github.io/monitoring/#installation)
*   [Track sent messages](https://php-enqueue.github.io/monitoring/#track-sent-messages)
*   [Track consumed message](https://php-enqueue.github.io/monitoring/#track-consumed-message)
*   [Track consumer metrics](https://php-enqueue.github.io/monitoring/#track-consumer-metrics)
*   [Consumption extension](https://php-enqueue.github.io/monitoring/#consumption-extension)
*   [Enqueue Client Extension](https://php-enqueue.github.io/monitoring/#enqueue-client-extension)
*   [InfluxDB Storage](https://php-enqueue.github.io/monitoring/#influxdb-storage)
*   [Datadog Storage](https://php-enqueue.github.io/monitoring/#datadog-storage)
*   [WAMP (Web Socket Messaging Protocol) Storage](https://php-enqueue.github.io/monitoring/#wamp-(web-socket-messaging-protocol)-storage)
*   [Symfony App](https://php-enqueue.github.io/monitoring/#symfony-app)

[](https://php-enqueue.github.io/monitoring/#installation) Installation
-----------------------------------------------------------------------

```
composer req enqueue/monitoring:0.9.x-dev
```

[](https://php-enqueue.github.io/monitoring/#track-sent-messages) Track sent messages
-------------------------------------------------------------------------------------

```
<?php
use Enqueue\Monitoring\SentMessageStats;
use Enqueue\Monitoring\GenericStatsStorageFactory;

$statsStorage = (new GenericStatsStorageFactory())->create('influxdb://127.0.0.1:8086?db=foo');
$statsStorage->pushSentMessageStats(new SentMessageStats(
    (int) (microtime(true) * 1000), // timestamp
    'queue_name', // queue
    'aMessageId',
    'aCorrelationId',
    [], // headers
    []  // properties
));
```

or, if you work with [Queue Interop](https://github.com/queue-interop/queue-interop) transport here’s how you can track a message sent

```
<?php
use Interop\Queue\Context;
use Enqueue\Monitoring\SentMessageStats;
use Enqueue\Monitoring\GenericStatsStorageFactory;

/** @var Context $context */

$queue = $context->createQueue('foo');
$message = $context->createMessage('body');

$context->createProducer()->send($queue, $message);

$statsStorage = (new GenericStatsStorageFactory())->create('influxdb://127.0.0.1:8086?db=foo');
$statsStorage->pushSentMessageStats(new SentMessageStats(
    (int) (microtime(true) * 1000),
    $queue->getQueueName(),
    $message->getMessageId(),
    $message->getCorrelationId(),
    $message->getHeaders()[],
    $message->getProperties()
));
```

[](https://php-enqueue.github.io/monitoring/#track-consumed-message) Track consumed message
-------------------------------------------------------------------------------------------

```
<?php
use Enqueue\Monitoring\ConsumedMessageStats;
use Enqueue\Monitoring\GenericStatsStorageFactory;

$receivedAt = (int) (microtime(true) * 1000);

// heavy processing here.

$statsStorage = (new GenericStatsStorageFactory())->create('influxdb://127.0.0.1:8086?db=foo');
$statsStorage->pushConsumedMessageStats(new ConsumedMessageStats(
    'consumerId',
    (int) (microtime(true) * 1000), // now
    $receivedAt,
    'aQueue',
    'aMessageId',
    'aCorrelationId',
    [], // headers
    [], // properties
    false, // redelivered or not
    ConsumedMessageStats::STATUS_ACK
));
```

or, if you work with [Queue Interop](https://github.com/queue-interop/queue-interop) transport here’s how you can track a message sent

```
<?php
use Interop\Queue\Context;
use Enqueue\Monitoring\ConsumedMessageStats;
use Enqueue\Monitoring\GenericStatsStorageFactory;

/** @var Context $context */

$queue = $context->createQueue('foo');

$consumer = $context->createConsumer($queue);

$consumerId = uniqid('consumer-id', true); // we suggest using UUID here
if ($message = $consumer->receiveNoWait()) {
    $receivedAt = (int) (microtime(true) * 1000);

    // heavy processing here.

    $consumer->acknowledge($message);

    $statsStorage = (new GenericStatsStorageFactory())->create('influxdb://127.0.0.1:8086?db=foo');
    $statsStorage->pushConsumedMessageStats(new ConsumedMessageStats(
        $consumerId,
        (int) (microtime(true) * 1000), // now
        $receivedAt,
        $queue->getQueueName(),
        $message->getMessageId(),
        $message->getCorrelationId(),
        $message->getHeaders(),
        $message->getProperties(),
        $message->isRedelivered(),
        ConsumedMessageStats::STATUS_ACK
    ));
}
```

[](https://php-enqueue.github.io/monitoring/#track-consumer-metrics) Track consumer metrics
-------------------------------------------------------------------------------------------

Consumers are long running processes. It vital to know how many of them are running right now, how they perform, how much memory do they use and so. This example shows how you can send such metrics. Call this code from time to time between processing messages.

```
<?php
use Enqueue\Monitoring\ConsumerStats;
use Enqueue\Monitoring\GenericStatsStorageFactory;

$startedAt = (int) (microtime(true) * 1000);

$statsStorage = (new GenericStatsStorageFactory())->create('influxdb://127.0.0.1:8086?db=foo');
$statsStorage->pushConsumerStats(new ConsumerStats(
    'consumerId',
    (int) (microtime(true) * 1000), // now
    $startedAt,
    null, // finished at
    true, // is started?
    false, // is finished?
    false, // is failed
    ['foo'], // consume from queues
    123, // received messages
    120, // acknowledged messages
    1, // rejected messages
    1, // requeued messages
    memory_get_usage(true),
    sys_getloadavg()[0]
));
```

[](https://php-enqueue.github.io/monitoring/#consumption-extension) Consumption extension
-----------------------------------------------------------------------------------------

There is an extension `ConsumerMonitoringExtension` for Enqueue [QueueConsumer](https://php-enqueue.github.io/quick_tour/#consumption). It could collect consumed messages and consumer stats for you.

```
<?php
use Enqueue\Consumption\QueueConsumer;
use Enqueue\Consumption\ChainExtension;
use Enqueue\Monitoring\ConsumerMonitoringExtension;
use Enqueue\Monitoring\GenericStatsStorageFactory;
use Interop\Queue\Context;

/** @var Context $context */

$statsStorage = (new GenericStatsStorageFactory())->create('influxdb://127.0.0.1:8086?db=foo');

$queueConsumer = new QueueConsumer($context, new ChainExtension([
    new ConsumerMonitoringExtension($statsStorage)
]));

// bind

// consume
```

[](https://php-enqueue.github.io/monitoring/#enqueue-client-extension) Enqueue Client Extension
-----------------------------------------------------------------------------------------------

There is an extension ClientMonitoringExtension for Enqueue [Client](https://php-enqueue.github.io/quick_tour/#client) too. It could collect sent messages stats for you.

[](https://php-enqueue.github.io/monitoring/#influxdb-storage) InfluxDB Storage
-------------------------------------------------------------------------------

Install additional packages:

```
composer req influxdb/influxdb-php:^1.14
```

```
<?php
use Enqueue\Monitoring\GenericStatsStorageFactory;

$statsStorage = (new GenericStatsStorageFactory())->create('influxdb://127.0.0.1:8086?db=foo');
```

There are available options:

```
*   'host' => '127.0.0.1',
*   'port' => '8086',
*   'user' => '',
*   'password' => '',
*   'db' => 'enqueue',
*   'measurementSentMessages' => 'sent-messages',
*   'measurementConsumedMessages' => 'consumed-messages',
*   'measurementConsumers' => 'consumers',
*   'client' => null,
*   'retentionPolicy' => null,
```

You can pass InfluxDB\Client instance in `client` option. Otherwise, it will be created on first use according to other options.

If your InfluxDB\Client uses driver that implements InfluxDB\Driver\QueryDriverInterface, then database will be automatically created for you if it doesn’t exist. Default InfluxDB\Client will also do that.

[](https://php-enqueue.github.io/monitoring/#datadog-storage) Datadog storage
-----------------------------------------------------------------------------

Install additional packages:

```
composer req datadog/php-datadogstatsd:^1.3
```

```
<?php
use Enqueue\Monitoring\GenericStatsStorageFactory;

$statsStorage = (new GenericStatsStorageFactory())->create('datadog://127.0.0.1:8125');
```

For best experience please adjust units and types in metric summary.

Example dashboard:

![Image 2: Datadog monitoring](https://php-enqueue.github.io/images/datadog_monitoring.png)

There are available options (and all available metrics):

```
*   'host' => '127.0.0.1',
*   'port' => '8125',
*   'batched' => true, // performance boost
*   'global_tags' => '', // should contain keys and values
*   'metric.messages.sent' => 'enqueue.messages.sent',
*   'metric.messages.consumed' => 'enqueue.messages.consumed',
*   'metric.messages.redelivered' => 'enqueue.messages.redelivered',
*   'metric.messages.failed' => 'enqueue.messages.failed',
*   'metric.consumers.started' => 'enqueue.consumers.started',
*   'metric.consumers.finished' => 'enqueue.consumers.finished',
*   'metric.consumers.failed' => 'enqueue.consumers.failed',
*   'metric.consumers.received' => 'enqueue.consumers.received',
*   'metric.consumers.acknowledged' => 'enqueue.consumers.acknowledged',
*   'metric.consumers.rejected' => 'enqueue.consumers.rejected',
*   'metric.consumers.requeued' => 'enqueue.consumers.requeued',
*   'metric.consumers.memoryUsage' => 'enqueue.consumers.memoryUsage',
```

[](https://php-enqueue.github.io/monitoring/#wamp-web-socket-messaging-protocol-storage) WAMP (Web Socket Messaging Protocol) Storage
-------------------------------------------------------------------------------------------------------------------------------------

Install additional packages:

```
composer req thruway/pawl-transport:^0.5.0 thruway/client:^0.5.0
```

```
<?php
use Enqueue\Monitoring\GenericStatsStorageFactory;

$statsStorage = (new GenericStatsStorageFactory())->create('wamp://127.0.0.1:9090?topic=stats');
```

There are available options:

```
*   'host'                => '127.0.0.1',
*   'port'                => '9090',
*   'topic'               => 'stats',
*   'max_retries'         => 15,
*   'initial_retry_delay' => 1.5,
*   'max_retry_delay'     => 300,
*   'retry_delay_growth'  => 1.5,
```

[](https://php-enqueue.github.io/monitoring/#symfony-app) Symfony App
---------------------------------------------------------------------

You have to register some services in order to incorporate monitoring facilities into your Symfony application.

```
# config/packages/enqueue.yaml

enqueue:
  default:
    transport: 'amqp://guest:guest@bar:5672/%2f'
    monitoring: 'influxdb://127.0.0.1:8086?db=foo'

  another:
    transport: 'amqp://guest:guest@foo:5672/%2f'
    monitoring: 'wamp://127.0.0.1:9090?topic=stats'
    client: ~

  datadog:
    transport: 'amqp://guest:guest@foo:5672/%2f'
    monitoring: 'datadog://127.0.0.1:8125?batched=false'
    client: ~
```

[back to index](https://php-enqueue.github.io/)
