# What\'s new in Celery 3.1 (Cipater) {#whatsnew-3.1}

Author

:   Ask Solem (`ask at celeryproject.org`)

::: sidebar
**Change history**

What\'s new documents describe the changes in major versions, we also
have a `changelog`{.interpreted-text role="ref"} that lists the changes
in bugfix releases (0.0.x), while older series are archived under the
`history`{.interpreted-text role="ref"} section.
:::

Celery is a simple, flexible, and reliable distributed system to process
vast amounts of messages, while providing operations with the tools
required to maintain such a system.

It\'s a task queue with focus on real-time processing, while also
supporting task scheduling.

Celery has a large and diverse community of users and contributors, you
should come join us `on IRC <irc-channel>`{.interpreted-text role="ref"}
or `our mailing-list <mailing-list>`{.interpreted-text role="ref"}.

To read more about Celery you should go read the
`introduction <intro>`{.interpreted-text role="ref"}.

While this version is backward compatible with previous versions it\'s
important that you read the following section.

This version is officially supported on CPython 2.6, 2.7, and 3.3, and
also supported on PyPy.

::: topic
**Table of Contents**

Make sure you read the important notes before upgrading to this version.
:::

::: {.contents local="" depth="2"}
:::

## Preface

Deadlocks have long plagued our workers, and while uncommon they\'re not
acceptable. They\'re also infamous for being extremely hard to diagnose
and reproduce, so to make this job easier I wrote a stress test suite
that bombards the worker with different tasks in an attempt to break it.

What happens if thousands of worker child processes are killed every
second? what if we also kill the broker connection every 10 seconds?
These are examples of what the stress test suite will do to the worker,
and it reruns these tests using different configuration combinations to
find edge case bugs.

The end result was that I had to rewrite the prefork pool to avoid the
use of the POSIX semaphore. This was extremely challenging, but after
months of hard work the worker now finally passes the stress test suite.

There\'s probably more bugs to find, but the good news is that we now
have a tool to reproduce them, so should you be so unlucky to experience
a bug then we\'ll write a test for it and squash it!

Note that I\'ve also moved many broker transports into experimental
status: the only transports recommended for production use today is
RabbitMQ and Redis.

I don\'t have the resources to maintain all of them, so bugs are left
unresolved. I wish that someone will step up and take responsibility for
these transports or donate resources to improve them, but as the
situation is now I don\'t think the quality is up to date with the rest
of the code-base so I cannot recommend them for production use.

The next version of Celery 4.0 will focus on performance and removing
rarely used parts of the library. Work has also started on a new message
protocol, supporting multiple languages and more. The initial draft can
be found `here <message-protocol-task-v2>`{.interpreted-text
role="ref"}.

This has probably been the hardest release I\'ve worked on, so no
introduction to this changelog would be complete without a massive thank
you to everyone who contributed and helped me test it!

Thank you for your support!

*--- Ask Solem*

## Important Notes {#v310-important}

### Dropped support for Python 2.5

Celery now requires Python 2.6 or later.

The new dual code base runs on both Python 2 and 3, without requiring
the `2to3` porting tool.

::: note
::: title
Note
:::

This is also the last version to support Python 2.6! From Celery 4.0 and
on-wards Python 2.7 or later will be required.
:::

### Last version to enable Pickle by default {#last-version-to-enable-pickle}

Starting from Celery 4.0 the default serializer will be json.

If you depend on pickle being accepted you should be prepared for this
change by explicitly allowing your worker to consume pickled messages
using the `CELERY_ACCEPT_CONTENT`{.interpreted-text role="setting"}
setting:

``` python
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']
```

Make sure you only select the serialization formats you\'ll actually be
using, and make sure you\'ve properly secured your broker from unwanted
access (see the `Security Guide <guide-security>`{.interpreted-text
role="ref"}).

The worker will emit a deprecation warning if you don\'t define this
setting.

::: topic
**for Kombu users**

Kombu 3.0 no longer accepts pickled messages by default, so if you use
Kombu directly then you have to configure your consumers: see the
`Kombu 3.0 Changelog <kombu:version-3.0.0>`{.interpreted-text
role="ref"} for more information.
:::

### Old command-line programs removed and deprecated

Everyone should move to the new `celery`{.interpreted-text
role="program"} umbrella command, so we\'re incrementally deprecating
the old command names.

In this version we\'ve removed all commands that aren\'t used in
init-scripts. The rest will be removed in 4.0.

  -------------------------------------------------------------------------------
  Program             New Status     Replacement
  ------------------- -------------- --------------------------------------------
  `celeryd`           *DEPRECATED*   `celery worker`{.interpreted-text
                                     role="program"}

  `celerybeat`        *DEPRECATED*   `celery beat`{.interpreted-text
                                     role="program"}

  `celeryd-multi`     *DEPRECATED*   `celery multi`{.interpreted-text
                                     role="program"}

  `celeryctl`         **REMOVED**    `celery inspect|control`{.interpreted-text
                                     role="program"}

  `celeryev`          **REMOVED**    `celery events`{.interpreted-text
                                     role="program"}

  `camqadm`           **REMOVED**    `celery amqp`{.interpreted-text
                                     role="program"}
  -------------------------------------------------------------------------------

