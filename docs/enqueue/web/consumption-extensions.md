# Source: https://php-enqueue.github.io/consumption/extensions/

Title: Extensions

URL Source: https://php-enqueue.github.io/consumption/extensions/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/consumption/extensions/#consumption-extensions) Consumption extensions.
--------------------------------------------------------------------------------------------------------

You can learn how to register extensions in [quick tour](https://php-enqueue.github.io/quick_tour/#consumption). There’s dedicated [chapter](https://php-enqueue.github.io/bundle/consumption_extension/) for how to add extension in Symfony app.

[](https://php-enqueue.github.io/consumption/extensions/#loggerextension)[LoggerExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue/Consumption/Extension/LoggerExtension.php)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It sets logger to queue consumer context. All log messages will go to it.

[](https://php-enqueue.github.io/consumption/extensions/#doctrineclearidentitymapextension)[DoctrineClearIdentityMapExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue-bundle/Consumption/Extension/DoctrineClearIdentityMapExtension.php)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It clears Doctrine’s identity map after a message is processed. It reduce memory usage.

[](https://php-enqueue.github.io/consumption/extensions/#doctrinepingconnectionextension)[DoctrinePingConnectionExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue-bundle/Consumption/Extension/DoctrinePingConnectionExtension.php)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It test a database connection and if it is lost it does reconnect. Fixes “MySQL has gone away” errors.

[](https://php-enqueue.github.io/consumption/extensions/#doctrineclosedentitymanagerextension)[DoctrineClosedEntityManagerExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue-bundle/Consumption/Extension/DoctrineClosedEntityManagerExtension.php)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The extension interrupts consumption if an entity manager has been closed.

[](https://php-enqueue.github.io/consumption/extensions/#resetservicesextension)[ResetServicesExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue-bundle/Consumption/Extension/ResetServicesExtension.php)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It resets all services with tag “kernel.reset”. For example, this includes all monolog loggers if installed and will flush/clean all buffers, reset internal state, and get them back to a state in which they can receive log records again.

[](https://php-enqueue.github.io/consumption/extensions/#replyextension)[ReplyExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue/Consumption/Extension/ReplyExtension.php)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It comes with RPC code and simplifies reply logic. It takes care of sending a reply message to reply queue.

[](https://php-enqueue.github.io/consumption/extensions/#setupbrokerextension)[SetupBrokerExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue/Client/ConsumptionExtension/SetupBrokerExtension.php)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It responsible for configuring everything at a broker side. queues, topics, bindings and so on. The extension is added at runtime when `--setup-broker` option is used.

[](https://php-enqueue.github.io/consumption/extensions/#limitconsumedmessagesextension)[LimitConsumedMessagesExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue/Consumption/Extension/LimitConsumedMessagesExtension.php)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The extension counts processed message and once a limit is reached it interrupts consumption. The extension is added at runtime when `--message-limit=10` option is used.

[](https://php-enqueue.github.io/consumption/extensions/#limitconsumermemoryextension)[LimitConsumerMemoryExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue/Consumption/Extension/LimitConsumerMemoryExtension.php)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The extension interrupts consumption once a memory limit is reached. The extension is added at runtime when `--memory-limit=512` option is used. The value is Mb.

[](https://php-enqueue.github.io/consumption/extensions/#limitconsumptiontimeextension)[LimitConsumptionTimeExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue/Consumption/Extension/LimitConsumptionTimeExtension.php)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The extension interrupts consumption once time limit is reached. The extension is added at runtime when `--time-limit="now + 2 minutes"` option is used.

[](https://php-enqueue.github.io/consumption/extensions/#signalextension)[SignalExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue/Consumption/Extension/SignalExtension.php)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The extension catch process signals and gracefully stops consumption. Works only on NIX platforms.

[](https://php-enqueue.github.io/consumption/extensions/#delayredeliveredmessageextension)[DelayRedeliveredMessageExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/pkg/enqueue/Client/ConsumptionExtension/DelayRedeliveredMessageExtension.php)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The extension checks whether the received message is redelivered (There was attempt to process message but it failed). If so the extension reject the origin message and creates a copy message with a delay.

[](https://php-enqueue.github.io/consumption/extensions/#consumermonitoringextension)[ConsumerMonitoringExtension](https://github.com/php-enqueue/enqueue-dev/blob/master/docs/monitoring.md#consumption-extension)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There is an extension ConsumerMonitoringExtension for Enqueue QueueConsumer. It could collect consumed messages and consumer stats for you and send them to Grafana, InfluxDB or Datadog.

[back to index](https://php-enqueue.github.io/)
