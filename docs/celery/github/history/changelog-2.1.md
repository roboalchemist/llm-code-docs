# Change history for Celery 2.1 {#changelog-2.1}

::: {.contents local=""}
:::

## 2.1.4 {#version-2.1.4}

release-date

:   2010-12-03 12:00 p.m. CEST

release-by

:   Ask Solem

### Fixes {#v214-fixes}

-   Execution options to [apply_async]{.title-ref} now takes precedence
    over options returned by active routers. This was a regression
    introduced recently (Issue #244).

-   curses monitor: Long arguments are now truncated so curses doesn\'t
    crash with out of bounds errors (Issue #235).

-   multi: Channel errors occurring while handling control commands no
    longer crash the worker but are instead logged with severity error.

-   SQLAlchemy database backend: Fixed a race condition occurring when
    the client wrote the pending state. Just like the Django database
    backend, it does no longer save the pending state (Issue #261 +
    Issue #262).

-   Error email body now uses [repr(exception)]{.title-ref} instead of
    [str(exception)]{.title-ref}, as the latter could result in Unicode
    decode errors (Issue #245).

-   Error email timeout value is now configurable by using the
    `EMAIL_TIMEOUT`{.interpreted-text role="setting"} setting.

-   \`celeryev\`: Now works on Windows (but the curses monitor won\'t
    work without having curses).

-   Unit test output no longer emits non-standard characters.

-   worker: The broadcast consumer is now closed if the connection is
    reset.

-   worker: Now properly handles errors occurring while trying to
    acknowledge the message.

-   

    [TaskRequest.on_failure]{.title-ref} now encodes traceback using the current file-system

    :   encoding (Issue #286).

-   [EagerResult]{.title-ref} can now be pickled (Issue #288).

### Documentation {#v214-documentation}

-   Adding `contributing`{.interpreted-text role="ref"}.
-   Added `guide-optimizing`{.interpreted-text role="ref"}.
-   Added `faq-security`{.interpreted-text role="ref"} section to the
    FAQ.

## 2.1.3 {#version-2.1.3}

release-date

:   2010-11-09 05:00 p.m. CEST

release-by

:   Ask Solem

::: {#v213-fixes}
-   Fixed deadlocks in [timer2]{.title-ref} which could lead to
    [djcelerymon]{.title-ref}/[celeryev -c]{.title-ref} hanging.

-   \`EventReceiver\`: now sends heartbeat request to find workers.

    > This means `celeryev`{.interpreted-text role="program"} and
    > friends finds workers immediately at start-up.

-   `celeryev` curses monitor: Set screen_delay to 10ms, so the screen
    refreshes more often.

-   Fixed pickling errors when pickling `AsyncResult`{.interpreted-text
    role="class"} on older Python versions.

-   worker: prefetch count was decremented by ETA tasks even if there
    were no active prefetch limits.
:::

## 2.1.2 {#version-2.1.2}

release-data

:   TBA

### Fixes {#v212-fixes}

-   worker: Now sends the `task-retried`{.interpreted-text role="event"}
    event for retried tasks.
-   worker: Now honors ignore result for
    `~@WorkerLostError`{.interpreted-text role="exc"} and timeout
    errors.
-   `celerybeat`: Fixed `UnboundLocalError`{.interpreted-text
    role="exc"} in `celerybeat` logging when using logging setup
    signals.
-   worker: All log messages now includes [exc_info]{.title-ref}.

## 2.1.1 {#version-2.1.1}

release-date

:   2010-10-14 02:00 p.m. CEST

release-by

:   Ask Solem

### Fixes {#v211-fixes}

-   Now working on Windows again.

    > Removed dependency on the `pwd`{.interpreted-text
    > role="mod"}/`grp`{.interpreted-text role="mod"} modules.

-   snapshots: Fixed race condition leading to loss of events.

-   worker: Reject tasks with an ETA that cannot be converted to a time
    stamp.

    > See issue #209

-   concurrency.processes.pool: The semaphore was released twice for
    each task (both at ACK and result ready).

    > This has been fixed, and it is now released only once per task.

-   docs/configuration: Fixed typo
    [CELERYD_TASK_SOFT_TIME_LIMIT]{.title-ref} -\>
    `CELERYD_TASK_SOFT_TIME_LIMIT`{.interpreted-text role="setting"}.

    > See issue #214

-   control command \`dump_scheduled\`: was using old .info attribute

-   

    multi: Fixed [set changed size during iteration]{.title-ref} bug

    :   occurring in the restart command.

-   worker: Accidentally tried to use additional command-line arguments.

    > This would lead to an error like:
    >
    > > [got multiple values for keyword argument
    > > \'concurrency\']{.title-ref}.
    > >
    > > Additional command-line arguments are now ignored, and doesn\'t
    > > produce this error. However \-- we do reserve the right to use
    > > positional arguments in the future, so please don\'t depend on
    > > this behavior.

-   `celerybeat`: Now respects routers and task execution options again.

-   `celerybeat`: Now reuses the publisher instead of the connection.

-   Cache result backend: Using `float`{.interpreted-text role="class"}
    as the expires argument to [cache.set]{.title-ref} is deprecated by
    the Memcached libraries, so we now automatically cast to
    `int`{.interpreted-text role="class"}.

-   unit tests: No longer emits logging and warnings in test output.

### News {#v211-news}

-   Now depends on carrot version 0.10.7.

-   Added `CELERY_REDIRECT_STDOUTS`{.interpreted-text role="setting"},
    and `CELERYD_REDIRECT_STDOUTS_LEVEL`{.interpreted-text
    role="setting"} settings.

    > `CELERY_REDIRECT_STDOUTS`{.interpreted-text role="setting"} is
    > used by the worker and beat. All output to [stdout]{.title-ref}
    > and [stderr]{.title-ref} will be redirected to the current logger
    > if enabled.
    >
    > `CELERY_REDIRECT_STDOUTS_LEVEL`{.interpreted-text role="setting"}
    > decides the log level used and is `WARNING`{.interpreted-text
    > role="const"} by default.

-   Added `CELERYBEAT_SCHEDULER`{.interpreted-text role="setting"}
    setting.

    > This setting is used to define the default for the -S option to
    > `celerybeat`{.interpreted-text role="program"}.
    >
    > Example:
    >
    > ``` python
    > CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
    > ```

-   Added Task.expires: Used to set default expiry time for tasks.

-   New remote control commands: [add_consumer]{.title-ref} and
    [cancel_consumer]{.title-ref}.

    > ::: {.method module=""}
    > add_consumer(queue, exchange, exchange_type, routing_key,
    > \*\*options)
    >
    > Tells the worker to declare and consume from the specified
    > declaration.
    > :::
    >
    > ::: {.method module=""}
    > cancel_consumer(queue_name)
    >
    > Tells the worker to stop consuming from queue (by queue name).
    > :::
    >
    > Commands also added to `celeryctl`{.interpreted-text
    > role="program"} and
    > `~celery.task.control.inspect`{.interpreted-text role="class"}.
    >
    > Example using `celeryctl` to start consuming from queue \"queue\",
    > in exchange \"exchange\", of type \"direct\" using binding key
    > \"key\":
    >
    > ``` console
    > $ celeryctl inspect add_consumer queue exchange direct key
    > $ celeryctl inspect cancel_consumer queue
    > ```
    >
    > See `monitoring-control`{.interpreted-text role="ref"} for more
    > information about the `celeryctl`{.interpreted-text
    > role="program"} program.
    >
    > Another example using
    > `~celery.task.control.inspect`{.interpreted-text role="class"}:
    >
    > ``` pycon
    > >>> from celery.task.control import inspect
    > >>> inspect.add_consumer(queue='queue', exchange='exchange',
    > ...                      exchange_type='direct',
    > ...                      routing_key='key',
    > ...                      durable=False,
    > ...                      auto_delete=True)
    >
    > >>> inspect.cancel_consumer('queue')
    > ```

-   `celerybeat`: Now logs the traceback if a message can\'t be sent.

-   `celerybeat`: Now enables a default socket timeout of 30 seconds.

-   `README`/introduction/homepage: Added link to
    [Flask-Celery](https://github.com/ask/flask-celery).

## 2.1.0 {#version-2.1.0}

release-date

:   2010-10-08 12:00 p.m. CEST

release-by

:   Ask Solem

### Important Notes {#v210-important}

-   Celery is now following the versioning semantics defined by
    [semver](http://semver.org).

    > This means we\'re no longer allowed to use odd/even versioning
    > semantics By our previous versioning scheme this stable release
    > should\'ve been version 2.2.

-   Now depends on Carrot 0.10.7.

-   No longer depends on SQLAlchemy, this needs to be installed
    separately if the database result backend is used.

-   `django-celery`{.interpreted-text role="pypi"} now comes with a
    monitor for the Django Admin interface. This can also be used if
    you\'re not a Django user. (Update: Django-Admin monitor has been
    replaced with Flower, see the Monitoring guide).

-   If you get an error after upgrading saying: [AttributeError:
    \'module\' object has no attribute \'system\']{.title-ref},

    > Then this is because the [celery.platform]{.title-ref} module has
    > been renamed to [celery.platforms]{.title-ref} to not collide with
    > the built-in `platform`{.interpreted-text role="mod"} module.
    >
    > You have to remove the old `platform.py`{.interpreted-text
    > role="file"} (and maybe `platform.pyc`{.interpreted-text
    > role="file"}) file from your previous Celery installation.
    >
    > To do this use `python`{.interpreted-text role="program"} to find
    > the location of this module:
    >
    > ``` console
    > $ python
    > >>> import celery.platform
    > >>> celery.platform
    > <module 'celery.platform' from '/opt/devel/celery/celery/platform.pyc'>
    > ```
    >
    > Here the compiled module is in
    > `/opt/devel/celery/celery/`{.interpreted-text role="file"}, to
    > remove the offending files do:
    >
    > ``` console
    > $ rm -f /opt/devel/celery/celery/platform.py*
    > ```

### News {#v210-news}

-   Added support for expiration of AMQP results (requires RabbitMQ
    2.1.0)

    > The new configuration option
    > `CELERY_AMQP_TASK_RESULT_EXPIRES`{.interpreted-text
    > role="setting"} sets the expiry time in seconds (can be int or
    > float):
    >
    > ``` python
    > CELERY_AMQP_TASK_RESULT_EXPIRES = 30 * 60  # 30 minutes.
    > CELERY_AMQP_TASK_RESULT_EXPIRES = 0.80     # 800 ms.
    > ```

-   `celeryev`: Event Snapshots

    > If enabled, the worker sends messages about what the worker is
    > doing. These messages are called \"events\". The events are used
    > by real-time monitors to show what the cluster is doing, but
    > they\'re not very useful for monitoring over a longer period of
    > time. Snapshots lets you take \"pictures\" of the clusters state
    > at regular intervals. This can then be stored in a database to
    > generate statistics with, or even monitoring over longer time
    > periods.
    >
    > `django-celery`{.interpreted-text role="pypi"} now comes with a
    > Celery monitor for the Django Admin interface. To use this you
    > need to run the `django-celery`{.interpreted-text role="pypi"}
    > snapshot camera, which stores snapshots to the database at
    > configurable intervals.
    >
    > To use the Django admin monitor you need to do the following:
    >
    > 1.  Create the new database tables:
    >
    >     > ``` console
    >     > $ python manage.py syncdb
    >     > ```
    >
    > 2.  Start the `django-celery`{.interpreted-text role="pypi"}
    >     snapshot camera:
    >
    >     > ``` console
    >     > $ python manage.py celerycam
    >     > ```
    >
    > 3.  Open up the django admin to monitor your cluster.
    >
    > The admin interface shows tasks, worker nodes, and even lets you
    > perform some actions, like revoking and rate limiting tasks, and
    > shutting down worker nodes.
    >
    > There\'s also a Debian init.d script for
    > `~celery.bin.events`{.interpreted-text role="mod"} available, see
    > `daemonizing`{.interpreted-text role="ref"} for more information.
    >
    > New command-line arguments to `celeryev`:
    >
    > > -   `celery events --camera`{.interpreted-text role="option"}:
    > >     Snapshot camera class to use.
    > > -   `celery events --logfile`{.interpreted-text role="option"}:
    > >     Log file
    > > -   `celery events --loglevel`{.interpreted-text role="option"}:
    > >     Log level
    > > -   `celery events --maxrate`{.interpreted-text role="option"}:
    > >     Shutter rate limit.
    > > -   `celery events --freq`{.interpreted-text role="option"}:
    > >     Shutter frequency
    >
    > The `--camera <celery events --camera>`{.interpreted-text
    > role="option"} argument is the name of a class used to take
    > snapshots with. It must support the interface defined by
    > `celery.events.snapshot.Polaroid`{.interpreted-text role="class"}.
    >
    > Shutter frequency controls how often the camera thread wakes up,
    > while the rate limit controls how often it will actually take a
    > snapshot. The rate limit can be an integer (snapshots/s), or a
    > rate limit string which has the same syntax as the task rate limit
    > strings ([\"200/m\"]{.title-ref}, [\"10/s\"]{.title-ref},
    > [\"1/h\",]{.title-ref} etc).
    >
    > For the Django camera case, this rate limit can be used to control
    > how often the snapshots are written to the database, and the
    > frequency used to control how often the thread wakes up to check
    > if there\'s anything new.
    >
    > The rate limit is off by default, which means it will take a
    > snapshot for every
    > `--frequency <celery events --frequency>`{.interpreted-text
    > role="option"} seconds.

-   `~celery.task.control.broadcast`{.interpreted-text role="func"}:
    Added callback argument, this can be used to process replies
    immediately as they arrive.

-   `celeryctl`: New command line utility to manage and inspect worker
    nodes, apply tasks and inspect the results of tasks.

    > ::: seealso
    > The `monitoring-control`{.interpreted-text role="ref"} section in
    > the `guide`{.interpreted-text role="ref"}.
    > :::
    >
    > Some examples:
    >
    > ``` console
    > $ celeryctl apply tasks.add -a '[2, 2]' --countdown=10
    >
    > $ celeryctl inspect active
    > $ celeryctl inspect registered_tasks
    > $ celeryctl inspect scheduled
    > $ celeryctl inspect --help
    > $ celeryctl apply --help
    > ```

-   Added the ability to set an expiry date and time for tasks.

    > Example:
    >
    >     >>> # Task expires after one minute from now.
    >     >>> task.apply_async(args, kwargs, expires=60)
    >     >>> # Also supports datetime
    >     >>> task.apply_async(args, kwargs,
    >     ...                  expires=datetime.now() + timedelta(days=1)
    >
    > When a worker receives a task that\'s been expired it will be
    > marked as revoked (`~@TaskRevokedError`{.interpreted-text
    > role="exc"}).

-   Changed the way logging is configured.

    > We now configure the root logger instead of only configuring our
    > custom logger. In addition we don\'t hijack the multiprocessing
    > logger anymore, but instead use a custom logger name for different
    > applications:
    >
    >   **Application**   **Logger Name**
    >   ----------------- -----------------
    >   `celeryd`         `"celery"`
    >   `celerybeat`      `"celery.beat"`
    >   `celeryev`        `"celery.ev"`
    >
    > This means that the [loglevel]{.title-ref} and
    > [logfile]{.title-ref} arguments will affect all registered loggers
    > (even those from third-party libraries). Unless you configure the
    > loggers manually as shown below, that is.
    >
    > *Users can choose to configure logging by subscribing to the
    > :signal:\`\~celery.signals.setup_logging\` signal:*
    >
    > ``` python
    > from logging.config import fileConfig
    > from celery import signals
    >
    > @signals.setup_logging.connect
    > def setup_logging(**kwargs):
    >     fileConfig('logging.conf')
    > ```
    >
    > If there are no receivers for this signal, the logging subsystem
    > will be configured using the
    > `--loglevel <celery worker --loglevel>`{.interpreted-text
    > role="option"}/
    > `--logfile <celery worker --logfile>`{.interpreted-text
    > role="option"} arguments, this will be used for *all defined
    > loggers*.
    >
    > Remember that the worker also redirects stdout and stderr to the
    > Celery logger, if manually configure logging you also need to
    > redirect the standard outs manually:
    >
    > ``` python
    > from logging.config import fileConfig
    > from celery import log
    >
    > def setup_logging(**kwargs):
    >     import logging
    >     fileConfig('logging.conf')
    >     stdouts = logging.getLogger('mystdoutslogger')
    >     log.redirect_stdouts_to_logger(stdouts, loglevel=logging.WARNING)
    > ```

-   worker Added command line option
    `--include <celery worker --include>`{.interpreted-text
    role="option"}:

    > A comma separated list of (task) modules to be imported.
    >
    > Example:
    >
    > ``` console
    > $ celeryd -I app1.tasks,app2.tasks
    > ```

-   worker: now emits a warning if running as the root user (euid is 0).

-   `celery.messaging.establish_connection`{.interpreted-text
    role="func"}: Ability to override defaults used using keyword
    argument \"defaults\".

-   worker: Now uses [multiprocessing.freeze_support()]{.title-ref} so
    that it should work with **py2exe**, **PyInstaller**, **cx_Freeze**,
    etc.

-   worker: Now includes more meta-data for the
    `STARTED`{.interpreted-text role="state"} state: PID and host name
    of the worker that started the task.

    > See issue #181

-   subtask: Merge additional keyword arguments to
    [subtask()]{.title-ref} into task keyword arguments.

    > For example:
    >
    > ``` pycon
    > >>> s = subtask((1, 2), {'foo': 'bar'}, baz=1)
    > >>> s.args
    > (1, 2)
    > >>> s.kwargs
    > {'foo': 'bar', 'baz': 1}
    > ```
    >
    > See issue #182.

-   worker: Now emits a warning if there\'s already a worker node using
    the same name running on the same virtual host.

-   AMQP result backend: Sending of results are now retried if the
    connection is down.

-   AMQP result backend: \`result.get()[: Wait for next state if state
    isn\'t in :data:]{.title-ref}\~celery.states.READY_STATES\`.

-   TaskSetResult now supports subscription.

    >     >>> res = TaskSet(tasks).apply_async()
    >     >>> res[0].get()

-   Added [Task.send_error_emails]{.title-ref} +
    [Task.error_whitelist]{.title-ref}, so these can be configured per
    task instead of just by the global setting.

-   Added [Task.store_errors_even_if_ignored]{.title-ref}, so it can be
    changed per Task, not just by the global setting.

-   The Crontab scheduler no longer wakes up every second, but
    implements [remaining_estimate]{.title-ref} (*Optimization*).

-   

    worker: Store `FAILURE`{.interpreted-text role="state"} result if the

    :   `~@WorkerLostError`{.interpreted-text role="exc"} exception
        occurs (worker process disappeared).

-   worker: Store `FAILURE`{.interpreted-text role="state"} result if
    one of the [\*TimeLimitExceeded]{.title-ref} exceptions occurs.

-   Refactored the periodic task responsible for cleaning up results.

    > -   
    >
    >     The backend cleanup task is now only added to the schedule if
    >
    >     :   `CELERY_TASK_RESULT_EXPIRES`{.interpreted-text
    >         role="setting"} is set.
    >
    > -   If the schedule already contains a periodic task named
    >     \"celery.backend_cleanup\" it won\'t change it, so the
    >     behavior of the backend cleanup task can be easily changed.
    >
    > -   The task is now run every day at 4:00 AM, rather than every
    >     day since the first time it was run (using Crontab schedule
    >     instead of [run_every]{.title-ref})
    >
    > -   
    >
    >     Renamed [celery.task.builtins.DeleteExpiredTaskMetaTask]{.title-ref}
    >
    >     :   -\>
    >         `celery.task.builtins.backend_cleanup`{.interpreted-text
    >         role="class"}
    >
    > -   The task itself has been renamed from
    >     \"celery.delete_expired_task_meta\" to
    >     \"celery.backend_cleanup\"
    >
    > See issue #134.

-   Implemented [AsyncResult.forget]{.title-ref} for
    SQLAlchemy/Memcached/Redis/Tokyo Tyrant backends (forget and remove
    task result).

    > See issue #184.

-   `TaskSetResult.join <celery.result.TaskSetResult.join>`{.interpreted-text
    role="meth"}: Added \'propagate=True\' argument.

    When set to `False`{.interpreted-text role="const"} exceptions
    occurring in subtasks will not be re-raised.

-   Added [Task.update_state(task_id, state, meta)]{.title-ref} as a
    shortcut to [task.backend.store_result(task_id, meta,
    state)]{.title-ref}.

    > The backend interface is \"private\" and the terminology outdated,
    > so better to move this to
    > `~celery.task.base.Task`{.interpreted-text role="class"} so it can
    > be used.

-   timer2: Set [self.running=False]{.title-ref} in
    `~celery.utils.timer2.Timer.stop`{.interpreted-text role="meth"} so
    it won\'t try to join again on subsequent calls to
    [stop()]{.title-ref}.

-   Log colors are now disabled by default on Windows.

-   [celery.platform]{.title-ref} renamed to
    `celery.platforms`{.interpreted-text role="mod"}, so it doesn\'t
    collide with the built-in `platform`{.interpreted-text role="mod"}
    module.

-   Exceptions occurring in Mediator+Pool callbacks are now caught and
    logged instead of taking down the worker.

-   Redis result backend: Now supports result expiration using the Redis
    [EXPIRE]{.title-ref} command.

-   unit tests: Don\'t leave threads running at tear down.

-   worker: Task results shown in logs are now truncated to 46 chars.

-   

    [Task.\_\_name\_\_]{.title-ref} is now an alias to [self.\_\_class\_\_.\_\_name\_\_]{.title-ref}.

    :   This way tasks introspects more like regular functions.

-   \`Task.retry\`: Now raises `TypeError`{.interpreted-text role="exc"}
    if kwargs argument is empty.

    > See issue #164.

-   `timedelta_seconds`: Use `timedelta.total_seconds` if running on
    Python 2.7

-   `~kombu.utils.limits.TokenBucket`{.interpreted-text role="class"}:
    Generic Token Bucket algorithm

-   `celery.events.state`{.interpreted-text role="mod"}: Recording of
    cluster state can now be paused and resumed, including support for
    buffering.

    > ::: method
    > State.freeze(buffer=True)
    >
    > Pauses recording of the stream.
    >
    > If [buffer]{.title-ref} is true, events received while being
    > frozen will be buffered, and may be replayed later.
    > :::
    >
    > ::: method
    > State.thaw(replay=True)
    >
    > Resumes recording of the stream.
    >
    > If [replay]{.title-ref} is true, then the recorded buffer will be
    > applied.
    > :::
    >
    > ::: method
    > State.freeze_while(fun)
    >
    > With a function to apply, freezes the stream before, and replays
    > the buffer after the function returns.
    > :::

-   `EventReceiver.capture <celery.events.EventReceiver.capture>`{.interpreted-text
    role="meth"} Now supports a timeout keyword argument.

-   worker: The mediator thread is now disabled if
    `CELERY_RATE_LIMITS`{.interpreted-text role="setting"} is enabled,
    and tasks are directly sent to the pool without going through the
    ready queue (*Optimization*).

### Fixes {#v210-fixes}

-   Pool: Process timed out by [TimeoutHandler]{.title-ref} must be
    joined by the Supervisor, so don\'t remove it from the internal
    process list.

    > See issue #192.

-   [TaskPublisher.delay_task]{.title-ref} now supports exchange
    argument, so exchange can be overridden when sending tasks in bulk
    using the same publisher

    > See issue #187.

-   the worker no longer marks tasks as revoked if
    `CELERY_IGNORE_RESULT`{.interpreted-text role="setting"} is enabled.

    > See issue #207.

-   AMQP Result backend: Fixed bug with [result.get()]{.title-ref} if
    `CELERY_TRACK_STARTED`{.interpreted-text role="setting"} enabled.

    > [result.get()]{.title-ref} would stop consuming after receiving
    > the `STARTED`{.interpreted-text role="state"} state.

-   Fixed bug where new processes created by the pool supervisor becomes
    stuck while reading from the task Queue.

    > See <http://bugs.python.org/issue10037>

-   Fixed timing issue when declaring the remote control command reply
    queue

    > This issue could result in replies being lost, but have now been
    > fixed.

-   Backward compatible [LoggerAdapter]{.title-ref} implementation: Now
    works for Python 2.4.

    > Also added support for several new methods: [fatal]{.title-ref},
    > [makeRecord]{.title-ref}, [\_log]{.title-ref}, [log]{.title-ref},
    > [isEnabledFor]{.title-ref}, [addHandler]{.title-ref},
    > [removeHandler]{.title-ref}.

### Experimental {#v210-experimental}

-   multi: Added daemonization support.

    > multi can now be used to start, stop and restart worker nodes:
    >
    > ``` console
    > $ celeryd-multi start jerry elaine george kramer
    > ```
    >
    > This also creates PID files and log files
    > (`celeryd@jerry.pid`{.interpreted-text role="file"}, \...,
    > `celeryd@jerry.log`{.interpreted-text role="file"}. To specify a
    > location for these files use the [\--pidfile]{.title-ref} and
    > [\--logfile]{.title-ref} arguments with the [%n]{.title-ref}
    > format:
    >
    > ``` console
    > $ celeryd-multi start jerry elaine george kramer \
    >                 --logfile=/var/log/celeryd@%n.log \
    >                 --pidfile=/var/run/celeryd@%n.pid
    > ```
    >
    > Stopping:
    >
    > ``` console
    > $ celeryd-multi stop jerry elaine george kramer
    > ```
    >
    > Restarting. The nodes will be restarted one by one as the old ones
    > are shutdown:
    >
    > ``` console
    > $ celeryd-multi restart jerry elaine george kramer
    > ```
    >
    > Killing the nodes (**WARNING**: Will discard currently executing
    > tasks):
    >
    > ``` console
    > $ celeryd-multi kill jerry elaine george kramer
    > ```
    >
    > See [celeryd-multi help]{.title-ref} for help.

-   multi: [start]{.title-ref} command renamed to [show]{.title-ref}.

    > [celeryd-multi start]{.title-ref} will now actually start and
    > detach worker nodes. To just generate the commands you have to use
    > [celeryd-multi show]{.title-ref}.

-   worker: Added [\--pidfile]{.title-ref} argument.

    > The worker will write its pid when it starts. The worker will not
    > be started if this file exists and the pid contained is still
    > alive.

-   Added generic init.d script using [celeryd-multi]{.title-ref}

    > <https://github.com/celery/celery/tree/master/extra/generic-init.d/celeryd>

### Documentation {#v210-documentation}

-   Added User guide section: Monitoring

-   Added user guide section: Periodic Tasks

    > Moved from [getting-started/periodic-tasks]{.title-ref} and
    > updated.

-   tutorials/external moved to new section: \"community\".

-   References has been added to all sections in the documentation.

    > This makes it easier to link between documents.