If this isn\'t a new installation then you may want to remove the old
commands:

``` console
$ pip uninstall celery
$ # repeat until it fails
# ...
$ pip uninstall celery
$ pip install celery
```

Please run `celery --help`{.interpreted-text role="program"} for help
using the umbrella command.

## News {#v310-news}

### Prefork Pool Improvements

These improvements are only active if you use an async capable
transport. This means only RabbitMQ (AMQP) and Redis are supported at
this point and other transports will still use the thread-based fallback
implementation.

-   Pool is now using one IPC queue per child process.

    > Previously the pool shared one queue between all child processes,
    > using a POSIX semaphore as a mutex to achieve exclusive read and
    > write access.
    >
    > The POSIX semaphore has now been removed and each child process
    > gets a dedicated queue. This means that the worker will require
    > more file descriptors (two descriptors per process), but it also
    > means that performance is improved and we can send work to
    > individual child processes.
    >
    > POSIX semaphores aren\'t released when a process is killed, so
    > killing processes could lead to a deadlock if it happened while
    > the semaphore was acquired. There\'s no good solution to fix this,
    > so the best option was to remove the semaphore.

-   Asynchronous write operations

    > The pool now uses async I/O to send work to the child processes.

-   Lost process detection is now immediate.

    > If a child process is killed or exits mysteriously the pool
    > previously had to wait for 30 seconds before marking the task with
    > a `~celery.exceptions.WorkerLostError`{.interpreted-text
    > role="exc"}. It had to do this because the out-queue was shared
    > between all processes, and the pool couldn\'t be certain whether
    > the process completed the task or not. So an arbitrary timeout of
    > 30 seconds was chosen, as it was believed that the out-queue
    > would\'ve been drained by this point.
    >
    > This timeout is no longer necessary, and so the task can be marked
    > as failed as soon as the pool gets the notification that the
    > process exited.

-   Rare race conditions fixed

    > Most of these bugs were never reported to us, but were discovered
    > while running the new stress test suite.

#### Caveats

::: topic
**Long running tasks**

The new pool will send tasks to a child process as long as the process
in-queue is writable, and since the socket is buffered this means that
the processes are, in effect, prefetching tasks.

This benefits performance but it also means that other tasks may be
stuck waiting for a long running task to complete:

    -> send T1 to Process A
    # A executes T1
    -> send T2 to Process B
    # B executes T2
    <- T2 complete

    -> send T3 to Process A
    # A still executing T1, T3 stuck in local buffer and
    # won't start until T1 returns

The buffer size varies based on the operating system: some may have a
buffer as small as 64KB but on recent Linux versions the buffer size is
1MB (can only be changed system wide).

You can disable this prefetching behavior by enabling the
`-Ofair <celery worker -O>`{.interpreted-text role="option"} worker
option:

``` console
$ celery -A proj worker -l info -Ofair
```

With this option enabled the worker will only write to workers that are
available for work, disabling the prefetch behavior.
:::

::: topic
**Max tasks per child**

If a process exits and pool prefetch is enabled the worker may have
already written many tasks to the process in-queue, and these tasks must
then be moved back and rewritten to a new process.

This is very expensive if you have the
`--max-tasks-per-child <celery worker --max-tasks-per-child>`{.interpreted-text
role="option"} option set to a low value (e.g., less than 10), you
should not be using the `-Ofast <celery worker -O>`{.interpreted-text
role="option"} scheduler option.
:::

### Django supported out of the box

Celery 3.0 introduced a shiny new API, but unfortunately didn\'t have a
solution for Django users.

The situation changes with this version as Django is now supported in
core and new Django users coming to Celery are now expected to use the
new API directly.

The Django community has a convention where there\'s a separate
`django-x` package for every library, acting like a bridge between
Django and the library.

Having a separate project for Django users has been a pain for Celery,
with multiple issue trackers and multiple documentation sources, and
then lastly since 3.0 we even had different APIs.

With this version we challenge that convention and Django users will use
the same library, the same API and the same documentation as everyone
else.

There\'s no rush to port your existing code to use the new API, but if
you\'d like to experiment with it you should know that:

-   You need to use a Celery application instance.

    > The new Celery API introduced in 3.0 requires users to instantiate
    > the library by creating an application:
    >
    > ``` python
    > from celery import Celery
    >
    > app = Celery()
    > ```

-   You need to explicitly integrate Celery with Django

    > Celery won\'t automatically use the Django settings, so you can
    > either configure Celery separately or you can tell it to use the
    > Django settings with:
    >
    > ``` python
    > app.config_from_object('django.conf:settings')
    > ```
    >
    > Neither will it automatically traverse your installed apps to find
    > task modules. If you want this behavior, you must explicitly pass
    > a list of Django instances to the Celery app:
    >
    > ``` python
    > from django.conf import settings
    > app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
    > ```

-   You no longer use `manage.py`

    > Instead you use the `celery`{.interpreted-text role="program"}
    > command directly:
    >
    > ``` console
    > $ celery -A proj worker -l info
    > ```
    >
    > For this to work your app module must store the
    > `DJANGO_SETTINGS_MODULE`{.interpreted-text role="envvar"}
    > environment variable, see the example in the `Django
    > guide <django-first-steps>`{.interpreted-text role="ref"}.

