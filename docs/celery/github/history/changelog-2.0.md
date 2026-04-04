# Change history for Celery 2.0 {#changelog-2.0}

::: {.contents local=""}
:::

## 2.0.3 {#version-2.0.3}

release-date

:   2010-08-27 12:00 p.m. CEST

release-by

:   Ask Solem

### Fixes {#v203-fixes}

-   Worker: Properly handle connection errors happening while closing
    consumers.

-   Worker: Events are now buffered if the connection is down, then sent
    when the connection is re-established.

-   No longer depends on the `mailer`{.interpreted-text role="pypi"}
    package.

    > This package had a name space collision with
    > [django-mailer]{.title-ref}, so its functionality was replaced.

-   Redis result backend: Documentation typos: Redis doesn\'t have
    database names, but database numbers. The default database is now 0.

-   `~celery.task.control.inspect`{.interpreted-text role="class"}:
    [registered_tasks]{.title-ref} was requesting an invalid command
    because of a typo.

    > See issue #170.

-   `CELERY_ROUTES`{.interpreted-text role="setting"}: Values defined in
    the route should now have precedence over values defined in
    `CELERY_QUEUES`{.interpreted-text role="setting"} when merging the
    two.

    > With the follow settings:
    >
    > ``` python
    > CELERY_QUEUES = {'cpubound': {'exchange': 'cpubound',
    >                               'routing_key': 'cpubound'}}
    >
    > CELERY_ROUTES = {'tasks.add': {'queue': 'cpubound',
    >                                'routing_key': 'tasks.add',
    >                                'serializer': 'json'}}
    > ```
    >
    > The final routing options for [tasks.add]{.title-ref} will become:
    >
    > ``` python
    > {'exchange': 'cpubound',
    >  'routing_key': 'tasks.add',
    >  'serializer': 'json'}
    > ```
    >
    > This wasn\'t the case before: the values in
    > `CELERY_QUEUES`{.interpreted-text role="setting"} would take
    > precedence.

-   Worker crashed if the value of
    `CELERY_TASK_ERROR_WHITELIST`{.interpreted-text role="setting"} was
    not an iterable

