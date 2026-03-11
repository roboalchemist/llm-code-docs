# Zenoh C++ API

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

*************
API Reference
*************

.. toctree::
   :maxdepth: 10

   commons
   error_handling
   keyexpr
   config
   session
   scouting
   publish_subscribe
   query_reply
   matching
   channels
   cancellation
   interop
   shared_memory
   ext

---

..
.. Copyright (c) 2025 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Query Cancellation
==================

.. doxygenclass:: zenoh::CancellationToken
   :members:
   :membergroups: Constructors Methods Operators

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Channels
========

Classes providing stream interface for Zenoh messages.

.. doxygenenum:: zenoh::channels::RecvError

.. doxygenclass:: zenoh::channels::FifoChannel
    :members:

.. doxygenclass:: zenoh::channels::FifoHandler
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::channels::RingChannel
    :members:

.. doxygenclass:: zenoh::channels::RingHandler
   :members:
   :membergroups: Constructors Operators Methods

---

if(${CMAKE_SOURCE_DIR} STREQUAL ${CMAKE_CURRENT_SOURCE_DIR})
    cmake_minimum_required (VERSION 3.16)
    project(zenohcxx_docs)
else()
    message(STATUS "zenoh-cxx docs")
    include(../cmake/helpers.cmake)
endif()

find_package(Doxygen)
if(NOT DOXYGEN_FOUND)
    message(STATUS "Doxygen not found, skipping docs")
    return()
endif()

find_package(Sphinx)
if(NOT SPHINX_FOUND)
    message(STATUS "Sphinx not found, skipping docs")
    return()
endif()

#
# Doxygen target
#

set(DOXYGEN_OUTPUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/docs/doxygen)
set(DOXYGEN_INDEX_FILE ${DOXYGEN_OUTPUT_DIR}/xml/index.xml)

message(STATUS "Doxygen output dir: ${DOXYGEN_OUTPUT_DIR}")

