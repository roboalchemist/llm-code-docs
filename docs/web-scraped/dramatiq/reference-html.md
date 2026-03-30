# Source: https://dramatiq.io/reference.html

Title: API Reference — Dramatiq 2.0.1 documentation

URL Source: https://dramatiq.io/reference.html

Markdown Content:
API Reference
Functions
dramatiq.get_broker() → Broker
[source]

Get the global broker instance.

If no global broker is set, a RabbitMQ broker will be returned. If the RabbitMQ dependencies are not installed, a Redis broker will be returned.

Returns:

The default Broker.

Return type:

Broker

dramatiq.set_broker(broker: Broker) → None
[source]

Configure the global broker instance.

Parameters:

broker (Broker) – The broker instance to use by default.

dramatiq.get_encoder() → Encoder
[source]

Get the global encoder object.

Returns:

Encoder

dramatiq.set_encoder(encoder: Encoder) → None
[source]

Set the global encoder object.

Parameters:

encoder (Encoder) – The encoder instance to use when serializing messages.

Actors & Messages
dramatiq.actor(fn: Callable[[P], Awaitable[R]]) → Actor[P, R]
[source]
dramatiq.actor(fn: Callable[[P], R]) → Actor[P, R]
dramatiq.actor(*, queue_name: str = 'default', priority: int = 0, actor_name: str | None = None, broker: Broker | None = None, actor_class: Callable[[...], Actor[Any, Any]] = Actor, **options: Any) → ActorDecorator

Declare an actor.

Examples

>>> import dramatiq

>>> @dramatiq.actor
... def add(x, y):
...     print(x + y)
...
>>> add
Actor(<function add at 0x106c6d488>, queue_name='default', actor_name='add')

>>> add(1, 2)
3

>>> add.send(1, 2)
Message(
  queue_name='default',
  actor_name='add',
  args=(1, 2), kwargs={}, options={},
  message_id='e0d27b45-7900-41da-bb97-553b8a081206',
  message_timestamp=1497862448685)

Parameters:

fn (callable) – The function to wrap.

actor_class (type) – Type created by the decorator. Defaults to Actor but can be any callable as long as it returns an actor and takes the same arguments as the Actor class.

actor_name (str) – The name of the actor.

queue_name (str) – The name of the queue to use.

priority (int) – The actor’s global priority. If two tasks have been pulled on a worker concurrently and one has a higher priority than the other then it will be processed first. Lower numbers represent higher priorities.

broker (Broker) – The broker to use with this actor.

**options – Arbitrary options that vary with the set of middleware that you use. See get_broker().actor_options.

Returns:

The decorated function.

Return type:

Actor

class dramatiq.Actor(fn: Callable[[P], Awaitable[R]] | Callable[[P], R], *, broker: Broker, actor_name: str, queue_name: str, priority: int, options: dict[str, Any])
[source]

Thin wrapper around callables that stores metadata about how they should be executed asynchronously. Actors are callable.

logger

The actor’s logger.

Type:

Logger

fn

The underlying callable.

Type:

callable

broker

The broker this actor is bound to.

Type:

Broker

actor_name

The actor’s name.

Type:

str

queue_name

The actor’s queue.

Type:

str

priority

The actor’s priority.

Type:

int

options

Arbitrary options that are passed to the broker and middleware.

Type:

dict

message(*args: ~typing.~P, **kwargs: ~typing.~P) → Message[R]
[source]

Build a message. This method is useful if you want to compose actors. See the actor composition documentation for details.

Parameters:

*args (tuple) – Positional arguments to send to the actor.

**kwargs – Keyword arguments to send to the actor.

Examples

>>> (add.message(1, 2) | add.message(3))
pipeline([add(1, 2), add(3)])

Returns:

A message that can be enqueued on a broker.

Return type:

Message

message_with_options(*, args: tuple = (), kwargs: dict[str, Any] | None = None, **options) → Message[R]
[source]

Build a message with an arbitrary set of processing options. This method is useful if you want to compose actors. See the actor composition documentation for details.

Parameters:

args (tuple) – Positional arguments that are passed to the actor.

kwargs (dict) – Keyword arguments that are passed to the actor.

**options – Arbitrary options that are passed to the broker and any registered middleware.

Returns:

A message that can be enqueued on a broker.

Return type:

Message

send(*args: ~typing.~P, **kwargs: ~typing.~P) → Message[R]
[source]

Asynchronously send a message to this actor.

Parameters:

*args – Positional arguments to send to the actor.

**kwargs – Keyword arguments to send to the actor.

Returns:

The enqueued message.

Return type:

Message

send_with_options(*, args: tuple = (), kwargs: dict[str, Any] | None = None, delay: timedelta | int | None = None, **options) → Message[R]
[source]

Asynchronously send a message to this actor, along with an arbitrary set of processing options for the broker and middleware.

Parameters:

args (tuple) – Positional arguments that are passed to the actor.

kwargs (dict) – Keyword arguments that are passed to the actor.

delay (int) – The minimum amount of time, in milliseconds, the message should be delayed by. Also accepts a timedelta.

**options – Arbitrary options that are passed to the broker and any registered middleware.

Returns:

The enqueued message.

Return type:

Message

class dramatiq.Message(queue_name: str, actor_name: str, args: tuple[~typing.Any, ...], kwargs: dict[str, ~typing.Any], options: dict[str, ~typing.Any], message_id: str = <factory>, message_timestamp: int = <factory>)
[source]

Encapsulates metadata about messages being sent to individual actors.

Parameters:

queue_name (str) – The name of the queue the message belongs to.

actor_name (str) – The name of the actor that will receive the message.

args (tuple) – Positional arguments that are passed to the actor.

kwargs (dict) – Keyword arguments that are passed to the actor.

options (dict) – Arbitrary options passed to the broker and middleware.

message_id (str) – A globally-unique id assigned to the actor.

message_timestamp (int) – The UNIX timestamp in milliseconds representing when the message was first enqueued.

asdict() → dict[str, Any]
[source]

Convert this message to a dictionary.

copy(**attributes) → Message
[source]

Create a copy of this message.

classmethod decode(data: bytes) → Message
[source]

Convert a bytestring to a message.

Raises:

DecodeError – When the decoder raises an exception while decoding data.

encode() → bytes
[source]

Convert this message to a bytestring.

get_result(*, backend: ResultBackend | None = None, block: bool = False, timeout: int | None = None) → R
[source]

Get the result associated with this message from a result backend.

Warning

If you use multiple result backends or brokers you should always pass the backend parameter. This method is only able to infer the result backend off of the default broker.

Parameters:

backend (ResultBackend) – The result backend to use to get the result. If omitted, this method will try to find and use the result backend on the default broker instance.

block (bool) – Whether or not to block while waiting for a result.

timeout (int) – The maximum amount of time, in ms, to block while waiting for a result. Defaults to 10 seconds.

Raises:

RuntimeError – If there is no result backend on the default broker.

ResultMissing – When block is False and the result isn’t set.

ResultTimeout – When waiting for a result times out.

Returns:

The result.

Return type:

object

property message_datetime: datetime

Read message_timestamp as a UTC-aware datetime.

Datetime precision is limited by the representation of Message.message_timestamp, which is an integer storing milliseconds.

Class-based Actors
class dramatiq.GenericActor
[source]

Base-class for class-based actors.

Each subclass may define an inner class named Meta. You can use the meta class to provide broker options for the actor.

