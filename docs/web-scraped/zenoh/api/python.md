# Zenoh Python API

..
.. Copyright (c) 2017, 2022 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh team, <zenoh@zettascale.tech>
..

API Reference
=============

module zenoh
------------

.. automodule:: zenoh
    :members:
    :undoc-members:

module zenoh.handlers
---------------------

.. automodule:: zenoh.handlers
    :members:
    :undoc-members:

module zenoh.ext
----------------

.. automodule:: zenoh.ext
    :members:
    :undoc-members:

module zenoh.shm
----------------

.. automodule:: zenoh.shm
    :members:
    :undoc-members:

---

..
.. Copyright (c) 2017, 2022 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh team, <zenoh@zettascale.tech>
..

Components and Concepts
=======================

.. _session-and-config:

Session and Config
------------------

Zenoh supports two paradigms of communication: :ref:`publish-subscribe` and :ref:`query-reply`. The entities
that perform communication (for example, publishers, subscribers, queriers, and queryables) are
declared through a :class:`zenoh.Session`. A session is created by the :func:`zenoh.open` function,
which takes a :class:`zenoh.Config` as an argument.

The configuration is stored in a JSON file and can be read with :func:`zenoh.Config.from_file`.
The file format is documented in the Zenoh Rust API
`Config <https://docs.rs/zenoh/latest/zenoh/config/struct.Config.html>`_ reference.

.. important::

   The recommended way to create a session is using a context manager (``with`` statement).
   If a session is not explicitly closed or managed with a context manager, on exit object 
   finalizers may be called when the library thread has already been killed, which can
   cause the script to hang.

   Either use a context manager (recommended) or explicitly call :meth:`zenoh.Session.close`
   before your script exits. See examples in the :doc:`quickstart` section.

Example: Creating a session with context manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/session_config.py
   :language: python
   :start-after: [session_context_manager]
   :end-before: # [session_context_manager]

Example: Creating a session with explicit close
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/session_config.py
   :language: python
   :start-after: [session_explicit_close]
   :end-before: # [session_explicit_close]

.. _key-expressions:

Key Expressions
---------------

`Key expressions <https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Key%20Expressions.md>`_ are Zenoh's address space.

In Zenoh, data is associated with keys in the form of a slash-separated path, e.g., ``robot/sensor/temp``. The
requesting side uses key expressions to address the data of interest. Key expressions can contain
wildcards:

- ``*`` matches any chunk (a chunk is a sequence of characters between ``/`` separators)
- ``**`` matches any number of chunks (including zero chunks)

For example:

