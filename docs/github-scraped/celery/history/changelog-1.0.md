# Change history for Celery 1.0 {#changelog-1.0}

::: {.contents local=""}
:::

## 1.0.6 {#version-1.0.6}

release-date

:   2010-06-30 09:57 a.m. CEST

release-by

:   Ask Solem

-   RabbitMQ 1.8.0 has extended their exchange equivalence tests to
    include [auto_delete]{.title-ref} and [durable]{.title-ref}. This
    broke the AMQP backend.

    If you\'ve already used the AMQP backend this means you have to
    delete the previous definitions:

    ``` console
    $ camqadm exchange.delete celeryresults
    ```

    or:

    ``` console
    $ python manage.py camqadm exchange.delete celeryresults
    ```

## 1.0.5 {#version-1.0.5}

release-date

:   2010-06-01 02:36 p.m. CEST

release-by

:   Ask Solem

### Critical {#v105-critical}

-   `INT`{.interpreted-text role="sig"}/`Control-c`{.interpreted-text
    role="kbd"} killed the pool, abruptly terminating the currently
    executing tasks.

    > Fixed by making the pool worker processes ignore
    > `SIGINT`{.interpreted-text role="const"}.

-   Shouldn\'t close the consumers before the pool is terminated, just
    cancel the consumers.

    > See issue #122.

-   Now depends on `billiard`{.interpreted-text role="pypi"} \>= 0.3.1

-   worker: Previously exceptions raised by worker components could
    stall start-up, now it correctly logs the exceptions and shuts down.

-   worker: Prefetch counts was set too late. QoS is now set as early as
    possible, so the worker: can\'t slurp in all the messages at
    start-up.

### Changes {#v105-changes}

-   `celery.contrib.abortable`{.interpreted-text role="mod"}: Abortable
    tasks.

    > Tasks that defines steps of execution, the task can then be
    > aborted after each step has completed.

-   `~celery.events.EventDispatcher`{.interpreted-text role="class"}: No
    longer creates AMQP channel if events are disabled

-   Added required RPM package names under [\[bdist_rpm\]]{.title-ref}
    section, to support building RPMs from the sources using
    `setup.py`{.interpreted-text role="file"}.

-   Running unit tests: `NOSE_VERBOSE`{.interpreted-text role="envvar"}
    environment var now enables verbose output from Nose.

-   `celery.execute.apply`{.interpreted-text role="func"}: Pass log
    file/log level arguments as task kwargs.

    > See issue #110.

-   celery.execute.apply: Should return exception, not
    `~billiard.einfo.ExceptionInfo`{.interpreted-text role="class"} on
    error.

    > See issue #111.

-   Added new entries to the `FAQs <faq>`{.interpreted-text role="ref"}:

    > -   Should I use retry or acks_late?
    > -   Can I call a task by name?

## 1.0.4 {#version-1.0.4}

release-date

:   2010-05-31 09:54 a.m. CEST

release-by

:   Ask Solem

-   Changelog merged with 1.0.5 as the release was never announced.

## 1.0.3 {#version-1.0.3}

release-date

:   2010-05-15 03:00 p.m. CEST

release-by

:   Ask Solem

### Important notes {#v103-important}

-   Messages are now acknowledged *just before* the task function is
    executed.

    > This is the behavior we\'ve wanted all along, but couldn\'t have
    > because of limitations in the multiprocessing module. The previous
    > behavior wasn\'t good, and the situation worsened with the release
    > of 1.0.1, so this change will definitely improve reliability,
    > performance and operations in general.
    >
    > For more information please see <http://bit.ly/9hom6T>