Classes that have abstract = True in their meta class are considered abstract base classes and are not converted into actors. You can’t send these classes messages, you can only inherit from them. Actors that subclass abstract base classes inherit their parents’ meta classes.

Example

>>> class BaseTask(GenericActor):
...     class Meta:
...         abstract = True
...         queue_name = "tasks"
...         max_retries = 20
...
...     def get_task_name(self):
...         raise NotImplementedError
...
...     def perform(self):
...         print(f"Hello from {self.get_task_name()}!")

>>> class FooTask(BaseTask):
...     def get_task_name(self):
...         return "Foo"

>>> class BarTask(BaseTask):
...     def get_task_name(self):
...         return "Bar"

>>> FooTask.send()
>>> BarTask.send()

logger

The actor’s logger.

Type:

Logger

broker

The broker this actor is bound to.

Type:

Broker

actor_name

The actor’s name.

Type:

str

queue_name

The actor’s queue.

Type:

str

priority

The actor’s priority.

Type:

int

options

Arbitrary options that are passed to the broker and middleware.

Type:

dict

perform()
[source]

This is the method that gets called when the actor receives a message. All non-abstract subclasses must implement this method.

Message Composition
class dramatiq.group(children, *, broker=None)
[source]

Run a group of actors in parallel.

Parameters:

children (Iterator[Message|group|pipeline]) – A sequence of messages, groups or pipelines.

broker (Broker) – The broker to run the group on. Defaults to the current global broker.

add_completion_callback(message)
[source]

Adds a completion callback to run once every job in this group has completed. Each group may have multiple completion callbacks.

Warning

This functionality is dependent upon the optional GroupCallbacks middleware. If that’s not set up correctly, then calling run after adding a callback will raise a RuntimeError.

Parameters:

message (Message)

property completed

Returns True when all the jobs in the group have been completed. Actors that don’t store results are not counted, meaning this may be inaccurate if all or some of your actors don’t store results.

Raises:

RuntimeError – If your broker doesn’t have a result backend set up.

property completed_count

Returns the total number of jobs that have been completed. Actors that don’t store results are not counted, meaning this may be inaccurate if all or some of your actors don’t store results.

Raises:

RuntimeError – If your broker doesn’t have a result backend set up.

Returns:

The total number of results.

Return type:

int

get_results(*, block=False, timeout=None)
[source]

Get the results of each job in the group.

Parameters:

block (bool) – Whether or not to block until the results are stored.

timeout (int) – The maximum amount of time, in milliseconds, to wait for results when block is True. Defaults to 10 seconds.

Raises:

ResultMissing – When block is False and the results aren’t set.

ResultTimeout – When waiting for results times out.

Returns:

A result generator.

run(*, delay=None)
[source]

Run the actors in this group.

Parameters:

delay (int) – The minimum amount of time, in milliseconds, each message in the group should be delayed by.

Returns:

This same group.

Return type:

group

wait(*, timeout=None)
[source]

Block until all the jobs in the group have finished or until the timeout expires.

Parameters:

timeout (int) – The maximum amount of time, in ms, to wait. Defaults to 10 seconds.

Raises:

ResultTimeout – When waiting times out.

class dramatiq.pipeline(children: Iterable[Message | pipeline], *, broker=None)
[source]

Chain actors together, passing the result of one actor to the next one in line.

Parameters:

children (Iterable[Message|pipeline]) – A sequence of messages or pipelines. Child pipelines are flattened into the resulting pipeline.

broker (Broker) – The broker to run the pipeline on. Defaults to the current global broker.

property completed

Returns True when all the jobs in the pipeline have been completed. This will always return False if the last actor in the pipeline doesn’t store results.

Raises:

RuntimeError – If your broker doesn’t have a result backend set up.

property completed_count

Returns the total number of jobs that have been completed. Actors that don’t store results are not counted, meaning this may be inaccurate if all or some of your actors don’t store results.

Raises:

RuntimeError – If your broker doesn’t have a result backend set up.

Returns:

The total number of results.

Return type:

int

get_result(*, block=False, timeout=None)
[source]

Get the result of this pipeline.

Pipeline results are represented by the result of the last message in the chain.

Parameters:

block (bool) – Whether or not to block until a result is set.

timeout (int) – The maximum amount of time, in ms, to wait for a result when block is True. Defaults to 10 seconds.

Raises:

ResultMissing – When block is False and the result isn’t set.

ResultTimeout – When waiting for a result times out.

Returns:

The result.

Return type:

object

get_results(*, block=False, timeout=None)
[source]

Get the results of each job in the pipeline.

Parameters:

block (bool) – Whether or not to block until a result is set.

timeout (int) – The maximum amount of time, in ms, to wait for a result when block is True. Defaults to 10 seconds.

Raises:

ResultMissing – When block is False and the result isn’t set.

ResultTimeout – When waiting for a result times out.

Returns:

A result generator.

run(*, delay=None)
[source]

Run this pipeline.

Parameters:

delay (int) – The minimum amount of time, in milliseconds, the pipeline should be delayed by. If both pipeline’s delay and first message’s delay are provided, the bigger value will be used.

Returns:

Itself.

Return type:

pipeline

Message Encoders

Encoders are used to serialize and deserialize messages over the wire.

class dramatiq.Encoder
[source]

Base class for message encoders.

abstract decode(data: bytes) → dict[str, Any]
[source]

Convert a bytestring into message metadata.

abstract encode(data: dict[str, Any]) → bytes
[source]

Convert message metadata into a bytestring.

class dramatiq.JSONEncoder
[source]

Encodes messages as JSON. This is the default encoder.

class dramatiq.PickleEncoder
[source]

Pickles messages.

Warning

This encoder is not secure against maliciously-constructed data. Use it at your own risk.

Brokers
class dramatiq.Broker(middleware: list[Middleware] | None = None)
[source]

Base class for broker implementations.

Parameters:

middleware (list[Middleware]) – The set of middleware that apply to this broker. If you supply this parameter, you are expected to declare all middleware. Most of the time, you’ll want to use add_middleware() instead. See Customizing Middleware for details.

actor_options

The names of all the options actors may overwrite when they are declared.

Type:

set[str]

add_middleware(middleware: Middleware, *, before: type[Middleware] | None = None, after: type[Middleware] | None = None) → None
[source]

Add a middleware object to this broker. The middleware is appended to the end of the middleware list by default.

You can specify another middleware (by class) as a reference point for where the new middleware should be added.

Duplicates of middleware are allowed. If there’s already a middleware object of the same class added to the broker, the middleware will be added for the second time.

Parameters:

middleware (Middleware) – The middleware.

before (type) – Add this middleware before a specific one.

after (type) – Add this middleware after a specific one.

Raises:

ValueError – When either before or after refer to a middleware that hasn’t been registered yet.

close() → None
[source]

Close this broker and perform any necessary cleanup actions.

consume(queue_name: str, prefetch: int = 1, timeout: int = 30000) → Consumer
[source]

Get an iterator that consumes messages off of the queue.

Raises:

QueueNotFound – If the given queue was never declared.

Parameters:

queue_name (str) – The name of the queue to consume messages off of.

prefetch (int) – The number of messages to prefetch per consumer.

timeout (int) – The amount of time in milliseconds to idle for.

Returns:

A message iterator.

Return type:

Consumer

declare_actor(actor: Actor) → None
[source]

Declare a new actor on this broker. Declaring an Actor twice replaces the first actor with the second by name.

Parameters:

