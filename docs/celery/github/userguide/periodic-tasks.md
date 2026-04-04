# Periodic Tasks {#guide-beat}

::: {.contents local=""}
:::

## Introduction

`celery beat`{.interpreted-text role="program"} is a scheduler; It kicks
off tasks at regular intervals, that are then executed by available
worker nodes in the cluster.

By default the entries are taken from the
`beat_schedule`{.interpreted-text role="setting"} setting, but custom
stores can also be used, like storing the entries in a SQL database.

You have to ensure only a single scheduler is running for a schedule at
a time, otherwise you\'d end up with duplicate tasks. Using a
centralized approach means the schedule doesn\'t have to be
synchronized, and the service can operate without using locks.

## Time Zones {#beat-timezones}

The periodic task schedules uses the UTC time zone by default, but you
can change the time zone used using the `timezone`{.interpreted-text
role="setting"} setting.

An example time zone could be \`Europe/London\`:

``` python
timezone = 'Europe/London'
```

This setting must be added to your app, either by configuring it
directly using (`app.conf.timezone = 'Europe/London'`), or by adding it
to your configuration module if you have set one up using
`app.config_from_object`. See
`celerytut-configuration`{.interpreted-text role="ref"} for more
information about configuration options.

The default scheduler (storing the schedule in the
`celerybeat-schedule`{.interpreted-text role="file"} file) will
automatically detect that the time zone has changed, and so will reset
the schedule itself, but other schedulers may not be so smart (e.g., the
Django database scheduler, see below) and in that case you\'ll have to
reset the schedule manually.

::: admonition
Django Users

Celery recommends and is compatible with the `USE_TZ` setting introduced
in Django 1.4.

For Django users the time zone specified in the `TIME_ZONE` setting will
be used, or you can specify a custom time zone for Celery alone by using
the `timezone`{.interpreted-text role="setting"} setting.

The database scheduler won\'t reset when timezone related settings
change, so you must do this manually:

``` console
$ python manage.py shell
>>> from djcelery.models import PeriodicTask
>>> PeriodicTask.objects.update(last_run_at=None)
```

Django-Celery only supports Celery 4.0 and below, for Celery 4.0 and
above, do as follow:

``` console
$ python manage.py shell
>>> from django_celery_beat.models import PeriodicTask
>>> PeriodicTask.objects.update(last_run_at=None)
```
:::

## Entries {#beat-entries}

To call a task periodically you have to add an entry to the beat
schedule list.

``` python
from celery import Celery
from celery.schedules import crontab

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('hello') every 30 seconds.
    # It uses the same signature of previous task, an explicit name is
    # defined to avoid this task replacing the previous one defined.
    sender.add_periodic_task(30.0, test.s('hello'), name='add every 30')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)

@app.task
def add(x, y):
    z = x + y
    print(z)
