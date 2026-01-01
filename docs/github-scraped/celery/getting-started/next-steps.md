# Next Steps

The `first-steps`{.interpreted-text role="ref"} guide is intentionally
minimal. In this guide I\'ll demonstrate what Celery offers in more
detail, including how to add Celery support for your application and
library.

This document doesn\'t document all of Celery\'s features and best
practices, so it\'s recommended that you also read the
`User Guide <guide>`{.interpreted-text role="ref"}

::: {.contents local="" depth="1"}
:::

## Using Celery in your Application

### Our Project {#project-layout}

Project layout:

    src/
        proj/__init__.py
            /celery.py
            /tasks.py

#### `proj/celery.py`{.interpreted-text role="file"}

::: {.literalinclude language="python"}
../../examples/next-steps/proj/celery.py
:::

In this module you created our `@Celery`{.interpreted-text role="class"}
instance (sometimes referred to as the *app*). To use Celery within your
project you simply import this instance.

-   The `broker` argument specifies the URL of the broker to use.

    > See `celerytut-broker`{.interpreted-text role="ref"} for more
    > information.

-   The `backend` argument specifies the result backend to use.

    > It\'s used to keep track of task state and results. While results
    > are disabled by default I use the RPC result backend here because
    > I demonstrate how retrieving results work later. You may want to
    > use a different backend for your application. They all have
    > different strengths and weaknesses. If you don\'t need results,
    > it\'s better to disable them. Results can also be disabled for
    > individual tasks by setting the `@task(ignore_result=True)`
    > option.
    >
    > See `celerytut-keeping-results`{.interpreted-text role="ref"} for
    > more information.

-   The `include` argument is a list of modules to import when the
    worker starts. You need to add our tasks module here so that the
    worker is able to find our tasks.

#### `proj/tasks.py`{.interpreted-text role="file"}

::: {.literalinclude language="python"}
../../examples/next-steps/proj/tasks.py
:::

### Starting the worker

The `celery`{.interpreted-text role="program"} program can be used to
start the worker (you need to run the worker in the directory above
[proj]{.title-ref}, according to the example project layout the
directory is [src]{.title-ref}):

``` console
$ celery -A proj worker -l INFO
```

When the worker starts you should see a banner and some messages:

    --------------- celery@halcyon.local v4.0 (latentcall)
    --- ***** -----
    -- ******* ---- [Configuration]
    - *** --- * --- . broker:      amqp://guest@localhost:5672//
    - ** ---------- . app:         __main__:0x1012d8590
    - ** ---------- . concurrency: 8 (processes)
    - ** ---------- . events:      OFF (enable -E to monitor this worker)
    - ** ----------
    - *** --- * --- [Queues]
    -- ******* ---- . celery:      exchange:celery(direct) binding:celery
    --- ***** -----

    [2012-06-08 16:23:51,078: WARNING/MainProcess] celery@halcyon.local has started.

\-- The *broker* is the URL you specified in the broker argument in our
`celery` module. You can also specify a different broker on the
command-line by using the `-b <celery -b>`{.interpreted-text
role="option"} option.

\-- *Concurrency* is the number of prefork worker process used to
process your tasks concurrently. When all of these are busy doing work,
new tasks will have to wait for one of the tasks to finish before it can
be processed.

The default concurrency number is the number of CPU\'s on that machine
(including cores). You can specify a custom number using the
`celery worker -c`{.interpreted-text role="option"} option. There\'s no
recommended value, as the optimal number depends on a number of factors,
but if your tasks are mostly I/O-bound then you can try to increase it.
Experimentation has shown that adding more than twice the number of
CPU\'s is rarely effective, and likely to degrade performance instead.

Including the default prefork pool, Celery also supports using Eventlet,
Gevent, and running in a single thread (see
`concurrency`{.interpreted-text role="ref"}).

\-- *Events* is an option that causes Celery to send monitoring messages
(events) for actions occurring in the worker. These can be used by
monitor programs like `celery events`, and Flower \-- the real-time
Celery monitor, which you can read about in the
`Monitoring and Management guide <guide-monitoring>`{.interpreted-text
role="ref"}.

\-- *Queues* is the list of queues that the worker will consume tasks
from. The worker can be told to consume from several queues at once, and
this is used to route messages to specific workers as a means for
Quality of Service, separation of concerns, and prioritization, all
described in the `Routing Guide
<guide-routing>`{.interpreted-text role="ref"}.