actor (Actor) – The actor being declared.

declare_queue(queue_name: str) → None
[source]

Declare a queue on this broker. This method must be idempotent.

Parameters:

queue_name (str) – The name of the queue being declared.

enqueue(message: Message, *, delay: int | None = None) → Message
[source]

Enqueue a message on this broker.

Parameters:

message (Message) – The message to enqueue.

delay (int) – The number of milliseconds to delay the message for.

Returns:

Either the original message or a copy of it.

Return type:

Message

flush(queue_name: str) → None
[source]

Drop all the messages from a queue.

Parameters:

queue_name (str) – The name of the queue to flush.

flush_all() → None
[source]

Drop all messages from all declared queues.

get_actor(actor_name: str) → Actor
[source]

Look up an actor by its name.

Parameters:

actor_name (str) – The name to look up.

Raises:

ActorNotFound – If the actor was never declared.

Returns:

The actor.

Return type:

Actor

get_declared_actors() → set[str]
[source]

Get all declared actors.

Returns:

The names of all the actors declared so far on this Broker.

Return type:

set[str]

get_declared_delay_queues() → set[str]
[source]

Get all declared delay queues.

Returns:

The names of all the delay queues declared so far on this Broker.

Return type:

set[str]

get_declared_queues() → set[str]
[source]

Get all declared queues.

Returns:

The names of all the queues declared so far on this Broker.

Return type:

set[str]

get_results_backend() → ResultBackend
[source]

Get the backend of the Results middleware.

Raises:

RuntimeError – If the broker doesn’t have a results backend.

Returns:

The backend.

Return type:

ResultBackend

join(queue_name: str, *, timeout: int | None = None) → None
[source]

Wait for all the messages on the given queue to be processed. This method is only meant to be used in tests to wait for all the messages in a queue to be processed.

Subclasses that implement this function may add parameters.

Parameters:

queue_name (str) – The queue to wait on.

timeout (Optional[int]) – The max amount of time, in milliseconds, to wait on this queue.

class dramatiq.Consumer
[source]

Consumers iterate over messages on a queue.

Consumers and their MessageProxies are not thread-safe.

ack(message: MessageProxy) → None
[source]

Acknowledge that a message has been processed, removing it from the broker.

Parameters:

message (MessageProxy) – The message to acknowledge.

close() → None
[source]

Close this consumer and perform any necessary cleanup actions.

nack(message: MessageProxy) → None
[source]

Move a message to the dead-letter queue.

Parameters:

message (MessageProxy) – The message to reject.

requeue(messages: Iterable[MessageProxy]) → None
[source]

Move unacked messages back to their queues. This is called by consumer threads when they fail or are shut down. The default implementation does nothing.

Parameters:

messages (Iterable[MessageProxy]) – The messages to requeue.

class dramatiq.MessageProxy(message: Message)
[source]

Base class for messages returned by Broker.consume().

clear_exception() → None
[source]

Remove the exception from this message.

fail() → None
[source]

Mark this message for rejection.

stuff_exception(exception: BaseException) → None
[source]

Stuff an exception into this message.

class dramatiq.brokers.rabbitmq.RabbitmqBroker(*, confirm_delivery: bool = False, url: str | list[str] | None = None, middleware: list[Middleware] | None = None, max_priority: int | None = None, parameters: list[dict[str, Any]] | None = None, **kwargs: Any)
[source]

Bases: Broker

A broker that can be used with RabbitMQ.

Examples

If you want to specify connection parameters individually:

>>> RabbitmqBroker(host="127.0.0.1", port=5672)


Alternatively, if you want to use a connection URL:

>>> RabbitmqBroker(url="amqp://guest:guest@127.0.0.1:5672")


To support queued message priorities, provide a max_priority…

>>> broker = RabbitmqBroker(url="...", max_priority=5)


… then enqueue messages with the broker_priority option:

>>> broker.enqueue(an_actor.message_with_options(
...    broker_priority=5,
... ))


broker_priority can also be provided to send_with_options:

>>> an_actor.send_with_options(
...    broker_priority=5,
... )


The broker_priority provided should have a value between 0 and max_priority, inclusive. Messages without a priority are treated as priority 0. RabbitMQ treats higher numbers as higher priorities.

Note

This the opposite to the Dramatiq actor priority option. (where lower numbers are higher priorities).

See also

ConnectionParameters for a list of all the available connection parameters.

Parameters:

confirm_delivery (bool) – Wait for RabbitMQ to confirm that messages have been committed on every call to enqueue. Defaults to False.

url (str|list[str]) – An optional connection URL. If both a URL and connection parameters are provided, the URL is used.

middleware (list[Middleware]) – The set of middleware that apply to this broker.

max_priority (int) – Configure queues with x-max-priority to support queue-global priority queueing.

parameters (list[dict]) – A sequence of (pika) connection parameters to determine which Rabbit server(s) to connect to.

**kwargs – The (pika) connection parameters to use to determine which Rabbit server to connect to.

add_middleware(middleware: Middleware, *, before: type[Middleware] | None = None, after: type[Middleware] | None = None) → None

Add a middleware object to this broker. The middleware is appended to the end of the middleware list by default.

You can specify another middleware (by class) as a reference point for where the new middleware should be added.

Duplicates of middleware are allowed. If there’s already a middleware object of the same class added to the broker, the middleware will be added for the second time.

Parameters:

middleware (Middleware) – The middleware.

before (type) – Add this middleware before a specific one.

after (type) – Add this middleware after a specific one.

Raises:

ValueError – When either before or after refer to a middleware that hasn’t been registered yet.

property channel

The pika.BlockingChannel for the current thread. This property may change without notice.

close() → None
[source]

Close all open RabbitMQ connections.

property connection

The pika.BlockingConnection for the current thread. This property may change without notice.

consume(queue_name: str, prefetch: int = 1, timeout: int = 5000) → Consumer
[source]

Create a new consumer for a queue.

Parameters:

queue_name (str) – The queue to consume.

prefetch (int) – The number of messages to prefetch.

timeout (int) – The idle timeout in milliseconds.

Returns:

A consumer that retrieves messages from RabbitMQ.

Return type:

Consumer

declare_actor(actor: Actor) → None

Declare a new actor on this broker. Declaring an Actor twice replaces the first actor with the second by name.

Parameters:

actor (Actor) – The actor being declared.

declare_queue(queue_name: str, *, ensure: bool = False) → None
[source]

Declare a queue. Has no effect if a queue with the given name already exists.

Parameters:

queue_name (str) – The name of the new queue.

ensure (bool) – When True, the queue is created on the server, if necessary.

Raises:

ConnectionClosed – When ensure=True if the underlying channel or connection fails.

enqueue(message: Message, *, delay: int | None = None) → Message
[source]

Enqueue a message.

Parameters:

message (Message) – The message to enqueue.

delay (int) – The minimum amount of time, in milliseconds, to delay the message by.

Raises:

ConnectionClosed – If the underlying channel or connection has been closed.

flush(queue_name: str) → None
[source]

Drop all the messages from a queue.

Parameters:

queue_name (str) – The queue to flush.

flush_all() → None
[source]

Drop all messages from all declared queues.

get_actor(actor_name: str) → Actor

Look up an actor by its name.

Parameters:

actor_name (str) – The name to look up.

Raises:

ActorNotFound – If the actor was never declared.

Returns:

The actor.

Return type:

Actor

get_declared_actors() → set[str]