# Input files are configured in "Doxyfile" with relative paths:
# INPUT = ../include/zenohcxx/base.hxx ../include/zenohcxx/api.hxx
# So on adding/changing header files, they should be added both here and in "Doxyfile"
#
# CMake script will copy the include files and Doxyfile to the build directory
#
# We do not use here "configure_file" from "Doxygen.in" to "Doxygen" scheme,
# because doxygen should work being executed from the source directory.
# This is the case for readthedocs.io where doxygen is executed by "conf.py",
# without CMakeLists.txt.
set(DOXYGEN_INPUT_FILES 
${CMAKE_CURRENT_SOURCE_DIR}/../include/zenohcxx/base.hxx 
${CMAKE_CURRENT_SOURCE_DIR}/../include/zenohcxx/api.hxx
${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile
)
file(MAKE_DIRECTORY ${DOXYGEN_OUTPUT_DIR})
file(MAKE_DIRECTORY ${DOXYGEN_OUTPUT_DIR}/../include)

add_custom_target(Doxygen)

add_custom_command(TARGET Doxygen PRE_BUILD
                   COMMAND ${CMAKE_COMMAND} -E copy_directory
                   ${CMAKE_CURRENT_SOURCE_DIR}/../include
                   ${DOXYGEN_OUTPUT_DIR}/../include)

add_custom_command(TARGET Doxygen PRE_BUILD
                   COMMAND ${CMAKE_COMMAND} -E copy
                   ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile
                   ${DOXYGEN_OUTPUT_DIR}/Doxyfile)

add_custom_command(TARGET Doxygen POST_BUILD
                   BYPRODUCTS ${DOXYGEN_INDEX_FILE}
                   DEPENDS ${DOXYGEN_INPUT_FILES}
                   WORKING_DIRECTORY ${DOXYGEN_OUTPUT_DIR}
                   COMMAND ${DOXYGEN_EXECUTABLE}
                   COMMENT "Generating docs")

#
# Sphinx target
#

set(SPHINX_SOURCE ${CMAKE_CURRENT_SOURCE_DIR})
set(SPHINX_BUILD ${CMAKE_CURRENT_BINARY_DIR}/docs/sphinx)

file (GLOB_RECURSE RST_FILES *.rst)
add_custom_target(Sphinx
                  DEPENDS conf.py ${RST_FILES} ${DOXYGEN_INDEX_FILE}
                  COMMAND ${SPHINX_EXECUTABLE} -b html
                  # Tell Breathe where to find the Doxygen output
                  -Dbreathe_projects.zenohcpp=${DOXYGEN_OUTPUT_DIR}/xml
                  ${SPHINX_SOURCE} ${SPHINX_BUILD}
                  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
                  COMMENT "Generating documentation with Sphinx")

add_custom_target(docs DEPENDS Sphinx)

add_custom_command(TARGET docs POST_BUILD
                   COMMAND ${CMAKE_COMMAND} -E cmake_echo_color --cyan
                   "See read-the-docs html in ${SPHINX_BUILD}/index.html")

---

..
.. Copyright (c) 2024 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Commonly used types
===================

Enums
-----

Enum types are C++ - style typedefs for corrresponding enums of `zenoh-c`_ / `zenoh-pico`_ C API.

.. doxygentypedef:: zenoh::SampleKind
.. doxygentypedef:: zenoh::ConsolidationMode

.. doxygentypedef:: zenoh::Reliability

.. doxygentypedef:: zenoh::CongestionControl

.. doxygentypedef:: zenoh::Priority

.. doxygentypedef:: zenoh::QueryTarget

.. doxygentypedef:: zenoh::WhatAmI
    
.. doxygentypedef:: zenoh::Locality

.. doxygenfunction:: whatami_as_str

.. _zenoh-c: https://zenoh-c.readthedocs.io
.. _zenoh-pico: https://zenoh-pico.readthedocs.io

Source Info
-----------

.. doxygenclass:: zenoh::Id
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenfunction:: zenoh::operator<<(std::ostream &os, const Id &id)

.. doxygenclass:: zenoh::EntityGlobalId
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::SourceInfo
   :members:
   :membergroups: Constructors Operators Methods

Timestamp
---------
.. doxygenclass:: zenoh::Timestamp
   :members:
   :membergroups: Constructors Operators Methods


Encoding
--------
.. doxygenclass:: zenoh::Encoding
   :members:
   :membergroups: Constructors Operators Methods

Sample
------
.. doxygenclass:: zenoh::Sample
   :members:
   :membergroups: Constructors Operators Methods

Bytes
------
.. doxygenclass:: zenoh::Bytes
   :members:
   :membergroups: Constructors Operators Methods

Logging
-------

.. doxygenfunction:: try_init_log_from_env
.. doxygenfunction:: init_log_from_env_or

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Configuration
=============

.. doxygenclass:: zenoh::Config
   :members:
   :membergroups: Constructors Operators Methods

---

..
.. Copyright (c) 2024 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Error Handling
==============

All failable Zenoh methods accept pointer to zenoh::ZResult as an optional argument.
If it is not provided (or set to ``nullptr``) a ``zenoh::ZException`` will be thrown in case of failure.
Otherwise a error code will be written to provided pointer and no exception will be thrown from Zenoh side.
If corresponding method is expected to return or consume (via ``std::move``) any objects, they will be reset to
gravestone state (i.e. None of the functions or methods will work with the object in this state, except 
explicit conversion to ``bool``, which will return false).

.. doxygenclass:: zenoh::ZException
   :members:
   :membergroups: Constructors Operators Methods
   
.. doxygentypedef:: zenoh::ZResult

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

********
Examples
********

.. toctree::
    :maxdepth: 10

    session_ex
    pubsub
    queryable

---

..
.. Copyright (c) 2024 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Extensions
==========
Extra functionality, which is not a part of core Zenoh API.

Serialization / Deserialization
-------------------------------
Support for data serialization and deserialization.

.. doxygenclass:: zenoh::ext::Serializer
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::ext::Deserializer
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenfunction:: zenoh::ext::serialize
.. doxygenfunction:: zenoh::ext::deserialize


Session Extension
-----------------
Extra Zenoh entities.

.. doxygenclass:: zenoh::ext::SessionExt
   :members:
   :membergroups: Constructors Operators Methods Fields

.. doxygenclass:: zenoh::ext::PublicationCache
   :members:
   :membergroups: Constructors Operators Methods Fields

.. doxygenclass:: zenoh::ext::QueryingSubscriber
   :members:
   :membergroups: Constructors Operators Methods Fields

.. doxygenclass:: zenoh::ext::AdvancedPublisher
   :members:
   :membergroups: Constructors Operators Methods Fields

.. doxygenclass:: zenoh::ext::AdvancedSubscriber
   :members:
   :membergroups: Constructors Operators Methods Fields

.. doxygenstruct:: zenoh::ext::Miss
   :members:
   :membergroups: Constructors Operators Methods Fields
   
.. doxygenclass:: zenoh::ext::SampleMissListener
   :members:
   :membergroups: Constructors Operators Methods

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Index
=====

.. Dummy file, which is actually replaced with autogenerated genidex.html
.. This hack found here:
.. https://stackoverflow.com/questions/40556423/how-can-i-link-the-generated-index-page-in-readthedocs-navigation-bar

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

*********
zenoh-cpp
*********

The *zenoh-cpp* library provides a client C++ API for the zenoh network protocol.

An introduction to Zenoh and its concepts is available on `zenoh.io`_. Since the zenoh-cpp is a header-only wrapper 
library over the `zenoh-c`_ and `zenoh-pico`_ C libraries, it can be useful to reference the documentation of these libraries as well.
The zenoh-c library is C interface to main implementation of zenoh in Rust (see `zenoh`_ Rust API api documentation for more information).

.. toctree::
    :maxdepth: 10

    examples
    api
    genindex

.. _zenoh.io: https://zenoh.io
.. _zenoh: https://docs.rs/zenoh
.. _zenoh-c: https://zenoh-c.readthedocs.io
.. _zenoh-pico: https://zenoh-pico.readthedocs.io 

---

..
.. Copyright (c) 2024 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Interoperability with zenoh-c / zenoh-pico
==========================================
This is the list of the functions that can be use for interoperability between zenoh-c/zenoh-pico and
zenoh-cpp. These functions essentially perform conversion of c-structs into c++ classes and back. They should be used with
care, and it is up to the user to ensure that all necessary invariants uphold.

.. doxygennamespace:: zenoh::interop
    :content-only:

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Key Expression
===============

.. doxygenclass:: zenoh::KeyExpr
   :members:
   :membergroups: Constructors Operators Methods

---

Matching
========
Classes related to getting information about matching Zenoh entities.

.. doxygenstruct:: zenoh::MatchingStatus
   :members:
   :membergroups: Constructors Operators Methods Fields
   
.. doxygenclass:: zenoh::MatchingListener
   :members:
   :membergroups: Constructors Operators Methods

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Publish-Subscribe
=================
Classes related to publish-subscribe pattern.

.. doxygenclass:: zenoh::Publisher
   :members:
   :membergroups: Constructors Operators Methods Fields
   
.. doxygenclass:: zenoh::Subscriber
   :members:
   :membergroups: Constructors Operators Methods

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Publish / Subscribe
===================

The publish / subscribe pattern is implemented with classes :cpp:class:`zenoh::Publisher`
and :cpp:class:`zenoh::Subscriber`.

Publisher example:

.. code-block:: c++

    #include "zenoh.hxx"

    using namespace zenoh;

    int main(int argc, char **argv) {
       Config config = Config::create_default();
       auto session = Session::open(std::move(config));
       // Publish without creating a Publisher object
       session.put(KeyExpr("demo/example/simple"), Bytes("Simple from session.put!"));

       // Publish from a Publisher object
       auto publisher = session.declare_publisher(KeyExpr("demo/example/simple"));
       publisher.put("Simple from publisher.put!");
    }

Subscriber example:

.. code-block:: c++

    #include "zenoh.hxx"
    #include <iostream>

    using namespace zenoh;

    int main(int argc, char **argv) {
       Config config = Config::create_default();
       auto session = Session::open(std::move(config));
       auto subscriber = session.declare_subscriber(
          KeyExpr("demo/example/simple"),
          [](const Sample& sample) {
             std::cout << "Received: " << sample.get_payload().as_string() << std::endl;
          },
          closures::none
       );
       // Wait for a key press to exit
       char c = getchar();
    }

Subscriber example with non-blocking stream interface:

.. code-block:: c++

    #include "zenoh.hxx"
    #include <chrono>
    #include <iostream>
    #include <thread>

    using namespace zenoh;
    using namespace std::chrono_literals;

    int main(int argc, char **argv) {
       Config config = Config::create_default();
       auto session = Session::open(std::move(config));
       auto subscriber = session.declare_subscriber(
          KeyExpr("demo/example/simple"),
          channels::FifoChannel(16)  // use FIFO buffer to store unprocessed messages
       );
       while (true) {
          auto res = subscriber.handler().try_recv();
          if (std::holds_alternative<Sample>(res)) {
             std::cout << "Received: " << std::get<Sample>(res).get_payload().as_string() << std::endl;
          } else if (std::get<channels::RecvError>(res) == channels::RecvError::Z_NODATA) {
             std::this_thread::sleep_for(1s); // do some other work
          } else {
             break; // channel is closed
          }
       }
    }

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Query-Reply
===========
Classes related to query-reply pattern.

.. doxygenclass:: zenoh::Querier
   :members:
   :membergroups: Constructors Operators Methods Fields

.. doxygenclass:: zenoh::Queryable
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::Query
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::QueryConsolidation
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::Reply
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::ReplyError
   :members:
   :membergroups: Constructors Operators Methods

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Queryable
=========

The data query pattern is implemented by the 
:cpp:class:`zenoh::Queryable` and :cpp:func:`zenoh::Session::get`.

Queryable example:

.. code-block:: c++

   #include "zenoh.hxx"
   #include <iostream>
   using namespace zenoh;

   int main(int argc, char **argv) {
      auto queryable_keyexpr = KeyExpr("demo/example/simple");
      Config config = Config::create_default();
      auto session = Session::open(std::move(config));
      auto queryable = session.declare_queryable(
            queryable_keyexpr, 
            [&queryable_expr](const Query& query) {
               std::cout << "Received Query '" 
                        << query.get_keyexpr().as_string_view() 
                        << "?" << query.get_parameters() << std::endl;
               query.reply(queryable_expr, Bytes::serialize("42"));
         },
         closures::none
      );
      // Wait for a key press to exit
      c = getchar();
   }

Client example. Notice that reply callback may receive error message instead of a sample.
Also notice that the callback is processed asynchronously, so the client must not exit immediately.

.. code-block:: c++

   #include "zenoh.hxx"
   using namespace zenoh;

   int main(int argc, char **argv) {
      Config config = Config::create_default();
      auto session = Session::open(std::move(config));

      auto on_reply = [](const Reply& reply) {
         if (reply.is_ok()) {
            auto&& sample = reply.get_ok();
            std::cout << "Received ('" << sample.get_keyexpr().as_string_view() << "' : '"
                      << sample.get_payload().deserialize<std::string>() << "')\n";
         } else {
            auto&& err = reply.get_err();
            std::cout << "Received an error :" 
                      << error.get_payload().deserialzie<std::string>() << "\n";
         }
      };

      auto on_done = []() {
         std::cout << "No more replies" << std::endl;
      };

      // Send a query and pass two callbacks: one for processing the reply 
      // and one for handle the end of replies
      session.get(KeyExpr("demo/example/simple"), "", on_reply, on_done);

      // Do not exit immediately, give time to process replies
      // Better to wait on a mutex signalled by the on_done callback
      c = getchar();
   }

Client example using blocking stream interface. Notice that reply callback may receive error message instead of a sample.
Also notice that the callback is processed asynchronously, so the client must not exit immediately.

.. code-block:: c++

   #include "zenoh.hxx"
   using namespace zenoh;

   int main(int argc, char **argv) {
      Config config = Config::create_default();
      auto session = Session::open(std::move(config));

      // Send a query and receive a stream providing replies.
      // We will receive a FIFO buffer to store unprocessed replies (with size of 16).
      auto replies = session.get(KeyExpr("demo/example/simple"), "", channels::FifoChannel(16));
      while (true) {
         auto res = replies.recv();
         Reply* reply = std::get_if(&res);
         if (reply == nullptr) break;
         if (reply->is_ok()) {
            const Sample& sample = reply->get_ok();
            std::cout << "Received ('" << sample.get_keyexpr().as_string_view() << "' : '"
                      << sample.get_payload().as_string() << "')\n";
         } else {
            const ReplyError& error = reply->get_err();
            std::cout << "Received an error :" 
                      << error.get_payload().as_string() << "\n";
         }
         
      }

      std::cout << "No more replies" << std::endl;
   }

---

# Building the documentation

## Install tools

- Ubuntu

  ```bash
  sudo apt install doxygen
  ```

- MacOS

  ```bash
  brew install doxygen
  ```

```bash
pip3 install sphinx
pip3 install breathe
pip3 install sphinx-rtd-theme
```

## Build documentation locally

```bash
git clone https://github.com/eclipse-zenoh/zenoh-cpp.git
mkdir build
cmake -Szenoh-cpp -Bbuild
```

the output should be

```raw
...
-- Found Doxygen: /usr/bin/doxygen (found version "1.9.1") found components: doxygen missing components: dot
-- Found Sphinx: /home/username/.local/bin/sphinx-build  
...
```

or something like this. If doxygen or sphinx are not found, check first step. If everything is ok,
build the documentation with this command:

```bash
cmake --build build --target docs
```

If everything is ok, the output is

```raw
...
See read-the-docs html in /username/build/docs/docs/sphinx/index.html
...
```

---

sphinx==7.2.6
sphinx_rtd_theme
breathe

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Scouting
========

.. doxygenfunction:: zenoh::scout

.. doxygenclass:: zenoh::Hello
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenstruct:: zenoh::ScoutOptions
   :members:

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Session
=======

The zenoh session is created using the :cpp:func:`zenoh::Session::open` function, 
consuming the configuration object :cpp:class:`zenoh::Config`.
Then a string is published on "demo/example/simple" key expression.

.. code-block:: c++

   #include "zenoh.hxx"
   using namespace zenoh;

   int main(int argc, char **argv) {
      try {
         Config config = Config::create_default();
         auto session = Session::open(std::move(config));
         session.put(KeyExpr("demo/example/simple"), "Simple!");
      } catch (ZException e) {
         std::cout << "Received an error :" << e.what() << "\n";
      }
   }

---

..
.. Copyright (c) 2023 ZettaScale Technology
..
.. This program and the accompanying materials are made available under the
.. terms of the Eclipse Public License 2.0 which is available at
.. http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
.. which is available at https://www.apache.org/licenses/LICENSE-2.0.
..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Session Management
==================

The :cpp:class:`zenoh::Session` is the main zenoh object. The instance of the session reprsents a single 
zenoh node in the network.

Session
-------

.. doxygenclass:: zenoh::Session
   :members:
   :membergroups: Constructors Operators Methods Fields

---

..
.. SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
..
.. Contributors:
..   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
..

Shared Memory
=============
.. doxygenclass:: zenoh::ZShm
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::ZShmMut
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::CppShmClient
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::ShmClient
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::CppShmSegment
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::ShmClientStorage
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::PosixShmClient
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::PosixShmProvider
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::CppShmProvider
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::PrecomputedLayout
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::MemoryLayout
   :members:
   :membergroups: Constructors Operators Methods

.. doxygenclass:: zenoh::ChunkAllocResult
   :members:
   :membergroups: Constructors Operators Methods


.. doxygentypedef:: zenoh::ProtocolId
.. doxygentypedef:: zenoh::SegmentId
.. doxygentypedef:: zenoh::ChunkId

.. doxygentypedef:: zenoh::ChunkDescriptor
.. doxygentypedef:: zenoh::AllocatedChunk

.. doxygentypedef:: zenoh::AllocError
.. doxygentypedef:: zenoh::LayoutError
.. doxygentypedef:: zenoh::AllocAlignment

.. doxygentypedef:: zenoh::BufAllocResult
.. doxygentypedef:: zenoh::BufLayoutAllocResult

.. doxygenfunction:: zenoh::cleanup_orphaned_shm_segments

---

<img src="https://raw.githubusercontent.com/eclipse-zenoh/zenoh/master/zenoh-dragon.png" height="150">

[![CI](https://github.com/eclipse-zenoh/zenoh-cpp/workflows/CI/badge.svg)](https://github.com/eclipse-zenoh/zenoh-cpp/actions?query=workflow%3A%22CI%22)
[![Documentation Status](https://readthedocs.org/projects/zenoh-cpp/badge/?version=latest)](https://zenoh-cpp.readthedocs.io/en/latest/?badge=latest)
[![Discussion](https://img.shields.io/badge/discussion-on%20github-blue)](https://github.com/eclipse-zenoh/roadmap/discussions)
[![Discord](https://img.shields.io/badge/chat-on%20discord-blue)](https://discord.gg/2GJ958VuHs)
[![License](https://img.shields.io/badge/License-EPL%202.0-blue)](https://choosealicense.com/licenses/epl-2.0/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Eclipse Zenoh

The Eclipse Zenoh: Zero Overhead Pub/sub, Store/Query and Compute.

Zenoh (pronounce _/zeno/_) unifies data in motion, data at rest and computations. It carefully blends traditional pub/sub with geo-distributed storages, queries and computations, while retaining a level of time and space efficiency that is well beyond any of the mainstream stacks.

Check the website [zenoh.io](http://zenoh.io) and the [roadmap](https://github.com/eclipse-zenoh/roadmap) for more detailed information.

# C++ API

The Zenoh C++ API are headers only C++ bindings for [zenoh-c] and [zenoh-pico] libraries.

C++ bindings are still under active development so the Zenoh team will highly appreciate any help in testing them on various platforms, system architecture, etc. and to report any issue you might encounter. This will help in greatly improving its maturity and robustness.

## Requirements

The only hard requirement for building the library is a C++17-compliant compiler.
Using the library requires either [zenoh-c] or [zenoh-pico] to be installed.

-------------------------------

## How to build and install it

To install [zenoh-cpp] do the following steps:

1. Clone the sources.

   ```bash
   git clone https://github.com/eclipse-zenoh/zenoh-cpp.git
   ```

2. Build and install.

   By default it is expected that you have [zenoh-c] installed. If you want to install for [zenoh-pico] backend or for both (or to not specify any backend), please set `ZENOHCXX_ZENOHC` or `ZENOHCXX_ZENOHPICO` Cmake variables to`ON` or `OFF` accordingly. Notice that at least one of the backends is required for using the library and/or building tests and examples.

   Use option `CMAKE_INSTALL_PREFIX` for specifying installation location. Without this parameter installation is performed to default system location `/usr/local` which requires root privileges.

    ```bash
    mkdir build && cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=~/.local # to configure only for zenoh-c backend
    cmake .. -DZENOHCXX_ZENOHC=OFF -DZENOHCXX_ZENOHPICO=ON  -DCMAKE_INSTALL_PREFIX=~/.local # to configure  only for zenoh-pico backend
    cmake .. -DZENOHCXX_ZENOHC=OFF -DZENOHCXX_ZENOHPICO=OFF  -DCMAKE_INSTALL_PREFIX=~/.local # to configure for none of the backends
    cmake .. -DZENOHCXX_ZENOHPICO=ON  -DCMAKE_INSTALL_PREFIX=~/.local # to configure for both backends
    cmake --install .
    ```

## Building and running tests

By default it is expected that you have [zenoh-c] installed. If you want to build and run tests for [zenoh-pico] backend or for both, please set `ZENOHCXX_ZENOHC` or `ZENOHCXX_ZENOHPICO` Cmake variables to`ON` or `OFF` accordingly.

To build tests run:

```bash
mkdir build && cd build
cmake ..  -DCMAKE_INSTALL_PREFIX=~/.local # to build tests only for zenoh-c backend
cmake .. -DZENOHCXX_ZENOHC=OFF -DZENOHCXX_ZENOHPICO=ON  -DCMAKE_INSTALL_PREFIX=~/.local # to build tests only for zenoh-pico backend
cmake .. -DZENOHCXX_ZENOHPICO=ON  -DCMAKE_INSTALL_PREFIX=~/.local # to build tests for both backends
cmake --build . --target tests
ctest
```

Notice that the output of `cmake ../zenoh-cpp` shows where [zenoh-c] and/or [zenoh-pico] the dependencies were found.

## Building the Examples

Examples are splitted into two subdirectories. Subdirectory `universal` contains [zenoh-cpp] examples buildable with both [zenoh-c] and [zenoh-pico] backends. The `zenohc` subdirectory contains examples with zenoh-c specific functionality.

By default it is expected that you have [zenoh-c] installed. If you want to build examples for [zenoh-pico] backend or for both, please set `ZENOHCXX_ZENOHC` or `ZENOHCXX_ZENOHPICO` Cmake variables to`ON` or `OFF` accordingly.

To build examples run:

```bash
cmake ..  -DCMAKE_INSTALL_PREFIX=~/.local # to build examples only for zenoh-c backend
cmake .. -DZENOHCXX_ZENOHC=OFF -DZENOHCXX_ZENOHPICO=ON  -DCMAKE_INSTALL_PREFIX=~/.local # to build examples only for zenoh-pico backend
cmake .. -DZENOHCXX_ZENOHPICO=ON  -DCMAKE_INSTALL_PREFIX=~/.local # to build examples for both backends
cmake --build . --target examples
```

Examples are placed into `build/examples/zenohc` and `build/examples/zenohpico` directories.

## Running the examples

See information about running examples [here](./examples/README.md).

Examples of linking [zenoh-cpp] to an external project can be found [here](./examples/simple/Readme.md).

## Library usage

Below are the steps to include [zenoh-cpp] into CMake project. See also [examples/simple](examples/simple) directory for short examples of CMakeLists.txt.

- include [zenoh-c] or [zenoh-pico] into your CMake project **before** dependency on [zenoh-cpp] itself.
  This is important as the library targets you need (`zenohcxx::zenohpico`, `zenohcxx::zenohc::lib`) are defined only if their backend library targets (`zenohpico::lib` and/or `zenohc::lib` are defined)

- include [zenoh-cpp] using [find_package] CMake function:

  ```cmake
  find_package(zenohc) #if using zenoh-c backend
  find_package(zenohpico) #if using zenoh-pico backend
  find_package(zenohcxx)
  ```

- add dependency on zenoh-cpp to your project:

  ```cmake
  target_link_libraries(yourproject PUBLIC zenohcxx::zenohc) #if using zenoh-c backend
  target_link_libraries(yourproject PUBLIC zenohcxx::zenohpico) #if using zenoh-pico backend
  ```

- include the [zenoh.hxx] header. All zenoh functionality is available under the namespace `zenoh`:

  ```c++
  #include "zenoh.hxx"
  using namespace zenoh;
  ```

### Documentation

The documentation is on [zenoh-cpp.readthedocs.io].
Instruction how to build documentation locally is at [docs/README.md].

[rust-lang](https://www.rust-lang.org)
[zenoh](https://github.com/eclipse-zenoh/zenoh)
[zenoh-c](https://github.com/eclipse-zenoh/zenoh-c)
[zenoh-cpp](https://github.com/eclipse-zenoh/zenoh-cpp)
[zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico)
[zenoh.hxx](https://github.com/eclipse-zenoh/zenoh-cpp/blob/main/include/zenoh.hxx)
[add_subdirectory](https://cmake.org/cmake/help/latest/command/add_subdirectory.html)
[find_package](https://cmake.org/cmake/help/latest/command/find_package.html)
[FetchContent](https://cmake.org/cmake/help/latest/module/FetchContent.html)
[zenoh-cpp.readthedocs.io](https://zenoh-cpp.readthedocs.io)
[docs/README.md](https://github.com/eclipse-zenoh/zenoh-cpp/blob/main/docs/README.md)

---