You can get a complete list of command-line arguments by passing in the
`!--help`{.interpreted-text role="option"} flag:

``` console
$ celery worker --help
```

These options are described in more detailed in the
`Workers Guide <guide-workers>`{.interpreted-text role="ref"}.

#### Stopping the worker

To stop the worker simply hit `Control-c`{.interpreted-text role="kbd"}.
A list of signals supported by the worker is detailed in the
`Workers Guide <guide-workers>`{.interpreted-text role="ref"}.

#### In the background

In production you\'ll want to run the worker in the background,
described in detail in the
`daemonization tutorial <daemonizing>`{.interpreted-text role="ref"}.

The daemonization scripts uses the `celery multi`{.interpreted-text
role="program"} command to start one or more workers in the background:

``` console
$ celery multi start w1 -A proj -l INFO
celery multi v4.0.0 (latentcall)
> Starting nodes...
    > w1.halcyon.local: OK
```

You can restart it too:

``` console
$ celery  multi restart w1 -A proj -l INFO
celery multi v4.0.0 (latentcall)
> Stopping nodes...
    > w1.halcyon.local: TERM -> 64024
> Waiting for 1 node.....
    > w1.halcyon.local: OK
> Restarting node w1.halcyon.local: OK
celery multi v4.0.0 (latentcall)
> Stopping nodes...
    > w1.halcyon.local: TERM -> 64052
```

or stop it:

``` console
$ celery multi stop w1 -A proj -l INFO
```

The `stop` command is asynchronous so it won\'t wait for the worker to
shutdown. You\'ll probably want to use the `stopwait` command instead,
which ensures that all currently executing tasks are completed before
exiting:

``` console
$ celery multi stopwait w1 -A proj -l INFO
```

::: note
::: title
Note
:::

`celery multi`{.interpreted-text role="program"} doesn\'t store
information about workers so you need to use the same command-line
arguments when restarting. Only the same pidfile and logfile arguments
must be used when stopping.
:::

By default it\'ll create pid and log files in the current directory. To
protect against multiple workers launching on top of each other you\'re
encouraged to put these in a dedicated directory:

``` console
$ mkdir -p /var/run/celery
$ mkdir -p /var/log/celery
$ celery multi start w1 -A proj -l INFO --pidfile=/var/run/celery/%n.pid \
                                        --logfile=/var/log/celery/%n%I.log
```

With the multi command you can start multiple workers, and there\'s a
powerful command-line syntax to specify arguments for different workers
too, for example:

``` console
$ celery multi start 10 -A proj -l INFO -Q:1-3 images,video -Q:4,5 data \
    -Q default -L:4,5 debug
```

For more examples see the `~celery.bin.multi`{.interpreted-text
role="mod"} module in the API reference.

#### About the `--app <celery --app>`{.interpreted-text role="option"} argument {#app-argument}

The `--app <celery --app>`{.interpreted-text role="option"} argument
specifies the Celery app instance to use, in the form of
`module.path:attribute`

But it also supports a shortcut form. If only a package name is
specified, it\'ll try to search for the app instance, in the following
order:

With `--app=proj <celery --app>`{.interpreted-text role="option"}:

1)  an attribute named `proj.app`, or
2)  an attribute named `proj.celery`, or
3)  any attribute in the module `proj` where the value is a Celery
    application, or

If none of these are found it\'ll try a submodule named `proj.celery`:

4)  an attribute named `proj.celery.app`, or
5)  an attribute named `proj.celery.celery`, or
6)  Any attribute in the module `proj.celery` where the value is a
    Celery application.

This scheme mimics the practices used in the documentation \-- that is,
`proj:app` for a single contained module, and `proj.celery:app` for
larger projects.

## Calling Tasks

You can call a task using the `delay`{.interpreted-text role="meth"}
method:

``` pycon
>>> from proj.tasks import add

>>> add.delay(2, 2)
```

This method is actually a star-argument shortcut to another method
called `apply_async`{.interpreted-text role="meth"}:

``` pycon
>>> add.apply_async((2, 2))
```

The latter enables you to specify execution options like the time to run
(countdown), the queue it should be sent to, and so on:

``` pycon
>>> add.apply_async((2, 2), queue='lopri', countdown=10)
```

In the above example the task will be sent to a queue named `lopri` and
the task will execute, at the earliest, 10 seconds after the message was
sent.

Applying the task directly will execute the task in the current process,
so that no message is sent:

``` pycon
>>> add(2, 2)
4
```

These three methods - `delay`{.interpreted-text role="meth"},
`apply_async`{.interpreted-text role="meth"}, and applying (`__call__`),
make up the Celery calling API, which is also used for signatures.

A more detailed overview of the Calling API can be found in the
`Calling User Guide <guide-calling>`{.interpreted-text role="ref"}.

Every task invocation will be given a unique identifier (an UUID) \--
this is the task id.

The `delay` and `apply_async` methods return an
`~@AsyncResult`{.interpreted-text role="class"} instance, which can be
used to keep track of the tasks execution state. But for this you need
to enable a `result backend <task-result-backends>`{.interpreted-text
role="ref"} so that the state can be stored somewhere.

Results are disabled by default because there is no result backend that
suits every application; to choose one you need to consider the
drawbacks of each individual backend. For many tasks keeping the return
value isn\'t even very useful, so it\'s a sensible default to have. Also
note that result backends aren\'t used for monitoring tasks and workers:
for that Celery uses dedicated event messages (see
`guide-monitoring`{.interpreted-text role="ref"}).

If you have a result backend configured you can retrieve the return
value of a task:

``` pycon
>>> res = add.delay(2, 2)
>>> res.get(timeout=1)
4
```

You can find the task\'s id by looking at the `id`{.interpreted-text
role="attr"} attribute:

``` pycon
>>> res.id
d6b3aea2-fb9b-4ebc-8da4-848818db9114
```

You can also inspect the exception and traceback if the task raised an
exception, in fact `result.get()` will propagate any errors by default:

``` pycon
>>> res = add.delay(2, '2')
>>> res.get(timeout=1)
```

``` pytb
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "celery/result.py", line 221, in get
    return self.backend.wait_for_pending(
  File "celery/backends/asynchronous.py", line 195, in wait_for_pending
    return result.maybe_throw(callback=callback, propagate=propagate)
  File "celery/result.py", line 333, in maybe_throw
    self.throw(value, self._to_remote_traceback(tb))
  File "celery/result.py", line 326, in throw
    self.on_ready.throw(*args, **kwargs)
  File "vine/promises.py", line 244, in throw
    reraise(type(exc), exc, tb)
  File "vine/five.py", line 195, in reraise
    raise value
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

If you don\'t wish for the errors to propagate, you can disable that by
passing `propagate`:

``` pycon
>>> res.get(propagate=False)
TypeError("unsupported operand type(s) for +: 'int' and 'str'")
```

In this case it\'ll return the exception instance raised instead \--so
to check whether the task succeeded or failed, you\'ll have to use the
corresponding methods on the result instance:

``` pycon
>>> res.failed()
True

>>> res.successful()
False
```

So how does it know if the task has failed or not? It can find out by
looking at the tasks *state*:

``` pycon
>>> res.state
'FAILURE'
```

A task can only be in a single state, but it can progress through
several states. The stages of a typical task can be:

    PENDING -> STARTED -> SUCCESS

The started state is a special state that\'s only recorded if the
`task_track_started`{.interpreted-text role="setting"} setting is
enabled, or if the `@task(track_started=True)` option is set for the
task.

The pending state is actually not a recorded state, but rather the
default state for any task id that\'s unknown: this you can see from
this example:

``` pycon
>>> from proj.celery import app