Get all declared actors.

Returns:

The names of all the actors declared so far on this Broker.

Return type:

set[str]

get_declared_delay_queues() → set[str]

Get all declared delay queues.

Returns:

The names of all the delay queues declared so far on this Broker.

Return type:

set[str]

get_declared_queues() → set[str]
[source]

Get all declared queues.

Returns:

The names of all the queues declared so far on this Broker.

Return type:

set[str]

get_queue_message_counts(queue_name: str) → tuple[int, int, int]
[source]

Get the number of messages in a queue. This method is only meant to be used in unit and integration tests.

Parameters:

queue_name (str) – The queue whose message counts to get.

Returns:

A triple representing the number of messages in the queue, its delayed queue and its dead letter queue.

Return type:

tuple

get_results_backend() → ResultBackend

Get the backend of the Results middleware.

Raises:

RuntimeError – If the broker doesn’t have a results backend.

Returns:

The backend.

Return type:

ResultBackend

join(queue_name: str, min_successes: int = 10, idle_time: int = 100, *, timeout: int | None = None) → None
[source]

Wait for all the messages on the given queue to be processed. This method is only meant to be used in tests to wait for all the messages in a queue to be processed.

Warning

This method doesn’t wait for unacked messages so it may not be completely reliable. Use the stub broker in your unit tests and only use this for simple integration tests.

Parameters:

queue_name (str) – The queue to wait on.

min_successes (int) – The minimum number of times all the polled queues should be empty.

idle_time (int) – The number of milliseconds to wait between counts.

timeout (Optional[int]) – The max amount of time, in milliseconds, to wait on this queue.

class dramatiq.brokers.redis.RedisBroker(*, url=None, middleware=None, namespace='dramatiq', maintenance_chance=1000, heartbeat_timeout=60000, dead_message_ttl=604800000, client=None, **parameters)
[source]

Bases: Broker

A broker than can be used with Redis.

Examples

If you want to specify connection parameters individually:

>>> RedisBroker(host="127.0.0.1", port=6379, db=0, password="hunter2")


Alternatively, if you want to use a connection URL:

>>> RedisBroker(url="redis://127.0.0.1:6379/0")


See also

redis.Redis for a list of all the available connection parameters.

Parameters:

url (str) – An optional connection URL. If both a URL and connection parameters are provided, the URL is used.

middleware (list[Middleware])

maintenance_chance (int) – How many commands out of a million should trigger queue maintenance.

namespace (str) – The str with which to prefix all Redis keys.

heartbeat_timeout (int) – The amount of time (in ms) that has to pass without a heartbeat for a broker process to be considered offline.

dead_message_ttl (int) – The amount of time (in ms) that dead-lettered messages are kept in Redis for.

client (redis.Redis) – A redis client to use.

**parameters – Connection parameters are passed directly to redis.Redis.

add_middleware(middleware: Middleware, *, before: type[Middleware] | None = None, after: type[Middleware] | None = None) → None

Add a middleware object to this broker. The middleware is appended to the end of the middleware list by default.

You can specify another middleware (by class) as a reference point for where the new middleware should be added.

Duplicates of middleware are allowed. If there’s already a middleware object of the same class added to the broker, the middleware will be added for the second time.

Parameters:

middleware (Middleware) – The middleware.

before (type) – Add this middleware before a specific one.

after (type) – Add this middleware after a specific one.

Raises:

ValueError – When either before or after refer to a middleware that hasn’t been registered yet.

close() → None

Close this broker and perform any necessary cleanup actions.

consume(queue_name: str, prefetch: int = 1, timeout: int = 5000) → Consumer
[source]

Create a new consumer for a queue.

Parameters:

queue_name (str) – The queue to consume.

prefetch (int) – The number of messages to prefetch.

timeout (int) – The idle timeout in milliseconds.

Returns:

A consumer that retrieves messages from Redis.

Return type:

Consumer

declare_actor(actor: Actor) → None

Declare a new actor on this broker. Declaring an Actor twice replaces the first actor with the second by name.

Parameters:

actor (Actor) – The actor being declared.

declare_queue(queue_name: str) → None
[source]

Declare a queue. Has no effect if a queue with the given name has already been declared.

Parameters:

queue_name (str) – The name of the new queue.

enqueue(message: Message, *, delay: int | None = None) → Message
[source]

Enqueue a message.

Parameters:

message (Message) – The message to enqueue.

delay (int) – The minimum amount of time, in milliseconds, to delay the message by. Must be less than 7 days.

Raises:

ValueError – If delay is longer than 7 days.

flush(queue_name: str) → None
[source]

Drop all the messages from a queue.

Parameters:

queue_name (str) – The queue to flush.

flush_all() → None
[source]

Drop all messages from all declared queues.

get_actor(actor_name: str) → Actor

Look up an actor by its name.

Parameters:

actor_name (str) – The name to look up.

Raises:

ActorNotFound – If the actor was never declared.

Returns:

The actor.

Return type:

Actor

get_declared_actors() → set[str]

Get all declared actors.

Returns:

The names of all the actors declared so far on this Broker.

Return type:

set[str]

get_declared_delay_queues() → set[str]

Get all declared delay queues.

Returns:

The names of all the delay queues declared so far on this Broker.

Return type:

set[str]

get_declared_queues() → set[str]
[source]

Get all declared queues.

Returns:

The names of all the queues declared so far on this Broker.

Return type:

set[str]

get_results_backend() → ResultBackend

Get the backend of the Results middleware.

Raises:

RuntimeError – If the broker doesn’t have a results backend.

Returns:

The backend.

Return type:

ResultBackend

join(queue_name: str, *, interval: int = 100, timeout: int | None = None) → None
[source]

Wait for all the messages on the given queue to be processed. This method is only meant to be used in tests to wait for all the messages in a queue to be processed.

Raises:

QueueJoinTimeout – When the timeout elapses.

Parameters:

queue_name (str) – The queue to wait on.

interval (Optional[int]) – The interval, in milliseconds, at which to check the queues.

timeout (Optional[int]) – The max amount of time, in milliseconds, to wait on this queue.

class dramatiq.brokers.stub.StubBroker(middleware: list[Middleware] | None = None, *, fail_fast_default: bool = True)
[source]

Bases: Broker

A broker that can be used within unit tests.

Parameters:

middleware – See Broker.

fail_fast_default – Specifies the default value for the fail_fast argument of join.

add_middleware(middleware: Middleware, *, before: type[Middleware] | None = None, after: type[Middleware] | None = None) → None

Add a middleware object to this broker. The middleware is appended to the end of the middleware list by default.

You can specify another middleware (by class) as a reference point for where the new middleware should be added.

Duplicates of middleware are allowed. If there’s already a middleware object of the same class added to the broker, the middleware will be added for the second time.

Parameters:

middleware (Middleware) – The middleware.

before (type) – Add this middleware before a specific one.

after (type) – Add this middleware after a specific one.

Raises:

ValueError – When either before or after refer to a middleware that hasn’t been registered yet.

close() → None

Close this broker and perform any necessary cleanup actions.

consume(queue_name: str, prefetch: int = 1, timeout: int = 100) → Consumer
[source]

Create a new consumer for a queue.

Parameters:

queue_name (str) – The queue to consume.

prefetch (int) – The number of messages to prefetch.

timeout (int) – The idle timeout in milliseconds.

Raises:

QueueNotFound – If the queue hasn’t been declared.

Returns:

A consumer that retrieves messages from Redis.

