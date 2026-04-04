# Zenoh Examples: zenoh-python

# Example: examples--common--__init__.py

```py
from .common import *
```

---

# Example: examples--common--common.py

```py
import argparse
import json

import zenoh


def add_config_arguments(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--mode",
        "-m",
        dest="mode",
        choices=["peer", "client"],
        type=str,
        help="The zenoh session mode.",
    )
    parser.add_argument(
        "--connect",
        "-e",
        dest="connect",
        metavar="ENDPOINT",
        action="append",
        type=str,
        help="Endpoints to connect to.",
    )
    parser.add_argument(
        "--listen",
        "-l",
        dest="listen",
        metavar="ENDPOINT",
        action="append",
        type=str,
        help="Endpoints to listen on.",
    )
    parser.add_argument(
        "--config",
        "-c",
        dest="config",
        metavar="FILE",
        type=str,
        help="A configuration file.",
    )
    parser.add_argument(
        "--no-multicast-scouting",
        dest="no_multicast_scouting",
        default=False,
        action="store_true",
        help="Disable multicast scouting.",
    )
    parser.add_argument(
        "--cfg",
        dest="cfg",
        metavar="CFG",
        default=[],
        action="append",
        type=str,
        help="Allows arbitrary configuration changes as column-separated KEY:VALUE pairs. Where KEY must be a valid config path and VALUE must be a valid JSON5 string that can be deserialized to the expected type for the KEY field. Example: --cfg='transport/unicast/max_links:2'.",
    )


def get_config_from_args(args) -> zenoh.Config:
    conf = (
        zenoh.Config.from_file(args.config)
        if args.config is not None
        else zenoh.Config()
    )
    if args.mode is not None:
        conf.insert_json5("mode", json.dumps(args.mode))
    if args.connect is not None:
        conf.insert_json5("connect/endpoints", json.dumps(args.connect))
    if args.listen is not None:
        conf.insert_json5("listen/endpoints", json.dumps(args.listen))
    if args.no_multicast_scouting:
        conf.insert_json5("scouting/multicast/enabled", json.dumps(False))

    for c in args.cfg:
        try:
            [key, value] = c.split(":", 1)
        except:
            print(f"`--cfg` argument: expected KEY:VALUE pair, got {c}")
            raise
        conf.insert_json5(key, value)

    return conf
```

---

# Zenoh Python Examples

## Get Started

```bash
python3 <example.py>
```

Each example accepts the `-h` or `--help` option that provides a description of its arguments and their default values.

If you run the tests against the zenoh router running in a Docker container, you need to add the
`-e tcp/localhost:7447` option to your examples. That's because Docker doesn't support UDP multicast
transport, and therefore the zenoh scouting and discrovery mechanism cannot work with.

## Examples description

### z_scout

Scouts for zenoh peers and routers available on the network.

Typical usage:

   ```bash
      python3 z_scout.py
   ```

### z_info

Gets information about the Zenoh session.

Typical usage:

   ```bash
      python3 z_info.py
   ```

### z_put