- ``robot/sensor/*`` matches ``robot/sensor/temp``, ``robot/sensor/humidity``, etc.
- ``robot/**`` matches ``robot/sensor/temp``, ``robot/actuator/motor``, ``robot/status``, etc.

The :class:`zenoh.KeyExpr` class provides validation and operations on key
expressions. The :class:`zenoh.KeyExpr` constructor validates the syntax of the provided string
and raises a :class:`zenoh.ZError` exception if the syntax is invalid (e.g., it contains spaces, other illegal characters, or has empty chunks like ``foo//bar`` or ``/foo``).

The :class:`zenoh.KeyExpr` constructor raises an exception for key expressions that are valid but not in
`canonical form <https://github.com/eclipse-zenoh/roadmap/blob/main/rfcs/ALL/Key%20Expressions.md#canon-forms>`_.
For example, ``robot/sensor/**/*`` is valid, but its canonical form is ``robot/sensor/*/**``.
The :meth:`zenoh.KeyExpr.autocanonize` method can accept such key expressions and
convert them to their canonical form.

Example: Validating key expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/keyexpr_validation.py
   :language: python
   :start-after: [keyexpr_validation]
   :end-before: # [keyexpr_validation]

Key expressions support operations such as intersection and inclusion (see
:meth:`zenoh.KeyExpr.intersects` and :meth:`zenoh.KeyExpr.includes`), which
help determine how different expressions relate to each other.

Example: Performing operations on key expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/keyexpr_operations.py
   :language: python
   :start-after: [keyexpr_operations]
   :end-before: # [keyexpr_operations]

Key expressions can also be declared with the session to optimize routing and
network usage:

Example: Declaring key expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/keyexpr_declare.py
   :language: python
   :start-after: [keyexpr_declare]
   :end-before: # [keyexpr_declare]

.. _publish-subscribe:

Publish/Subscribe
-----------------

Data is published via a :class:`zenoh.Publisher`, which is declared using
:meth:`zenoh.Session.declare_publisher`. The publisher exposes two primary operations:
:meth:`zenoh.Publisher.put` and :meth:`zenoh.Publisher.delete`. Publishing can also be performed
directly from the session via :meth:`zenoh.Session.put` and :meth:`zenoh.Session.delete`.

Published data is received as :class:`zenoh.Sample` instances by a :class:`zenoh.Subscriber`,
which is declared using :meth:`zenoh.Session.declare_subscriber`. The samples are delivered to the
callback or channel (:ref:`channels-and-callbacks`).

Publishing can express two different semantics:

- producing a sequence of values
- updating a single value associated with a key expression

In the second case, it is necessary to indicate that a key is no longer associated
with any value; the :meth:`zenoh.Publisher.delete` operation is used for this.

On the receiving side, the subscriber distinguishes between
:attr:`zenoh.SampleKind.PUT` and :attr:`zenoh.SampleKind.DELETE` using the
:attr:`zenoh.Sample.kind` field in the :class:`zenoh.Sample` structure.

The delete operation allows a subscriber to work with a :class:`zenoh.Queryable`
that caches the values associated with key expressions.

Example: Declaring a publisher and publishing data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/pubsub_publisher.py
   :language: python
   :start-after: [pubsub_publisher]
   :end-before: # [pubsub_publisher]

Example: Declaring a subscriber and receiving data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/pubsub_subscriber.py
   :language: python
   :start-after: [pubsub_subscriber]
   :end-before: # [pubsub_subscriber]

Example: Using session methods directly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/pubsub_session_direct.py
   :language: python
   :start-after: [pubsub_session_direct]
   :end-before: # [pubsub_session_direct]

.. _query-reply:

Query/Reply
-----------

In the query/reply paradigm, data is made available by a :class:`zenoh.Queryable` and
requested by a :class:`zenoh.Querier` or directly via :meth:`zenoh.Session.get`.

A :class:`zenoh.Queryable` is declared using :meth:`zenoh.Session.declare_queryable`. 
It serves :class:`zenoh.Query` requests via a callback or channel
(:ref:`channels-and-callbacks`).

The :class:`zenoh.Query` provides the :meth:`zenoh.Query.reply` method to reply with a
data sample of the :attr:`zenoh.SampleKind.PUT` kind, and
:meth:`zenoh.Query.reply_del` to send a :attr:`zenoh.SampleKind.DELETE` reply.
See :ref:`publish-subscribe` for more details on the difference between the
two sample kinds. There is also the :meth:`zenoh.Query.reply_err` method 
which can be used to send a reply containing error information.

Data is requested from queryables via :meth:`zenoh.Session.get` or via a
:class:`zenoh.Querier` object. Each request returns zero or more
:class:`zenoh.Reply` structures — one per queryable that matches the request.
Each reply contains either a :class:`zenoh.Sample` from `reply` and `reply_del`
or a :class:`zenoh.ReplyError` from `reply_err`.

Example: Declaring a queryable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/query_queryable.py
   :language: python
   :start-after: [query_queryable]
   :end-before: # [query_queryable]

Example: Requesting data using Session.get
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/query_session_get.py
   :language: python
   :start-after: [query_session_get]
   :end-before: # [query_session_get]

Example: Using a Querier
~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/query_querier.py
   :language: python
   :start-after: [query_querier]
   :end-before: # [query_querier] 

.. _query-parameters:

Query Parameters
----------------

The query/reply API allows specifying additional parameters for the request.
A :class:`zenoh.Selector` object is passed to the :meth:`zenoh.Session.get` operation.
It combines a key expression with optional parameters and can be constructed from these
elements or by parsing a selector string. The selector string has
a syntax similar to a URL: it is a key expression followed by a question mark
and a list of parameters in the format "name=value", separated by ``;``.
For example: ``key/expression?param1=value1;param2=value2``.

Alternatively, parameters can be constructed programmatically using the
:class:`zenoh.Parameters` class, which accepts a dictionary, and then combined
with a key expression to create a :class:`zenoh.Selector`.

On the receiving side, queryables can access these parameters via
:attr:`zenoh.Query.parameters`.

Example: Constructing a Selector from dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/query_parameters.py
   :language: python
   :start-after: [query_parameters]
   :end-before: # [query_parameters]

.. _data-representation:

Data representation
-------------------

Data is received as :class:`zenoh.Sample` objects, which contain the
:attr:`zenoh.Sample.payload` and associated metadata like :attr:`zenoh.Sample.timestamp`,
:attr:`zenoh.Sample.encoding`, and :attr:`zenoh.Sample.kind`. Additionally, optional
user-defined metadata can be attached via :attr:`zenoh.Sample.attachment`.


Both :attr:`zenoh.Sample.payload` and :attr:`zenoh.Sample.attachment` are of type
:class:`zenoh.ZBytes`, which represents raw byte data. 

Example: Using :class:`zenoh.ZBytes`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/data_representation.py
   :language: python
   :start-after: [raw_data]
   :end-before: # [raw_data]

Serialization and deserialization of basic types and structures is provided in the :mod:`zenoh.ext`
module via :func:`zenoh.ext.z_serialize` and :func:`zenoh.ext.z_deserialize`.

Example: Data serialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/data_representation.py
   :language: python
   :start-after: [serialized_data]
   :end-before: # [serialized_data]

.. _encoding:

Encoding
--------

Zenoh uses :class:`zenoh.Encoding` to indicate how data should be interpreted by the application. An encoding has a similar role to Content-Type in HTTP and is represented as a string in MIME-like format: ``type/subtype[;schema]``.

To optimize network usage, Zenoh internally maps some predefined encoding strings to integer identifiers. These encodings are provided as class attributes of the :class:`zenoh.Encoding` class, such as :attr:`zenoh.Encoding.ZENOH_BYTES`, :attr:`zenoh.Encoding.APPLICATION_JSON`, etc. This internal mapping is not exposed to the application layer, but using these predefined encodings is more efficient than custom strings.

The Zenoh protocol does not impose any encoding value and does not operate on it. It can be seen as optional metadata that is carried over by Zenoh, allowing applications to perform different operations depending on the encoding value.

Additionally, a schema can be associated with the encoding. The convention is to use the ``;`` separator if an encoding is created from a string. Alternatively, :meth:`zenoh.Encoding.with_schema` can be used to add a schema to one of the predefined class attributes.

Example: Creating an :class:`zenoh.Encoding` from a string and vice versa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/encoding.py
   :language: python
   :start-after: [string_operations]
   :end-before: # [string_operations]

Example: Using the schema
~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/encoding.py
   :language: python
   :start-after: [schema]
   :end-before: # [schema]

.. _scouting:

Scouting
--------

Scouting is the process of discovering Zenoh nodes on the network. The scouting
process depends on the transport layer and the Zenoh configuration. Note that
it is not necessary to explicitly discover other nodes to publish, subscribe, or
query data.

Scouting is performed using the :func:`zenoh.scout` function, which returns a
:class:`zenoh.Scout` object that yields :class:`zenoh.Hello` messages for each
discovered Zenoh node.

Scouting is different from :ref:`liveliness <liveliness>` requesting and monitoring. Liveliness
works on the Zenoh protocol logical level and allows getting information about resources in terms of
:ref:`key expressions <key-expressions>`. On the other hand, :ref:`scouting <scouting>` is about discovering Zenoh nodes visible
to the local node on the network. The result of scouting is a list of :class:`zenoh.Hello` messages,
each containing information about a discovered Zenoh node:

- unique node identifier (:attr:`zenoh.Hello.zid`)
- node type (:attr:`zenoh.Hello.whatami`)
- list of node's network addresses (:attr:`zenoh.Hello.locators`)

See more details at `scouting documentation <https://zenoh.io/docs/getting-started/deployment/#scouting>`_.

Example: Scouting for Zenoh nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/scouting.py
   :language: python
   :start-after: [scouting]
   :end-before: # [scouting]

.. _liveliness:

Liveliness
----------

Zenoh supports liveliness monitoring to notify when a specified resource appears
or disappears on the network.

Sometimes it is necessary to know whether a Zenoh node is available. This
can be achieved by declaring special publishers and queryables, but the 
dedicated liveliness API is more convenient and efficient.

The :class:`zenoh.Liveliness` object is created by calling :meth:`zenoh.Session.liveliness`.
It allows a node to declare a :class:`zenoh.LivelinessToken` associated with a key expression.
To declare the token, use :meth:`zenoh.Liveliness.declare_token`.

Other nodes can query this key expression using :meth:`zenoh.Liveliness.get`.
They can also subscribe using :meth:`zenoh.Liveliness.declare_subscriber` to be notified when the token appears or disappears.

The `history` parameter of
:meth:`zenoh.Liveliness.declare_subscriber` allows immediate receipt of tokens
that are already present on the network.


Example: Declaring a liveliness token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/liveliness_token.py
   :language: python
   :start-after: [liveliness_token]
   :end-before: # [liveliness_token]

Example: Getting currently present liveliness tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/liveliness_get.py
   :language: python
   :start-after: [liveliness_get]
   :end-before: # [liveliness_get]

Example: Checking if a liveliness token is present and subscribing to changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/liveliness_subscriber.py
   :language: python
   :start-after: [liveliness_subscriber]
   :end-before: # [liveliness_subscriber]

.. _matching:

Matching
--------

The matching API lets the active side of communication (publisher or querier)
learn whether there are interested parties on the other side (subscriber or
queryable). This information can save bandwidth and CPU resources.

Declare a :class:`zenoh.MatchingListener` via
:meth:`zenoh.Publisher.declare_matching_listener` or
:meth:`zenoh.Querier.declare_matching_listener`.

The matching listener behaves like a subscriber, but instead of producing data
samples it yields :class:`zenoh.MatchingStatus` instances whenever the matching
status changes — for example, when the first matching subscriber or queryable
appears or when the last one disappears.


Example: Declaring a matching listener for a publisher
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/matching_publisher.py
   :language: python
   :start-after: [matching_publisher]
   :end-before: # [matching_publisher]

Example: Declaring a matching listener for a querier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: examples/matching_querier.py
   :language: python
   :start-after: [matching_querier]
   :end-before: # [matching_querier]

.. _channels-and-callbacks:

Channels and callbacks
----------------------

Overview
^^^^^^^^

There are two ways to receive sequential data from Zenoh primitives (for
example, a series of :class:`zenoh.Sample` objects from a
:class:`zenoh.Subscriber` or :class:`zenoh.Reply` objects from a
:class:`zenoh.Query`): by channel or by callback.

This behavior is controlled by the ``handler`` parameter of the declare
methods (for example, :meth:`zenoh.Session.declare_subscriber` and
:meth:`zenoh.Session.declare_querier`). The parameter can be either a callable
(a function or a method) or a channel type (blocking
:class:`zenoh.handlers.FifoChannel` or non-blocking :class:`zenoh.handlers.RingChannel`).
By default, the ``handler`` parameter is ``None``, which uses
:class:`zenoh.handlers.DefaultHandler` (a FIFO channel with default capacity).

Channels
~~~~~~~~

When constructed with a :class:`zenoh.handlers.FifoChannel` or :class:`zenoh.handlers.RingChannel`
as ``handler`` (or using the default one), the returned object is iterable
and can be used in a ``for`` loop to receive data sequentially. It also provides explicit
methods such as :meth:`zenoh.Subscriber.recv` to wait for data and
:meth:`zenoh.Subscriber.try_recv` to attempt a non-blocking receive. The
subscriber (or queryable) is automatically undeclared when the object goes out of scope
or when :meth:`zenoh.Subscriber.undeclare` is explicitly called.

.. literalinclude:: examples/channels.py
   :language: python
   :start-after: [channels]
   :end-before: # [channels]

Callbacks
~~~~~~~~~

.. caution::

   Calling Zenoh API functions, as well as performing any blocking operations from within a callback is disallowed.
   Even if this works in some particular cases, it's unsafe and may lead to deadlocks or crashes at any moment or with
   the future updates of the library.

It is possible to pass a callable object as ``handler``. This callable is invoked for each received
:class:`zenoh.Sample` or :class:`zenoh.Reply`. This also means the subscriber or queryable runs in
**background mode**, i.e., it remains active even if the returned object
goes out of scope. This allows declaring a subscriber without managing the
returned object's lifetime.

.. literalinclude:: examples/callback_simple.py
   :language: python
   :start-after: [callback_simple]
   :end-before: # [callback_simple]


For more advanced callback handling, you can use :class:`zenoh.handlers.Callback`
to create a callback handler with cleanup functionality.

.. literalinclude:: examples/callback_advanced.py
   :language: python
   :start-after: [callback_advanced]
   :end-before: # [callback_advanced]


Custom channel implementation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For advanced use cases, you can implement your own custom channel in Python and pass
it in the tuple form ``(callback, handler)`` where ``callback`` is a callable and ``handler``
is your custom Python object. This solution has the same performance penalties as the
callback API, but it can be useful in some scenarios.

The callback is invoked for each received item and stores the data in the custom channel,
which is accessible via the :meth:`zenoh.Subscriber.handler` property, in the same way
as with built-in channels.

**Custom channel with priority queue**

.. literalinclude:: examples/custom_channel.py
   :language: python
   :start-after: [custom_channel]
   :end-before: # [custom_channel]

**Usage of the custom channel**

.. literalinclude:: examples/custom_channel.py
   :language: python
   :start-after: [custom_channel_usage]
   :end-before: # [custom_channel_usage]

---

# Example: docs--conf.py

```py
#
#
# Copyright (c) 2022 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#
#


# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project setup --------------------------------------------------------------

import tomllib

import zenoh
import zenoh.ext
import zenoh.handlers
import zenoh.shm

# -- Project information -----------------------------------------------------

project = "zenoh-python"
copyright = "2020, ZettaScale Zenoh team, <zenoh@zettascale.tech>"
author = "ZettaScale Zenoh team, <zenoh@zettascale.tech>"

# Extract the release number from the Cargo manifest
with open("../Cargo.toml", "rb") as f:
    release = tomllib.load(f)["package"]["version"]


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
    "enum_tools.autoenum",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "python"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**/*.rs"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