Return type:

Consumer

property dead_letters: list[MessageProxy]

The dead-lettered messages for all defined queues.

declare_actor(actor: Actor) → None

Declare a new actor on this broker. Declaring an Actor twice replaces the first actor with the second by name.

Parameters:

actor (Actor) – The actor being declared.

declare_queue(queue_name: str) → None
[source]

Declare a queue. Has no effect if a queue with the given name has already been declared.

Parameters:

queue_name (str) – The name of the new queue.

enqueue(message: Message, *, delay: int | None = None) → Message
[source]

Enqueue a message.

Parameters:

message (Message) – The message to enqueue.

delay (int) – The minimum amount of time, in milliseconds, to delay the message by.

Raises:

QueueNotFound – If the queue the message is being enqueued on doesn’t exist.

flush(queue_name: str) → None
[source]

Drop all the messages from a queue.

Parameters:

queue_name (str) – The queue to flush.

flush_all() → None
[source]

Drop all messages from all declared queues.

get_actor(actor_name: str) → Actor

Look up an actor by its name.

Parameters:

actor_name (str) – The name to look up.

Raises:

ActorNotFound – If the actor was never declared.

Returns:

The actor.

Return type:

Actor

get_declared_actors() → set[str]

Get all declared actors.

Returns:

The names of all the actors declared so far on this Broker.

Return type:

set[str]

get_declared_delay_queues() → set[str]

Get all declared delay queues.

Returns:

The names of all the delay queues declared so far on this Broker.

Return type:

set[str]

get_declared_queues() → set[str]

Get all declared queues.

Returns:

The names of all the queues declared so far on this Broker.

Return type:

set[str]

get_results_backend() → ResultBackend

Get the backend of the Results middleware.

Raises:

RuntimeError – If the broker doesn’t have a results backend.

Returns:

The backend.

Return type:

ResultBackend

join(queue_name: str, *, timeout: int | None = None, fail_fast: bool | None = None) → None
[source]

Wait for all the messages on the given queue to be processed. This method is only meant to be used in tests to wait for all the messages in a queue to be processed.

Raises:

QueueJoinTimeout – When the timeout elapses.

QueueNotFound – If the given queue was never declared.

Parameters:

queue_name (str) – The queue to wait on.

fail_fast (bool) – When this is True and any message gets dead-lettered during the join, then an exception will be raised. When False, no exception will be raised. Defaults to None, which means use the value of the fail_fast_default instance attribute (which defaults to True).

timeout (Optional[int]) – The max amount of time, in milliseconds, to wait on this queue.

Changed in version 2.0.0: The fail_fast parameter now defaults to self.fail_fast_default (which defaults to True).

Middleware
Middleware Base Class

This defines the hooks available for middleware to implement, and can be subclassed to implement custom middleware.

class dramatiq.Middleware
[source]

Base class for broker middleware. The default implementations for all hooks are no-ops and subclasses may implement whatever subset of hooks they like.

property actor_options: set[str]

The set of options that may be configured on each actor.

property forks: list[Callable[[], int]]

A list of functions to run in separate forks of the main process.

before_ack(broker: Broker, message: MessageProxy) → None
[source]

Called before a message is acknowledged.

after_ack(broker: Broker, message: MessageProxy) → None
[source]

Called after a message has been acknowledged.

before_nack(broker: Broker, message: MessageProxy) → None
[source]

Called before a message is rejected.

after_nack(broker: Broker, message: MessageProxy) → None
[source]

Called after a message has been rejected.

before_declare_actor(broker: Broker, actor: Actor) → None
[source]

Called before an actor is declared.

after_declare_actor(broker: Broker, actor: Actor) → None
[source]

Called after an actor has been declared.

before_declare_queue(broker: Broker, queue_name: str) → None
[source]

Called before a queue is declared.

after_declare_queue(broker: Broker, queue_name: str) → None
[source]

Called after a queue has been declared.

This signals that the queue has been registered with the broker, but it does not necessarily mean that it was created on the server yet. For example, the RabbitMQ broker declares queues when actors are created, but it doesn’t instantiate them until messages are enqueued or consumed.

after_declare_delay_queue(broker: Broker, queue_name: str) → None
[source]

Called after a delay queue has been declared.

before_enqueue(broker: Broker, message: Message, delay: int) → None
[source]

Called before a message is enqueued (including retries).

after_enqueue(broker: Broker, message: Message, delay: int) → None
[source]

Called after a message has been enqueued (including retries).

before_delay_message(broker: Broker, message: MessageProxy) → None
[source]

Called before a message has been delayed in worker memory.

before_process_message(broker: Broker, message: MessageProxy) → None
[source]

Called before a message is processed.

Raises:

SkipMessage – If the current message should be skipped. When this is raised, after_skip_message is emitted instead of after_process_message.

after_process_message(broker: Broker, message: MessageProxy, *, result: Any | None = None, exception: BaseException | None = None) → None
[source]

Called after a message has been processed.

after_skip_message(broker: Broker, message: MessageProxy) → None
[source]

Called instead of after_process_message after a message has been skipped.

after_process_boot(broker: Broker) → None
[source]

Called immediately after subprocess start up.

before_worker_boot(broker: Broker, worker: Worker) → None
[source]

Called before the worker process starts up.

after_worker_boot(broker: Broker, worker: Worker) → None
[source]

Called after the worker process has started up.

before_worker_shutdown(broker: Broker, worker: Worker) → None
[source]

Called before the worker process shuts down.

after_worker_shutdown(broker: Broker, worker: Worker) → None
[source]

Called after the worker process shuts down.

after_consumer_thread_boot(broker: Broker, thread: ConsumerThread) → None
[source]

Called from a consumer thread after it starts but before it starts its run loop.

before_consumer_thread_shutdown(broker: Broker, thread: ConsumerThread) → None
[source]

Called before a consumer thread shuts down. This may be used to clean up thread-local resources (such as Django database connections).

after_worker_thread_boot(broker: Broker, thread: WorkerThread) → None
[source]

Called from a worker thread after it starts but before it starts its run loop.

before_worker_thread_shutdown(broker: Broker, thread: WorkerThread) → None
[source]

Called before a worker thread shuts down. This may be used to clean up thread-local resources (such as Django database connections).

Default Middleware

The following middleware classes are all enabled by default, with their default settings.

class dramatiq.middleware.AgeLimit(*, max_age: int | None = None)
[source]

Middleware that drops messages that have been in the queue for too long.

Parameters:

max_age (int) – The default message age limit in milliseconds. Defaults to None, meaning that messages can exist indefinitely.

class dramatiq.middleware.Callbacks
[source]

Middleware that lets you chain success and failure callbacks onto Actors.

Parameters:

on_failure (str) – The name of an actor to send a message to on failure.

on_success (str) – The name of an actor to send a message to on success.

class dramatiq.middleware.Pipelines
[source]

Middleware that lets you pipe actors together so that the output of one actor feeds into the input of another.

Parameters:

pipe_ignore (bool) – When True, ignores the result of the previous actor in the pipeline.

pipe_target (dict) – A message representing the actor the current result should be fed into.

class dramatiq.middleware.Retries(*, max_retries: int = 20, min_backoff: int | None = None, max_backoff: int | None = None, retry_when: Callable[[int, BaseException], bool] | None = None)
[source]

Middleware that automatically retries failed tasks with exponential backoff.

