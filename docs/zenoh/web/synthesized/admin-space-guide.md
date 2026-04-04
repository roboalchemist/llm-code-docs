# Zenoh Admin Space Guide

The Admin Space is a built-in introspection mechanism that exposes live runtime state through standard zenoh key expressions. Any zenoh application that can perform a `get()` query can inspect routers, sessions, subscribers, publishers, routing tables, and plugins — across the entire network.

---

## Table of Contents

- [What the Admin Space Is](#what-the-admin-space-is)
  - [Two Layers](#two-layers)
  - [Access Patterns](#access-patterns)
- [Configuration](#configuration)
  - [JSON5 (zenohd config)](#json5-zenohd-config)
  - [TOML format](#toml-format)
  - [Programmatic (Rust)](#programmatic-rust)
  - [Via environment or CLI flag](#via-environment-or-cli-flag)
  - [Access Control Note](#access-control-note)
- [Key Expression Reference](#key-expression-reference)
  - [Runtime Admin Keys (`@/<zid>/<whatami>/...`)](#runtime-admin-keys-zidwhatami)
  - [Session Admin Keys (`@/<zid>/session/...`)](#session-admin-keys-zidsession)
- [How to Query the Admin Space](#how-to-query-the-admin-space)
  - [Rust Examples](#rust-examples)
  - [Python Examples](#python-examples)
- [Use Cases](#use-cases)
  - [Monitoring](#monitoring)
  - [Debugging](#debugging)
  - [Topology Discovery](#topology-discovery)
- [Summary of All Keys](#summary-of-all-keys)

## What the Admin Space Is

The Admin Space maps the `@/` key prefix namespace to live router and session state. Everything under `@/` is queryable using the normal zenoh `get()` API. The space is read-only by default and writable only for runtime config changes when explicitly enabled.

### Two Layers

There are two distinct layers of the admin space:

**1. Runtime admin** (`@/<zid>/<whatami>/...`): Populated by the `zenohd` router daemon or any session running in peer mode. Contains routing state, declared publishers/subscribers/queryables, link state tables, metrics, and plugin info.

**2. Session admin** (`@/<zid>/session/...`): Populated by every zenoh session (router, peer, or client). Contains the session's own transport connections and link-level details. Also emits real-time events as pub/sub messages.

### Access Patterns

| Purpose | Key expression |
|---------|---------------|
| Query your own node | `@/<own_zid>/<whatami>/**` |
| Query a specific remote node | `@/<remote_zid>/<whatami>/**` |
| Scan all reachable nodes | `@/**` |

The `<whatami>` segment is literally `router`, `peer`, or `client` depending on the node's mode.

Remote nodes are reachable via zenoh's built-in linkstate routing — the query is forwarded automatically to the target node.

---

## Configuration

The admin space is **disabled by default**. Enable it in the node's config:

### JSON5 (zenohd config)

```json5
{
  adminspace: {
    // Enable the admin space (default: false)
    enabled: true,
    permissions: {
      // Allow GET queries to the admin space (default: true when enabled)
      read: true,
      // Allow PUT/DELETE to @/<zid>/<whatami>/config/** for runtime config changes (default: false)
      write: false,
    }
  }
}
```

### TOML format

```toml
[adminspace]
enabled = true

[adminspace.permissions]
read = true
write = false
```

### Programmatic (Rust)

```rust
let mut config = zenoh::Config::default();
config.adminspace.set_enabled(true).unwrap();
let session = zenoh::open(config).await.unwrap();
```

### Via environment or CLI flag

```bash
zenohd --cfg 'adminspace/enabled:true'
```

### Access Control Note

The `@` prefix is subject to standard zenoh access control rules. If your deployment uses ACL, ensure the `@/**` key space is permitted for the principals that need to query it. The `adminspace.permissions.read` flag is a secondary gate checked after ACL.

---

## Key Expression Reference

All keys below use `<zid>` for the node's ZenohId (a 128-bit hex string, e.g. `a1b2c3d4e5f60718293a4b5c6d7e8f90`) and `<whatami>` for the mode string.

### Runtime Admin Keys (`@/<zid>/<whatami>/...`)

---

#### `@/<zid>/<whatami>` — Node identity and sessions

The root key returns a comprehensive snapshot of the node.

**Returns** `application/json`:

```json
{
  "zid": "a1b2c3d4e5f60718293a4b5c6d7e8f90",
  "version": "1.0.0 built with rustc 1.78.0",
  "metadata": {
    "name": "strawberry",
    "location": "Penny Lane"
  },
  "locators": [
    "tcp/192.168.1.10:7447"
  ],
  "sessions": [
    {
      "peer": "b2c3d4e5f6071829",
      "whatami": "router",
      "links": [
        { "src": "tcp/192.168.1.10:7447", "dst": "tcp/192.168.1.20:7447" }
      ],
      "weight": null,
      "shm": false
    }
  ],
  "plugins": {
    "storage_manager": {
      "name": "zenoh_plugin_storage_manager",
      "path": "/usr/local/lib/libzenoh_plugin_storage_manager.so"
    }
  }
}
```

The `metadata` field mirrors the `metadata:` block from the node's config file. The `sessions` array lists all active unicast and multicast transport sessions. Add `?_stats=true` to the query selector to include traffic statistics in the response (requires `stats` feature).

---

#### `@/<zid>/<whatami>/metrics` — Prometheus metrics

**Returns** `application/openmetrics-text; version=1.0.0; charset=utf-8` (gzip-compressed by default).

```
# HELP zenoh_build Zenoh build version.
# TYPE zenoh_build info
zenoh_build_info{local_id="a1b2c3d4...",local_whatami="router",version="1.0.0"} 1
# HELP zenoh_rx_z_put_msgs_total Total z_put messages received
# TYPE zenoh_rx_z_put_msgs_total counter
zenoh_rx_z_put_msgs_total{transport="a1b2...",link="tcp/..."} 42
# EOF
```

**Query parameters:**

| Parameter | Default | Effect |
|-----------|---------|--------|
| `per_transport=false` | true | Aggregate across transports |
| `per_link=false` | true | Aggregate across links |
| `per_key=false` | true | Aggregate across key expressions |
| `disconnected=true` | false | Include stats for closed transports |
| `descriptors=false` | true | Omit `# HELP` / `# TYPE` lines |
| `compression=false` | true | Return uncompressed text |

Requires the `stats` Cargo feature to be enabled at compile time. Without it, only `zenoh_build_info` is returned.

---

#### `@/<zid>/router/linkstate/routers` — Router link state table

**Available on**: nodes running in `router` mode only.

**Returns** `text/plain` — human-readable linkstate table showing which routers are known to this router and through which path.

---

#### `@/<zid>/<whatami>/linkstate/peers` — Peer link state table

**Available on**: `router` and `peer` mode nodes (not `client`).

**Returns** `text/plain` — link state table for known peers.

---

#### `@/<zid>/<whatami>/subscriber/**` — Declared subscribers

Each matching sub-key is one subscriber declaration. The `**` glob returns all subscribers; use a more specific suffix to filter by resource name.

**Key pattern**: `@/<zid>/<whatami>/subscriber/<resource_key_expr>`

**Returns** `application/json` — source metadata per subscriber:

```json
{
  "face_id": 3,
  "source_id": 0,
  "source_sn": 0
}
```

Example: to find all subscribers for keys under `sensors/`:
```
@/*/router/subscriber/sensors/**
```

---

#### `@/<zid>/<whatami>/publisher/**` — Declared publishers

**Key pattern**: `@/<zid>/<whatami>/publisher/<resource_key_expr>`

**Returns** `application/json` — source metadata per publisher (same structure as subscriber).

---

#### `@/<zid>/<whatami>/queryable/**` — Declared queryables

**Key pattern**: `@/<zid>/<whatami>/queryable/<resource_key_expr>`

**Returns** `application/json` — source metadata per queryable.

---

#### `@/<zid>/<whatami>/querier/**` — Declared queriers

**Key pattern**: `@/<zid>/<whatami>/querier/<resource_key_expr>`

**Returns** `application/json` — source metadata per querier.

---

#### `@/<zid>/<whatami>/token/**` — Liveliness tokens

**Key pattern**: `@/<zid>/<whatami>/token/<liveliness_key_expr>`

**Returns** `application/json` — source metadata per liveliness token.

---

#### `@/<zid>/router/route/successor/**` — Routing successor table

**Available on**: `router` mode nodes only.

Returns the next-hop router for each (source, destination) pair in the routing table.

**Full table query**:
```
@/<zid>/router/route/successor/**
```
Returns one reply per entry, each at key:
```
@/<zid>/router/route/successor/src/<src_zid>/dst/<dst_zid>
```
Value is a JSON string containing the successor router ZID.

**Point query** (more efficient):
```
@/<zid>/router/route/successor/src/<src_zid>/dst/<dst_zid>
```
Returns the single successor ZID for that specific (src, dst) pair.

---

#### `@/<zid>/<whatami>/plugins/**` — Loaded plugin metadata

**Available when**: compiled with the `plugins` feature.

**Key pattern**: `@/<zid>/<whatami>/plugins/<plugin_id>`

**Returns** `application/json`:

```json
{
  "id": "storage_manager",
  "name": "zenoh_plugin_storage_manager",
  "path": "/usr/local/lib/libzenoh_plugin_storage_manager.so"
}
```

---

#### `@/<zid>/<whatami>/status/plugins/**` — Plugin runtime status

**Available when**: compiled with the `plugins` feature.

Each plugin exposes its own status sub-keys via its `adminspace_getter()` implementation.

**Plugin path sub-key** (always present):
```
@/<zid>/<whatami>/status/plugins/<plugin_id>/__path__
```
Returns the filesystem path of the loaded plugin library.

**Plugin-specific status** (varies by plugin):
```
@/<zid>/<whatami>/status/plugins/storage_manager/**
@/<zid>/<whatami>/status/plugins/rest/**
```

---

#### `@/<zid>/<whatami>/config/**` — Runtime configuration (writable)

**Read**: GET returns the current config value at the given path as JSON5.

**Write**: PUT with a JSON5 value updates the running config. Requires `adminspace.permissions.write: true`.

Example: change the log level at runtime:
```
PUT @/<zid>/router/config/mode  "peer"
```

---

### Session Admin Keys (`@/<zid>/session/...`)

These keys are managed by the session-level admin registered in `api/admin.rs`. They represent the session's transport connectivity and emit live events.

---

#### `@/<zid>/session/transport/unicast/<peer_zid>` — Unicast transport

One key per active unicast peer connection.

**Returns** `application/json`:

```json
{
  "zid": "b2c3d4e5f6071829",
  "whatami": "router",
  "is_qos": true
}
```

Also emits **real-time pub/sub events**: a `Put` sample when a transport opens, a `Delete` sample when it closes.

---

#### `@/<zid>/session/transport/multicast/<peer_zid>` — Multicast transport peer

One key per multicast group peer.

**Returns** `application/json`:

```json
{
  "zid": "c3d4e5f607182930",
  "whatami": "peer",
  "is_qos": false
}
```

---

#### `@/<zid>/session/transport/<type>/<peer_zid>/link/<link_hash>` — Transport link

One key per physical link (identified by a hash of the link's properties).

`<type>` is `unicast` or `multicast`. `<link_hash>` is a decimal integer (hash of the link struct).

**Returns** `application/json`:

```json
{
  "src": "tcp/192.168.1.10:7447",
  "dst": "tcp/192.168.1.20:7447",
  "group": null,
  "mtu": 65000,
  "is_streamed": true,
  "interfaces": ["eth0"],
  "auth_identifier": null,
  "priorities": {
    "start": "RealTime",
    "end": "Background"
  },
  "reliability": "Reliable"
}
```

Also emits **real-time pub/sub events** when links open or close.

---

## How to Query the Admin Space

### Rust Examples

#### Get local node identity and sessions

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let mut config = Config::default();
    config.adminspace.set_enabled(true).unwrap();

    let session = zenoh::open(config).await.unwrap();

    // Get our own ZID
    let own_zid = session.info().zid().await.to_string();

    // Query the root key — returns node identity, locators, sessions, plugins
    let replies = session
        .get(format!("@/{own_zid}/router"))
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            let json: serde_json::Value = serde_json::from_slice(
                &sample.payload().to_bytes()
            ).unwrap();
            println!("ZID: {}", json["zid"]);
            println!("Version: {}", json["version"]);
            println!("Sessions: {}", json["sessions"]);
        }
    }
}
```

#### List all active sessions (transports)

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let mut config = Config::default();
    config.adminspace.set_enabled(true).unwrap();

    let session = zenoh::open(config).await.unwrap();
    let own_zid = session.info().zid().await.to_string();

    // Query session-level transport info
    let replies = session
        .get(format!("@/{own_zid}/session/transport/unicast/**"))
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            let json: serde_json::Value = serde_json::from_slice(
                &sample.payload().to_bytes()
            ).unwrap();
            println!(
                "Connected to peer {} ({}), QoS: {}",
                json["zid"], json["whatami"], json["is_qos"]
            );
        }
    }
}
```

#### List all subscribers on the local router

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let mut config = Config::default();
    config.adminspace.set_enabled(true).unwrap();

    let session = zenoh::open(config).await.unwrap();
    let own_zid = session.info().zid().await.to_string();

    let replies = session
        .get(format!("@/{own_zid}/router/subscriber/**"))
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            // The key expression suffix after /subscriber/ is the declared KE pattern
            let ke = sample.key_expr().as_str();
            let sub_ke = ke
                .split("/subscriber/")
                .nth(1)
                .unwrap_or("?");
            println!("Subscriber: {sub_ke}");
        }
    }
}
```

#### Discover all reachable routers

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let mut config = Config::default();
    config.adminspace.set_enabled(true).unwrap();

    let session = zenoh::open(config).await.unwrap();

    // Query all nodes — wildcard ZID matches any reachable router
    let replies = session
        .get("@/*/router")
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            let json: serde_json::Value = serde_json::from_slice(
                &sample.payload().to_bytes()
            ).unwrap();
            println!(
                "Router: {} at {:?}",
                json["zid"], json["locators"]
            );
        }
    }
}
```

#### Get storage manager status

```rust
use zenoh::Config;

#[tokio::main]
async fn main() {
    let mut config = Config::default();
    config.adminspace.set_enabled(true).unwrap();

    let session = zenoh::open(config).await.unwrap();
    let own_zid = session.info().zid().await.to_string();

    let replies = session
        .get(format!("@/{own_zid}/router/status/plugins/storage_manager/**"))
        .await
        .unwrap();

    while let Ok(reply) = replies.recv_async().await {
        if let Ok(sample) = reply.result() {
            println!("{}: {}",
                sample.key_expr(),
                sample.payload().try_to_string().unwrap_or_default()
            );
        }
    }
}
```

#### Monitor link events in real time (subscriber on admin KE)

```rust
use zenoh::{Config, sample::SampleKind};

#[tokio::main]
async fn main() {
    let mut config = Config::default();
    config.adminspace.set_enabled(true).unwrap();

    let session = zenoh::open(config).await.unwrap();
    let own_zid = session.info().zid().await.to_string();

    // Subscribe to all transport/link events for this session
    let subscriber = session
        .declare_subscriber(format!("@/{own_zid}/session/**"))
        .await
        .unwrap();

    println!("Monitoring session events for {own_zid}...");
    while let Ok(sample) = subscriber.recv_async().await {
        match sample.kind() {
            SampleKind::Put => {
                println!("[UP]   {}", sample.key_expr());
            }
            SampleKind::Delete => {
                println!("[DOWN] {}", sample.key_expr());
            }
        }
    }
}
```

---

### Python Examples

#### Get local router info

```python
import zenoh
import json

config = zenoh.Config()
config.insert_json5("adminspace/enabled", "true")

with zenoh.open(config) as session:
    own_zid = str(session.info().zid())

    replies = session.get(f"@/{own_zid}/router")
    for reply in replies:
        if reply.ok:
            data = json.loads(reply.ok.payload.to_bytes())
            print(f"ZID: {data['zid']}")
            print(f"Version: {data['version']}")
            print(f"Locators: {data['locators']}")
            for s in data.get("sessions", []):
                print(f"  Session: {s['peer']} ({s['whatami']})")
```

#### List all subscribers

```python
import zenoh
import json

config = zenoh.Config()
config.insert_json5("adminspace/enabled", "true")

with zenoh.open(config) as session:
    own_zid = str(session.info().zid())

    replies = session.get(f"@/{own_zid}/router/subscriber/**")
    for reply in replies:
        if reply.ok:
            ke = str(reply.ok.key_expr)
            # The key after /subscriber/ is the declared resource KE
            sub_ke = ke.split("/subscriber/", 1)[-1] if "/subscriber/" in ke else ke
            print(f"Subscriber: {sub_ke}")
```

#### Discover all routers in the network

```python
import zenoh
import json

config = zenoh.Config()
config.insert_json5("adminspace/enabled", "true")
# Connect to a router so we can reach the wider network
config.insert_json5("connect/endpoints", '["tcp/localhost:7447"]')

with zenoh.open(config) as session:
    replies = session.get("@/*/router")
    for reply in replies:
        if reply.ok:
            data = json.loads(reply.ok.payload.to_bytes())
            print(f"Router {data['zid']} @ {data.get('locators', [])}")
```

#### Monitor link events

```python
import zenoh

def on_event(sample):
    kind = "UP" if str(sample.kind) == "Put" else "DOWN"
    print(f"[{kind}] {sample.key_expr}")

config = zenoh.Config()
config.insert_json5("adminspace/enabled", "true")

with zenoh.open(config) as session:
    own_zid = str(session.info().zid())

    sub = session.declare_subscriber(f"@/{own_zid}/session/**", on_event)
    print(f"Watching events for {own_zid}. Press CTRL-C to stop.")
    try:
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
```

#### Update config at runtime (requires write permission)

```python
import zenoh

config = zenoh.Config()
config.insert_json5("adminspace/enabled", "true")
config.insert_json5("adminspace/permissions/write", "true")

with zenoh.open(config) as session:
    own_zid = str(session.info().zid())

    # Set metadata name at runtime
    session.put(
        f"@/{own_zid}/router/config/metadata/name",
        b'"new-node-name"'
    )
    print("Config updated")
```

---

## Use Cases

### Monitoring

**Topology dashboard**: Poll `@/*/router` periodically to enumerate all routers. For each, extract `locators` and `sessions` to build a network graph. Each session's `peer` field links nodes.

**Session drop detection**: Subscribe to `@/<zid>/session/transport/unicast/**`. A `Delete` sample on this key expression fires when a peer disconnects. The key expression suffix (`/transport/unicast/<peer_zid>`) identifies which peer disconnected.

**Count active subscribers per namespace**: Query `@/*/router/subscriber/sensors/**` to find all subscriptions under `sensors/` across all routers. Count distinct replies to get the total.

**Operational metrics**: Query `@/*/router/metrics` to collect Prometheus-compatible metrics from every router. Feed directly into Prometheus or a compatible scraper.

---

### Debugging

**Verify subscription propagation**: After declaring a subscriber on `sensors/temperature`, query `@/*/router/subscriber/sensors/temperature` across all routers. Every router in the network that has a route for this KE should appear in the replies.

**Check publisher visibility**: Query `@/*/router/publisher/my/key/**`. If a specific router is missing, it has no route to the publisher's KE — check linkstate or routing config.

**Inspect routing table**: When data isn't flowing from `src_zid` to `dst_zid`, query:
```
@/<src_zid>/router/route/successor/src/<src_zid>/dst/<dst_zid>
```
If there's no reply, that router has no path. If the reply is an unexpected ZID, the routing is suboptimal or misconfigured.

**Debug a disconnected peer**: When a client can't reach data, query its session's transport state:
```
@/<client_zid>/session/transport/unicast/**
```
If empty, the client has no connected router. If the router ZID appears but data is still not flowing, the issue is routing or subscription visibility.

---

### Topology Discovery

Walk the entire zenoh network:

```python
import zenoh
import json
from collections import defaultdict

config = zenoh.Config()
config.insert_json5("adminspace/enabled", "true")
config.insert_json5("connect/endpoints", '["tcp/localhost:7447"]')

with zenoh.open(config) as session:
    # Step 1: discover all routers
    routers = {}
    for reply in session.get("@/*/router"):
        if reply.ok:
            data = json.loads(reply.ok.payload.to_bytes())
            zid = data["zid"]
            routers[zid] = {
                "locators": data.get("locators", []),
                "metadata": data.get("metadata", {}),
                "peers": []
            }

    # Step 2: for each router, get its peer connections
    for zid in routers:
        for reply in session.get(f"@/{zid}/session/transport/unicast/**"):
            if reply.ok:
                peer_data = json.loads(reply.ok.payload.to_bytes())
                routers[zid]["peers"].append({
                    "zid": peer_data["zid"],
                    "whatami": peer_data["whatami"]
                })

    # Print the topology
    for zid, info in routers.items():
        print(f"\nRouter {zid[:8]}...")
        print(f"  Locators: {info['locators']}")
        print(f"  Metadata: {info['metadata']}")
        for peer in info["peers"]:
            print(f"  -> {peer['whatami']} {peer['zid'][:8]}...")
```

---

## Summary of All Keys

| Key expression | Mode | Returns | Notes |
|---|---|---|---|
| `@/<zid>/<whatami>` | all | JSON: zid, version, metadata, locators, sessions, plugins | Root identity |
| `@/<zid>/<whatami>/metrics` | all | OpenMetrics text | Gzip by default; requires `stats` feature for full data |
| `@/<zid>/router/linkstate/routers` | router | Text | Router link state |
| `@/<zid>/<whatami>/linkstate/peers` | router, peer | Text | Peer link state |
| `@/<zid>/<whatami>/subscriber/**` | all | JSON sources per KE | All declared subscribers |
| `@/<zid>/<whatami>/publisher/**` | all | JSON sources per KE | All declared publishers |
| `@/<zid>/<whatami>/queryable/**` | all | JSON sources per KE | All declared queryables |
| `@/<zid>/<whatami>/querier/**` | all | JSON sources per KE | All declared queriers |
| `@/<zid>/<whatami>/token/**` | all | JSON sources per KE | All liveliness tokens |
| `@/<zid>/router/route/successor/**` | router | JSON ZID | Next-hop routing table |
| `@/<zid>/<whatami>/plugins/**` | all | JSON plugin info | Loaded plugins (requires `plugins` feature) |
| `@/<zid>/<whatami>/status/plugins/**` | all | JSON plugin status | Per-plugin runtime status (requires `plugins` feature) |
| `@/<zid>/<whatami>/config/**` | all | JSON5 config value | Readable always; writable if `permissions.write=true` |
| `@/<zid>/session/transport/unicast/<peer_zid>` | all | JSON transport info | Live events via pub/sub |
| `@/<zid>/session/transport/multicast/<peer_zid>` | all | JSON transport info | Live events via pub/sub |
| `@/<zid>/session/transport/<type>/<peer_zid>/link/<hash>` | all | JSON link info | Live events via pub/sub |

## See Also

- [ACL Guide](acl-guide.md) — access control lists that protect the `@/**` admin namespace from external access
- [Config Misc](config-misc.md) — `adminspace.enabled` and `adminspace.permissions` configuration fields
- [Architecture Guide](architecture-guide.md) — protocol context for how the admin space fits into the overall Zenoh architecture
