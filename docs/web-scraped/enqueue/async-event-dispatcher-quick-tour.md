# Source: https://php-enqueue.github.io/async_event_dispatcher/quick_tour/

Title: enqueue-dev

URL Source: https://php-enqueue.github.io/async_event_dispatcher/quick_tour/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/async_event_dispatcher/quick_tour/#async-event-dispatcher-symfony) Async event dispatcher (Symfony)
------------------------------------------------------------------------------------------------------------------------------------

The doc shows how you can setup async event dispatching in plain PHP. If you are looking for the ways to use it in Symfony application [read this post instead](https://php-enqueue.github.io/bundle/async_events/)

*   [Installation](https://php-enqueue.github.io/async_event_dispatcher/quick_tour/#installation)
*   [Configuration](https://php-enqueue.github.io/async_event_dispatcher/quick_tour/#configuration)
*   [Dispatch event](https://php-enqueue.github.io/async_event_dispatcher/quick_tour/#dispatch-event)
*   [Process async events](https://php-enqueue.github.io/async_event_dispatcher/quick_tour/#process-async-events)

[](https://php-enqueue.github.io/async_event_dispatcher/quick_tour/#installation) Installation
----------------------------------------------------------------------------------------------

You need the async dispatcher library and a one of [the supported transports](https://php-enqueue.github.io/async_event_dispatcher/transport)

```
$ composer require enqueue/async-event-dispatcher enqueue/fs
```

[](https://php-enqueue.github.io/async_event_dispatcher/quick_tour/#configuration) Configuration
------------------------------------------------------------------------------------------------

```
<?php

// config.php

use Enqueue\AsyncEventDispatcher\AsyncListener;
use Enqueue\AsyncEventDispatcher\AsyncProcessor;
use Enqueue\AsyncEventDispatcher\PhpSerializerEventTransformer;
use Enqueue\AsyncEventDispatcher\AsyncEventDispatcher;
use Enqueue\AsyncEventDispatcher\SimpleRegistry;
use Enqueue\Fs\FsConnectionFactory;
use Symfony\Component\EventDispatcher\EventDispatcher;

require_once __DIR__.'/vendor/autoload.php';

// it could be any other queue-interop/queue-interop compatible context.
$context = (new FsConnectionFactory('file://'.__DIR__.'/queues'))->createContext();
$eventQueue = $context->createQueue('symfony_events');

$registry = new SimpleRegistry(
    ['the_event' => 'default'],
    ['default' => new PhpSerializerEventTransformer($context)]
);

$asyncListener = new AsyncListener($context, $registry, $eventQueue);

$dispatcher = new EventDispatcher();

// the listener sends even as a message through MQ
$dispatcher->addListener('the_event', $asyncListener);

$asyncDispatcher = new AsyncEventDispatcher($dispatcher, $asyncListener);

// the listener is executed on consumer side.
$asyncDispatcher->addListener('the_event', function() {
});

$asyncProcessor = new AsyncProcessor($registry, $asyncDispatcher);
```

[](https://php-enqueue.github.io/async_event_dispatcher/quick_tour/#dispatch-event) Dispatch event
--------------------------------------------------------------------------------------------------

```
<?php

// send.php

use Symfony\Component\EventDispatcher\GenericEvent;

require_once __DIR__.'/vendor/autoload.php';

include __DIR__.'/config.php';

$dispatcher->dispatch('the_event', new GenericEvent('theSubject'));
```

[](https://php-enqueue.github.io/async_event_dispatcher/quick_tour/#process-async-events) Process async events
--------------------------------------------------------------------------------------------------------------

```
<?php

// consume.php

use Interop\Queue\Processor;

require_once __DIR__.'/vendor/autoload.php';
include __DIR__.'/config.php';

$consumer = $context->createConsumer($eventQueue);

while (true) {
    if ($message = $consumer->receive(5000)) {
        $result = $asyncProcessor->process($message, $context);

        switch ((string) $result) {
            case Processor::ACK:
                $consumer->acknowledge($message);
                break;
            case Processor::REJECT:
                $consumer->reject($message);
                break;
            case Processor::REQUEUE:
                $consumer->reject($message, true);
                break;
            default:
                throw new \LogicException('Result is not supported');
        }
    }
}
```

[back to index](https://php-enqueue.github.io/)