Disabling this middleware will cause messages that fail due to exceptions to be marked ‘done’ rather than ‘failed’. If you don’t want actors to retry automatically, it’s better to set their max_retries options to 0 than to remove this middleware.

If you need to intentionally retry an actor and you don’t want the exception to get logged, then consider raising the Retry exception from within your actor.

Actors that have their throws option set to an exception class or a tuple of exception classes will not be retried if one of those exceptions is raised within them. For example:

>>> @actor(throws=(RuntimeError,))
... def example():
...     raise RuntimeError("never retried")

Parameters:

max_retries (int) – The maximum number of times tasks can be retried.

min_backoff (int) – The minimum amount of backoff milliseconds to apply to retried tasks. Defaults to 15 seconds.

max_backoff (int) – The maximum amount of backoff milliseconds to apply to retried tasks. Defaults to 7 days.

retry_when (Callable[[int, BaseException], bool]) – An optional predicate that can be used to programmatically determine whether a task should be retried or not. This takes precedence over max_retries when set.

on_retry_exhausted (str) – Name of an actor to send a message to when message is failed due to retries being exceeded.

class dramatiq.middleware.ShutdownNotifications(notify_shutdown: bool = False)
[source]

Middleware that interrupts actors whose worker process has been signaled for termination. Currently, this is only available on CPython.

Note

This works by setting an async exception in the worker thread that runs the actor. This means that the exception will only get called the next time that thread acquires the GIL. Concretely, this means that this middleware can’t cancel system calls.

Parameters:

notify_shutdown (bool) – When True, the actor will be interrupted if the worker process was terminated. Defaults to False, meaning actors will not be interrupted, and allowed to finish.

class dramatiq.middleware.TimeLimit(*, time_limit: float = 600000, interval: int = 1000)
[source]

Middleware that cancels actors that run for too long. Currently, this is only available on CPython.

Note

This works by setting an async exception in the worker thread that runs the actor. This means that the exception will only get called the next time that thread acquires the GIL. Concretely, this means that this middleware can’t cancel system calls.

Parameters:

time_limit (float) – The maximum number of milliseconds actors may run for. Use float(“inf”) to avoid setting a timeout for the actor. Defaults to 10 minutes (600,000 milliseconds).

interval (int) – The interval (in milliseconds) with which to check for actors that have exceeded the limit. This does not take effect when using gevent because the timers are managed by gevent. Defaults to 1 second (1,000 milliseconds).

Optional Middleware

The following middleware classes are available, but not enabled by default.

class dramatiq.middleware.AsyncIO
[source]

This middleware manages the event loop thread for async actors.

class dramatiq.middleware.CurrentMessage
[source]

Middleware that exposes the current message via a thread-local variable.

Example

>>> import dramatiq
>>> from dramatiq.middleware import CurrentMessage

>>> @dramatiq.actor
... def example(x):
...     print(CurrentMessage.get_current_message())
...
>>> example.send(1)

classmethod get_current_message() → Message[Any] | None
[source]

Get the message that triggered the current actor. Messages are thread local so this returns None when called outside of actor code.

class dramatiq.middleware.GroupCallbacks(rate_limiter_backend: RateLimiterBackend, *, barrier_ttl: int = 86400000)
[source]

Middleware that enables adding completion callbacks to Groups.

class dramatiq.middleware.prometheus.Prometheus
[source]

A middleware that exports stats via Prometheus.

class dramatiq.results.Results

Middleware that automatically stores actor results. See dramatiq.results.Results for details.

Middleware Errors

The class hierarchy for middleware exceptions:

BaseException
+-- Exception
|   +-- dramatiq.middleware.MiddlewareError
|       +-- dramatiq.middleware.SkipMessage
+-- dramatiq.middleware.Interrupt
    +-- dramatiq.middleware.Shutdown
    +-- dramatiq.middleware.TimeLimitExceeded

exception dramatiq.middleware.MiddlewareError
[source]

Bases: Exception

Base class for middleware errors.

exception dramatiq.middleware.SkipMessage
[source]

Bases: MiddlewareError

An exception that may be raised by Middleware inside the before_process_message hook in order to skip a message.

exception dramatiq.middleware.Interrupt
[source]

Bases: BaseException

Base class for exceptions used to asynchronously interrupt a thread’s execution. An actor may catch these exceptions in order to respond gracefully, such as performing any necessary cleanup.

This is not a subclass of DramatiqError to avoid it being caught unintentionally.

exception dramatiq.middleware.TimeLimitExceeded
[source]

Bases: Interrupt

Exception used to interrupt worker threads when actors exceed their time limits.

exception dramatiq.middleware.Shutdown
[source]

Bases: Interrupt

Exception used to interrupt worker threads when their worker processes have been signaled for termination.

Results

Actor results can be stored and retrieved by leveraging result backends and the results middleware. Results and result backends are not enabled by default and you should avoid using them until you have a really good use case. Most of the time you can get by with actors simply updating data in your database instead of using results.

Results Middleware
class dramatiq.results.Results(*, backend, store_results=False, result_ttl=None)
[source]

Middleware that automatically stores actor results.

Example

>>> from dramatiq.results import Results
>>> from dramatiq.results.backends import RedisBackend
>>> backend = RedisBackend()
>>> broker.add_middleware(Results(backend=backend))

>>> @dramatiq.actor(store_results=True)
... def add(x, y):
...     return x + y

>>> message = add.send(1, 2)
>>> message.get_result(backend=backend)
3

>>> @dramatiq.actor(store_results=True)
... def fail():
...     raise Exception("failed")

>>> message = fail.send()
>>> message.get_result(backend=backend)
Traceback (most recent call last):
  ...
ResultFailure: actor raised Exception: failed

Parameters:

backend (ResultBackend) – The result backend to use when storing results.

store_results (bool) – Whether or not actor results should be stored. Defaults to False and can be set on a per-actor basis.

result_ttl (int) – The maximum number of milliseconds results are allowed to exist in the backend. Defaults to 10 minutes and can be set on a per-actor basis.

Warning

If you have retries turned on for an actor that stores results, then the result of a message may be delayed until its retries run out!

Results Backends
class dramatiq.results.ResultBackend(*, namespace: str = 'dramatiq-results', encoder: Encoder | None = None)
[source]

ABC for result backends.

Parameters:

namespace (str) – The logical namespace under which the data should be stored.

encoder (Encoder) – The encoder to use when storing and retrieving result data. Defaults to JSONEncoder.

build_message_key(message) → str
[source]

Given a message, return its globally-unique key.

Parameters:

message (Message)

Returns:

str

get_result(message, *, block: bool = False, timeout: int | None = None) → Any
[source]

Get a result from the backend.

Parameters:

message (Message)

block (bool) – Whether or not to block until a result is set.

timeout (int) – The maximum amount of time, in ms, to wait for a result when block is True. Defaults to 10 seconds.

Raises:

ResultMissing – When block is False and the result isn’t set.

ResultTimeout – When waiting for a result times out.

Returns:

The result.

Return type:

object

store_exception(message, exception: Exception, ttl: int) → None
[source]

Store an exception in the backend.

Parameters:

message (Message)

exception (Exception)

ttl (int) – The maximum amount of time the exception may be stored in the backend for.

store_result(message, result: Any, ttl: int) → None
[source]

Store a result in the backend.

Parameters:

message (Message)

result (object) – Must be serializable.

ttl (int) – The maximum amount of time the result may be stored in the backend for.

unwrap_result(res)
[source]