autodoc_typehints = "description"
autodoc_mock_imports = ["zenoh"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
autodoc_member_order = "groupwise"
```

---

# Example: docs--examples--callback_advanced.py

```py
#
# Copyright (c) 2024 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#
import zenoh

# Open session
session = zenoh.open(zenoh.Config())


# [callback_advanced]
def on_sample(sample):
    print(sample.payload.to_string())


def on_cleanup():
    print("Subscriber undeclared")


callback = zenoh.handlers.Callback(on_sample, drop=on_cleanup)
subscriber = session.declare_subscriber("key/expr", callback)
# The subscriber remains active even if 'subscriber' variable is not used
# [callback_advanced]

session.close()
```

---

# Example: docs--examples--callback_simple.py

```py
#
# Copyright (c) 2024 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#
import zenoh

# Open session
session = zenoh.open(zenoh.Config())


# [callback_simple]
def on_sample(sample):
    print(sample.payload.to_string())


# Subscriber runs in background mode
subscriber = session.declare_subscriber("key/expr", on_sample)
# The subscriber remains active even if 'subscriber' variable is not used
# [callback_simple]

session.close()
```

---

# Example: docs--examples--channels.py

```py
#
# Copyright (c) 2024 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#
import threading
import time

import zenoh

# Open session
session = zenoh.open(zenoh.Config())

# [channels]
# Default channel
subscriber_default = session.declare_subscriber("key/expr")

# Explicit FIFO channel with custom capacity
subscriber_fifo = session.declare_subscriber(
    "key/expr", zenoh.handlers.FifoChannel(100)
)

# Ring channel (drops oldest when full)
subscriber_ring = session.declare_subscriber("key/expr", zenoh.handlers.RingChannel(50))
# [channels]

session.close()
```

---

# Example: docs--examples--custom_channel.py

```py
#
# Copyright (c) 2024 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#
import queue
import threading
import time
from collections.abc import Callable
from typing import Generic, TypeVar, Union

import zenoh


# Test support: send data in background
def send_data():
    time.sleep(3)
    for i in range(2):
        session.put("key/expression", f"sample_{i}")


threading.Thread(target=send_data, daemon=True).start()


# [custom_channel]
class PriorityChannel:
    def __init__(self, maxsize=100):
        self.queue: queue.PriorityQueue = queue.PriorityQueue(maxsize)
        # Counter to preserve FIFO order for samples with same priority
        self._counter = 0

    def recv(self) -> zenoh.Sample:
        return self.queue.get()[2]

    def send(self, sample: zenoh.Sample):
        self.queue.put((sample.priority, self._counter, sample))
        self._counter += 1

    # [custom_channel]
    def count(self) -> int:
        return self.queue.qsize()


# [custom_channel_usage]
with zenoh.open(zenoh.Config()) as session:
    channel = PriorityChannel(maxsize=50)
    subscriber = session.declare_subscriber("key/expression", (channel.send, channel))
    sample = subscriber.handler.recv()
    print(f">> Received: {sample.payload.to_string()}")
    # [custom_channel_usage]
    # one sample should remain in the channel
    time.sleep(1)  # wait a bit for the background sender
    assert channel.count() == 1  # verify that one sample is still in the channel
```

---

# Example: docs--examples--data_representation.py

```py
#
# Copyright (c) 2024 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#
import zenoh

# [raw_data]
# Raw bytes
payload = zenoh.ZBytes(b"Hello, World!")
data = payload.to_bytes()
assert isinstance(data, bytes)
assert data == b"Hello, World!"

# String data
payload = zenoh.ZBytes("Hello, World!")
text = payload.to_string()
assert isinstance(text, str)
assert text == "Hello, World!"
# [raw_data]

# [serialized_data]
# Using zenoh.ext for serialization
from zenoh.ext import z_deserialize, z_serialize

# Serialize a dictionary
data = {"temperature": 25.5, "humidity": 60.0}
payload = z_serialize(data)
assert isinstance(payload, zenoh.ZBytes)

# Deserialize back
received = z_deserialize(dict[str, float], payload)
assert isinstance(received, dict)
assert received == {"temperature": 25.5, "humidity": 60.0}
# [serialized_data]
```

---

# Example: docs--examples--encoding.py

```py
#
# Copyright (c) 2024 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#

import zenoh

# [string_operations]
encoding = zenoh.Encoding("text/plain")
text = str(encoding)
assert text == "text/plain"
# [string_operations]

# [schema]
encoding1 = zenoh.Encoding("text/plain;utf-8")
encoding2 = zenoh.Encoding.TEXT_PLAIN.with_schema("utf-8")
assert encoding1 == encoding2
assert str(encoding1) == "text/plain;utf-8"
assert str(encoding2) == "text/plain;utf-8"
# [schema]
```

---

# Example: docs--examples--keyexpr_declare.py

```py
import zenoh

# Open session
# [session_creation]
session = zenoh.open(zenoh.Config())
# [session_creation]

# [keyexpr_declare]
# Declare a key expression for optimized routing
declared_ke = session.declare_keyexpr("robot/sensor/temperature")

# Use the declared key expression
publisher = session.declare_publisher(declared_ke)
# [keyexpr_declare]

session.close()
```

---

# Example: docs--examples--keyexpr_operations.py

```py
import zenoh
from zenoh import KeyExpr

# [keyexpr_operations]
# Create a key expression with validation
sensor_ke = KeyExpr("robot/sensor")
assert str(sensor_ke) == "robot/sensor"

# Join with another segment
temp_ke = sensor_ke.join("temp")
assert str(temp_ke) == "robot/sensor/temp"

# Create a wildcard expression
all_sensors = sensor_ke.join("**")
assert str(all_sensors) == "robot/sensor/**"

# Check inclusion
assert all_sensors.includes(temp_ke)
assert not temp_ke.includes(all_sensors)

# Check intersection
assert all_sensors.intersects(temp_ke)
assert not sensor_ke.intersects(KeyExpr("robot/actuator"))
# [keyexpr_operations]
```

---

# Example: docs--examples--keyexpr_validation.py

```py
import zenoh
from zenoh import KeyExpr

# Test verification
valids_created = False
error_caught = False

# Example: Key expression validation
# The KeyExpr constructor validates the syntax and raises ZError on invalid input

# [keyexpr_validation]
try:
    # Valid key expressions
    valid_ke = KeyExpr("robot/sensor/temperature")
    assert str(valid_ke) == "robot/sensor/temperature"
    canonized_ke = KeyExpr.autocanonize("robot/sensor/**/*/**/**")
    assert str(canonized_ke) == "robot/sensor/*/**"

    # Invalid key expression (empty segment)
    invalid_ke = KeyExpr("robot/sensor//*")
    assert True, "This line should not be reached"
except zenoh.ZError as e:
    print(f"Validation error: {e}")
# [keyexpr_validation]
```

---

# Example: docs--examples--liveliness_get.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

import threading

# Test support: declare liveliness token in background
import time


def provide_token():
    time.sleep(0.1)
    token = session.liveliness().declare_token("node/A")
    time.sleep(0.5)


threading.Thread(target=provide_token, daemon=True).start()
time.sleep(0.2)  # Wait for token to be declared

# [liveliness_get]
# Get currently present liveliness tokens
replies = session.liveliness().get("node/A", timeout=5)
for reply in replies:
    if reply.ok:
        print(f"Alive token ('{reply.ok.key_expr}')")
    else:
        print(f"Received (ERROR: '{reply.err.payload.to_string()}')")
    # [liveliness_get]
    break  # Exit after first reply for testing

session.close()
```

---

# Example: docs--examples--liveliness_subscriber.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

import threading

# Test support: declare and undeclare liveliness token in background
import time


def provide_token():
    time.sleep(0.1)
    token = session.liveliness().declare_token("node/A")
    time.sleep(0.2)  # Keep token alive briefly
    token.undeclare()  # Trigger DELETE


threading.Thread(target=provide_token, daemon=True).start()

# Test verification counters
put_count = 0
delete_count = 0

# [liveliness_subscriber]
# Check if a liveliness token is present and subscribe to changes
subscriber = session.liveliness().declare_subscriber("node/A", history=True)
for sample in subscriber:
    if sample.kind == zenoh.SampleKind.PUT:
        print(f"Alive token ('{sample.key_expr}')")
    elif sample.kind == zenoh.SampleKind.DELETE:
        print(f"Dropped token ('{sample.key_expr}')")
    # [liveliness_subscriber]
    # Test verification
    if sample.kind == zenoh.SampleKind.PUT:
        put_count += 1
    elif sample.kind == zenoh.SampleKind.DELETE:
        delete_count += 1

    # Exit after receiving both events
    if put_count > 0 and delete_count > 0:
        break

assert put_count > 0, "Expected at least one PUT sample"
assert delete_count > 0, "Expected at least one DELETE sample"

session.close()
```

---

# Example: docs--examples--liveliness_token.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

# [liveliness_token]
# Declare a liveliness token
token = session.liveliness().declare_token("node/A")
# [liveliness_token]

session.close()
```

---

# Example: docs--examples--matching_publisher.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

import threading

# Test support: declare subscriber, then undeclare to trigger both states
import time

subscriber = session.declare_subscriber("key/expression")


def undeclare_subscriber():
    time.sleep(0.2)  # Let matching=True be received first
    subscriber.undeclare()  # Trigger matching=False


threading.Thread(target=undeclare_subscriber, daemon=True).start()

# Test verification counters
matching_true_count = 0
matching_false_count = 0

# [matching_publisher]
# Declare a matching listener for a publisher
publisher = session.declare_publisher("key/expression")
listener = publisher.declare_matching_listener()
for status in listener:
    if status.matching:
        print(">> Publisher has at least one matching subscriber")
    else:
        print(">> Publisher has no matching subscribers")
    # [matching_publisher]
    # Test verification
    if status.matching:
        matching_true_count += 1
    else:
        matching_false_count += 1

    # Exit after receiving both events
    if matching_true_count > 0 and matching_false_count > 0:
        break

assert matching_true_count > 0, "Expected at least one matching=True status"
assert matching_false_count > 0, "Expected at least one matching=False status"

session.close()
```

---

# Example: docs--examples--matching_querier.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

import threading

# Test support: declare queryable, then undeclare to trigger both states
import time

queryable = session.declare_queryable("service/endpoint")


def undeclare_queryable():
    time.sleep(0.2)  # Let matching=True be received first
    queryable.undeclare()  # Trigger matching=False


threading.Thread(target=undeclare_queryable, daemon=True).start()

# Test verification counters
matching_true_count = 0
matching_false_count = 0

# [matching_querier]
# Declare a matching listener for a querier
querier = session.declare_querier("service/endpoint")
listener = querier.declare_matching_listener()
for status in listener:
    if status.matching:
        print(">> Querier has at least one matching queryable")
    else:
        print(">> Querier has no matching queryables")
    # [matching_querier]
    # Test verification
    if status.matching:
        matching_true_count += 1
    else:
        matching_false_count += 1

    # Exit after receiving both events
    if matching_true_count > 0 and matching_false_count > 0:
        break

assert matching_true_count > 0, "Expected at least one matching=True status"
assert matching_false_count > 0, "Expected at least one matching=False status"

session.close()
```

---

# Example: docs--examples--pubsub_publisher.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

# [pubsub_publisher]
# Declare a publisher and publish data
publisher = session.declare_publisher("key/expression")
publisher.put("value")
# [pubsub_publisher]

session.close()
```

---

# Example: docs--examples--pubsub_session_direct.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

# [pubsub_session_direct]
# Direct put operation
session.put("key/expression", "value")

# Direct delete operation
session.delete("key/expression")
# [pubsub_session_direct]

session.close()
```

---

# Example: docs--examples--pubsub_subscriber.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

import threading

# Test support: send data in background
import time


def send_data():
    time.sleep(0.1)
    session.put("key/expression", "test data")


threading.Thread(target=send_data, daemon=True).start()

# [pubsub_subscriber]
# Declare a subscriber and receive data
subscriber = session.declare_subscriber("key/expression")
for sample in subscriber:
    print(f">> Received {sample.payload.to_string()}")
    # [pubsub_subscriber]
    break  # Exit after first sample for testing

session.close()
```

---

# Example: docs--examples--query_parameters.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

import threading
import time


def provide_queryable():
    time.sleep(0.05)
    queryable = session.declare_queryable("room/temperature/history")
    for query in queryable:
        # Access query parameters
        day = query.parameters.get("day", "unknown")
        format = query.parameters.get("format", "celsius")
        query.reply("room/temperature/history", f"22.5°C on {day} ({format})")
        break


threading.Thread(target=provide_queryable, daemon=True).start()
time.sleep(0.1)  # Wait for queryable to be ready

# Test verification
reply_count = 0

# [query_parameters]
# Create parameters from a dictionary
params = zenoh.Parameters({"day": "2023-03-15", "format": "celsius"})

# Create a selector from key expression and parameters
selector = zenoh.Selector("room/temperature/history", params)

# Request data using the selector
replies = session.get(selector)
for reply in replies:
    if reply.ok:
        print(f">> {reply.ok.payload.to_string()}")
    # [query_parameters]
    # Test verification
    if reply.ok:
        reply_count += 1
        assert "2023-03-15" in reply.ok.payload.to_string()
        assert "celsius" in reply.ok.payload.to_string()

assert reply_count > 0, "Expected at least one reply"

session.close()
```

---

# Example: docs--examples--query_querier.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

import threading

# Test support: provide queryables in background (one success, one error)
import time


def provide_queryable_ok():
    time.sleep(0.05)
    queryable = session.declare_queryable("room/temperature/history")
    for query in queryable:
        query.reply("room/temperature/history", "22.5°C")
        break


def provide_queryable_err():
    time.sleep(0.05)
    queryable = session.declare_queryable("room/temperature/history")
    for query in queryable:
        query.reply_err("sensor malfunction")
        break


threading.Thread(target=provide_queryable_ok, daemon=True).start()
threading.Thread(target=provide_queryable_err, daemon=True).start()
time.sleep(0.1)  # Wait for queryables to be ready

# Test verification counters
ok_count = 0
err_count = 0

# [query_querier]
# Declare a querier for multiple queries
querier = session.declare_querier("room/temperature/history")

# Send a query with parameters
replies = querier.get(parameters="?day=2023-03-15")
for reply in replies:
    if reply.ok:
        print(f">> Temperature is {reply.ok.payload.to_string()}")
    else:
        print(f">> Error: {reply.err.payload.to_string()}")
    # [query_querier]
    # Test verification
    if reply.ok:
        ok_count += 1
    else:
        err_count += 1

assert ok_count > 0, "Expected at least one OK reply"
assert err_count > 0, "Expected at least one error reply"

session.close()
```

---

# Example: docs--examples--query_queryable.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

# Sample data
temperature_data = {"2023-03-15": "22.5°C", "2023-03-16": "23.1°C"}

import threading

# Test support: send all 3 query variants in background
import time


def send_queries():
    time.sleep(0.2)  # Wait for queryable to be ready

    # Send all 3 queries with callback (non-blocking)
    def callback(reply):
        pass

    # Query 1: has data (reply)
    session.get("room/temperature/history?day=2023-03-15", callback)
    # Query 2: no data (reply_del)
    session.get("room/temperature/history?day=2023-03-17", callback)
    # Query 3: missing parameter (reply_err)
    session.get("room/temperature/history", callback)


send_thread = threading.Thread(target=send_queries)
send_thread.start()

# [query_queryable]
# Queryable that replies with temperature data for a given day
queryable = session.declare_queryable("room/temperature/history")
query_count = 0
for query in queryable:
    if "day" in query.selector.parameters:
        day = query.selector.parameters["day"]
        if day in temperature_data:
            query.reply("room/temperature/history", temperature_data[day])
        else:
            query.reply_del("room/temperature/history")
    else:
        query.reply_err("missing day parameter")
    # [query_queryable]
    query_count += 1
    if query_count >= 3:  # Exit after handling all 3 queries
        break

send_thread.join()
session.close()
```

---

# Example: docs--examples--query_session_get.py

```py
import zenoh

# Open session
session = zenoh.open(zenoh.Config())

import threading

# Test support: provide queryables in background (one success, one error)
import time


def provide_queryable_ok():
    time.sleep(0.05)
    queryable = session.declare_queryable("room/temperature/history")
    for query in queryable:
        query.reply("room/temperature/history", "22.5°C")
        break


def provide_queryable_err():
    time.sleep(0.05)
    queryable = session.declare_queryable("room/temperature/history")
    for query in queryable:
        query.reply_err("sensor malfunction")
        break


threading.Thread(target=provide_queryable_ok, daemon=True).start()
threading.Thread(target=provide_queryable_err, daemon=True).start()
time.sleep(0.1)  # Wait for queryables to be ready

# Test verification counters
ok_count = 0
err_count = 0

# [query_session_get]
# Request temperature for a specific day
replies = session.get("room/temperature/history?day=2023-03-15")
for reply in replies:
    if reply.ok:
        print(f">> Temperature is {reply.ok.payload.to_string()}")
    else:
        print(f">> Error: {reply.err.payload.to_string()}")
    # [query_session_get]
    # Test verification
    if reply.ok:
        ok_count += 1
    else:
        err_count += 1

assert ok_count > 0, "Expected at least one OK reply"
assert err_count > 0, "Expected at least one error reply"

session.close()
```

---

# Example: docs--examples--quickstart_get.py

```py
import zenoh

# DOC_EXAMPLE_START
# Get keys/values from zenoh
with zenoh.open(zenoh.Config()) as session:
    for response in session.get("demo/example/**"):
        response = response.ok
        print(f"{response.key_expr} => {response.payload.to_string()}")
# DOC_EXAMPLE_END
```

---

# Example: docs--examples--quickstart_put.py

```py
import zenoh

# DOC_EXAMPLE_START
# Publish a key/value pair onto Zenoh
with zenoh.open(zenoh.Config()) as session:
    session.put("demo/example/hello", "Hello World!")
# DOC_EXAMPLE_END
```

---

# Example: docs--examples--quickstart_sub.py

```py
import threading
import time

import zenoh


def send_data():
    send_session = zenoh.open(zenoh.Config())
    for _ in range(5):
        time.sleep(0.2)
        send_session.put("demo/example/foo/bar", "test data")
    send_session.close()


threading.Thread(target=send_data, daemon=True).start()
received = False

# DOC_EXAMPLE_START
# Subscribe to a set of keys with Zenoh
with zenoh.open(zenoh.Config()) as session:
    with session.declare_subscriber("demo/example/**") as subscriber:
        for sample in subscriber:
            print(f"{sample.key_expr} => {sample.payload.to_string()}")
            # DOC_EXAMPLE_END
            received = True
            break

assert received, "Did not receive any sample within the timeout"
```

---

# Example: docs--examples--scouting.py

```py
import threading

import zenoh

# [scouting]
scout = zenoh.scout(what="peer|router")
threading.Timer(1.0, lambda: scout.stop()).start()
for hello in scout:
    print(hello)
# [scouting]
```

---

# Example: docs--examples--session_config.py

```py
#
# Copyright (c) 2024 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#
import zenoh

# [session_context_manager]
# Recommended: Using context manager
# The session is automatically closed when exiting the 'with' block
with zenoh.open(zenoh.Config()) as session:
    # Use the session
    session.put("demo/example/hello", "Hello World!")
# [session_context_manager]

# [session_explicit_close]
# Alternative: Explicit open and close
# You must explicitly close the session before script exit
session = zenoh.open(zenoh.Config())
try:
    # Use the session
    session.put("demo/example/hello", "Hello World!")
finally:
    # Always close the session
    session.close()
# [session_explicit_close]
```

---

..
.. Copyright (c) 2017, 2022 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh team, <zenoh@zettascale.tech>
..

**************************
Zenoh Python API Reference
**************************

`Zenoh <https://zenoh.io>`_ /zeno/ is a stack that unifies data in motion, data at
rest and computations. It elegantly blends traditional pub/sub with geo distributed
storage, queries and computations, while retaining a level of time and space efficiency
that is well beyond any of the mainstream stacks.

The Zenoh protocol allows nodes to form a graph with an arbitrary topology, such as a mesh, 
a star, or a clique. The zenoh routers keeps the network connected and routes the messages
between the nodes.

This documentation provides an overview of the Zenoh concepts and components and a
reference of the Zenoh python API. For more information about Zenoh, please visit the
documentation section on the `Zenoh website <https://zenoh.io/docs/getting-started/first-app/>`_.
It's useful to consult also the `Zenoh Rust API <https://docs.rs/crate/zenoh/latest/>`_ 
reference since the Python API is a binding over the Rust implementation.

All examples presented in this documentation can be found in the examples/ directory of the
`Zenoh Python GitHub repository <https://github.com/eclipse-zenoh/zenoh-python/tree/main/docs/examples>`_.

Documentation Contents
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   concepts
   api_reference

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

---

..
.. Copyright (c) 2017, 2022 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh team, <zenoh@zettascale.tech>
..

Quick Start Examples
====================

Below are some examples that highlight these key concepts and show how easy it is to get
started with. The more detailed documentation is available in the other sections.

Publish a key/value pair onto Zenoh
-----------------------------------

.. literalinclude:: examples/quickstart_put.py
   :language: python
   :start-after: # DOC_EXAMPLE_START
   :end-before: # DOC_EXAMPLE_END

Subscribe to a set of keys with Zenoh
-------------------------------------

.. literalinclude:: examples/quickstart_sub.py
   :language: python
   :start-after: # DOC_EXAMPLE_START
   :end-before: # DOC_EXAMPLE_END

Get keys/values from zenoh
--------------------------

.. literalinclude:: examples/quickstart_get.py
   :language: python
   :start-after: # DOC_EXAMPLE_START
   :end-before: # DOC_EXAMPLE_END

---

# Zenoh Python Documentation

This directory contains the documentation for zenoh-python, built using [Sphinx](https://www.sphinx-doc.org/).

## Requirements

- Python 3.8 or later
- zenoh-python package built and installed
- Sphinx and related packages (see `requirements.txt`)

## Installation

1. **Build and install zenoh-python:**

   ```bash
   cd /path/to/zenoh-python
   pip install -e .
   ```

2. **Install documentation dependencies:**

   ```bash
   cd docs
   pip install -r requirements.txt
   ```

## Building Documentation

The documentation build process requires converting stub files (`.pyi`) to source files (`.py`) so that Sphinx can extract API documentation.

### Quick Build

Use the provided script to build and open documentation:

```bash
./open.sh
```

This script:

1. Converts stub files to source files
2. Builds HTML documentation
3. Opens the documentation in your browser
4. Restores original files

### Manual Build

If you prefer to build manually:

1. **Convert stubs to sources:**

   ```bash
   python3 stubs_to_sources.py
   ```

2. **Build HTML documentation:**

   ```bash
   make html
   ```

3. **Restore original files:**

   ```bash
   python3 stubs_to_sources.py --recover
   ```

4. **View documentation:**

   Open `_build/html/index.html` in your browser.

## Understanding Stub Conversion

Zenoh-python's API is implemented in Rust via PyO3. The Python type information exists in `.pyi` stub files. However, Sphinx's autodoc cannot read stub files directly - it needs `.py` files.

The `stubs_to_sources.py` script:

- Creates `.py` versions of `.pyi` files with documentation
- Backs up original `.py` files to `_stubs_backup/`
- Keeps `.pyi` files unchanged (they're ignored at runtime)
- Can restore everything with `--recover`

## Documentation Examples

Examples in `docs/examples/` are tested using pytest to ensure they run without errors:

```bash
# Test all docs examples (from project root)
python3 -m pytest tests/examples_check.py::test_docs_examples -v
```

This test:

- Finds all `.py` files in `docs/examples/` using glob patterns
- Runs each example individually as a standalone script
- Verifies each example completes without errors (exit code 0)
- Ensures no timeouts occur (10 second limit per example)

Examplples should exercise all code paths demonstrated in the documentation to ensure they work correctly.

---

sphinx==7.2.6
sphinx_rtd_theme==2.0.0
enum-tools[sphinx]

---

# Example: docs--stubs_to_sources.py

```py
#
# Copyright (c) 2024 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#
"""Transform Python stubs into Python code.

Create `*.py` from `*.pyi`. Also, because overloaded functions doesn't render nicely,
overloaded functions are rewritten in a non-overloaded form. Handler parameter types
are merged, and return type is unspecialized, while handler delegated methods are
kept without the `Never` overload. `serializer`/`deserializer` are kept untouched,
because it's ok.
Moreover, all function parameters annotations are stringified in order to allow
referencing a type not declared yet (i.e. forward reference).

Usage:
    python stubs_to_sources.py          # Convert stubs to sources
    python stubs_to_sources.py --recover # Restore original files from backups
"""

import argparse
import ast
import inspect
import shutil
from collections import defaultdict
from pathlib import Path

PACKAGE = (Path(__file__) / "../../zenoh").resolve()
BACKUP_DIR = Path(__file__).parent / "_stubs_backup"


def _unstable(item):
    warning = ".. warning:: This API has been marked as unstable: it works as advertised, but it may be changed in a future release."
    if item.__doc__:
        item.__doc__ += "\n" + warning
    else:
        item.__doc__ = warning
    return item


class Sourcify(ast.NodeTransformer):
    def __init__(self):
        self.current_cls = None
        # only the first overloaded signature is modified, others are removed
        # modified functions are stored here
        self.overloaded_by_class: defaultdict[str | None, set[str]] = defaultdict(set)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        # remove `from . import ext` kind of imports,
        # as they cause circular import outside of stubs
        return node if node.module is not None else None

    def visit_ClassDef(self, node: ast.ClassDef):
        # register the current class for method name disambiguation
        self.current_cls = node.name
        res = self.generic_visit(node)
        self.current_cls = None
        return res

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # replace _unstable
        if node.name == "_unstable":
            return ast.parse(inspect.getsource(_unstable))
        for decorator in node.decorator_list:
            if isinstance(decorator, ast.Name) and decorator.id == "overload":
                if node.name in self.overloaded_by_class[self.current_cls]:
                    # there is no implementation in stub, so one has to be added
                    # for (de)serializer
                    if node.name in ("serializer", "deserializer"):
                        func = ast.parse(
                            f"def {node.name}(arg, /): {ast.unparse(node.body[0])}"
                        )
                        return [node, func]
                    # remove already modified overloaded signature
                    return None
                self.overloaded_by_class[self.current_cls].add(node.name)
                # (de)serializer is kept overloaded
                if node.name in ("serializer", "deserializer"):
                    return node
                # remove overloaded decorator
                node.decorator_list.clear()
                if node.name not in ("recv", "try_recv", "__iter__"):
                    # retrieve the handled type (Scout/Reply/etc.) from the return type
                    if isinstance(node.returns, ast.Subscript):
                        if isinstance(node.returns.slice, ast.Subscript):
                            # `Subscriber[Handler[Sample]]` case
                            tp = node.returns.slice.slice
                        else:
                            # `Handler[Reply]` case
                            tp = node.returns.slice
                        assert isinstance(tp, ast.Name)
                        # replace `handler` parameter annotation
                        annotation = f"_RustHandler[{tp.id}] | tuple[Callable[[{tp.id}], Any], Any] | Callable[[{tp.id}], Any] | None"
                        for arg in (*node.args.args, *node.args.kwonlyargs):
                            if arg.arg == "handler":
                                arg.annotation = ast.parse(annotation)
                        node.returns = node.returns.value
        # stringify all parameters and return annotation
        for arg in (*node.args.posonlyargs, *node.args.args, *node.args.kwonlyargs):
            if ann := arg.annotation:
                arg.annotation = ast.Constant(f"{ast.unparse(ann)}")
        if ret := node.returns:
            node.returns = ast.Constant(f"{ast.unparse(ret)}")
        return node


def backup_files():
    """Backup .py files that have corresponding .pyi stubs.

    Only backs up .py files that will be overwritten during conversion.
    """
    BACKUP_DIR.mkdir(exist_ok=True)

    for pyi_file in PACKAGE.glob("*.pyi"):
        py_file = PACKAGE / f"{pyi_file.stem}.py"
        if py_file.exists():
            backup_path = BACKUP_DIR / py_file.name
            shutil.copy2(py_file, backup_path)
            print(f"Backed up: {py_file.name}")


def convert_stubs():
    """Convert stub files to source files for documentation."""
    print(f"Converting stubs in: {PACKAGE}")

    # First, backup all files
    backup_files()

    # Now convert stubs
    print()
    for entry in PACKAGE.glob("*.pyi"):
        # read stub file
        with open(entry) as f:
            stub: ast.Module = ast.parse(f.read())
            # update ast to make it like source
            stub = Sourcify().visit(stub)

        # write modified code into source file
        target_path = PACKAGE / f"{entry.stem}.py"
        with open(target_path, "w") as f:
            f.write(ast.unparse(stub))
        print(f"Converted: {entry.name} -> {target_path.name}")

    print(f"\nTo restore, run: python {Path(__file__).name} --recover")


def recover_files():
    """Restore original .py files from backup.

    This removes any .py files created from .pyi stubs and restores the originals.
    """
    if not BACKUP_DIR.exists():
        print(f"Error: Backup directory not found: {BACKUP_DIR}")
        print("Cannot recover - no backups available")
        return

    print(f"Restoring files from: {BACKUP_DIR}")

    # Remove .py files that were created from .pyi stubs
    print()
    for pyi_file in PACKAGE.glob("*.pyi"):
        py_file = PACKAGE / f"{pyi_file.stem}.py"
        if py_file.exists():
            py_file.unlink()
            print(f"Removed: {py_file.name}")

    # Restore the backed-up .py files
    print()
    for backup_file in BACKUP_DIR.glob("*.py"):
        target_path = PACKAGE / backup_file.name
        shutil.copy2(backup_file, target_path)
        print(f"Restored: {backup_file.name}")

    # Clean up backup directory
    shutil.rmtree(BACKUP_DIR)
    print(f"\nRemoved backup directory: {BACKUP_DIR}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert Python stub files to source files for documentation generation"
    )
    parser.add_argument(
        "--recover", action="store_true", help="Restore original files from backup"
    )

    args = parser.parse_args()

    if args.recover:
        recover_files()
    else:
        convert_stubs()


if __name__ == "__main__":
    main()
```

---

<img src="https://raw.githubusercontent.com/eclipse-zenoh/zenoh/main/zenoh-dragon.png" height="150">

[![CI](https://github.com/eclipse-zenoh/zenoh-python/workflows/CI/badge.svg)](https://github.com/eclipse-zenoh/zenoh-python/actions?query=workflow%3A%22CI%22)
[![Documentation Status](https://readthedocs.org/projects/zenoh-python/badge/?version=latest)](https://zenoh-python.readthedocs.io/en/latest/?badge=latest)
[![Discussion](https://img.shields.io/badge/discussion-on%20github-blue)](https://github.com/eclipse-zenoh/roadmap/discussions)
[![Discord](https://img.shields.io/badge/chat-on%20discord-blue)](https://discord.gg/2GJ958VuHs)
[![License](https://img.shields.io/badge/License-EPL%202.0-blue)](https://choosealicense.com/licenses/epl-2.0/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Eclipse Zenoh

The Eclipse Zenoh: Zero Overhead Pub/sub, Store/Query and Compute.

Zenoh (pronounce _/zeno/_) unifies data in motion, data at rest and computations. It carefully blends traditional pub/sub with geo-distributed storages, queries and computations, while retaining a level of time and space efficiency that is well beyond any of the mainstream stacks.

Check the website [zenoh.io](http://zenoh.io) and the [roadmap](https://github.com/eclipse-zenoh/roadmap) for more detailed information.

-------------------------------

# Python API

This repository provides a Python binding based on the main [Zenoh implementation written in Rust](https://github.com/eclipse-zenoh/zenoh).

-------------------------------

## How to install it

The Eclipse zenoh-python library is available on [Pypi.org](https://pypi.org/project/eclipse-zenoh/).
Install the latest available version using `pip` in a [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/):

```bash
pip install eclipse-zenoh
```

:warning:WARNING:warning: zenoh-python is developped in Rust.
On Pypi.org we provide binary wheels for the most common platforms (Linux x86_64, i686, ARMs, MacOS universal2 and Windows amd64). But also a source distribution package for other platforms.
However, for `pip` to be able to build this source distribution, there are some prerequisites:

- `pip` version 19.3.1 minimum (for full support of PEP 517).
   (if necessary upgrade it with command: `'sudo pip install --upgrade pip'` )
- Have a Rust toolchain installed (instructions at [rustup.rs](https://rustup.rs/))

### Supported Python versions and platforms

zenoh-python has been tested with Python 3.8, 3.9, 3.10, 3.11 and 3.12

It relies on the [zenoh](https://github.com/eclipse-zenoh/zenoh/tree/main/zenoh) Rust API which require the full `std` library. See the list in [Rust Platform Support](https://doc.rust-lang.org/nightly/rustc/platform-support.html).

### Enable zenoh features

To enable some compilation features of the Rust library that are disabled by default, for example `shared-memory`, execute the following command:

```bash
pip install eclipse-zenoh --no-binary :all: --config-settings build-args="--features=zenoh/shared-memory"
```

-------------------------------

## How to build it

Requirements:

- Python >= 3.8
- pip >= 19.3.1
- [Rust and Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html). If you already have the Rust toolchain installed, make sure it is up-to-date with:

   ```bash
   rustup update
   ```

### Recommended: Build with Virtual Environment

Using a virtual environment is **strongly recommended** to avoid Python version conflicts and dependency issues.

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install development requirements:

   ```bash
   pip install -r requirements-dev.txt
   ```

3. Build and install in development mode:

   ```bash
   maturin develop --release
   ```

4. Run examples:

   ```bash
   python examples/z_info.py
   ```

When you're done, deactivate the virtual environment:

```bash
deactivate
```

### Alternative: Build without Virtual Environment

If you cannot use a virtual environment, follow these steps carefully:

1. Install development requirements:

   ```bash
   pip install -r requirements-dev.txt
   ```

2. Ensure your system can find the building tool `maturin` (installed by previous step).
   For example, it is placed at _$HOME/.local/bin/maturin_ by default on Ubuntu 20.04.

   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```

3. Build the wheel:

   ```bash
   maturin build --release
   ```

4. Install the built wheel:

   ```bash
   pip install ./target/wheels/*.whl --break-system-packages
   ```

   :warning: **Important:** Systems may have multiple Python installations. Ensure you use the same `pip` that corresponds to the `python3` you intend to use for running examples. You can verify this with:

   ```bash
   pip --version      # Shows which Python version pip uses
   python3 --version  # Shows which Python version python3 uses
   ```

   If they don't match, use `python3 -m pip install ./target/wheels/*.whl` instead to ensure the package is installed for the correct Python version.

5. Run examples using the same Python:

   ```bash
   python3 examples/z_info.py
   ```

-------------------------------

## Building Documentation

To build the documentation locally:

1. Ensure you have zenoh-python installed (follow the build instructions above)

2. Install documentation requirements:

   ```bash
   pip install -r docs/requirements.txt
   ```

3. Build the HTML documentation:

   ```bash
   cd docs
   make html
   ```

4. Open the documentation:

   ```bash
   open _build/html/index.html  # macOS
   # or
   xdg-open _build/html/index.html  # Linux
   # or navigate to docs/_build/html/index.html in your browser
   ```

The documentation is also available online at [zenoh-python.readthedocs.io](https://zenoh-python.readthedocs.io/).

-------------------------------

## Running the Examples

You can install Zenoh Router first (See [the instructions](https://github.com/eclipse-zenoh/zenoh/?tab=readme-ov-file#how-to-install-it)).
Then, run the zenoh-python examples following the instructions in [examples/README.md](https://github.com/eclipse-zenoh/zenoh-python/tree/main/examples#readme)

---

