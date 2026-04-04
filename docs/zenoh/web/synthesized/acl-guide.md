# Zenoh Access Control (ACL) Guide

## Table of Contents

- [Overview](#overview)
- [Configuration Structure](#configuration-structure)
- [Rules](#rules)
- [Subjects](#subjects)
  - [Subject Dimensions](#subject-dimensions)
  - [ZID Warning](#zid-warning)
  - [Example Subjects](#example-subjects)
- [Policies](#policies)
- [Default Permission](#default-permission)
- [Examples](#examples)
  - [Example 1: Allow only subscribers from a specific interface](#example-1-allow-only-subscribers-from-a-specific-interface)
  - [Example 2: mTLS cert CN-based authorization](#example-2-mtls-cert-cn-based-authorization)
  - [Example 3: Deny admin-space access for all external connections](#example-3-deny-admin-space-access-for-all-external-connections)
- [Important Notes](#important-notes)
  - [Rule Evaluation Order](#rule-evaluation-order)
  - [Performance Considerations](#performance-considerations)
  - [ZID Is Not Authentication](#zid-is-not-authentication)
  - [ACL Scope](#acl-scope)

## Overview

Zenoh's Access Control List (ACL) system lets you restrict which nodes can publish, subscribe, query, or reply on specific key expressions. ACL rules are evaluated at the router or peer level — messages matching a deny rule (or not matching any allow rule when `default_permission` is `deny`) are dropped before routing.

ACL is absent from the zenoh.io website docs but is fully documented in `DEFAULT_CONFIG.json5` and implemented in `zenoh/src/net/routing/interceptor/access_control.rs`.

**When to use ACL:**
- Multi-tenant deployments where different clients should not see each other's data
- Edge nodes that must not publish admin-space (`@/...`) data to the cloud
- TLS-authenticated endpoints where you want per-CN authorization
- Defense-in-depth alongside transport-layer authentication

---

## Configuration Structure

ACL is configured under the `access_control` key in the JSON5 config. It is disabled by default.

```json5
access_control: {
  "enabled": true,
  "default_permission": "deny",   // "deny" (secure default) or "allow"
  "rules": [ /* ... */ ],         // Optional: can be omitted
  "subjects": [ /* ... */ ],      // Optional: can be omitted
  "policies": [ /* ... */ ],      // Optional: can be omitted
}
```

All fields have defaults: `enabled` defaults to `false`, `default_permission` defaults to `"deny"`. The `rules`, `subjects`, and `policies` arrays are all **optional** (`Option<Vec<...>>`): they may be omitted entirely when not needed.

The three sections are independent:
- **rules** — what messages/flows/key-expressions are affected
- **subjects** — which connections are targeted (by interface, cert CN, username, link protocol, or ZID)
- **policies** — binds rules to subjects

---

## Rules

Each rule has a unique `id` and specifies:

| Field | Values | Notes |
|-------|--------|-------|
| `id` | string | Required. Must be unique within `rules` |
| `messages` | list of message types (see below) | Required, non-empty. What kinds of traffic |
| `flows` | `"egress"`, `"ingress"`, or both | **Optional** (`null` = both directions). Non-empty if present. |
| `permission` | `"allow"` or `"deny"` | What to do when matched |
| `key_exprs` | list of key expression strings | Required, non-empty. Zenoh key expression matching (supports `*`, `**`, etc.) |

**Message types:**

```
put                        — Publisher put operations
delete                     — Publisher delete operations
declare_subscriber         — Subscriber declarations
query                      — Get/query operations
reply                      — Queryable replies
declare_queryable          — Queryable declarations
liveliness_token           — Liveliness token publication
liveliness_query           — Liveliness get queries
declare_liveliness_subscriber — Liveliness subscriber declarations
```

**Example rules:**

```json5
"rules": [
  {
    "id": "allow-demo",
    "messages": ["put", "delete", "declare_subscriber", "query", "reply", "declare_queryable"],
    "flows": ["egress", "ingress"],
    "permission": "allow",
    "key_exprs": ["demo/**"]
  },
  {
    "id": "deny-admin",
    "messages": ["put", "delete", "declare_subscriber", "query", "reply"],
    "flows": ["ingress"],
    "permission": "deny",
    "key_exprs": ["@/**"]
  }
]
```

---

## Subjects

Subjects identify which connections a policy applies to. Each subject is a logical AND of its defined properties, with multiple values in a property treated as OR. An empty subject (no properties) is a wildcard that matches all connections.

### Subject Dimensions

| Dimension | Config Key | Auth Requirement | Notes |
|-----------|-----------|-----------------|-------|
| Subject ID | `id` | — | Required string. Used as reference key in `policies[].subjects`. Must be unique within `subjects`. |
| Network interface | `interfaces` | None | Optional. Non-empty list if present. e.g., `"lo0"`, `"en0"`, `"eth0"` |
| TLS cert common name | `cert_common_names` | mTLS (TLS + client cert) | Optional. Non-empty list if present. Matches the CN field of the peer's x.509 cert |
| Username | `usernames` | User/password authentication | Optional. Non-empty list if present. Matches the username presented at session open |
| Link protocol | `link_protocols` | None | Optional. Non-empty list if present. Valid values (kebab-case): `"tcp"`, `"udp"`, `"tls"`, `"quic"`, `"serial"`, `"unixpipe"`, `"unixsock-stream"`, `"vsock"`, `"ws"` |
| ZID | `zids` | **None — not production safe** | Optional. Non-empty list if present. See warning below |

**Internal filter logic for a subject with multiple dimensions:**

```
(interface="lo0" AND cert_common_name="example.zenoh.io" AND username="alice") OR
(interface="en0" AND cert_common_name="example.zenoh.io" AND username="alice")
```

That is: within a subject, cross-property is AND; within a property (multiple values), it is OR.

### ZID Warning

> **NOTE:** ZID is not backed by an authentication mechanism. It can only be trusted for ACL if it is dynamically added/removed by dedicated Zenoh mechanisms when transports are opened/closed. If managed manually in ACL config, it is useful for prototyping but **must not be used in production**.

### Example Subjects

```json5
"subjects": [
  {
    "id": "internal-clients",
    "interfaces": ["lo0", "eth0"],
    "cert_common_names": ["internal.zenoh.io"]
  },
  {
    "id": "external-tls-clients",
    "link_protocols": ["tls", "quic"],
    "cert_common_names": ["partner.example.com"]
  },
  {
    "id": "wildcard",
    // Empty subject — matches all connections
  }
]
```

---

## Policies

Policies bind rules to subjects. Each policy entry has the following fields:

| Field | Type | Notes |
|-------|------|-------|
| `id` | `Optional<String>` | Optional. Must be unique across policies if provided. |
| `rules` | `Vec<String>` | Required. List of rule `id` strings to apply. |
| `subjects` | `Vec<String>` | Required. List of subject `id` strings this policy applies to. |

```json5
"policies": [
  {
    "id": "internal-policy",   // optional, must be unique if provided
    "rules": ["allow-demo"],
    "subjects": ["internal-clients"]
  },
  {
    "id": "external-policy",
    "rules": ["deny-admin"],
    "subjects": ["external-tls-clients", "wildcard"]
  }
]
```

Multiple rules or subjects in a single policy are treated as OR: the policy applies if the connection matches any listed subject, and any matching rule's permission is applied.

---

## Default Permission

```json5
"default_permission": "deny"
```

- `"deny"` (recommended): Any message not explicitly allowed by a matching allow-rule is dropped. This is the secure default.
- `"allow"`: Any message not explicitly denied is forwarded. Use only in permissive environments or for incremental deny-list deployments.

If `access_control` is omitted or `"enabled": false`, no ACL filtering occurs.

---

## Examples

### Example 1: Allow only subscribers from a specific interface

Allow `demo/**` subscriptions only from the loopback interface; deny everything else.

```json5
access_control: {
  "enabled": true,
  "default_permission": "deny",
  "rules": [
    {
      "id": "allow-demo-sub",
      "messages": ["put", "delete", "declare_subscriber"],
      "flows": ["ingress", "egress"],
      "permission": "allow",
      "key_exprs": ["demo/**"]
    }
  ],
  "subjects": [
    {
      "id": "loopback",
      "interfaces": ["lo0"]
    }
  ],
  "policies": [
    {
      "rules": ["allow-demo-sub"],
      "subjects": ["loopback"]
    }
  ]
}
```

### Example 2: mTLS cert CN-based authorization

Allow full access for nodes presenting `robot.fleet.internal` as their TLS certificate CN. All other nodes are denied.

```json5
access_control: {
  "enabled": true,
  "default_permission": "deny",
  "rules": [
    {
      "id": "fleet-full-access",
      "messages": ["put", "delete", "declare_subscriber", "query", "reply", "declare_queryable"],
      "flows": ["ingress", "egress"],
      "permission": "allow",
      "key_exprs": ["**"]
    }
  ],
  "subjects": [
    {
      "id": "fleet-robots",
      "link_protocols": ["tls"],
      "cert_common_names": ["robot.fleet.internal"]
    }
  ],
  "policies": [
    {
      "rules": ["fleet-full-access"],
      "subjects": ["fleet-robots"]
    }
  ]
}
```

> Requires configuring TLS with `require_client_auth: true` so the router can see the peer's certificate CN.

### Example 3: Deny admin-space access for all external connections

A router that bridges internal and external networks. Internal (`lo0`) clients get full access; all other connections are blocked from the admin space (`@/**`).

```json5
access_control: {
  "enabled": true,
  "default_permission": "allow",
  "rules": [
    {
      "id": "deny-admin-external",
      "messages": ["put", "delete", "declare_subscriber", "query", "reply", "declare_queryable"],
      "flows": ["ingress"],
      "permission": "deny",
      "key_exprs": ["@/**"]
    }
  ],
  "subjects": [
    {
      "id": "all-external",
      // Empty = wildcard, matches all. In a deny rule this is appropriate.
    }
  ],
  "policies": [
    {
      "rules": ["deny-admin-external"],
      "subjects": ["all-external"]
    }
  ]
}
```

---

## Important Notes

### Rule Evaluation Order

Rules are not evaluated in list order. Instead:
1. If any matching rule has `permission: "deny"` → message is dropped.
2. If any matching rule has `permission: "allow"` → message is forwarded.
3. If no rule matches → `default_permission` is applied.

Effectively, **deny rules take precedence** over allow rules when both match.

### Performance Considerations

ACL adds per-message overhead for matching key expressions against rules. For high-throughput deployments:
- Keep the rule set small
- Use specific key expressions rather than broad wildcards where possible
- Set `default_permission: "deny"` and enumerate allowed key expressions (fewer checks on the hot path than enumerating denials in a permissive config)

### ZID Is Not Authentication

ZID-based subjects are convenient for development but ZIDs are self-reported and not cryptographically verified. For production access control, use `cert_common_names` (mTLS) or `usernames` (user/password auth), both of which are authenticated by the transport layer before ACL checks occur.

### ACL Scope

ACL is evaluated at the node where the config is applied. It is not enforced end-to-end across a router topology unless each router in the path has its own ACL config. For full end-to-end enforcement, configure ACL on every router and peer that handles the traffic.

## See Also

- [Encryption Guide](encryption-guide.md) — TLS/mTLS transport security that works alongside ACL; mTLS is required to use `cert_common_names` in ACL subjects
- [Node Types Guide](node-types-guide.md) — understanding router, peer, and client roles affects which nodes need ACL configured
- [Admin Space Guide](admin-space-guide.md) — the `@/**` key space is commonly restricted via ACL to prevent external access
