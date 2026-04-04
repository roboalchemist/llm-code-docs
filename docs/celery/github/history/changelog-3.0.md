# Change history for Celery 3.0 {#changelog-3.0}

::: {.contents local=""}
:::

If you\'re looking for versions prior to 3.0.x you should go to
`history`{.interpreted-text role="ref"}.

## 3.0.24 {#version-3.0.24}

release-date

:   2013-10-11 04:40 p.m. BST

release-by

:   Ask Solem

-   Now depends on
    `Kombu 2.5.15 <kombu:version-2.5.15>`{.interpreted-text role="ref"}.

-   Now depends on `billiard`{.interpreted-text role="pypi"} version
    2.7.3.34.

-   AMQP Result backend: No longer caches queue declarations.

    > The queues created by the AMQP result backend are always unique,
    > so caching the declarations caused a slow memory leak.

-   Worker: Fixed crash when hostname contained Unicode characters.

    > Contributed by Daodao.

-   The worker would no longer start if the [-P solo]{.title-ref} pool
    was selected (Issue #1548).

-   Redis/Cache result backends wouldn\'t complete chords if any of the
    tasks were retried (Issue #1401).

-   Task decorator is no longer lazy if app is finalized.

-   AsyncResult: Fixed bug with `copy(AsyncResult)` when no
    `current_app` available.

-   ResultSet: Now properly propagates app when passed string id\'s.

-   Loader now ignores `CELERY_CONFIG_MODULE`{.interpreted-text
    role="envvar"} if value is empty string.

-   Fixed race condition in Proxy object where it tried to delete an
    attribute twice, resulting in `AttributeError`{.interpreted-text
    role="exc"}.

-   Task methods now works with the
    `CELERY_ALWAYS_EAGER`{.interpreted-text role="setting"} setting
    (Issue #1478).

-   `~kombu.common.Broadcast`{.interpreted-text role="class"} queues
    were accidentally declared when publishing tasks (Issue #1540).

-   New `C_FAKEFORK`{.interpreted-text role="envvar"} environment
    variable can be used to debug the init-scripts.

    > Setting this will skip the daemonization step so that errors
    > printed to stderr after standard outs are closed can be seen:
    >
    > ``` console
    > $ C_FAKEFORK /etc/init.d/celeryd start
    > ```
    >
    > This works with the [celery multi]{.title-ref} command in general.

-   `get_pickleable_etype` didn\'t always return a value (Issue #1556).

-   Fixed bug where `app.GroupResult.restore` would fall back to the
    default app.

-   Fixed rare bug where built-in tasks would use the current_app.

-   `~celery.platforms.maybe_fileno`{.interpreted-text role="func"} now
    handles `ValueError`{.interpreted-text role="exc"}.

## 3.0.23 {#version-3.0.23}

release-date

:   2013-09-02 01:00 p.m. BST

release-by

:   Ask Solem

-   Now depends on
    `Kombu 2.5.14 <kombu:version-2.5.14>`{.interpreted-text role="ref"}.

-   `send_task` didn\'t honor `link` and `link_error` arguments.

    > This had the side effect of chains not calling unregistered tasks,
    > silently discarding them.
    >
    > Fix contributed by Taylor Nelson.

-   `celery.state`{.interpreted-text role="mod"}: Optimized precedence
    lookup.

    > Contributed by Matt Robenolt.

-   POSIX: Daemonization didn\'t redirect `sys.stdin` to `/dev/null`.

    > Fix contributed by Alexander Smirnov.

-   Canvas: group bug caused fallback to default app when `.apply_async`
    used (Issue #1516)

-   Canvas: generator arguments wasn\'t always pickleable.

## 3.0.22 {#version-3.0.22}

release-date

:   2013-08-16 04:30 p.m. BST

release-by

:   Ask Solem

-   Now depends on
    `Kombu 2.5.13 <kombu:version-2.5.13>`{.interpreted-text role="ref"}.

-   Now depends on `billiard`{.interpreted-text role="pypi"} 2.7.3.32

-   Fixed bug with monthly and yearly Crontabs (Issue #1465).

    > Fix contributed by Guillaume Gauvrit.

-   Fixed memory leak caused by time limits (Issue #1129, Issue #1427)

-   Worker will now sleep if being restarted more than 5 times in one
    second to avoid spamming with `worker-online` events.

-   Includes documentation fixes

    > Contributed by: Ken Fromm, Andreas Savvides, Alex Kiriukha,
    > Michael Fladischer.

## 3.0.21 {#version-3.0.21}

release-date

:   2013-07-05 04:30 p.m. BST

release-by

:   Ask Solem

-   Now depends on `billiard`{.interpreted-text role="pypi"} 2.7.3.31.

    > This version fixed a bug when running without the billiard C
    > extension.

-   3.0.20 broke eventlet/gevent support (worker not starting).

-   Fixed memory leak problem when MongoDB result backend was used with
    the gevent pool.

    > Fix contributed by Ross Lawley.

## 3.0.20 {#version-3.0.20}

release-date

:   2013-06-28 04:00 p.m. BST

release-by

:   Ask Solem

-   Contains workaround for deadlock problems.

    > A better solution will be part of Celery 3.1.

-   Now depends on
    `Kombu 2.5.12 <kombu:version-2.5.12>`{.interpreted-text role="ref"}.

-   Now depends on `billiard`{.interpreted-text role="pypi"} 2.7.3.30.

-   `--loader <celery --loader>`{.interpreted-text role="option"}
    argument no longer supported importing loaders from the current
    directory.

-   \[Worker\] Fixed memory leak when restarting after connection lost
    (Issue #1325).

-   \[Worker\] Fixed UnicodeDecodeError at start-up (Issue #1373).

    > Fix contributed by Jessica Tallon.

-   \[Worker\] Now properly rewrites unpickleable exceptions again.

-   Fixed possible race condition when evicting items from the revoked
    task set.

-   \[generic-init.d\] Fixed compatibility with Ubuntu\'s minimal Dash
    shell (Issue #1387).

    > Fix contributed by `monkut`{.interpreted-text role="github_user"}.

-   `Task.apply`/`ALWAYS_EAGER` now also executes callbacks and errbacks
    (Issue #1336).

-   \[Worker\] The `worker-shutdown`{.interpreted-text role="signal"}
    signal was no longer being dispatched (Issue #1339)j

-   \[Python 3\] Fixed problem with threading.Event.

    > Fix contributed by Xavier Ordoquy.

-   \[Python 3\] Now handles `io.UnsupportedOperation` that may be
    raised by `file.fileno()` in Python 3.

-   \[Python 3\] Fixed problem with `qualname`.

-   \[events.State\] Now ignores unknown event-groups.

-   \[MongoDB backend\] No longer uses deprecated `safe` parameter.

    > Fix contributed by `rfkrocktk`{.interpreted-text
    > role="github_user"}.

-   The eventlet pool now imports on Windows.

-   \[Canvas\] Fixed regression where immutable chord members may
    receive arguments (Issue #1340).

    > Fix contributed by Peter Brook.

-   \[Canvas\] chain now accepts generator argument again (Issue #1319).

-   `celery.migrate` command now consumes from all queues if no queues
    specified.

    > Fix contributed by John Watson.

## 3.0.19 {#version-3.0.19}

release-date

:   2013-04-17 04:30:00 p.m. BST

release-by

:   Ask Solem

-   Now depends on `billiard`{.interpreted-text role="pypi"} 2.7.3.28

-   A Python 3 related fix managed to disable the deadlock fix announced
    in 3.0.18.

    > Tests have been added to make sure this doesn\'t happen again.

-   Task retry policy: Default max_retries is now 3.

    > This ensures clients won\'t be hanging while the broker is down.
    >
    > ::: note
    > ::: title
    > Note
    > :::
    >
    > You can set a longer retry for the worker by using the
    > `celeryd_after_setup`{.interpreted-text role="signal"} signal:
    >
    > ``` python
    > from celery.signals import celeryd_after_setup
    >
    > @celeryd_after_setup.connect
    > def configure_worker(instance, conf, **kwargs):
    >     conf.CELERY_TASK_PUBLISH_RETRY_POLICY = {
    >         'max_retries': 100,
    >         'interval_start': 0,
    >         'interval_max': 1,
    >         'interval_step': 0.2,
    >     }
    > ```
    > :::

-   Worker: Will now properly display message body in error messages
    even if the body is a buffer instance.

-   3.0.18 broke the MongoDB result backend (Issue #1303).

## 3.0.18 {#version-3.0.18}

release-date

:   2013-04-12 05:00:00 p.m. BST

release-by

:   Ask Solem

-   Now depends on `kombu`{.interpreted-text role="pypi"} 2.5.10.

    > See the `kombu changelog <kombu:version-2.5.10>`{.interpreted-text
    > role="ref"}.

-   Now depends on `billiard`{.interpreted-text role="pypi"} 2.7.3.27.

-   Can now specify a white-list of accepted serializers using the new
    `CELERY_ACCEPT_CONTENT`{.interpreted-text role="setting"} setting.

    > This means that you can force the worker to discard messages
    > serialized with pickle and other untrusted serializers. For
    > example to only allow JSON serialized messages use:
    >
    >     CELERY_ACCEPT_CONTENT = ['json']
    >
    > you can also specify MIME types in the white-list:
    >
    >     CELERY_ACCEPT_CONTENT = ['application/json']

-   Fixed deadlock in multiprocessing\'s pool caused by the semaphore
    not being released when terminated by signal.

-   Processes Pool: It\'s now possible to debug pool processes using
    GDB.

-   `celery report` now censors possibly secret settings, like passwords
    and secret tokens.

    > You should still check the output before pasting anything on the
    > internet.

-   Connection URLs now ignore multiple \'+\' tokens.

-   Worker/`statedb`: Now uses pickle protocol 2 (Python 2.5+)

-   Fixed Python 3 compatibility issues.

-   Worker: A warning is now given if a worker is started with the same
    node name as an existing worker.

-   Worker: Fixed a deadlock that could occur while revoking tasks
    (Issue #1297).

-   Worker: The `HUP`{.interpreted-text role="sig"} handler now closes
    all open file descriptors before restarting to ensure file
    descriptors doesn\'t leak (Issue #1270).

-   Worker: Optimized storing/loading the revoked tasks list (Issue
    #1289).

    > After this change the `celery worker --statedb`{.interpreted-text
    > role="option"} file will take up more disk space, but loading from
    > and storing the revoked tasks will be considerably faster (what
    > before took 5 minutes will now take less than a second).

-   Celery will now suggest alternatives if there\'s a typo in the
    broker transport name (e.g., `ampq` -\> `amqp`).

-   Worker: The auto-reloader would cause a crash if a monitored file
    was unlinked.

    > Fix contributed by Agris Ameriks.

-   Fixed AsyncResult pickling error.

    > Fix contributed by Thomas Minor.

-   Fixed handling of Unicode in logging output when using log colors
    (Issue #427).

-   `~celery.app.utils.ConfigurationView`{.interpreted-text
    role="class"} is now a `MutableMapping`.

    > Contributed by Aaron Harnly.

-   Fixed memory leak in LRU cache implementation.

    > Fix contributed by Romuald Brunet.

-   `celery.contrib.rdb`: Now works when sockets are in non-blocking
    mode.

    > Fix contributed by Theo Spears.

-   The [inspect reserved]{.title-ref} remote control command included
    active (started) tasks with the reserved tasks (Issue #1030).

-   The `task_failure`{.interpreted-text role="signal"} signal received
    a modified traceback object meant for pickling purposes, this has
    been fixed so that it now receives the real traceback instead.

-   The `@task` decorator silently ignored positional arguments, it now
    raises the expected `TypeError`{.interpreted-text role="exc"}
    instead (Issue #1125).

-   The worker will now properly handle messages with invalid
    ETA/expires fields (Issue #1232).

-   The `pool_restart` remote control command now reports an error if
    the `CELERYD_POOL_RESTARTS`{.interpreted-text role="setting"}
    setting isn\'t set.

-   `@add_defaults`{.interpreted-text role="meth"}\` can now be used
    with non-dict objects.

-   Fixed compatibility problems in the Proxy class (Issue #1087).

    > The class attributes `__module__`, `__name__` and `__doc__` are
    > now meaningful string objects.
    >
    > Thanks to Marius Gedminas.

-   MongoDB Backend: The `MONGODB_BACKEND_SETTINGS`{.interpreted-text
    role="setting"} setting now accepts a `option` key that lets you
    forward arbitrary kwargs to the underlying `pymongo.Connection`
    object (Issue #1015).

-   Beat: The daily backend cleanup task is no longer enabled for result
    backends that support automatic result expiration (Issue #1031).

-   Canvas list operations now takes application instance from the first
    task in the list, instead of depending on the `current_app` (Issue
    #1249).

-   Worker: Message decoding error log message now includes traceback
    information.

-   Worker: The start-up banner now includes system platform.

-   `celery inspect|status|control` now gives an error if used with a
    SQL based broker transport.

## 3.0.17 {#version-3.0.17}

release-date

:   2013-03-22 04:00:00 p.m. UTC

release-by

:   Ask Solem

-   Now depends on kombu 2.5.8

-   Now depends on billiard 2.7.3.23

-   RabbitMQ/Redis: thread-less and lock-free rate-limit implementation.

    > This means that rate limits pose minimal overhead when used with
    > RabbitMQ/Redis or future transports using the event-loop, and that
    > the rate-limit implementation is now thread-less and lock-free.
    >
    > The thread-based transports will still use the old implementation
    > for now, but the plan is to use the timer also for other broker
    > transports in Celery 3.1.

-   Rate limits now works with eventlet/gevent if using RabbitMQ/Redis
    as the broker.

-   A regression caused `task.retry` to ignore additional keyword
    arguments.

    > Extra keyword arguments are now used as execution options again.
    > Fix contributed by Simon Engledew.

-   Windows: Fixed problem with the worker trying to pickle the Django
    settings module at worker start-up.

-   generic-init.d: No longer double quotes `$CELERYD_CHDIR` (Issue
    #1235).

-   generic-init.d: Removes bash-specific syntax.

    > Fix contributed by Pär Wieslander.

-   Cassandra Result Backend: Now handles the
    `~pycassa.AllServersUnavailable`{.interpreted-text role="exc"} error
    (Issue #1010).

    > Fix contributed by Jared Biel.

-   Result: Now properly forwards apps to GroupResults when
    deserializing (Issue #1249).

    > Fix contributed by Charles-Axel Dein.

-   `GroupResult.revoke` now supports the `terminate` and `signal`
    keyword arguments.

-   Worker: Multiprocessing pool workers now import task
    modules/configuration before setting up the logging system so that
    logging signals can be connected before they\'re dispatched.

-   chord: The `AsyncResult` instance returned now has its `parent`
    attribute set to the header `GroupResult`.

    > This is consistent with how `chain` works.

## 3.0.16 {#version-3.0.16}

release-date

:   2013-03-07 04:00:00 p.m. UTC

release-by

:   Ask Solem

-   Happy International Women\'s Day!

    > We have a long way to go, so this is a chance for you to get
    > involved in one of the organizations working for making our
    > communities more diverse.
    >
    > > -   PyLadies --- <http://pyladies.com>
    > > -   Girls Who Code --- <http://www.girlswhocode.com>
    > > -   Women Who Code ---
    > >     <http://www.meetup.com/Women-Who-Code-SF/>

-   Now depends on `kombu`{.interpreted-text role="pypi"} version 2.5.7

-   Now depends on `billiard`{.interpreted-text role="pypi"} version
    2.7.3.22

-   AMQP heartbeats are now disabled by default.

    > Some users experiences issues with heartbeats enabled, and it\'s
    > not strictly necessary to use them.
    >
    > If you\'re experiencing problems detecting connection failures,
    > you can re-enable heartbeats by configuring the
    > `BROKER_HEARTBEAT`{.interpreted-text role="setting"} setting.

-   Worker: Now propagates connection errors occurring in
    multiprocessing callbacks, so that the connection can be reset
    (Issue #1226).

-   Worker: Now propagates connection errors occurring in timer
    callbacks, so that the connection can be reset.

-   The modules in `CELERY_IMPORTS`{.interpreted-text role="setting"}
    and `CELERY_INCLUDE`{.interpreted-text role="setting"} are now
    imported in the original order (Issue #1161).

    > The modules in `CELERY_IMPORTS`{.interpreted-text role="setting"}
    > will be imported first, then continued by
    > `CELERY_INCLUDE`{.interpreted-text role="setting"}.
    >
    > Thanks to Joey Wilhelm.

-   New bash completion for `celery` available in the git repository:

    > <https://github.com/celery/celery/tree/3.0/extra/bash-completion>
    >
    > You can source this file or put it in `bash_completion.d` to get
    > auto-completion for the `celery` command-line utility.

-   The node name of a worker can now include unicode characters (Issue
    #1186).

-   The repr of a `crontab` object now displays correctly (Issue #972).

-   `events.State` no longer modifies the original event dictionary.

-   No longer uses `Logger.warn` deprecated in Python 3.

-   Cache Backend: Now works with chords again (Issue #1094).

-   Chord unlock now handles errors occurring while calling the
    callback.

-   Generic worker init.d script: Status check is now performed by
    querying the pid of the instance instead of sending messages.

    > Contributed by Milen Pavlov.

-   Improved init-scripts for CentOS.

    > -   Updated to support Celery 3.x conventions.
    > -   Now uses CentOS built-in `status` and `killproc`
    > -   Support for multi-node / multi-pid worker services.
    > -   Standard color-coded CentOS service-init output.
    > -   A test suite.
    >
    > Contributed by Milen Pavlov.

-   `ResultSet.join` now always works with empty result set (Issue
    #1219).

-   A `group` consisting of a single task is now supported (Issue
    #1219).

-   Now supports the `pycallgraph` program (Issue #1051).

-   Fixed Jython compatibility problems.

-   Django tutorial: Now mentions that the example app must be added to
    `INSTALLED_APPS` (Issue #1192).

## 3.0.15 {#version-3.0.15}

release-date

:   2013-02-11 04:30:00 p.m. UTC

release-by

:   Ask Solem

-   Now depends on billiard 2.7.3.21 which fixed a syntax error crash.
-   Fixed bug with `CELERY_SEND_TASK_SENT_EVENT`{.interpreted-text
    role="setting"}.

## 3.0.14 {#version-3.0.14}

release-date

:   2013-02-08 05:00:00 p.m. UTC

release-by

:   Ask Solem

-   Now depends on Kombu 2.5.6

-   Now depends on billiard 2.7.3.20

-   `execv` is now disabled by default.

    > It was causing too many problems for users, you can still enable
    > it using the [CELERYD_FORCE_EXECV]{.title-ref} setting.
    >
    > execv was only enabled when transports other than AMQP/Redis was
    > used, and it\'s there to prevent deadlocks caused by mutexes not
    > being released before the process forks. Unfortunately it also
    > changes the environment introducing many corner case bugs that\'re
    > hard to fix without adding horrible hacks. Deadlock issues are
    > reported far less often than the bugs that execv are causing, so
    > we now disable it by default.
    >
    > Work is in motion to create non-blocking versions of these
    > transports so that execv isn\'t necessary (which is the situation
    > with the amqp and redis broker transports)

-   Chord exception behavior defined (Issue #1172).

    > From Celery 3.1 the chord callback will change state to FAILURE
    > when a task part of a chord raises an exception.
    >
    > It was never documented what happens in this case, and the actual
    > behavior was very unsatisfactory, indeed it will just forward the
    > exception value to the chord callback.
    >
    > For backward compatibility reasons we don\'t change to the new
    > behavior in a bugfix release, even if the current behavior was
    > never documented. Instead you can enable the
    > `CELERY_CHORD_PROPAGATES`{.interpreted-text role="setting"}
    > setting to get the new behavior that\'ll be default from Celery
    > 3.1.
    >
    > See more at `chord-errors`{.interpreted-text role="ref"}.

-   worker: Fixes bug with ignored and retried tasks.

    > The `on_chord_part_return` and `Task.after_return` callbacks, nor
    > the `task_postrun` signal should be called when the task was
    > retried/ignored.
    >
    > Fix contributed by Vlad.

-   `GroupResult.join_native` now respects the `propagate` argument.

-   `subtask.id` added as an alias to `subtask['options'].id`

    > ``` pycon
    > >>> s = add.s(2, 2)
    > >>> s.id = 'my-id'
    > >>> s['options']
    > {'task_id': 'my-id'}
    >
    > >>> s.id
    > 'my-id'
    > ```

-   worker: Fixed error [Could not start worker processes]{.title-ref}
    occurring when restarting after connection failure (Issue #1118).

-   Adds new signal `task-retried`{.interpreted-text role="signal"}
    (Issue #1169).

-   [celery events \--dumper]{.title-ref} now handles connection loss.

-   Will now retry sending the task-sent event in case of connection
    failure.

-   amqp backend: Now uses `Message.requeue` instead of republishing the
    message after poll.

-   New `BROKER_HEARTBEAT_CHECKRATE`{.interpreted-text role="setting"}
    setting introduced to modify the rate at which broker connection
    heartbeats are monitored.

    > The default value was also changed from 3.0 to 2.0.

-   `celery.events.state.State`{.interpreted-text role="class"} is now
    pickleable.

    > Fix contributed by Mher Movsisyan.

-   `celery.utils.functional.LRUCache`{.interpreted-text role="class"}
    is now pickleable.

    > Fix contributed by Mher Movsisyan.

-   The stats broadcast command now includes the workers pid.

    > Contributed by Mher Movsisyan.

-   New `conf` remote control command to get a workers current
    configuration.

    > Contributed by Mher Movsisyan.

-   Adds the ability to modify the chord unlock task\'s countdown
    argument (Issue #1146).

    > Contributed by Jun Sakai

-   beat: The scheduler now uses the [now()]{.title-ref}\` method of the
    schedule, so that schedules can provide a custom way to get the
    current date and time.

    > Contributed by Raphaël Slinckx

-   Fixed pickling of configuration modules on Windows or when execv is
    used (Issue #1126).

-   Multiprocessing logger is now configured with loglevel `ERROR` by
    default.

    > Since 3.0 the multiprocessing loggers were disabled by default
    > (only configured when the `MP_LOG`{.interpreted-text
    > role="envvar"} environment variable was set).

## 3.0.13 {#version-3.0.13}

release-date

:   2013-01-07 04:00:00 p.m. UTC

release-by

:   Ask Solem

-   Now depends on Kombu 2.5

    > -   `amqp`{.interpreted-text role="pypi"} has replaced
    >     `amqplib`{.interpreted-text role="pypi"} as the default
    >     transport, gaining support for AMQP 0.9, and the RabbitMQ
    >     extensions, including Consumer Cancel Notifications and
    >     heartbeats.
    > -   support for multiple connection URLs for failover.
    > -   Read more in the
    >     `Kombu 2.5 changelog <kombu:version-2.5.0>`{.interpreted-text
    >     role="ref"}.

-   Now depends on billiard 2.7.3.19

-   Fixed a deadlock issue that could occur when the producer pool
    inherited the connection pool instance of the parent process.

-   The `--loader <celery --loader>`{.interpreted-text role="option"}
    option now works again (Issue #1066).

-   `celery`{.interpreted-text role="program"} umbrella command: All
    sub-commands now supports the
    `--workdir <celery --workdir>`{.interpreted-text role="option"}
    option (Issue #1063).

-   Groups included in chains now give GroupResults (Issue #1057)

    > Previously it would incorrectly add a regular result instead of a
    > group result, but now this works:
    >
    > ``` pycon
    > >>> # [4 + 4, 4 + 8, 16 + 8]
    > >>> res = (add.s(2, 2) | group(add.s(4), add.s(8), add.s(16)))()
    > >>> res
    > <GroupResult: a0acf905-c704-499e-b03a-8d445e6398f7 [
    >     4346501c-cb99-4ad8-8577-12256c7a22b1,
    >     b12ead10-a622-4d44-86e9-3193a778f345,
    >     26c7a420-11f3-4b33-8fac-66cd3b62abfd]>
    > ```

-   Chains can now chain other chains and use partial arguments (Issue
    #1057).

    > Example:
    >
    > ``` pycon
    > >>> c1 = (add.s(2) | add.s(4))
    > >>> c2 = (add.s(8) | add.s(16))
    >
    > >>> c3 = (c1 | c2)
    >
    > >>> # 8 + 2 + 4 + 8 + 16
    > >>> assert c3(8).get() == 38
    > ```

-   Subtasks can now be used with unregistered tasks.

    > You can specify subtasks even if you just have the name:
    >
    >     >>> s = subtask(task_name, args=(), kwargs=())
    >     >>> s.delay()

-   The `celery shell`{.interpreted-text role="program"} command now
    always adds the current directory to the module path.

-   The worker will now properly handle the
    `pytz.AmbiguousTimeError`{.interpreted-text role="exc"} exception
    raised when an ETA/countdown is prepared while being in DST
    transition (Issue #1061).

-   force_execv: Now makes sure that task symbols in the original task
    modules will always use the correct app instance (Issue #1072).

-   AMQP Backend: Now republishes result messages that have been polled
    (using `result.ready()` and friends, `result.get()` won\'t do this
    in this version).

-   Crontab schedule values can now \"wrap around\"

    > This means that values like `11-1` translates to `[11, 12, 1]`.
    >
    > Contributed by Loren Abrams.

-   `multi stopwait` command now shows the pid of processes.

    > Contributed by Loren Abrams.

-   

    Handling of ETA/countdown fixed when the `CELERY_ENABLE_UTC`{.interpreted-text role="setting"}

    :   setting is disabled (Issue #1065).

-   A number of unneeded properties were included in messages, caused by
    accidentally passing `Queue.as_dict` as message properties.

-   Rate limit values can now be float

    > This also extends the string format so that values like `"0.5/s"`
    > works.
    >
    > Contributed by Christoph Krybus

-   Fixed a typo in the broadcast routing documentation (Issue #1026).

-   Rewrote confusing section about idempotence in the task user guide.

-   Fixed typo in the daemonization tutorial (Issue #1055).

-   Fixed several typos in the documentation.

    > Contributed by Marius Gedminas.

-   Batches: Now works when using the eventlet pool.

    > Fix contributed by Thomas Grainger.

-   Batches: Added example sending results to `celery.contrib.batches`.

    > Contributed by Thomas Grainger.

-   MongoDB backend: Connection `max_pool_size` can now be set in
    `CELERY_MONGODB_BACKEND_SETTINGS`{.interpreted-text role="setting"}.

    > Contributed by Craig Younkins.

-   Fixed problem when using earlier versions of
    `pytz`{.interpreted-text role="pypi"}.

    > Fix contributed by Vlad.

-   Docs updated to include the default value for the
    `CELERY_TASK_RESULT_EXPIRES`{.interpreted-text role="setting"}
    setting.

-   Improvements to the `django-celery`{.interpreted-text role="pypi"}
    tutorial.

    > Contributed by Locker537.

-   The `add_consumer` control command didn\'t properly persist the
    addition of new queues so that they survived connection failure
    (Issue #1079).

## 3.0.12

release-date

:   2012-11-06 02:00 p.m. UTC

release-by

:   Ask Solem

-   Now depends on kombu 2.4.8

    > -   \[Redis\] New and improved fair queue cycle algorithm (Kevin
    >     McCarthy).
    >
    > -   \[Redis\] Now uses a Redis-based mutex when restoring
    >     messages.
    >
    > -   
    >
    >     \[Redis\] Number of messages that can be restored in one interval is no
    >
    >     :   longer limited (but can be set using the
    >         `unacked_restore_limit`
    >         `transport option <BROKER_TRANSPORT_OPTIONS>`{.interpreted-text
    >         role="setting"}).
    >
    > -   Heartbeat value can be specified in broker URLs (Mher
    >     Movsisyan).
    >
    > -   Fixed problem with msgpack on Python 3 (Jasper Bryant-Greene).

-   Now depends on billiard 2.7.3.18

-   Celery can now be used with static analysis tools like
    PyDev/PyCharm/pylint etc.

-   Development documentation has moved to Read The Docs.

    > The new URL is: <https://docs.celeryq.dev/en/master>

-   New `CELERY_QUEUE_HA_POLICY`{.interpreted-text role="setting"}
    setting used to set the default HA policy for queues when using
    RabbitMQ.

-   New method `Task.subtask_from_request` returns a subtask using the
    current request.

-   Results get_many method didn\'t respect timeout argument.

    > Fix contributed by Remigiusz Modrzejewski

-   generic_init.d scripts now support setting
    `CELERY_CREATE_DIRS`{.interpreted-text role="envvar"} to always
    create log and pid directories (Issue #1045).

    > This can be set in your `/etc/default/celeryd`{.interpreted-text
    > role="file"}.

-   Fixed strange kombu import problem on Python 3.2 (Issue #1034).

-   Worker: ETA scheduler now uses millisecond precision (Issue #1040).

-   The `--config <celery --config>`{.interpreted-text role="option"}
    argument to programs is now supported by all loaders.

-   The `CASSANDRA_OPTIONS`{.interpreted-text role="setting"} setting
    has now been documented.

    > Contributed by Jared Biel.

-   Task methods (`celery.contrib.methods`{.interpreted-text
    role="mod"}) cannot be used with the old task base class, the task
    decorator in that module now inherits from the new.

-   An optimization was too eager and caused some logging messages to
    never emit.

-   `celery.contrib.batches` now works again.

-   Fixed missing white-space in `bdist_rpm` requirements (Issue #1046).

-   Event state\'s `tasks_by_name` applied limit before filtering by
    name.

    > Fix contributed by Alexander A. Sosnovskiy.

## 3.0.11 {#version-3.0.11}

release-date

:   2012-09-26 04:00 p.m. UTC

release-by

:   Ask Solem

-   \[security:low\] generic-init.d scripts changed permissions of
    /var/log & /var/run

    > In the daemonization tutorial the recommended directories were as
    > follows:
    >
    > ``` bash
    > CELERYD_LOG_FILE="/var/log/celery/%n.log"
    > CELERYD_PID_FILE="/var/run/celery/%n.pid"
    > ```
    >
    > But in the scripts themselves the default files were
    > `/var/log/celery%n.log` and `/var/run/celery%n.pid`, so if the
    > user didn\'t change the location by configuration, the directories
    > `/var/log` and `/var/run` would be created - and worse have their
    > permissions and owners changed.
    >
    > This change means that:
    >
    > > -   Default pid file is `/var/run/celery/%n.pid`
    > > -   Default log file is `/var/log/celery/%n.log`
    > > -   The directories are only created and have their permissions
    > >     changed if *no custom locations are set*.
    >
    > Users can force paths to be created by calling the `create-paths`
    > sub-command:
    >
    > ``` console
    > $ sudo /etc/init.d/celeryd create-paths
    > ```
    >
    > ::: admonition
    > Upgrading Celery won\'t update init-scripts
    >
    > To update the init-scripts you have to re-download the files from
    > source control and update them manually. You can find the
    > init-scripts for version 3.0.x at:
    >
    > > <https://github.com/celery/celery/tree/3.0/extra/generic-init.d>
    > :::

-   Now depends on billiard 2.7.3.17

-   Fixes request stack protection when app is initialized more than
    once (Issue #1003).

-   ETA tasks now properly works when system timezone isn\'t same as the
    configured timezone (Issue #1004).

-   Terminating a task now works if the task has been sent to the pool
    but not yet acknowledged by a pool process (Issue #1007).

    > Fix contributed by Alexey Zatelepin

-   Terminating a task now properly updates the state of the task to
    revoked, and sends a `task-revoked` event.

-   Generic worker init-script now waits for workers to shutdown by
    default.

-   Multi: No longer parses \--app option (Issue #1008).

-   Multi: `stop_verify` command renamed to `stopwait`.

-   Daemonization: Now delays trying to create pidfile/logfile until
    after the working directory has been changed into.

-   `celery worker`{.interpreted-text role="program"} and
    `celery beat`{.interpreted-text role="program"} commands now
    respects the `--no-color <celery --no-color>`{.interpreted-text
    role="option"} option (Issue #999).

-   Fixed typos in eventlet examples (Issue #1000)

    > Fix contributed by Bryan Bishop. Congratulations on opening bug
    > #1000!

-   Tasks that raise `~celery.exceptions.Ignore`{.interpreted-text
    role="exc"} are now acknowledged.

-   Beat: Now shows the name of the entry in `sending due task` logs.

## 3.0.10 {#version-3.0.10}

release-date

:   2012-09-20 05:30 p.m. BST

release-by

:   Ask Solem

-   Now depends on kombu 2.4.7

-   Now depends on billiard 2.7.3.14

    > -   Fixes crash at start-up when using Django and pre-1.4 projects
    >     (`setup_environ`).
    >
    > -   Hard time limits now sends the KILL signal shortly after TERM,
    >     to terminate processes that have signal handlers blocked by C
    >     extensions.
    >
    > -   Billiard now installs even if the C extension cannot be built.
    >
    >     > It\'s still recommended to build the C extension if you\'re
    >     > using a transport other than RabbitMQ/Redis (or use forced
    >     > execv for some other reason).
    >
    > -   Pool now sets a `current_process().index` attribute that can
    >     be used to create as many log files as there are processes in
    >     the pool.

-   Canvas: chord/group/chain no longer modifies the state when called

    > Previously calling a chord/group/chain would modify the ids of
    > subtasks so that:
    >
    > ``` pycon
    > >>> c = chord([add.s(2, 2), add.s(4, 4)], xsum.s())
    > >>> c()
    > >>> c() <-- call again
    > ```
    >
    > at the second time the ids for the tasks would be the same as in
    > the previous invocation. This is now fixed, so that calling a
    > subtask won\'t mutate any options.

-   Canvas: Chaining a chord to another task now works (Issue #965).

-   Worker: Fixed a bug where the request stack could be corrupted if
    relative imports are used.

    > Problem usually manifested itself as an exception while trying to
    > send a failed task result (`NoneType does not have id attribute`).
    >
    > Fix contributed by Sam Cooke.

-   Tasks can now raise `~celery.exceptions.Ignore`{.interpreted-text
    role="exc"} to skip updating states or events after return.

    > Example:
    >
    > ``` python
    > from celery.exceptions import Ignore
    >
    > @task
    > def custom_revokes():
    >     if redis.sismember('tasks.revoked', custom_revokes.request.id):
    >         raise Ignore()
    > ```

-   The worker now makes sure the request/task stacks aren\'t modified
    by the initial `Task.__call__`.

    > This would previously be a problem if a custom task class defined
    > `__call__` and also called `super()`.

-   Because of problems the fast local optimization has been disabled,
    and can only be enabled by setting the
    `USE_FAST_LOCALS`{.interpreted-text role="envvar"} attribute.

-   Worker: Now sets a default socket timeout of 5 seconds at shutdown
    so that broken socket reads don\'t hinder proper shutdown (Issue
    #975).

-   More fixes related to late eventlet/gevent patching.

-   Documentation for settings out of sync with reality:

    > -   `CELERY_TASK_PUBLISH_RETRY`{.interpreted-text role="setting"}
    >
    >     > Documented as disabled by default, but it was enabled by
    >     > default since 2.5 as stated by the 2.5 changelog.
    >
    > -   `CELERY_TASK_PUBLISH_RETRY_POLICY`{.interpreted-text
    >     role="setting"}
    >
    >     > The default max_retries had been set to 100, but documented
    >     > as being 3, and the interval_max was set to 1 but documented
    >     > as 0.2. The default setting are now set to 3 and 0.2 as it
    >     > was originally documented.
    >
    > Fix contributed by Matt Long.

-   Worker: Log messages when connection established and lost have been
    improved.

-   The repr of a Crontab schedule value of \'0\' should be \'\*\'
    (Issue #972).

-   Revoked tasks are now removed from reserved/active state in the
    worker (Issue #969)

    > Fix contributed by Alexey Zatelepin.

-   gevent: Now supports hard time limits using `gevent.Timeout`.

-   Documentation: Links to init-scripts now point to the 3.0 branch
    instead of the development branch (master).

-   Documentation: Fixed typo in signals user guide (Issue #986).

    > `instance.app.queues` -\> `instance.app.amqp.queues`.

-   Eventlet/gevent: The worker didn\'t properly set the custom app for
    new greenlets.

-   Eventlet/gevent: Fixed a bug where the worker could not recover from
    connection loss (Issue #959).

    > Also, because of a suspected bug in gevent the
    > `BROKER_CONNECTION_TIMEOUT`{.interpreted-text role="setting"}
    > setting has been disabled when using gevent

## 3.0.9

release-date

:   2012-08-31 06:00 p.m. BST

release-by

:   Ask Solem

-   Important note for users of Django and the database scheduler!

    > Recently a timezone issue has been fixed for periodic tasks, but
    > erroneous timezones could have already been stored in the
    > database, so for the fix to work you need to reset the
    > `last_run_at` fields.
    >
    > You can do this by executing the following command:
    >
    > ``` console
    > $ python manage.py shell
    > >>> from djcelery.models import PeriodicTask
    > >>> PeriodicTask.objects.update(last_run_at=None)
    > ```
    >
    > You also have to do this if you change the timezone or
    > `CELERY_ENABLE_UTC`{.interpreted-text role="setting"} setting.

-   Note about the `CELERY_ENABLE_UTC`{.interpreted-text role="setting"}
    setting.

    > If you previously disabled this just to force periodic tasks to
    > work with your timezone, then you\'re now *encouraged to re-enable
    > it*.

-   Now depends on Kombu 2.4.5 which fixes PyPy + Jython installation.

-   Fixed bug with timezones when `CELERY_ENABLE_UTC`{.interpreted-text
    role="setting"} is disabled (Issue #952).

-   Fixed a typo in the `celerybeat` upgrade mechanism (Issue #951).

-   Make sure the [exc_info]{.title-ref} argument to logging is resolved
    (Issue #899).

-   Fixed problem with Python 3.2 and thread join timeout overflow
    (Issue #796).

-   A test case was occasionally broken for Python 2.5.

-   Unit test suite now passes for PyPy 1.9.

-   App instances now supports the `with`{.interpreted-text
    role="keyword"} statement.

    > This calls the new `@close`{.interpreted-text role="meth"} method
    > at exit, which cleans up after the app like closing pool
    > connections.
    >
    > Note that this is only necessary when dynamically creating apps,
    > for example \"temporary\" apps.

-   Support for piping a subtask to a chain.

    > For example:
    >
    > ``` python
    > pipe = sometask.s() | othertask.s()
    > new_pipe = mytask.s() | pipe
    > ```
    >
    > Contributed by Steve Morin.

-   Fixed problem with group results on non-pickle serializers.

    > Fix contributed by Steeve Morin.

## 3.0.8 {#version-3.0.8}

release-date

:   2012-08-29 05:00 p.m. BST

release-by

:   Ask Solem

-   Now depends on Kombu 2.4.4

-   Fixed problem with `amqplib`{.interpreted-text role="pypi"} and
    receiving larger message payloads (Issue #922).

    > The problem would manifest itself as either the worker hanging, or
    > occasionally a `Framing error` exception appearing.
    >
    > Users of the new `pyamqp://` transport must upgrade to
    > `amqp`{.interpreted-text role="pypi"} 0.9.3.

-   Beat: Fixed another timezone bug with interval and Crontab schedules
    (Issue #943).

-   Beat: The schedule file is now automatically cleared if the timezone
    is changed.

    > The schedule is also cleared when you upgrade to 3.0.8 from an
    > earlier version, this to register the initial timezone info.

-   Events: The `worker-heartbeat`{.interpreted-text role="event"} event
    now include processed and active count fields.

    > Contributed by Mher Movsisyan.

-   Fixed error with error email and new task classes (Issue #931).

-   `BaseTask.__call__` is no longer optimized away if it has been
    monkey patched.

-   Fixed shutdown issue when using gevent (Issue #911 & Issue #936).

    > Fix contributed by Thomas Meson.

## 3.0.7 {#version-3.0.7}

release-date

:   2012-08-24 05:00 p.m. BST

release-by

:   Ask Solem

-   Fixes several problems with periodic tasks and timezones (Issue
    #937).

-   Now depends on kombu 2.4.2

    > -   Redis: Fixes a race condition crash
    > -   Fixes an infinite loop that could happen when retrying
    >     establishing the broker connection.

-   Daemons now redirect standard file descriptors to
    `/dev/null`{.interpreted-text role="file"}

    > Though by default the standard outs are also redirected to the
    > logger instead, but you can disable this by changing the
    > `CELERY_REDIRECT_STDOUTS`{.interpreted-text role="setting"}
    > setting.

-   Fixes possible problems when eventlet/gevent is patched too late.

-   `LoggingProxy` no longer defines `fileno()` (Issue #928).

-   Results are now ignored for the chord unlock task.

    > Fix contributed by Steeve Morin.

-   Cassandra backend now works if result expiry is disabled.

    > Fix contributed by Steeve Morin.

-   The traceback object is now passed to signal handlers instead of the
    string representation.

    > Fix contributed by Adam DePue.

-   Celery command: Extensions are now sorted by name.

-   A regression caused the `task-failed`{.interpreted-text
    role="event"} event to be sent with the exception object instead of
    its string representation.

-   The worker daemon would try to create the pid file before
    daemonizing to catch errors, but this file wasn\'t immediately
    released (Issue #923).

-   Fixes Jython compatibility.

-   `billiard.forking_enable` was called by all pools not just the
    processes pool, which would result in a useless warning if the
    billiard C extensions weren\'t installed.

## 3.0.6 {#version-3.0.6}

release-date

:   2012-08-17 11:00 p.mp.m. Ask Solem

-   Now depends on kombu 2.4.0

-   Now depends on billiard 2.7.3.12

-   Redis: Celery now tries to restore messages whenever there are no
    messages in the queue.

-   Crontab schedules now properly respects
    `CELERY_TIMEZONE`{.interpreted-text role="setting"} setting.

    > It\'s important to note that Crontab schedules uses UTC time by
    > default unless this setting is set.
    >
    > Issue #904 and `django-celery`{.interpreted-text role="pypi"}
    > #150.

-   `billiard.enable_forking` is now only set by the processes pool.

-   The transport is now properly shown by
    `celery report`{.interpreted-text role="program"} (Issue #913).

-   The [\--app]{.title-ref} argument now works if the last part is a
    module name (Issue #921).

-   Fixed problem with unpickleable exceptions (billiard #12).

-   Adds `task_name` attribute to `EagerResult` which is always
    `None`{.interpreted-text role="const"} (Issue #907).

-   Old Task class in `celery.task`{.interpreted-text role="mod"} no
    longer accepts magic kwargs by default (Issue #918).

    > A regression long ago disabled magic kwargs for these, and since
    > no one has complained about it we don\'t have any incentive to fix
    > it now.

-   The `inspect reserved` control command didn\'t work properly.

-   Should now play better with tools for static analysis by explicitly
    specifying dynamically created attributes in the
    `celery`{.interpreted-text role="mod"} and
    `celery.task`{.interpreted-text role="mod"} modules.

-   Terminating a task now results in
    `~celery.exceptions.RevokedTaskError`{.interpreted-text role="exc"}
    instead of a `WorkerLostError`.

-   `AsyncResult.revoke` now accepts `terminate` and `signal` arguments.

-   The `task-revoked`{.interpreted-text role="event"} event now
    includes new fields: `terminated`, `signum`, and `expired`.

-   The argument to
    `~celery.exceptions.TaskRevokedError`{.interpreted-text
    role="class"} is now one of the reasons `revoked`, `expired` or
    `terminated`.

-   Old Task class does no longer use `classmethod`{.interpreted-text
    role="class"} for `push_request` and `pop_request` (Issue #912).

-   `GroupResult` now supports the `children` attribute (Issue #916).

-   `AsyncResult.collect` now respects the `intermediate` argument
    (Issue #917).

-   Fixes example task in documentation (Issue #902).

-   Eventlet fixed so that the environment is patched as soon as
    possible.

-   eventlet: Now warns if Celery related modules that depends on
    threads are imported before eventlet is patched.

-   Improved event and camera examples in the monitoring guide.

-   Disables celery command setuptools entry-points if the command
    can\'t be loaded.

-   Fixed broken `dump_request` example in the tasks guide.

## 3.0.5 {#version-3.0.5}

release-date

:   2012-08-01 04:00 p.m. BST

release-by

:   Ask Solem

-   Now depends on kombu 2.3.1 + billiard 2.7.3.11

-   Fixed a bug with the -B option (`cannot pickle thread.lock objects`)
    (Issue #894 + Issue #892, + `django-celery`{.interpreted-text
    role="pypi"} #154).

-   The `restart_pool`{.interpreted-text role="control"} control command
    now requires the `CELERYD_POOL_RESTARTS`{.interpreted-text
    role="setting"} setting to be enabled

    > This change was necessary as the multiprocessing event that the
    > restart command depends on is responsible for creating many
    > semaphores/file descriptors, resulting in problems in some
    > environments.

-   `chain.apply` now passes args to the first task (Issue #889).

-   Documented previously secret options to the
    `django-celery`{.interpreted-text role="pypi"} monitor in the
    monitoring user guide (Issue #396).

-   Old changelog are now organized in separate documents for each
    series, see `history`{.interpreted-text role="ref"}.

## 3.0.4 {#version-3.0.4}

release-date

:   2012-07-26 07:00 p.m. BST

release-by

:   Ask Solem

-   Now depends on Kombu 2.3

-   New experimental standalone Celery monitor: Flower

    > See `monitoring-flower`{.interpreted-text role="ref"} to read more
    > about it!
    >
    > Contributed by Mher Movsisyan.

-   Now supports AMQP heartbeats if using the new `pyamqp://` transport.

    > -   The `amqp`{.interpreted-text role="pypi"} transport requires
    >     the `amqp`{.interpreted-text role="pypi"} library to be
    >     installed:
    >
    >     > ``` console
    >     > $ pip install amqp
    >     > ```
    >
    > -   Then you need to set the transport URL prefix to `pyamqp://`.
    >
    > -   The default heartbeat value is 10 seconds, but this can be
    >     changed using the `BROKER_HEARTBEAT`{.interpreted-text
    >     role="setting"} setting:
    >
    >         BROKER_HEARTBEAT = 5.0
    >
    > -   If the broker heartbeat is set to 10 seconds, the heartbeats
    >     will be monitored every 5 seconds (double the heartbeat rate).
    >
    > See the
    > `Kombu 2.3 changelog <kombu:version-2.3.0>`{.interpreted-text
    > role="ref"} for more information.

-   Now supports RabbitMQ Consumer Cancel Notifications, using the
    `pyamqp://` transport.

    > This is essential when running RabbitMQ in a cluster.
    >
    > See the
    > `Kombu 2.3 changelog <kombu:version-2.3.0>`{.interpreted-text
    > role="ref"} for more information.

-   Delivery info is no longer passed directly through.

    > It was discovered that the SQS transport adds objects that can\'t
    > be pickled to the delivery info mapping, so we had to go back to
    > using the white-list again.
    >
    > Fixing this bug also means that the SQS transport is now working
    > again.

-   The semaphore wasn\'t properly released when a task was revoked
    (Issue #877).

    > This could lead to tasks being swallowed and not released until a
    > worker restart.
    >
    > Thanks to Hynek Schlawack for debugging the issue.

-   Retrying a task now also forwards any linked tasks.

    > This means that if a task is part of a chain (or linked in some
    > other way) and that even if the task is retried, then the next
    > task in the chain will be executed when the retry succeeds.

-   Chords: Now supports setting the interval and other keyword
    arguments to the chord unlock task.

    > -   The interval can now be set as part of the chord subtasks
    >     kwargs:
    >
    >         chord(header)(body, interval=10.0)
    >
    > -   In addition the chord unlock task now honors the
    >     Task.default_retry_delay option, used when none is specified,
    >     which also means that the default interval can also be changed
    >     using annotations:
    >
    >     > ``` python
    >     > CELERY_ANNOTATIONS = {
    >     >     'celery.chord_unlock': {
    >     >         'default_retry_delay': 10.0,
    >     >     }
    >     > }
    >     > ```

-   New `@add_defaults`{.interpreted-text role="meth"} method can add
    new default configuration dictionaries to the applications
    configuration.

    > For example:
    >
    >     config = {'FOO': 10}
    >
    >     app.add_defaults(config)
    >
    > is the same as `app.conf.update(config)` except that data won\'t
    > be copied, and that it won\'t be pickled when the worker spawns
    > child processes.
    >
    > In addition the method accepts a callable:
    >
    >     def initialize_config():
    >         # insert heavy stuff that can't be done at import time here.
    >
    >     app.add_defaults(initialize_config)
    >
    > which means the same as the above except that it won\'t happen
    > until the Celery configuration is actually used.
    >
    > As an example, Celery can lazily use the configuration of a Flask
    > app:
    >
    >     flask_app = Flask()
    >     app = Celery()
    >     app.add_defaults(lambda: flask_app.config)

-   Revoked tasks weren\'t marked as revoked in the result backend
    (Issue #871).

    > Fix contributed by Hynek Schlawack.

-   Event-loop now properly handles the case when the
    `epoll`{.interpreted-text role="manpage"} poller object has been
    closed (Issue #882).

-   Fixed syntax error in `funtests/test_leak.py`

    > Fix contributed by Catalin Iacob.

-   group/chunks: Now accepts empty task list (Issue #873).

-   New method names:

    > -   `Celery.default_connection()` ➠
    >     `~@connection_or_acquire`{.interpreted-text role="meth"}.
    > -   `Celery.default_producer()` ➠
    >     `~@producer_or_acquire`{.interpreted-text role="meth"}.
    >
    > The old names still work for backward compatibility.

## 3.0.3 {#version-3.0.3}

release-date

:   2012-07-20 09:17 p.m. BST

release-by

:   Ask Solem

-   `amqplib`{.interpreted-text role="pypi"} passes the channel object
    as part of the delivery_info and it\'s not pickleable, so we now
    remove it.

## 3.0.2 {#version-3.0.2}

release-date

:   2012-07-20 04:00 p.m. BST

release-by

:   Ask Solem

-   

    A bug caused the following task options to not take defaults from the

    :   configuration (Issue #867 + Issue #858)

        > The following settings were affected:
        >
        > -   `CELERY_IGNORE_RESULT`{.interpreted-text role="setting"}
        > -   `CELERYD_SEND_TASK_ERROR_EMAILS`{.interpreted-text
        >     role="setting"}
        > -   `CELERY_TRACK_STARTED`{.interpreted-text role="setting"}
        > -   `CElERY_STORE_ERRORS_EVEN_IF_IGNORED`{.interpreted-text
        >     role="setting"}
        >
        > Fix contributed by John Watson.

-   Task Request: `delivery_info` is now passed through as-is (Issue
    #807).

-   The ETA argument now supports datetime\'s with a timezone set (Issue
    #855).

-   The worker\'s banner displayed the autoscale settings in the wrong
    order (Issue #859).

-   Extension commands are now loaded after concurrency is set up so
    that they don\'t interfere with things like eventlet patching.

-   Fixed bug in the threaded pool (Issue #863)

-   The task failure handler mixed up the fields in
    `sys.exc_info`{.interpreted-text role="func"}.

    > Fix contributed by Rinat Shigapov.

-   Fixed typos and wording in the docs.

    > Fix contributed by Paul McMillan

-   New setting: `CELERY_WORKER_DIRECT`{.interpreted-text
    role="setting"}

    > If enabled each worker will consume from their own dedicated queue
    > which can be used to route tasks to specific workers.

-   Fixed several edge case bugs in the add consumer remote control
    command.

-   `~celery.contrib.migrate`{.interpreted-text role="mod"}: Can now
    filter and move tasks to specific workers if
    `CELERY_WORKER_DIRECT`{.interpreted-text role="setting"} is enabled.

    > Among other improvements, the following functions have been added:
    >
    > > -   `move_direct(filterfun, **opts)`
    > > -   `move_direct_by_id(task_id, worker_hostname, **opts)`
    > > -   `move_direct_by_idmap({task_id: worker_hostname, ...}, **opts)`
    > > -   `move_direct_by_taskmap({task_name: worker_hostname, ...}, **opts)`

-   `~celery.Celery.default_connection`{.interpreted-text role="meth"}
    now accepts a pool argument that if set to false causes a new
    connection to be created instead of acquiring one from the pool.

-   New signal: `celeryd_after_setup`{.interpreted-text role="signal"}.

-   Default loader now keeps lowercase attributes from the configuration
    module.

## 3.0.1 {#version-3.0.1}

release-date

:   2012-07-10 06:00 p.m. BST

release-by

:   Ask Solem

-   Now depends on kombu 2.2.5

-   inspect now supports limit argument:

        myapp.control.inspect(limit=1).ping()

-   Beat: now works with timezone aware datetime\'s.

-   Task classes inheriting `from celery import Task` mistakenly enabled
    `accept_magic_kwargs`.

-   Fixed bug in `inspect scheduled` (Issue #829).

-   Beat: Now resets the schedule to upgrade to UTC.

-   The `celery worker`{.interpreted-text role="program"} command now
    works with eventlet/gevent.

    > Previously it wouldn\'t patch the environment early enough.

-   The `celery`{.interpreted-text role="program"} command now supports
    extension commands using setuptools entry-points.

    > Libraries can add additional commands to the
    > `celery`{.interpreted-text role="program"} command by adding an
    > entry-point like:
    >
    >     setup(
    >         entry_points=[
    >             'celery.commands': [
    >                 'foo = my.module:Command',
    >         ],
    >     ],
    >     ...)
    >
    > The command must then support the interface of
    > `celery.bin.base.Command`{.interpreted-text role="class"}.

-   contrib.migrate: New utilities to move tasks from one queue to
    another.

    > -   `~celery.contrib.migrate.move_tasks`{.interpreted-text
    >     role="func"}
    > -   `~celery.contrib.migrate.move_task_by_id`{.interpreted-text
    >     role="func"}

-   The `task-sent`{.interpreted-text role="event"} event now contains
    `exchange` and `routing_key` fields.

-   Fixes bug with installing on Python 3.

    > Fix contributed by Jed Smith.

## 3.0.0 (Chiastic Slide) {#version-3.0.0}

release-date

:   2012-07-07 01:30 p.m. BST

release-by

:   Ask Solem

See `whatsnew-3.0`{.interpreted-text role="ref"}.
