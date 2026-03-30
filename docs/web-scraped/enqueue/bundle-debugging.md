# Source: https://php-enqueue.github.io/bundle/debugging/

Title: Debugging

URL Source: https://php-enqueue.github.io/bundle/debugging/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/bundle/debugging/#profiler) Profiler
---------------------------------------------------------------------

It may be useful to see what messages were sent during a http request. The bundle provides a collector for Symfony [profiler](http://symfony.com/doc/current/profiler.html). The extension collects all sent messages

To enable profiler

```
# app/config/config_dev.yml

enqueue:
    default:
        client:
            traceable_producer: true
```

Now suppose you have this code in an action:

```
<?php

use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Request;
use Enqueue\Client\Message;
use Enqueue\Client\ProducerInterface;

class DefaultController extends Controller
    /**
     * @Route("/", name="homepage")
     */
    public function indexAction(Request $request)
    {
        /** @var ProducerInterface $producer */
        $producer = $this->get('enqueue.producer');

        $producer->sendEvent('foo_topic', 'Hello world');

        $producer->sendEvent('bar_topic', ['bar' => 'val']);

        $message = new Message();
        $message->setBody('baz');
        $producer->sendEvent('baz_topic', $message);

        // ...
    }
```

For this action you may see something like this in the profiler:

![Image 1: Symfony profiler](https://php-enqueue.github.io/images/symfony_profiler.png)

[](https://php-enqueue.github.io/bundle/debugging/#queues-and-topics-available) Queues and topics available
-----------------------------------------------------------------------------------------------------------

There are two console commands `./bin/console enqueue:queues` and `./bin/console enqueue:topics`. They are here to help you to learn more about existing topics and queues.

Here’s the result:

![Image 2: Cli debug commands](https://php-enqueue.github.io/images/cli_debug_commands.png)

[](https://php-enqueue.github.io/bundle/debugging/#consume-command-verbosity) Consume command verbosity
-------------------------------------------------------------------------------------------------------

By default the commands `enqueue:consume` or `enqueue:transport:consume` does not output anything. You can add `-vvv` to see more information.

![Image 3: Consume command verbosity](https://php-enqueue.github.io/images/consume_command_verbosity.png)

[back to index](https://php-enqueue.github.io/symfony)