Unwrap the serialized result. Passes through to unwrap_result() by default, but can be overridden to complement changes to how store_result() or store_exception() serialize their results.

Parameters:

res (object) – The result data, typically a dict.

Returns:

The result.

Return type:

object

class dramatiq.results.backends.MemcachedBackend(*, namespace='dramatiq-results', encoder=None, pool=None, pool_size=8, **parameters)
[source]

Bases: ResultBackend

A result backend for Memcached. This backend uses long polling to retrieve results.

Parameters:

namespace (str) – A string with which to prefix result keys.

encoder (Encoder) – The encoder to use when storing and retrieving result data. Defaults to JSONEncoder.

pool (ClientPool) – An optional pylibmc client pool to use. If this is passed, all other connection params are ignored.

pool_size (int) – The size of the connection pool to use.

**parameters – Connection parameters are passed directly to pylibmc.Client.

class dramatiq.results.backends.RedisBackend(*, namespace='dramatiq-results', encoder=None, client=None, url=None, **parameters)
[source]

Bases: ResultBackend

A result backend for Redis. This is the recommended result backend as waiting for a result is resource efficient.

Parameters:

namespace (str) – A string with which to prefix result keys.

encoder (Encoder) – The encoder to use when storing and retrieving result data. Defaults to JSONEncoder.

client (Redis) – An optional client. If this is passed, then all other parameters are ignored.

url (str) – An optional connection URL. If both a URL and connection parameters are provided, the URL is used.

**parameters – Connection parameters are passed directly to redis.Redis.

class dramatiq.results.backends.StubBackend(*, namespace: str = 'dramatiq-results', encoder: Encoder | None = None)
[source]

Bases: ResultBackend

An in-memory result backend. For use in unit tests.

Parameters:

namespace (str) – A string with which to prefix result keys.

encoder (Encoder) – The encoder to use when storing and retrieving result data. Defaults to JSONEncoder.

Rate Limiters

Rate limiters can be used to determine whether or not an operation can be run at the current time across many processes and machines by using a shared storage backend.

Rate Limiters Backends

Rate limiter backends are used to store metadata about rate limits.

class dramatiq.rate_limits.RateLimiterBackend
[source]

ABC for rate limiter backends.

add(key, value, ttl)
[source]

Add a key to the backend iff it doesn’t exist.

Parameters:

key (str) – The key to add.

value (int) – The value to add.

ttl (int) – The max amount of time in milliseconds the key can live in the backend for.

decr(key, amount, minimum, ttl)
[source]

Atomically decrement a key in the backend up to the given maximum.

Parameters:

key (str) – The key to decrement.

amount (int) – The amount to decrement the value by.

minimum (int) – The minimum amount the value can have.

ttl (int) – The max amount of time in milliseconds the key can live in the backend for.

Returns:

True if the key was successfully decremented.

Return type:

bool

incr(key, amount, maximum, ttl)
[source]

Atomically increment a key in the backend up to the given maximum.

Parameters:

key (str) – The key to increment.

amount (int) – The amount to increment the value by.

maximum (int) – The maximum amount the value can have.

ttl (int) – The max amount of time in milliseconds the key can live in the backend for.

Returns:

True if the key was successfully incremented.

Return type:

bool

incr_and_sum(key, keys, amount, maximum, ttl)
[source]

Atomically increment a key unless the sum of keys is greater than the given maximum.

Parameters:

key (str) – The key to increment.

keys (callable) – A callable to return the list of keys to be summed over.

amount (int) – The amount to decrement the value by.

maximum (int) – The maximum sum of the keys.

ttl (int) – The max amount of time in milliseconds the key can live in the backend for.

Returns:

True if the key was successfully incremented.

Return type:

bool

wait(key, timeout)
[source]

Wait until an event is published to the given key or the timeout expires. This is used to implement efficient blocking against a synchronized resource.

Parameters:

key (str) – The key to wait on.

timeout (int) – The timeout in milliseconds.

Returns:

True if en event was published before the timeout.

Return type:

bool

wait_notify(key, ttl)
[source]

Notify parties wait()ing on a key that an event has occurred. The default implementation is a no-op.

Parameters:

key (str) – The key to notify on.

ttl (int) – The max amount of time in milliseconds that the notification should exist for.

Returns:

None

class dramatiq.rate_limits.backends.MemcachedBackend(*, pool=None, pool_size=8, **parameters)
[source]

Bases: RateLimiterBackend

A rate limiter backend for Memcached.

Examples

>>> from dramatiq.rate_limits.backends import MemcachedBackend
>>> backend = MemcachedBackend(servers=["127.0.0.1"], binary=True)

Parameters:

pool (ClientPool) – An optional pylibmc client pool to use. If this is passed, all other connection params are ignored.

pool_size (int) – The size of the connection pool to use.

**parameters – Connection parameters are passed directly to pylibmc.Client.

class dramatiq.rate_limits.backends.RedisBackend(*, client=None, url=None, **parameters)
[source]

Bases: RateLimiterBackend

A rate limiter backend for Redis.

Parameters:

client (Redis) – An optional client. If this is passed, then all other parameters are ignored.

url (str) – An optional connection URL. If both a URL and connection parameters are provided, the URL is used.

**parameters – Connection parameters are passed directly to redis.Redis.

class dramatiq.rate_limits.backends.StubBackend
[source]

Bases: RateLimiterBackend

An in-memory rate limiter backend. For use in unit tests.

Limiters
class dramatiq.rate_limits.RateLimiter(backend, key)
[source]

ABC for rate limiters.

Examples

>>> from dramatiq.rate_limits.backends import RedisBackend

>>> backend = RedisBackend()
>>> limiter = ConcurrentRateLimiter(backend, "distributed-mutex", limit=1)

>>> with limiter.acquire(raise_on_failure=False) as acquired:
...     if not acquired:
...         print("Mutex not acquired.")
...         return
...
...     print("Mutex acquired.")

Parameters:

backend (RateLimiterBackend) – The rate limiting backend to use.

key (str) – The key to rate limit on.

acquire(*, raise_on_failure=True)
[source]

Attempt to acquire a slot under this rate limiter.

Parameters:

raise_on_failure (bool) – Whether or not failures should raise an exception. If this is false, the context manager will instead return a boolean value representing whether or not the rate limit slot was acquired.

Returns:

Whether or not the slot could be acquired.

Return type:

bool

class dramatiq.rate_limits.BucketRateLimiter(backend, key, *, limit=1, bucket=1000)
[source]

Bases: RateLimiter

A rate limiter that ensures that only up to limit operations may happen over some time interval.

Examples

Up to 10 operations every second:

>>> BucketRateLimiter(backend, "some-key", limit=10, bucket=1_000)


Up to 1 operation every minute:

>>> BucketRateLimiter(backend, "some-key", limit=1, bucket=60_000)


Warning

Bucket rate limits are cheap to maintain but are susceptible to burst “attacks”. Given a bucket rate limit of 100 per minute, an attacker could make a burst of 100 calls in the last second of a minute and then another 100 calls in the first second of the subsequent minute.

For a rate limiter that doesn’t have this problem (but is more expensive to maintain), see WindowRateLimiter.

Parameters:

backend (RateLimiterBackend) – The backend to use.

key (str) – The key to rate limit on.

limit (int) – The maximum number of operations per bucket per key.

bucket (int) – The bucket interval in milliseconds.

class dramatiq.rate_limits.ConcurrentRateLimiter(backend, key, *, limit=1, ttl=900000)
[source]

