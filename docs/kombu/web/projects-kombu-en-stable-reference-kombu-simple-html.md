# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html

Title: Simple Messaging API - kombu.simple — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.simple.html).

Simple messaging interface.

*   [Persistent](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#persistent)

*   [Buffer](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#buffer)

[Persistent](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#id1)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#persistent "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.simple.SimpleQueue(_channel_, _name_, _no\_ack=None_, _queue\_opts=None_, _queue\_args=None_, _exchange\_opts=None_, _serializer=None_, _compression=None_, _accept=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/simple.html#SimpleQueue)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue "Link to this definition")
Simple API for persistent queues.

channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.channel "Link to this definition")
Current channel

producer[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.producer "Link to this definition")
[`Producer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer "kombu.Producer") used to publish messages.

consumer[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.consumer "Link to this definition")
[`Consumer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer "kombu.Consumer") used to receive messages.

no_ack[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.no_ack "Link to this definition")
flag to enable/disable acknowledgments.

queue[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.queue "Link to this definition")
[`Queue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue "kombu.Queue") to consume from (if consuming).

queue_opts[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.queue_opts "Link to this definition")
> Additional options for the queue declaration.

exchange_opts[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.exchange_opts "Link to this definition")
Additional options for the exchange declaration.

get(_block=True_, _timeout=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.get "Link to this definition")get_nowait()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.get_nowait "Link to this definition")put(_message_, _serializer=None_, _headers=None_, _compression=None_, _routing\_key=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.put "Link to this definition")clear()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.clear "Link to this definition") __len__ ()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.__len__ "Link to this definition")
len(self) -> self.qsize().

qsize()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.qsize "Link to this definition")close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleQueue.close "Link to this definition")
[Buffer](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#id2)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#buffer "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

_class_ kombu.simple.SimpleBuffer(_channel_, _name_, _no\_ack=None_, _queue\_opts=None_, _queue\_args=None_, _exchange\_opts=None_, _serializer=None_, _compression=None_, _accept=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/simple.html#SimpleBuffer)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer "Link to this definition")
Simple API for ephemeral queues.

channel[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.channel "Link to this definition")
Current channel

producer[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.producer "Link to this definition")
[`Producer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Producer "kombu.Producer") used to publish messages.

consumer[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.consumer "Link to this definition")
[`Consumer`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Consumer "kombu.Consumer") used to receive messages.

no_ack[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.no_ack "Link to this definition")
flag to enable/disable acknowledgments.

queue[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.queue "Link to this definition")
[`Queue`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.html#kombu.Queue "kombu.Queue") to consume from (if consuming).

queue_opts[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.queue_opts "Link to this definition")
> Additional options for the queue declaration.

exchange_opts[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.exchange_opts "Link to this definition")
Additional options for the exchange declaration.

get(_block=True_, _timeout=None_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.get "Link to this definition")get_nowait()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.get_nowait "Link to this definition")put(_message_, _serializer=None_, _headers=None_, _compression=None_, _routing\_key=None_, _**kwargs_)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.put "Link to this definition")clear()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.clear "Link to this definition") __len__ ()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.__len__ "Link to this definition")
len(self) -> self.qsize().

qsize()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.qsize "Link to this definition")close()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.simple.html#kombu.simple.SimpleBuffer.close "Link to this definition")
