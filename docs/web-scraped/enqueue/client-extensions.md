# Source: https://php-enqueue.github.io/client/extensions/

Title: Extensions

URL Source: https://php-enqueue.github.io/client/extensions/

Markdown Content:
Extensions | enqueue-dev
===============
[Skip to main content](https://php-enqueue.github.io/client/extensions/#main-content)

[enqueue-dev](https://php-enqueue.github.io/)

*   [Index](https://php-enqueue.github.io/)
*   [Key concepts](https://php-enqueue.github.io/concepts/)
*   [Quick tour](https://php-enqueue.github.io/quick_tour/)
*   [Transports](https://php-enqueue.github.io/transport)
    *   [AMQP](https://php-enqueue.github.io/transport/amqp/)
    *   [AMQP Bunny](https://php-enqueue.github.io/transport/amqp_bunny/)
    *   [AMQP Lib](https://php-enqueue.github.io/transport/amqp_lib/)
    *   [DBAL](https://php-enqueue.github.io/transport/dbal/)
    *   [Filesystem](https://php-enqueue.github.io/transport/filesystem/)
    *   [Gearman](https://php-enqueue.github.io/transport/gearman/)
    *   [GPS](https://php-enqueue.github.io/transport/gps/)
    *   [Kafka](https://php-enqueue.github.io/transport/kafka/)
    *   [MongoDB](https://php-enqueue.github.io/transport/mongodb/)
    *   [Null](https://php-enqueue.github.io/transport/null/)
    *   [Pheanstalk](https://php-enqueue.github.io/transport/pheanstalk/)
    *   [Redis](https://php-enqueue.github.io/transport/redis/)
    *   [Amazon SNS](https://php-enqueue.github.io/transport/sns/)
    *   [Amazon SNS-SQS](https://php-enqueue.github.io/transport/snsqs/)
    *   [Amazon SQS](https://php-enqueue.github.io/transport/sqs/)
    *   [STOMP](https://php-enqueue.github.io/transport/stomp/)
    *   [WAMP](https://php-enqueue.github.io/transport/wamp/)

*   [Consumption](https://php-enqueue.github.io/consumption)
    *   [Extensions](https://php-enqueue.github.io/consumption/extensions/)
    *   [Message processors](https://php-enqueue.github.io/consumption/message_processor/)

*   [Client](https://php-enqueue.github.io/client)
    *   [Quick tour](https://php-enqueue.github.io/client/quick_tour/)
    *   [Message examples](https://php-enqueue.github.io/client/message_examples/)
    *   [Supported brokers](https://php-enqueue.github.io/client/supported_brokers/)
    *   [Message bus](https://php-enqueue.github.io/client/message_bus/)
    *   [RPC call](https://php-enqueue.github.io/client/rpc_call/)
    *   [Extensions](https://php-enqueue.github.io/client/extensions/)

*   [Elastica bundle](https://php-enqueue.github.io/elastica-bundle/overview/)
*   [Job Queue](https://php-enqueue.github.io/job-queue)
    *   [Run unique job](https://php-enqueue.github.io/job_queue/run_unique_job/)
    *   [Run sub job](https://php-enqueue.github.io/job_queue/run_sub_job/)

*   [Symfony bundle](https://php-enqueue.github.io/symfony)
    *   [Quick tour](https://php-enqueue.github.io/bundle/quick_tour/)
    *   [Config reference](https://php-enqueue.github.io/bundle/config_reference/)
    *   [CLI commands](https://php-enqueue.github.io/bundle/cli_commands/)
    *   [Message producer](https://php-enqueue.github.io/bundle/message_producer/)
    *   [Message processor](https://php-enqueue.github.io/bundle/message_processor/)
    *   [Async events](https://php-enqueue.github.io/bundle/async_events/)
    *   [Async commands](https://php-enqueue.github.io/bundle/async_commands/)
    *   [Job queue](https://php-enqueue.github.io/bundle/job_queue/)
    *   [Consumption extension](https://php-enqueue.github.io/bundle/consumption_extension/)
    *   [Production settings](https://php-enqueue.github.io/bundle/production_settings/)
    *   [Debugging](https://php-enqueue.github.io/bundle/debugging/)
    *   [Functional testing](https://php-enqueue.github.io/bundle/functional_testing/)

*   [Laravel](https://php-enqueue.github.io/laravel)
    *   [Quick tour](https://php-enqueue.github.io/laravel/quick_tour/)
    *   [Queues](https://php-enqueue.github.io/laravel/queues/)

*   [Magento](https://php-enqueue.github.io/magento)
    *   [Quick tour](https://php-enqueue.github.io/magento/quick_tour/)
    *   [CLI commands](https://php-enqueue.github.io/magento/cli_commands/)

*   [Magento 2](https://php-enqueue.github.io/magento2)
    *   [Quick tour](https://php-enqueue.github.io/magento2/quick_tour/)
    *   [CLI commands](https://php-enqueue.github.io/magento2/cli_commands/)

*   [Yii](https://php-enqueue.github.io/yii)
    *   [AMQP Interop driver](https://php-enqueue.github.io/yii/amqp_driver/)

*   [Messages](https://php-enqueue.github.io/messages/)
*   [DSN Parser](https://php-enqueue.github.io/dsn/)
*   [Monitoring](https://php-enqueue.github.io/monitoring/)
*   [Contribution](https://php-enqueue.github.io/contribution/)

 This site uses [Just the Docs](https://github.com/just-the-docs/just-the-docs), a documentation theme for Jekyll. 

*   [enqueue-dev on GitHub](https://github.com/php-enqueue/enqueue-dev)

1.   [Client](https://php-enqueue.github.io/client)
2.   Extensions

Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/client/extensions/#client-extensions) Client extensions.
=========================================================================================

There is an ability to hook into sending process. You have to create an extension class that implements 
```plaintext
Enqueue\Client\ExtensionInterface
```
 interface. For example, 
```plaintext
TimestampMessageExtension
```
 extension adds timestamps every message before sending it to MQ.

```
<?php
namespace Acme;

use Enqueue\Client\ExtensionInterface;
use Enqueue\Client\Message;

class TimestampMessageExtension implements ExtensionInterface
{
    public function onPreSend($topic, Message $message)
    {
        if ($message->getTimestamp()) {
            $message->setTimestamp(time());
        }
    }

    public function onPostSend($topic, Message $message)
    {

    }
}
```

[](https://php-enqueue.github.io/client/extensions/#symfony) Symfony
--------------------------------------------------------------------

To use the extension in Symfony, you have to register it as a container service with a special tag.

```
# config/services.yaml

services:
  timestamp_message_extension:
    class: Acme\TimestampMessageExtension
    tags:
      - { name: 'enqueue.client.extension' }
```

You can add 
```plaintext
priority
```
 attribute with a number. The higher value you set the earlier the extension is called.

[back to index](https://php-enqueue.github.io/)
