# Change history for Celery 2.4 {#changelog-2.4}

::: {.contents local=""}
:::

## 2.4.5 {#version-2.4.5}

release-date

:   2011-12-02 05:00 p.m. GMT

release-by

:   Ask Solem

-   Periodic task interval schedules were accidentally rounded down,
    resulting in some periodic tasks being executed early.

-   Logging of humanized times in the beat log is now more detailed.

-   New `brokers`{.interpreted-text role="ref"} section in the Getting
    Started part of the Documentation

    > This replaces the old \"Other queues\" tutorial, and adds
    > documentation for MongoDB, Beanstalk and CouchDB.

## 2.4.4 {#version-2.4.4}

release-date

:   2011-11-25 04:00 p.m. GMT

release-by

:   Ask Solem

### Security Fixes {#v244-security-fixes}

-   \[Security:
    [CELERYSA-0001](https://github.com/celery/celery/tree/master/docs/sec/CELERYSA-0001.txt)\]
    Daemons would set effective id\'s rather than real id\'s when the
    `!--uid`{.interpreted-text role="option"}/
    `!--gid`{.interpreted-text role="option"} arguments to
    `celery multi`{.interpreted-text role="program"},
    `celeryd_detach`{.interpreted-text role="program"},
    `celery beat`{.interpreted-text role="program"} and
    `celery events`{.interpreted-text role="program"} were used.

    This means privileges weren\'t properly dropped, and that it would
    be possible to regain supervisor privileges later.

### Fixes {#v244-fixes}

-   Processes pool: Fixed rare deadlock at shutdown (Issue #523).

    > Fix contributed by Ionel Maries Christian.

-   Webhook tasks issued the wrong HTTP POST headers (Issue #515).

    > The *Content-Type* header has been changed from `application/json`
    > ⇒ `application/x-www-form-urlencoded`, and adds a proper
    > *Content-Length* header.
    >
    > Fix contributed by Mitar.

-   Daemonization tutorial: Adds a configuration example using Django
    and virtualenv together (Issue #505).

    > Contributed by Juan Ignacio Catalano.

-   generic init-scripts now automatically creates log and pid file
    directories (Issue #545).

    > Contributed by Chris Streeter.

## 2.4.3 {#version-2.4.3}

release-date

:   2011-11-22 06:00 p.m. GMT

release-by

:   Ask Solem

-   Fixes module import typo in [celeryctl]{.title-ref} (Issue #538).

    > Fix contributed by Chris Streeter.

## 2.4.2 {#version-2.4.2}

release-date

:   2011-11-14 12:00 p.m. GMT

release-by

:   Ask Solem

-   Program module no longer uses relative imports so that it\'s
    possible to do `python -m celery.bin.name`.

## 2.4.1 {#version-2.4.1}

release-date

:   2011-11-07 06:00 p.m. GMT

release-by

:   Ask Solem

-   `celeryctl inspect` commands was missing output.
-   processes pool: Decrease polling interval for less idle CPU usage.
-   processes pool: MaybeEncodingError wasn\'t wrapped in ExceptionInfo
    (Issue #524).
-   worker: would silence errors occurring after task consumer started.
-   logging: Fixed a bug where unicode in stdout redirected log messages
    couldn\'t be written (Issue #522).

## 2.4.0 {#version-2.4.0}

release-date

:   2011-11-04 04:00 p.m. GMT

release-by

:   Ask Solem

### Important Notes {#v240-important}

-   Now supports Python 3.

-   Fixed deadlock in worker process handling (Issue #496).

    > A deadlock could occur after spawning new child processes because
    > the logging library\'s mutex wasn\'t properly reset after fork.
    >
    > The symptoms of this bug affecting would be that the worker simply
    > stops processing tasks, as none of the workers child processes are
    > functioning. There was a greater chance of this bug occurring with
    > `maxtasksperchild` or a time-limit enabled.
    >
    > This is a workaround for
    > <http://bugs.python.org/issue6721#msg140215>.
    >
    > Be aware that while this fixes the logging library lock, there
    > could still be other locks initialized in the parent process,
    > introduced by custom code.
    >
    > Fix contributed by Harm Verhagen.

-   AMQP Result backend: Now expires results by default.

    > The default expiration value is now taken from the
    > `CELERY_TASK_RESULT_EXPIRES`{.interpreted-text role="setting"}
    > setting.
    >
    > The old `CELERY_AMQP_TASK_RESULT_EXPIRES`{.interpreted-text
    > role="setting"} setting has been deprecated and will be removed in
    > version 4.0.
    >
    > Note that this means that the result backend requires RabbitMQ
    > 2.1.0 or higher, and that you have to disable expiration if
    > you\'re running with an older version. You can do so by disabling
    > the `CELERY_TASK_RESULT_EXPIRES`{.interpreted-text role="setting"}
    > setting:
    >
    >     CELERY_TASK_RESULT_EXPIRES = None

-   Eventlet: Fixed problem with shutdown (Issue #457).

-   Broker transports can be now be specified using URLs

    > The broker can now be specified as a URL instead. This URL must
    > have the format:
    >
    > ``` text
    > transport://user:password@hostname:port/virtual_host
    > ```
    >
    > for example the default broker is written as:
    >
    > ``` text
    > amqp://guest:guest@localhost:5672//
    > ```
    >
    > The scheme is required, so that the host is identified as a URL
    > and not just a host name. User, password, port and virtual_host
    > are optional and defaults to the particular transports default
    > value.
    >
    > ::: note
    > ::: title
    > Note
    > :::
    >
    > Note that the path component (virtual_host) always starts with a
    > forward-slash. This is necessary to distinguish between the
    > virtual host `''` (empty) and `'/'`, which are both acceptable
    > virtual host names.
    >
    > A virtual host of `'/'` becomes:
    >
    > ``` text
    > amqp://guest:guest@localhost:5672//
    > ```
    >
    > and a virtual host of `''` (empty) becomes:
    >
    > ``` text
    > amqp://guest:guest@localhost:5672/
    > ```
    >
    > So the leading slash in the path component is **always required**.
    > :::
    >
    > In addition the `BROKER_URL`{.interpreted-text role="setting"}
    > setting has been added as an alias to `BROKER_HOST`. Any broker
    > setting specified in both the URL and in the configuration will be
    > ignored, if a setting isn\'t provided in the URL then the value
    > from the configuration will be used as default.
    >
    > Also, programs now support the
    > `--broker <celery --broker>`{.interpreted-text role="option"}
    > option to specify a broker URL on the command-line:
    >
    > ``` console
    > $ celery worker -b redis://localhost
    >
    > $ celery inspect -b amqp://guest:guest@localhost//e
    > ```
    >
    > The environment variable `CELERY_BROKER_URL`{.interpreted-text
    > role="envvar"} can also be used to easily override the default
    > broker used.

-   The deprecated `celery.loaders.setup_loader`{.interpreted-text
    role="func"} function has been removed.

-   The `CELERY_TASK_ERROR_WHITELIST`{.interpreted-text role="setting"}
    setting has been replaced by a more flexible approach (Issue #447).

    > The error mail sending logic is now available as `Task.ErrorMail`,
    > with the implementation (for reference) in
    > `celery.utils.mail`{.interpreted-text role="mod"}.
    >
    > The error mail class can be sub-classed to gain complete control
    > of when error messages are sent, thus removing the need for a
    > separate white-list setting.
    >
    > The `CELERY_TASK_ERROR_WHITELIST`{.interpreted-text
    > role="setting"} setting has been deprecated, and will be removed
    > completely in version 4.0.

-   Additional Deprecations

    > The following functions has been deprecated and is scheduled for
    > removal in version 4.0:
    >
    >   **Old function**                              **Alternative**
    >   --------------------------------------------- -----------------------------------------
    >   [celery.loaders.current_loader]{.title-ref}   [celery.current_app.loader]{.title-ref}
    >   [celery.loaders.load_settings]{.title-ref}    [celery.current_app.conf]{.title-ref}
    >   [celery.execute.apply]{.title-ref}            [Task.apply]{.title-ref}
    >   [celery.execute.apply_async]{.title-ref}      [Task.apply_async]{.title-ref}
    >   [celery.execute.delay_task]{.title-ref}       [celery.execute.send_task]{.title-ref}
    >
    > The following settings has been deprecated and is scheduled for
    > removal in version 4.0:
    >
    >   **Old setting**                      **Alternative**
    >   ------------------------------------ -----------------------------
    >   [CELERYD_LOG_LEVEL]{.title-ref}      `celery worker --loglevel=`
    >   [CELERYD_LOG_FILE]{.title-ref}       `celery worker --logfile=`
    >   [CELERYBEAT_LOG_LEVEL]{.title-ref}   `celery beat --loglevel=`
    >   [CELERYBEAT_LOG_FILE]{.title-ref}    `celery beat --logfile=`
    >   [CELERYMON_LOG_LEVEL]{.title-ref}    `celerymon --loglevel=`
    >   [CELERYMON_LOG_FILE]{.title-ref}     `celerymon --logfile=`

### News {#v240-news}

-   No longer depends on `pyparsing`{.interpreted-text role="pypi"}.

-   Now depends on Kombu 1.4.3.

-   CELERY_IMPORTS can now be a scalar value (Issue #485).

    > It\'s too easy to forget to add the comma after the sole element
    > of a tuple, and this is something that often affects newcomers.
    >
    > The docs should probably use a list in examples, as using a tuple
    > for this doesn\'t even make sense. Nonetheless, there are many
    > tutorials out there using a tuple, and this change should be a
    > help to new users.
    >
    > Suggested by `jsaxon-cars`{.interpreted-text role="github_user"}.

-   Fixed a memory leak when using the thread pool (Issue #486).

    > Contributed by Kornelijus Survila.

-   The `statedb` wasn\'t saved at exit.

    > This has now been fixed and it should again remember previously
    > revoked tasks when a `--statedb` is enabled.

-   Adds `EMAIL_USE_TLS`{.interpreted-text role="setting"} to enable
    secure SMTP connections (Issue #418).

    > Contributed by Stefan Kjartansson.

-   Now handles missing fields in task messages as documented in the
    message format documentation.

    > -   Missing required field throws
    >     `~@InvalidTaskError`{.interpreted-text role="exc"}
    > -   Missing args/kwargs is assumed empty.
    >
    > Contributed by Chris Chamberlin.

-   Fixed race condition in `celery.events.state`{.interpreted-text
    role="mod"} (`celerymon`/`celeryev`) where task info would be
    removed while iterating over it (Issue #501).

-   The Cache, Cassandra, MongoDB, Redis and Tyrant backends now
    respects the `CELERY_RESULT_SERIALIZER`{.interpreted-text
    role="setting"} setting (Issue #435).

    > This means that only the database (Django/SQLAlchemy) backends
    > currently doesn\'t support using custom serializers.
    >
    > Contributed by Steeve Morin

-   Logging calls no longer manually formats messages, but delegates
    that to the logging system, so tools like Sentry can easier work
    with the messages (Issue #445).

    > Contributed by Chris Adams.

-   `multi` now supports a `stop_verify` command to wait for processes
    to shutdown.

-   Cache backend didn\'t work if the cache key was unicode (Issue
    #504).

    > Fix contributed by Neil Chintomby.

-   New setting
    `CELERY_RESULT_DB_SHORT_LIVED_SESSIONS`{.interpreted-text
    role="setting"} added, which if enabled will disable the caching of
    SQLAlchemy sessions (Issue #449).

    > Contributed by Leo Dirac.

-   All result backends now implements `__reduce__` so that they can be
    pickled (Issue #441).

    > Fix contributed by Remy Noel

-   multi didn\'t work on Windows (Issue #472).

-   New-style `CELERY_REDIS_*` settings now takes precedence over the
    old `REDIS_*` configuration keys (Issue #508).

    > Fix contributed by Joshua Ginsberg

-   Generic beat init-script no longer sets [bash -e]{.title-ref} (Issue
    #510).

    > Fix contributed by Roger Hu.

-   Documented that Chords don\'t work well with
    `redis-server`{.interpreted-text role="command"} versions before
    2.2.

    > Contributed by Dan McGee.

-   The `CELERYBEAT_MAX_LOOP_INTERVAL`{.interpreted-text role="setting"}
    setting wasn\'t respected.

-   `inspect.registered_tasks` renamed to `inspect.registered` for
    naming consistency.

    > The previous name is still available as an alias.
    >
    > Contributed by Mher Movsisyan

-   Worker logged the string representation of args and kwargs without
    safe guards (Issue #480).

-   RHEL init-script: Changed worker start-up priority.

    > The default start / stop priorities for MySQL on RHEL are:
    >
    > ``` console
    > # chkconfig: - 64 36
    > ```
    >
    > Therefore, if Celery is using a database as a broker / message
    > store, it should be started after the database is up and running,
    > otherwise errors will ensue. This commit changes the priority in
    > the init-script to:
    >
    > ``` console
    > # chkconfig: - 85 15
    > ```
    >
    > which are the default recommended settings for 3-rd party
    > applications and assure that Celery will be started after the
    > database service & shut down before it terminates.
    >
    > Contributed by Yury V. Zaytsev.

-   KeyValueStoreBackend.get_many didn\'t respect the `timeout` argument
    (Issue #512).

-   beat/events\'s `--workdir` option didn\'t
    `chdir(2)`{.interpreted-text role="manpage"} before after
    configuration was attempted (Issue #506).

-   After deprecating 2.4 support we can now name modules correctly,
    since we can take use of absolute imports.

    > Therefore the following internal modules have been renamed:
    >
    > > `celery.concurrency.evlet` -\> `celery.concurrency.eventlet`
    > > `celery.concurrency.evg` -\> `celery.concurrency.gevent`

-   `AUTHORS`{.interpreted-text role="file"} file is now sorted
    alphabetically.

    > Also, as you may have noticed the contributors of new
    > features/fixes are now mentioned in the Changelog.
