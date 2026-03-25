# Zenoh Config: Connect & Listen

Configuration reference for `connect` and `listen` sections of the Zenoh config. These control how a session establishes outgoing connections and inbound listening endpoints, including retry behavior.

---

## Table of Contents

- [Connect Configuration (`connect`)](#connect-configuration-connect)
  - [`connect.timeout_ms`](#connecttimeout_ms)
  - [`connect.endpoints`](#connectendpoints)
  - [`connect.exit_on_failure`](#connectexit_on_failure)
  - [`connect.retry`](#connectretry)
- [Listen Configuration (`listen`)](#listen-configuration-listen)
  - [`listen.timeout_ms`](#listentimeout_ms)
  - [`listen.endpoints`](#listenendpoints)
  - [`listen.exit_on_failure`](#listenexit_on_failure)
  - [`listen.retry`](#listenretry)
- [Special Values for `timeout_ms`](#special-values-for-timeout_ms)
- [`open` Configuration](#open-configuration)
  - [`open.return_conditions.connect_scouted`](#openreturn_conditionsconnect_scouted)
  - [`open.return_conditions.declares`](#openreturn_conditionsdeclares)
- [Source](#source)

## Connect Configuration (`connect`)

Controls which remote endpoints the session connects to at startup.

### `connect.timeout_ms`

**Type**: `Option<ModeDependentValue<i64>>`
**Default**: `{ router: -1, peer: -1, client: 0 }`

Total timeout in milliseconds for the full connect cycle (all endpoints, including retries).

- `-1` = wait indefinitely (infinite retry loop) — default for router and peer
- `0` = no retry; fail immediately if the initial connection attempt fails — default for client
- `> 0` = wait at most this many milliseconds across all retries

Accepts either a single value applied to all modes, or per-mode values:

```json5
// Single value:
connect: { timeout_ms: 5000 }

// Per-mode:
connect: { timeout_ms: { router: -1, peer: -1, client: 3000 } }
```

### `connect.endpoints`

**Type**: `ModeDependentValue<Vec<EndPoint>>`
**Default**: `[]` (empty — no outgoing connections)

List of endpoints to connect to at startup. Accepts a flat list or per-mode lists.

```json5
connect: {
  endpoints: ["tcp/192.168.1.10:7447", "tcp/192.168.1.11:7447"]
}

// Or per-mode:
connect: {
  endpoints: {
    router: ["tcp/10.0.0.1:7447"],
    peer:   ["tcp/10.0.0.2:7447"],
    client: ["tcp/10.0.0.1:7447"]
  }
}
```

Endpoint URI syntax: `<proto>/<address>`, e.g. `tcp/192.168.0.1:7447`.

Per-endpoint overrides (appended as `#key=value`):
- `iface=eth0` — bind to specific interface (TCP/UDP on Linux)
- `so_sndbuf=65000;so_rcvbuf=65000` — TCP socket buffer sizes
- `bind=192.168.0.1:0` — bind local socket to this address
- `dscp=0x08` — set DSCP field in IP header
- `prio=6-7;rel=0` — assign priority range and reliability to this link
- `exit_on_failure=true` — override global exit_on_failure for this endpoint
- `retry_period_init_ms=500` — override retry init period for this endpoint
- `retry_period_max_ms=5000` — override retry max period for this endpoint
- `retry_period_increase_factor=1.5` — override retry increase factor

### `connect.exit_on_failure`

**Type**: `Option<ModeDependentValue<bool>>`
**Default**: `{ router: false, peer: false, client: true }`

If true, the process exits when `timeout_ms` is exceeded without successful connection. If false, it continues running without the failed connections.

### `connect.retry`

**Type**: `Option<ConnectionRetryModeDependentConf>`

Retry backoff configuration for failed connect attempts. The entire `retry` block is optional; when omitted, defaults apply.

#### `connect.retry.period_init_ms`

**Type**: `Option<ModeDependentValue<i64>>` (or scalar)
**Default**: `1000` (1 second)

Initial wait in milliseconds before the first retry.

#### `connect.retry.period_max_ms`

**Type**: `Option<ModeDependentValue<i64>>` (or scalar)
**Default**: `4000` (4 seconds)

Maximum wait in milliseconds between retries. The backoff is capped at this value.

#### `connect.retry.period_increase_factor`

**Type**: `Option<ModeDependentValue<f64>>` (or scalar)
**Default**: `2.0`

Multiplicative factor applied to the retry period after each failed attempt. With default settings:
1s → 2s → 4s → 4s (capped) → …

**Full connect example:**

```json5
connect: {
  timeout_ms: { router: -1, peer: -1, client: 10000 },
  endpoints: ["tcp/10.0.0.1:7447"],
  exit_on_failure: { router: false, peer: false, client: true },
  retry: {
    period_init_ms: 1000,
    period_max_ms: 4000,
    period_increase_factor: 2,
  },
}
```

---

## Listen Configuration (`listen`)

Controls which local endpoints the session listens on for incoming connections.

### `listen.timeout_ms`

**Type**: `Option<ModeDependentValue<i64>>`
**Default**: `0` (all modes)

Total timeout in milliseconds for the full listen cycle (binding all endpoints).

- `0` = no retry; fail immediately if an endpoint cannot be bound
- `-1` = wait indefinitely
- `> 0` = maximum wait across all retries

### `listen.endpoints`

**Type**: `ModeDependentValue<Vec<EndPoint>>`
**Default**:
- **router**: `["tcp/[::]:7447"]` — listen on all interfaces, port 7447
- **peer**: `["tcp/[::]:0"]` — listen on all interfaces, OS-assigned port
- **client**: `[]` — no listening

```json5
listen: {
  endpoints: { router: ["tcp/[::]:7447"], peer: ["tcp/[::]:0"] }
}
```

### `listen.exit_on_failure`

**Type**: `Option<ModeDependentValue<bool>>`
**Default**: `true` (all modes)

If true, the process exits when a listen endpoint fails to bind after retries.

### `listen.retry`

Same structure as `connect.retry`.

**Defaults**:
- `period_init_ms`: `1000` (1 second)
- `period_max_ms`: `4000` (4 seconds)
- `period_increase_factor`: `2.0`

```json5
listen: {
  timeout_ms: 0,
  endpoints: { router: ["tcp/[::]:7447"], peer: ["tcp/[::]:0"] },
  exit_on_failure: true,
  retry: {
    period_init_ms: 1000,
    period_max_ms: 4000,
    period_increase_factor: 2,
  },
}
```

---

## Special Values for `timeout_ms`

| Value | Meaning |
|-------|---------|
| `-1`  | Infinite — retry forever |
| `0`   | No retry — fail immediately if not connectable |
| `> 0` | Timeout in milliseconds (across all retries) |

---

## `open` Configuration

The `open` section controls what conditions must be met before `zenoh::open()` returns.

### `open.return_conditions.connect_scouted`

**Type**: `Option<bool>`
**Default**: `true`

When `true`, `zenoh::open()` waits until scouted peers and routers are connected before returning. Setting to `false` may cause the first publications/queries after session open to be lost if a peer was scouted but not yet connected.

### `open.return_conditions.declares`

**Type**: `Option<bool>`
**Default**: `true`

When `true`, `zenoh::open()` waits until initial declarations (subscribers, publishers, queryables) from connected peers have been received before returning. Setting to `false` may cause extra startup traffic from peers.

```json5
open: {
  return_conditions: {
    connect_scouted: true,
    declares: true,
  },
}
```

---

## Source

- `repos/zenoh/commons/zenoh-config/src/lib.rs` — `ConnectConfig`, `ListenConfig`, `OpenConf`, `ReturnConditionsConf`
- `repos/zenoh/commons/zenoh-config/src/connection_retry.rs` — `ConnectionRetryModeDependentConf`, `ConnectionRetryConf`
- `repos/zenoh/commons/zenoh-config/src/defaults.rs` — default values
- `repos/zenoh/DEFAULT_CONFIG.json5` — annotated examples

## See Also

- [Scouting Guide](scouting-guide.md) — how nodes discover each other before establishing connections; complements static endpoints
- [Node Types Guide](node-types-guide.md) — router, peer, and client mode behaviors that determine default connect/listen settings
- [Encryption Guide](encryption-guide.md) — TLS/QUIC endpoint configuration that extends these connect/listen settings
- [Config Transport Unicast Multicast](config-transport-unicast-multicast.md) — transport-level session parameters once a connection is established