-   `~celery.execute.apply`{.interpreted-text role="func"}: Make sure
    [kwargs\[\'task_id\'\]]{.title-ref} is always set.

-   \`AsyncResult.traceback\`: Now returns `None`{.interpreted-text
    role="const"}, instead of raising `KeyError`{.interpreted-text
    role="exc"} if traceback is missing.

-   `~celery.task.control.inspect`{.interpreted-text role="class"}:
    Replies didn\'t work correctly if no destination was specified.

-   Can now store result/meta-data for custom states.

-   Worker: A warning is now emitted if the sending of task error emails
    fails.

-   `celeryev`: Curses monitor no longer crashes if the terminal window
    is resized.

    > See issue #160.

-   Worker: On macOS it isn\'t possible to run [os.exec\*]{.title-ref}
    in a process that\'s threaded.

    > This breaks the SIGHUP restart handler, and is now disabled on
    > macOS, emitting a warning instead.
    >
    > See issue #152.

-   `celery.execute.trace`{.interpreted-text role="mod"}: Properly
    handle [raise(str)]{.title-ref}, which is still allowed in Python
    2.4.

    > See issue #175.

-   Using urllib2 in a periodic task on macOS crashed because of the
    proxy auto detection used in macOS.

    > This is now fixed by using a workaround. See issue #143.

-   Debian init-scripts: Commands shouldn\'t run in a sub shell

    > See issue #163.

-   Debian init-scripts: Use the absolute path of `celeryd` program to
    allow stat

    > See issue #162.

### Documentation {#v203-documentation}

-   getting-started/broker-installation: Fixed typo

    > [set_permissions \"\"]{.title-ref} -\> [set_permissions
    > \".\*\"]{.title-ref}.

-   Tasks User Guide: Added section on database transactions.

    > See issue #169.

-   Routing User Guide: Fixed typo [\"feed\": -\> {\"queue\":
    \"feeds\"}]{.title-ref}.

    > See issue #169.

-   Documented the default values for the
    `CELERYD_CONCURRENCY`{.interpreted-text role="setting"} and
    `CELERYD_PREFETCH_MULTIPLIER`{.interpreted-text role="setting"}
    settings.

-   Tasks User Guide: Fixed typos in the subtask example

-   celery.signals: Documented worker_process_init.

-   Daemonization cookbook: Need to export DJANGO_SETTINGS_MODULE in
    [/etc/default/celeryd]{.title-ref}.

-   Added some more FAQs from stack overflow

-   Daemonization cookbook: Fixed typo
    [CELERYD_LOGFILE/CELERYD_PIDFILE]{.title-ref}

    > to [CELERYD_LOG_FILE]{.title-ref} / [CELERYD_PID_FILE]{.title-ref}
    >
    > Also added troubleshooting section for the init-scripts.

## 2.0.2 {#version-2.0.2}

release-date

:   2010-07-22 11:31 a.m. CEST

release-by

:   Ask Solem

-   Routes: When using the dict route syntax, the exchange for a task
    could disappear making the task unroutable.

    > See issue #158.

-   Test suite now passing on Python 2.4

-   No longer have to type [PYTHONPATH=.]{.title-ref} to use
    `celeryconfig` in the current directory.

    > This is accomplished by the default loader ensuring that the
    > current directory is in [sys.path]{.title-ref} when loading the
    > config module. [sys.path]{.title-ref} is reset to its original
    > state after loading.
    >
    > Adding the current working directory to [sys.path]{.title-ref}
    > without the user knowing may be a security issue, as this means
    > someone can drop a Python module in the users directory that
    > executes arbitrary commands. This was the original reason not to
    > do this, but if done *only when loading the config module*, this
    > means that the behavior will only apply to the modules imported in
    > the config module, which I think is a good compromise (certainly
    > better than just explicitly setting [PYTHONPATH=.]{.title-ref}
    > anyway)

-   Experimental Cassandra backend added.

-   Worker: SIGHUP handler accidentally propagated to worker pool
    processes.

    > In combination with
    > `7a7c44e39344789f11b5346e9cc8340f5fe4846c`{.interpreted-text
    > role="sha"} this would make each child process start a new worker
    > instance when the terminal window was closed :/

-   Worker: Don\'t install SIGHUP handler if running from a terminal.

    > This fixes the problem where the worker is launched in the
    > background when closing the terminal.

-   Worker: Now joins threads at shutdown.

    > See issue #152.

-   Test tear down: Don\'t use [atexit]{.title-ref} but nose\'s
    [teardown()]{.title-ref} functionality instead.

    > See issue #154.

-   Debian worker init-script: Stop now works correctly.

-   Task logger: [warn]{.title-ref} method added (synonym for
    [warning]{.title-ref})

-   Can now define a white list of errors to send error emails for.

    > Example:
    >
    > ``` python
    > CELERY_TASK_ERROR_WHITELIST = ('myapp.MalformedInputError',)
    > ```
    >
    > See issue #153.

-   Worker: Now handles overflow exceptions in [time.mktime]{.title-ref}
    while parsing the ETA field.

-   LoggerWrapper: Try to detect loggers logging back to stderr/stdout
    making an infinite loop.

-   Added `celery.task.control.inspect`{.interpreted-text role="class"}:
    Inspects a running worker.

    > Examples:
    >
    > ``` pycon
    > # Inspect a single worker
    > >>> i = inspect('myworker.example.com')
    >
    > # Inspect several workers
    > >>> i = inspect(['myworker.example.com', 'myworker2.example.com'])
    >
    > # Inspect all workers consuming on this vhost.
    > >>> i = inspect()
    >
    > ### Methods
    >
    > # Get currently executing tasks
    > >>> i.active()
    >
    > # Get currently reserved tasks
    > >>> i.reserved()
    >
    > # Get the current ETA schedule
    > >>> i.scheduled()
    >
    > # Worker statistics and info
    > >>> i.stats()
    >
    > # List of currently revoked tasks
    > >>> i.revoked()
    >
    > # List of registered tasks
    > >>> i.registered_tasks()
    > ```

-   Remote control commands
    [dump_active]{.title-ref}/[dump_reserved]{.title-ref}/[dump_schedule]{.title-ref}
    now replies with detailed task requests.

    > Containing the original arguments and fields of the task
    > requested.
    >
    > In addition the remote control command [set_loglevel]{.title-ref}
    > has been added, this only changes the log level for the main
    > process.

-   Worker control command execution now catches errors and returns
    their string representation in the reply.

-   Functional test suite added

    > `celery.tests.functional.case`{.interpreted-text role="mod"}
    > contains utilities to start and stop an embedded worker process,
    > for use in functional testing.

## 2.0.1 {#version-2.0.1}

release-date

:   2010-07-09 03:02 p.m. CEST

release-by

:   Ask Solem

-   multiprocessing.pool: Now handles encoding errors, so that pickling
    errors doesn\'t crash the worker processes.

-   The remote control command replies wasn\'t working with RabbitMQ
    1.8.0\'s stricter equivalence checks.

    > If you\'ve already hit this problem you may have to delete the
    > declaration:
    >
    > ``` console
    > $ camqadm exchange.delete celerycrq
    > ```
    >
    > or:
    >
    > ``` console
    > $ python manage.py camqadm exchange.delete celerycrq
    > ```

-   A bug sneaked in the ETA scheduler that made it only able to execute
    one task per second(!)

    > The scheduler sleeps between iterations so it doesn\'t consume too
    > much CPU. It keeps a list of the scheduled items sorted by time,
    > at each iteration it sleeps for the remaining time of the item
    > with the nearest deadline. If there are no ETA tasks it will sleep
    > for a minimum amount of time, one second by default.
    >
    > A bug sneaked in here, making it sleep for one second for every
    > task that was scheduled. This has been fixed, so now it should
    > move tasks like hot knife through butter.
    >
    > In addition a new setting has been added to control the minimum
    > sleep interval;
    > `CELERYD_ETA_SCHEDULER_PRECISION`{.interpreted-text
    > role="setting"}. A good value for this would be a float between 0
    > and 1, depending on the needed precision. A value of 0.8 means
    > that when the ETA of a task is met, it will take at most 0.8
    > seconds for the task to be moved to the ready queue.

-   Pool: Supervisor didn\'t release the semaphore.

    > This would lead to a deadlock if all workers terminated
    > prematurely.

-   Added Python version trove classifiers: 2.4, 2.5, 2.6 and 2.7

-   Tests now passing on Python 2.7.

-   Task.\_\_reduce\_\_: Tasks created using the task decorator can now
    be pickled.

-   `setup.py`{.interpreted-text role="file"}: `nose`{.interpreted-text
    role="pypi"} added to [tests_require]{.title-ref}.

-   Pickle should now work with SQLAlchemy 0.5.x

-   New homepage design by Jan Henrik Helmers:
    <http://celeryproject.org>

-   New Sphinx theme by Armin Ronacher: <https://docs.celeryq.dev/>

-   Fixed \"pending_xref\" errors shown in the HTML rendering of the
    documentation. Apparently this was caused by new changes in Sphinx
    1.0b2.

-   Router classes in `CELERY_ROUTES`{.interpreted-text role="setting"}
    are now imported lazily.

    > Importing a router class in a module that also loads the Celery
    > environment would cause a circular dependency. This is solved by
    > importing it when needed after the environment is set up.

-   `CELERY_ROUTES`{.interpreted-text role="setting"} was broken if set
    to a single dict.

    > This example in the docs should now work again:
    >
    > ``` python
    > CELERY_ROUTES = {'feed.tasks.import_feed': 'feeds'}
    > ```

-   [CREATE_MISSING_QUEUES]{.title-ref} wasn\'t honored by apply_async.

-   New remote control command: [stats]{.title-ref}

    > Dumps information about the worker, like pool process ids, and
    > total number of tasks executed by type.
    >
    > Example reply:
    >
    > ``` python
    > [{'worker.local':
    >      'total': {'tasks.sleeptask': 6},
    >      'pool': {'timeouts': [None, None],
    >               'processes': [60376, 60377],
    >               'max-concurrency': 2,
    >               'max-tasks-per-child': None,
    >               'put-guarded-by-semaphore': True}}]
    > ```

-   New remote control command: [dump_active]{.title-ref}

    > Gives a list of tasks currently being executed by the worker. By
    > default arguments are passed through repr in case there are
    > arguments that\'s not JSON encodable. If you know the arguments
    > are JSON safe, you can pass the argument [safe=True]{.title-ref}.
    >
    > Example reply:
    >
    > ``` pycon
    > >>> broadcast('dump_active', arguments={'safe': False}, reply=True)
    > [{'worker.local': [
    >     {'args': '(1,)',
    >      'time_start': 1278580542.6300001,
    >      'name': 'tasks.sleeptask',
    >      'delivery_info': {
    >          'consumer_tag': '30',
    >          'routing_key': 'celery',
    >          'exchange': 'celery'},
    >      'hostname': 'casper.local',
    >      'acknowledged': True,
    >      'kwargs': '{}',
    >      'id': '802e93e9-e470-47ed-b913-06de8510aca2',
    >     }
    > ]}]
    > ```

-   Added experimental support for persistent revokes.

    > Use the [-S\|\--statedb]{.title-ref} argument to the worker to
    > enable it:
    >
    > ``` console
    > $ celeryd --statedb=/var/run/celeryd
    > ```
    >
    > This will use the file: [/var/run/celeryd.db]{.title-ref}, as the
    > [shelve]{.title-ref} module automatically adds the
    > [.db]{.title-ref} suffix.

## 2.0.0 {#version-2.0.0}

release-date

:   2010-07-02 02:30 p.m. CEST

release-by

:   Ask Solem

### Foreword

Celery 2.0 contains backward incompatible changes, the most important
being that the Django dependency has been removed so Celery no longer
supports Django out of the box, but instead as an add-on package called
`django-celery`{.interpreted-text role="pypi"}.

We\'re very sorry for breaking backwards compatibility, but there\'s
also many new and exciting features to make up for the time you lose
upgrading, so be sure to read the `News <v200-news>`{.interpreted-text
role="ref"} section.

Quite a lot of potential users have been upset about the Django
dependency, so maybe this is a chance to get wider adoption by the
Python community as well.

Big thanks to all contributors, testers and users!

### Upgrading for Django-users {#v200-django-upgrade}

Django integration has been moved to a separate package:
`django-celery`{.interpreted-text role="pypi"}.

-   To upgrade you need to install the `django-celery`{.interpreted-text
    role="pypi"} module and change:

    ``` python
    INSTALLED_APPS = 'celery'
    ```

    to:

    ``` python
    INSTALLED_APPS = 'djcelery'
    ```

-   If you use [mod_wsgi]{.title-ref} you need to add the following line
    to your [.wsgi]{.title-ref} file:

    > ``` python
    > import os
    > os.environ['CELERY_LOADER'] = 'django'
    > ```

-   The following modules has been moved to
    `django-celery`{.interpreted-text role="pypi"}:

    >   **Module name**                          **Replace with**
    >   ---------------------------------------- ------------------------------------------
    >   [celery.models]{.title-ref}              [djcelery.models]{.title-ref}
    >   [celery.managers]{.title-ref}            [djcelery.managers]{.title-ref}
    >   [celery.views]{.title-ref}               [djcelery.views]{.title-ref}
    >   [celery.urls]{.title-ref}                [djcelery.urls]{.title-ref}
    >   [celery.management]{.title-ref}          [djcelery.management]{.title-ref}
    >   [celery.loaders.djangoapp]{.title-ref}   [djcelery.loaders]{.title-ref}
    >   [celery.backends.database]{.title-ref}   [djcelery.backends.database]{.title-ref}
    >   [celery.backends.cache]{.title-ref}      [djcelery.backends.cache]{.title-ref}

Importing `djcelery`{.interpreted-text role="mod"} will automatically
setup Celery to use Django loader. loader. It does this by setting the
`CELERY_LOADER`{.interpreted-text role="envvar"} environment variable to
[\"django\"]{.title-ref} (it won\'t change it if a loader is already
set).

When the Django loader is used, the \"database\" and \"cache\" result
backend aliases will point to the `djcelery`{.interpreted-text
role="mod"} backends instead of the built-in backends, and configuration
will be read from the Django settings.

### Upgrading for others {#v200-upgrade}

#### Database result backend {#v200-upgrade-database}

The database result backend is now using
[SQLAlchemy](http://www.sqlalchemy.org) instead of the Django ORM, see
[Supported
Databases](http://www.sqlalchemy.org/docs/core/engines.html#supported-databases)
for a table of supported databases.

The [DATABASE\_\*]{.title-ref} settings has been replaced by a single
setting: `CELERY_RESULT_DBURI`{.interpreted-text role="setting"}. The
value here should be an [SQLAlchemy Connection
String](http://www.sqlalchemy.org/docs/core/engines.html#database-urls),
some examples include:

``` python
# sqlite (filename)
CELERY_RESULT_DBURI = 'sqlite:///celerydb.sqlite'

# mysql
CELERY_RESULT_DBURI = 'mysql://scott:tiger@localhost/foo'

# postgresql
CELERY_RESULT_DBURI = 'postgresql://scott:tiger@localhost/mydatabase'

# oracle
CELERY_RESULT_DBURI = 'oracle://scott:tiger@127.0.0.1:1521/sidname'
```

See [SQLAlchemy Connection
Strings](http://www.sqlalchemy.org/docs/core/engines.html#database-urls)
for more information about connection strings.

To specify additional SQLAlchemy database engine options you can use the
`CELERY_RESULT_ENGINE_OPTIONS`{.interpreted-text role="setting"}
setting:

> ``` python
> # echo enables verbose logging from SQLAlchemy.
> CELERY_RESULT_ENGINE_OPTIONS = {'echo': True}
> ```

#### Cache result backend {#v200-upgrade-cache}

The cache result backend is no longer using the Django cache framework,
but it supports mostly the same configuration syntax:

> ``` python
> CELERY_CACHE_BACKEND = 'memcached://A.example.com:11211;B.example.com'
> ```

To use the cache backend you must either have the
`pylibmc`{.interpreted-text role="pypi"} or
`python-memcached`{.interpreted-text role="pypi"} library installed, of
which the former is regarded as the best choice.

The support backend types are [memcached://]{.title-ref} and
[memory://]{.title-ref}, we haven\'t felt the need to support any of the
other backends provided by Django.

### Backward incompatible changes {#v200-incompatible}

-   Default (python) loader now prints warning on missing
    [celeryconfig.py]{.title-ref} instead of raising
    `ImportError`{.interpreted-text role="exc"}.

    > The worker raises `~@ImproperlyConfigured`{.interpreted-text
    > role="exc"} if the configuration isn\'t set up. This makes it
    > possible to use [\--help]{.title-ref} etc., without having a
    > working configuration.
    >
    > Also this makes it possible to use the client side of Celery
    > without being configured:
    >
    > ``` pycon
    > >>> from carrot.connection import BrokerConnection
    > >>> conn = BrokerConnection('localhost', 'guest', 'guest', '/')
    > >>> from celery.execute import send_task
    > >>> r = send_task('celery.ping', args=(), kwargs={}, connection=conn)
    > >>> from celery.backends.amqp import AMQPBackend
    > >>> r.backend = AMQPBackend(connection=conn)
    > >>> r.get()
    > 'pong'
    > ```

-   The following deprecated settings has been removed (as scheduled by
    the `deprecation-timeline`{.interpreted-text role="ref"}):

    >   **Setting name**                                  **Replace with**
    >   ------------------------------------------------- --------------------------------------------
    >   [CELERY_AMQP_CONSUMER_QUEUES]{.title-ref}         [CELERY_QUEUES]{.title-ref}
    >   [CELERY_AMQP_EXCHANGE]{.title-ref}                [CELERY_DEFAULT_EXCHANGE]{.title-ref}
    >   [CELERY_AMQP_EXCHANGE_TYPE]{.title-ref}           [CELERY_DEFAULT_EXCHANGE_TYPE]{.title-ref}
    >   [CELERY_AMQP_CONSUMER_ROUTING_KEY]{.title-ref}    [CELERY_QUEUES]{.title-ref}
    >   [CELERY_AMQP_PUBLISHER_ROUTING_KEY]{.title-ref}   [CELERY_DEFAULT_ROUTING_KEY]{.title-ref}

-   The [celery.task.rest]{.title-ref} module has been removed, use
    [celery.task.http]{.title-ref} instead (as scheduled by the
    `deprecation-timeline`{.interpreted-text role="ref"}).

-   It\'s no longer allowed to skip the class name in loader names. (as
    scheduled by the `deprecation-timeline`{.interpreted-text
    role="ref"}):

    > Assuming the implicit [Loader]{.title-ref} class name is no longer
    > supported, for example, if you use:
    >
    > ``` python
    > CELERY_LOADER = 'myapp.loaders'
    > ```
    >
    > You need to include the loader class name, like this:
    >
    > ``` python
    > CELERY_LOADER = 'myapp.loaders.Loader'
    > ```

-   `CELERY_TASK_RESULT_EXPIRES`{.interpreted-text role="setting"} now
    defaults to 1 day.

    > Previous default setting was to expire in 5 days.

-   AMQP backend: Don\'t use different values for
    [auto_delete]{.title-ref}.

    > This bug became visible with RabbitMQ 1.8.0, which no longer
    > allows conflicting declarations for the auto_delete and durable
    > settings.
    >
    > If you\'ve already used Celery with this backend chances are you
    > have to delete the previous declaration:
    >
    > ``` console
    > $ camqadm exchange.delete celeryresults
    > ```

-   Now uses pickle instead of cPickle on Python versions \<= 2.5

    > cPickle is broken in Python \<= 2.5.
    >
    > It unsafely and incorrectly uses relative instead of absolute
    > imports, so for example:
    >
    > ``` python
    > exceptions.KeyError
    > ```
    >
    > becomes:
    >
    > ``` python
    > celery.exceptions.KeyError
    > ```
    >
    > Your best choice is to upgrade to Python 2.6, as while the pure
    > pickle version has worse performance, it is the only safe option
    > for older Python versions.

### News {#v200-news}

-   **celeryev**: Curses Celery Monitor and Event Viewer.

    > This is a simple monitor allowing you to see what tasks are
    > executing in real-time and investigate tracebacks and results of
    > ready tasks. It also enables you to set new rate limits and revoke
    > tasks.
    >
    > Screenshot:
    >
    > ![](../images/celeryevshotsm.jpg)
    >
    > If you run [celeryev]{.title-ref} with the [-d]{.title-ref} switch
    > it will act as an event dumper, simply dumping the events it
    > receives to standard out:
    >
    > ``` console
    > $ celeryev -d
    > -> celeryev: starting capture...
    > casper.local [2010-06-04 10:42:07.020000] heartbeat
    > casper.local [2010-06-04 10:42:14.750000] task received:
    >     tasks.add(61a68756-27f4-4879-b816-3cf815672b0e) args=[2, 2] kwargs={}
    >     eta=2010-06-04T10:42:16.669290, retries=0
    > casper.local [2010-06-04 10:42:17.230000] task started
    >     tasks.add(61a68756-27f4-4879-b816-3cf815672b0e) args=[2, 2] kwargs={}
    > casper.local [2010-06-04 10:42:17.960000] task succeeded:
    >     tasks.add(61a68756-27f4-4879-b816-3cf815672b0e)
    >     args=[2, 2] kwargs={} result=4, runtime=0.782663106918
    >
    > The fields here are, in order: *sender hostname*, *timestamp*, *event type* and
    > *additional event fields*.
    > ```

-   AMQP result backend: Now supports [.ready()]{.title-ref},
    [.successful()]{.title-ref}, [.result]{.title-ref},
    [.status]{.title-ref}, and even responds to changes in task state

-   New user guides:

    > -   `guide-workers`{.interpreted-text role="ref"}
    > -   `guide-canvas`{.interpreted-text role="ref"}
    > -   `guide-routing`{.interpreted-text role="ref"}

-   Worker: Standard out/error is now being redirected to the log file.

-   `billiard`{.interpreted-text role="pypi"} has been moved back to the
    Celery repository.

    >   **Module name**                           **celery equivalent**
    >   ----------------------------------------- -------------------------------------------------
    >   [billiard.pool]{.title-ref}               [celery.concurrency.processes.pool]{.title-ref}
    >   [billiard.serialization]{.title-ref}      [celery.serialization]{.title-ref}
    >   [billiard.utils.functional]{.title-ref}   [celery.utils.functional]{.title-ref}
    >
    > The `billiard`{.interpreted-text role="pypi"} distribution may be
    > maintained, depending on interest.

-   now depends on `carrot`{.interpreted-text role="pypi"} \>= 0.10.5

-   now depends on `pyparsing`{.interpreted-text role="pypi"}

-   Worker: Added [\--purge]{.title-ref} as an alias to
    [\--discard]{.title-ref}.

-   Worker: `Control-c`{.interpreted-text role="kbd"} (SIGINT) once does
    warm shutdown, hitting `Control-c`{.interpreted-text role="kbd"}
    twice forces termination.

-   Added support for using complex Crontab-expressions in periodic
    tasks. For example, you can now use:

    > ``` pycon
    > >>> crontab(minute='*/15')
    > ```
    >
    > or even:
    >
    > ``` pycon
    > >>> crontab(minute='*/30', hour='8-17,1-2', day_of_week='thu-fri')
    > ```

    See `guide-beat`{.interpreted-text role="ref"}.

-   Worker: Now waits for available pool processes before applying new
    tasks to the pool.

    > This means it doesn\'t have to wait for dozens of tasks to finish
    > at shutdown because it has applied prefetched tasks without having
    > any pool processes available to immediately accept them.
    >
    > See issue #122.

-   New built-in way to do task callbacks using
    `~celery.subtask`{.interpreted-text role="class"}.

    See `guide-canvas`{.interpreted-text role="ref"} for more
    information.

-   TaskSets can now contain several types of tasks.

    `~celery.task.sets.TaskSet`{.interpreted-text role="class"} has been
    refactored to use a new syntax, please see
    `guide-canvas`{.interpreted-text role="ref"} for more information.

    The previous syntax is still supported, but will be deprecated in
    version 1.4.

-   TaskSet failed() result was incorrect.

    > See issue #132.

-   Now creates different loggers per task class.

    > See issue #129.

-   Missing queue definitions are now created automatically.

    > You can disable this using the
    > `CELERY_CREATE_MISSING_QUEUES`{.interpreted-text role="setting"}
    > setting.
    >
    > The missing queues are created with the following options:
    >
    > ``` python
    > CELERY_QUEUES[name] = {'exchange': name,
    >                        'exchange_type': 'direct',
    >                        'routing_key': 'name}
    > ```
    >
    > This feature is added for easily setting up routing using the
    > [-Q]{.title-ref} option to the worker:
    >
    > ``` console
    > $ celeryd -Q video, image
    > ```
    >
    > See the new routing section of the User Guide for more
    > information: `guide-routing`{.interpreted-text role="ref"}.

-   New Task option: [Task.queue]{.title-ref}

    > If set, message options will be taken from the corresponding entry
    > in `CELERY_QUEUES`{.interpreted-text role="setting"}.
    > [exchange]{.title-ref}, [exchange_type]{.title-ref} and
    > [routing_key]{.title-ref} will be ignored

-   Added support for task soft and hard time limits.

    > New settings added:
    >
    > -   `CELERYD_TASK_TIME_LIMIT`{.interpreted-text role="setting"}
    >
    >     > Hard time limit. The worker processing the task will be
    >     > killed and replaced with a new one when this is exceeded.
    >
    > -   `CELERYD_TASK_SOFT_TIME_LIMIT`{.interpreted-text
    >     role="setting"}
    >
    >     > Soft time limit. The
    >     > `~@SoftTimeLimitExceeded`{.interpreted-text role="exc"}
    >     > exception will be raised when this is exceeded. The task can
    >     > catch this to, for example, clean up before the hard time
    >     > limit comes.
    >
    > New command-line arguments to `celeryd` added:
    > [\--time-limit]{.title-ref} and [\--soft-time-limit]{.title-ref}.
    >
    > What\'s left?
    >
    > This won\'t work on platforms not supporting signals (and
    > specifically the [SIGUSR1]{.title-ref} signal) yet. So an
    > alternative the ability to disable the feature all together on
    > nonconforming platforms must be implemented.
    >
    > Also when the hard time limit is exceeded, the task result should
    > be a [TimeLimitExceeded]{.title-ref} exception.

-   Test suite is now passing without a running broker, using the carrot
    in-memory backend.

-   Log output is now available in colors.

    >   **Log level**            **Color**
    >   ------------------------ -----------
    >   [DEBUG]{.title-ref}      Blue
    >   [WARNING]{.title-ref}    Yellow
    >   [CRITICAL]{.title-ref}   Magenta
    >   [ERROR]{.title-ref}      Red
    >
    > This is only enabled when the log output is a tty. You can
    > explicitly enable/disable this feature using the
    > `CELERYD_LOG_COLOR`{.interpreted-text role="setting"} setting.

-   Added support for task router classes (like the django multi-db
    routers)

    > -   New setting: `CELERY_ROUTES`{.interpreted-text role="setting"}
    >
    > This is a single, or a list of routers to traverse when sending
    > tasks. Dictionaries in this list converts to a
    > `celery.routes.MapRoute`{.interpreted-text role="class"} instance.
    >
    > Examples:
    >
    > > \>\>\> CELERY_ROUTES = {\'celery.ping\': \'default\',
    > >
    > > :   \'mytasks.add\': \'cpu-bound\', \'video.encode\': {
    > >     \'queue\': \'video\', \'exchange\': \'media\'
    > >     \'routing_key\': \'media.video.encode\'}}
    > >
    > > \>\>\> CELERY_ROUTES = (\'myapp.tasks.Router\',
    > >
    > > :   {\'celery.ping\': \'default\'})
    >
    > Where [myapp.tasks.Router]{.title-ref} could be:
    >
    > ``` python
    > class Router(object):
    >
    >     def route_for_task(self, task, args=None, kwargs=None):
    >         if task == 'celery.ping':
    >             return 'default'
    > ```
    >
    > route_for_task may return a string or a dict. A string then means
    > it\'s a queue name in `CELERY_QUEUES`{.interpreted-text
    > role="setting"}, a dict means it\'s a custom route.
    >
    > When sending tasks, the routers are consulted in order. The first
    > router that doesn\'t return [None]{.title-ref} is the route to
    > use. The message options is then merged with the found route
    > settings, where the routers settings have priority.
    >
    > Example if `~celery.execute.apply_async`{.interpreted-text
    > role="func"} has these arguments:
    >
    > ``` pycon
    > >>> Task.apply_async(immediate=False, exchange='video',
    > ...                  routing_key='video.compress')
    > ```
    >
    > and a router returns:
    >
    > ``` python
    > {'immediate': True,
    >  'exchange': 'urgent'}
    > ```
    >
    > the final message options will be:
    >
    > ``` pycon
    > >>> task.apply_async(
    > ...    immediate=True,
    > ...    exchange='urgent',
    > ...    routing_key='video.compress',
    > ... )
    > ```
    >
    > (and any default message options defined in the
    > `~celery.task.base.Task`{.interpreted-text role="class"} class)

-   New Task handler called after the task returns:
    `~celery.task.base.Task.after_return`{.interpreted-text
    role="meth"}.

-   

    `~billiard.einfo.ExceptionInfo`{.interpreted-text role="class"} now passed to

    :   `~celery.task.base.Task.on_retry`{.interpreted-text
        role="meth"}/
        `~celery.task.base.Task.on_failure`{.interpreted-text
        role="meth"} as `einfo` keyword argument.

-   Worker: Added `CELERYD_MAX_TASKS_PER_CHILD`{.interpreted-text
    role="setting"} / `celery worker --maxtasksperchild`.

    > Defines the maximum number of tasks a pool worker can process
    > before the process is terminated and replaced by a new one.

-   Revoked tasks now marked with state `REVOKED`{.interpreted-text
    role="state"}, and [result.get()]{.title-ref} will now raise
    `~@TaskRevokedError`{.interpreted-text role="exc"}.

-   `celery.task.control.ping`{.interpreted-text role="func"} now works
    as expected.

-   [apply(throw=True)]{.title-ref} /
    `CELERY_EAGER_PROPAGATES_EXCEPTIONS`{.interpreted-text
    role="setting"}: Makes eager execution re-raise task errors.

-   New signal: `~celery.signals.worker_process_init`{.interpreted-text
    role="signal"}: Sent inside the pool worker process at init.

-   Worker: `celery worker -Q`{.interpreted-text role="option"} option:
    Ability to specify list of queues to use, disabling other configured
    queues.

    > For example, if `CELERY_QUEUES`{.interpreted-text role="setting"}
    > defines four queues: [image]{.title-ref}, [video]{.title-ref},
    > [data]{.title-ref} and [default]{.title-ref}, the following
    > command would make the worker only consume from the
    > [image]{.title-ref} and [video]{.title-ref} queues:
    >
    > ``` console
    > $ celeryd -Q image,video
    > ```

-   Worker: New return value for the [revoke]{.title-ref} control
    command:

    > Now returns:
    >
    > ``` python
    > {'ok': 'task $id revoked'}
    > ```
    >
    > instead of `True`{.interpreted-text role="const"}.

-   Worker: Can now enable/disable events using remote control

    > Example usage:
    >
    > > \>\>\> from celery.task.control import broadcast \>\>\>
    > > broadcast(\'enable_events\') \>\>\>
    > > broadcast(\'disable_events\')

-   Removed top-level tests directory. Test config now in
    celery.tests.config

    > This means running the unit tests doesn\'t require any special
    > setup. [celery/tests/\_\_init\_\_]{.title-ref} now configures the
    > `CELERY_CONFIG_MODULE`{.interpreted-text role="envvar"} and
    > `CELERY_LOADER`{.interpreted-text role="envvar"} environment
    > variables, so when [nosetests]{.title-ref} imports that, the unit
    > test environment is all set up.
    >
    > Before you run the tests you need to install the test
    > requirements:
    >
    > ``` console
    > $ pip install -r requirements/test.txt
    > ```
    >
    > Running all tests:
    >
    > ``` console
    > $ nosetests
    > ```
    >
    > Specifying the tests to run:
    >
    > ``` console
    > $ nosetests celery.tests.test_task
    > ```
    >
    > Producing HTML coverage:
    >
    > ``` console
    > $ nosetests --with-coverage3
    > ```
    >
    > The coverage output is then located in
    > [celery/tests/cover/index.html]{.title-ref}.

-   Worker: New option \`\--version\`: Dump version info and exit.

-   `celeryd-multi <celeryd.bin.multi>`{.interpreted-text role="mod"}:
    Tool for shell scripts to start multiple workers.

    > Some examples:
    >
    > -   Advanced example with 10 workers:
    >
    >     > -   Three of the workers processes the images and video
    >     >     queue
    >     > -   Two of the workers processes the data queue with
    >     >     loglevel DEBUG
    >     > -   the rest processes the default\' queue.
    >     >
    >     > ``` console
    >     > $ celeryd-multi start 10 -l INFO -Q:1-3 images,video -Q:4,5:data -Q default -L:4,5 DEBUG
    >     > ```
    >
    > -   Get commands to start 10 workers, with 3 processes each
    >
    >     > ``` console
    >     > $ celeryd-multi start 3 -c 3
    >     > celeryd -n celeryd1.myhost -c 3
    >     > celeryd -n celeryd2.myhost -c 3
    >     > celeryd -n celeryd3.myhost -c 3
    >     > ```
    >
    > -   Start 3 named workers
    >
    >     > ``` console
    >     > $ celeryd-multi start image video data -c 3
    >     > celeryd -n image.myhost -c 3
    >     > celeryd -n video.myhost -c 3
    >     > celeryd -n data.myhost -c 3
    >     > ```
    >
    > -   Specify custom hostname
    >
    >     > ``` console
    >     > $ celeryd-multi start 2 -n worker.example.com -c 3
    >     > celeryd -n celeryd1.worker.example.com -c 3
    >     > celeryd -n celeryd2.worker.example.com -c 3
    >     > ```
    >     >
    >     > Additional options are added to each `celeryd`, but you can
    >     > also modify the options for ranges of or single workers
    >
    > -   3 workers: Two with 3 processes, and one with 10 processes.
    >
    >     > ``` console
    >     > $ celeryd-multi start 3 -c 3 -c:1 10
    >     > celeryd -n celeryd1.myhost -c 10
    >     > celeryd -n celeryd2.myhost -c 3
    >     > celeryd -n celeryd3.myhost -c 3
    >     > ```
    >
    > -   Can also specify options for named workers
    >
    >     > ``` console
    >     > $ celeryd-multi start image video data -c 3 -c:image 10
    >     > celeryd -n image.myhost -c 10
    >     > celeryd -n video.myhost -c 3
    >     > celeryd -n data.myhost -c 3
    >     > ```
    >
    > -   Ranges and lists of workers in options is also allowed:
    >     (`-c:1-3` can also be written as `-c:1,2,3`)
    >
    >     > ``` console
    >     > $ celeryd-multi start 5 -c 3  -c:1-3 10
    >     > celeryd-multi -n celeryd1.myhost -c 10
    >     > celeryd-multi -n celeryd2.myhost -c 10
    >     > celeryd-multi -n celeryd3.myhost -c 10
    >     > celeryd-multi -n celeryd4.myhost -c 3
    >     > celeryd-multi -n celeryd5.myhost -c 3
    >     > ```
    >
    > -   Lists also work with named workers:
    >
    >     > ``` console
    >     > $ celeryd-multi start foo bar baz xuzzy -c 3 -c:foo,bar,baz 10
    >     > celeryd-multi -n foo.myhost -c 10
    >     > celeryd-multi -n bar.myhost -c 10
    >     > celeryd-multi -n baz.myhost -c 10
    >     > celeryd-multi -n xuzzy.myhost -c 3
    >     > ```

-   The worker now calls the result backends
    [process_cleanup]{.title-ref} method *after* task execution instead
    of before.

-   AMQP result backend now supports Pika.
