# Source: https://php-enqueue.github.io/bundle/async_commands/

Title: Async commands

URL Source: https://php-enqueue.github.io/bundle/async_commands/

Markdown Content:
Supporting Enqueue
------------------

Enqueue is an MIT-licensed open source project with its ongoing development made possible entirely by the support of community and our customers. If you’d like to join them, please consider:

*   [Become our client](http://forma-pro.com/)

* * *

[](https://php-enqueue.github.io/bundle/async_commands/#installation) Installation
----------------------------------------------------------------------------------

```
$ composer require enqueue/async-command:0.9.x-dev
```

[](https://php-enqueue.github.io/bundle/async_commands/#configuration) Configuration
------------------------------------------------------------------------------------

```
# config/packages/enqueue_async_commands.yaml

enqueue:
    default:
        async_commands:
            enabled: true
            timeout: 60
            command_name: ~
            queue_name: ~
```

[](https://php-enqueue.github.io/bundle/async_commands/#usage) Usage
--------------------------------------------------------------------

```
<?php

use Enqueue\Client\ProducerInterface;
use Enqueue\AsyncCommand\Commands;
use Enqueue\AsyncCommand\RunCommand;
use Symfony\Component\DependencyInjection\ContainerInterface;

/** @var $container ContainerInterface */

/** @var ProducerInterface $producer */
$producer = $container->get(ProducerInterface::class);

$cmd = new RunCommand('debug:container', ['--tag=form.type']);
$producer->sendCommand(Commands::RUN_COMMAND, $cmd);
```

optionally you can get a command execution result:

```
<?php

use Enqueue\Client\ProducerInterface;
use Enqueue\AsyncCommand\CommandResult;
use Enqueue\AsyncCommand\Commands;
use Enqueue\AsyncCommand\RunCommand;
use Symfony\Component\DependencyInjection\ContainerInterface;

/** @var $container ContainerInterface */

/** @var ProducerInterface $producer */
$producer = $container->get(ProducerInterface::class);

$promise = $producer->sendCommand(Commands::RUN_COMMAND, new RunCommand('debug:container'), true);

// do other stuff.

if ($replyMessage = $promise->receive(5000)) {
    $result = CommandResult::jsonUnserialize($replyMessage->getBody());

    echo $result->getOutput();
}
```

[back to index](https://php-enqueue.github.io/symfony)
