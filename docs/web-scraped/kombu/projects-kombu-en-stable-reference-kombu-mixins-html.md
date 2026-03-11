# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html

Title: kombu.mixins — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html

Published Time: Mon, 29 Dec 2025 20:31:32 GMT

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.mixins.html).

Mixin Classes - `kombu.mixins`[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#mixin-classes-kombu-mixins "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Mixins.

_class_ kombu.mixins.ConsumerMixin[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin "Link to this definition")
Convenience mixin for implementing consumer programs.

It can be used outside of threads, with threads, or greenthreads (eventlet/gevent) too.

The basic class would need a [`connection`](https://docs.celeryq.dev/en/main/userguide/extending.html#connection "(in Celery v5.6)") attribute which must be a [`Connection`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Connection "kombu.Connection") instance, and define a [`get_consumers()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.get_consumers "kombu.mixins.ConsumerMixin.get_consumers") method that returns a list of [`kombu.Consumer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer "kombu.Consumer") instances to use. Supporting multiple consumers is important so that multiple channels can be used for different QoS requirements.

Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#example "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

> class Worker(ConsumerMixin):
>     task_queue = Queue('tasks', Exchange('tasks'), 'tasks')
> 
>     def  __init__ (self, connection):
>         self.connection = None
> 
>     def get_consumers(self, Consumer, channel):
>         return [Consumer(queues=[self.task_queue],
>                          callbacks=[self.on_task])]
> 
>     def on_task(self, body, message):
>         print('Got task: {0!r}'.format(body))
>         message.ack()

\*:meth:`extra_context`
Optional extra context manager that will be entered after the connection and consumers have been set up.

Takes arguments `(connection, channel)`.

\*:meth:`on_connection_error`
Handler called if the connection is lost/ or is unavailable.

Takes arguments `(exc, interval)`, where interval is the time in seconds when the connection will be retried.

The default handler will log the exception.

\*:meth:`on_connection_revived`
Handler called as soon as the connection is re-established after connection failure.

Takes no arguments.

\*:meth:`on_consume_ready`
Handler called when the consumer is ready to accept messages.

Takes arguments `(connection, channel, consumers)`. Also keyword arguments to `consume` are forwarded to this handler.

\*:meth:`on_consume_end`
Handler called after the consumers are canceled. Takes arguments `(connection, channel)`.

\*:meth:`on_iteration`
Handler called for every iteration while draining events.

Takes no arguments.

\*:meth:`on_decode_error`
Handler called if a consumer was unable to decode the body of a message.

Takes arguments `(message, exc)` where message is the original message object.

The default handler will log the error and acknowledge the message, so if you override make sure to call super, or perform these steps yourself.

Consumer()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.Consumer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.Consumer "Link to this definition")_property_ channel_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.channel_errors "Link to this definition")connect_max_retries _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.connect_max_retries "Link to this definition")
maximum number of retries trying to re-establish the connection, if the connection is lost/unavailable.

_property_ connection_errors[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.connection_errors "Link to this definition")consume(_limit=None_, _timeout=None_, _safety\_interval=1_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.consume "Link to this definition")consumer_context(_**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.consumer_context)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.consumer_context "Link to this definition")create_connection()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.create_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.create_connection "Link to this definition")establish_connection()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.establish_connection)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.establish_connection "Link to this definition")get_consumers(_Consumer_, _channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.get_consumers)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.get_consumers "Link to this definition")maybe_conn_error(_fun_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.maybe_conn_error)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.maybe_conn_error "Link to this definition")
Use `kombu.common.ignore_errors()` instead.

on_connection_error(_exc_, _interval_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.on_connection_error)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.on_connection_error "Link to this definition")on_connection_revived()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.on_connection_revived)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.on_connection_revived "Link to this definition")on_consume_end(_connection_, _channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.on_consume_end)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.on_consume_end "Link to this definition")on_consume_ready(_connection_, _channel_, _consumers_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.on_consume_ready)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.on_consume_ready "Link to this definition")on_decode_error(_message_, _exc_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.on_decode_error)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.on_decode_error "Link to this definition")on_iteration()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.on_iteration)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.on_iteration "Link to this definition")_property_ restart_limit[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.restart_limit "Link to this definition")run(_\_tokens=1_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerMixin.run)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.run "Link to this definition")should_stop _=False_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerMixin.should_stop "Link to this definition")
When this is set to true the consumer should stop consuming and return, so that it can be joined if it is the implementation of a thread.

_class_ kombu.mixins.ConsumerProducerMixin[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerProducerMixin)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerProducerMixin "Link to this definition")
Consumer and Producer mixin.

Version of ConsumerMixin having separate connection for also publishing messages.

Example:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#id1 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

> class Worker(ConsumerProducerMixin):
> 
>     def  __init__ (self, connection):
>         self.connection = connection
> 
>     def get_consumers(self, Consumer, channel):
>         return [Consumer(queues=Queue('foo'),
>                          on_message=self.handle_message,
>                          accept='application/json',
>                          prefetch_count=10)]
> 
>     def handle_message(self, message):
>         self.producer.publish(
>             {'message': 'hello to you'},
>             exchange='',
>             routing_key=message.properties['reply_to'],
>             correlation_id=message.properties['correlation_id'],
>             retry=True,
>         )

on_consume_end(_connection_, _channel_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/mixins.html#ConsumerProducerMixin.on_consume_end)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerProducerMixin.on_consume_end "Link to this definition")_property_ producer[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerProducerMixin.producer "Link to this definition")_property_ producer_connection[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.mixins.html#kombu.mixins.ConsumerProducerMixin.producer_connection "Link to this definition")