Puts a path/payload into Zenoh.
The path/payload will be received by all matching subscribers, for instance the [z_sub](#z_sub)
and [z_storage](#z_storage) examples.

Typical usage:

   ```bash
      python3 z_put.py
   ```

or

   ```bash
      python3 z_put.py -k demo/example/test -p 'Hello World'
   ```

### z_pub

Declares a resource with a path and a publisher on this resource. Then puts a payload using the numerical resource id.
The path/payload will be received by all matching subscribers, for instance the [z_sub](#z_sub)
and [z_storage](#z_storage) examples.

Typical usage:

   ```bash
      python3 z_pub.py
   ```

or

   ```bash
      python3 z_pub.py -k demo/example/test -p 'Hello World'
   ```

### z_sub

Creates a subscriber with a key expression.
The subscriber will be notified of each put made on any key expression matching
the subscriber's key expression, and will print this notification.

Typical usage:

   ```bash
      python3 z_sub.py
   ```

or

   ```bash
      python3 z_sub.py -k 'demo/**'
   ```

### z_get

Sends a query message for a selector.
The queryables with a matching path or selector (for instance [z_queryable](#z_queryable) and [z_storage](#z_storage))
will receive this query and reply with paths/payloads that will be received by the query callback.

Typical usage:

   ```bash
      python3 z_get.py
   ```

or

   ```bash
      python3 z_get.py -s 'demo/**'
   ```

### z_querier

Continuously sends query messages for a selector.
The queryables with a matching path or selector (for instance [z_queryable](#z_queryable) and [z_storage](#z_storage))
will receive these queries and reply with paths/payloads that will be received by the querier's query callback.

Typical usage:

   ```bash
      python3 z_querier.py
   ```

or

   ```bash
      python3 z_get.py -s 'demo/**'
   ```

### z_queryable

Creates a queryable function with a key expression.
This queryable function will be triggered by each call to a get operation on zenoh
with a selector that matches the key expression, and will return a payload to the querier.

Typical usage:

   ```bash
      python3 z_queryable.py
   ```

or

   ```bash
      python3 z_queryable.py -k demo/example/queryable -p 'This is the result'
   ```

### z_storage

Trivial implementation of a storage in memory.
This examples creates a subscriber and a queryable on the same key expression.
The subscriber callback will store the received key/values in an hashmap.
The queryable callback will answer to queries with the key/values stored in the hashmap
and that match the queried selector.

Typical usage:

   ```bash
      python3 z_storage.py
   ```

or

   ```bash
      python3 z_storage.py -k 'demo/**'
   ```

### z_pub_thr & z_sub_thr

Pub/Sub throughput test.
This example allows to perform throughput measurements between a pubisher performing
put operations and a subscriber receiving notifications of those puts.

Typical Subscriber usage:

   ```bash
      python3 z_sub_thr.py
   ```

Typical Publisher usage:

   ```bash
      python3 z_pub_thr.py 1024
   ```

---

# Example: examples--z_advanced_pub.py

```py
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
import time
from typing import Optional

import zenoh
from zenoh.ext import CacheConfig, MissDetectionConfig, declare_advanced_publisher


def main(conf: zenoh.Config, key: str, payload: str, history: int):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring AdvancedPublisher on '{key}'...")
        pub = declare_advanced_publisher(
            session,
            key,
            cache=CacheConfig(max_samples=history),
            sample_miss_detection=MissDetectionConfig(heartbeat=5),
            publisher_detection=True,
        )

        print("Press CTRL-C to quit...")
        for idx in itertools.count():
            time.sleep(1)
            buf = f"[{idx:4d}] {payload}"
            print(f"Putting Data ('{key}': '{buf}')...")
            pub.put(buf)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse
    import itertools

    import common

    parser = argparse.ArgumentParser(
        prog="z_advanced_pub", description="zenoh advanced pub example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/zenoh-python-pub",
        type=str,
        help="The key expression to publish onto.",
    )
    parser.add_argument(
        "--payload",
        "-p",
        dest="payload",
        default="Pub from Python!",
        type=str,
        help="The payload to publish.",
    )
    parser.add_argument(
        "--history",
        dest="history",
        type=int,
        default=1,
        help="The number of publications to keep in cache",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key, args.payload, args.history)
```

---

# Example: examples--z_advanced_sub.py

```py
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
import time

import zenoh
from zenoh.ext import HistoryConfig, Miss, RecoveryConfig, declare_advanced_subscriber


def main(conf: zenoh.Config, key: str):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring Subscriber on '{key}'...")

        def listener(sample: zenoh.Sample):
            print(
                f">> [Subscriber] Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')"
            )

        advanced_sub = declare_advanced_subscriber(
            session,
            key,
            listener,
            history=HistoryConfig(detect_late_publishers=True),
            recovery=RecoveryConfig(heartbeat=True),
            subscriber_detection=True,
        )

        def miss_listener(miss: Miss):
            print(f">> [Subscriber] Missed {miss.nb} samples from {miss.source} !!!")

        advanced_sub.sample_miss_listener(miss_listener)

        print("Press CTRL-C to quit...")
        while True:
            time.sleep(1)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(
        prog="z_advanced_sub", description="zenoh advanced sub example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/**",
        type=str,
        help="The key expression to subscribe to.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key)
```

---

# Example: examples--z_bytes.py

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
from zenoh import ZBytes


def main():
    # Raw bytes
    input = b"raw bytes"
    payload = ZBytes(input)
    output = payload.to_bytes()  # equivalent to `bytes(payload)`
    assert input == output
    # Corresponding encoding to be used in operations like `.put()`, `.reply()`, etc.
    # encoding = Encoding.ZENOH_BYTES;

    # Raw utf8 bytes, i.e. string
    input = "raw bytes"
    payload = ZBytes(input)
    output = payload.to_string()  # equivalent to `str(payload)`
    assert input == output
    # Corresponding encoding to be used in operations like `.put()`, `.reply()`, etc.
    # encoding = Encoding.ZENOH_STRING;

    # JSON
    import json

    input = {"name": "John Doe", "age": 43, "phones": ["+44 1234567", "+44 2345678"]}
    payload = ZBytes(json.dumps(input))
    output = json.loads(payload.to_string())
    assert input == output
    # Corresponding encoding to be used in operations like `.put()`, `.reply()`, etc.
    # encoding = Encoding.APPLICATION_JSON;

    # Protobuf
    try:
        import entity_pb2

        input = entity_pb2.Entity(id=1234, name="John Doe")
        payload = ZBytes(input.SerializeToString())
        output = entity_pb2.Entity()
        output.ParseFromString(payload.to_bytes())
        assert input == output
        # Corresponding encoding to be used in operations like `.put()`, `.reply()`, etc.
        # encoding = Encoding.APPLICATION_PROTOBUF;
    except ImportError:
        # You must install protobuf and generate the protobuf classes from the schema with
        # $ pip install protobuf
        # $ protoc --python_out=. --pyi_out=. examples/entity.proto
        pass

    # zenoh.ext serialization
    from zenoh.ext import UInt32, z_deserialize, z_serialize

    if True:
        # Numeric: UInt8, UInt16, Uint32, UInt64, UInt128, Int8, Int16, Int32, Int64,
        # Int128, int (handled as int32), Float32, Float64, float (handled as Float64)
        input = UInt32(1234)
        payload = z_serialize(input)
        output = z_deserialize(UInt32, payload)
        assert input == output

        # list
        input = [0.0, 1.5, 42.0]  # all items must have the same type
        payload = z_serialize(input)
        output = z_deserialize(list[float], payload)
        assert input == output

        # dict
        input = {0: "abc", 1: "def"}
        payload = z_serialize(input)
        output = z_deserialize(dict[int, str], payload)
        assert input == output

        # tuple
        input = (0.42, "string")
        payload = z_serialize(input)
        output = z_deserialize(tuple[float, str], payload)
        assert input == output


if __name__ == "__main__":
    main()
```

---

# Example: examples--z_delete.py

```py
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
import zenoh


def main(conf: zenoh.Config, key: str):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Deleting resources matching '{key}'...")
        session.delete(key)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(prog="z_delete", description="zenoh put example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/zenoh-python-put",
        type=str,
        help="The key expression matching resources to delete.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    key = args.key

    main(conf, key)
```

---

# Example: examples--z_get_liveliness.py

```py
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
import zenoh


def main(conf: zenoh.Config, key: str, timeout: float):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Sending Liveliness Query '{key}'...")
        replies = session.liveliness().get(key, timeout=timeout)
        for reply in replies:
            try:
                print(f">> Alive token ('{reply.ok.key_expr}')")
            except:
                print(f">> Received (ERROR: '{reply.err.payload.to_string()}')")


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(
        prog="z_get_liveliness", description="zenoh put example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="group1/**",
        type=str,
        help="The key expression to write.",
    )
    parser.add_argument(
        "--timeout",
        "-o",
        dest="timeout",
        default=10.0,
        type=float,
        help="The query timeout.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key, args.timeout)
```

---

# Example: examples--z_get.py

```py
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
import zenoh


def main(
    conf: zenoh.Config,
    selector: str,
    target: zenoh.QueryTarget,
    payload: str,
    timeout: float,
):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Sending Query '{selector}'...")
        replies = session.get(selector, target=target, payload=payload, timeout=timeout)
        for reply in replies:
            try:
                print(
                    f">> Received ('{reply.ok.key_expr}': '{reply.ok.payload.to_string()}')"
                )
            except:
                print(f">> Received (ERROR: '{reply.err.payload.to_string()}')")


if __name__ == "__main__":
    # --- Command line argument parsing --- --- --- --- --- ---
    import argparse
    import json

    import common

    parser = argparse.ArgumentParser(prog="z_get", description="zenoh get example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--selector",
        "-s",
        dest="selector",
        default="demo/example/**",
        type=str,
        help="The selection of resources to query.",
    )
    parser.add_argument(
        "--target",
        "-t",
        dest="target",
        choices=["ALL", "BEST_MATCHING", "ALL_COMPLETE", "NONE"],
        default="BEST_MATCHING",
        type=str,
        help="The target queryables of the query.",
    )
    parser.add_argument(
        "--payload",
        "-p",
        dest="payload",
        type=str,
        help="An optional payload to send in the query.",
    )
    parser.add_argument(
        "--timeout",
        "-o",
        dest="timeout",
        default=10.0,
        type=float,
        help="The query timeout",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    target = {
        "ALL": zenoh.QueryTarget.ALL,
        "BEST_MATCHING": zenoh.QueryTarget.BEST_MATCHING,
        "ALL_COMPLETE": zenoh.QueryTarget.ALL_COMPLETE,
    }.get(args.target)

    main(conf, args.selector, target, args.payload, args.timeout)
```

---

# Example: examples--z_info.py

```py
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
import zenoh


def main(conf: zenoh.Config):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        info = session.info
        print(f"zid: {info.zid()}")
        print(f"routers: {info.routers_zid()}")
        print(f"peers: {info.peers_zid()}")


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse
    import json

    import common

    parser = argparse.ArgumentParser(prog="z_info", description="zenoh info example")
    common.add_config_arguments(parser)

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf)
```

---

# Example: examples--z_liveliness.py

```py
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
import time

import zenoh


def main(conf: zenoh.Config, key: str):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring LivelinessToken on '{key}'...")
        with session.liveliness().declare_token(key) as token:
            print("Press CTRL-C to quit...")
            while True:
                time.sleep(1)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(
        prog="z_liveliness", description="zenoh put example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="group1/zenoh-py",
        type=str,
        help="The key expression to write.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key)
```

---

# Example: examples--z_ping.py

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
import time

import zenoh


def main(conf: zenoh.Config, payload_size: int, warmup: int, samples: int):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        sub = session.declare_subscriber("test/pong")
        pub = session.declare_publisher(
            "test/ping", congestion_control=zenoh.CongestionControl.BLOCK
        )
        data = bytes(i % 10 for i in range(0, payload_size))

        print(f"Warming up for {warmup}...")
        warmup_end = time.time() + warmup
        while time.time() < warmup_end:
            pub.put(data)
            sub.recv()

        sample_list = []
        for i in range(samples):
            write_time = time.time()
            pub.put(data)
            sub.recv()
            sample_list.append(round((time.time() - write_time) * 1_000_000))

        for i, rtt in enumerate(sample_list):
            print(f"{payload_size} bytes: seq={i} rtt={rtt}µs lat={rtt / 2}µs")


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(prog="z_ping", description="zenoh get example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--warmup",
        "-w",
        dest="warmup",
        metavar="WARMUP",
        type=float,
        default=1.0,
        help="The number of seconds to warmup (float)",
    )
    parser.add_argument(
        "--samples",
        "-n",
        dest="samples",
        metavar="SAMPLES",
        type=int,
        default=100,
        help="The number of round-trip to measure",
    )
    parser.add_argument(
        "payload_size",
        metavar="PAYLOAD_SIZE",
        type=int,
        help="Sets the size of the payload to publish.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.payload_size, args.warmup, args.samples)
```

---

# Example: examples--z_pong.py

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
import time

import zenoh


def main(conf: zenoh.Config, express: bool):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        pub = session.declare_publisher(
            "test/pong",
            congestion_control=zenoh.CongestionControl.BLOCK,
            express=express,
        )
        session.declare_subscriber("test/ping", lambda s: pub.put(s.payload))

        print("Press CTRL-C to quit...")
        while True:
            time.sleep(1)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(prog="z_pong", description="zenoh get example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--express",
        dest="express",
        metavar="EXPRESS",
        type=bool,
        default=False,
        help="Express publishing",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.express)
```

---

# Example: examples--z_pub_shm.py

```py
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
import time
from typing import Optional

import zenoh


def main(
    conf: zenoh.Config, key: str, payload: str, iter: Optional[int], interval: int
):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:

        print("Creating POSIX SHM provider...")
        provider = zenoh.shm.ShmProvider.default_backend(1024 * 1024)

        print(f"Declaring Publisher on '{key}'...")
        pub = session.declare_publisher(key)

        print("Press CTRL-C to quit...")
        for idx in itertools.count() if iter is None else range(iter):
            time.sleep(interval)
            prefix = f"[{idx:4d}] "
            sbuf = provider.alloc(
                len(prefix) + len(payload),
                policy=zenoh.shm.BlockOn(zenoh.shm.GarbageCollect()),
            )
            sbuf[: len(prefix)] = prefix.encode()
            sbuf[len(prefix) :] = payload.encode()

            print(f"Putting Data ('{key}': '{sbuf}')...")
            pub.put(sbuf)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse
    import itertools

    import common

    parser = argparse.ArgumentParser(prog="z_pub", description="zenoh pub example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/zenoh-python-pub",
        type=str,
        help="The key expression to publish onto.",
    )
    parser.add_argument(
        "--payload",
        "-p",
        dest="payload",
        default="Pub from Python!",
        type=str,
        help="The payload to publish.",
    )
    parser.add_argument(
        "--iter", dest="iter", type=int, help="How many puts to perform"
    )
    parser.add_argument(
        "--interval",
        dest="interval",
        type=float,
        default=1.0,
        help="Interval between each put",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key, args.payload, args.iter, args.interval)
```

---

# Example: examples--z_pub_thr.py

```py
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
import zenoh


def main(conf: zenoh.Config, payload_size: int):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    data = bytearray()
    for i in range(0, payload_size):
        data.append(i % 10)
    data = zenoh.ZBytes(data)
    congestion_control = zenoh.CongestionControl.BLOCK

    with zenoh.open(conf) as session:
        pub = session.declare_publisher(
            "test/thr", congestion_control=congestion_control
        )

        print("Press CTRL-C to quit...")
        while True:
            pub.put(data)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse
    import json

    import common

    parser = argparse.ArgumentParser(
        prog="z_pub_thr", description="zenoh throughput pub example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "payload_size", type=int, help="Sets the size of the payload to publish."
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.payload_size)
```

---

# Example: examples--z_pub.py

```py
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
import time
from typing import Optional

import zenoh


def main(
    conf: zenoh.Config,
    key: str,
    payload: str,
    iter: Optional[int],
    interval: int,
    add_matching_listener: bool,
):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring Publisher on '{key}'...")
        pub = session.declare_publisher(key)

        if add_matching_listener:

            def on_matching_status_update(status: zenoh.MatchingStatus):
                if status.matching:
                    print("Publisher has matching subscribers.")
                else:
                    print("Publisher has NO MORE matching subscribers")

            pub.declare_matching_listener(on_matching_status_update)

        print("Press CTRL-C to quit...")
        for idx in itertools.count() if iter is None else range(iter):
            time.sleep(interval)
            buf = f"[{idx:4d}] {payload}"
            print(f"Putting Data ('{key}': '{buf}')...")
            pub.put(buf)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse
    import itertools

    import common

    parser = argparse.ArgumentParser(prog="z_pub", description="zenoh pub example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/zenoh-python-pub",
        type=str,
        help="The key expression to publish onto.",
    )
    parser.add_argument(
        "--payload",
        "-p",
        dest="payload",
        default="Pub from Python!",
        type=str,
        help="The payload to publish.",
    )
    parser.add_argument(
        "--iter", dest="iter", type=int, help="How many puts to perform"
    )
    parser.add_argument(
        "--interval",
        dest="interval",
        type=float,
        default=1.0,
        help="Interval between each put",
    )
    parser.add_argument(
        "--add-matching-listener",
        default=False,
        action="store_true",
        help="Add matching listener",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(
        conf,
        args.key,
        args.payload,
        args.iter,
        args.interval,
        args.add_matching_listener,
    )
```

---

# Example: examples--z_pull.py

```py
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
import time

import zenoh


def main(conf: zenoh.Config, key: str, size: int, interval: int):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring Subscriber on '{key}'...")
        # Subscriber doesn't receive messages over the RingBuffer size.
        # The oldest message is overwritten by the latest one.
        sub = session.declare_subscriber(key, zenoh.handlers.RingChannel(size))

        print("Press CTRL-C to quit...")
        while True:
            time.sleep(interval)
            while True:
                sample = sub.try_recv()
                if sample is None:
                    break
                print(
                    f">> [Subscriber] Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')"
                )


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(prog="z_pull", description="zenoh pull example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/**",
        type=str,
        help="The key expression matching resources to pull.",
    )
    parser.add_argument(
        "--size", dest="size", default=3, type=int, help="The size of the ringbuffer"
    )
    parser.add_argument(
        "--interval",
        dest="interval",
        default=1.0,
        type=float,
        help="The interval for pulling the ringbuffer",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key, args.size, args.interval)
```

---

# Example: examples--z_put_float.py

```py
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
import zenoh
from zenoh.ext import z_serialize


def main(conf: zenoh.Config, key: str, payload: float):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Putting Data ('{key}': '{payload}')...")
        # Refer to z_bytes.py to see how to serialize different types of message
        session.put(key, z_serialize(payload))


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(
        prog="z_put_float", description="zenoh put example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/zenoh-python-put",
        type=str,
        help="The key expression to write.",
    )
    parser.add_argument(
        "--payload",
        "-p",
        dest="payload",
        default=42.0,
        type=float,
        help="The payload to write.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key, args.payload)
```

---

# Example: examples--z_put.py

```py
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
import zenoh


def main(conf: zenoh.Config, key: str, payload: str):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Putting Data ('{key}': '{payload}')...")
        # Refer to z_bytes.py to see how to serialize different types of message
        session.put(key, payload)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(prog="z_put", description="zenoh put example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/zenoh-python-put",
        type=str,
        help="The key expression to write.",
    )
    parser.add_argument(
        "--payload",
        "-p",
        dest="payload",
        default="Put from Python!",
        type=str,
        help="The payload to write.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key, args.payload)
```

---

# Example: examples--z_querier.py

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
import itertools
import time
from typing import Optional

import zenoh


def main(
    conf: zenoh.Config,
    selector: str,
    target: zenoh.QueryTarget,
    payload: str,
    timeout: float,
    iter: Optional[int],
    add_matching_listener: bool,
):
    # initiate logging
    zenoh.init_log_from_env_or("error")
    print("Opening session...")
    with zenoh.open(conf) as session:
        query_selector = zenoh.Selector(selector)

        print(f"Declaring Querier on '{query_selector.key_expr}'...")
        querier = session.declare_querier(
            query_selector.key_expr, target=target, timeout=timeout
        )

        if add_matching_listener:

            def on_matching_status_update(status: zenoh.MatchingStatus):
                if status.matching:
                    print("Querier has matching queryables.")
                else:
                    print("Querier has NO MORE matching queryables")

            querier.declare_matching_listener(on_matching_status_update)

        print("Press CTRL-C to quit...")
        for idx in itertools.count() if iter is None else range(iter):
            time.sleep(1.0)
            buf = f"[{idx:4d}] {payload if payload else ''}"
            print(f"Querying '{selector}' with payload '{buf}')...")

            replies = querier.get(parameters=query_selector.parameters, payload=buf)
            for reply in replies:
                try:
                    print(
                        f">> Received ('{reply.ok.key_expr}': '{reply.ok.payload.to_string()}')"
                    )
                except:
                    print(f">> Received (ERROR: '{reply.err.payload.to_string()}')")


if __name__ == "__main__":
    # --- Command line argument parsing --- --- --- --- --- ---
    import argparse
    import json

    import common

    parser = argparse.ArgumentParser(
        prog="z_querier", description="zenoh querier example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--selector",
        "-s",
        dest="selector",
        default="demo/example/**",
        type=str,
        help="The selection of resources to query.",
    )
    parser.add_argument(
        "--target",
        "-t",
        dest="target",
        choices=["ALL", "BEST_MATCHING", "ALL_COMPLETE", "NONE"],
        default="BEST_MATCHING",
        type=str,
        help="The target queryables of the query.",
    )
    parser.add_argument(
        "--payload",
        "-p",
        dest="payload",
        type=str,
        help="An optional payload to send in the query.",
    )
    parser.add_argument(
        "--timeout",
        "-o",
        dest="timeout",
        default=10.0,
        type=float,
        help="The query timeout",
    )
    parser.add_argument(
        "--iter", dest="iter", type=int, help="How many gets to perform"
    )
    parser.add_argument(
        "--add-matching-listener",
        default=False,
        action="store_true",
        help="Add matching listener",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    target = {
        "ALL": zenoh.QueryTarget.ALL,
        "BEST_MATCHING": zenoh.QueryTarget.BEST_MATCHING,
        "ALL_COMPLETE": zenoh.QueryTarget.ALL_COMPLETE,
    }.get(args.target)

    main(
        conf,
        args.selector,
        target,
        args.payload,
        args.timeout,
        args.iter,
        args.add_matching_listener,
    )
```

---

# Example: examples--z_queryable.py

```py
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
import time

import zenoh


def main(conf: zenoh.Config, key: str, payload: str, complete: bool):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring Queryable on '{key}'...")
        queryable = session.declare_queryable(key, complete=complete)

        print("Press CTRL-C to quit...")
        while True:
            with queryable.recv() as query:
                if query.payload is not None:
                    print(
                        f">> [Queryable ] Received Query '{query.selector}'"
                        f" with payload: '{query.payload.to_string()}'"
                    )
                else:
                    print(f">> [Queryable ] Received Query '{query.selector}'")
                query.reply(key, payload)
                # it's possible to call `query.drop()` after handling it
                # instead of using a context manager


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse
    import json

    import common

    parser = argparse.ArgumentParser(
        prog="z_queryable", description="zenoh queryable example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/zenoh-python-queryable",
        type=str,
        help="The key expression matching queries to reply to.",
    )
    parser.add_argument(
        "--payload",
        "-p",
        dest="payload",
        default="Queryable from Python!",
        type=str,
        help="The payload to reply to queries.",
    )
    parser.add_argument(
        "--complete",
        dest="complete",
        default=False,
        action="store_true",
        help="Declare the queryable as complete w.r.t. the key expression.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key, args.payload, args.complete)
```

---

# Example: examples--z_scout.py

```py
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
import threading

import zenoh


def main():
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Scouting...")
    scout = zenoh.scout(what="peer|router")
    threading.Timer(1.0, lambda: scout.stop()).start()

    for hello in scout:
        print(hello)


if __name__ == "__main__":
    main()
```

---

# Example: examples--z_storage.py

```py
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
import time

import zenoh

store = {}


def listener(sample: zenoh.Sample):
    print(
        f">> [Subscriber] Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')"
    )
    if sample.kind == zenoh.SampleKind.DELETE:
        store.pop(sample.key_expr, None)
    else:
        store[sample.key_expr] = sample


def query_handler(query: zenoh.Query):
    print(f">> [Queryable ] Received Query '{query.selector}'")
    for stored_name, sample in store.items():
        if query.key_expr.intersects(stored_name):
            query.reply(
                sample.key_expr,
                sample.payload,
                encoding=sample.encoding,
                congestion_control=sample.congestion_control,
                priority=sample.priority,
                express=sample.express,
            )


def main(conf: zenoh.Config, key: str, complete: bool):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring Subscriber on '{key}'...")
        session.declare_subscriber(key, listener)

        print(f"Declaring Queryable on '{key}'...")
        session.declare_queryable(key, query_handler, complete=complete)

        print("Press CTRL-C to quit...")
        while True:
            time.sleep(1)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse
    import json

    import common

    parser = argparse.ArgumentParser(
        prog="z_storage", description="zenoh storage example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/**",
        type=str,
        help="The key expression matching resources to store.",
    )
    parser.add_argument(
        "--complete",
        dest="complete",
        default=False,
        action="store_true",
        help="Declare the storage as complete w.r.t. the key expression.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key, args.complete)
```

---

# Example: examples--z_sub_liveliness.py

```py
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
import zenoh


def main(conf: zenoh.Config, key: str, history: bool):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring Liveliness Subscriber on '{key}'...")
        with session.liveliness().declare_subscriber(key, history=history) as sub:
            for sample in sub:
                if sample.kind == zenoh.SampleKind.PUT:
                    print(
                        f">> [LivelinessSubscriber] New alive token ('{sample.key_expr}')"
                    )
                elif sample.kind == zenoh.SampleKind.DELETE:
                    print(
                        f">> [LivelinessSubscriber] Dropped token ('{sample.key_expr}')"
                    )


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(
        prog="z_sub_liveliness", description="zenoh sub example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="group1/**",
        type=str,
        help="The key expression to subscribe to.",
    )
    parser.add_argument(
        "--history",
        dest="history",
        default=False,
        type=bool,
        help="Get historical liveliness tokens.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key, args.history)
```

---

# Example: examples--z_sub_queued.py

```py
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
import zenoh


def main(conf: zenoh.Config, key: str):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring Subscriber on '{key}'...")
        with session.declare_subscriber(key) as sub:
            print("Press CTRL-C to quit...")
            for sample in sub:
                print(
                    f">> [Subscriber] Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')"
                )


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse
    import json

    import common

    parser = argparse.ArgumentParser(
        prog="z_sub_queued", description="zenoh sub example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/**",
        type=str,
        help="The key expression to subscribe to.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key)
```

---

# Example: examples--z_sub_shm.py

```py
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
import zenoh


def main(conf: zenoh.Config, key: str):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring Subscriber on '{key}'...")
        with session.declare_subscriber(key) as sub:
            print("Press CTRL-C to quit...")
            for sample in sub:
                payload_type, payload = handle_bytes(sample.payload)
                print(
                    f">> [Subscriber] Received {sample.kind} ('{sample.key_expr}': '{payload}')[{payload_type}] ",
                    end="",
                )
                if att := sample.attachment:
                    attachment_type, attachment = handle_bytes(att)
                    print(f" ({attachment_type}: {attachment})")
                print()


def handle_bytes(bytes: zenoh.ZBytes) -> tuple[str, str]:
    bytes_type = "SHM" if bytes.as_shm() is not None else "RAW"
    return bytes_type, bytes.to_string()


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse
    import json

    import common

    parser = argparse.ArgumentParser(
        prog="z_sub_queued", description="zenoh sub example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/**",
        type=str,
        help="The key expression to subscribe to.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key)
```

---

# Example: examples--z_sub_thr.py

```py
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
import time

import zenoh

batch_count = 0
count = 0
start = None
global_start = None


def main(conf: zenoh.Config, number: int):
    def listener(_sample: zenoh.Sample):
        global count, batch_count, start, global_start
        if count == 0:
            start = time.time()
            if global_start is None:
                global_start = start
            count += 1
        elif count < number:
            count += 1
        else:
            stop = time.time()
            print(f"{number / (stop - start):.6f} msgs/sec")
            batch_count += 1
            count = 0

    def report():
        assert global_start is not None
        end = time.time()
        total = batch_count * number + count
        print(
            f"Received {total} messages in {end - global_start}: averaged {total / (end - global_start):.6f} msgs/sec"
        )

    # initiate logging
    zenoh.init_log_from_env_or("error")

    with zenoh.open(conf) as session:
        session.declare_subscriber(
            "test/thr", zenoh.handlers.Callback(listener, report)
        )

        print("Press CTRL-C to quit...")
        while True:
            time.sleep(1)


if __name__ == "__main__":
    # --- Command line argument parsing --- --- --- --- --- ---
    import argparse
    import json

    import common

    parser = argparse.ArgumentParser(
        prog="z_sub_thr", description="zenoh throughput sub example"
    )
    common.add_config_arguments(parser)
    parser.add_argument(
        "--number",
        "-n",
        dest="number",
        default=50000,
        metavar="NUMBER",
        type=int,
        help="Number of messages in each throughput measurements.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.number)
```

---

# Example: examples--z_sub.py

```py
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
import time

import zenoh


def main(conf: zenoh.Config, key: str):
    # initiate logging
    zenoh.init_log_from_env_or("error")

    print("Opening session...")
    with zenoh.open(conf) as session:
        print(f"Declaring Subscriber on '{key}'...")

        def listener(sample: zenoh.Sample):
            print(
                f">> [Subscriber] Received {sample.kind} ('{sample.key_expr}': '{sample.payload.to_string()}')"
            )

        session.declare_subscriber(key, listener)

        print("Press CTRL-C to quit...")
        while True:
            time.sleep(1)


# --- Command line argument parsing --- --- --- --- --- ---
if __name__ == "__main__":
    import argparse

    import common

    parser = argparse.ArgumentParser(prog="z_sub", description="zenoh sub example")
    common.add_config_arguments(parser)
    parser.add_argument(
        "--key",
        "-k",
        dest="key",
        default="demo/example/**",
        type=str,
        help="The key expression to subscribe to.",
    )

    args = parser.parse_args()
    conf = common.get_config_from_args(args)

    main(conf, args.key)
```

---