```

Setting these up from within the
`~@on_after_configure`{.interpreted-text role="data"} handler means that
we\'ll not evaluate the app at module level when using `test.s()`. Note
that `~@on_after_configure`{.interpreted-text role="data"} is sent after
the app is set up, so tasks outside the module where the app is declared
(e.g. in a [tasks.py]{.title-ref} file located by
`celery.Celery.autodiscover_tasks`{.interpreted-text role="meth"}) must
use a later signal, such as `~@on_after_finalize`{.interpreted-text
role="data"}.

The `~@add_periodic_task`{.interpreted-text role="meth"} function will
add the entry to the `beat_schedule`{.interpreted-text role="setting"}
setting behind the scenes, and the same setting can also be used to set
up periodic tasks manually:

Example: Run the [tasks.add]{.title-ref} task every 30 seconds.

``` python
app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'UTC'
```

::: note
::: title
Note
:::

If you\'re wondering where these settings should go then please see
`celerytut-configuration`{.interpreted-text role="ref"}. You can either
set these options on your app directly or you can keep a separate module
for configuration.

If you want to use a single item tuple for [args]{.title-ref}, don\'t
forget that the constructor is a comma, and not a pair of parentheses.
:::

Using a `~datetime.timedelta`{.interpreted-text role="class"} for the
schedule means the task will be sent in 30 second intervals (the first
task will be sent 30 seconds after [celery beat]{.title-ref} starts, and
then every 30 seconds after the last run).

A Crontab like schedule also exists, see the section on [Crontab
schedules](#crontab-schedules).

Like with `cron`{.interpreted-text role="command"}, the tasks may
overlap if the first task doesn\'t complete before the next. If that\'s
a concern you should use a locking strategy to ensure only one instance
can run at a time (see for example
`cookbook-task-serial`{.interpreted-text role="ref"}).

### Available Fields {#beat-entry-fields}

-   [task]{.title-ref}

    > The name of the task to execute.
    >
    > Task names are described in the `task-names`{.interpreted-text
    > role="ref"} section of the User Guide. Note that this is not the
    > import path of the task, even though the default naming pattern is
    > built like it is.

-   [schedule]{.title-ref}

    > The frequency of execution.
    >
    > This can be the number of seconds as an integer, a
    > `~datetime.timedelta`{.interpreted-text role="class"}, or a
    > `~celery.schedules.crontab`{.interpreted-text role="class"}. You
    > can also define your own custom schedule types, by extending the
    > interface of `~celery.schedules.schedule`{.interpreted-text
    > role="class"}.

-   [args]{.title-ref}

    > Positional arguments (`list`{.interpreted-text role="class"} or
    > `tuple`{.interpreted-text role="class"}).

-   [kwargs]{.title-ref}

    > Keyword arguments (`dict`{.interpreted-text role="class"}).

-   [options]{.title-ref}

    > Execution options (`dict`{.interpreted-text role="class"}).
    >
    > This can be any argument supported by
    > `~celery.app.task.Task.apply_async`{.interpreted-text role="meth"}
    > \--[exchange]{.title-ref}, [routing_key]{.title-ref},
    > [expires]{.title-ref}, and so on.

-   [relative]{.title-ref}

    > If [relative]{.title-ref} is true
    > `~datetime.timedelta`{.interpreted-text role="class"} schedules
    > are scheduled \"by the clock.\" This means the frequency is
    > rounded to the nearest second, minute, hour or day depending on
    > the period of the `~datetime.timedelta`{.interpreted-text
    > role="class"}.
    >
    > By default [relative]{.title-ref} is false, the frequency isn\'t
    > rounded and will be relative to the time when
    > `celery beat`{.interpreted-text role="program"} was started.

## Crontab schedules {#beat-crontab}

If you want more control over when the task is executed, for example, a
particular time of day or day of the week, you can use the
`~celery.schedules.crontab`{.interpreted-text role="class"} schedule
type:

``` python
from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}
```

The syntax of these Crontab expressions are very flexible.

Some examples:

+---------------------------------+------------------------------------+
| **Example**                     | **Meaning**                        |
+---------------------------------+------------------------------------+
| `crontab()`                     | Execute every minute.              |
+---------------------------------+------------------------------------+
| `crontab(minute=0, hour=0)`     | Execute daily at midnight.         |
+---------------------------------+------------------------------------+
| `crontab(minute=0, hour='*/3')` | Execute every three hours:         |
|                                 | midnight, 3am, 6am, 9am, noon,     |
|                                 | 3pm, 6pm, 9pm.                     |
+---------------------------------+------------------------------------+
| `crontab(minute=0,`             | Same as previous.                  |
|                                 |                                    |
| :                               |                                    |
|   `hour='0,3,6,9,12,15,18,21')` |                                    |
+---------------------------------+------------------------------------+
| `crontab(minute='*/15')`        | Execute every 15 minutes.          |
+---------------------------------+------------------------------------+
| `crontab(day_of_week='sunday')` | Execute every minute (!) at        |
|                                 | Sundays.                           |
+---------------------------------+------------------------------------+
| `crontab(minute='*',`           | Same as previous.                  |
|                                 |                                    |
| :   `hour='*',`                 |                                    |
|     `day_of_week='sun')`        |                                    |
+---------------------------------+------------------------------------+
| `crontab(minute='*/10',`        | Execute every ten minutes, but     |
|                                 | only between 3-4 am, 5-6 pm, and   |
| :   `hour='3,17,22',`           | 10-11 pm on Thursdays or Fridays.  |
|     `day_of_week='thu,fri')`    |                                    |
+---------------------------------+------------------------------------+
| `cro                            | Execute every even hour, and every |
| ntab(minute=0, hour='*/2,*/3')` | hour divisible by three. This      |
|                                 | means: at every hour *except*:     |
|                                 | 1am, 5am, 7am, 11am, 1pm, 5pm,     |
|                                 | 7pm, 11pm                          |
+---------------------------------+------------------------------------+
| `crontab(minute=0, hour='*/5')` | Execute hour divisible by 5. This  |
|                                 | means that it is triggered at 3pm, |
|                                 | not 5pm (since 3pm equals the      |
|                                 | 24-hour clock value of \"15\",     |
|                                 | which is divisible by 5).          |
+---------------------------------+------------------------------------+
| `cron                           | Execute every hour divisible by 3, |
| tab(minute=0, hour='*/3,8-17')` | and every hour during office hours |
|                                 | (8am-5pm).                         |
+---------------------------------+------------------------------------+
| `c                              | Execute on the second day of every |
| rontab(0, 0, day_of_month='2')` | month.                             |
+---------------------------------+------------------------------------+
| `crontab(0, 0,`                 | Execute on every even numbered     |
|                                 | day.                               |
| :   `day_of_month='2-30/2')`    |                                    |
+---------------------------------+------------------------------------+
| `crontab(0, 0,`                 | Execute on the first and third     |
|                                 | weeks of the month.                |
| :   `day_of_month='1-7,15-21')` |                                    |
+---------------------------------+------------------------------------+
| `cr                             | Execute on the eleventh of May     |
| ontab(0, 0, day_of_month='11',` | every year.                        |
|                                 |                                    |
| :   `month_of_year='5')`        |                                    |
+---------------------------------+------------------------------------+
| `crontab(0, 0,`                 | Execute every day on the first     |
|                                 | month of every quarter.            |
| :   `month_of_year='*/3')`      |                                    |
+---------------------------------+------------------------------------+

See `celery.schedules.crontab`{.interpreted-text role="class"} for more
documentation.

## Solar schedules {#beat-solar}

If you have a task that should be executed according to sunrise, sunset,
dawn or dusk, you can use the
`~celery.schedules.solar`{.interpreted-text role="class"} schedule type:

``` python
from celery.schedules import solar