To get started with the new API you should first read the
`first-steps`{.interpreted-text role="ref"} tutorial, and then you
should read the Django-specific instructions in
`django-first-steps`{.interpreted-text role="ref"}.

The fixes and improvements applied by the
`django-celery`{.interpreted-text role="pypi"} library are now
automatically applied by core Celery when it detects that the
`DJANGO_SETTINGS_MODULE`{.interpreted-text role="envvar"} environment
variable is set.

The distribution ships with a new example project using Django in
`examples/django`{.interpreted-text role="file"}:

<https://github.com/celery/celery/tree/3.1/examples/django>

Some features still require the `django-celery`{.interpreted-text
role="pypi"} library:

> -   Celery doesn\'t implement the Django database or cache result
>     backends.
>
> -   
>
>     Celery doesn\'t ship with the database-based periodic task
>
>     :   scheduler.

::: note
::: title
Note
:::

If you\'re still using the old API when you upgrade to Celery 3.1 then
you must make sure that your settings module contains the
`djcelery.setup_loader()` line, since this will no longer happen as a
side-effect of importing the `django-celery`{.interpreted-text
role="pypi"} module.

New users (or if you\'ve ported to the new API) don\'t need the
`setup_loader` line anymore, and must make sure to remove it.
:::

### Events are now ordered using logical time

Keeping physical clocks in perfect sync is impossible, so using
time-stamps to order events in a distributed system isn\'t reliable.

Celery event messages have included a logical clock value for some time,
but starting with this version that field is also used to order them.

Also, events now record timezone information by including a new
`utcoffset` field in the event message. This is a signed integer telling
the difference from UTC time in hours, so for example, an event sent
from the Europe/London timezone in daylight savings time will have an
offset of 1.

`@events.Receiver`{.interpreted-text role="class"} will automatically
convert the time-stamps to the local timezone.

::: note
::: title
Note
:::

The logical clock is synchronized with other nodes in the same cluster
(neighbors), so this means that the logical epoch will start at the
point when the first worker in the cluster starts.

If all of the workers are shutdown the clock value will be lost and
reset to 0. To protect against this, you should specify the
`celery worker --statedb`{.interpreted-text role="option"} option such
that the worker can persist the clock value at shutdown.

You may notice that the logical clock is an integer value and increases
very rapidly. Don\'t worry about the value overflowing though, as even
in the most busy clusters it may take several millennium before the
clock exceeds a 64 bits value.
:::

### New worker node name format (`name@host`)

Node names are now constructed by two elements: name and host-name
separated by \'@\'.

This change was made to more easily identify multiple instances running
on the same machine.

If a custom name isn\'t specified then the worker will use the name
\'celery\' by default, resulting in a fully qualified node name of
\'<celery@hostname>\':

``` console
$ celery worker -n example.com
celery@example.com
```

To also set the name you must include the @:

``` console
$ celery worker -n worker1@example.com
worker1@example.com
```

The worker will identify itself using the fully qualified node name in
events and broadcast messages, so where before a worker would identify
itself as \'worker1.example.com\', it\'ll now use
\'<celery@worker1.example.com>\'.

Remember that the `-n <celery worker -n>`{.interpreted-text
role="option"} argument also supports simple variable substitutions, so
if the current host-name is *george.example.com* then the `%h` macro
will expand into that:

``` console
$ celery worker -n worker1@%h
worker1@george.example.com
```

The available substitutions are as follows:

  --------------------------------------------------------
  Variable        Substitution
  --------------- ----------------------------------------
  `%h`            Full host-name (including domain name)

  `%d`            Domain name only

  `%n`            Host-name only (without domain name)

  `%%`            The character `%`
  --------------------------------------------------------

### Bound tasks

The task decorator can now create \"bound tasks\", which means that the
task will receive the `self` argument.

``` python
@app.task(bind=True)
def send_twitter_status(self, oauth, tweet):
    try:
        twitter = Twitter(oauth)
        twitter.update_status(tweet)
    except (Twitter.FailWhaleError, Twitter.LoginError) as exc:
        raise self.retry(exc=exc)
```

Using *bound tasks* is now the recommended approach whenever you need
access to the task instance or request context. Previously one would\'ve
to refer to the name of the task instead (`send_twitter_status.retry`),
but this could lead to problems in some configurations.

### Mingle: Worker synchronization

The worker will now attempt to synchronize with other workers in the
same cluster.

Synchronized data currently includes revoked tasks and logical clock.

This only happens at start-up and causes a one second start-up delay to
collect broadcast responses from other workers.

You can disable this bootstep using the
`celery worker --without-mingle`{.interpreted-text role="option"}
option.

### Gossip: Worker \<-\> Worker communication

Workers are now passively subscribing to worker related events like
heartbeats.

This means that a worker knows what other workers are doing and can
detect if they go offline. Currently this is only used for clock
synchronization, but there are many possibilities for future additions
and you can write extensions that take advantage of this already.

Some ideas include consensus protocols, reroute task to best worker
(based on resource usage or data locality) or restarting workers when
they crash.

We believe that although this is a small addition, it opens amazing
possibilities.

You can disable this bootstep using the
`celery worker --without-gossip`{.interpreted-text role="option"}
option.

### Bootsteps: Extending the worker

By writing bootsteps you can now easily extend the consumer part of the
worker to add additional features, like custom message consumers.

The worker has been using bootsteps for some time, but these were never
documented. In this version the consumer part of the worker has also
been rewritten to use bootsteps and the new
`guide-extending`{.interpreted-text role="ref"} guide documents examples
extending the worker, including adding custom message consumers.

See the `guide-extending`{.interpreted-text role="ref"} guide for more
information.

::: note
::: title
Note
:::

Bootsteps written for older versions won\'t be compatible with this
version, as the API has changed significantly.

The old API was experimental and internal but should you be so unlucky
to use it then please contact the mailing-list and we\'ll help you port
the bootstep to the new API.
:::

### New RPC result backend

This new experimental version of the `amqp` result backend is a good
alternative to use in classical RPC scenarios, where the process that
initiates the task is always the process to retrieve the result.

It uses Kombu to send and retrieve results, and each client uses a
unique queue for replies to be sent to. This avoids the significant
overhead of the original amqp result backend which creates one queue per
task.

By default results sent using this backend won\'t persist, so they
won\'t survive a broker restart. You can enable the
`CELERY_RESULT_PERSISTENT`{.interpreted-text role="setting"} setting to
change that.

``` python
CELERY_RESULT_BACKEND = 'rpc'
CELERY_RESULT_PERSISTENT = True
```

Note that chords are currently not supported by the RPC backend.

### Time limits can now be set by the client

Two new options have been added to the Calling API: `time_limit` and
`soft_time_limit`:

``` pycon
>>> res = add.apply_async((2, 2), time_limit=10, soft_time_limit=8)

>>> res = add.subtask((2, 2), time_limit=10, soft_time_limit=8).delay()

>>> res = add.s(2, 2).set(time_limit=10, soft_time_limit=8).delay()
```

Contributed by Mher Movsisyan.

### Redis: Broadcast messages and virtual hosts

Broadcast messages are currently seen by all virtual hosts when using
the Redis transport. You can now fix this by enabling a prefix to all
channels so that the messages are separated:

``` python
BROKER_TRANSPORT_OPTIONS = {'fanout_prefix': True}
```

Note that you\'ll not be able to communicate with workers running older
versions or workers that doesn\'t have this setting enabled.

This setting will be the default in a future version.

Related to Issue #1490.

### `pytz`{.interpreted-text role="pypi"} replaces `python-dateutil`{.interpreted-text role="pypi"} dependency

Celery no longer depends on the `python-dateutil`{.interpreted-text
role="pypi"} library, but instead a new dependency on the
`pytz`{.interpreted-text role="pypi"} library was added.

The `pytz`{.interpreted-text role="pypi"} library was already
recommended for accurate timezone support.

This also means that dependencies are the same for both Python 2 and
Python 3, and that the `requirements/default-py3k.txt`{.interpreted-text
role="file"} file has been removed.

### Support for `setuptools`{.interpreted-text role="pypi"} extra requirements

Pip now supports the `setuptools`{.interpreted-text role="pypi"} extra
requirements format, so we\'ve removed the old bundles concept, and
instead specify setuptools extras.

You install extras by specifying them inside brackets:

``` console
$ pip install celery[redis,mongodb]
```

The above will install the dependencies for Redis and MongoDB. You can
list as many extras as you want.

::: warning
::: title
Warning
:::

You can\'t use the `celery-with-*` packages anymore, as these won\'t be
updated to use Celery 3.1.
:::

  -------------------------------------------------------------------
  Extension     Requirement entry         Type
  ------------- ------------------------- ---------------------------
  Redis         `celery[redis]`           transport, result backend

  MongoDB       `celery[mongodb]`         transport, result backend

  CouchDB       `celery[couchdb]`         transport

  Beanstalk     `celery[beanstalk]`       transport

  ZeroMQ        `celery[zeromq]`          transport

  Zookeeper     `celery[zookeeper]`       transport

  SQLAlchemy    `celery[sqlalchemy]`      transport, result backend

  librabbitmq   `celery[librabbitmq]`     transport (C amqp client)
  -------------------------------------------------------------------

The complete list with examples is found in the
`bundles`{.interpreted-text role="ref"} section.

### `subtask.__call__()` now executes the task directly

A misunderstanding led to `Signature.__call__` being an alias of
`.delay` but this doesn\'t conform to the calling API of `Task` which
calls the underlying task method.

This means that:

``` python
@app.task
def add(x, y):
    return x + y

add.s(2, 2)()
```

now does the same as calling the task directly:

``` pycon
>>> add(2, 2)
```

### In Other News

-   Now depends on `Kombu 3.0 <kombu:version-3.0.0>`{.interpreted-text
    role="ref"}.

-   Now depends on `billiard`{.interpreted-text role="pypi"} version
    3.3.

-   Worker will now crash if running as the root user with pickle
    enabled.

-   Canvas: `group.apply_async` and `chain.apply_async` no longer starts
    separate task.

    > That the group and chord primitives supported the \"calling API\"
    > like other subtasks was a nice idea, but it was useless in
    > practice and often confused users. If you still want this behavior
    > you can define a task to do it for you.

-   New method `Signature.freeze()` can be used to \"finalize\"
    signatures/subtask.

    > Regular signature:
    >
    > ``` pycon
    > >>> s = add.s(2, 2)
    > >>> result = s.freeze()
    > >>> result
    > <AsyncResult: ffacf44b-f8a1-44e9-80a3-703150151ef2>
    > >>> s.delay()
    > <AsyncResult: ffacf44b-f8a1-44e9-80a3-703150151ef2>
    > ```
    >
    > Group:
    >
    > ``` pycon
    > >>> g = group(add.s(2, 2), add.s(4, 4))
    > >>> result = g.freeze()
    > <GroupResult: e1094b1d-08fc-4e14-838e-6d601b99da6d [
    >     70c0fb3d-b60e-4b22-8df7-aa25b9abc86d,
    >     58fcd260-2e32-4308-a2ea-f5be4a24f7f4]>
    > >>> g()
    > <GroupResult: e1094b1d-08fc-4e14-838e-6d601b99da6d [70c0fb3d-b60e-4b22-8df7-aa25b9abc86d, 58fcd260-2e32-4308-a2ea-f5be4a24f7f4]>
    > ```

-   Chord exception behavior defined (Issue #1172).

    > From this version the chord callback will change state to FAILURE
    > when a task part of a chord raises an exception.
    >
    > See more at `chord-errors`{.interpreted-text role="ref"}.

-   New ability to specify additional command line options to the worker
    and beat programs.

    > The `@user_options`{.interpreted-text role="attr"} attribute can
    > be used to add additional command-line arguments, and expects
    > `optparse`{.interpreted-text role="mod"}-style options:
    >
    > ``` python
    > from celery import Celery
    > from celery.bin import Option
    >
    > app = Celery()
    > app.user_options['worker'].add(
    >     Option('--my-argument'),
    > )
    > ```
    >
    > See the `guide-extending`{.interpreted-text role="ref"} guide for
    > more information.

-   All events now include a `pid` field, which is the process id of the
    process that sent the event.

-   Event heartbeats are now calculated based on the time when the event
    was received by the monitor, and not the time reported by the
    worker.

    > This means that a worker with an out-of-sync clock will no longer
    > show as \'Offline\' in monitors.
    >
    > A warning is now emitted if the difference between the senders
    > time and the internal time is greater than 15 seconds, suggesting
    > that the clocks are out of sync.

-   Monotonic clock support.

    > A monotonic clock is now used for timeouts and scheduling.
    >
    > The monotonic clock function is built-in starting from Python 3.4,
    > but we also have fallback implementations for Linux and macOS.

-   `celery worker`{.interpreted-text role="program"} now supports a new
    `--detach <celery worker --detach>`{.interpreted-text role="option"}
    argument to start the worker as a daemon in the background.

-   `@events.Receiver`{.interpreted-text role="class"} now sets a
    `local_received` field for incoming events, which is set to the time
    of when the event was received.

-   `@events.Dispatcher`{.interpreted-text role="class"} now accepts a
    `groups` argument which decides a white-list of event groups
    that\'ll be sent.

    > The type of an event is a string separated by \'-\', where the
    > part before the first \'-\' is the group. Currently there are only
    > two groups: `worker` and `task`.
    >
    > A dispatcher instantiated as follows:
    >
    > ``` pycon
    > >>> app.events.Dispatcher(connection, groups=['worker'])
    > ```
    >
    > will only send worker related events and silently drop any
    > attempts to send events related to any other group.

-   New `BROKER_FAILOVER_STRATEGY`{.interpreted-text role="setting"}
    setting.

    > This setting can be used to change the transport fail-over
    > strategy, can either be a callable returning an iterable or the
    > name of a Kombu built-in failover strategy. Default is
    > \"round-robin\".
    >
    > Contributed by Matt Wise.

-   `Result.revoke` will no longer wait for replies.

    > You can add the `reply=True` argument if you really want to wait
    > for responses from the workers.

-   Better support for link and link_error tasks for chords.

    > Contributed by Steeve Morin.

-   Worker: Now emits warning if the `CELERYD_POOL`{.interpreted-text
    role="setting"} setting is set to enable the eventlet/gevent pools.

    > The [-P]{.title-ref} option should always be used to select the
    > eventlet/gevent pool to ensure that the patches are applied as
    > early as possible.
    >
    > If you start the worker in a wrapper (like Django\'s
    > `manage.py`{.interpreted-text role="file"}) then you must apply
    > the patches manually, for example by creating an alternative
    > wrapper that monkey patches at the start of the program before
    > importing any other modules.

-   There\'s a now an \'inspect clock\' command which will collect the
    current logical clock value from workers.

-   [celery inspect stats]{.title-ref} now contains the process id of
    the worker\'s main process.

    > Contributed by Mher Movsisyan.

-   New remote control command to dump a workers configuration.

    > Example:
    >
    > ``` console
    > $ celery inspect conf
    > ```
    >
    > Configuration values will be converted to values supported by JSON
    > where possible.
    >
    > Contributed by Mher Movsisyan.

-   New settings `CELERY_EVENT_QUEUE_TTL`{.interpreted-text
    role="setting"} and `CELERY_EVENT_QUEUE_EXPIRES`{.interpreted-text
    role="setting"}.

    > These control when a monitors event queue is deleted, and for how
    > long events published to that queue will be visible. Only
    > supported on RabbitMQ.

-   New Couchbase result backend.

    > This result backend enables you to store and retrieve task results
    > using [Couchbase]().
    >
    > See `conf-couchbase-result-backend`{.interpreted-text role="ref"}
    > for more information about configuring this result backend.
    >
    > Contributed by Alain Masiero.

-   CentOS init-script now supports starting multiple worker instances.

    > See the script header for details.
    >
    > Contributed by Jonathan Jordan.

-   `AsyncResult.iter_native` now sets default interval parameter to 0.5

    > Fix contributed by Idan Kamara

-   New setting `BROKER_LOGIN_METHOD`{.interpreted-text role="setting"}.

    > This setting can be used to specify an alternate login method for
    > the AMQP transports.
    >
    > Contributed by Adrien Guinet

-   The `dump_conf` remote control command will now give the string
    representation for types that aren\'t JSON compatible.

-   Function [celery.security.setup_security]{.title-ref} is now
    `@setup_security`{.interpreted-text role="func"}.

-   Task retry now propagates the message expiry value (Issue #980).

    > The value is forwarded at is, so the expiry time won\'t change. To
    > update the expiry time you\'d\'ve to pass a new expires argument
    > to `retry()`.

-   Worker now crashes if a channel error occurs.

    > Channel errors are transport specific and is the list of
    > exceptions returned by `Connection.channel_errors`. For RabbitMQ
    > this means that Celery will crash if the equivalence checks for
    > one of the queues in `CELERY_QUEUES`{.interpreted-text
    > role="setting"} mismatches, which makes sense since this is a
    > scenario where manual intervention is required.

-   Calling `AsyncResult.get()` on a chain now propagates errors for
    previous tasks (Issue #1014).

-   The parent attribute of `AsyncResult` is now reconstructed when
    using JSON serialization (Issue #1014).

-   Worker disconnection logs are now logged with severity warning
    instead of error.

    > Contributed by Chris Adams.

-   `events.State` no longer crashes when it receives unknown event
    types.

-   SQLAlchemy Result Backend: New
    `CELERY_RESULT_DB_TABLENAMES`{.interpreted-text role="setting"}
    setting can be used to change the name of the database tables used.

    > Contributed by Ryan Petrello.

-   

    SQLAlchemy Result Backend: Now calls `enginge.dispose` after fork

    :   (Issue #1564).

        > If you create your own SQLAlchemy engines then you must also
        > make sure that these are closed after fork in the worker:
        >
        > ``` python
        > from multiprocessing.util import register_after_fork
        >
        > engine = create_engine(*engine_args)
        > register_after_fork(engine, engine.dispose)
        > ```

-   A stress test suite for the Celery worker has been written.

    > This is located in the `funtests/stress` directory in the git
    > repository. There\'s a README file there to get you started.

-   The logger named `celery.concurrency` has been renamed to
    `celery.pool`.

-   New command line utility `celery graph`.

    > This utility creates graphs in GraphViz dot format.
    >
    > You can create graphs from the currently installed bootsteps:
    >
    > ``` console
    > # Create graph of currently installed bootsteps in both the worker
    > # and consumer name-spaces.
    > $ celery graph bootsteps | dot -T png -o steps.png
    >
    > # Graph of the consumer name-space only.
    > $ celery graph bootsteps consumer | dot -T png -o consumer_only.png
    >
    > # Graph of the worker name-space only.
    > $ celery graph bootsteps worker | dot -T png -o worker_only.png
    > ```
    >
    > Or graphs of workers in a cluster:
    >
    > ``` console
    > # Create graph from the current cluster
    > $ celery graph workers | dot -T png -o workers.png
    >
    > # Create graph from a specified list of workers
    > $ celery graph workers nodes:w1,w2,w3 | dot -T png workers.png
    >
    > # also specify the number of threads in each worker
    > $ celery graph workers nodes:w1,w2,w3 threads:2,4,6
    >
    > # …also specify the broker and backend URLs shown in the graph
    > $ celery graph workers broker:amqp:// backend:redis://
    >
    > # …also specify the max number of workers/threads shown (wmax/tmax),
    > # enumerating anything that exceeds that number.
    > $ celery graph workers wmax:10 tmax:3
    > ```

-   Changed the way that app instances are pickled.

    > Apps can now define a `__reduce_keys__` method that\'s used
    > instead of the old `AppPickler` attribute. For example, if your
    > app defines a custom \'foo\' attribute that needs to be preserved
    > when pickling you can define a `__reduce_keys__` as such:
    >
    > ``` python
    > import celery
    >
    > class Celery(celery.Celery):
    >
    >     def __init__(self, *args, **kwargs):
    >         super(Celery, self).__init__(*args, **kwargs)
    >         self.foo = kwargs.get('foo')
    >
    >     def __reduce_keys__(self):
    >         return super(Celery, self).__reduce_keys__().update(
    >             foo=self.foo,
    >         )
    > ```
    >
    > This is a much more convenient way to add support for pickling
    > custom attributes. The old `AppPickler` is still supported but its
    > use is discouraged and we would like to remove it in a future
    > version.

-   Ability to trace imports for debugging purposes.

    > The `C_IMPDEBUG`{.interpreted-text role="envvar"} can be set to
    > trace imports as they occur:
    >
    > ``` console
    > $ C_IMDEBUG=1 celery worker -l info
    > ```
    >
    > ``` console
    > $ C_IMPDEBUG=1 celery shell
    > ```

-   Message headers now available as part of the task request.

    > Example adding and retrieving a header value:
    >
    > ``` python
    > @app.task(bind=True)
    > def t(self):
    >     return self.request.headers.get('sender')
    >
    > >>> t.apply_async(headers={'sender': 'George Costanza'})
    > ```

-   New `before_task_publish`{.interpreted-text role="signal"} signal
    dispatched before a task message is sent and can be used to modify
    the final message fields (Issue #1281).

-   New `after_task_publish`{.interpreted-text role="signal"} signal
    replaces the old `task_sent`{.interpreted-text role="signal"}
    signal.

    > The `task_sent`{.interpreted-text role="signal"} signal is now
    > deprecated and shouldn\'t be used.

-   New `worker_process_shutdown`{.interpreted-text role="signal"}
    signal is dispatched in the prefork pool child processes as they
    exit.

    > Contributed by Daniel M Taub.

-   `celery.platforms.PIDFile` renamed to
    `celery.platforms.Pidfile`{.interpreted-text role="class"}.

-   MongoDB Backend: Can now be configured using a URL:

-   MongoDB Backend: No longer using deprecated `pymongo.Connection`.

-   MongoDB Backend: Now disables `auto_start_request`.

-   MongoDB Backend: Now enables `use_greenlets` when eventlet/gevent is
    used.

-   `subtask()` / `maybe_subtask()` renamed to
    `signature()`/`maybe_signature()`.

    > Aliases still available for backwards compatibility.

-   The `correlation_id` message property is now automatically set to
    the id of the task.

-   The task message `eta` and `expires` fields now includes timezone
    information.

-   All result backends `store_result`/`mark_as_*` methods must now
    accept a `request` keyword argument.

-   Events now emit warning if the broken `yajl` library is used.

-   The `celeryd_init`{.interpreted-text role="signal"} signal now takes
    an extra keyword argument: `option`.

    > This is the mapping of parsed command line arguments, and can be
    > used to prepare new preload arguments
    > (`app.user_options['preload']`).

-   New callback: `@on_configure`{.interpreted-text role="meth"}.

    > This callback is called when an app is about to be configured (a
    > configuration key is required).

-   Worker: No longer forks on `HUP`{.interpreted-text role="sig"}.

    > This means that the worker will reuse the same pid for better
    > support with external process supervisors.
    >
    > Contributed by Jameel Al-Aziz.

-   Worker: The log message `Got task from broker …` was changed to
    `Received task …`.

-   Worker: The log message `Skipping revoked task …` was changed to
    `Discarding revoked task …`.

-   Optimization: Improved performance of `ResultSet.join_native()`.

    > Contributed by Stas Rudakou.

-   The `task_revoked`{.interpreted-text role="signal"} signal now
    accepts new `request` argument (Issue #1555).

    > The revoked signal is dispatched after the task request is removed
    > from the stack, so it must instead use the
    > `~celery.worker.request.Request`{.interpreted-text role="class"}
    > object to get information about the task.

-   Worker: New `-X <celery worker -X>`{.interpreted-text role="option"}
    command line argument to exclude queues (Issue #1399).

    > The `-X <celery worker -X>`{.interpreted-text role="option"}
    > argument is the inverse of the
    > `-Q <celery worker -Q>`{.interpreted-text role="option"} argument
    > and accepts a list of queues to exclude (not consume from):
    >
    > ``` console
    > # Consume from all queues in CELERY_QUEUES, but not the 'foo' queue.
    > $ celery worker -A proj -l info -X foo
    > ```

-   Adds `C_FAKEFORK`{.interpreted-text role="envvar"} environment
    variable for simple init-script/`celery multi`{.interpreted-text
    role="program"} debugging.

    > This means that you can now do:
    >
    > ``` console
    > $ C_FAKEFORK=1 celery multi start 10
    > ```
    >
    > or:
    >
    > ``` console
    > $ C_FAKEFORK=1 /etc/init.d/celeryd start
    > ```
    >
    > to avoid the daemonization step to see errors that aren\'t visible
    > due to missing stdout/stderr.
    >
    > A `dryrun` command has been added to the generic init-script that
    > enables this option.

-   New public API to push and pop from the current task stack:

    > `celery.app.push_current_task`{.interpreted-text role="func"} and
    > `celery.app.pop_current_task`{.interpreted-text role="func"}\`.

-   `RetryTaskError` has been renamed to
    `~celery.exceptions.Retry`{.interpreted-text role="exc"}.

    > The old name is still available for backwards compatibility.

-   New semi-predicate exception
    `~celery.exceptions.Reject`{.interpreted-text role="exc"}.

    > This exception can be raised to `reject`/`requeue` the task
    > message, see `task-semipred-reject`{.interpreted-text role="ref"}
    > for examples.

-   `Semipredicates <task-semipredicates>`{.interpreted-text role="ref"}
    documented: (Retry/Ignore/Reject).

## Scheduled Removals {#v310-removals}

-   The `BROKER_INSIST` setting and the `insist` argument to
    `~@connection` is no longer supported.

-   The `CELERY_AMQP_TASK_RESULT_CONNECTION_MAX` setting is no longer
    supported.

    > Use `BROKER_POOL_LIMIT`{.interpreted-text role="setting"} instead.

-   The `CELERY_TASK_ERROR_WHITELIST` setting is no longer supported.

    > You should set the
    > `~celery.utils.mail.ErrorMail`{.interpreted-text role="class"}
    > attribute of the task class instead. You can also do this using
    > `CELERY_ANNOTATIONS`{.interpreted-text role="setting"}:
    >
    > > ``` python
    > > from celery import Celery
    > > from celery.utils.mail import ErrorMail
    > >
    > > class MyErrorMail(ErrorMail):
    > >     whitelist = (KeyError, ImportError)
    > >
    > >     def should_send(self, context, exc):
    > >         return isinstance(exc, self.whitelist)
    > >
    > > app = Celery()
    > > app.conf.CELERY_ANNOTATIONS = {
    > >     '*': {
    > >         'ErrorMail': MyErrorMails,
    > >     }
    > > }
    > > ```

-   Functions that creates a broker connections no longer supports the
    `connect_timeout` argument.

    > This can now only be set using the
    > `BROKER_CONNECTION_TIMEOUT`{.interpreted-text role="setting"}
    > setting. This is because functions no longer create connections
    > directly, but instead get them from the connection pool.

-   The `CELERY_AMQP_TASK_RESULT_EXPIRES` setting is no longer
    supported.

    > Use `CELERY_TASK_RESULT_EXPIRES`{.interpreted-text role="setting"}
    > instead.

## Deprecation Time-line Changes {#v310-deprecations}

See the `deprecation-timeline`{.interpreted-text role="ref"}.

## Fixes {#v310-fixes}

-   AMQP Backend: join didn\'t convert exceptions when using the json
    serializer.

-   Non-abstract task classes are now shared between apps (Issue #1150).

    > Note that non-abstract task classes shouldn\'t be used in the new
    > API. You should only create custom task classes when you use them
    > as a base class in the `@task` decorator.
    >
    > This fix ensure backwards compatibility with older Celery versions
    > so that non-abstract task classes works even if a module is
    > imported multiple times so that the app is also instantiated
    > multiple times.

-   Worker: Workaround for Unicode errors in logs (Issue #427).

-   Task methods: `.apply_async` now works properly if args list is None
    (Issue #1459).

-   Eventlet/gevent/solo/threads pools now properly handles
    `BaseException`{.interpreted-text role="exc"} errors raised by
    tasks.

-   `autoscale`{.interpreted-text role="control"} and
    `pool_grow`{.interpreted-text
    role="control"}/`pool_shrink`{.interpreted-text role="control"}
    remote control commands will now also automatically increase and
    decrease the consumer prefetch count.

    > Fix contributed by Daniel M. Taub.

-   `celery control pool_` commands didn\'t coerce string arguments to
    int.

-   Redis/Cache chords: Callback result is now set to failure if the
    group disappeared from the database (Issue #1094).

-   Worker: Now makes sure that the shutdown process isn\'t initiated
    more than once.

-   Programs: `celery multi`{.interpreted-text role="program"} now
    properly handles both `-f` and
    `--logfile <celery worker --logfile>`{.interpreted-text
    role="option"} options (Issue #1541).

## Internal changes {#v310-internal}

-   Module `celery.task.trace` has been renamed to
    `celery.app.trace`{.interpreted-text role="mod"}.

-   Module `celery.concurrency.processes` has been renamed to
    `celery.concurrency.prefork`{.interpreted-text role="mod"}.

-   Classes that no longer fall back to using the default app:

    > -   Result backends
    >     (`celery.backends.base.BaseBackend`{.interpreted-text
    >     role="class"})
    > -   `celery.worker.WorkController`{.interpreted-text role="class"}
    > -   `celery.worker.Consumer`{.interpreted-text role="class"}
    > -   `celery.worker.request.Request`{.interpreted-text
    >     role="class"}
    >
    > This means that you have to pass a specific app when instantiating
    > these classes.

-   `EventDispatcher.copy_buffer` renamed to
    `@events.Dispatcher.extend_buffer`{.interpreted-text role="meth"}.

-   Removed unused and never documented global instance
    `celery.events.state.state`.

-   `@events.Receiver`{.interpreted-text role="class"} is now a
    `kombu.mixins.ConsumerMixin`{.interpreted-text role="class"}
    subclass.

-   `celery.apps.worker.Worker`{.interpreted-text role="class"} has been
    refactored as a subclass of
    `celery.worker.WorkController`{.interpreted-text role="class"}.

    > This removes a lot of duplicate functionality.

-   The `Celery.with_default_connection` method has been removed in
    favor of `with app.connection_or_acquire`
    (`@connection_or_acquire`{.interpreted-text role="meth"})

-   The `celery.results.BaseDictBackend` class has been removed and is
    replaced by `celery.results.BaseBackend`{.interpreted-text
    role="class"}.
