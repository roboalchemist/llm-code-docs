# Source: https://dramatiq.io/advanced.html

Title: Advanced Topics — Dramatiq 2.0.1 documentation

URL Source: https://dramatiq.io/advanced.html

Markdown Content:
Customizing Middleware[¶](https://dramatiq.io/advanced.html#customizing-middleware "Link to this heading")
----------------------------------------------------------------------------------------------------------

Some of Dramatiq’s built-in functionality is actually implemented by the [Default Middleware](https://dramatiq.io/reference.html#default-middleware).

To customise the middleware Dramatiq uses, there are two typical approaches;

### 2. Providing a list of Middleware Classes[¶](https://dramatiq.io/advanced.html#providing-a-list-of-middleware-classes "Link to this heading")

If you wish to have full control over the middleware (so the [Default Middleware](https://dramatiq.io/reference.html#default-middleware) is not used) you must pass a list of Middleware when instantiating your [`Broker`](https://dramatiq.io/reference.html#dramatiq.Broker "dramatiq.Broker"). When you do so, Dramatiq will only use the middleware in the list you pass (plus any middleware you add to the broker later with the [`add_middleware`](https://dramatiq.io/reference.html#dramatiq.Broker.add_middleware "dramatiq.Broker.add_middleware") method). The list can contain any of the [Default Middleware](https://dramatiq.io/reference.html#default-middleware) or [Optional Middleware](https://dramatiq.io/reference.html#optional-middleware), or your own custom [`Middleware`](https://dramatiq.io/reference.html#dramatiq.Middleware "dramatiq.Middleware") subclasses.

Warning

Omitting from the list or changing the settings of default middleware can lead to behavior different to what is documented.

For example if you wish to

1.   Disable the [`Callbacks`](https://dramatiq.io/reference.html#dramatiq.middleware.Callbacks "dramatiq.middleware.Callbacks") and [`Pipelines`](https://dramatiq.io/reference.html#dramatiq.middleware.Pipelines "dramatiq.middleware.Pipelines") middleware.

2.   Set a custom default [max_retries](https://dramatiq.io/guide.html#message-retries) of 5 for the [`Retries`](https://dramatiq.io/reference.html#dramatiq.middleware.Retries "dramatiq.middleware.Retries") middleware.

3.   Add in the non-default [`CurrentMessage`](https://dramatiq.io/reference.html#dramatiq.middleware.CurrentMessage "dramatiq.middleware.CurrentMessage") middleware.

you can do the following:

import dramatiq
from dramatiq.middleware import AgeLimit, TimeLimit, ShutdownNotifications, Retries, CurrentMessage

# Replace `dramatiq.Broker` with a concrete class, e.g. dramatiq.brokers.redis.RedisBroker.
broker = dramatiq.Broker(
    middleware=[
        AgeLimit(),
        TimeLimit(),
        ShutdownNotifications(),
        # Note: custom default max_retries of 5
        Retries(max_retries=5),
        # Note: non-default middleware class included.
        CurrentMessage(),
        # Note: Callbacks and Pipelines are not included.
        # They will not be added back by dramatiq.
    ],
)

dramatiq.set_broker(broker)

Brokers[¶](https://dramatiq.io/advanced.html#brokers "Link to this heading")
----------------------------------------------------------------------------

### Multi-tenancy[¶](https://dramatiq.io/advanced.html#multi-tenancy "Link to this heading")

With Dramatiq you can run multiple logical apps on the same broker. The way you do this is different for each broker, but fairly simple in each case.

#### RabbitMQ[¶](https://dramatiq.io/advanced.html#id2 "Link to this heading")

RabbitMQ has the concept of [virtual hosts](https://www.rabbitmq.com/vhosts.html) built into it. They provide logical grouping and separation of resources. You can create virtual hosts using the rabbitmqctl command:

$ rabbitmqctl add_vhost app1
$ rabbitmqctl set_permissions -p app1 my_user ".*" ".*" ".*"

You can then pass that vhost to [`RabbitmqBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker "dramatiq.brokers.rabbitmq.RabbitmqBroker") when you instantiate it.

#### Redis[¶](https://dramatiq.io/advanced.html#id3 "Link to this heading")

The [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker") takes a `namespace` parameter that you can use to logically split queues across multiple apps.

### Highly Available Queues[¶](https://dramatiq.io/advanced.html#highly-available-queues "Link to this heading")

#### RabbitMQ[¶](https://dramatiq.io/advanced.html#id4 "Link to this heading")

When running RabbitMQ with a [high availability cluster](https://www.rabbitmq.com/ha.html), you can pass

*   a sequence of pika [connection parameters](https://pika.readthedocs.io/en/0.12.0/modules/parameters.html) or

*   a connection URL with one or more targets split by `;` or

*   a list connection URLs

to [`RabbitmqBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker "dramatiq.brokers.rabbitmq.RabbitmqBroker") when instantiating it. This will make dramatiq failover if the currently connected node fails.

from dramatiq.brokers.rabbitmq import RabbitmqBroker

# Using a sequence of connection parameters:

rabbitmq_broker = RabbitmqBroker(parameters=[
    dict(host='node1.foo.net'),
    dict(host='node2.foo.net'),
])

# Using a single string containing multiple targets:

rabbitmq_broker = RabbitmqBroker(
  url='amqp://node1.foo.net;ampq://node2.foo.net'
)

# Using a list of connection URLs:

rabbitmq_broker = RabbitmqBroker(
  url=['amqp://node1.foo.net', 'ampq://node2.foo.net']
)

### Other brokers[¶](https://dramatiq.io/advanced.html#other-brokers "Link to this heading")

Other broker implementations are available through third-party packages:

*   [Amazon SQS](https://aws.amazon.com/sqs/) with [dramatiq_sqs](https://github.com/Bogdanp/dramatiq_sqs).

Messages[¶](https://dramatiq.io/advanced.html#messages "Link to this heading")
------------------------------------------------------------------------------

### Message Persistence[¶](https://dramatiq.io/advanced.html#message-persistence "Link to this heading")

Messages sent to Dramatiq brokers are persisted to disk and survive across broker reboots. Exactly how often messages are flushed to disk depends on your broker.

Messages that have been pulled by workers but not processed are returned to the broker on graceful shutdown and any messages that are in flight when a worker is terminated are going to be redelivered later. Messages are only ever acknowledged to (removed from) the broker after they have been successfully processed.

When a worker goes down while processing messages (eg. due to hardware, power or network failure) then the messages it pulled from the broker will eventually be re-delivered to it (assuming it recovers) or another worker.

### Message Results[¶](https://dramatiq.io/advanced.html#message-results "Link to this heading")

Dramatiq can store actor return values to Memcached and Redis by leveraging the [`Results`](https://dramatiq.io/reference.html#dramatiq.results.Results "dramatiq.results.Results") middleware. In most cases you can get by without needing this capability so the middleware is not turned on by default. When you do need it, however, it’s there.

### Message Interrupts[¶](https://dramatiq.io/advanced.html#message-interrupts "Link to this heading")

Dramatiq may interrupt message processing mid-execution. This is achieved by asynchronously raising an exception in the worker thread that is currently processing the message.

Attention

Currently, interrupts are only supported on CPython and are subject to the restrictions of the GIL. This means the interrupt exception will only be raised the next time that thread acquires the GIL, and they are unable to cancel system calls.

Interrupts are used by the following middleware:

*   [`ShutdownNotifications`](https://dramatiq.io/reference.html#dramatiq.middleware.ShutdownNotifications "dramatiq.middleware.ShutdownNotifications") (raises [`Shutdown`](https://dramatiq.io/reference.html#dramatiq.middleware.Shutdown "dramatiq.middleware.Shutdown"))

*   [`TimeLimit`](https://dramatiq.io/reference.html#dramatiq.middleware.TimeLimit "dramatiq.middleware.TimeLimit") (raises [`TimeLimitExceeded`](https://dramatiq.io/reference.html#dramatiq.middleware.TimeLimitExceeded "dramatiq.middleware.TimeLimitExceeded"))

In order to gracefully handle interrupts, wrap the code in a try/except block, catching the appropriate exception type. To attempt to requeue the message, raise an exception to indicate failure.

import dramatiq
from dramatiq.middleware import Interrupt

@dramatiq.actor(max_retries=3, notify_shutdown=True)
def long_running_task():
    try:
        setup()
        do_work()
    except Shutdown:
        cleanup()
        raise

### Accessing Messages from Within Actors[¶](https://dramatiq.io/advanced.html#accessing-messages-from-within-actors "Link to this heading")

Actors can access their own messages via the [`CurrentMessage`](https://dramatiq.io/reference.html#dramatiq.middleware.CurrentMessage "dramatiq.middleware.CurrentMessage") middleware. This middleware is not enabled by default, but you can add it to your broker when you instantiate it or by calling [`add_middleware`](https://dramatiq.io/reference.html#dramatiq.Broker.add_middleware "dramatiq.Broker.add_middleware"):

from dramatiq.middleware import CurrentMessage

broker.add_middleware(CurrentMessage())

With this middleware in place, every actor can access its own message by calling [`get_current_message`](https://dramatiq.io/reference.html#dramatiq.middleware.CurrentMessage.get_current_message "dramatiq.middleware.CurrentMessage.get_current_message") on the [`CurrentMessage`](https://dramatiq.io/reference.html#dramatiq.middleware.CurrentMessage "dramatiq.middleware.CurrentMessage") class:

@dramatiq.actor
def example():
    print(CurrentMessage.get_current_message())

### Enqueueing Messages from Other Languages[¶](https://dramatiq.io/advanced.html#enqueueing-messages-from-other-languages "Link to this heading")

You can enqueue Dramatiq messages using any language that has bindings to one of its brokers. All you have to do is push a JSON-encoded dictionary containing the following fields to your queue:

{
 "queue_name": "default", // The name of the queue the message is being pushed on
 "actor_name": "add", // The name of the actor that should handle this message
 "args": [1, 2], // A list of positional arguments that are passed to the actor
 "kwargs": {}, // A dictionary of keyword arguments that are passed to the actor
 "options": {}, // Arbitrary options that are used by middleware. Leave this empty
 "message_id": "unique-id", // A UUID4 value representing the message's unique id in the system
 "message_timestamp": 0, // The UNIX timestamp in milliseconds representing when the message was first enqueued
}

#### Using RabbitMQ[¶](https://dramatiq.io/advanced.html#using-rabbitmq "Link to this heading")

Assuming you want to enqueue a message on a queue named `default`, publish a persistent message to that queue in RabbitMQ.

#### Using Redis[¶](https://dramatiq.io/advanced.html#using-redis "Link to this heading")

Add a field to the `options` dictionary of the message called `redis_message_id` that is a different UUID4 value than `message_id`:

{
 ...
 "options": { "redis_message_id": "unique-id-2"},
 ...
}

Assuming you want to enqueue a message on a queue named `default`, run:

> HSET dramatiq:default.msgs $YOUR_REDIS_MESSAGE_ID $YOUR_MESSAGE_PAYLOAD
> RPUSH dramatiq:default $YOUR_REDIS_MESSAGE_ID

`$YOUR_REDIS_MESSAGE_ID` is the `redis_message_id` in the `options` field of the message payload.

Workers[¶](https://dramatiq.io/advanced.html#workers "Link to this heading")
----------------------------------------------------------------------------

### Worker Exit Codes[¶](https://dramatiq.io/advanced.html#worker-exit-codes "Link to this heading")

Dramatiq uses process exit codes to denote several scenarios:

| Code | Description |
| --- | --- |
| `0` | Returned when the process exits gracefully. |
| `1` | Returned when the process is killed. |
| `2` | Returned when a module cannot be imported or when a command line argument is invalid. |
| `3` | Returned when a broker connection cannot be established during worker startup. |
| `4` | Returned when a PID file is set and Dramatiq is already running. |

### Controlling Workers[¶](https://dramatiq.io/advanced.html#controlling-workers "Link to this heading")

The main Dramatiq process responds to several signals:

$ kill -TERM [master-process-pid]

#### `INT` and `TERM`[¶](https://dramatiq.io/advanced.html#int-and-term "Link to this heading")

Sending an `INT` or `TERM` signal to the main process triggers graceful shutdown. Consumer threads will stop receiving new work and worker threads will finish processing the work they have in flight before shutting down. Any tasks still in worker memory at this point are re-queued on the broker.

If you send a second `INT` or `TERM` signal then the worker processes will be killed immediately.

#### `HUP`[¶](https://dramatiq.io/advanced.html#hup "Link to this heading")

Sending `HUP` to the main process triggers a graceful shutdown followed by a reload of the workers. This is useful if you want to reload code without completely restarting the main process.

### Using gevent[¶](https://dramatiq.io/advanced.html#using-gevent "Link to this heading")

Dramatiq comes with a CLI utility called `dramatiq-gevent` that can run workers under [gevent](http://www.gevent.org/). The following invocation would run 8 worker processes with 250 greenlets per process for a total of 2k lightweight worker threads:

$ dramatiq-gevent my_app -p 8 -t 250

If your tasks spend most of their time doing network IO and don’t depend on C extensions to execute those network calls then using gevent could provide a significant performance improvement.

I suggest at least experimenting with it to see if it fits your use case.

### Prometheus Metrics[¶](https://dramatiq.io/advanced.html#prometheus-metrics "Link to this heading")

Prometheus metrics are automatically exported by workers whenever you run them using the command line utility (assuming you’re using the Prometheus middleware). By default, the exposition server listens on port `9191` so you can tell Prometheus to scrape that or you can specify what host and port it should listen on by setting the `dramatiq_prom_host` and `dramatiq_prom_port` environment variables.

The following metrics are exported:

`dramatiq_messages_total`
A _counter_ for the total number of messages processed.

`dramatiq_message_errors_total`
A _counter_ for the total number of errored messages.

`dramatiq_message_retries_total`
A _counter_ for the total number of retried messages.

`dramatiq_message_rejects_total`
A _counter_ for the total number of dead-lettered messages.

`dramatiq_messages_inprogress`
A _gauge_ for the number of messages currently being processed.

`dramatiq_delayed_messages_inprogress`
A _gauge_ for the number of delayed messages currently in memory.

`dramatiq_message_duration_milliseconds`
A _histogram_ for the time spent processing messages.

All metrics define labels for `queue_name` and `actor_name`.

#### Grafana Dashboard[¶](https://dramatiq.io/advanced.html#grafana-dashboard "Link to this heading")

You can find a Grafana dashboard that displays these metrics [here](https://grafana.com/grafana/dashboards/3692-dramatiq/).

#### Gotchas with Prometheus[¶](https://dramatiq.io/advanced.html#gotchas-with-prometheus "Link to this heading")

The Prometheus client for Python is a bit finicky when it comes to exporting metrics from a multi-process configuration. If your own app uses Prometheus, then you should export `prometheus_multiproc_dir` and `dramatiq_prom_db` environment variables – both pointing to an existing folder – and remove any files in that folder before running Dramatiq. For example:

mkdir -p /tmp/dramatiq-prometheus \
  && rm -r /tmp/dramatiq-prometheus/* \
  && env prometheus_multiproc_dir=/tmp/dramatiq-prometheus \
         dramatiq_prom_db=/tmp/dramatiq-prometheus \
         dramatiq app

If you don’t do this, then metrics will likely fail to export properly.

Workflows[¶](https://dramatiq.io/advanced.html#workflows "Link to this heading")
--------------------------------------------------------------------------------

### Nested Pipelines and Groups[¶](https://dramatiq.io/advanced.html#nested-pipelines-and-groups "Link to this heading")

Dramatiq supports running tasks in parallel via [`group`](https://dramatiq.io/reference.html#dramatiq.group "dramatiq.group") and in sequence via [`pipeline`](https://dramatiq.io/reference.html#dramatiq.pipeline "dramatiq.pipeline"), but it does not provide a built-in way to run a pipeline of groups out of the box. If you need more advanced orchestration capabilities, such as nesting chains and groups of tasks at arbitrary depth, you may find the [dramatiq-workflow](https://github.com/Outset-AI/dramatiq-workflow) package useful.