>>> res = app.AsyncResult('this-id-does-not-exist')
>>> res.state
'PENDING'
```

If the task is retried the stages can become even more complex. To
demonstrate, for a task that\'s retried two times the stages would be:

``` text
PENDING -> STARTED -> RETRY -> STARTED -> RETRY -> STARTED -> SUCCESS
```

To read more about task states you should see the
`task-states`{.interpreted-text role="ref"} section in the tasks user
guide.

Calling tasks is described in detail in the
`Calling Guide <guide-calling>`{.interpreted-text role="ref"}.

## *Canvas*: Designing Work-flows {#designing-workflows}

You just learned how to call a task using the tasks `delay` method, and
this is often all you need. But sometimes you may want to pass the
signature of a task invocation to another process or as an argument to
another function, for which Celery uses something called *signatures*.

A signature wraps the arguments and execution options of a single task
invocation in such a way that it can be passed to functions or even
serialized and sent across the wire.

You can create a signature for the `add` task using the arguments
`(2, 2)`, and a countdown of 10 seconds like this:

``` pycon
>>> add.signature((2, 2), countdown=10)
tasks.add(2, 2)
```

There\'s also a shortcut using star arguments:

``` pycon
>>> add.s(2, 2)
tasks.add(2, 2)
```

### And there\'s that calling API again...

Signature instances also support the calling API, meaning they have
`delay` and `apply_async` methods.

But there\'s a difference in that the signature may already have an
argument signature specified. The `add` task takes two arguments, so a
signature specifying two arguments would make a complete signature:

``` pycon
>>> s1 = add.s(2, 2)
>>> res = s1.delay()
>>> res.get()
4
```

But, you can also make incomplete signatures to create what we call
*partials*:

``` pycon
# incomplete partial: add(?, 2)
>>> s2 = add.s(2)
```

`s2` is now a partial signature that needs another argument to be
complete, and this can be resolved when calling the signature:

``` pycon
# resolves the partial: add(8, 2)
>>> res = s2.delay(8)
>>> res.get()
10
```

Here you added the argument 8 that was prepended to the existing
argument 2 forming a complete signature of `add(8, 2)`.

Keyword arguments can also be added later; these are then merged with
any existing keyword arguments, but with new arguments taking
precedence:

``` pycon
>>> s3 = add.s(2, 2, debug=True)
>>> s3.delay(debug=False)   # debug is now False.
```

As stated, signatures support the calling API: meaning that

-   `sig.apply_async(args=(), kwargs={}, **options)`

    > Calls the signature with optional partial arguments and partial
    > keyword arguments. Also supports partial execution options.

-   `sig.delay(*args, **kwargs)`

    Star argument version of `apply_async`. Any arguments will be
    prepended to the arguments in the signature, and keyword arguments
    is merged with any existing keys.

So this all seems very useful, but what can you actually do with these?
To get to that I must introduce the canvas primitives...

### The Primitives

::: topic
**\\**

::: {.hlist columns="2"}
-   `group <canvas-group>`{.interpreted-text role="ref"}
-   `chain <canvas-chain>`{.interpreted-text role="ref"}
-   `chord <canvas-chord>`{.interpreted-text role="ref"}
-   `map <canvas-map>`{.interpreted-text role="ref"}
-   `starmap <canvas-map>`{.interpreted-text role="ref"}
-   `chunks <canvas-chunks>`{.interpreted-text role="ref"}
:::
:::

These primitives are signature objects themselves, so they can be
combined in any number of ways to compose complex work-flows.

::: note
::: title
Note
:::

These examples retrieve results, so to try them out you need to
configure a result backend. The example project above already does that
(see the backend argument to `~celery.Celery`{.interpreted-text
role="class"}).
:::

Let\'s look at some examples:

#### Groups

A `~celery.group`{.interpreted-text role="class"} calls a list of tasks
in parallel, and it returns a special result instance that lets you
inspect the results as a group, and retrieve the return values in order.

``` pycon
>>> from celery import group
>>> from proj.tasks import add

>>> group(add.s(i, i) for i in range(10))().get()
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

-   Partial group

``` pycon
>>> g = group(add.s(i) for i in range(10))
>>> g(10).get()
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

#### Chains

Tasks can be linked together so that after one task returns the other is
called:

``` pycon
>>> from celery import chain
>>> from proj.tasks import add, mul

# (4 + 4) * 8
>>> chain(add.s(4, 4) | mul.s(8))().get()
64
```

or a partial chain:

``` pycon
>>> # (? + 4) * 8
>>> g = chain(add.s(4) | mul.s(8))
>>> g(4).get()
64
```

Chains can also be written like this:

``` pycon
>>> (add.s(4, 4) | mul.s(8))().get()
64
```

#### Chords

A chord is a group with a callback:

``` pycon
>>> from celery import chord
>>> from proj.tasks import add, xsum