-   Database result backend: result now explicitly sets
    [null=True]{.title-ref} as [django-picklefield]{.title-ref} version
    0.1.5 changed the default behavior right under our noses :(

    > See: <http://bit.ly/d5OwMr>
    >
    > This means those who created their Celery tables (via `syncdb` or
    > `celeryinit`) with `django-picklefield`{.interpreted-text
    > role="pypi"}[ versions \>= 0.1.5 has to alter their tables to
    > allow the result field to be \`NULL]{.title-ref} manually.
    >
    > MySQL:
    >
    > ``` sql
    > ALTER TABLE celery_taskmeta MODIFY result TEXT NULL
    > ```
    >
    > PostgreSQL:
    >
    > ``` sql
    > ALTER TABLE celery_taskmeta ALTER COLUMN result DROP NOT NULL
    > ```

-   Removed [Task.rate_limit_queue_type]{.title-ref}, as it wasn\'t
    really useful and made it harder to refactor some parts.

-   Now depends on carrot \>= 0.10.4

-   Now depends on billiard \>= 0.3.0

### News {#v103-news}

-   AMQP backend: Added timeout support for [result.get()]{.title-ref} /
    [result.wait()]{.title-ref}.

-   New task option: [Task.acks_late]{.title-ref} (default:
    `CELERY_ACKS_LATE`{.interpreted-text role="setting"})

    > Late ack means the task messages will be acknowledged **after**
    > the task has been executed, not *right before*, which is the
    > default behavior.
    >
    > ::: note
    > ::: title
    > Note
    > :::
    >
    > This means the tasks may be executed twice if the worker crashes
    > in mid-execution. Not acceptable for most applications, but
    > desirable for others.
    > :::

-   Added Crontab-like scheduling to periodic tasks.

    > Like a cronjob, you can specify units of time of when you\'d like
    > the task to execute. While not a full implementation of
    > `cron`{.interpreted-text role="command"}\'s features, it should
    > provide a fair degree of common scheduling needs.
    >
    > You can specify a minute (0-59), an hour (0-23), and/or a day of
    > the week (0-6 where 0 is Sunday, or by names:
    > `sun, mon, tue, wed, thu, fri, sat`).
    >
    > Examples:
    >
    > ``` python
    > from celery.schedules import crontab
    > from celery.decorators import periodic_task
    >
    > @periodic_task(run_every=crontab(hour=7, minute=30))
    > def every_morning():
    >     print('Runs every morning at 7:30a.m')
    >
    > @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week='mon'))
    > def every_monday_morning():
    >     print('Run every monday morning at 7:30a.m')
    >
    > @periodic_task(run_every=crontab(minutes=30))
    > def every_hour():
    >     print('Runs every hour on the clock (e.g., 1:30, 2:30, 3:30 etc.).')
    > ```
    >
    > ::: note
    > ::: title
    > Note
    > :::
    >
    > This a late addition. While we have unit tests, due to the nature
    > of this feature we haven\'t been able to completely test this in
    > practice, so consider this experimental.
    > :::

-   \`TaskPool.apply_async\`: Now supports the
    [accept_callback]{.title-ref} argument.

-   \`apply_async\`: Now raises `ValueError`{.interpreted-text
    role="exc"} if task args isn\'t a list, or kwargs isn\'t a tuple
    (Issue #95).

-   [Task.max_retries]{.title-ref} can now be [None]{.title-ref}, which
    means it will retry forever.

-   `celerybeat`: Now reuses the same connection when publishing large
    sets of tasks.

-   Modified the task locking example in the documentation to use
    [cache.add]{.title-ref} for atomic locking.

-   Added experimental support for a *started* status on tasks.

    > If [Task.track_started]{.title-ref} is enabled the task will
    > report its status as \"started\" when the task is executed by a
    > worker.
    >
    > The default value is [False]{.title-ref} as the normal behavior is
    > to not report that level of granularity. Tasks are either pending,
    > finished, or waiting to be retried. Having a \"started\" status
    > can be useful for when there are long running tasks and there\'s a
    > need to report which task is currently running.
    >
    > The global default can be overridden by the
    > `CELERY_TRACK_STARTED`{.interpreted-text role="setting"} setting.

-   User Guide: New section [Tips and Best Practices]{.title-ref}.

    > Contributions welcome!

### Remote control commands {#v103-remote-control}

-   Remote control commands can now send replies back to the caller.

    > Existing commands has been improved to send replies, and the
    > client interface in [celery.task.control]{.title-ref} has new
    > keyword arguments: [reply]{.title-ref}, [timeout]{.title-ref} and
    > [limit]{.title-ref}. Where reply means it will wait for replies,
    > timeout is the time in seconds to stop waiting for replies, and
    > limit is the maximum number of replies to get.
    >
    > By default, it will wait for as many replies as possible for one
    > second.
    >
    > -   rate_limit(task_name, destination=all, reply=False, timeout=1,
    >     limit=0)
    >
    >     > Worker returns [{\'ok\': message}]{.title-ref} on success,
    >     > or [{\'failure\': message}]{.title-ref} on failure.
    >     >
    >     > > \>\>\> from celery.task.control import rate_limit \>\>\>
    >     > > rate_limit(\'tasks.add\', \'10/s\', reply=True)
    >     > > \[{\'worker1\': {\'ok\': \'new rate limit set
    >     > > successfully\'}}, {\'worker2\': {\'ok\': \'new rate limit
    >     > > set successfully\'}}\]
    >
    > -   ping(destination=all, reply=False, timeout=1, limit=0)
    >
    >     > Worker returns the simple message [\"pong\"]{.title-ref}.
    >     >
    >     > > \>\>\> from celery.task.control import ping \>\>\>
    >     > > ping(reply=True) \[{\'worker1\': \'pong\'}, {\'worker2\':
    >     > > \'pong\'},
    >
    > -   revoke(destination=all, reply=False, timeout=1, limit=0)
    >
    >     > Worker simply returns [True]{.title-ref}.
    >     >
    >     > > \>\>\> from celery.task.control import revoke \>\>\>
    >     > > revoke(\'419e46eb-cf6a-4271-86a8-442b7124132c\',
    >     > > reply=True) \[{\'worker1\': True}, {\'worker2\'; True}\]

-   You can now add your own remote control commands!

    > Remote control commands are functions registered in the command
    > registry. Registering a command is done using
    > `celery.worker.control.Panel.register`{.interpreted-text
    > role="meth"}:
    >
    > ``` python
    > from celery.task.control import Panel
    >
    > @Panel.register
    > def reset_broker_connection(state, **kwargs):
    >     state.consumer.reset_connection()
    >     return {'ok': 'connection re-established'}
    > ```
    >
    > With this module imported in the worker, you can launch the
    > command using \`celery.task.control.broadcast\`:
    >
    >     >>> from celery.task.control import broadcast
    >     >>> broadcast('reset_broker_connection', reply=True)
    >     [{'worker1': {'ok': 'connection re-established'},
    >      {'worker2': {'ok': 'connection re-established'}}]
    >
    > **TIP** You can choose the worker(s) to receive the command by
    > using the [destination]{.title-ref} argument:
    >
    >     >>> broadcast('reset_broker_connection', destination=['worker1'])
    >     [{'worker1': {'ok': 'connection re-established'}]

-   New remote control command: [dump_reserved]{.title-ref}

    > Dumps tasks reserved by the worker, waiting to be executed:
    >
    >     >>> from celery.task.control import broadcast
    >     >>> broadcast('dump_reserved', reply=True)
    >     [{'myworker1': [<TaskRequest ....>]}]

-   New remote control command: [dump_schedule]{.title-ref}

    > Dumps the workers currently registered ETA schedule. These are
    > tasks with an [eta]{.title-ref} (or [countdown]{.title-ref})
    > argument waiting to be executed by the worker.
    >
    > > \>\>\> from celery.task.control import broadcast \>\>\>
    > > broadcast(\'dump_schedule\', reply=True) \[{\'w1\': \[\]},
    > > {\'w3\': \[\]}, {\'w2\': \[\'0. 2010-05-12 11:06:00 pri0
    > > \<TaskRequest {name:\'opalfeeds.tasks.refresh_feed_slice\',
    > > id:\'95b45760-4e73-4ce8-8eac-f100aa80273a\', args:\'(\<Feeds
    > > freq_max:3600 freq_min:60 start:2184.0 stop:3276.0\>,)\',
    > > kwargs:\'{\'page\': 2}\'}\>\'\]}, {\'w4\': \[\'0. 2010-05-12
    > > 11:00:00 pri0 \<TaskRequest
    > > {name:\'opalfeeds.tasks.refresh_feed_slice\',
    > > id:\'c053480b-58fb-422f-ae68-8d30a464edfe\', args:\'(\<Feeds
    > > freq_max:3600 freq_min:60 start:1092.0 stop:2184.0\>,)\',
    > > kwargs:\'{\'page\': 1}\'}\>\', \'1. 2010-05-12 11:12:00 pri0
    > > \<TaskRequest {name:\'opalfeeds.tasks.refresh_feed_slice\',
    > > id:\'ab8bc59e-6cf8-44b8-88d0-f1af57789758\', args:\'(\<Feeds
    > > freq_max:3600 freq_min:60 start:3276.0 stop:4365\>,)\',
    > > kwargs:\'{\'page\': 3}\'}\>\'\]}\]

### Fixes {#v103-fixes}

-   Mediator thread no longer blocks for more than 1 second.

    > With rate limits enabled and when there was a lot of remaining
    > time, the mediator thread could block shutdown (and potentially
    > block other jobs from coming in).

-   Remote rate limits wasn\'t properly applied (Issue #98).

-   Now handles exceptions with Unicode messages correctly in
    [TaskRequest.on_failure]{.title-ref}.

-   Database backend: \`TaskMeta.result\`: default value should be
    [None]{.title-ref} not empty string.

## 1.0.2 {#version-1.0.2}

release-date

:   2010-03-31 12:50 p.m. CET

release-by

:   Ask Solem

-   Deprecated: `CELERY_BACKEND`{.interpreted-text role="setting"},
    please use `CELERY_RESULT_BACKEND`{.interpreted-text role="setting"}
    instead.

-   We now use a custom logger in tasks. This logger supports task magic
    keyword arguments in formats.

    > The default format for tasks
    > (`CELERYD_TASK_LOG_FORMAT`{.interpreted-text role="setting"}) now
    > includes the id and the name of tasks so the origin of task log
    > messages can easily be traced.
    >
    > Example output::
    >
    > :   
    >
    >     \[2010-03-25 13:11:20,317: INFO/PoolWorker-1\]
    >
    >     :   \[tasks.add(a6e1c5ad-60d9-42a0-8b24-9e39363125a4)\] Hello
    >         from add
    >
    > To revert to the previous behavior you can set:
    >
    >     CELERYD_TASK_LOG_FORMAT = """
    >         [%(asctime)s: %(levelname)s/%(processName)s] %(message)s
    >     """.strip()

-   Unit tests: Don\'t disable the django test database tear down,
    instead fixed the underlying issue which was caused by modifications
    to the [DATABASE_NAME]{.title-ref} setting (Issue #82).

-   Django Loader: New config `CELERY_DB_REUSE_MAX`{.interpreted-text
    role="setting"} (max number of tasks to reuse the same database
    connection)

    > The default is to use a new connection for every task. We\'d very
    > much like to reuse the connection, but a safe number of reuses
    > isn\'t known, and we don\'t have any way to handle the errors that
    > might happen, which may even be database dependent.
    >
    > See: <http://bit.ly/94fwdd>

-   worker: The worker components are now configurable:
    `CELERYD_POOL`{.interpreted-text role="setting"},
    `CELERYD_CONSUMER`{.interpreted-text role="setting"},
    `CELERYD_MEDIATOR`{.interpreted-text role="setting"}, and
    `CELERYD_ETA_SCHEDULER`{.interpreted-text role="setting"}.

    > The default configuration is as follows:
    >
    > ``` python
    > CELERYD_POOL = 'celery.concurrency.processes.TaskPool'
    > CELERYD_MEDIATOR = 'celery.worker.controllers.Mediator'
    > CELERYD_ETA_SCHEDULER = 'celery.worker.controllers.ScheduleController'
    > CELERYD_CONSUMER = 'celery.worker.consumer.Consumer'
    > ```
    >
    > The `CELERYD_POOL`{.interpreted-text role="setting"} setting makes
    > it easy to swap out the multiprocessing pool with a threaded pool,
    > or how about a twisted/eventlet pool?
    >
    > Consider the competition for the first pool plug-in started!

-   Debian init-scripts: Use [-a]{.title-ref} not [&&]{.title-ref}
    (Issue #82).

-   Debian init-scripts: Now always preserves
    [\$CELERYD_OPTS]{.title-ref} from the
    [/etc/default/celeryd]{.title-ref} and
    [/etc/default/celerybeat]{.title-ref}.

-   celery.beat.Scheduler: Fixed a bug where the schedule wasn\'t
    properly flushed to disk if the schedule hadn\'t been properly
    initialized.

-   `celerybeat`: Now syncs the schedule to disk when receiving the
    `SIGTERM`{.interpreted-text role="sig"} and
    `SIGINT`{.interpreted-text role="sig"} signals.

-   Control commands: Make sure keywords arguments aren\'t in Unicode.

-   ETA scheduler: Was missing a logger object, so the scheduler crashed
    when trying to log that a task had been revoked.

-   `management.commands.camqadm`: Fixed typo [camqpadm]{.title-ref} -\>
    [camqadm]{.title-ref} (Issue #83).

-   PeriodicTask.delta_resolution: wasn\'t working for days and hours,
    now fixed by rounding to the nearest day/hour.

-   Fixed a potential infinite loop in
    [BaseAsyncResult.\_\_eq\_\_]{.title-ref}, although there\'s no
    evidence that it has ever been triggered.

-   worker: Now handles messages with encoding problems by acking them
    and emitting an error message.

## 1.0.1 {#version-1.0.1}

release-date

:   2010-02-24 07:05 p.m. CET

release-by

:   Ask Solem

-   Tasks are now acknowledged early instead of late.

    > This is done because messages can only be acknowledged within the
    > same connection channel, so if the connection is lost we\'d\'ve to
    > re-fetch the message again to acknowledge it.
    >
    > This might or might not affect you, but mostly those running tasks
    > with a really long execution time are affected, as all tasks
    > that\'s made it all the way into the pool needs to be executed
    > before the worker can safely terminate (this is at most the number
    > of pool workers, multiplied by the
    > `CELERYD_PREFETCH_MULTIPLIER`{.interpreted-text role="setting"}
    > setting).
    >
    > We multiply the prefetch count by default to increase the
    > performance at times with bursts of tasks with a short execution
    > time. If this doesn\'t apply to your use case, you should be able
    > to set the prefetch multiplier to zero, without sacrificing
    > performance.
    >
    > ::: note
    > ::: title
    > Note
    > :::
    >
    > A patch to `multiprocessing`{.interpreted-text role="mod"} is
    > currently being worked on, this patch would enable us to use a
    > better solution, and is scheduled for inclusion in the
    > [2.0.0]{.title-ref} release.
    > :::

-   The worker now shutdowns cleanly when receiving the
    `SIGTERM`{.interpreted-text role="sig"} signal.

-   The worker now does a cold shutdown if the
    `SIGINT`{.interpreted-text role="sig"} signal is received
    (`Control-c`{.interpreted-text role="kbd"}), this means it tries to
    terminate as soon as possible.

-   Caching of results now moved to the base backend classes, so no need
    to implement this functionality in the base classes.

-   Caches are now also limited in size, so their memory usage doesn\'t
    grow out of control.

    > You can set the maximum number of results the cache can hold using
    > the `CELERY_MAX_CACHED_RESULTS`{.interpreted-text role="setting"}
    > setting (the default is five thousand results). In addition, you
    > can re-fetch already retrieved results using
    > [backend.reload_task_result]{.title-ref} +
    > [backend.reload_taskset_result]{.title-ref} (that\'s for those who
    > want to send results incrementally).

-   The worker now works on Windows again.

    > ::: warning
    > ::: title
    > Warning
    > :::
    >
    > If you\'re using Celery with Django, you can\'t use
    > [project.settings]{.title-ref} as the settings module name, but
    > the following should work:
    >
    > ``` console
    > $ python manage.py celeryd --settings=settings
    > ```
    > :::

-   Execution: [.messaging.TaskPublisher.send_task]{.title-ref} now
    incorporates all the functionality apply_async previously did.

    > Like converting countdowns to ETA, so
    > `celery.execute.apply_async`{.interpreted-text role="func"} is now
    > simply a convenient front-end to
    > `celery.messaging.TaskPublisher.send_task`{.interpreted-text
    > role="meth"}, using the task classes default options.
    >
    > Also `celery.execute.send_task`{.interpreted-text role="func"} has
    > been introduced, which can apply tasks using just the task name
    > (useful if the client doesn\'t have the destination task in its
    > task registry).
    >
    > Example:
    >
    > > \>\>\> from celery.execute import send_task \>\>\> result =
    > > send_task(\'celery.ping\', args=\[\], kwargs={}) \>\>\>
    > > result.get() \'pong\'

-   \`camqadm\`: This is a new utility for command-line access to the
    AMQP API.

    > Excellent for deleting queues/bindings/exchanges, experimentation
    > and testing:
    >
    > ``` console
    > $ camqadm
    > 1> help
    > ```
    >
    > Gives an interactive shell, type [help]{.title-ref} for a list of
    > commands.
    >
    > When using Django, use the management command instead:
    >
    > ``` console
    > $ python manage.py camqadm
    > 1> help
    > ```

-   Redis result backend: To conform to recent Redis API changes, the
    following settings has been deprecated:

    > -   [REDIS_TIMEOUT]{.title-ref}
    > -   [REDIS_CONNECT_RETRY]{.title-ref}
    >
    > These will emit a [DeprecationWarning]{.title-ref} if used.
    >
    > A [REDIS_PASSWORD]{.title-ref} setting has been added, so you can
    > use the new simple authentication mechanism in Redis.

-   The redis result backend no longer calls [SAVE]{.title-ref} when
    disconnecting, as this is apparently better handled by Redis itself.

-   If [settings.DEBUG]{.title-ref} is on, the worker now warns about
    the possible memory leak it can result in.

-   The ETA scheduler now sleeps at most two seconds between iterations.

-   The ETA scheduler now deletes any revoked tasks it might encounter.

    > As revokes aren\'t yet persistent, this is done to make sure the
    > task is revoked even though, for example, it\'s currently being
    > hold because its ETA is a week into the future.

-   The [task_id]{.title-ref} argument is now respected even if the task
    is executed eagerly (either using apply, or
    `CELERY_ALWAYS_EAGER`{.interpreted-text role="setting"}).

-   The internal queues are now cleared if the connection is reset.

-   New magic keyword argument: [delivery_info]{.title-ref}.

    > Used by retry() to resend the task to its original destination
    > using the same exchange/routing_key.

-   Events: Fields wasn\'t passed by [.send()]{.title-ref} (fixes the
    UUID key errors in celerymon)

-   Added [\--schedule]{.title-ref}/[-s]{.title-ref} option to the
    worker, so it is possible to specify a custom schedule filename when
    using an embedded `celerybeat` server (the
    [-B]{.title-ref}/[\--beat]{.title-ref}) option.

-   Better Python 2.4 compatibility. The test suite now passes.

-   task decorators: Now preserve docstring as
    [cls.\_\_doc\_\_]{.title-ref}, (was previously copied to
    [cls.run.\_\_doc\_\_]{.title-ref})

-   The [testproj]{.title-ref} directory has been renamed to
    [tests]{.title-ref} and we\'re now using [nose]{.title-ref} +
    [django-nose]{.title-ref} for test discovery, and
    [unittest2]{.title-ref} for test cases.

-   New pip requirements files available in
    `requirements`{.interpreted-text role="file"}.

-   TaskPublisher: Declarations are now done once (per process).

-   Added [Task.delivery_mode]{.title-ref} and the
    `CELERY_DEFAULT_DELIVERY_MODE`{.interpreted-text role="setting"}
    setting.

    > These can be used to mark messages non-persistent (i.e., so
    > they\'re lost if the broker is restarted).

-   Now have our own [ImproperlyConfigured]{.title-ref} exception,
    instead of using the Django one.

-   Improvements to the Debian init-scripts: Shows an error if the
    program is not executable. Does not modify [CELERYD]{.title-ref}
    when using django with virtualenv.

## 1.0.0 {#version-1.0.0}

release-date

:   2010-02-10 04:00 p.m. CET

release-by

:   Ask Solem

### Backward incompatible changes {#v100-incompatible}

-   Celery doesn\'t support detaching anymore, so you have to use the
    tools available on your platform, or something like
    `supervisor`{.interpreted-text role="pypi"} to make
    `celeryd`/`celerybeat`/`celerymon` into background processes.

    > We\'ve had too many problems with the worker daemonizing itself,
    > so it was decided it has to be removed. Example start-up scripts
    > has been added to the [extra/]{.title-ref} directory:
    >
    > -   Debian, Ubuntu, (`start-stop-daemon`{.interpreted-text
    >     role="command"})
    >
    >     > [extra/debian/init.d/celeryd]{.title-ref}
    >     > [extra/debian/init.d/celerybeat]{.title-ref}
    >
    > -   macOS `launchd`{.interpreted-text role="command"}
    >
    >     > [extra/mac/org.celeryq.celeryd.plist]{.title-ref}
    >     > [extra/mac/org.celeryq.celerybeat.plist]{.title-ref}
    >     > [extra/mac/org.celeryq.celerymon.plist]{.title-ref}
    >
    > -   Supervisor (<http://supervisord.org>)
    >
    >     > [extra/supervisord/supervisord.conf]{.title-ref}
    >
    > In addition to [\--detach]{.title-ref}, the following program
    > arguments has been removed: [\--uid]{.title-ref},
    > [\--gid]{.title-ref}, [\--workdir]{.title-ref},
    > [\--chroot]{.title-ref}, [\--pidfile]{.title-ref},
    > [\--umask]{.title-ref}. All good daemonization tools should
    > support equivalent functionality, so don\'t worry.
    >
    > Also the following configuration keys has been removed:
    > [CELERYD_PID_FILE]{.title-ref}, [CELERYBEAT_PID_FILE]{.title-ref},
    > [CELERYMON_PID_FILE]{.title-ref}.

-   Default worker loglevel is now [WARN]{.title-ref}, to enable the
    previous log level start the worker with
    [\--loglevel=INFO]{.title-ref}.

-   Tasks are automatically registered.

    > This means you no longer have to register your tasks manually. You
    > don\'t have to change your old code right away, as it doesn\'t
    > matter if a task is registered twice.
    >
    > If you don\'t want your task to be automatically registered you
    > can set the [abstract]{.title-ref} attribute
    >
    > ``` python
    > class MyTask(Task):
    >     abstract = True
    > ```
    >
    > By using [abstract]{.title-ref} only tasks subclassing this task
    > will be automatically registered (this works like the Django ORM).
    >
    > If you don\'t want subclasses to be registered either, you can set
    > the [autoregister]{.title-ref} attribute to [False]{.title-ref}.
    >
    > Incidentally, this change also fixes the problems with automatic
    > name assignment and relative imports. So you also don\'t have to
    > specify a task name anymore if you use relative imports.

-   You can no longer use regular functions as tasks.

    > This change was added because it makes the internals a lot more
    > clean and simple. However, you can now turn functions into tasks
    > by using the [\@task]{.title-ref} decorator:
    >
    > ``` python
    > from celery.decorators import task
    >
    > @task()
    > def add(x, y):
    >     return x + y
    > ```
    >
    > ::: seealso
    > `guide-tasks`{.interpreted-text role="ref"} for more information
    > about the task decorators.
    > :::

-   The periodic task system has been rewritten to a centralized
    solution.

    > This means the worker no longer schedules periodic tasks by
    > default, but a new daemon has been introduced:
    > [celerybeat]{.title-ref}.
    >
    > To launch the periodic task scheduler you have to run
    > `celerybeat`:
    >
    > ``` console
    > $ celerybeat
    > ```
    >
    > Make sure this is running on one server only, if you run it twice,
    > all periodic tasks will also be executed twice.
    >
    > If you only have one worker server you can embed it into the
    > worker like this:
    >
    > ``` console
    > $ celeryd --beat # Embed celerybeat in celeryd.
    > ```

-   The supervisor has been removed.

    > This means the [-S]{.title-ref} and [\--supervised]{.title-ref}
    > options to [celeryd]{.title-ref} is no longer supported. Please
    > use something like <http://supervisord.org> instead.

-   [TaskSet.join]{.title-ref} has been removed, use
    [TaskSetResult.join]{.title-ref} instead.

-   The task status [\"DONE\"]{.title-ref} has been renamed to
    [\"SUCCESS\"]{.title-ref}.

-   [AsyncResult.is_done]{.title-ref} has been removed, use
    [AsyncResult.successful]{.title-ref} instead.

-   The worker no longer stores errors if
    [Task.ignore_result]{.title-ref} is set, to revert to the previous
    behavior set `CELERY_STORE_ERRORS_EVEN_IF_IGNORED`{.interpreted-text
    role="setting"} to [True]{.title-ref}.

-   The statistics functionality has been removed in favor of events, so
    the [-S]{.title-ref} and \--statistics\` switches has been removed.

-   The module [celery.task.strategy]{.title-ref} has been removed.

-   [celery.discovery]{.title-ref} has been removed, and it\'s
    `autodiscover` function is now in
    [celery.loaders.djangoapp]{.title-ref}. Reason: Internal API.

-   The `CELERY_LOADER`{.interpreted-text role="envvar"} environment
    variable now needs loader class name in addition to module name,

    > For example, where you previously had:
    > [\"celery.loaders.default\"]{.title-ref}, you now need
    > [\"celery.loaders.default.Loader\"]{.title-ref}, using the
    > previous syntax will result in a [DeprecationWarning]{.title-ref}.

-   Detecting the loader is now lazy, and so isn\'t done when importing
    [celery.loaders]{.title-ref}.

    > To make this happen [celery.loaders.settings]{.title-ref} has been
    > renamed to [load_settings]{.title-ref} and is now a function
    > returning the settings object.
    > [celery.loaders.current_loader]{.title-ref} is now also a
    > function, returning the current loader.
    >
    > So:
    >
    >     loader = current_loader
    >
    > needs to be changed to:
    >
    >     loader = current_loader()

### Deprecations {#v100-deprecations}

-   The following configuration variables has been renamed and will be
    deprecated in v2.0:

    > -   `CELERYD_DAEMON_LOG_FORMAT` -\> `CELERYD_LOG_FORMAT`
    > -   `CELERYD_DAEMON_LOG_LEVEL` -\> `CELERYD_LOG_LEVEL`
    > -   `CELERY_AMQP_CONNECTION_TIMEOUT` -\>
    >     `CELERY_BROKER_CONNECTION_TIMEOUT`
    > -   `CELERY_AMQP_CONNECTION_RETRY` -\>
    >     `CELERY_BROKER_CONNECTION_RETRY`
    > -   `CELERY_AMQP_CONNECTION_MAX_RETRIES` -\>
    >     `CELERY_BROKER_CONNECTION_MAX_RETRIES`
    > -   `SEND_CELERY_TASK_ERROR_EMAILS` -\>
    >     `CELERY_SEND_TASK_ERROR_EMAILS`

-   The public API names in celery.conf has also changed to a consistent
    naming scheme.

-   We now support consuming from an arbitrary number of queues.

    > To do this we had to rename the configuration syntax. If you use
    > any of the custom AMQP routing options
    > (queue/exchange/routing_key, etc.), you should read the new FAQ
    > entry: `faq-task-routing`{.interpreted-text role="ref"}.
    >
    > The previous syntax is deprecated and scheduled for removal in
    > v2.0.

-   [TaskSet.run]{.title-ref} has been renamed to
    [TaskSet.apply_async]{.title-ref}.

    > [TaskSet.run]{.title-ref} has now been deprecated, and is
    > scheduled for removal in v2.0.

### News

-   Rate limiting support (per task type, or globally).

-   New periodic task system.

-   Automatic registration.

-   New cool task decorator syntax.

-   worker: now sends events if enabled with the [-E]{.title-ref}
    argument.

    > Excellent for monitoring tools, one is already in the making
    > (<https://github.com/celery/celerymon>).
    >
    > Current events include: `worker-heartbeat`{.interpreted-text
    > role="event"}, task-\[received/succeeded/failed/retried\],
    > `worker-online`{.interpreted-text role="event"},
    > `worker-offline`{.interpreted-text role="event"}.

-   You can now delete (revoke) tasks that\'s already been applied.

-   You can now set the hostname the worker identifies as using the
    [\--hostname]{.title-ref} argument.

-   Cache backend now respects the
    `CELERY_TASK_RESULT_EXPIRES`{.interpreted-text role="setting"}
    setting.

-   Message format has been standardized and now uses ISO-8601 format
    for dates instead of datetime.

-   worker now responds to the `SIGHUP`{.interpreted-text role="sig"}
    signal by restarting itself.

-   Periodic tasks are now scheduled on the clock.

    > That is, [timedelta(hours=1)]{.title-ref} means every hour at :00
    > minutes, not every hour from the server starts. To revert to the
    > previous behavior you can set [PeriodicTask.relative =
    > True]{.title-ref}.

-   Now supports passing execute options to a TaskSets list of args.

    > Example:
    >
    > ``` pycon
    > >>> ts = TaskSet(add, [([2, 2], {}, {'countdown': 1}),
    > ...                    ([4, 4], {}, {'countdown': 2}),
    > ...                    ([8, 8], {}, {'countdown': 3})])
    > >>> ts.run()
    > ```

-   Got a 3x performance gain by setting the prefetch count to four
    times the concurrency, (from an average task round-trip of 0.1s to
    0.03s!).

    > A new setting has been added:
    > `CELERYD_PREFETCH_MULTIPLIER`{.interpreted-text role="setting"},
    > which is set to [4]{.title-ref} by default.

-   Improved support for webhook tasks.

    > [celery.task.rest]{.title-ref} is now deprecated, replaced with
    > the new and shiny [celery.task.http]{.title-ref}. With more
    > reflective names, sensible interface, and it\'s possible to
    > override the methods used to perform HTTP requests.

-   The results of task sets are now cached by storing it in the result
    backend.

### Changes {#v100-changes}

-   Now depends on `carrot`{.interpreted-text role="pypi"} \>= 0.8.1

-   New dependencies: `billiard`{.interpreted-text role="pypi"},
    `python-dateutil`{.interpreted-text role="pypi"},
    `django-picklefield`{.interpreted-text role="pypi"}.

-   No longer depends on python-daemon

-   The [uuid]{.title-ref} distribution is added as a dependency when
    running Python 2.4.

-   Now remembers the previously detected loader by keeping it in the
    `CELERY_LOADER`{.interpreted-text role="envvar"} environment
    variable.

    > This may help on windows where fork emulation is used.

-   ETA no longer sends datetime objects, but uses ISO 8601 date format
    in a string for better compatibility with other platforms.

-   No longer sends error mails for retried tasks.

-   Task can now override the backend used to store results.

-   Refactored the ExecuteWrapper, [apply]{.title-ref} and
    `CELERY_ALWAYS_EAGER`{.interpreted-text role="setting"} now also
    executes the task callbacks and signals.

-   Now using a proper scheduler for the tasks with an ETA.

    > This means waiting ETA tasks are sorted by time, so we don\'t have
    > to poll the whole list all the time.

-   Now also imports modules listed in
    `CELERY_IMPORTS`{.interpreted-text role="setting"} when running with
    django (as documented).

-   Log level for stdout/stderr changed from INFO to ERROR

-   ImportErrors are now properly propagated when auto-discovering
    tasks.

-   You can now use [celery.messaging.establish_connection]{.title-ref}
    to establish a connection to the broker.

-   When running as a separate service the periodic task scheduler does
    some smart moves to not poll too regularly.

    > If you need faster poll times you can lower the value of
    > `CELERYBEAT_MAX_LOOP_INTERVAL`{.interpreted-text role="setting"}.

-   You can now change periodic task intervals at runtime, by making
    [run_every]{.title-ref} a property, or subclassing
    [PeriodicTask.is_due]{.title-ref}.

-   The worker now supports control commands enabled through the use of
    a broadcast queue, you can remotely revoke tasks or set the rate
    limit for a task type. See `celery.task.control`{.interpreted-text
    role="mod"}.

-   The services now sets informative process names (as shown in
    [ps]{.title-ref} listings) if the `setproctitle`{.interpreted-text
    role="pypi"} module is installed.

-   `~@NotRegistered`{.interpreted-text role="exc"} now inherits from
    `KeyError`{.interpreted-text role="exc"}, and
    [TaskRegistry.\_\_getitem\_\_]{.title-ref}+\`pop\` raises
    [NotRegistered]{.title-ref} instead

-   You can set the loader via the `CELERY_LOADER`{.interpreted-text
    role="envvar"} environment variable.

-   You can now set `CELERY_IGNORE_RESULT`{.interpreted-text
    role="setting"} to ignore task results by default (if enabled, tasks
    doesn\'t save results or errors to the backend used).

-   The worker now correctly handles malformed messages by throwing away
    and acknowledging the message, instead of crashing.

### Bugs {#v100-bugs}

-   Fixed a race condition that could happen while storing task results
    in the database.

### Documentation {#v100-documentation}

-   Reference now split into two sections; API reference and internal
    module reference.

## 0.8.4 {#version-0.8.4}

release-date

:   2010-02-05 01:52 p.m. CEST

release-by

:   Ask Solem

-   Now emits a warning if the \--detach argument is used. \--detach
    shouldn\'t be used anymore, as it has several not easily fixed bugs
    related to it. Instead, use something like start-stop-daemon,
    `supervisor`{.interpreted-text role="pypi"} or
    `launchd`{.interpreted-text role="command"} (macOS).
-   Make sure logger class is process aware, even if running Python \>=
    2.6.
-   Error emails are not sent anymore when the task is retried.

## 0.8.3 {#version-0.8.3}

release-date

:   2009-12-22 09:43 a.m. CEST

release-by

:   Ask Solem

-   Fixed a possible race condition that could happen when
    storing/querying task results using the database backend.
-   Now has console script entry points in the
    `setup.py`{.interpreted-text role="file"} file, so tools like
    `zc.buildout`{.interpreted-text role="pypi"} will correctly install
    the programs `celeryd` and `celeryinit`.

## 0.8.2 {#version-0.8.2}

release-date

:   2009-11-20 03:40 p.m. CEST

release-by

:   Ask Solem

-   QOS Prefetch count wasn\'t applied properly, as it was set for every
    message received (which apparently behaves like, \"receive one
    more\"), instead of only set when our wanted value changed.

## 0.8.1 {#version-0.8.1}

release-date

:   2009-11-16 05:21 p.m. CEST

release-by

:   Ask Solem

### Very important note {#v081-very-important}

This release (with carrot 0.8.0) enables AMQP QoS (quality of service),
which means the workers will only receive as many messages as it can
handle at a time. As with any release, you should test this version
upgrade on your development servers before rolling it out to production!

### Important changes {#v081-important}

-   If you\'re using Python \< 2.6 and you use the multiprocessing
    backport, then multiprocessing version 2.6.2.1 is required.

-   All [AMQP]()\* settings has been renamed to [BROKER]()\*, and in
    addition AMQP_SERVER has been renamed to BROKER_HOST, so before
    where you had:

        AMQP_SERVER = 'localhost'
        AMQP_PORT = 5678
        AMQP_USER = 'myuser'
        AMQP_PASSWORD = 'mypassword'
        AMQP_VHOST = 'celery'

    You need to change that to:

        BROKER_HOST = 'localhost'
        BROKER_PORT = 5678
        BROKER_USER = 'myuser'
        BROKER_PASSWORD = 'mypassword'
        BROKER_VHOST = 'celery'

-   Custom carrot backends now need to include the backend class name,
    so before where you had:

        CARROT_BACKEND = 'mycustom.backend.module'

    you need to change it to:

        CARROT_BACKEND = 'mycustom.backend.module.Backend'

    where [Backend]{.title-ref} is the class name. This is probably
    [\"Backend\"]{.title-ref}, as that was the previously implied name.

-   New version requirement for carrot: 0.8.0

### Changes {#v081-changes}

-   Incorporated the multiprocessing backport patch that fixes the
    [processName]{.title-ref} error.
-   Ignore the result of PeriodicTask\'s by default.
-   Added a Redis result store backend
-   Allow `/etc/default/celeryd`{.interpreted-text role="file"} to
    define additional options for the `celeryd` init-script.
-   MongoDB periodic tasks issue when using different time than UTC
    fixed.
-   Windows specific: Negate test for available `os.fork` (thanks
    `miracle2k`{.interpreted-text role="github_user"}).
-   Now tried to handle broken PID files.
-   Added a Django test runner to contrib that sets [CELERY_ALWAYS_EAGER
    = True]{.title-ref} for testing with the database backend.
-   Added a `CELERY_CACHE_BACKEND`{.interpreted-text role="setting"}
    setting for using something other than the Django-global cache
    backend.
-   Use custom implementation of `functools.partial` for Python 2.4
    support (Probably still problems with running on 2.4, but it will
    eventually be supported)
-   Prepare exception to pickle when saving `RETRY`{.interpreted-text
    role="state"} status for all backends.
-   SQLite no concurrency limit should only be effective if the database
    backend is used.

## 0.8.0 {#version-0.8.0}

release-date

:   2009-09-22 03:06 p.m. CEST

release-by

:   Ask Solem

### Backward incompatible changes {#v080-incompatible}

-   Add traceback to result value on failure.

    > ::: note
    > ::: title
    > Note
    > :::
    >
    > If you use the database backend you have to re-create the database
    > table [celery_taskmeta]{.title-ref}.
    >
    > Contact the `mailing-list`{.interpreted-text role="ref"} or
    > `irc-channel`{.interpreted-text role="ref"} channel for help doing
    > this.
    > :::

-   Database tables are now only created if the database backend is
    used, so if you change back to the database backend at some point,
    be sure to initialize tables (django: [syncdb]{.title-ref}, python:
    [celeryinit]{.title-ref}).

    ::: note
    ::: title
    Note
    :::

    This is only applies if using Django version 1.1 or higher.
    :::

-   Now depends on [carrot]{.title-ref} version 0.6.0.

-   Now depends on python-daemon 1.4.8

### Important changes {#v080-important}

-   Celery can now be used in pure Python (outside of a Django project).

    > This means Celery is no longer Django specific.
    >
    > For more information see the FAQ entry
    > `faq-is-celery-for-django-only`{.interpreted-text role="ref"}.

-   Celery now supports task retries.

    > See `task-retry`{.interpreted-text role="ref"} for more
    > information.

-   We now have an AMQP result store backend.

    > It uses messages to publish task return value and status. And
    > it\'s incredibly fast!
    >
    > See issue #6 for more info!

-   AMQP QoS (prefetch count) implemented:

    > This to not receive more messages than we can handle.

-   Now redirects stdout/stderr to the workers log file when detached

-   

    Now uses [inspect.getargspec]{.title-ref} to only pass default arguments

    :   the task supports.

-   

    Add Task.on_success, .on_retry, .on_failure handlers

    :   

        See `celery.task.base.Task.on_success`{.interpreted-text role="meth"},

        :   `celery.task.base.Task.on_retry`{.interpreted-text
            role="meth"},
            `celery.task.base.Task.on_failure`{.interpreted-text
            role="meth"},

-   

    \`celery.utils.gen_unique_id\`: Workaround for

    :   <http://bugs.python.org/issue4607>

-   

    You can now customize what happens at worker start, at process init, etc.,

    :   by creating your own loaders (see
        `celery.loaders.default`{.interpreted-text role="mod"},
        `celery.loaders.djangoapp`{.interpreted-text role="mod"},
        `celery.loaders`{.interpreted-text role="mod"}).

-   Support for multiple AMQP exchanges and queues.

    > This feature misses documentation and tests, so anyone interested
    > is encouraged to improve this situation.

-   The worker now survives a restart of the AMQP server!

    Automatically re-establish AMQP broker connection if it\'s lost.

    New settings:

    > -   
    >
    >     AMQP_CONNECTION_RETRY
    >
    >     :   Set to [True]{.title-ref} to enable connection retries.
    >
    > -   
    >
    >     AMQP_CONNECTION_MAX_RETRIES.
    >
    >     :   Maximum number of restarts before we give up. Default:
    >         [100]{.title-ref}.

### News {#v080-news}

-   

    Fix an incompatibility between python-daemon and multiprocessing,

    :   which resulted in the [\[Errno 10\] No child
        processes]{.title-ref} problem when detaching.

-   

    Fixed a possible DjangoUnicodeDecodeError being raised when saving pickled

    :   data to Django\`s Memcached cache backend.

-   Better Windows compatibility.

-   

    New version of the pickled field (taken from

    :   <http://www.djangosnippets.org/snippets/513/>)

-   

    New signals introduced: [task_sent]{.title-ref}, [task_prerun]{.title-ref} and

    :   [task_postrun]{.title-ref}, see
        `celery.signals`{.interpreted-text role="mod"} for more
        information.

-   

    [TaskSetResult.join]{.title-ref} caused [TypeError]{.title-ref} when [timeout=None]{.title-ref}.

    :   Thanks Jerzy Kozera. Closes #31

-   

    [views.apply]{.title-ref} should return [HttpResponse]{.title-ref} instance.

    :   Thanks to Jerzy Kozera. Closes #32

-   

    \`PeriodicTask\`: Save conversion of [run_every]{.title-ref} from [int]{.title-ref}

    :   to [timedelta]{.title-ref} to the class attribute instead of on
        the instance.

-   

    Exceptions has been moved to [celery.exceptions]{.title-ref}, but are still

    :   available in the previous module.

-   

    Try to rollback transaction and retry saving result if an error happens

    :   while setting task status with the database backend.

-   jail() refactored into
    `celery.execute.ExecuteWrapper`{.interpreted-text role="class"}.

-   [views.apply]{.title-ref} now correctly sets mime-type to
    \"application/json\"

-   [views.task_status]{.title-ref} now returns exception if state is
    `RETRY`{.interpreted-text role="state"}

-   

    [views.task_status]{.title-ref} now returns traceback if state is `FAILURE`{.interpreted-text role="state"}

    :   or `RETRY`{.interpreted-text role="state"}

-   Documented default task arguments.

-   Add a sensible \_\_repr\_\_ to ExceptionInfo for easier debugging

-   

    Fix documentation typo [.. import map]{.title-ref} -\> [.. import dmap]{.title-ref}.

    :   Thanks to `mikedizon`{.interpreted-text role="github_user"}.

## 0.6.0 {#version-0.6.0}

release-date

:   2009-08-07 06:54 a.m. CET

release-by

:   Ask Solem

### Important changes {#v060-important}

-   

    Fixed a bug where tasks raising unpickleable exceptions crashed pool

    :   workers. So if you\'ve had pool workers mysteriously
        disappearing, or problems with the worker stopping working, this
        has been fixed in this version.

-   Fixed a race condition with periodic tasks.

-   

    The task pool is now supervised, so if a pool worker crashes,

    :   goes away or stops responding, it is automatically replaced with
        a new one.

-   Task.name is now automatically generated out of class module+name,
    for example
    [\"djangotwitter.tasks.UpdateStatusesTask\"]{.title-ref}. Very
    convenient. No idea why we didn\'t do this before. Some
    documentation is updated to not manually specify a task name.

### News {#v060-news}

-   Tested with Django 1.1

-   New Tutorial: Creating a click counter using Carrot and Celery

-   

    Database entries for periodic tasks are now created at the workers

    :   start-up instead of for each check (which has been a forgotten
        TODO/XXX in the code for a long time)

-   

    New settings variable: `CELERY_TASK_RESULT_EXPIRES`{.interpreted-text role="setting"}

    :   Time (in seconds, or a [datetime.timedelta]{.title-ref} object)
        for when after stored task results are deleted. For the moment
        this only works for the database backend.

-   

    The worker now emits a debug log message for which periodic tasks

    :   has been launched.

-   

    The periodic task table is now locked for reading while getting

    :   periodic task status (MySQL only so far, seeking patches for
        other engines)

-   

    A lot more debugging information is now available by turning on the

    :   [DEBUG]{.title-ref} log level ([\--loglevel=DEBUG]{.title-ref}).

-   Functions/methods with a timeout argument now works correctly.

-   

    New: \`celery.strategy.even_time_distribution\`:

    :   With an iterator yielding task args, kwargs tuples, evenly
        distribute the processing of its tasks throughout the time
        window available.

-   Log message [Unknown task ignored\...]{.title-ref} now has log level
    [ERROR]{.title-ref}

-   

    Log message when task is received is now emitted for all tasks, even if

    :   the task has an ETA (estimated time of arrival). Also the log
        message now includes the ETA for the task (if any).

-   

    Acknowledgment now happens in the pool callback. Can\'t do ack in the job

    :   target, as it\'s not pickleable (can\'t share AMQP connection,
        etc.).

-   Added note about .delay hanging in README

-   Tests now passing in Django 1.1

-   Fixed discovery to make sure app is in INSTALLED_APPS

-   

    Previously overridden pool behavior (process reap, wait until pool worker

    :   available, etc.) is now handled by
        [multiprocessing.Pool]{.title-ref} itself.

-   Convert statistics data to Unicode for use as kwargs. Thanks Lucy!

## 0.4.1 {#version-0.4.1}

release-date

:   2009-07-02 01:42 p.m. CET

release-by

:   Ask Solem

-   Fixed a bug with parsing the message options
    ([mandatory]{.title-ref}, [routing_key]{.title-ref},
    [priority]{.title-ref}, [immediate]{.title-ref})

## 0.4.0 {#version-0.4.0}

release-date

:   2009-07-01 07:29 p.m. CET

release-by

:   Ask Solem

-   Adds eager execution.
    [celery.execute.apply]{.title-ref}\|[Task.apply]{.title-ref}
    executes the function blocking until the task is done, for API
    compatibility it returns a [celery.result.EagerResult]{.title-ref}
    instance. You can configure Celery to always run tasks locally by
    setting the `CELERY_ALWAYS_EAGER`{.interpreted-text role="setting"}
    setting to [True]{.title-ref}.
-   Now depends on [anyjson]{.title-ref}.
-   99% coverage using Python [coverage]{.title-ref} 3.0.

## 0.3.20 {#version-0.3.20}

release-date

:   2009-06-25 08:42 p.m. CET

release-by

:   Ask Solem

-   New arguments to [apply_async]{.title-ref} (the advanced version of
    [delay_task]{.title-ref}), [countdown]{.title-ref} and
    [eta]{.title-ref};

    > \>\>\> \# Run 10 seconds into the future. \>\>\> res =
    > apply_async(MyTask, countdown=10);
    >
    > \>\>\> \# Run 1 day from now \>\>\> res = apply_async(MyTask, \...
    > eta=datetime.now() + timedelta(days=1))

-   Now unlinks stale PID files

-   Lots of more tests.

-   Now compatible with carrot \>= 0.5.0.

-   **IMPORTANT** The [subtask_ids]{.title-ref} attribute on the
    [TaskSetResult]{.title-ref} instance has been removed. To get this
    information instead use:

    > \>\>\> subtask_ids = \[subtask.id for subtask in ts_res.subtasks\]

-   [Taskset.run()]{.title-ref} now respects extra message options from
    the task class.

-   Task: Add attribute \`ignore_result\`: Don\'t store the status and
    return value. This means you can\'t use the
    [celery.result.AsyncResult]{.title-ref} to check if the task is
    done, or get its return value. Only use if you need the performance
    and is able live without these features. Any exceptions raised will
    store the return value/status as usual.

-   Task: Add attribute [disable_error_emails]{.title-ref} to disable
    sending error emails for that task.

-   Should now work on Windows (although running in the background
    won\'t work, so using the [\--detach]{.title-ref} argument results
    in an exception being raised).

-   Added support for statistics for profiling and monitoring. To start
    sending statistics start the worker with the [\--statistics option.
    Then after a while you can dump the results by running \`python
    manage.py celerystats]{.title-ref}. See
    [celery.monitoring]{.title-ref} for more information.

-   The Celery daemon can now be supervised (i.e., it is automatically
    restarted if it crashes). To use this start the worker with the
    \--supervised\` option (or alternatively [-S]{.title-ref}).

-   views.apply: View calling a task.

    > Example:
    >
    > ``` text
    > http://e.com/celery/apply/task_name/arg1/arg2//?kwarg1=a&kwarg2=b
    > ```
    >
    > ::: warning
    > ::: title
    > Warning
    > :::
    >
    > Use with caution! Don\'t expose this URL to the public without
    > first ensuring that your code is safe!
    > :::

-   Refactored [celery.task]{.title-ref}. It\'s now split into three
    modules:

    > -   `celery.task`
    >
    >     > Contains [apply_async]{.title-ref},
    >     > [delay_task]{.title-ref}, [discard_all]{.title-ref}, and
    >     > task shortcuts, plus imports objects from
    >     > [celery.task.base]{.title-ref} and
    >     > [celery.task.builtins]{.title-ref}
    >
    > -   `celery.task.base`
    >
    >     > Contains task base classes: [Task]{.title-ref},
    >     > [PeriodicTask]{.title-ref}, [TaskSet]{.title-ref},
    >     > [AsynchronousMapTask]{.title-ref},
    >     > [ExecuteRemoteTask]{.title-ref}.
    >
    > -   `celery.task.builtins`
    >
    >     > Built-in tasks: [PingTask]{.title-ref},
    >     > [DeleteExpiredTaskMetaTask]{.title-ref}.

## 0.3.7 {#version-0.3.7}

release-date

:   2008-06-16 11:41 p.m. CET

release-by

:   Ask Solem

-   **IMPORTANT** Now uses AMQP\`s [basic.consume]{.title-ref} instead
    of [basic.get]{.title-ref}. This means we\'re no longer polling the
    broker for new messages.

-   **IMPORTANT** Default concurrency limit is now set to the number of
    CPUs available on the system.

-   **IMPORTANT** \`tasks.register\`: Renamed [task_name]{.title-ref}
    argument to [name]{.title-ref}, so:

        >>> tasks.register(func, task_name='mytask')

    has to be replaced with:

        >>> tasks.register(func, name='mytask')

-   The daemon now correctly runs if the pidfile is stale.

-   Now compatible with carrot 0.4.5

-   Default AMQP connection timeout is now 4 seconds.

-   [AsyncResult.read()]{.title-ref} was always returning
    [True]{.title-ref}.

-   Only use README as long_description if the file exists so
    easy_install doesn\'t break.

-   \`celery.view\`: JSON responses now properly set its mime-type.

-   [apply_async]{.title-ref} now has a [connection]{.title-ref} keyword
    argument so you can re-use the same AMQP connection if you want to
    execute more than one task.

-   Handle failures in task_status view such that it won\'t throw 500s.

-   Fixed typo [AMQP_SERVER]{.title-ref} in documentation to
    [AMQP_HOST]{.title-ref}.

-   Worker exception emails sent to administrators now works properly.

-   No longer depends on [django]{.title-ref}, so installing
    [celery]{.title-ref} won\'t affect the preferred Django version
    installed.

-   Now works with PostgreSQL (`psycopg2`{.interpreted-text
    role="pypi"}) again by registering the [PickledObject]{.title-ref}
    field.

-   Worker: Added [\--detach]{.title-ref} option as an alias to
    [\--daemon]{.title-ref}, and it\'s the term used in the
    documentation from now on.

-   Make sure the pool and periodic task worker thread is terminated
    properly at exit (so `Control-c`{.interpreted-text role="kbd"} works
    again).

-   Now depends on [python-daemon]{.title-ref}.

-   Removed dependency to [simplejson]{.title-ref}

-   Cache Backend: Re-establishes connection for every task process if
    the Django cache backend is `python-memcached`{.interpreted-text
    role="pypi"}/`libmemcached`{.interpreted-text role="pypi"}.

-   Tyrant Backend: Now re-establishes the connection for every task
    executed.

## 0.3.3 {#version-0.3.3}

release-date

:   2009-06-08 01:07 p.m. CET

release-by

:   Ask Solem

-   The [PeriodicWorkController]{.title-ref} now sleeps for 1 second
    between checking for periodic tasks to execute.

## 0.3.2 {#version-0.3.2}

release-date

:   2009-06-08 01:07 p.m. CET

release-by

:   Ask Solem

-   worker: Added option \`\--discard\`: Discard (delete!) all waiting
    messages in the queue.
-   Worker: The [\--wakeup-after]{.title-ref} option wasn\'t handled as
    a float.

## 0.3.1 {#version-0.3.1}

release-date

:   2009-06-08 01:07 p.m. CET

release-by

:   Ask Solem

-   The [PeriodicTask]{.title-ref} worker is now running in its own
    thread instead of blocking the [TaskController]{.title-ref} loop.
-   Default [QUEUE_WAKEUP_AFTER]{.title-ref} has been lowered to
    [0.1]{.title-ref} (was [0.3]{.title-ref})

## 0.3.0 {#version-0.3.0}

release-date

:   2009-06-08 12:41 p.m. CET

release-by

:   Ask Solem

::: warning
::: title
Warning
:::

This is a development version, for the stable release, please see
versions 0.2.x.
:::

**VERY IMPORTANT:** Pickle is now the encoder used for serializing task
arguments, so be sure to flush your task queue before you upgrade.

-   **IMPORTANT** TaskSet.run() now returns a
    `celery.result.TaskSetResult` instance, which lets you inspect the
    status and return values of a taskset as it was a single entity.

-   **IMPORTANT** Celery now depends on carrot \>= 0.4.1.

-   The Celery daemon now sends task errors to the registered admin
    emails. To turn off this feature, set
    [SEND_CELERY_TASK_ERROR_EMAILS]{.title-ref} to [False]{.title-ref}
    in your [settings.py]{.title-ref}. Thanks to Grégoire Cachet.

-   You can now run the Celery daemon by using \`manage.py\`:

    ``` console
    $ python manage.py celeryd
    ```

    Thanks to Grégoire Cachet.

-   Added support for message priorities, topic exchanges, custom
    routing keys for tasks. This means we\'ve introduced
    [celery.task.apply_async]{.title-ref}, a new way of executing tasks.

    You can use [celery.task.delay]{.title-ref} and
    [celery.Task.delay]{.title-ref} like usual, but if you want greater
    control over the message sent, you want
    [celery.task.apply_async]{.title-ref} and
    [celery.Task.apply_async]{.title-ref}.

    This also means the AMQP configuration has changed. Some settings
    has been renamed, while others are new:

    > -   `CELERY_AMQP_EXCHANGE`
    > -   `CELERY_AMQP_PUBLISHER_ROUTING_KEY`
    > -   `CELERY_AMQP_CONSUMER_ROUTING_KEY`
    > -   `CELERY_AMQP_CONSUMER_QUEUE`
    > -   `CELERY_AMQP_EXCHANGE_TYPE`

    See the entry `faq-task-routing`{.interpreted-text role="ref"} in
    the `FAQ <faq>`{.interpreted-text role="ref"} for more information.

-   Task errors are now logged using log level [ERROR]{.title-ref}
    instead of [INFO]{.title-ref}, and stack-traces are dumped. Thanks
    to Grégoire Cachet.

-   Make every new worker process re-establish it\'s Django DB
    connection, this solving the \"MySQL connection died?\" exceptions.
    Thanks to Vitaly Babiy and Jirka Vejrazka.

-   **IMPORTANT** Now using pickle to encode task arguments. This means
    you now can pass complex Python objects to tasks as arguments.

-   Removed dependency to [yadayada]{.title-ref}.

-   Added a FAQ, see [docs/faq.rst]{.title-ref}.

-   Now converts any Unicode keys in task [kwargs]{.title-ref} to
    regular strings. Thanks Vitaly Babiy.

-   Renamed the [TaskDaemon]{.title-ref} to
    [WorkController]{.title-ref}.

-   [celery.datastructures.TaskProcessQueue]{.title-ref} is now renamed
    to [celery.pool.TaskPool]{.title-ref}.

-   The pool algorithm has been refactored for greater performance and
    stability.

## 0.2.0 {#version-0.2.0}

release-date

:   2009-05-20 05:14 p.m. CET

release-by

:   Ask Solem

-   Final release of 0.2.0
-   Compatible with carrot version 0.4.0.
-   Fixes some syntax errors related to fetching results from the
    database backend.

## 0.2.0-pre3 {#version-0.2.0-pre3}

release-date

:   2009-05-20 05:14 p.m. CET

release-by

:   Ask Solem

-   *Internal release*. Improved handling of unpickleable exceptions,
    [get_result]{.title-ref} now tries to recreate something looking
    like the original exception.

## 0.2.0-pre2 {#version-0.2.0-pre2}

release-date

:   2009-05-20 01:56 p.m. CET

release-by

:   Ask Solem

-   Now handles unpickleable exceptions (like the dynamically generated
    subclasses of
    [django.core.exception.MultipleObjectsReturned]{.title-ref}).

## 0.2.0-pre1 {#version-0.2.0-pre1}

release-date

:   2009-05-20 12:33 p.m. CET

release-by

:   Ask Solem

-   It\'s getting quite stable, with a lot of new features, so bump
    version to 0.2. This is a pre-release.
-   [celery.task.mark_as_read()]{.title-ref} and
    [celery.task.mark_as_failure()]{.title-ref} has been removed. Use
    [celery.backends.default_backend.mark_as_read()]{.title-ref}, and
    [celery.backends.default_backend.mark_as_failure()]{.title-ref}
    instead.

## 0.1.15 {#version-0.1.15}

release-date

:   2009-05-19 04:13 p.m. CET

release-by

:   Ask Solem

-   The Celery daemon was leaking AMQP connections, this should be
    fixed, if you have any problems with too many files open (like
    [emfile]{.title-ref} errors in [rabbit.log]{.title-ref}, please
    contact us!

## 0.1.14 {#version-0.1.14}

release-date

:   2009-05-19 01:08 p.m. CET

release-by

:   Ask Solem

-   Fixed a syntax error in the [TaskSet]{.title-ref} class (no such
    variable [TimeOutError]{.title-ref}).

## 0.1.13 {#version-0.1.13}

release-date

:   2009-05-19 12:36 p.m. CET

release-by

:   Ask Solem

-   Forgot to add [yadayada]{.title-ref} to install requirements.

-   Now deletes all expired task results, not just those marked as done.

-   Able to load the Tokyo Tyrant backend class without django
    configuration, can specify tyrant settings directly in the class
    constructor.

-   Improved API documentation

-   Now using the Sphinx documentation system, you can build the html
    documentation by doing:

    > ``` console
    > $ cd docs
    > $ make html
    > ```

    and the result will be in [docs/\_build/html]{.title-ref}.

## 0.1.12 {#version-0.1.12}

release-date

:   2009-05-18 04:38 p.m. CET

release-by

:   Ask Solem

-   [delay_task()]{.title-ref} etc. now returns
    [celery.task.AsyncResult]{.title-ref} object, which lets you check
    the result and any failure that might\'ve happened. It kind of works
    like the [multiprocessing.AsyncResult]{.title-ref} class returned by
    [multiprocessing.Pool.map_async]{.title-ref}.

-   Added `dmap()` and `dmap_async()`. This works like the
    [multiprocessing.Pool]{.title-ref} versions except they\'re tasks
    distributed to the Celery server. Example:

    > ``` pycon
    > >>> from celery.task import dmap
    > >>> import operator
    > >>> dmap(operator.add, [[2, 2], [4, 4], [8, 8]])
    > >>> [4, 8, 16]
    >
    > >>> from celery.task import dmap_async
    > >>> import operator
    > >>> result = dmap_async(operator.add, [[2, 2], [4, 4], [8, 8]])
    > >>> result.ready()
    > False
    > >>> time.sleep(1)
    > >>> result.ready()
    > True
    > >>> result.result
    > [4, 8, 16]
    > ```

-   Refactored the task meta-data cache and database backends, and added
    a new backend for Tokyo Tyrant. You can set the backend in your
    django settings file.

    > Example:
    >
    > ``` python
    > CELERY_RESULT_BACKEND = 'database'; # Uses the database
    > CELERY_RESULT_BACKEND = 'cache'; # Uses the django cache framework
    > CELERY_RESULT_BACKEND = 'tyrant'; # Uses Tokyo Tyrant
    > TT_HOST = 'localhost'; # Hostname for the Tokyo Tyrant server.
    > TT_PORT = 6657; # Port of the Tokyo Tyrant server.
    > ```

## 0.1.11 {#version-0.1.11}

release-date

:   2009-05-12 02:08 p.m. CET

release-by

:   Ask Solem

-   The logging system was leaking file descriptors, resulting in
    servers stopping with the EMFILES (too many open files) error
    (fixed).

## 0.1.10 {#version-0.1.10}

release-date

:   2009-05-11 12:46 p.m. CET

release-by

:   Ask Solem

-   Tasks now supports both positional arguments and keyword arguments.
-   Requires carrot 0.3.8.
-   The daemon now tries to reconnect if the connection is lost.

## 0.1.8 {#version-0.1.8}

release-date

:   2009-05-07 12:27 p.m. CET

release-by

:   Ask Solem

-   Better test coverage
-   More documentation
-   The worker doesn\'t emit [Queue is empty]{.title-ref} message if
    [settings.CELERYD_EMPTY_MSG_EMIT_EVERY]{.title-ref} is 0.

## 0.1.7 {#version-0.1.7}

release-date

:   2009-04-30 01:50 p.m. CET

release-by

:   Ask Solem

-   Added some unit tests
-   Can now use the database for task meta-data (like if the task has
    been executed or not). Set [settings.CELERY_TASK_META]{.title-ref}
-   Can now run [python setup.py test]{.title-ref} to run the unit tests
    from within the [tests]{.title-ref} project.
-   Can set the AMQP exchange/routing key/queue using
    [settings.CELERY_AMQP_EXCHANGE]{.title-ref},
    [settings.CELERY_AMQP_ROUTING_KEY]{.title-ref}, and
    [settings.CELERY_AMQP_CONSUMER_QUEUE]{.title-ref}.

## 0.1.6 {#version-0.1.6}

release-date

:   2009-04-28 02:13 p.m. CET

release-by

:   Ask Solem

-   Introducing [TaskSet]{.title-ref}. A set of subtasks is executed and
    you can find out how many, or if all them, are done (excellent for
    progress bars and such)

-   Now catches all exceptions when running
    [Task.\_\_call\_\_]{.title-ref}, so the daemon doesn\'t die. This
    doesn\'t happen for pure functions yet, only [Task]{.title-ref}
    classes.

-   [autodiscover()]{.title-ref} now works with zipped eggs.

-   Worker: Now adds current working directory to [sys.path]{.title-ref}
    for convenience.

-   The [run_every]{.title-ref} attribute of [PeriodicTask]{.title-ref}
    classes can now be a [datetime.timedelta()]{.title-ref} object.

-   Worker: You can now set the [DJANGO_PROJECT_DIR]{.title-ref}
    variable for the worker and it will add that to
    [sys.path]{.title-ref} for easy launching.

-   Can now check if a task has been executed or not via HTTP.

-   You can do this by including the Celery [urls.py]{.title-ref} into
    your project,

    > \>\>\> url(r\'\^celery/\$\', include(\'celery.urls\'))

    then visiting the following URL:

    ``` text
    http://mysite/celery/$task_id/done/
    ```

    this will return a JSON dictionary, for example:

    ``` json
    {"task": {"id": "TASK_ID", "executed": true}}
    ```

-   [delay_task]{.title-ref} now returns string id, not
    [uuid.UUID]{.title-ref} instance.

-   Now has [PeriodicTasks]{.title-ref}, to have [cron]{.title-ref} like
    functionality.

-   Project changed name from [crunchy]{.title-ref} to
    [celery]{.title-ref}. The details of the name change request is in
    [docs/name_change_request.txt]{.title-ref}.

## 0.1.0 {#version-0.1.0}

release-date

:   2009-04-24 11:28 a.m. CET

release-by

:   Ask Solem

-   Initial release

Sphinx started sucking by removing images from \_static, so we need to
add them here into actual content to ensure they are included :-(

![image](../images/celery-banner.png)

![image](../images/celery-banner-small.png)
