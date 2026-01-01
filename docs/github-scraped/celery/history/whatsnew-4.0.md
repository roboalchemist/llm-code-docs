# What\'s new in Celery 4.0 (latentcall) {#whatsnew-4.0}

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

This version is officially supported on CPython 2.7, 3.4, and 3.5. and
also supported on PyPy.

::: topic
**Table of Contents**

Make sure you read the important notes before upgrading to this version.
:::

::: {.contents local="" depth="3"}
:::

## Preface

Welcome to Celery 4!

This is a massive release with over two years of changes. Not only does
it come with many new features, but it also fixes a massive list of
bugs, so in many ways you could call it our \"Snow Leopard\" release.

The next major version of Celery will support Python 3.5 only, where we
are planning to take advantage of the new asyncio library.

This release would not have been possible without the support of my
employer, [Robinhood](https://robinhood.com) (we\'re hiring!).

-   Ask Solem

Dedicated to Sebastian \"Zeb\" Bjørnerud (RIP), with special thanks to
[Ty Wilkins](http://tywilkins.com), for designing our new logo, all the
contributors who help make this happen, and my colleagues at
[Robinhood](https://robinhood.com).

### Wall of Contributors

Aaron McMillin, Adam Chainz, Adam Renberg, Adriano Martins de Jesus,
Adrien Guinet, Ahmet Demir, Aitor Gómez-Goiri, Alan Justino, Albert
Wang, Alex Koshelev, Alex Rattray, Alex Williams, Alexander Koshelev,
Alexander Lebedev, Alexander Oblovatniy, Alexey Kotlyarov, Ali
Bozorgkhan, Alice Zoë Bevan--McGregor, Allard Hoeve, Alman One, Amir
Rustamzadeh, Andrea Rabbaglietti, Andrea Rosa, Andrei Fokau, Andrew
Rodionoff, Andrew Stewart, Andriy Yurchuk, Aneil Mallavarapu, Areski
Belaid, Armenak Baburyan, Arthur Vuillard, Artyom Koval, Asif Saifuddin
Auvi, Ask Solem, Balthazar Rouberol, Batiste Bieler, Berker Peksag, Bert
Vanderbauwhede, Brendan Smithyman, Brian Bouterse, Bryce Groff, Cameron
Will, ChangBo Guo, Chris Clark, Chris Duryee, Chris Erway, Chris Harris,
Chris Martin, Chillar Anand, Colin McIntosh, Conrad Kramer, Corey
Farwell, Craig Jellick, Cullen Rhodes, Dallas Marlow, Daniel Devine,
Daniel Wallace, Danilo Bargen, Davanum Srinivas, Dave Smith, David
Baumgold, David Harrigan, David Pravec, Dennis Brakhane, Derek Anderson,
Dmitry Dygalo, Dmitry Malinovsky, Dongweiming, Dudás Ádám, Dustin J.
Mitchell, Ed Morley, Edward Betts, Éloi Rivard, Emmanuel Cazenave, Fahad
Siddiqui, Fatih Sucu, Feanil Patel, Federico Ficarelli, Felix Schwarz,
Felix Yan, Fernando Rocha, Flavio Grossi, Frantisek Holop, Gao
Jiangmiao, George Whewell, Gerald Manipon, Gilles Dartiguelongue, Gino
Ledesma, Greg Wilbur, Guillaume Seguin, Hank John, Hogni Gylfason, Ilya
Georgievsky, Ionel Cristian Mărieș, Ivan Larin, James Pulec, Jared
Lewis, Jason Veatch, Jasper Bryant-Greene, Jeff Widman, Jeremy Tillman,
Jeremy Zafran, Jocelyn Delalande, Joe Jevnik, Joe Sanford, John
Anderson, John Barham, John Kirkham, John Whitlock, Jonathan Vanasco,
Joshua Harlow, João Ricardo, Juan Carlos Ferrer, Juan Rossi, Justin
Patrin, Kai Groner, Kevin Harvey, Kevin Richardson, Komu Wairagu,
Konstantinos Koukopoulos, Kouhei Maeda, Kracekumar Ramaraju, Krzysztof
Bujniewicz, Latitia M. Haskins, Len Buckens, Lev Berman, lidongming,
Lorenzo Mancini, Lucas Wiman, Luke Pomfrey, Luyun Xie, Maciej
Obuchowski, Manuel Kaufmann, Marat Sharafutdinov, Marc Sibson, Marcio
Ribeiro, Marin Atanasov Nikolov, Mathieu Fenniak, Mark Parncutt, Mauro
Rocco, Maxime Beauchemin, Maxime Vdb, Mher Movsisyan, Michael Aquilina,
Michael Duane Mooring, Michael Permana, Mickaël Penhard, Mike Attwood,
Mitchel Humpherys, Mohamed Abouelsaoud, Morris Tweed, Morton Fox, Môshe
van der Sterre, Nat Williams, Nathan Van Gheem, Nicolas Unravel, Nik
Nyby, Omer Katz, Omer Korner, Ori Hoch, Paul Pearce, Paulo Bu, Pavlo
Kapyshin, Philip Garnero, Pierre Fersing, Piotr Kilczuk, Piotr Maślanka,
Quentin Pradet, Radek Czajka, Raghuram Srinivasan, Randy Barlow, Raphael
Michel, Rémy Léone, Robert Coup, Robert Kolba, Rockallite Wulf, Rodolfo
Carvalho, Roger Hu, Romuald Brunet, Rongze Zhu, Ross Deane, Ryan Luckie,
Rémy Greinhofer, Samuel Giffard, Samuel Jaillet, Sergey Azovskov, Sergey
Tikhonov, Seungha Kim, Simon Peeters, Spencer E. Olson, Srinivas
Garlapati, Stephen Milner, Steve Peak, Steven Sklar, Stuart Axon, Sukrit
Khera, Tadej Janež, Taha Jahangir, Takeshi Kanemoto, Tayfun Sen, Tewfik
Sadaoui, Thomas French, Thomas Grainger, Tomas Machalek, Tobias
Schottdorf, Tocho Tochev, Valentyn Klindukh, Vic Kumar, Vladimir
Bolshakov, Vladimir Gorbunov, Wayne Chang, Wieland Hoffmann, Wido den
Hollander, Wil Langford, Will Thompson, William King, Yury Selivanov,
Vytis Banaitis, Zoran Pavlovic, Xin Li, 許邱翔,
`allenling`{.interpreted-text role="github_user"},
`alzeih`{.interpreted-text role="github_user"},
`bastb`{.interpreted-text role="github_user"},
`bee-keeper`{.interpreted-text role="github_user"},
`ffeast`{.interpreted-text role="github_user"},
`firefly4268`{.interpreted-text role="github_user"},
`flyingfoxlee`{.interpreted-text role="github_user"},
`gdw2`{.interpreted-text role="github_user"},
`gitaarik`{.interpreted-text role="github_user"},
`hankjin`{.interpreted-text role="github_user"}, `lvh`{.interpreted-text
role="github_user"}, `m-vdb`{.interpreted-text role="github_user"},
`kindule`{.interpreted-text role="github_user"}, `mdk`{.interpreted-text
role="github_user"}:, `michael-k`{.interpreted-text role="github_user"},
`mozillazg`{.interpreted-text role="github_user"},
`nokrik`{.interpreted-text role="github_user"},
`ocean1`{.interpreted-text role="github_user"},
`orlo666`{.interpreted-text role="github_user"},
`raducc`{.interpreted-text role="github_user"},
`wanglei`{.interpreted-text role="github_user"},
`worldexception`{.interpreted-text role="github_user"},
`xBeAsTx`{.interpreted-text role="github_user"}.

::: note
::: title
Note
:::

This wall was automatically generated from git history, so sadly it
doesn\'t not include the people who help with more important things like
answering mailing-list questions.
:::

## Upgrading from Celery 3.1

### Step 1: Upgrade to Celery 3.1.25

If you haven\'t already, the first step is to upgrade to Celery 3.1.25.

This version adds forward compatibility to the new message protocol, so
that you can incrementally upgrade from 3.1 to 4.0.

Deploy the workers first by upgrading to 3.1.25, this means these
workers can process messages sent by clients using both 3.1 and 4.0.

After the workers are upgraded you can upgrade the clients (e.g. web
servers).

### Step 2: Update your configuration with the new setting names

This version radically changes the configuration setting names, to be
more consistent.

The changes are fully backwards compatible, so you have the option to
wait until the old setting names are deprecated, but to ease the
transition we have included a command-line utility that rewrites your
settings automatically.

See `v400-upgrade-settings`{.interpreted-text role="ref"} for more
information.

### Step 3: Read the important notes in this document

Make sure you are not affected by any of the important upgrade notes
mentioned in the following section.

An especially important note is that Celery now checks the arguments you
send to a task by matching it to the signature
(`v400-typing`{.interpreted-text role="ref"}).

### Step 4: Upgrade to Celery 4.0

At this point you can upgrade your workers and clients with the new
version.

## Important Notes {#v400-important}

### Dropped support for Python 2.6

Celery now requires Python 2.7 or later, and also drops support for
Python 3.3 so supported versions are:

-   CPython 2.7
-   CPython 3.4
-   CPython 3.5
-   PyPy 5.4 (`pypy2`)
-   PyPy 5.5-alpha (`pypy3`)

### Last major version to support Python 2

Starting from Celery 5.0 only Python 3.5+ will be supported.

To make sure you\'re not affected by this change you should pin the
Celery version in your requirements file, either to a specific version:
`celery==4.0.0`, or a range: `celery>=4.0,<5.0`.

Dropping support for Python 2 will enable us to remove massive amounts
of compatibility code, and going with Python 3.5 allows us to take
advantage of typing, async/await, asyncio, and similar concepts there\'s
no alternative for in older versions.

Celery 4.x will continue to work on Python 2.7, 3.4, 3.5; just as Celery
3.x still works on Python 2.6.

### Django support

Celery 4.x requires Django 1.8 or later, but we really recommend using
at least Django 1.9 for the new `transaction.on_commit` feature.

A common problem when calling tasks from Django is when the task is
related to a model change, and you wish to cancel the task if the
transaction is rolled back, or ensure the task is only executed after
the changes have been written to the database.

`transaction.atomic` enables you to solve this problem by adding the
task as a callback to be called only when the transaction is committed.

Example usage:

``` python
from functools import partial
from django.db import transaction

from .models import Article, Log
from .tasks import send_article_created_notification

def create_article(request):
    with transaction.atomic():
        article = Article.objects.create(**request.POST)
        # send this task only if the rest of the transaction succeeds.
        transaction.on_commit(partial(
            send_article_created_notification.delay, article_id=article.pk))
        Log.objects.create(type=Log.ARTICLE_CREATED, object_pk=article.pk)
```

### Removed features

-   Microsoft Windows is no longer supported.

    The test suite is passing, and Celery seems to be working with
    Windows, but we make no guarantees as we are unable to diagnose
    issues on this platform. If you are a company requiring support on
    this platform, please get in touch.

-   Jython is no longer supported.

#### Features removed for simplicity

-   Webhook task machinery (`celery.task.http`) has been removed.

    > Nowadays it\'s easy to use the `requests`{.interpreted-text
    > role="pypi"} module to write webhook tasks manually. We would love
    > to use requests but we are simply unable to as there\'s a very
    > vocal \'anti-dependency\' mob in the Python community
    >
    > If you need backwards compatibility you can simply copy + paste
    > the 3.1 version of the module and make sure it\'s imported by the
    > worker:
    > <https://github.com/celery/celery/blob/3.1/celery/task/http.py>

-   Tasks no longer sends error emails.

    > This also removes support for `app.mail_admins`, and any
    > functionality related to sending emails.

-   `celery.contrib.batches` has been removed.

    > This was an experimental feature, so not covered by our
    > deprecation timeline guarantee.
    >
    > You can copy and pass the existing batches code for use within
    > your projects:
    > <https://github.com/celery/celery/blob/3.1/celery/contrib/batches.py>

#### Features removed for lack of funding

We announced with the 3.1 release that some transports were moved to
experimental status, and that there\'d be no official support for the
transports.

As this subtle hint for the need of funding failed we\'ve removed them
completely, breaking backwards compatibility.

-   Using the Django ORM as a broker is no longer supported.

    > You can still use the Django ORM as a result backend: see
    > `django-celery-results`{.interpreted-text role="ref"} section for
    > more information.

-   Using SQLAlchemy as a broker is no longer supported.

    > You can still use SQLAlchemy as a result backend.

-   Using CouchDB as a broker is no longer supported.

    > You can still use CouchDB as a result backend.

-   Using IronMQ as a broker is no longer supported.

-   Using Beanstalk as a broker is no longer supported.

In addition some features have been removed completely so that
attempting to use them will raise an exception:

-   The `--autoreload` feature has been removed.

    This was an experimental feature, and not covered by our deprecation
    timeline guarantee. The flag is removed completely so the worker
    will crash at startup when present. Luckily this flag isn\'t used in
    production systems.

-   The experimental `threads` pool is no longer supported and has been
    removed.

-   The `force_execv` feature is no longer supported.

    > The `celery worker` command now ignores the `--no-execv`,
    > `--force-execv`, and the `CELERYD_FORCE_EXECV` setting.
    >
    > This flag will be removed completely in 5.0 and the worker will
    > raise an error.

-   The old legacy \"amqp\" result backend has been deprecated, and will
    be removed in Celery 5.0.

    > Please use the `rpc` result backend for RPC-style calls, and a
    > persistent result backend for multi-consumer results.

We think most of these can be fixed without considerable effort, so if
you\'re interested in getting any of these features back, please get in
touch.

**Now to the good news**\...

### New Task Message Protocol

This version introduces a brand new task message protocol, the first
major change to the protocol since the beginning of the project.

The new protocol is enabled by default in this version and since the new
version isn\'t backwards compatible you have to be careful when
upgrading.

The 3.1.25 version was released to add compatibility with the new
protocol so the easiest way to upgrade is to upgrade to that version
first, then upgrade to 4.0 in a second deployment.

If you wish to keep using the old protocol you may also configure the
protocol version number used:

``` python
app = Celery()
app.conf.task_protocol = 1
```

Read more about the features available in the new protocol in the news
section found later in this document.

### Lowercase setting names {#v400-upgrade-settings}

In the pursuit of beauty all settings are now renamed to be in all
lowercase and some setting names have been renamed for consistency.

This change is fully backwards compatible so you can still use the
uppercase setting names, but we would like you to upgrade as soon as
possible and you can do this automatically using the
`celery upgrade settings`{.interpreted-text role="program"} command:

``` console
$ celery upgrade settings proj/settings.py
```

This command will modify your module in-place to use the new lower-case
names (if you want uppercase with a \"`CELERY`\" prefix see block
below), and save a backup in `proj/settings.py.orig`{.interpreted-text
role="file"}.

> If you\'re loading Celery configuration from the Django settings
> module then you\'ll want to keep using the uppercase names.
>
> You also want to use a `CELERY_` prefix so that no Celery settings
> collide with Django settings used by other apps.
>
> To do this, you\'ll first need to convert your settings file to use
> the new consistent naming scheme, and add the prefix to all Celery
> related settings:
>
> ``` console
> $ celery upgrade settings proj/settings.py --django
> ```
>
> After upgrading the settings file, you need to set the prefix
> explicitly in your `proj/celery.py` module:
>
> ``` python
> app.config_from_object('django.conf:settings', namespace='CELERY')
> ```
>
> You can find the most up to date Django Celery integration example
> here: `django-first-steps`{.interpreted-text role="ref"}.
>
> ::: note
> ::: title
> Note
> :::
>
> This will also add a prefix to settings that didn\'t previously have
> one, for example `BROKER_URL` should be written `CELERY_BROKER_URL`
> with a namespace of `CELERY` `CELERY_BROKER_URL`.
> :::
>
> Luckily you don\'t have to manually change the files, as the
> `celery upgrade settings --django`{.interpreted-text role="program"}
> program should do the right thing.

The loader will try to detect if your configuration is using the new
format, and act accordingly, but this also means you\'re not allowed to
mix and match new and old setting names, that\'s unless you provide a
value for both alternatives.

The major difference between previous versions, apart from the lower
case names, are the renaming of some prefixes, like `celerybeat_` to
`beat_`, `celeryd_` to `worker_`.

The `celery_` prefix has also been removed, and task related settings
from this name-space is now prefixed by `task_`, worker related settings
with `worker_`.

Apart from this most of the settings will be the same in lowercase,
apart from a few special ones:

  **Setting name**                     **Replace with**
  ------------------------------------ --------------------------------------------------------------------------------------------------------------
  `CELERY_MAX_CACHED_RESULTS`          `result_cache_max`{.interpreted-text role="setting"}
  `CELERY_MESSAGE_COMPRESSION`         `result_compression`{.interpreted-text role="setting"}/`task_compression`{.interpreted-text role="setting"}.
  `CELERY_TASK_RESULT_EXPIRES`         `result_expires`{.interpreted-text role="setting"}
  `CELERY_RESULT_DBURI`                `result_backend`{.interpreted-text role="setting"}
  `CELERY_RESULT_ENGINE_OPTIONS`       `database_engine_options`{.interpreted-text role="setting"}
  `-*-_DB_SHORT_LIVED_SESSIONS`        `database_short_lived_sessions`{.interpreted-text role="setting"}
  `CELERY_RESULT_DB_TABLE_NAMES`       `database_db_names`{.interpreted-text role="setting"}
  `CELERY_ACKS_LATE`                   `task_acks_late`{.interpreted-text role="setting"}
  `CELERY_ALWAYS_EAGER`                `task_always_eager`{.interpreted-text role="setting"}
  `CELERY_ANNOTATIONS`                 `task_annotations`{.interpreted-text role="setting"}
  `CELERY_MESSAGE_COMPRESSION`         `task_compression`{.interpreted-text role="setting"}
  `CELERY_CREATE_MISSING_QUEUES`       `task_create_missing_queues`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_DELIVERY_MODE`       `task_default_delivery_mode`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_EXCHANGE`            `task_default_exchange`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_EXCHANGE_TYPE`       `task_default_exchange_type`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_QUEUE`               `task_default_queue`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_RATE_LIMIT`          `task_default_rate_limit`{.interpreted-text role="setting"}
  `CELERY_DEFAULT_ROUTING_KEY`         `task_default_routing_key`{.interpreted-text role="setting"}
  `-"-_EAGER_PROPAGATES_EXCEPTIONS`    `task_eager_propagates`{.interpreted-text role="setting"}
  `CELERY_IGNORE_RESULT`               `task_ignore_result`{.interpreted-text role="setting"}
  `CELERY_TASK_PUBLISH_RETRY`          `task_publish_retry`{.interpreted-text role="setting"}
  `CELERY_TASK_PUBLISH_RETRY_POLICY`   `task_publish_retry_policy`{.interpreted-text role="setting"}
  `CELERY_QUEUES`                      `task_queues`{.interpreted-text role="setting"}
  `CELERY_ROUTES`                      `task_routes`{.interpreted-text role="setting"}
  `CELERY_SEND_TASK_SENT_EVENT`        `task_send_sent_event`{.interpreted-text role="setting"}
  `CELERY_TASK_SERIALIZER`             `task_serializer`{.interpreted-text role="setting"}
  `CELERYD_TASK_SOFT_TIME_LIMIT`       `task_soft_time_limit`{.interpreted-text role="setting"}
  `CELERYD_TASK_TIME_LIMIT`            `task_time_limit`{.interpreted-text role="setting"}
  `CELERY_TRACK_STARTED`               `task_track_started`{.interpreted-text role="setting"}
  `CELERY_DISABLE_RATE_LIMITS`         `worker_disable_rate_limits`{.interpreted-text role="setting"}
  `CELERY_ENABLE_REMOTE_CONTROL`       `worker_enable_remote_control`{.interpreted-text role="setting"}
  `CELERYD_SEND_EVENTS`                `worker_send_task_events`{.interpreted-text role="setting"}

You can see a full table of the changes in
`conf-old-settings-map`{.interpreted-text role="ref"}.

### Json is now the default serializer

The time has finally come to end the reign of `pickle`{.interpreted-text
role="mod"} as the default serialization mechanism, and json is the
default serializer starting from this version.

This change was `announced with the release of Celery 3.1
<last-version-to-enable-pickle>`{.interpreted-text role="ref"}.

If you\'re still depending on `pickle`{.interpreted-text role="mod"}
being the default serializer, then you have to configure your app before
upgrading to 4.0:

``` python
task_serializer = 'pickle'
result_serializer = 'pickle'
accept_content = {'pickle'}
```

The Json serializer now also supports some additional types:

-   `~datetime.datetime`{.interpreted-text role="class"},
    `~datetime.time`{.interpreted-text role="class"},
    `~datetime.date`{.interpreted-text role="class"}

    > Converted to json text, in ISO-8601 format.

-   `~decimal.Decimal`{.interpreted-text role="class"}

    > Converted to json text.

-   `django.utils.functional.Promise`{.interpreted-text role="class"}

    > Django only: Lazy strings used for translation etc., are evaluated
    > and conversion to a json type is attempted.

-   `uuid.UUID`{.interpreted-text role="class"}

    > Converted to json text.

You can also define a `__json__` method on your custom classes to
support JSON serialization (must return a json compatible type):

``` python
class Person:
    first_name = None
    last_name = None
    address = None

    def __json__(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
        }
```

### The Task base class no longer automatically register tasks

The `~@Task`{.interpreted-text role="class"} class is no longer using a
special meta-class that automatically registers the task in the task
registry.

Instead this is now handled by the `@task`{.interpreted-text
role="class"} decorators.

If you\'re still using class based tasks, then you need to register
these manually:

``` python
class CustomTask(Task):
    def run(self):
        print('running')
CustomTask = app.register_task(CustomTask())
```

The best practice is to use custom task classes only for overriding
general behavior, and then using the task decorator to realize the task:

``` python
@app.task(bind=True, base=CustomTask)
def custom(self):
    print('running')
```

This change also means that the `abstract` attribute of the task no
longer has any effect.

### Task argument checking {#v400-typing}

The arguments of the task are now verified when calling the task, even
asynchronously:

``` pycon
>>> @app.task
... def add(x, y):
...     return x + y

>>> add.delay(8, 8)
<AsyncResult: f59d71ca-1549-43e0-be41-4e8821a83c0c>

>>> add.delay(8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "celery/app/task.py", line 376, in delay
    return self.apply_async(args, kwargs)
  File "celery/app/task.py", line 485, in apply_async
    check_arguments(*(args or ()), **(kwargs or {}))
TypeError: add() takes exactly 2 arguments (1 given)
```

You can disable the argument checking for any task by setting its
`~@Task.typing`{.interpreted-text role="attr"} attribute to
`False`{.interpreted-text role="const"}:

``` pycon
>>> @app.task(typing=False)
... def add(x, y):
...     return x + y
```

Or if you would like to disable this completely for all tasks you can
pass `strict_typing=False` when creating the app:

``` python
app = Celery(..., strict_typing=False)
```

### Redis Events not backward compatible

The Redis `fanout_patterns` and `fanout_prefix` transport options are
now enabled by default.

Workers/monitors without these flags enabled won\'t be able to see
workers with this flag disabled. They can still execute tasks, but they
cannot receive each others monitoring messages.

You can upgrade in a backward compatible manner by first configuring
your 3.1 workers and monitors to enable the settings, before the final
upgrade to 4.0:

``` python
BROKER_TRANSPORT_OPTIONS = {
    'fanout_patterns': True,
    'fanout_prefix': True,
}
```

### Redis Priorities Reversed

Priority 0 is now lowest, 9 is highest.

This change was made to make priority support consistent with how it
works in AMQP.

Contributed by **Alex Koshelev**.

### Django: Auto-discover now supports Django app configurations

The `autodiscover_tasks()` function can now be called without arguments,
and the Django handler will automatically find your installed apps:

``` python
app.autodiscover_tasks()
```

The Django integration `example in the documentation
<django-first-steps>`{.interpreted-text role="ref"} has been updated to
use the argument-less call.

This also ensures compatibility with the new, ehm, `AppConfig` stuff
introduced in recent Django versions.

### Worker direct queues no longer use auto-delete

Workers/clients running 4.0 will no longer be able to send worker direct
messages to workers running older versions, and vice versa.

If you\'re relying on worker direct messages you should upgrade your 3.x
workers and clients to use the new routing settings first, by replacing
`celery.utils.worker_direct`{.interpreted-text role="func"} with this
implementation:

``` python
from kombu import Exchange, Queue

worker_direct_exchange = Exchange('C.dq2')

def worker_direct(hostname):
    return Queue(
        '{hostname}.dq2'.format(hostname),
        exchange=worker_direct_exchange,
        routing_key=hostname,
    )
```

This feature closed Issue #2492.

### Old command-line programs removed

Installing Celery will no longer install the `celeryd`, `celerybeat` and
`celeryd-multi` programs.

This was announced with the release of Celery 3.1, but you may still
have scripts pointing to the old names, so make sure you update these to
use the new umbrella command:

  -----------------------------------------------------------------------
  Program             New Status     Replacement
  ------------------- -------------- ------------------------------------
  `celeryd`           **REMOVED**    `celery worker`{.interpreted-text
                                     role="program"}

  `celerybeat`        **REMOVED**    `celery beat`{.interpreted-text
                                     role="program"}

  `celeryd-multi`     **REMOVED**    `celery multi`{.interpreted-text
                                     role="program"}
  -----------------------------------------------------------------------

## News {#v400-news}

### New protocol highlights

The new protocol fixes many problems with the old one, and enables some
long-requested features:

-   Most of the data are now sent as message headers, instead of being
    serialized with the message body.

    > In version 1 of the protocol the worker always had to deserialize
    > the message to be able to read task meta-data like the task id,
    > name, etc. This also meant that the worker was forced to
    > double-decode the data, first deserializing the message on
    > receipt, serializing the message again to send to child process,
    > then finally the child process deserializes the message again.
    >
    > Keeping the meta-data fields in the message headers means the
    > worker doesn\'t actually have to decode the payload before
    > delivering the task to the child process, and also that it\'s now
    > possible for the worker to reroute a task written in a language
    > different from Python to a different worker.

-   A new `lang` message header can be used to specify the programming
    language the task is written in.

-   Worker stores results for internal errors like `ContentDisallowed`,
    and other deserialization errors.

-   Worker stores results and sends monitoring events for unregistered
    task errors.

-   Worker calls callbacks/errbacks even when the result is sent by the
    parent process (e.g., `WorkerLostError`{.interpreted-text
    role="exc"} when a child process terminates, deserialization errors,
    unregistered tasks).

-   A new `origin` header contains information about the process sending
    the task (worker node-name, or PID and host-name information).

-   A new `shadow` header allows you to modify the task name used in
    logs.

    > This is useful for dispatch like patterns, like a task that calls
    > any function using pickle (don\'t do this at home):
    >
    > ``` python
    > from celery import Task
    > from celery.utils.imports import qualname
    >
    > class call_as_task(Task):
    >
    >     def shadow_name(self, args, kwargs, options):
    >         return 'call_as_task:{0}'.format(qualname(args[0]))
    >
    >     def run(self, fun, *args, **kwargs):
    >         return fun(*args, **kwargs)
    > call_as_task = app.register_task(call_as_task())
    > ```

-   New `argsrepr` and `kwargsrepr` fields contain textual
    representations of the task arguments (possibly truncated) for use
    in logs, monitors, etc.

    > This means the worker doesn\'t have to deserialize the message
    > payload to display the task arguments for informational purposes.

-   Chains now use a dedicated `chain` field enabling support for chains
    of thousands and more tasks.

-   New `parent_id` and `root_id` headers adds information about a tasks
    relationship with other tasks.

    > -   `parent_id` is the task id of the task that called this task
    > -   `root_id` is the first task in the work-flow.
    >
    > These fields can be used to improve monitors like flower to group
    > related messages together (like chains, groups, chords, complete
    > work-flows, etc).

-   `app.TaskProducer` replaced by
    `@amqp.create_task_message`{.interpreted-text role="meth"} and
    `@amqp.send_task_message`{.interpreted-text role="meth"}.

    > Dividing the responsibilities into creating and sending means that
    > people who want to send messages using a Python AMQP client
    > directly, don\'t have to implement the protocol.
    >
    > The `@amqp.create_task_message`{.interpreted-text role="meth"}
    > method calls either `@amqp.as_task_v2`{.interpreted-text
    > role="meth"}, or `@amqp.as_task_v1`{.interpreted-text role="meth"}
    > depending on the configured task protocol, and returns a special
    > `~celery.app.amqp.task_message`{.interpreted-text role="class"}
    > tuple containing the headers, properties and body of the task
    > message.

::: seealso
The new task protocol is documented in full here:
`message-protocol-task-v2`{.interpreted-text role="ref"}.
:::

### Prefork Pool Improvements

#### Tasks now log from the child process

Logging of task success/failure now happens from the child process
executing the task. As a result logging utilities, like Sentry can get
full information about tasks, including variables in the traceback
stack.

#### `-Ofair` is now the default scheduling strategy

To re-enable the default behavior in 3.1 use the `-Ofast` command-line
option.

There\'s been lots of confusion about what the `-Ofair` command-line
option does, and using the term \"prefetch\" in explanations have
probably not helped given how confusing this terminology is in AMQP.

When a Celery worker using the prefork pool receives a task, it needs to
delegate that task to a child process for execution.

The prefork pool has a configurable number of child processes
(`--concurrency`) that can be used to execute tasks, and each child
process uses pipes/sockets to communicate with the parent process:

-   inqueue (pipe/socket): parent sends task to the child process
-   outqueue (pipe/socket): child sends result/return value to the
    parent.

In Celery 3.1 the default scheduling mechanism was simply to send the
task to the first `inqueue` that was writable, with some heuristics to
make sure we round-robin between them to ensure each child process would
receive the same amount of tasks.

This means that in the default scheduling strategy, a worker may send
tasks to the same child process that is already executing a task. If
that task is long running, it may block the waiting task for a long
time. Even worse, hundreds of short-running tasks may be stuck behind a
long running task even when there are child processes free to do work.

The `-Ofair` scheduling strategy was added to avoid this situation, and
when enabled it adds the rule that no task should be sent to the a child
process that is already executing a task.

The fair scheduling strategy may perform slightly worse if you have only
short running tasks.

#### Limit child process resident memory size

You can now limit the maximum amount of memory allocated per prefork
pool child process by setting the worker
`--max-memory-per-child <celery worker --max-memory-per-child>`{.interpreted-text
role="option"} option, or the
`worker_max_memory_per_child`{.interpreted-text role="setting"} setting.

The limit is for RSS/resident memory size and is specified in kilobytes.

A child process having exceeded the limit will be terminated and
replaced with a new process after the currently executing task returns.

See `worker-max-memory-per-child`{.interpreted-text role="ref"} for more
information.

Contributed by **Dave Smith**.

#### One log-file per child process

Init-scrips and `celery multi`{.interpreted-text role="program"} now
uses the [%I]{.title-ref} log file format option (e.g.,
`/var/log/celery/%n%I.log`{.interpreted-text role="file"}).

This change was necessary to ensure each child process has a separate
log file after moving task logging to the child process, as multiple
processes writing to the same log file can cause corruption.

You\'re encouraged to upgrade your init-scripts and
`celery multi`{.interpreted-text role="program"} arguments to use this
new option.

### Transports

#### RabbitMQ priority queue support

See `routing-options-rabbitmq-priorities`{.interpreted-text role="ref"}
for more information.

Contributed by **Gerald Manipon**.

#### Configure broker URL for read/write separately

New `broker_read_url`{.interpreted-text role="setting"} and
`broker_write_url`{.interpreted-text role="setting"} settings have been
added so that separate broker URLs can be provided for connections used
for consuming/publishing.

In addition to the configuration options, two new methods have been
added the app API:

> -   `app.connection_for_read()`
> -   `app.connection_for_write()`

These should now be used in place of `app.connection()` to specify the
intent of the required connection.

::: note
::: title
Note
:::

Two connection pools are available: `app.pool` (read), and
`app.producer_pool` (write). The latter doesn\'t actually give
connections but full `kombu.Producer`{.interpreted-text role="class"}
instances.

``` python
def publish_some_message(app, producer=None):
    with app.producer_or_acquire(producer) as producer:
        ...

def consume_messages(app, connection=None):
    with app.connection_or_acquire(connection) as connection:
        ...
```
:::

#### RabbitMQ queue extensions support

Queue declarations can now set a message TTL and queue expiry time
directly, by using the `message_ttl` and `expires` arguments

New arguments have been added to `~kombu.Queue`{.interpreted-text
role="class"} that lets you directly and conveniently configure RabbitMQ
queue extensions in queue declarations:

-   `Queue(expires=20.0)`

    > Set queue expiry time in float seconds.
    >
    > See `kombu.Queue.expires`{.interpreted-text role="attr"}.

-   `Queue(message_ttl=30.0)`

    > Set queue message time-to-live float seconds.
    >
    > See `kombu.Queue.message_ttl`{.interpreted-text role="attr"}.

-   `Queue(max_length=1000)`

    > Set queue max length (number of messages) as int.
    >
    > See `kombu.Queue.max_length`{.interpreted-text role="attr"}.

-   `Queue(max_length_bytes=1000)`

    > Set queue max length (message size total in bytes) as int.
    >
    > See `kombu.Queue.max_length_bytes`{.interpreted-text role="attr"}.

-   `Queue(max_priority=10)`

    > Declare queue to be a priority queue that routes messages based on
    > the `priority` field of the message.
    >
    > See `kombu.Queue.max_priority`{.interpreted-text role="attr"}.

#### Amazon SQS transport now officially supported

The SQS broker transport has been rewritten to use async I/O and as such
joins RabbitMQ, Redis and QPid as officially supported transports.

The new implementation also takes advantage of long polling, and closes
several issues related to using SQS as a broker.

This work was sponsored by Nextdoor.

#### Apache QPid transport now officially supported

Contributed by **Brian Bouterse**.

### Redis: Support for Sentinel

You can point the connection to a list of sentinel URLs like:

``` text
sentinel://0.0.0.0:26379;sentinel://0.0.0.0:26380/...
```

where each sentinel is separated by a [;]{.title-ref}. Multiple
sentinels are handled by `kombu.Connection`{.interpreted-text
role="class"} constructor, and placed in the alternative list of servers
to connect to in case of connection failure.

Contributed by **Sergey Azovskov**, and **Lorenzo Mancini**.

### Tasks

#### Task Auto-retry Decorator

Writing custom retry handling for exception events is so common that we
now have built-in support for it.

For this a new `autoretry_for` argument is now supported by the task
decorators, where you can specify a tuple of exceptions to automatically
retry for:

``` python
from twitter.exceptions import FailWhaleError

@app.task(autoretry_for=(FailWhaleError,))
def refresh_timeline(user):
    return twitter.refresh_timeline(user)
```

See `task-autoretry`{.interpreted-text role="ref"} for more information.

Contributed by **Dmitry Malinovsky**.

#### `Task.replace` Improvements

-   `self.replace(signature)` can now replace any task, chord or group,
    and the signature to replace with can be a chord, group or any other
    type of signature.

-   No longer inherits the callbacks and errbacks of the existing task.

    > If you replace a node in a tree, then you wouldn\'t expect the new
    > node to inherit the children of the old node.

-   `Task.replace_in_chord` has been removed, use `.replace` instead.

-   If the replacement is a group, that group will be automatically
    converted to a chord, where the callback \"accumulates\" the results
    of the group tasks.

    > A new built-in task ([celery.accumulate]{.title-ref} was added for
    > this purpose)

Contributed by **Steeve Morin**, and **Ask Solem**.

#### Remote Task Tracebacks

The new `task_remote_tracebacks`{.interpreted-text role="setting"} will
make task tracebacks more useful by injecting the stack of the remote
worker.

This feature requires the additional `tblib`{.interpreted-text
role="pypi"} library.

Contributed by **Ionel Cristian Mărieș**.

#### Handling task connection errors

Connection related errors occurring while sending a task is now
re-raised as a `kombu.exceptions.OperationalError`{.interpreted-text
role="exc"} error:

``` pycon
>>> try:
...     add.delay(2, 2)
... except add.OperationalError as exc:
...     print('Could not send task %r: %r' % (add, exc))
```

See `calling-connection-errors`{.interpreted-text role="ref"} for more
information.

#### Gevent/Eventlet: Dedicated thread for consuming results

When using `gevent`{.interpreted-text role="pypi"}, or
`eventlet`{.interpreted-text role="pypi"} there is now a single thread
responsible for consuming events.

This means that if you have many calls retrieving results, there will be
a dedicated thread for consuming them:

``` python
result = add.delay(2, 2)

# this call will delegate to the result consumer thread:
#   once the consumer thread has received the result this greenlet can
# continue.
value = result.get(timeout=3)
```

This makes performing RPC calls when using gevent/eventlet perform much
better.

#### `AsyncResult.then(on_success, on_error)`

The AsyncResult API has been extended to support the
`~vine.promise`{.interpreted-text role="class"} protocol.

This currently only works with the RPC (amqp) and Redis result backends,
but lets you attach callbacks to when tasks finish:

``` python
import gevent.monkey
monkey.patch_all()

import time
from celery import Celery

app = Celery(broker='amqp://', backend='rpc')

@app.task
def add(x, y):
    return x + y

def on_result_ready(result):
    print('Received result for id %r: %r' % (result.id, result.result,))

add.delay(2, 2).then(on_result_ready)

time.sleep(3)  # run gevent event loop for a while.
```

Demonstrated using `gevent`{.interpreted-text role="pypi"} here, but
really this is an API that\'s more useful in callback-based event loops
like `twisted`{.interpreted-text role="pypi"}, or
`tornado`{.interpreted-text role="pypi"}.

#### New Task Router API

The `task_routes`{.interpreted-text role="setting"} setting can now hold
functions, and map routes now support glob patterns and regexes.

Instead of using router classes you can now simply define a function:

``` python
def route_for_task(name, args, kwargs, options, task=None, **kwargs):
    from proj import tasks

    if name == tasks.add.name:
        return {'queue': 'hipri'}
```

If you don\'t need the arguments you can use start arguments, just make
sure you always also accept star arguments so that we have the ability
to add more features in the future:

``` python
def route_for_task(name, *args, **kwargs):
    from proj import tasks
    if name == tasks.add.name:
        return {'queue': 'hipri', 'priority': 9}
```

Both the `options` argument and the new `task` keyword argument are new
to the function-style routers, and will make it easier to write routers
based on execution options, or properties of the task.

The optional `task` keyword argument won\'t be set if a task is called
by name using `@send_task`{.interpreted-text role="meth"}.

For more examples, including using glob/regexes in routers please see
`task_routes`{.interpreted-text role="setting"} and
`routing-automatic`{.interpreted-text role="ref"}.

#### Canvas Refactor

The canvas/work-flow implementation have been heavily refactored to fix
some long outstanding issues.

-   Error callbacks can now take real exception and traceback instances
    (Issue #2538).

    > ``` pycon
    > >>> add.s(2, 2).on_error(log_error.s()).delay()
    > ```
    >
    > Where `log_error` could be defined as:
    >
    > ``` python
    > @app.task
    > def log_error(request, exc, traceback):
    >     with open(os.path.join('/var/errors', request.id), 'a') as fh:
    >         print('--\n\n{0} {1} {2}'.format(
    >             task_id, exc, traceback), file=fh)
    > ```
    >
    > See `guide-canvas`{.interpreted-text role="ref"} for more
    > examples.

-   `chain(a, b, c)` now works the same as `a | b | c`.

    > This means chain may no longer return an instance of `chain`,
    > instead it may optimize the workflow so that e.g. two groups
    > chained together becomes one group.

-   Now unrolls groups within groups into a single group (Issue #1509).

-   chunks/map/starmap tasks now routes based on the target task

-   chords and chains can now be immutable.

-   Fixed bug where serialized signatures weren\'t converted back into
    signatures (Issue #2078)

    > Fix contributed by **Ross Deane**.

-   Fixed problem where chains and groups didn\'t work when using JSON
    serialization (Issue #2076).

    > Fix contributed by **Ross Deane**.

-   Creating a chord no longer results in multiple values for keyword
    argument \'task_id\' (Issue #2225).

    > Fix contributed by **Aneil Mallavarapu**.

-   Fixed issue where the wrong result is returned when a chain contains
    a chord as the penultimate task.

    > Fix contributed by **Aneil Mallavarapu**.

-   Special case of `group(A.s() | group(B.s() | C.s()))` now works.

-   Chain: Fixed bug with incorrect id set when a subtask is also a
    chain.

-   `group | group` is now flattened into a single group (Issue #2573).

-   Fixed issue where `group | task` wasn\'t upgrading correctly to
    chord (Issue #2922).

-   Chords now properly sets `result.parent` links.

-   `chunks`/`map`/`starmap` are now routed based on the target task.

-   

    `Signature.link` now works when argument is scalar (not a list)

    :   (Issue #2019).

-   `group()` now properly forwards keyword arguments (Issue #3426).

    > Fix contributed by **Samuel Giffard**.

-   A `chord` where the header group only consists of a single task is
    now turned into a simple chain.

-   Passing a `link` argument to `group.apply_async()` now raises an
    error (Issue #3508).

-   `chord | sig` now attaches to the chord callback (Issue #3356).

### Periodic Tasks

#### New API for configuring periodic tasks

This new API enables you to use signatures when defining periodic tasks,
removing the chance of mistyping task names.

An example of the new API is `here <beat-entries>`{.interpreted-text
role="ref"}.

#### Optimized Beat implementation

The `celery beat`{.interpreted-text role="program"} implementation has
been optimized for millions of periodic tasks by using a heap to
schedule entries.

Contributed by **Ask Solem** and **Alexander Koshelev**.

#### Schedule tasks based on sunrise, sunset, dawn and dusk

See `beat-solar`{.interpreted-text role="ref"} for more information.

Contributed by **Mark Parncutt**.

### Result Backends

#### RPC Result Backend matured

Lots of bugs in the previously experimental RPC result backend have been
fixed and can now be considered to production use.

Contributed by **Ask Solem**, **Morris Tweed**.

#### Redis: Result backend optimizations

##### `result.get()` is now using pub/sub for streaming task results

Calling `result.get()` when using the Redis result backend used to be
extremely expensive as it was using polling to wait for the result to
become available. A default polling interval of 0.5 seconds didn\'t help
performance, but was necessary to avoid a spin loop.

The new implementation is using Redis Pub/Sub mechanisms to publish and
retrieve results immediately, greatly improving task round-trip times.

Contributed by **Yaroslav Zhavoronkov** and **Ask Solem**.

##### New optimized chord join implementation

This was an experimental feature introduced in Celery 3.1, that could
only be enabled by adding `?new_join=1` to the result backend URL
configuration.

We feel that the implementation has been tested thoroughly enough to be
considered stable and enabled by default.

The new implementation greatly reduces the overhead of chords, and
especially with larger chords the performance benefit can be massive.

#### New Riak result backend introduced

See `conf-riak-result-backend`{.interpreted-text role="ref"} for more
information.

Contributed by **Gilles Dartiguelongue**, **Alman One** and **NoKriK**.

#### New CouchDB result backend introduced

See `conf-couchdb-result-backend`{.interpreted-text role="ref"} for more
information.

Contributed by **Nathan Van Gheem**.

#### New Consul result backend introduced

Add support for Consul as a backend using the Key/Value store of Consul.

Consul has an HTTP API where through you can store keys with their
values.

The backend extends KeyValueStoreBackend and implements most of the
methods.

Mainly to set, get and remove objects.

This allows Celery to store Task results in the K/V store of Consul.

Consul also allows to set a TTL on keys using the Sessions from Consul.
This way the backend supports auto expiry of Task results.

For more information on Consul visit <https://consul.io/>

The backend uses `python-consul`{.interpreted-text role="pypi"} for
talking to the HTTP API. This package is fully Python 3 compliant just
as this backend is:

``` console
$ pip install python-consul
```

That installs the required package to talk to Consul\'s HTTP API from
Python.

You can also specify consul as an extension in your dependency on
Celery:

``` console
$ pip install celery[consul]
```

See `bundles`{.interpreted-text role="ref"} for more information.

Contributed by **Wido den Hollander**.

#### Brand new Cassandra result backend

A brand new Cassandra backend utilizing the new
`cassandra-driver`{.interpreted-text role="pypi"} library is replacing
the old result backend using the older `pycassa`{.interpreted-text
role="pypi"} library.

See `conf-cassandra-result-backend`{.interpreted-text role="ref"} for
more information.

To depend on Celery with Cassandra as the result backend use:

``` console
$ pip install celery[cassandra]
```

You can also combine multiple extension requirements, please see
`bundles`{.interpreted-text role="ref"} for more information.

#### New Elasticsearch result backend introduced

See `conf-elasticsearch-result-backend`{.interpreted-text role="ref"}
for more information.

To depend on Celery with Elasticsearch as the result backend use:

``` console
$ pip install celery[elasticsearch]
```

You can also combine multiple extension requirements, please see
`bundles`{.interpreted-text role="ref"} for more information.

Contributed by **Ahmet Demir**.

#### New File-system result backend introduced

See `conf-filesystem-result-backend`{.interpreted-text role="ref"} for
more information.

Contributed by **Môshe van der Sterre**.

### Event Batching

Events are now buffered in the worker and sent as a list, reducing the
overhead required to send monitoring events.

For authors of custom event monitors there will be no action required as
long as you\'re using the Python Celery helpers
(`~@events.Receiver`{.interpreted-text role="class"}) to implement your
monitor.

However, if you\'re parsing raw event messages you must now account for
batched event messages, as they differ from normal event messages in the
following way:

-   The routing key for a batch of event messages will be set to
    `<event-group>.multi` where the only batched event group is
    currently `task` (giving a routing key of `task.multi`).
-   The message body will be a serialized list-of-dictionaries instead
    of a dictionary. Each item in the list can be regarded as a normal
    event message body.

### In Other News\...

#### Requirements

-   Now depends on `Kombu 4.0 <kombu:version-4.0>`{.interpreted-text
    role="ref"}.
-   Now depends on `billiard`{.interpreted-text role="pypi"} version
    3.5.
-   No longer depends on `anyjson`{.interpreted-text role="pypi"}.
    Good-bye old friend :(

#### Tasks

-   The \"anon-exchange\" is now used for simple name-name direct
    routing.

    This increases performance as it completely bypasses the routing
    table, in addition it also improves reliability for the Redis broker
    transport.

-   An empty ResultSet now evaluates to True.

    > Fix contributed by **Colin McIntosh**.

-   The default routing key
    (`task_default_routing_key`{.interpreted-text role="setting"}) and
    exchange name (`task_default_exchange`{.interpreted-text
    role="setting"}) is now taken from the
    `task_default_queue`{.interpreted-text role="setting"} setting.

    > This means that to change the name of the default queue, you now
    > only have to set a single setting.

-   New `task_reject_on_worker_lost`{.interpreted-text role="setting"}
    setting, and `~@Task.reject_on_worker_lost`{.interpreted-text
    role="attr"} task attribute decides what happens when the child
    worker process executing a late ack task is terminated.

    > Contributed by **Michael Permana**.

-   `Task.subtask` renamed to `Task.signature` with alias.

-   `Task.subtask_from_request` renamed to `Task.signature_from_request`
    with alias.

-   The `delivery_mode` attribute for `kombu.Queue`{.interpreted-text
    role="class"} is now respected (Issue #1953).

-   Routes in `task-routes`{.interpreted-text role="setting"} can now
    specify a `~kombu.Queue`{.interpreted-text role="class"} instance
    directly.

    > Example:
    >
    > ``` python
    > task_routes = {'proj.tasks.add': {'queue': Queue('add')}}
    > ```

-   `AsyncResult` now raises `ValueError`{.interpreted-text role="exc"}
    if task_id is None. (Issue #1996).

-   Retried tasks didn\'t forward expires setting (Issue #3297).

-   `result.get()` now supports an `on_message` argument to set a
    callback to be called for every message received.

-   New abstract classes added:

    > -   `~celery.utils.abstract.CallableTask`{.interpreted-text
    >     role="class"}
    >
    >     > Looks like a task.
    >
    > -   `~celery.utils.abstract.CallableSignature`{.interpreted-text
    >     role="class"}
    >
    >     > Looks like a task signature.

-   `Task.replace` now properly forwards callbacks (Issue #2722).

    > Fix contributed by **Nicolas Unravel**.

-   `Task.replace`: Append to chain/chord (Closes #3232)

    > Fixed issue #3232, adding the signature to the chain (if there\'s
    > any). Fixed the chord suppress if the given signature contains
    > one.
    >
    > Fix contributed by `honux`{.interpreted-text role="github_user"}.

-   Task retry now also throws in eager mode.

    > Fix contributed by **Feanil Patel**.

#### Beat

-   Fixed crontab infinite loop with invalid date.

    > When occurrence can never be reached (example, April, 31th),
    > trying to reach the next occurrence would trigger an infinite
    > loop.
    >
    > Try fixing that by raising a `RuntimeError`{.interpreted-text
    > role="exc"} after 2,000 iterations
    >
    > (Also added a test for crontab leap years in the process)
    >
    > Fix contributed by **Romuald Brunet**.

-   Now ensures the program exits with a non-zero exit code when an
    exception terminates the service.

    > Fix contributed by **Simon Peeters**.

#### App

-   Dates are now always timezone aware even if
    `enable_utc`{.interpreted-text role="setting"} is disabled (Issue
    #943).

    > Fix contributed by **Omer Katz**.

-   **Config**: App preconfiguration is now also pickled with the
    configuration.

    > Fix contributed by **Jeremy Zafran**.

-   

    The application can now change how task names are generated using

    :   the `~@gen_task_name`{.interpreted-text role="meth"} method.

        Contributed by **Dmitry Malinovsky**.

-   App has new `app.current_worker_task` property that returns the task
    that\'s currently being worked on (or `None`{.interpreted-text
    role="const"}). (Issue #2100).

#### Logging

-   `~celery.utils.log.get_task_logger`{.interpreted-text role="func"}
    now raises an exception if trying to use the name \"celery\" or
    \"celery.task\" (Issue #3475).

#### Execution Pools

-   **Eventlet/Gevent**: now enables AMQP heartbeat (Issue #3338).

-   **Eventlet/Gevent**: Fixed race condition leading to \"simultaneous
    read\" errors (Issue #2755).

-   **Prefork**: Prefork pool now uses `poll` instead of `select` where
    available (Issue #2373).

-   **Prefork**: Fixed bug where the pool would refuse to shut down the
    worker (Issue #2606).

-   **Eventlet**: Now returns pool size in
    `celery inspect stats`{.interpreted-text role="program"} command.

    > Contributed by **Alexander Oblovatniy**.

### Testing

-   Celery is now a `pytest`{.interpreted-text role="pypi"} plugin,
    including fixtures useful for unit and integration testing.

    > See the `testing user guide <testing>`{.interpreted-text
    > role="ref"} for more information.

#### Transports

-   `amqps://` can now be specified to require SSL.

-   **Redis Transport**: The Redis transport now supports the
    `broker_use_ssl`{.interpreted-text role="setting"} option.

    > Contributed by **Robert Kolba**.

-   JSON serializer now calls `obj.__json__` for unsupported types.

    > This means you can now define a `__json__` method for custom types
    > that can be reduced down to a built-in json type.
    >
    > Example:
    >
    > ``` python
    > class Person:
    >     first_name = None
    >     last_name = None
    >     address = None
    >
    >     def __json__(self):
    >         return {
    >             'first_name': self.first_name,
    >             'last_name': self.last_name,
    >             'address': self.address,
    >         }
    > ```

-   JSON serializer now handles datetime\'s, Django promise, UUID and
    Decimal.

-   New `Queue.consumer_arguments` can be used for the ability to set
    consumer priority via `x-priority`.

    See <https://www.rabbitmq.com/consumer-priority.html>

    Example:

    ``` python
    consumer = Consumer(channel, consumer_arguments={'x-priority': 3})
    ```

-   Queue/Exchange: `no_declare` option added (also enabled for internal
    amq. exchanges).

#### Programs

-   Celery is now using `argparse`{.interpreted-text role="mod"},
    instead of `optparse`{.interpreted-text role="mod"}.

-   All programs now disable colors if the controlling terminal is not a
    TTY.

-   `celery worker`{.interpreted-text role="program"}: The `-q` argument
    now disables the startup banner.

-   `celery worker`{.interpreted-text role="program"}: The \"worker
    ready\" message is now logged using severity info, instead of warn.

-   `celery multi`{.interpreted-text role="program"}: `%n` format for is
    now synonym with `%N` to be consistent with
    `celery worker`{.interpreted-text role="program"}.

-   `celery inspect`{.interpreted-text
    role="program"}/`celery control`{.interpreted-text role="program"}:
    now supports a new
    `--json <celery inspect --json>`{.interpreted-text role="option"}
    option to give output in json format.

-   `celery inspect registered`{.interpreted-text role="program"}: now
    ignores built-in tasks.

-   `celery purge`{.interpreted-text role="program"} now takes `-Q` and
    `-X` options used to specify what queues to include and exclude from
    the purge.

-   New `celery logtool`{.interpreted-text role="program"}: Utility for
    filtering and parsing celery worker log-files

-   `celery multi`{.interpreted-text role="program"}: now passes through
    [%i]{.title-ref} and [%I]{.title-ref} log file formats.

-   General: `%p` can now be used to expand to the full worker node-name
    in log-file/pid-file arguments.

-   

    A new command line option

    :   `--executable <celery worker --executable>`{.interpreted-text
        role="option"} is now available for daemonizing programs
        (`celery worker`{.interpreted-text role="program"} and
        `celery beat`{.interpreted-text role="program"}).

        > Contributed by **Bert Vanderbauwhede**.

-   `celery worker`{.interpreted-text role="program"}: supports new
    `--prefetch-multiplier <celery worker --prefetch-multiplier>`{.interpreted-text
    role="option"} option.

    > Contributed by **Mickaël Penhard**.

-   The `--loader` argument is now always effective even if an app
    argument is set (Issue #3405).

-   inspect/control now takes commands from registry

    > This means user remote-control commands can also be used from the
    > command-line.
    >
    > Note that you need to specify the arguments/and type of arguments
    > for the arguments to be correctly passed on the command-line.
    >
    > There are now two decorators, which use depends on the type of
    > command: [\@inspect_command]{.title-ref} + \`@control_command\`:
    >
    > ``` python
    > from celery.worker.control import control_command
    >
    > @control_command(
    >     args=[('n', int)]
    >     signature='[N=1]',
    > )
    > def something(state, n=1, **kwargs):
    >     ...
    > ```
    >
    > Here `args` is a list of args supported by the command. The list
    > must contain tuples of `(argument_name, type)`.
    >
    > `signature` is just the command-line help used in e.g.
    > `celery -A proj control --help`.
    >
    > Commands also support [variadic]{.title-ref} arguments, which
    > means that any arguments left over will be added to a single
    > variable. Here demonstrated by the `terminate` command which takes
    > a signal argument and a variable number of task_ids:
    >
    > ``` python
    > from celery.worker.control import control_command
    >
    > @control_command(
    >     args=[('signal', str)],
    >     signature='<signal> [id1, [id2, [..., [idN]]]]',
    >     variadic='ids',
    > )
    > def terminate(state, signal, ids, **kwargs):
    >     ...
    > ```
    >
    > This command can now be called using:
    >
    > ``` console
    > $ celery -A proj control terminate SIGKILL id1 id2 id3`
    > ```
    >
    > See `worker-custom-control-commands`{.interpreted-text role="ref"}
    > for more information.

#### Worker

-   Improvements and fixes for
    `~celery.utils.collections.LimitedSet`{.interpreted-text
    role="class"}.

    > Getting rid of leaking memory + adding `minlen` size of the set:
    > the minimal residual size of the set after operating for some
    > time. `minlen` items are kept, even if they should\'ve been
    > expired.
    >
    > Problems with older and even more old code:
    >
    > 1.  Heap would tend to grow in some scenarios (like adding an item
    >     multiple times).
    > 2.  Adding many items fast wouldn\'t clean them soon enough (if
    >     ever).
    > 3.  When talking to other workers, revoked.\_data was sent, but it
    >     was processed on the other side as iterable. That means giving
    >     those keys new (current) time-stamp. By doing this workers
    >     could recycle items forever. Combined with 1) and 2), this
    >     means that in large set of workers, you\'re getting out of
    >     memory soon.
    >
    > All those problems should be fixed now.
    >
    > This should fix issues #3095, #3086.
    >
    > Contributed by **David Pravec**.

-   New settings to control remote control command queues.

    > -   `control_queue_expires`{.interpreted-text role="setting"}
    >
    >     > Set queue expiry time for both remote control command
    >     > queues, and remote control reply queues.
    >
    > -   `control_queue_ttl`{.interpreted-text role="setting"}
    >
    >     > Set message time-to-live for both remote control command
    >     > queues, and remote control reply queues.
    >
    > Contributed by **Alan Justino**.

-   The `worker_shutdown`{.interpreted-text role="signal"} signal is now
    always called during shutdown.

    > Previously it would not be called if the worker instance was
    > collected by gc first.

-   Worker now only starts the remote control command consumer if the
    broker transport used actually supports them.

-   Gossip now sets `x-message-ttl` for event queue to
    heartbeat_interval s. (Issue #2005).

-   Now preserves exit code (Issue #2024).

-   Now rejects messages with an invalid ETA value (instead of ack,
    which means they will be sent to the dead-letter exchange if one is
    configured).

-   Fixed crash when the `-purge` argument was used.

-   Log\--level for unrecoverable errors changed from `error` to
    `critical`.

-   Improved rate limiting accuracy.

-   Account for missing timezone information in task expires field.

    > Fix contributed by **Albert Wang**.

-   

    The worker no longer has a `Queues` bootsteps, as it is now

    :   superfluous.

-   Now emits the \"Received task\" line even for revoked tasks. (Issue
    #3155).

-   Now respects `broker_connection_retry`{.interpreted-text
    role="setting"} setting.

    > Fix contributed by **Nat Williams**.

-   New `control_queue_ttl`{.interpreted-text role="setting"} and
    `control_queue_expires`{.interpreted-text role="setting"} settings
    now enables you to configure remote control command message TTLs,
    and queue expiry time.

    > Contributed by **Alan Justino**.

-   New `celery.worker.state.requests`{.interpreted-text role="data"}
    enables O(1) loookup of active/reserved tasks by id.

-   Auto-scale didn\'t always update keep-alive when scaling down.

    > Fix contributed by **Philip Garnero**.

-   Fixed typo `options_list` -\> `option_list`.

    > Fix contributed by **Greg Wilbur**.

-   Some worker command-line arguments and `Worker()` class arguments
    have been renamed for consistency.

    > All of these have aliases for backward compatibility.
    >
    > -   `--send-events` -\> `--task-events`
    > -   `--schedule` -\> `--schedule-filename`
    > -   `--maxtasksperchild` -\> `--max-tasks-per-child`
    > -   `Beat(scheduler_cls=)` -\> `Beat(scheduler=)`
    > -   `Worker(send_events=True)` -\> `Worker(task_events=True)`
    > -   `Worker(task_time_limit=)` -\> `Worker(time_limit=`)
    > -   `Worker(task_soft_time_limit=)` -\> `Worker(soft_time_limit=)`
    > -   `Worker(state_db=)` -\> `Worker(statedb=)`
    > -   `Worker(working_directory=)` -\> `Worker(workdir=)`

#### Debugging Utilities

-   `celery.contrib.rdb`{.interpreted-text role="mod"}: Changed remote
    debugger banner so that you can copy and paste the address easily
    (no longer has a period in the address).

    > Contributed by **Jonathan Vanasco**.

-   Fixed compatibility with recent `psutil`{.interpreted-text
    role="pypi"} versions (Issue #3262).

#### Signals

-   **App**: New signals for app configuration/finalization:

    > -   `app.on_configure <@on_configure>`{.interpreted-text
    >     role="data"}
    > -   `app.on_after_configure <@on_after_configure>`{.interpreted-text
    >     role="data"}
    > -   `app.on_after_finalize <@on_after_finalize>`{.interpreted-text
    >     role="data"}

-   **Task**: New task signals for rejected task messages:

    > -   `celery.signals.task_rejected`{.interpreted-text role="data"}.
    > -   `celery.signals.task_unknown`{.interpreted-text role="data"}.

-   **Worker**: New signal for when a heartbeat event is sent.

    > -   `celery.signals.heartbeat_sent`{.interpreted-text role="data"}
    >
    >     > Contributed by **Kevin Richardson**.

#### Events

-   Event messages now uses the RabbitMQ `x-message-ttl` option to
    ensure older event messages are discarded.

    > The default is 5 seconds, but can be changed using the
    > `event_queue_ttl`{.interpreted-text role="setting"} setting.

-   `Task.send_event` now automatically retries sending the event on
    connection failure, according to the task publish retry settings.

-   Event monitors now sets the `event_queue_expires`{.interpreted-text
    role="setting"} setting by default.

    > The queues will now expire after 60 seconds after the monitor
    > stops consuming from it.

-   Fixed a bug where a None value wasn\'t handled properly.

    > Fix contributed by **Dongweiming**.

-   New `event_queue_prefix`{.interpreted-text role="setting"} setting
    can now be used to change the default `celeryev` queue prefix for
    event receiver queues.

    > Contributed by **Takeshi Kanemoto**.

-   `State.tasks_by_type` and `State.tasks_by_worker` can now be used as
    a mapping for fast access to this information.

#### Deployment

-   Generic init-scripts now support `CELERY_SU`{.interpreted-text
    role="envvar"} and `CELERYD_SU_ARGS`{.interpreted-text
    role="envvar"} environment variables to set the path and arguments
    for `su`{.interpreted-text role="command"}
    (`su(1)`{.interpreted-text role="manpage"}).

-   Generic init-scripts now better support FreeBSD and other BSD
    systems by searching `/usr/local/etc/`{.interpreted-text
    role="file"} for the configuration file.

    > Contributed by **Taha Jahangir**.

-   Generic init-script: Fixed strange bug for `celerybeat` where
    restart didn\'t always work (Issue #3018).

-   The systemd init script now uses a shell when executing services.

    > Contributed by **Tomas Machalek**.

#### Result Backends

-   Redis: Now has a default socket timeout of 120 seconds.

    > The default can be changed using the new
    > `redis_socket_timeout`{.interpreted-text role="setting"} setting.
    >
    > Contributed by **Raghuram Srinivasan**.

-   RPC Backend result queues are now auto delete by default (Issue
    #2001).

-   RPC Backend: Fixed problem where exception wasn\'t deserialized
    properly with the json serializer (Issue #2518).

    > Fix contributed by **Allard Hoeve**.

-   CouchDB: The backend used to double-json encode results.

    > Fix contributed by **Andrew Stewart**.

-   CouchDB: Fixed typo causing the backend to not be found (Issue
    #3287).

    > Fix contributed by **Andrew Stewart**.

-   MongoDB: Now supports setting the
    `result_serialzier`{.interpreted-text role="setting"} setting to
    `bson` to use the MongoDB libraries own serializer.

    > Contributed by **Davide Quarta**.

-   

    MongoDB: URI handling has been improved to use

    :   database name, user and password from the URI if provided.

        Contributed by **Samuel Jaillet**.

-   SQLAlchemy result backend: Now ignores all result engine options
    when using NullPool (Issue #1930).

-   SQLAlchemy result backend: Now sets max char size to 155 to deal
    with brain damaged MySQL Unicode implementation (Issue #1748).

-   **General**: All Celery exceptions/warnings now inherit from common
    `~celery.exceptions.CeleryError`{.interpreted-text
    role="class"}/`~celery.exceptions.CeleryWarning`{.interpreted-text
    role="class"}. (Issue #2643).

#### Documentation Improvements

Contributed by:

-   Adam Chainz
-   Amir Rustamzadeh
-   Arthur Vuillard
-   Batiste Bieler
-   Berker Peksag
-   Bryce Groff
-   Daniel Devine
-   Edward Betts
-   Jason Veatch
-   Jeff Widman
-   Maciej Obuchowski
-   Manuel Kaufmann
-   Maxime Beauchemin
-   Mitchel Humpherys
-   Pavlo Kapyshin
-   Pierre Fersing
-   Rik
-   Steven Sklar
-   Tayfun Sen
-   Wieland Hoffmann

## Reorganization, Deprecations, and Removals

### Incompatible changes

-   Prefork: Calling `result.get()` or joining any result from within a
    task now raises `RuntimeError`{.interpreted-text role="exc"}.

    > In previous versions this would emit a warning.

-   `celery.worker.consumer`{.interpreted-text role="mod"} is now a
    package, not a module.

-   Module `celery.worker.job` renamed to
    `celery.worker.request`{.interpreted-text role="mod"}.

-   Beat: `Scheduler.Publisher`/`.publisher` renamed to
    `.Producer`/`.producer`.

-   Result: The task_name argument/attribute of
    `@AsyncResult`{.interpreted-text role="class"} was removed.

    > This was historically a field used for `pickle`{.interpreted-text
    > role="mod"} compatibility, but is no longer needed.

-   Backends: Arguments named `status` renamed to `state`.

-   Backends: `backend.get_status()` renamed to `backend.get_state()`.

-   Backends: `backend.maybe_reraise()` renamed to `.maybe_throw()`

    > The promise API uses .throw(), so this change was made to make it
    > more consistent.
    >
    > There\'s an alias available, so you can still use maybe_reraise
    > until Celery 5.0.

### Unscheduled Removals {#v400-unscheduled-removals}

-   The experimental `celery.contrib.methods`{.interpreted-text
    role="mod"} feature has been removed, as there were far many bugs in
    the implementation to be useful.

-   The CentOS init-scripts have been removed.

    > These didn\'t really add any features over the generic
    > init-scripts, so you\'re encouraged to use them instead, or
    > something like `supervisor`{.interpreted-text role="pypi"}.

### Reorganization Deprecations {#v400-deprecations-reorg}

These symbols have been renamed, and while there\'s an alias available
in this version for backward compatibility, they will be removed in
Celery 5.0, so make sure you rename these ASAP to make sure it won\'t
break for that release.

Chances are that you\'ll only use the first in this list, but you never
know:

-   `celery.utils.worker_direct` -\>
    `celery.utils.nodenames.worker_direct`{.interpreted-text
    role="meth"}.
-   `celery.utils.nodename` -\>
    `celery.utils.nodenames.nodename`{.interpreted-text role="meth"}.
-   `celery.utils.anon_nodename` -\>
    `celery.utils.nodenames.anon_nodename`{.interpreted-text
    role="meth"}.
-   `celery.utils.nodesplit` -\>
    `celery.utils.nodenames.nodesplit`{.interpreted-text role="meth"}.
-   `celery.utils.default_nodename` -\>
    `celery.utils.nodenames.default_nodename`{.interpreted-text
    role="meth"}.
-   `celery.utils.node_format` -\>
    `celery.utils.nodenames.node_format`{.interpreted-text role="meth"}.
-   `celery.utils.host_format` -\>
    `celery.utils.nodenames.host_format`{.interpreted-text role="meth"}.

### Scheduled Removals {#v400-removals}

#### Modules

-   Module `celery.worker.job` has been renamed to
    `celery.worker.request`{.interpreted-text role="mod"}.

    > This was an internal module so shouldn\'t have any effect. It\'s
    > now part of the public API so must not change again.

-   Module `celery.task.trace` has been renamed to `celery.app.trace` as
    the `celery.task` package is being phased out. The module will be
    removed in version 5.0 so please change any import from:

        from celery.task.trace import X

    to:

        from celery.app.trace import X

-   Old compatibility aliases in the `celery.loaders`{.interpreted-text
    role="mod"} module has been removed.

    > -   Removed `celery.loaders.current_loader()`, use:
    >     `current_app.loader`
    > -   Removed `celery.loaders.load_settings()`, use:
    >     `current_app.conf`

#### Result

-   

    `AsyncResult.serializable()` and `celery.result.from_serializable`

    :   has been removed:

        Use instead:

        ``` pycon
        >>> tup = result.as_tuple()
        >>> from celery.result import result_from_tuple
        >>> result = result_from_tuple(tup)
        ```

-   Removed `BaseAsyncResult`, use `AsyncResult` for instance checks
    instead.

-   Removed `TaskSetResult`, use `GroupResult` instead.

    > -   `TaskSetResult.total` -\> `len(GroupResult)`
    > -   `TaskSetResult.taskset_id` -\> `GroupResult.id`

-   Removed `ResultSet.subtasks`, use `ResultSet.results` instead.

#### TaskSet

TaskSet has been removed, as it was replaced by the `group` construct in
Celery 3.0.

If you have code like this:

``` pycon
>>> from celery.task import TaskSet

>>> TaskSet(add.subtask((i, i)) for i in xrange(10)).apply_async()
```

You need to replace that with:

``` pycon
>>> from celery import group
>>> group(add.s(i, i) for i in xrange(10))()
```

#### Events

-   Removals for class `celery.events.state.Worker`{.interpreted-text
    role="class"}:

    > -   `Worker._defaults` attribute.
    >
    >     > Use `{k: getattr(worker, k) for k in worker._fields}`.
    >
    > -   `Worker.update_heartbeat`
    >
    >     > Use `Worker.event(None, timestamp, received)`
    >
    > -   `Worker.on_online`
    >
    >     > Use `Worker.event('online', timestamp, received, fields)`
    >
    > -   `Worker.on_offline`
    >
    >     > Use `Worker.event('offline', timestamp, received, fields)`
    >
    > -   `Worker.on_heartbeat`
    >
    >     > Use `Worker.event('heartbeat', timestamp, received, fields)`

-   Removals for class `celery.events.state.Task`{.interpreted-text
    role="class"}:

    > -   `Task._defaults` attribute.
    >
    >     > Use `{k: getattr(task, k) for k in task._fields}`.
    >
    > -   `Task.on_sent`
    >
    >     > Use `Worker.event('sent', timestamp, received, fields)`
    >
    > -   `Task.on_received`
    >
    >     > Use `Task.event('received', timestamp, received, fields)`
    >
    > -   `Task.on_started`
    >
    >     > Use `Task.event('started', timestamp, received, fields)`
    >
    > -   `Task.on_failed`
    >
    >     > Use `Task.event('failed', timestamp, received, fields)`
    >
    > -   `Task.on_retried`
    >
    >     > Use `Task.event('retried', timestamp, received, fields)`
    >
    > -   `Task.on_succeeded`
    >
    >     > Use `Task.event('succeeded', timestamp, received, fields)`
    >
    > -   `Task.on_revoked`
    >
    >     > Use `Task.event('revoked', timestamp, received, fields)`
    >
    > -   `Task.on_unknown_event`
    >
    >     > Use `Task.event(short_type, timestamp, received, fields)`
    >
    > -   `Task.update`
    >
    >     > Use `Task.event(short_type, timestamp, received, fields)`
    >
    > -   `Task.merge`
    >
    >     > Contact us if you need this.

#### Magic keyword arguments

Support for the very old magic keyword arguments accepted by tasks is
finally removed in this version.

If you\'re still using these you have to rewrite any task still using
the old `celery.decorators` module and depending on keyword arguments
being passed to the task, for example:

    from celery.decorators import task

    @task()
    def add(x, y, task_id=None):
        print('My task id is %r' % (task_id,))

should be rewritten into:

    from celery import task

    @task(bind=True)
    def add(self, x, y):
        print('My task id is {0.request.id}'.format(self))

### Removed Settings

The following settings have been removed, and is no longer supported:

#### Logging Settings

  **Setting name**         **Replace with**
  ------------------------ -------------------------------------------------------------
  `CELERYD_LOG_LEVEL`      `celery worker --loglevel`{.interpreted-text role="option"}
  `CELERYD_LOG_FILE`       `celery worker --logfile`{.interpreted-text role="option"}
  `CELERYBEAT_LOG_LEVEL`   `celery beat --loglevel`{.interpreted-text role="option"}
  `CELERYBEAT_LOG_FILE`    `celery beat --logfile`{.interpreted-text role="option"}
  `CELERYMON_LOG_LEVEL`    celerymon is deprecated, use flower
  `CELERYMON_LOG_FILE`     celerymon is deprecated, use flower
  `CELERYMON_LOG_FORMAT`   celerymon is deprecated, use flower

#### Task Settings

  **Setting name**            **Replace with**
  --------------------------- ------------------
  `CELERY_CHORD_PROPAGATES`   N/A

### Changes to internal API

-   Module `celery.datastructures` renamed to
    `celery.utils.collections`{.interpreted-text role="mod"}.

-   Module `celery.utils.timeutils` renamed to
    `celery.utils.time`{.interpreted-text role="mod"}.

-   `celery.utils.datastructures.DependencyGraph` moved to
    `celery.utils.graph`{.interpreted-text role="mod"}.

-   `celery.utils.jsonify` is now
    `celery.utils.serialization.jsonify`{.interpreted-text role="func"}.

-   `celery.utils.strtobool` is now
    `celery.utils.serialization.strtobool`{.interpreted-text
    role="func"}.

-   `celery.utils.is_iterable` has been removed.

    > Instead use:
    >
    > ``` python
    > isinstance(x, collections.Iterable)
    > ```

-   `celery.utils.lpmerge` is now
    `celery.utils.collections.lpmerge`{.interpreted-text role="func"}.

-   `celery.utils.cry` is now `celery.utils.debug.cry`{.interpreted-text
    role="func"}.

-   `celery.utils.isatty` is now
    `celery.platforms.isatty`{.interpreted-text role="func"}.

-   `celery.utils.gen_task_name` is now
    `celery.utils.imports.gen_task_name`{.interpreted-text role="func"}.

-   `celery.utils.deprecated` is now
    `celery.utils.deprecated.Callable`{.interpreted-text role="func"}

-   `celery.utils.deprecated_property` is now
    `celery.utils.deprecated.Property`{.interpreted-text role="func"}.

-   `celery.utils.warn_deprecated` is now
    `celery.utils.deprecated.warn`{.interpreted-text role="func"}

## Deprecation Time-line Changes {#v400-deprecations}

See the `deprecation-timeline`{.interpreted-text role="ref"}.