Bases: RateLimiter

A rate limiter that ensures that only limit concurrent operations may happen at the same time.

Note

You can use a concurrent rate limiter of size 1 to get a distributed mutex.

Parameters:

backend (RateLimiterBackend) – The backend to use.

key (str) – The key to rate limit on.

limit (int) – The maximum number of concurrent operations per key.

ttl (int) – The time in milliseconds that keys may live for.

class dramatiq.rate_limits.WindowRateLimiter(backend, key, *, limit=1, window=1)
[source]

Bases: RateLimiter

A rate limiter that ensures that only limit operations may happen over some sliding window.

Note

Windows are in seconds rather that milliseconds. This is different from most durations and intervals used in Dramatiq, because keeping metadata at the millisecond level is far too expensive for most use cases.

Parameters:

backend (RateLimiterBackend) – The backend to use.

key (str) – The key to rate limit on.

limit (int) – The maximum number of operations per window per key.

window (int) – The window size in seconds. The wider the window, the more expensive it is to maintain.

Barriers
class dramatiq.rate_limits.Barrier(backend, key, *, ttl=900000)
[source]

A distributed barrier.

Examples

>>> from dramatiq.rate_limits import Barrier
>>> from dramatiq.rate_limits.backends import RedisBackend

>>> backend = RedisBackend()
>>> barrier = Barrier(backend, "some-barrier", ttl=30_000)

>>> created = barrier.create(parties=3)
>>> barrier.wait(block=False)
False
>>> barrier.wait(block=False)
False
>>> barrier.wait(block=False)
True

Parameters:

backend (BarrierBackend) – The barrier backend to use.

key (str) – The key for the barrier.

ttl (int) – The TTL for the barrier key, in milliseconds.

create(parties)
[source]

Create the barrier for the given number of parties.

Parameters:

parties (int) – The number of parties to wait for.

Returns:

Whether or not the new barrier was successfully created.

Return type:

bool

wait(*, block=True, timeout=None)
[source]

Signal that a party has reached the barrier.

Warning

Barrier blocking is currently only supported by the stub and Redis backends.

Warning

Re-using keys between blocking calls may lead to undefined behaviour. Make sure your barrier keys are always unique (use a UUID).

Parameters:

block (bool) – Whether or not to block while waiting for the other parties.

timeout (int) – The maximum number of milliseconds to wait for the barrier to be cleared.

Returns:

Whether or not the barrier has been reached by all parties.

Return type:

bool

Workers
class dramatiq.Worker(broker: Broker, *, queues: set[str] | None = None, worker_timeout: int = 1000, worker_threads: int = 8)
[source]

Workers consume messages off of all declared queues and distribute those messages to individual worker threads for processing. Workers don’t block the current thread so it’s up to the caller to keep it alive.

Don’t run more than one Worker per process.

Parameters:

broker (Broker)

queues (set[str]) – An optional subset of queues to listen on. By default, if this is not provided, the worker will listen on all declared queues.

worker_timeout (int) – The number of milliseconds workers should wake up after if the queue is idle.

worker_threads (int) – The number of worker threads to spawn.

join() → None
[source]

Wait for this worker to complete its work in progress. This method is useful when testing code.

pause() → None
[source]

Pauses all the worker threads.

resume() → None
[source]

Resumes all the worker threads.

start() → None
[source]

Initialize the worker boot sequence and start up all the worker threads.

stop(timeout: int = 600000) → None
[source]

Gracefully stop the Worker and all of its consumers and workers.

Parameters:

timeout (int) – The number of milliseconds to wait for everything to shut down.

Errors
exception dramatiq.DramatiqError(message)
[source]

Bases: Exception

Base class for all dramatiq errors.

exception dramatiq.BrokerError(message)
[source]

Bases: DramatiqError

Base class for broker-related errors.

exception dramatiq.DecodeError(message, data, error)
[source]

Bases: DramatiqError

Raised when a message fails to decode.

exception dramatiq.ActorNotFound(message)
[source]

Bases: BrokerError

Raised when a message is sent to an actor that hasn’t been declared.

exception dramatiq.QueueNotFound(message)
[source]

Bases: BrokerError

Raised when a message is sent to an queue that hasn’t been declared.

exception dramatiq.ConnectionError(message)
[source]

Bases: BrokerError

Base class for broker connection-related errors.

exception dramatiq.ConnectionClosed(message)
[source]

Bases: ConnectionError

Raised when a broker connection is suddenly closed.

exception dramatiq.ConnectionFailed(message)
[source]

Bases: ConnectionError

Raised when a broker connection could not be opened.

exception dramatiq.RateLimitExceeded(message)
[source]

Bases: DramatiqError

Raised when a rate limit has been exceeded.

exception dramatiq.Retry(message: str = '', delay: int | None = None)
[source]

Bases: DramatiqError

Actors may raise this error when they should be retried. This behaves just like any other exception from the perspective of the Retries middleware, the only difference is it doesn’t get logged as an error.

If the delay argument is provided, then the message will be retried after at least that amount of time (in milliseconds).

exception dramatiq.results.ResultError(message)
[source]

Bases: DramatiqError

Base class for result errors.

exception dramatiq.results.ResultMissing(message)
[source]

Bases: ResultError

Raised when a result can’t be found.

exception dramatiq.results.ResultTimeout(message)
[source]

Bases: ResultError

Raised when waiting for a result times out.

exception dramatiq.results.ResultFailure(message='', orig_exc_type='', orig_exc_msg='')
[source]

Bases: ResultError

Raised when getting a result from an actor that failed.

Environment Variables

These are the environment variables that dramatiq reads

Name

	

Default

	

Description




dramatiq_restart_delay

	

3000 (3 seconds)

	

The number of milliseconds to wait before restarting consumers after a connection error.




dramatiq_queue_prefetch

	

2 times number of worker threads

	

The number of messages to prefetch from the queue for each worker process. In-progress messages are included in the count.




dramatiq_delay_queue_prefetch

	

1000 times number of worker threads

	

The number of messages to prefetch from the delay queue for each worker.




dramatiq_dead_message_ttl

	

604800000 (One week)

	

The maximum amount of time a message can be in the dead letter queue for the RabbitMQ Broker (in milliseconds).




dramatiq_group_callback_barrier_ttl

	

86400000 (One day)

	

Deprecated. Use the barrier_ttl parameter of GroupCallbacks middleware instead.




dramatiq_prom_db

	

tempfile.gettempdir()/dramatiq-prometheus

	

The path to store the prometheus database files. See Gotchas with Prometheus.




dramatiq_prom_host

	

0.0.0.0

	

See Prometheus Metrics.




dramatiq_prom_port

	

9191

	

See Prometheus Metrics.




dramatiq_worker_timeout

	

1000

	

The number of milliseconds workers should wake up after if the queue is idle.







Navigation
Installation
Motivation
User Guide
Best Practices
Troubleshooting
Advanced Topics
Cookbook
API Reference
Functions
Actors & Messages
Brokers
Middleware
Results
Rate Limiters
Workers
Errors
Environment Variables
Source Code
Changelog
PyPI
Contributing
Discussion Board
Project License
Quick search
Sponsors
Franz — Desktop Client for Apache Kafka


Podcatcher — iOS Podcast Player
©2017, 2018, 2019 CLEARTYPE SRL. | Powered by Sphinx 8.1.3 & Alabaster 1.0.0 | Page source
