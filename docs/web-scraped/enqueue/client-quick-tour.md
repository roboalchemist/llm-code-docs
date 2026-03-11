# Source: https://php-enqueue.github.io/client/quick_tour/

Title: Quick tour

URL Source: https://php-enqueue.github.io/client/quick_tour/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/client/quick_tour/#simple-client-quick-tour) Simple client. Quick tour.
--------------------------------------------------------------------------------------------------------

The simple client library takes Enqueue client classes and Symfony components and makes an easy to use client facade. It reduces the boiler plate code you have to write to start using the Enqueue client features.

*   [Install](https://php-enqueue.github.io/client/quick_tour/#install)
*   [Configure](https://php-enqueue.github.io/client/quick_tour/#configure)
*   [Producer message](https://php-enqueue.github.io/client/quick_tour/#produce-message)
*   [Consume messages](https://php-enqueue.github.io/client/quick_tour/#consume-messages)

[](https://php-enqueue.github.io/client/quick_tour/#install) Install
--------------------------------------------------------------------

```
$ composer require enqueue/simple-client enqueue/amqp-ext
```

[](https://php-enqueue.github.io/client/quick_tour/#configure) Configure
------------------------------------------------------------------------

The code below shows how to use simple client with AMQP transport. There are other [supported brokers](https://php-enqueue.github.io/client/supported_brokers/).

```
<?php
use Enqueue\SimpleClient\SimpleClient;

include __DIR__.'/vendor/autoload.php';

$client = new SimpleClient('amqp:');
```

[](https://php-enqueue.github.io/client/quick_tour/#produce-message) Produce message
------------------------------------------------------------------------------------

There two types of message a client can produce: events and commands. Events are used to notify others about something, in other words it is an implementation of [publish-subscribe pattern](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern), sometimes called “fire-and-forget” too. With events there is no way to get a reply as a producer is not aware of any subscribed consumers. Commands are used to request a job to be done. It is an implementation of one-to-one messaging pattern. A producer can request a reply from the consumer though it is up to the consumer whether send it or not.

Commands work inside the app [scope](https://php-enqueue.github.io/client/message_examples/#scope) where events work inside the app scope as well as on [message bus](https://php-enqueue.github.io/client/message_bus/) scope.

Send event examples:

```
<?php

/** @var \Enqueue\SimpleClient\SimpleClient $client */

$client->setupBroker();

$client->sendEvent('user_updated', 'aMessageData');

// or an array

$client->sendEvent('order_price_calculated', ['foo', 'bar']);

// or an json serializable object
$client->sendEvent('user_activated', new class() implements \JsonSerializable {
    public function jsonSerialize() {
        return ['foo', 'bar'];
    }
});
```

Send command examples:

```
<?php

/** @var \Enqueue\SimpleClient\SimpleClient $client */

$client->setupBroker();

// accepts same type of arguments as sendEvent method
$client->sendCommand('calculate_statistics', 'aMessageData');

$reply = $client->sendCommand('build_category_tree', 'aMessageData', true);

$replyMessage = $reply->receive(5000); // wait for reply for 5 seconds

$replyMessage->getBody();
```

[](https://php-enqueue.github.io/client/quick_tour/#consume-messages) Consume messages
--------------------------------------------------------------------------------------

```
<?php

use Interop\Queue\Message;
use Interop\Queue\Processor;

/** @var \Enqueue\SimpleClient\SimpleClient $client */

$client->bindTopic('a_bar_topic', function(Message $psrMessage) {
    // processing logic here

    return Processor::ACK;
});

$client->consume();
```

[](https://php-enqueue.github.io/client/quick_tour/#cli-commands) Cli commands
------------------------------------------------------------------------------

```
#!/usr/bin/env php
<?php

// bin/enqueue.php

use Enqueue\Symfony\Client\SimpleConsumeCommand;
use Enqueue\Symfony\Client\SimpleProduceCommand;
use Enqueue\Symfony\Client\SimpleRoutesCommand;
use Enqueue\Symfony\Client\SimpleSetupBrokerCommand;
use Enqueue\Symfony\Client\SetupBrokerCommand;
use Symfony\Component\Console\Application;

/** @var \Enqueue\SimpleClient\SimpleClient $client */

$application = new Application();
$application->add(new SimpleSetupBrokerCommand($client->getDriver()));
$application->add(new SimpleRoutesCommand($client->getDriver()));
$application->add(new SimpleProduceCommand($client->getProducer()));
$application->add(new SimpleConsumeCommand(
    $client->getQueueConsumer(),
    $client->getDriver(),
    $client->getDelegateProcessor()
));

$application->run();
```

and run to see what is there:

```
$ php bin/enqueue.php
```

or consume messages

```
$ php bin/enqueue.php enqueue:consume -vvv --setup-broker
```

[back to index](https://php-enqueue.github.io/)
