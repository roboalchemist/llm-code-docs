# Source: https://php-enqueue.github.io/magento/quick_tour/

Title: Quick tour

URL Source: https://php-enqueue.github.io/magento/quick_tour/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/magento/quick_tour/#magento-enqueue-quick-tour) Magento Enqueue. Quick tour
------------------------------------------------------------------------------------------------------------

The module integrates [Enqueue Client](https://php-enqueue.github.io/client/quick_tour/) with Magento1. You can send and consume messages to different message queues such as RabbitMQ, AMQP, STOMP, Amazon SQS, Kafka, Redis, Google PubSub, Gearman, Beanstalk, Google PubSub and others. Or integrate Magento2 app with other applications or service via [Message Bus](https://php-enqueue.github.io/client/message_bus/). There is [a module](https://php-enqueue.github.io/magento2/quick_tour/) for Magento2 too.

[](https://php-enqueue.github.io/magento/quick_tour/#installation) Installation
-------------------------------------------------------------------------------

We use [composer](https://getcomposer.org/) and [cotya/magento-composer-installer](https://github.com/Cotya/magento-composer-installer) plugin to install [magento-enqueue](https://github.com/php-enqueue/magento-enqueue) extension.

To install libraries run the commands in the application root directory.

```
composer require "magento-hackathon/magento-composer-installer:~3.0"
composer require "enqueue/magento-enqueue:*@dev" "enqueue/amqp-ext"
```

_**Note**: You could use not only AMQP transport but any other [available](https://php-enqueue.github.io/magento/transport)._

[](https://php-enqueue.github.io/magento/quick_tour/#configuration) Configuration
---------------------------------------------------------------------------------

At this stage we have configure the Enqueue extension in Magento backend. The config is here: `System -> Configuration -> Enqueue Message Queue`. Here’s the example of Amqp transport that connects to RabbitMQ broker on localhost:

![Image 1: Сonfiguration](https://php-enqueue.github.io/images/magento_enqueue_configuration.jpeg)

[](https://php-enqueue.github.io/magento/quick_tour/#publish-message) Publish Message
-------------------------------------------------------------------------------------

To send a message you have to take enqueue helper and call `send` method.

```
<?php

Mage::helper('enqueue')->send('a_topic', 'aMessage');
```

[](https://php-enqueue.github.io/magento/quick_tour/#message-consumption) Message Consumption
---------------------------------------------------------------------------------------------

I assume you have `acme` Magento module properly created, configured and registered. To consume messages you have to define a processor class first:

```
<?php
// app/code/local/Acme/Module/Helper/Async/Foo.php

use Interop\Queue\Context;
use Interop\Queue\Message;
use Interop\Queue\Processor;

class Acme_Module_Helper_Async_Foo implements Processor
{
    public function process(Message $message, Context $context)
    {
        // do job
        // $message->getBody() -> 'payload'

        return self::ACK;         // acknowledge message
        // return self::REJECT;   // reject message
        // return self::REQUEUE;  // requeue message
    }
}
```

than subscribe it to a topic or several topics:

```
<!-- app/etc/local.xml -->

<config>
  <default>
    <enqueue>
      <processors>
        <foo-processor>
          <topic>a_topic</topic>
          <helper>acme/async_foo</helper>
        </foo-processor>
      </processors>
    </enqueue>
  </default>
</config>
```

and run message consume command:

```
$ php shell/enqueue.php enqueue:consume -vvv --setup-broker
```

[back to index](https://php-enqueue.github.io/)
