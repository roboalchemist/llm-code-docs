# Source: https://php-enqueue.github.io/bundle/production_settings/

Title: Production settings

URL Source: https://php-enqueue.github.io/bundle/production_settings/

Markdown Content:
Production settings | enqueue-dev
===============
[Skip to main content](https://php-enqueue.github.io/bundle/production_settings/#main-content)

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

1.   [Symfony bundle](https://php-enqueue.github.io/symfony)
2.   Production settings

Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/bundle/production_settings/#production-settings) Production settings
=====================================================================================================

[](https://php-enqueue.github.io/bundle/production_settings/#supervisord) Supervisord
-------------------------------------------------------------------------------------

As you may read in [quick tour](https://php-enqueue.github.io/bundle/quick_tour/) you have to run 
```plaintext
enqueue:consume
```
 in order to process messages The php process is not designed to work for a long time. So it has to quit periodically. Or, the command may exit because of error or exception. Something has to bring it back and continue message consumption. We advise you to use [Supervisord](http://supervisord.org/) for that. It starts processes and keep an eye on them while they are working.

Here an example of supervisord configuration. It runs four instances of 
```plaintext
enqueue:consume
```
 command.

```
[program:pf_message_consumer]
command=/path/to/bin/console --env=prod --no-debug --time-limit="now + 5 minutes" enqueue:consume
process_name=%(program_name)s_%(process_num)02d
numprocs=4
autostart=true
autorestart=true
startsecs=0
user=apache
redirect_stderr=true
```

_**Note**: Pay attention to 
```plaintext
--time-limit
```
 it tells the command to exit after 5 minutes._

[back to index](https://php-enqueue.github.io/symfony)
