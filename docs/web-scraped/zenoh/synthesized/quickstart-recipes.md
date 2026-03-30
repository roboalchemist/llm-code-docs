# Zenoh Quickstart Recipes

Minimal working code snippets for the most common Zenoh tasks. All examples use
the default peer mode with multicast scouting unless otherwise noted.

---

## Table of Contents

- [Basic Patterns](#basic-patterns)
  - [Pub/Sub (Python)](#pubsub-python)
  - [Pub/Sub (Rust)](#pubsub-rust)
  - [Pub/Sub (C)](#pubsub-c)
  - [Get/Queryable — Request/Reply (Python)](#getqueryable-requestreply-python)
  - [Get/Queryable — Request/Reply (Rust)](#getqueryable-requestreply-rust)
  - [Pub/Sub (Go)](#pubsub-go)
  - [Pub/Sub (TypeScript / Node.js)](#pubsub-typescript-nodejs)
- [Configuration Patterns](#configuration-patterns)
  - [Connect to a specific router (client mode)](#connect-to-a-specific-router-client-mode)
  - [Connect two peers without a router (P2P)](#connect-two-peers-without-a-router-p2p)
  - [Connect to the public demo endpoint](#connect-to-the-public-demo-endpoint)
  - [Start an embedded router from code (Rust)](#start-an-embedded-router-from-code-rust)
  - [Enable REST API and memory storage](#enable-rest-api-and-memory-storage)
- [Common Patterns](#common-patterns)
  - [Wildcard subscriber](#wildcard-subscriber)
  - [Liveliness detection — detect when a peer goes offline](#liveliness-detection-detect-when-a-peer-goes-offline)
  - [Storage query — retrieve historical data](#storage-query-retrieve-historical-data)
  - [In-memory storage queryable (pure application, no router)](#in-memory-storage-queryable-pure-application-no-router)
  - [SHM publisher — zero-copy same-host pattern (Rust)](#shm-publisher-zero-copy-same-host-pattern-rust)
  - [QoS: real-time priority publisher (Rust)](#qos-real-time-priority-publisher-rust)
  - [Matching listener — react when subscribers appear/disappear](#matching-listener-react-when-subscribers-appeardisappear)
- [Installation Quick Reference](#installation-quick-reference)

## Basic Patterns

### Pub/Sub (Python)

**Publisher** — publishes to `demo/example/hello` every second:

```python
import time
import zenoh

with zenoh.open(zenoh.Config()) as session:
    pub = session.declare_publisher("demo/example/hello")
    for i in range(100):
        msg = f"Hello #{i}"
        print(f"Publishing: {msg}")
        pub.put(msg)
        time.sleep(1)
```

**Subscriber** — receives everything under `demo/example/**`:

```python
import time
import zenoh

def on_sample(sample: zenoh.Sample):
    print(f"Received [{sample.key_expr}]: {sample.payload.to_string()}")

with zenoh.open(zenoh.Config()) as session:
    sub = session.declare_subscriber("demo/example/**", on_sample)
    print("Listening... Ctrl-C to quit")
    while True:
        time.sleep(1)
```

---

### Pub/Sub (Rust)

**Publisher**:

```rust
use std::time::Duration;
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session
        .declare_publisher("demo/example/hello")
        .await
        .unwrap();

    for i in 0..100u32 {
        let msg = format!("Hello #{i}");
        println!("Publishing: {msg}");
        publisher.put(msg).await.unwrap();
        tokio::time::sleep(Duration::from_secs(1)).await;
    }
}
```

**Subscriber**:

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let subscriber = session
        .declare_subscriber("demo/example/**")
        .await
        .unwrap();

    println!("Listening... Ctrl-C to quit");
    while let Ok(sample) = subscriber.recv_async().await {
        let payload = sample.payload().try_to_string().unwrap_or_default();
        println!("Received [{}]: {}", sample.key_expr(), payload);
    }
}
```

---

### Pub/Sub (C)

**Publisher**:

```c
#include <stdio.h>
#include <string.h>
#include "zenoh.h"

int main(void) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    z_config_default(&config);

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) {
        printf("Unable to open session!\n");
        return -1;
    }

    z_owned_publisher_t pub;
    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, "demo/example/hello");
    if (z_declare_publisher(z_loan(s), &pub, z_loan(ke), NULL) < 0) {
        printf("Unable to declare publisher!\n");
        return -1;
    }

    char buf[64];
    for (int i = 0; i < 100; i++) {
        snprintf(buf, sizeof(buf), "Hello #%d", i);
        printf("Publishing: %s\n", buf);
        z_owned_bytes_t payload;
        z_bytes_copy_from_str(&payload, buf);
        z_publisher_put(z_loan(pub), z_move(payload), NULL);
        z_sleep_s(1);
    }

    z_drop(z_move(pub));
    z_drop(z_move(s));
    return 0;
}
```

**Subscriber**:

```c
#include <stdio.h>
#include "zenoh.h"

void data_handler(z_loaned_sample_t* sample, void* arg) {
    z_view_string_t key;
    z_keyexpr_as_view_string(z_sample_keyexpr(sample), &key);
    z_owned_string_t payload;
    z_bytes_to_string(z_sample_payload(sample), &payload);
    printf("Received [%.*s]: %.*s\n",
           (int)z_string_len(z_loan(key)), z_string_data(z_loan(key)),
           (int)z_string_len(z_loan(payload)), z_string_data(z_loan(payload)));
    z_drop(z_move(payload));
}

int main(void) {
    zc_init_log_from_env_or("error");

    z_owned_config_t config;
    z_config_default(&config);

    z_owned_session_t s;
    if (z_open(&s, z_move(config), NULL) < 0) return -1;

    z_view_keyexpr_t ke;
    z_view_keyexpr_from_str(&ke, "demo/example/**");

    z_owned_closure_sample_t callback;
    z_closure(&callback, data_handler, NULL, NULL);

    z_owned_subscriber_t sub;
    if (z_declare_subscriber(z_loan(s), &sub, z_loan(ke), z_move(callback), NULL) < 0) {
        printf("Unable to declare subscriber!\n");
        return -1;
    }

    printf("Listening... Ctrl-C to quit\n");
    while (1) z_sleep_s(1);

    z_drop(z_move(sub));
    z_drop(z_move(s));
    return 0;
}
```

---

### Get/Queryable — Request/Reply (Python)

**Queryable** — handles incoming queries and replies:

```python
import time
import zenoh

with zenoh.open(zenoh.Config()) as session:
    queryable = session.declare_queryable("demo/example/queryable")
    print("Queryable ready. Ctrl-C to quit")
    while True:
        with queryable.recv() as query:
            print(f"Received query: {query.selector}")
            # Reply with a value on the same key
            query.reply("demo/example/queryable", "Reply from Python!")
```

**Getter** — sends a query and collects replies:

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    replies = session.get("demo/example/**", timeout=5.0)
    for reply in replies:
        try:
            print(f"Reply [{reply.ok.key_expr}]: {reply.ok.payload.to_string()}")
        except Exception:
            print(f"Error reply: {reply.err.payload.to_string()}")
```

---

### Get/Queryable — Request/Reply (Rust)

**Queryable**:

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let queryable = session
        .declare_queryable("demo/example/queryable")
        .await
        .unwrap();

    println!("Queryable ready. Ctrl-C to quit");
    while let Ok(query) = queryable.recv_async().await {
        println!("Received query: {}", query.selector());
        query
            .reply("demo/example/queryable", "Reply from Rust!")
            .await
            .unwrap_or_else(|e| eprintln!("Reply error: {e}"));
    }
}
```

**Getter**:

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let replies = session.get("demo/example/**").await.unwrap();

    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => {
                let payload = sample.payload().try_to_string().unwrap_or_default();
                println!("Reply [{}]: {}", sample.key_expr(), payload);
            }
            Err(err) => eprintln!("Error reply: {:?}", err.payload().try_to_string()),
        }
    }
}
```

---

### Pub/Sub (Go)

Go bindings (`zenoh-go`) wrap the zenoh-c library. Install via the module, then:

```go
package main

import (
    "fmt"
    "time"
    "github.com/eclipse-zenoh/zenoh-go"
)

func main() {
    // Open session with default config (peer mode, multicast scouting)
    z, err := zenoh.Open(zenoh.NewConfig())
    if err != nil {
        panic(err)
    }
    defer z.Close()

    pub, err := z.DeclarePublisher("demo/example/hello", zenoh.NewPublisherOptions())
    if err != nil {
        panic(err)
    }
    defer pub.Undeclare()

    for i := 0; i < 100; i++ {
        msg := fmt.Sprintf("Hello #%d", i)
        fmt.Printf("Publishing: %s\n", msg)
        pub.Put(zenoh.NewValue([]byte(msg), zenoh.StringEncoding()))
        time.Sleep(time.Second)
    }
}
```

**Subscriber (Go)**:

```go
package main

import (
    "fmt"
    "time"
    "github.com/eclipse-zenoh/zenoh-go"
)

func main() {
    z, err := zenoh.Open(zenoh.NewConfig())
    if err != nil {
        panic(err)
    }
    defer z.Close()

    sub, err := z.DeclareSubscriber("demo/example/**",
        func(sample *zenoh.Sample) {
            fmt.Printf("Received [%s]: %s\n",
                sample.Path(), string(sample.Value().Payload()))
        },
        zenoh.NewSubscriberOptions())
    if err != nil {
        panic(err)
    }
    defer sub.Undeclare()

    fmt.Println("Listening... Ctrl-C to quit")
    for {
        time.Sleep(time.Second)
    }
}
```

---

### Pub/Sub (TypeScript / Node.js)

The `@eclipse-zenoh/zenoh-ts` package is available via npm. Requires Node.js 18+.

```bash
npm install @eclipse-zenoh/zenoh-ts
```

**Publisher**:

```typescript
import { Zenoh, Config } from "@eclipse-zenoh/zenoh-ts";

async function main() {
    const session = await Zenoh.open(new Config());
    const pub = await session.declarePublisher("demo/example/hello");

    for (let i = 0; i < 100; i++) {
        const msg = `Hello #${i}`;
        console.log(`Publishing: ${msg}`);
        await pub.put(msg);
        await new Promise(resolve => setTimeout(resolve, 1000));
    }

    await session.close();
}

main().catch(console.error);
```

**Subscriber**:

```typescript
import { Zenoh, Config, Sample } from "@eclipse-zenoh/zenoh-ts";

async function main() {
    const session = await Zenoh.open(new Config());
    const sub = await session.declareSubscriber(
        "demo/example/**",
        (sample: Sample) => {
            console.log(`Received [${sample.keyexpr}]: ${sample.payload.toString()}`);
        }
    );

    console.log("Listening... Ctrl-C to quit");
    await new Promise(() => {}); // run forever
}

main().catch(console.error);
```

---

## Configuration Patterns

### Connect to a specific router (client mode)

```json5
// config.json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/192.168.1.100:7447"]
  }
}
```

Load in Python:
```python
conf = zenoh.Config.from_file("config.json5")
session = zenoh.open(conf)
```

Load in Rust:
```rust
let config = Config::from_file("config.json5").unwrap();
let session = zenoh::open(config).await.unwrap();
```

Pass on command line (no file):
```bash
./my_app --cfg='mode:"client"' --cfg='connect/endpoints:["tcp/192.168.1.100:7447"]'
```

---

### Connect two peers without a router (P2P)

Both sides use `peer` mode. Multicast scouting handles discovery automatically on the same LAN:

```json5
{ mode: "peer" }
```

If multicast is unavailable, use gossip scouting with an explicit initial contact:

```json5
{
  mode: "peer",
  connect: { endpoints: ["tcp/192.168.1.50:7447"] },
  scouting: { gossip: { enabled: true } }
}
```

---

### Connect to the public demo endpoint

```json5
{
  mode: "client",
  connect: {
    endpoints: ["tcp/demo.zenoh.io:7447"]
  }
}
```

Note: `demo.zenoh.io` is only online during ZettaScale demos. For production, run your own router.

---

### Start an embedded router from code (Rust)

```rust
use zenoh::config::{Config, WhatAmI};

#[tokio::main]
async fn main() {
    let mut config = Config::default();
    config.set_mode(Some(WhatAmI::Router)).unwrap();

    let session = zenoh::open(config).await.unwrap();
    println!("Router running. Press Ctrl-C to quit.");
    std::future::pending::<()>().await;
}
```

From command line:
```bash
zenohd                                    # default config, listens on tcp/[::]:7447
zenohd --rest-http-port 8000              # also enable REST API
zenohd -c my-config.json5                 # custom config file
```

---

### Enable REST API and memory storage

```json5
{
  plugins: {
    rest: {
      http_port: 8000
    },
    storage_manager: {
      storages: {
        demo: {
          key_expr: "demo/**",
          volume: { id: "memory" }
        }
      }
    }
  }
}
```

```bash
zenohd -c config.json5
# Write a value:
curl -X PUT -d "hello world" http://localhost:8000/demo/test/key
# Read it back:
curl http://localhost:8000/demo/test/key
# Read everything under demo/:
curl http://localhost:8000/demo/**
```

---

## Common Patterns

### Wildcard subscriber

Subscribe to all temperature sensors across any room:

```python
import time
import zenoh

with zenoh.open(zenoh.Config()) as session:
    # * = single segment, ** = any depth
    sub = session.declare_subscriber(
        "building/*/sensors/temperature",
        lambda s: print(f"{s.key_expr}: {s.payload.to_string()}")
    )
    while True:
        time.sleep(1)
```

```rust
// Rust equivalent
let subscriber = session
    .declare_subscriber("building/*/sensors/temperature")
    .await.unwrap();
```

---

### Liveliness detection — detect when a peer goes offline

**Declare a liveliness token** (peer announces itself as alive):

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    // Token is alive as long as this session is open
    let _token = session
        .liveliness()
        .declare_token("robot/fleet/unit-42")
        .await
        .unwrap();

    println!("Token alive. Ctrl-C to drop it.");
    std::future::pending::<()>().await;
}
```

**Subscribe to liveliness events** (detect when any fleet unit appears/disappears):

```rust
use zenoh::{Config, sample::SampleKind};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let subscriber = session
        .liveliness()
        .declare_subscriber("robot/fleet/**")
        .history(true)   // also get currently-alive tokens on startup
        .await
        .unwrap();

    while let Ok(sample) = subscriber.recv_async().await {
        match sample.kind() {
            SampleKind::Put    => println!("ONLINE:  {}", sample.key_expr()),
            SampleKind::Delete => println!("OFFLINE: {}", sample.key_expr()),
        }
    }
}
```

Python equivalent:

```python
import time
import zenoh

with zenoh.open(zenoh.Config()) as session:
    def on_liveliness(sample: zenoh.Sample):
        status = "ONLINE" if sample.kind == zenoh.SampleKind.PUT() else "OFFLINE"
        print(f"{status}: {sample.key_expr}")

    sub = session.liveliness().declare_subscriber(
        "robot/fleet/**", on_liveliness, history=True
    )
    while True:
        time.sleep(1)
```

---

### Storage query — retrieve historical data

Query a memory (or RocksDB/S3) storage for previously published values:

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    # Get all values stored under "sensor/**"
    replies = session.get("sensor/**", timeout=5.0)
    for reply in replies:
        try:
            print(f"[{reply.ok.key_expr}] = {reply.ok.payload.to_string()}")
        except Exception:
            print(f"Error: {reply.err.payload.to_string()}")
```

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let replies = session.get("sensor/**").await.unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            let v = sample.payload().try_to_string().unwrap_or_default();
            println!("[{}] = {}", sample.key_expr(), v);
        }
    }
}
```

The storage must be running somewhere in the Zenoh network (via `zenohd` with `storage_manager` plugin, or an embedded storage in a peer application). See the configuration pattern above.

---

### In-memory storage queryable (pure application, no router)

Implement your own key/value store that responds to `get()` queries — useful when you don't want to run a separate router:

```rust
use std::collections::HashMap;
use futures::select;
use zenoh::{Config, key_expr::keyexpr, sample::SampleKind};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let mut store: HashMap<String, zenoh::sample::Sample> = HashMap::new();

    let subscriber = session.declare_subscriber("mystore/**").await.unwrap();
    let queryable  = session.declare_queryable("mystore/**").complete(true).await.unwrap();

    loop {
        select!(
            sample = subscriber.recv_async() => {
                let sample = sample.unwrap();
                match sample.kind() {
                    SampleKind::Delete => { store.remove(&sample.key_expr().to_string()); }
                    SampleKind::Put    => { store.insert(sample.key_expr().to_string(), sample); }
                }
            },
            query = queryable.recv_async() => {
                let query = query.unwrap();
                for (k, s) in &store {
                    if query.key_expr().intersects(unsafe { keyexpr::from_str_unchecked(k) }) {
                        query.reply(s.key_expr().clone(), s.payload().clone()).await.unwrap();
                    }
                }
            }
        );
    }
}
```

---

### SHM publisher — zero-copy same-host pattern (Rust)

SHM (shared memory) eliminates serialization overhead for large payloads between processes on the same host. Requires the `shared-memory` and `unstable` features.

```toml
# Cargo.toml
[dependencies]
zenoh = { version = "1", features = ["shared-memory", "unstable"] }
```

```rust
use zenoh::{Config, shm::{BlockOn, GarbageCollect, ShmProviderBuilder}, Wait};

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    let session = zenoh::open(Config::default()).await?;

    // Create a 1 MB SHM provider
    let provider = ShmProviderBuilder::default_backend(1024 * 1024)
        .wait()?;

    let publisher = session.declare_publisher("demo/example/shm").await?;

    for i in 0..100u32 {
        let msg = format!("[{i:4}] SHM payload");
        let mut buf = provider
            .alloc(msg.len())
            .with_policy::<BlockOn<GarbageCollect>>()
            .await?;
        buf[..msg.len()].copy_from_slice(msg.as_bytes());
        println!("Put SHM: {msg}");
        publisher.put(buf).await?;
        tokio::time::sleep(std::time::Duration::from_secs(1)).await;
    }
    Ok(())
}
```

The subscriber side uses the standard `z_sub` example unchanged — SHM is transparent to subscribers on the same host.

---

### QoS: real-time priority publisher (Rust)

```rust
use zenoh::{Config, qos::Priority};

#[tokio::main]
async fn main() {
    let session = zenoh::open(Config::default()).await.unwrap();
    let publisher = session
        .declare_publisher("robot/control/cmd_vel")
        .priority(Priority::RealTime)
        .congestion_control(zenoh::qos::CongestionControl::Block) // never drop
        .await
        .unwrap();

    publisher.put("move forward").await.unwrap();
}
```

---

### Matching listener — react when subscribers appear/disappear

Know when your publisher has active subscribers (Python):

```python
import zenoh

def on_matching_status(status: zenoh.MatchingStatus):
    if status.matching:
        print("Publisher has matching subscribers")
    else:
        print("Publisher has NO more matching subscribers")

with zenoh.open(zenoh.Config()) as session:
    pub = session.declare_publisher("demo/example/hello")
    pub.declare_matching_listener(on_matching_status)

    import time
    while True:
        pub.put("hello")
        time.sleep(1)
```

---

## Installation Quick Reference

```bash
# Router
brew install zenoh              # macOS
sudo apt install zenoh          # Debian/Ubuntu
# Or download from https://github.com/eclipse-zenoh/zenoh/releases
zenohd                          # start with defaults

# Python
pip install eclipse-zenoh

# Rust
cargo add zenoh                 # add to Cargo.toml
# Or add manually: zenoh = "1"

# C/C++
# Download pre-built from https://github.com/eclipse-zenoh/zenoh-c/releases
# Or build: cargo build --release (in zenoh-c repo)

# TypeScript/Node.js
npm install @eclipse-zenoh/zenoh-ts

# Go
go get github.com/eclipse-zenoh/zenoh-go
```

## See Also

- [Programming Model Guide](programming-model-guide.md) — detailed explanation of every API pattern shown here
- [Node Types Guide](node-types-guide.md) — when to use peer, client, or router mode in the configuration patterns
- [Key Expressions Guide](key-expressions-guide.md) — full syntax reference for the key expressions used in these examples
- [Config Connect Listen](config-connect-listen.md) — the connect/listen endpoint configuration shown in the multi-config patterns