>>> chord((add.s(i, i) for i in range(10)), xsum.s())().get()
90
```

A group chained to another task will be automatically converted to a
chord:

``` pycon
>>> (group(add.s(i, i) for i in range(10)) | xsum.s())().get()
90
```

Since these primitives are all of the signature type they can be
combined almost however you want, for example:

``` pycon
>>> upload_document.s(file) | group(apply_filter.s() for filter in filters)
```

Be sure to read more about work-flows in the
`Canvas <guide-canvas>`{.interpreted-text role="ref"} user guide.

## Routing

Celery supports all of the routing facilities provided by AMQP, but it
also supports simple routing where messages are sent to named queues.

The `task_routes`{.interpreted-text role="setting"} setting enables you
to route tasks by name and keep everything centralized in one location:

``` python
app.conf.update(
    task_routes = {
        'proj.tasks.add': {'queue': 'hipri'},
    },
)
```

You can also specify the queue at runtime with the `queue` argument to
`apply_async`:

``` pycon
>>> from proj.tasks import add
>>> add.apply_async((2, 2), queue='hipri')
```

You can then make a worker consume from this queue by specifying the
`celery worker -Q`{.interpreted-text role="option"} option:

``` console
$ celery -A proj worker -Q hipri
```

You may specify multiple queues by using a comma-separated list. For
example, you can make the worker consume from both the default queue and
the `hipri` queue, where the default queue is named `celery` for
historical reasons:

``` console
$ celery -A proj worker -Q hipri,celery
```

The order of the queues doesn\'t matter as the worker will give equal
weight to the queues.

To learn more about routing, including taking use of the full power of
AMQP routing, see the `Routing Guide <guide-routing>`{.interpreted-text
role="ref"}.

## Remote Control

If you\'re using RabbitMQ (AMQP), Redis, or Qpid as the broker then you
can control and inspect the worker at runtime.

For example you can see what tasks the worker is currently working on:

``` console
$ celery -A proj inspect active
```

This is implemented by using broadcast messaging, so all remote control
commands are received by every worker in the cluster.

You can also specify one or more workers to act on the request using the
`--destination <celery inspect --destination>`{.interpreted-text
role="option"} option. This is a comma-separated list of worker host
names:

``` console
$ celery -A proj inspect active --destination=celery@example.com
```

If a destination isn\'t provided then every worker will act and reply to
the request.

The `celery inspect`{.interpreted-text role="program"} command contains
commands that don\'t change anything in the worker; it only returns
information and statistics about what\'s going on inside the worker. For
a list of inspect commands you can execute:

``` console
$ celery -A proj inspect --help
```

Then there\'s the `celery control`{.interpreted-text role="program"}
command, which contains commands that actually change things in the
worker at runtime:

``` console
$ celery -A proj control --help
```

For example you can force workers to enable event messages (used for
monitoring tasks and workers):

``` console
$ celery -A proj control enable_events
```

When events are enabled you can then start the event dumper to see what
the workers are doing:

``` console
$ celery -A proj events --dump
```

or you can start the curses interface:

``` console
$ celery -A proj events
```

when you\'re finished monitoring you can disable events again:

``` console
$ celery -A proj control disable_events
```

The `celery status`{.interpreted-text role="program"} command also uses
remote control commands and shows a list of online workers in the
cluster:

``` console
$ celery -A proj status
```

You can read more about the `celery`{.interpreted-text role="program"}
command and monitoring in the
`Monitoring Guide <guide-monitoring>`{.interpreted-text role="ref"}.

## Timezone

All times and dates, internally and in messages use the UTC timezone.

When the worker receives a message, for example with a countdown set it
converts that UTC time to local time. If you wish to use a different
timezone than the system timezone then you must configure that using the
`timezone`{.interpreted-text role="setting"} setting:

``` python
app.conf.timezone = 'Europe/London'
```

## Optimization

The default configuration isn\'t optimized for throughput. By default,
it tries to walk the middle way between many short tasks and fewer long
tasks, a compromise between throughput and fair scheduling.

If you have strict fair scheduling requirements, or want to optimize for
throughput then you should read the `Optimizing Guide
<guide-optimizing>`{.interpreted-text role="ref"}.

## What to do now?

Now that you have read this document you should continue to the
`User Guide <guide>`{.interpreted-text role="ref"}.

There\'s also an `API reference <apiref>`{.interpreted-text role="ref"}
if you\'re so inclined.