app.conf.beat_schedule = {
    # Executes at sunset in Melbourne
    'add-at-melbourne-sunset': {
        'task': 'tasks.add',
        'schedule': solar('sunset', -37.81753, 144.96715),
        'args': (16, 16),
    },
}
```

The arguments are simply: `solar(event, latitude, longitude)`

Be sure to use the correct sign for latitude and longitude:

  --------------- ------------------- ----------------------
  **Sign**        **Argument**        **Meaning**

  `+`             `latitude`          North

  `-`             `latitude`          South

  `+`             `longitude`         East

  `-`             `longitude`         West
  --------------- ------------------- ----------------------

Possible event types are:

  ---------------------------------- ------------------------------------
  **Event**                          **Meaning**

  `dawn_astronomical`                Execute at the moment after which
                                     the sky is no longer completely
                                     dark. This is when the sun is 18
                                     degrees below the horizon.

  `dawn_nautical`                    Execute when there\'s enough
                                     sunlight for the horizon and some
                                     objects to be distinguishable;
                                     formally, when the sun is 12 degrees
                                     below the horizon.

  `dawn_civil`                       Execute when there\'s enough light
                                     for objects to be distinguishable so
                                     that outdoor activities can
                                     commence; formally, when the Sun is
                                     6 degrees below the horizon.

  `sunrise`                          Execute when the upper edge of the
                                     sun appears over the eastern horizon
                                     in the morning.

  `solar_noon`                       Execute when the sun is highest
                                     above the horizon on that day.

  `sunset`                           Execute when the trailing edge of
                                     the sun disappears over the western
                                     horizon in the evening.

  `dusk_civil`                       Execute at the end of civil
                                     twilight, when objects are still
                                     distinguishable and some stars and
                                     planets are visible. Formally, when
                                     the sun is 6 degrees below the
                                     horizon.

  `dusk_nautical`                    Execute when the sun is 12 degrees
                                     below the horizon. Objects are no
                                     longer distinguishable, and the
                                     horizon is no longer visible to the
                                     naked eye.

  `dusk_astronomical`                Execute at the moment after which
                                     the sky becomes completely dark;
                                     formally, when the sun is 18 degrees
                                     below the horizon.
  ---------------------------------- ------------------------------------

All solar events are calculated using UTC, and are therefore unaffected
by your timezone setting.

In polar regions, the sun may not rise or set every day. The scheduler
is able to handle these cases (i.e., a `sunrise` event won\'t run on a
day when the sun doesn\'t rise). The one exception is `solar_noon`,
which is formally defined as the moment the sun transits the celestial
meridian, and will occur every day even if the sun is below the horizon.

Twilight is defined as the period between dawn and sunrise; and between
sunset and dusk. You can schedule an event according to \"twilight\"
depending on your definition of twilight (civil, nautical, or
astronomical), and whether you want the event to take place at the
beginning or end of twilight, using the appropriate event from the list
above.

See `celery.schedules.solar`{.interpreted-text role="class"} for more
documentation.

## Starting the Scheduler {#beat-starting}

To start the `celery beat`{.interpreted-text role="program"} service:

``` console
$ celery -A proj beat
```

You can also embed [beat]{.title-ref} inside the worker by enabling the
workers `-B <celery worker -B>`{.interpreted-text role="option"} option,
this is convenient if you\'ll never run more than one worker node, but
it\'s not commonly used and for that reason isn\'t recommended for
production use:

``` console
$ celery -A proj worker -B
```

Beat needs to store the last run times of the tasks in a local database
file (named [celerybeat-schedule]{.title-ref} by default), so it needs
access to write in the current directory, or alternatively you can
specify a custom location for this file:

``` console
$ celery -A proj beat -s /home/celery/var/run/celerybeat-schedule
```

::: note
::: title
Note
:::

To daemonize beat see `daemonizing`{.interpreted-text role="ref"}.
:::

### Using custom scheduler classes {#beat-custom-schedulers}

Custom scheduler classes can be specified on the command-line (the
`--scheduler <celery beat --scheduler>`{.interpreted-text role="option"}
argument).

The default scheduler is the
`celery.beat.PersistentScheduler`{.interpreted-text role="class"}, that
simply keeps track of the last run times in a local
`shelve`{.interpreted-text role="mod"} database file.

There\'s also the `django-celery-beat`{.interpreted-text role="pypi"}
extension that stores the schedule in the Django database, and presents
a convenient admin interface to manage periodic tasks at runtime.

To install and use this extension:

1.  Use `pip`{.interpreted-text role="command"} to install the package:

    > ``` console
    > $ pip install django-celery-beat
    > ```

2.  Add the `django_celery_beat` module to `INSTALLED_APPS` in your
    Django project\' `settings.py`{.interpreted-text role="file"}:

        INSTALLED_APPS = (
            ...,
            'django_celery_beat',
        )

    Note that there is no dash in the module name, only underscores.

3.  Apply Django database migrations so that the necessary tables are
    created:

    > ``` console
    > $ python manage.py migrate
    > ```

4.  Start the `celery beat`{.interpreted-text role="program"} service
    using the `django_celery_beat.schedulers:DatabaseScheduler`
    scheduler:

    > ``` console
    > $ celery -A proj beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
    > ```

    Note: You may also add this as the
    `beat_scheduler`{.interpreted-text role="setting"} setting directly.

5.  Visit the Django-Admin interface to set up some periodic tasks.
