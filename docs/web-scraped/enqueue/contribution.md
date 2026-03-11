# Source: https://php-enqueue.github.io/contribution/

Title: Contribution

URL Source: https://php-enqueue.github.io/contribution/

Markdown Content:
Contribution | enqueue-dev
===============
[Skip to main content](https://php-enqueue.github.io/contribution/#main-content)

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

Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/contribution/#contribution) Contribution
=========================================================================

To contribute you have to send a pull request to [enqueue-dev](https://github.com/php-enqueue/enqueue-dev) repository. The pull requests to read only subtree split [repositories](https://github.com/php-enqueue/enqueue-dev/blob/master/bin/subtree-split#L46) will be closed.

[](https://php-enqueue.github.io/contribution/#setup-environment) Setup environment
-----------------------------------------------------------------------------------

```
composer install
./bin/pre-commit -i
./bin/dev -b
```

Once you did it you can work on a feature or bug fix.

If you need, you can also use composer scripts to run code linting and static analysis:

*   For code style linting, run 
```plaintext
composer run cs-lint
```
. Optionally add file names: 
```plaintext
composer run cs-lint pkg/null/NullTopic.php
```
 for example.
*   You can also fix your code style with 
```plaintext
composer run cs-fix
```
.
*   Static code analysis can be run using 
```plaintext
composer run phpstan
```
. As above, you can pass specific files.

[](https://php-enqueue.github.io/contribution/#testing) Testing
---------------------------------------------------------------

To run tests

```
./bin/test.sh
```

or for a package only:

```
./bin/test.sh pkg/enqueue
```

[](https://php-enqueue.github.io/contribution/#commit) Commit
-------------------------------------------------------------

When you try to commit changes 
```plaintext
php-cs-fixer
```
 is run. It fixes all coding style issues. Don’t forget to stage them and commit everything. Once everything is done open a pull request on official repository.

[](https://php-enqueue.github.io/contribution/#wtf) WTF?!
---------------------------------------------------------

*   If you get 
```plaintext
rabbitmqssl: forward host lookup failed: Unknown host, wait for service rabbitmqssl:5671
```
 do 
```plaintext
docker compose down
```
.

[back to index](https://php-enqueue.github.io/)
