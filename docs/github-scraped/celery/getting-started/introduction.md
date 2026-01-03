# Introduction to Celery {#intro}

::: {.contents local="" depth="1"}
:::

## What\'s a Task Queue?

Task queues are used as a mechanism to distribute work across threads or
machines.

A task queue\'s input is a unit of work called a task. Dedicated worker
processes constantly monitor task queues for new work to perform.

Celery communicates via messages, usually using a broker to mediate
between clients and workers. To initiate a task the client adds a
message to the queue, the broker then delivers that message to a worker.

A Celery system can consist of multiple workers and brokers, giving way
to high availability and horizontal scaling.

Celery is written in Python, but the protocol can be implemented in any
language. In addition to Python there\'s
[node-celery](https://github.com/mher/node-celery) for Node.js, a [PHP
client](https://github.com/gjedeer/celery-php),
[gocelery](https://github.com/gocelery/gocelery),
[gopher-celery](https://github.com/marselester/gopher-celery) for Go,
and [rusty-celery](https://github.com/rusty-celery/rusty-celery) for
Rust.

Language interoperability can also be achieved exposing an HTTP endpoint
and having a task that requests it (webhooks).

## What do I need?

::: {.sidebar subtitle="Celery version 5.5.x runs on:"}
**Version Requirements: Celery version 5.5.x runs on:**

-   Python ❨3.8, 3.9, 3.10, 3.11, 3.12, 3.13❩
-   PyPy3.9+ ❨v7.3.12+❩

If you\'re running an older version of Python, you need to be running an
older version of Celery:

-   Python 3.7: Celery 5.2 or earlier.
-   Python 3.6: Celery 5.1 or earlier.
-   Python 2.7: Celery 4.x series.
-   Python 2.6: Celery series 3.1 or earlier.
-   Python 2.5: Celery series 3.0 or earlier.
-   Python 2.4: Celery series 2.2 or earlier..

Celery is a project with minimal funding, so we don\'t support Microsoft
Windows. Please don\'t open any issues related to that platform.
:::

*Celery* requires a message transport to send and receive messages. The
RabbitMQ and Redis broker transports are feature complete, but there\'s
also support for a myriad of other experimental solutions, including
using SQLite for local development.

*Celery* can run on a single machine, on multiple machines, or even
across data centers.

## Get Started

If this is the first time you\'re trying to use Celery, or if you
haven\'t kept up with development in the 3.1 version and are coming from
previous versions, then you should read our getting started tutorials:

-   `first-steps`{.interpreted-text role="ref"}
-   `next-steps`{.interpreted-text role="ref"}

## Celery is...

::: topic
**\\**

-   **Simple**

    > Celery is easy to use and maintain, and it *doesn\'t need
    > configuration files*.
    >
    > It has an active, friendly community you can talk to for support,
    > including a
    > [mailing-list](https://groups.google.com/group/celery-users) and
    > an `IRC channel <irc-channel>`{.interpreted-text role="ref"}.
    >
    > Here\'s one of the simplest applications you can make:
    >
    > ``` python
    > from celery import Celery
    >
    > app = Celery('hello', broker='amqp://guest@localhost//')
    >
    > @app.task
    > def hello():
    >     return 'hello world'
    > ```

-   **Highly Available**

    > Workers and clients will automatically retry in the event of
    > connection loss or failure, and some brokers support HA in way of
    > *Primary/Primary* or *Primary/Replica* replication.

-   **Fast**

    > A single Celery process can process millions of tasks a minute,
    > with sub-millisecond round-trip latency (using RabbitMQ,
    > librabbitmq, and optimized settings).

-   **Flexible**

    > Almost every part of *Celery* can be extended or used on its own,
    > Custom pool implementations, serializers, compression schemes,
    > logging, schedulers, consumers, producers, broker transports, and
    > much more.
:::

::: topic
**It supports**

::: {.hlist columns="2"}
-   **Brokers**

    > -   `RabbitMQ <broker-rabbitmq>`{.interpreted-text role="ref"},
    >     `Redis <broker-redis>`{.interpreted-text role="ref"},
    > -   `Amazon SQS <broker-sqs>`{.interpreted-text role="ref"}, and
    >     more...

-   **Concurrency**

    > -   prefork (multiprocessing),
    > -   [Eventlet](http://eventlet.net/), [gevent](http://gevent.org/)
    > -   thread (multithreaded)
    > -   [solo]{.title-ref} (single threaded)

-   **Result Stores**

    > -   AMQP, Redis
    > -   Memcached,
    > -   SQLAlchemy, Django ORM
    > -   Apache Cassandra, Elasticsearch, Riak
    > -   MongoDB, CouchDB, Couchbase, ArangoDB
    > -   Amazon DynamoDB, Amazon S3
    > -   Microsoft Azure Block Blob, Microsoft Azure Cosmos DB
    > -   Google Cloud Storage
    > -   File system

-   **Serialization**

    > -   *pickle*, *json*, *yaml*, *msgpack*.
    > -   *zlib*, *bzip2* compression.
    > -   Cryptographic message signing.
:::
:::

## Features

::: topic
**\\**

::: {.hlist columns="2"}
-   **Monitoring**

    > A stream of monitoring events is emitted by workers and is used by
    > built-in and external tools to tell you what your cluster is doing
    > \-- in real-time.
    >
    > `Read more… <guide-monitoring>`{.interpreted-text role="ref"}.

-   **Work-flows**

    > Simple and complex work-flows can be composed using a set of
    > powerful primitives we call the \"canvas\", including grouping,
    > chaining, chunking, and more.
    >
    > `Read more… <guide-canvas>`{.interpreted-text role="ref"}.

-   **Time & Rate Limits**

    > You can control how many tasks can be executed per
    > second/minute/hour, or how long a task can be allowed to run, and
    > this can be set as a default, for a specific worker or
    > individually for each task type.
    >
    > `Read more… <worker-time-limits>`{.interpreted-text role="ref"}.

-   **Scheduling**

    > You can specify the time to run a task in seconds or a
    > `~datetime.datetime`{.interpreted-text role="class"}, or you can
    > use periodic tasks for recurring events based on a simple
    > interval, or Crontab expressions supporting minute, hour, day of
    > week, day of month, and month of year.
    >
    > `Read more… <guide-beat>`{.interpreted-text role="ref"}.

-   **Resource Leak Protection**

    > The
    > `--max-tasks-per-child <celery worker --max-tasks-per-child>`{.interpreted-text
    > role="option"} option is used for user tasks leaking resources,
    > like memory or file descriptors, that are simply out of your
    > control.
    >
    > `Read more… <worker-max-tasks-per-child>`{.interpreted-text
    > role="ref"}.

-   **User Components**

    > Each worker component can be customized, and additional components
    > can be defined by the user. The worker is built up using
    > \"bootsteps\" --- a dependency graph enabling fine grained control
    > of the worker\'s internals.
:::
:::

## Framework Integration

Celery is easy to integrate with web frameworks, some of them even have
integration packages:

>   ---------------------------------------------------------------------- ------------------------------------
>   [Pyramid](http://docs.pylonsproject.org/en/latest/docs/pyramid.html)   `pyramid_celery`{.interpreted-text
>                                                                          role="pypi"}
>
>   [Pylons](http://pylonshq.com/)                                         `celery-pylons`{.interpreted-text
>                                                                          role="pypi"}
>
>   [Flask](http://flask.pocoo.org/)                                       not needed
>
>   [web2py](http://web2py.com/)                                           `web2py-celery`{.interpreted-text
>                                                                          role="pypi"}
>
>   [Tornado](http://www.tornadoweb.org/)                                  `tornado-celery`{.interpreted-text
>                                                                          role="pypi"}
>
>   [Tryton](http://www.tryton.org/)                                       `celery_tryton`{.interpreted-text
>                                                                          role="pypi"}
>   ---------------------------------------------------------------------- ------------------------------------

For [Django](https://djangoproject.com/) see
`django-first-steps`{.interpreted-text role="ref"}.

The integration packages aren\'t strictly necessary, but they can make
development easier, and sometimes they add important hooks like closing
database connections at `fork(2)`{.interpreted-text role="manpage"}.

## Quick Jump

::: topic
**I want to ⟶**

::: {.hlist columns="2"}
-   `get the return value of a task <task-states>`{.interpreted-text
    role="ref"}
-   `use logging from my task <task-logging>`{.interpreted-text
    role="ref"}
-   `learn about best practices <task-best-practices>`{.interpreted-text
    role="ref"}
-   `create a custom task base class <task-custom-classes>`{.interpreted-text
    role="ref"}
-   `add a callback to a group of tasks <canvas-chord>`{.interpreted-text
    role="ref"}
-   `split a task into several chunks <canvas-chunks>`{.interpreted-text
    role="ref"}
-   `optimize the worker <guide-optimizing>`{.interpreted-text
    role="ref"}
-   `see a list of built-in task states <task-builtin-states>`{.interpreted-text
    role="ref"}
-   `create custom task states <custom-states>`{.interpreted-text
    role="ref"}
-   `set a custom task name <task-names>`{.interpreted-text role="ref"}
-   `track when a task starts <task-track-started>`{.interpreted-text
    role="ref"}
-   `retry a task when it fails <task-retry>`{.interpreted-text
    role="ref"}
-   `get the id of the current task <task-request-info>`{.interpreted-text
    role="ref"}
-   `know what queue a task was delivered to <task-request-info>`{.interpreted-text
    role="ref"}
-   `see a list of running workers <monitoring-control>`{.interpreted-text
    role="ref"}
-   `purge all messages <monitoring-control>`{.interpreted-text
    role="ref"}
-   `inspect what the workers are doing <monitoring-control>`{.interpreted-text
    role="ref"}
-   `see what tasks a worker has registered <monitoring-control>`{.interpreted-text
    role="ref"}
-   `migrate tasks to a new broker <monitoring-control>`{.interpreted-text
    role="ref"}
-   `see a list of event message types <event-reference>`{.interpreted-text
    role="ref"}
-   `contribute to Celery <contributing>`{.interpreted-text role="ref"}
-   `learn about available configuration settings <configuration>`{.interpreted-text
    role="ref"}
-   `get a list of people and companies using Celery <res-using-celery>`{.interpreted-text
    role="ref"}
-   `write my own remote control command <worker-custom-control-commands>`{.interpreted-text
    role="ref"}
-   `change worker queues at runtime <worker-queues>`{.interpreted-text
    role="ref"}
:::
:::

::: topic
**Jump to ⟶**

::: {.hlist columns="4"}
-   `Brokers <brokers>`{.interpreted-text role="ref"}
-   `Applications <guide-app>`{.interpreted-text role="ref"}
-   `Tasks <guide-tasks>`{.interpreted-text role="ref"}
-   `Calling <guide-calling>`{.interpreted-text role="ref"}
-   `Workers <guide-workers>`{.interpreted-text role="ref"}
-   `Daemonizing <daemonizing>`{.interpreted-text role="ref"}
-   `Monitoring <guide-monitoring>`{.interpreted-text role="ref"}
-   `Optimizing <guide-optimizing>`{.interpreted-text role="ref"}
-   `Security <guide-security>`{.interpreted-text role="ref"}
-   `Routing <guide-routing>`{.interpreted-text role="ref"}
-   `Configuration <configuration>`{.interpreted-text role="ref"}
-   `Django <django>`{.interpreted-text role="ref"}
-   `Contributing <contributing>`{.interpreted-text role="ref"}
-   `Signals <signals>`{.interpreted-text role="ref"}
-   `FAQ <faq>`{.interpreted-text role="ref"}
-   `API Reference <apiref>`{.interpreted-text role="ref"}
:::
:::

## Installation {#celery-installation}

You can install Celery either via the Python Package Index (PyPI) or
from source.

To install using `pip`{.interpreted-text role="command"}:

``` console
$ pip install -U Celery
```

### Bundles

Celery also defines a group of bundles that can be used to install
Celery and the dependencies for a given feature.

You can specify these in your requirements or on the
`pip`{.interpreted-text role="command"} command-line by using brackets.
Multiple bundles can be specified by separating them by commas.

``` console
$ pip install "celery[librabbitmq]"

$ pip install "celery[librabbitmq,redis,auth,msgpack]"
```

The following bundles are available:

#### Serializers

`celery[auth]`

:   for using the `auth` security serializer.

`celery[msgpack]`

:   for using the msgpack serializer.

`celery[yaml]`

:   for using the yaml serializer.

#### Concurrency

`celery[eventlet]`

:   for using the `eventlet`{.interpreted-text role="pypi"} pool.

`celery[gevent]`

:   for using the `gevent`{.interpreted-text role="pypi"} pool.

#### Transports and Backends

`celery[librabbitmq]`

:   for using the librabbitmq C library.

`celery[redis]`

:   for using Redis as a message transport or as a result backend.

`celery[sqs]`

:   for using Amazon SQS as a message transport (*experimental*).

`celery[tblib]`

:   for using the `task_remote_tracebacks`{.interpreted-text
    role="setting"} feature.

`celery[memcache]`

:   for using Memcached as a result backend (using
    `pylibmc`{.interpreted-text role="pypi"})

`celery[pymemcache]`

:   for using Memcached as a result backend (pure-Python
    implementation).

`celery[cassandra]`

:   for using Apache Cassandra/Astra DB as a result backend with
    DataStax driver.

`celery[couchbase]`

:   for using Couchbase as a result backend.

`celery[arangodb]`

:   for using ArangoDB as a result backend.

`celery[elasticsearch]`

:   for using Elasticsearch as a result backend.

`celery[riak]`

:   for using Riak as a result backend.

`celery[dynamodb]`

:   for using AWS DynamoDB as a result backend.

`celery[zookeeper]`

:   for using Zookeeper as a message transport.

`celery[sqlalchemy]`

:   for using SQLAlchemy as a result backend (*supported*).

`celery[pyro]`

:   for using the Pyro4 message transport (*experimental*).

`celery[slmq]`

:   for using the SoftLayer Message Queue transport (*experimental*).

`celery[consul]`

:   for using the Consul.io Key/Value store as a message transport or
    result backend (*experimental*).

`celery[django]`

:   specifies the lowest version possible for Django support.

    You should probably not use this in your requirements, it\'s here
    for informational purposes only.

`celery[gcs]`

:   for using the Google Cloud Storage as a result backend
    (*experimental*).

`celery[gcpubsub]`

:   for using the Google Cloud Pub/Sub as a message transport
    (*experimental*)..

### Downloading and installing from source {#celery-installing-from-source}

Download the latest version of Celery from PyPI:

<https://pypi.org/project/celery/>

You can install it by doing the following,:

``` console
$ tar xvfz celery-0.0.0.tar.gz
$ cd celery-0.0.0
$ python setup.py build
# python setup.py install
```

The last command must be executed as a privileged user if you aren\'t
currently using a virtualenv.

### Using the development version {#celery-installing-from-git}

#### With pip

The Celery development version also requires the development versions of
`kombu`{.interpreted-text role="pypi"}, `amqp`{.interpreted-text
role="pypi"}, `billiard`{.interpreted-text role="pypi"}, and
`vine`{.interpreted-text role="pypi"}.

You can install the latest snapshot of these using the following pip
commands:

``` console
$ pip install https://github.com/celery/celery/zipball/main#egg=celery
$ pip install https://github.com/celery/billiard/zipball/main#egg=billiard
$ pip install https://github.com/celery/py-amqp/zipball/main#egg=amqp
$ pip install https://github.com/celery/kombu/zipball/main#egg=kombu
$ pip install https://github.com/celery/vine/zipball/main#egg=vine
```

#### With git

Please see the `Contributing <contributing>`{.interpreted-text
role="ref"} section.
