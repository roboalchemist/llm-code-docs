# Zenoh Config: Miscellaneous Top-Level Fields

Configuration reference for miscellaneous top-level fields: session identity, metadata, namespace, timestamping, downsampling, low-pass filter, stats, plugins, and QoS overrides.

---

## Table of Contents

- [Session Identity](#session-identity)
  - [`id`](#id)
  - [`metadata`](#metadata)
  - [`mode`](#mode)
  - [`namespace`](#namespace)
- [Timestamping](#timestamping)
  - [`timestamping.enabled`](#timestampingenabled)
  - [`timestamping.drop_future_timestamp`](#timestampingdrop_future_timestamp)
- [Downsampling (`downsampling`)](#downsampling-downsampling)
  - [Item Fields](#item-fields)
- [Low-Pass Filter (`low_pass_filter`)](#low-pass-filter-low_pass_filter)
  - [Item Fields](#item-fields)
- [Per-Key Stats (`stats`)](#per-key-stats-stats)
  - [`stats.filters`](#statsfilters)
- [Plugins Loading (`plugins_loading`)](#plugins-loading-plugins_loading)
  - [`plugins_loading.enabled`](#plugins_loadingenabled)
  - [`plugins_loading.search_dirs`](#plugins_loadingsearch_dirs)
- [QoS Overrides (`qos`)](#qos-overrides-qos)
  - [`qos.publication`](#qospublication)
  - [`qos.network`](#qosnetwork)
- [Source](#source)

## Session Identity

### `id`

**Type**: `Option<ZenohId>` (128-bit hex string, up to 32 hex chars, no leading zeros)
**Default**: randomly generated `u128` at session creation

The Zenoh ID of this session. Must be unique across the entire Zenoh infrastructure. If not set, a random ID is generated each time the session opens.

```json5
// id: "1234567890abcdef1234567890abcdef"
```

> **Warning**: Setting a fixed ID means all instances using this config file will collide unless you ensure uniqueness. Omit this field in production deployments unless you manage IDs explicitly.

### `metadata`

**Type**: `Value` (arbitrary JSON)
**Default**: `null`

Arbitrary JSON metadata attached to this node. Not interpreted by Zenoh — available in the admin space at `@/<zid>/router`, `@/<zid>/peer`, or `@/<zid>/client`.

```json5
metadata: {
  name: "sensor-node-1",
  location: "Building A, Floor 2",
  version: "1.0.0",
}
```

### `mode`

**Type**: `Option<WhatAmI>`
**Default**: `null` (library default: `peer`; `zenohd` daemon default: `router`)
**Valid values**: `"router"`, `"peer"`, `"client"`

The operating mode of this Zenoh session. Controls routing behavior, scouting role, and default connect/listen endpoints.

```json5
mode: "peer"
```

### `namespace`

**Type**: `Option<OwnedNonWildKeyExpr>` (non-wildcard key expression)
**Default**: `null` (no namespace)

A prefix applied to all outgoing key expressions from this session, and stripped from all incoming key expressions. Creates a logical namespace for the session.

Example: with `namespace: "factory1"`, a `session.put("sensor/temp", ...)` publishes to `factory1/sensor/temp`, and subscriptions to `factory1/sensor/temp` are received as `sensor/temp`.

```json5
namespace: "factory1"
```

> **Note**: The namespace must not contain wildcards. Use a plain prefix string.

---

## Timestamping

### `timestamping.enabled`

**Type**: `Option<ModeDependentValue<bool>>`
**Default**: `{ router: true, peer: false, client: false }`

When enabled, the node adds a HLC (Hybrid Logical Clock) timestamp to data messages that do not already have one. Timestamps are used by storage backends for conflict resolution and data ordering.

Routers timestamp by default; peers and clients do not.

```json5
timestamping: {
  enabled: { router: true, peer: false, client: false }
}
```

### `timestamping.drop_future_timestamp`

**Type**: `Option<bool>`
**Default**: `false`

Controls what happens when a message arrives with a timestamp in the future (relative to the node's local HLC).

- `false` (default): Future-timestamped messages are **re-timestamped** to the current HLC time before forwarding.
- `true`: Future-timestamped messages are **dropped**.

```json5
timestamping: { drop_future_timestamp: false }
```

> Setting `drop_future_timestamp: true` is useful when strict monotonicity is required and clock skew is a concern, but note that messages will be lost.

---

## Downsampling (`downsampling`)

**Type**: `Vec<DownsamplingItemConf>`
**Default**: `[]` (no downsampling)

An array of downsampling rules. Each item specifies interfaces, link protocols, message types, and rules that throttle messages to a maximum frequency.

### Item Fields

#### `downsampling[].id`

**Type**: `Option<String>`
**Default**: `null`

Optional identifier for this downsampling configuration item (for debugging/logging).

#### `downsampling[].interfaces`

**Type**: `Option<NEVec<String>>`
**Default**: `null` (applies to all interfaces)

List of network interface names to apply this rule to. If `null`, applies to all interfaces.

#### `downsampling[].link_protocols`

**Type**: `Option<NEVec<InterceptorLink>>`
**Default**: `null` (applies to all link protocols)

List of link protocol types to filter on. Valid values: `"tcp"`, `"udp"`, `"tls"`, `"quic"`, `"serial"`, `"unixpipe"`, `"unixsock-stream"`, `"vsock"`, `"ws"`.

#### `downsampling[].messages`

**Type**: `NEVec<DownsamplingMessage>` (required, non-empty)

Message types to downsample. Valid values: `"put"`, `"delete"`, `"query"`, `"reply"`.

> **Deprecated**: `"push"` is deprecated; use `"put"` and/or `"delete"` instead.

#### `downsampling[].flows`

**Type**: `Option<NEVec<InterceptorFlow>>`
**Default**: `null` (applies to both directions)

Direction(s) to apply downsampling: `"egress"` (outgoing) and/or `"ingress"` (incoming).

#### `downsampling[].rules`

**Type**: `NEVec<DownsamplingRuleConf>` (required, non-empty)

List of per-key-expression downsampling rules.

Each rule:
- `key_expr` (`OwnedKeyExpr`, required): Key expression to match
- `freq` (`f64`, required): Maximum frequency in **Hertz** (messages per second)

```json5
downsampling: [
  {
    interfaces: ["eth0"],
    messages: ["put"],
    flows: ["egress"],
    rules: [
      { key_expr: "sensor/**", freq: 10.0 },
      { key_expr: "telemetry/high-rate/**", freq: 1.0 },
    ],
  }
]
```

> **Note**: The frequency field is named `freq` (not `rate`) in the source.

---

## Low-Pass Filter (`low_pass_filter`)

**Type**: `Vec<LowPassFilterConf>`
**Default**: `[]`

Drops messages whose payload exceeds a size limit. Unlike downsampling (which rate-limits), the low-pass filter drops by size.

### Item Fields

#### `low_pass_filter[].id`

**Type**: `Option<String>` — optional identifier.

#### `low_pass_filter[].interfaces`

**Type**: `Option<NEVec<String>>` — network interfaces to apply this filter to (`null` = all).

#### `low_pass_filter[].link_protocols`

**Type**: `Option<NEVec<InterceptorLink>>` — link protocols to filter on (`null` = all).

#### `low_pass_filter[].flows`

**Type**: `Option<NEVec<InterceptorFlow>>` — direction(s): `"egress"` / `"ingress"` (`null` = both).

#### `low_pass_filter[].messages`

**Type**: `NEVec<LowPassFilterMessage>` (required)

Message types to apply the filter to. Valid values: `"put"`, `"delete"`, `"query"`, `"reply"`.

#### `low_pass_filter[].key_exprs`

**Type**: `NEVec<OwnedKeyExpr>` (required)

Key expressions to apply the size filter to.

#### `low_pass_filter[].size_limit`

**Type**: `usize` (bytes, required)

Maximum allowed payload size in bytes. Messages larger than this value are dropped.

```json5
low_pass_filter: [
  {
    interfaces: null,
    messages: ["put"],
    key_exprs: ["video/**"],
    size_limit: 65536,  // drop video > 64 KiB
  }
]
```

---

## Per-Key Stats (`stats`)

### `stats.filters`

**Type**: `Vec<StatsFilterConfig>`
**Default**: `[]`

Configures per-key-expression statistics collection. Each entry specifies a key expression to track. Statistics are available in the admin space.

Each item:
- `key` (`OwnedKeyExpr`, required): Key expression to collect stats for

> **Note**: The field is named `key` (not `key_expr`) in the source.

```json5
stats: {
  filters: [
    { key: "sensor/**" },
    { key: "control/robot/*" },
  ]
}
```

---

## Plugins Loading (`plugins_loading`)

### `plugins_loading.enabled`

**Type**: `bool`
**Default**: `false`

Whether dynamic plugin loading is enabled. When `false`, no plugins are loaded even if `plugins` entries are configured.

### `plugins_loading.search_dirs`

**Type**: `LibSearchDirs` (list of directory paths)
**Default**: `[<exe-parent>, ".", "~/.zenoh/lib", "/opt/homebrew/lib", "/usr/local/lib", "/usr/lib"]`

Directories searched for plugin shared libraries when no explicit `__path__` is given in a plugin configuration. The default list includes the executable's directory, current directory, and standard system library paths. Setting this field overrides the default list.

```json5
plugins_loading: {
  enabled: true,
  search_dirs: ["/usr/lib/zenoh/plugins", "/opt/zenoh/plugins"],
}
```

---

## QoS Overrides (`qos`)

### `qos.publication`

**Type**: `PublisherQoSConfList`
**Default**: `[]` (no overrides)

A list of per-key-expression QoS configurations for PUT and DELETE messages. Each entry specifies:
- `key_exprs`: List of key expressions to match
- `config.congestion_control`: `"drop"` | `"block"` | `"block_first"` (unstable)
- `config.priority`: `"real_time"` | `"interactive_high"` | `"interactive_low"` | `"data_high"` | `"data"` | `"data_low"` | `"background"`
- `config.express`: `bool` — disable batching for this key expression
- `config.reliability`: `"reliable"` | `"best_effort"` (unstable)
- `config.allowed_destination`: publisher locality (unstable)

```json5
qos: {
  publication: [
    {
      key_exprs: ["control/**"],
      config: {
        priority: "interactive_high",
        congestion_control: "block",
        express: true,
      }
    }
  ]
}
```

### `qos.network`

**Type**: `Vec<QosOverwriteItemConf>`
**Default**: `[]`

Network-level QoS overwrite rules. Unlike `qos.publication` (which affects the publisher API), these rules are applied by the transport interceptor regardless of the publisher's configured QoS. Useful for enforcing QoS policies at the network boundary.

Each item has a **required** `messages` field (`NEVec<QosOverwriteMessage>`, non-empty; valid values: `"put"`, `"delete"`, `"query"`). Optional filtering by: `zids`, `interfaces`, `link_protocols`, `key_exprs`, `flows`, `qos` (filter), `payload_size` (byte range).

The `overwrite` field specifies the new values:
- `priority` — accepts either a priority name string (`"real_time"`, `"interactive_high"`, `"interactive_low"`, `"data_high"`, `"data"`, `"data_low"`, `"background"`) **or** a signed integer increment (`+1`, `-2`, etc.)
- `congestion_control` — `"drop"` or `"block"`
- `express` — `bool`

Note: `reliability` overwrite is not currently supported (commented-out TODO in `qos.rs`).

```json5
qos: {
  network: [
    {
      messages: ["put"],
      key_exprs: ["telemetry/**"],
      overwrite: {
        priority: "data_low",
        congestion_control: "drop",
      }
    }
  ]
}
```

---

## Source

- `repos/zenoh/commons/zenoh-config/src/lib.rs` — `Config`, `TimestampingConf`, `DownsamplingItemConf`, `DownsamplingRuleConf`, `LowPassFilterConf`, `StatsConfig`, `StatsFilterConfig`, `PluginsLoading`, `QoSConfig`, `QosOverwriteItemConf`
- `repos/zenoh/commons/zenoh-config/src/qos.rs` — `PublisherQoSConfList`, `PublisherQoSConf`, `PublisherQoSConfig`
- `repos/zenoh/commons/zenoh-config/src/defaults.rs` — `timestamping.enabled`, `timestamping.drop_future_timestamp`, `queries_default_timeout`
- `repos/zenoh/DEFAULT_CONFIG.json5` — annotated examples

## See Also

- [Admin Space Guide](admin-space-guide.md) — the `adminspace.enabled` and `adminspace.permissions` settings controlled by this config
- [QoS Guide](qos-guide.md) — complete guide to the `qos.publication` and `qos.network` override patterns documented here
- [Config Routing Aggregation](config-routing-aggregation.md) — the `routing` and `aggregation` config sections that complement these top-level fields
- [Scouting Guide](scouting-guide.md) — scouting-related config fields referenced in the identity and mode sections
