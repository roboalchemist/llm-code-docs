# Zenoh Security Documentation

## Table of Contents

1. [Security Overview](#security-overview)
2. [Transport Security (TLS/QUIC)](#transport-security)
3. [Mutual TLS (mTLS)](#mutual-tls)
4. [Authentication](#authentication)
5. [Access Control Lists (ACL)](#access-control-lists)
6. [Threat Model](#threat-model)
7. [Example Configurations](#example-configurations)

---

## Security Overview

Zenoh provides security through two complementary layers:

| Layer | Mechanism | Purpose |
|---|---|---|
| Transport | TLS / QUIC | Encrypts data in transit, authenticates endpoints |
| Application | ACL rules | Controls which subjects can perform which operations on which key expressions |

These layers are independent and composable. TLS secures the wire; ACL enforces policy on messages. Both can be used together or independently depending on your threat model.

---

## Transport Security

### How TLS Works in Zenoh

Zenoh supports TLS over TCP (`tls://`) and QUIC (`quic://`). Both use the same underlying certificate infrastructure. QUIC inherits TLS 1.3 security properties by design.

When a zenoh node connects to a TLS endpoint:

1. The connecting side verifies the server's certificate against its configured root CA.
2. Optionally (with mTLS enabled), the server also verifies the client's certificate.
3. An encrypted channel is established before any zenoh protocol messages are exchanged.

### Certificate Requirements

You need the following artifacts:

| Artifact | Description | Used By |
|---|---|---|
| Root CA certificate | Signs server and client certificates | Both sides for verification |
| Server private key | Private key for the listening node | Listener |
| Server certificate | Public certificate signed by the CA | Listener |
| Client private key | Private key for the connecting node | Connector (mTLS only) |
| Client certificate | Public certificate signed by the CA | Connector (mTLS only) |

### Generating Certificates (Example with OpenSSL)

```bash
# 1. Generate a root CA key and self-signed certificate
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 3650 -key ca.key -out ca.pem \
  -subj "/CN=Zenoh CA/O=My Organization"

# 2. Generate the server (listener) key and certificate
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr \
  -subj "/CN=zenoh-router.example.com/O=My Organization"
openssl x509 -req -days 365 -in server.csr \
  -CA ca.pem -CAkey ca.key -CAcreateserial \
  -out server.pem

# 3. Generate the client (connector) key and certificate (for mTLS)
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr \
  -subj "/CN=zenoh-client.example.com/O=My Organization"
openssl x509 -req -days 365 -in client.csr \
  -CA ca.pem -CAkey ca.key -CAcreateserial \
  -out client.pem
```

> **Security note:** Protect private key files with filesystem permissions (`chmod 600`). Never share private keys across nodes. Use separate certificates per node for proper revocation granularity.

### TLS Configuration Reference

All TLS parameters live under `transport.link.tls`:

```json5
transport: {
  link: {
    tls: {
      // Path to the root CA certificate (PEM format).
      // Used to verify remote certificates.
      // On routers acting as listeners, if omitted, the system's WebPKI
      // (public internet CA) roots are used instead.
      root_ca_certificate: "/path/to/ca.pem",

      // Listener (server) side credentials.
      // Required on nodes that listen on tls:// or quic:// endpoints.
      listen_private_key: "/path/to/server.key",
      listen_certificate: "/path/to/server.pem",

      // Connector (client) side credentials.
      // Required when mTLS is enabled on the remote listener.
      connect_private_key: "/path/to/client.key",
      connect_certificate: "/path/to/client.pem",

      // Enable mutual TLS: the listener will require and verify
      // a certificate from connecting clients.
      enable_mtls: false,

      // When true (default), the CN/SAN in the server's certificate
      // must match the hostname in the connect endpoint URL.
      // Set to false only in controlled test environments.
      verify_name_on_connect: true,

      // When true, zenoh will close the link when the remote
      // certificate's expiration time is reached.
      // Requires mTLS to work for listener-to-client enforcement.
      close_link_on_expiration: false,

      // Optional: override TCP socket buffer sizes for TLS links (bytes).
      // so_rcvbuf: 65536,
      // so_sndbuf: 65536,
    },
  },
},
```

### Enabling TLS Endpoints

Configure listen and connect endpoints using the `tls://` scheme:

```json5
// On the router/listener:
listen: {
  endpoints: ["tls/0.0.0.0:7447"],
},

// On the client/connector:
connect: {
  endpoints: ["tls/router.example.com:7447"],
},
```

For QUIC, replace `tls` with `quic`:

```json5
listen: {
  endpoints: ["quic/0.0.0.0:7447"],
},
connect: {
  endpoints: ["quic/router.example.com:7447"],
},
```

> **Note:** QUIC uses the same `transport.link.tls` configuration block. There is no separate QUIC-specific certificate configuration.

### Restricting to Secure Transports Only

To ensure zenoh never falls back to plaintext TCP, restrict the allowed link protocols:

```json5
transport: {
  link: {
    protocols: ["tls", "quic"],
  },
},
```

This causes zenoh to reject any connection attempt or listen endpoint using an unencrypted protocol.

---

## Mutual TLS

Mutual TLS (mTLS) requires both sides to present and verify certificates, enabling cryptographic client identity that can be used downstream by the ACL system (via `cert_common_names`).

### Enabling mTLS

Set `enable_mtls: true` on the **listener** side. The connecting node must provide `connect_private_key` and `connect_certificate`.

```json5
// Router (listener) config
transport: {
  link: {
    tls: {
      root_ca_certificate: "/etc/zenoh/ca.pem",
      listen_private_key:  "/etc/zenoh/router.key",
      listen_certificate:  "/etc/zenoh/router.pem",
      enable_mtls: true,
    },
  },
},

// Client (connector) config
transport: {
  link: {
    tls: {
      root_ca_certificate:  "/etc/zenoh/ca.pem",
      connect_private_key:  "/etc/zenoh/client.key",
      connect_certificate:  "/etc/zenoh/client.pem",
    },
  },
},
```

When mTLS is active, the CN (Common Name) of the client's certificate is available to the ACL engine as `cert_common_names`. This allows per-client access control without any additional authentication mechanism.

### Certificate Expiration Enforcement

When `close_link_on_expiration: true` is set alongside mTLS, zenoh will automatically disconnect clients whose certificates have expired:

```json5
transport: {
  link: {
    tls: {
      enable_mtls: true,
      close_link_on_expiration: true,
      // ...
    },
  },
},
```

---

## Authentication

Zenoh supports two authentication mechanisms that can be used independently or together.

### Username/Password Authentication

Username and password authentication is configured under `transport.auth.usrpwd`.

**On the authenticating side (router/listener):**

Provide a dictionary file mapping usernames to passwords:

```json5
transport: {
  auth: {
    usrpwd: {
      // Path to a file containing username:password pairs (one per line)
      dictionary_file: "/etc/zenoh/users.txt",
    },
  },
},
```

Example `users.txt`:
```
sensor-node-1:s3cr3tP@ssw0rd
dashboard-reader:readonlypass
admin-writer:adminP@ss
```

**On the connecting side (client):**

```json5
transport: {
  auth: {
    usrpwd: {
      user: "sensor-node-1",
      password: "s3cr3tP@ssw0rd",
    },
  },
},
```

> **Security note:** Username/password credentials are exchanged during the session open handshake. Always combine username/password authentication with TLS to protect these credentials in transit.

### Certificate-Based Authentication (via mTLS)

When mTLS is enabled, the client's certificate acts as its credential. No username or password is needed. The certificate's Common Name (CN) is extracted and made available for ACL matching.

This is the preferred authentication method when all nodes are managed and can receive certificates from a central CA.

### Combining Both Methods

Both mechanisms can be active simultaneously. A client must satisfy both to connect:

```json5
transport: {
  auth: {
    usrpwd: {
      dictionary_file: "/etc/zenoh/users.txt",
    },
  },
  link: {
    tls: {
      enable_mtls: true,
      // ... certificate paths ...
    },
  },
},
```

---

## Access Control Lists

The ACL system controls which entities can perform which operations on which key expressions. It operates independently of transport security and applies to the zenoh message layer.

### Core Concepts

```
Subject → Policy → Rule → (Messages + Key Expressions + Flow + Permission)
```

| Concept | Description |
|---|---|
| **Subject** | Who is sending or receiving (identified by interface, cert CN, username, etc.) |
| **Rule** | What operations on what key expressions are affected, and whether they are allowed or denied |
| **Policy** | Binds one or more subjects to one or more rules |
| **Default permission** | What happens when no rule matches: `"allow"` or `"deny"` |

### Enabling ACL

```json5
access_control: {
  enabled: true,
  default_permission: "deny",  // Secure default: deny unless explicitly allowed
  rules: [...],
  subjects: [...],
  policies: [...],
},
```

> **Best practice:** Always set `default_permission: "deny"` in production. This implements a deny-by-default posture where only explicitly permitted operations are allowed.

### Subjects

A subject identifies a connecting entity. Multiple identifying properties within one subject entry are ANDed together; multiple entries in a subject's lists are ORed.

```json5
subjects: [
  {
    "id": "trusted-local",
    // Match connections arriving on these network interfaces
    "interfaces": ["lo0", "eth0"],
  },
  {
    "id": "sensor-devices",
    // Match by TLS client certificate Common Name (requires mTLS)
    "cert_common_names": ["sensor.example.com"],
  },
  {
    "id": "dashboard-users",
    // Match by username (requires username/password auth)
    "usernames": ["dashboard-reader", "dashboard-admin"],
  },
  {
    "id": "combined-identity",
    // All conditions must match simultaneously (AND logic within the entry)
    // Multiple values within a list are OR'd.
    // So this means:
    //   (interface=eth0 AND cert_cn=client.example.com) OR
    //   (interface=wlan0 AND cert_cn=client.example.com)
    "interfaces": ["eth0", "wlan0"],
    "cert_common_names": ["client.example.com"],
  },
  {
    "id": "wildcard-subject",
    // Empty subject matches ALL connections (wildcard)
  },
  {
    "id": "protocol-filtered",
    // Match by link protocol
    "link_protocols": ["tls", "quic"],
  },
],
```

> **Warning on ZID-based subjects:** The `zids` field in subjects is **not backed by an authentication mechanism**. ZIDs can be spoofed. Use ZID-based subjects only for development and prototyping, never in production security policies.

### Messages and Actions

The `messages` field in a rule specifies which zenoh operation types the rule applies to:

| Message Type | Description |
|---|---|
| `"put"` | Publishing data (write) |
| `"delete"` | Deleting data (write) |
| `"declare_subscriber"` | Subscribing to key expressions (read intent) |
| `"query"` | Issuing get/query requests (read) |
| `"reply"` | Responding to queries (write) |
| `"declare_queryable"` | Declaring a queryable handler |
| `"liveliness_token"` | Publishing a liveliness token |
| `"liveliness_query"` | Querying liveliness tokens |
| `"declare_liveliness_subscriber"` | Subscribing to liveliness events |

### Flows

Rules apply to one or both data flows:

| Flow | Description |
|---|---|
| `"ingress"` | Messages **arriving** at this node from the network |
| `"egress"` | Messages **leaving** this node to the network |

Controlling both flows gives fine-grained directional control. For example, you can allow a node to subscribe (`declare_subscriber` egress) but block it from receiving certain data (`put` ingress).

### Rules

A rule specifies a permission for a combination of messages, flows, and key expressions:

```json5
rules: [
  {
    "id": "allow-sensor-writes",
    "messages": ["put", "delete"],
    "flows": ["egress"],         // Only applies to outgoing publishes
    "permission": "allow",
    "key_exprs": ["sensors/**"],
  },
  {
    "id": "allow-read-dashboard",
    "messages": ["query", "declare_subscriber"],
    "flows": ["egress", "ingress"],
    "permission": "allow",
    "key_exprs": ["sensors/**", "status/**"],
  },
  {
    "id": "deny-admin-space",
    "messages": ["put", "delete", "query"],
    "flows": ["egress", "ingress"],
    "permission": "deny",
    "key_exprs": ["@/**"],      // Block access to admin space key expressions
  },
],
```

### Policies

Policies bind subjects to rules:

```json5
policies: [
  {
    "id": "sensor-policy",
    "subjects": ["sensor-devices"],
    "rules": ["allow-sensor-writes"],
  },
  {
    "id": "dashboard-policy",
    "subjects": ["dashboard-users"],
    "rules": ["allow-read-dashboard"],
  },
],
```

### Rule Evaluation Order

When a message arrives:

1. Zenoh identifies the subject (interface, cert CN, username).
2. It finds all policies that reference a matching subject.
3. It evaluates all rules in those policies against the message type, key expression, and flow.
4. If any matching rule **denies** the operation, it is denied.
5. If any matching rule **allows** the operation (and none deny), it is allowed.
6. If no rule matches, the `default_permission` applies.

> **Note:** An explicit `"deny"` rule takes precedence over an explicit `"allow"` rule when both match.

---

## Threat Model

### What Zenoh Secures

| Threat | Mitigation |
|---|---|
| Eavesdropping on wire | TLS/QUIC encryption |
| Man-in-the-middle attacks | TLS certificate verification, `verify_name_on_connect: true` |
| Unauthorized clients connecting | mTLS client certificates, username/password |
| Unauthorized publish/subscribe | ACL rules on message types and key expressions |
| Expired credentials | `close_link_on_expiration: true` with mTLS |
| Overly permissive defaults | `default_permission: "deny"` |

### What Zenoh Does NOT Secure

| Limitation | Explanation |
|---|---|
| **Key expression confidentiality in routing metadata** | Routers must inspect key expressions to route messages. Even with TLS, key expressions are visible to intermediate routers within the zenoh network. |
| **Payload confidentiality from routers** | Routers can see message payloads in memory. End-to-end payload encryption must be implemented at the application layer if routers should not see data. |
| **ZID authenticity** | Zenoh IDs (ZIDs) are not cryptographically authenticated. Do not use `zids` in ACL subjects for production security decisions. |
| **Multicast transport security** | Zenoh multicast (UDP) does not support TLS. Multicast scouting and transport should only be used on trusted network segments. |
| **Plugin security** | Plugins (REST, storage manager, etc.) have their own security considerations not covered by zenoh core ACL. |
| **Admin space protection** | The admin space (`@/<zid>/...`) is not automatically protected. Restrict it explicitly with ACL rules. |

### Trusted Network Assumptions

When operating **without TLS** (plaintext TCP or UDP):

- All nodes on the network segment are assumed trusted.
- Any node can read all traffic.
- ACL rules still apply at the message level but cannot prevent eavesdropping.
- Suitable for: isolated lab networks, localhost development, air-gapped systems with physical access control.

When operating **with TLS but without mTLS**:

- Traffic is encrypted and the server is authenticated.
- Any client with network access can connect (no client authentication).
- ACL subjects based on `cert_common_names` will not be meaningful.
- Suitable for: protecting data in transit on shared networks where client identity is established by other means.

When operating **with mTLS**:

- Both server and client are cryptographically authenticated.
- `cert_common_names` in ACL subjects are trustworthy.
- Suitable for: production deployments requiring strong endpoint identity.

---

## Example Configurations

### Example 1: Minimal TLS (Server Authentication Only)

Protects data in transit. Any client can connect but traffic is encrypted.

**Router config** (`router.json5`):
```json5
{
  mode: "router",
  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },
  transport: {
    link: {
      protocols: ["tls"],
      tls: {
        root_ca_certificate: "/etc/zenoh/ca.pem",
        listen_private_key:  "/etc/zenoh/router.key",
        listen_certificate:  "/etc/zenoh/router.pem",
        enable_mtls: false,
        verify_name_on_connect: true,
      },
    },
  },
}
```

**Client config** (`client.json5`):
```json5
{
  mode: "client",
  connect: {
    endpoints: ["tls/router.example.com:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/ca.pem",
        verify_name_on_connect: true,
      },
    },
  },
}
```

---

### Example 2: Full mTLS with ACL

Enforces client certificate authentication and applies per-client access control. This is the recommended production configuration.

**Scenario:** Sensor nodes may only publish to `sensors/**`. Dashboard clients may only subscribe and query `sensors/**`.

**Router config** (`router-mtls-acl.json5`):
```json5
{
  mode: "router",
  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },
  transport: {
    link: {
      protocols: ["tls"],
      tls: {
        root_ca_certificate: "/etc/zenoh/ca.pem",
        listen_private_key:  "/etc/zenoh/router.key",
        listen_certificate:  "/etc/zenoh/router.pem",
        enable_mtls: true,
        verify_name_on_connect: true,
        close_link_on_expiration: true,
      },
    },
  },
  access_control: {
    enabled: true,
    default_permission: "deny",
    rules: [
      {
        id: "sensor-publish",
        messages: ["put", "delete"],
        flows: ["ingress"],      // Incoming publishes arriving at the router
        permission: "allow",
        key_exprs: ["sensors/**"],
      },
      {
        id: "sensor-declare",
        messages: ["declare_subscriber"],
        flows: ["egress"],       // Router sending subscribe declarations outward
        permission: "allow",
        key_exprs: ["sensors/**"],
      },
      {
        id: "dashboard-subscribe",
        messages: ["declare_subscriber", "query"],
        flows: ["ingress"],      // Client sending subscribe/query to router
        permission: "allow",
        key_exprs: ["sensors/**"],
      },
      {
        id: "dashboard-receive",
        messages: ["put", "reply"],
        flows: ["egress"],       // Router sending data out to dashboard
        permission: "allow",
        key_exprs: ["sensors/**"],
      },
    ],
    subjects: [
      {
        id: "sensors",
        // Matches clients whose TLS cert CN starts with "sensor"
        // Use exact CNs in production
        cert_common_names: [
          "sensor-node-1.example.com",
          "sensor-node-2.example.com",
        ],
      },
      {
        id: "dashboards",
        cert_common_names: [
          "dashboard.example.com",
        ],
      },
    ],
    policies: [
      {
        id: "sensor-policy",
        subjects: ["sensors"],
        rules: ["sensor-publish", "sensor-declare"],
      },
      {
        id: "dashboard-policy",
        subjects: ["dashboards"],
        rules: ["dashboard-subscribe", "dashboard-receive"],
      },
    ],
  },
}
```

**Sensor node config** (`sensor.json5`):
```json5
{
  mode: "client",
  connect: {
    endpoints: ["tls/router.example.com:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate:  "/etc/zenoh/ca.pem",
        connect_private_key:  "/etc/zenoh/sensor-node-1.key",
        connect_certificate:  "/etc/zenoh/sensor-node-1.pem",
        verify_name_on_connect: true,
      },
    },
  },
}
```

**Dashboard client config** (`dashboard.json5`):
```json5
{
  mode: "client",
  connect: {
    endpoints: ["tls/router.example.com:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate:  "/etc/zenoh/ca.pem",
        connect_private_key:  "/etc/zenoh/dashboard.key",
        connect_certificate:  "/etc/zenoh/dashboard.pem",
        verify_name_on_connect: true,
      },
    },
  },
}
```

---

### Example 3: ACL-Only (Trusted Network, No TLS)

For isolated networks where encryption is not required but logical access separation is still desired.

**Scenario:** Separate production and test namespaces. Nodes on `eth0` (production) cannot access `test/**`. Nodes on `eth1` (test) cannot access `production/**`.

```json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"],
  },
  access_control: {
    enabled: true,
    default_permission: "deny",
    rules: [
      {
        id: "allow-production",
        messages: [
          "put", "delete", "declare_subscriber",
          "query", "reply", "declare_queryable",
        ],
        flows: ["ingress", "egress"],
        permission: "allow",
        key_exprs: ["production/**"],
      },
      {
        id: "allow-test",
        messages: [
          "put", "delete", "declare_subscriber",
          "query", "reply", "declare_queryable",
        ],
        flows: ["ingress", "egress"],
        permission: "allow",
        key_exprs: ["test/**"],
      },
    ],
    subjects: [
      {
        id: "production-network",
        interfaces: ["eth0"],
      },
      {
        id: "test-network",
        interfaces: ["eth1"],
      },
    ],
    policies: [
      {
        id: "production-policy",
        subjects: ["production-network"],
        rules: ["allow-production"],
      },
      {
        id: "test-policy",
        subjects: ["test-network"],
        rules: ["allow-test"],
      },
    ],
  },
}
```

---

### Example 4: Read-Only vs Read-Write Clients with Username/Password

Differentiate clients by credential, without mTLS.

```json5
{
  mode: "router",
  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/ca.pem",
        listen_private_key:  "/etc/zenoh/router.key",
        listen_certificate:  "/etc/zenoh/router.pem",
        enable_mtls: false,
      },
    },
    auth: {
      usrpwd: {
        dictionary_file: "/etc/zenoh/users.txt",
      },
    },
  },
  access_control: {
    enabled: true,
    default_permission: "deny",
    rules: [
      {
        id: "read-only",
        messages: ["declare_subscriber", "query"],
        flows: ["ingress", "egress"],
        permission: "allow",
        key_exprs: ["data/**"],
      },
      {
        id: "read-write",
        messages: [
          "put", "delete", "declare_subscriber",
          "query", "reply", "declare_queryable",
        ],
        flows: ["ingress", "egress"],
        permission: "allow",
        key_exprs: ["data/**"],
      },
    ],
    subjects: [
      {
        id: "readers",
        usernames: ["reader-1", "reader-2", "dashboard"],
      },
      {
        id: "writers",
        usernames: ["sensor-writer", "control-node"],
      },
    ],
    policies: [
      {
        id: "reader-policy",
        subjects: ["readers"],
        rules: ["read-only"],
      },
      {
        id: "writer-policy",
        subjects: ["writers"],
        rules: ["read-write"],
      },
    ],
  },
}
```

`/etc/zenoh/users.txt`:
```
reader-1:readerpass1
reader-2:readerpass2
dashboard:dashpass
sensor-writer:writerpass1
control-node:controlpass
```

---

## Security Hardening Checklist

Use this checklist when deploying zenoh in a production environment:

- [ ] Enable TLS (`tls://` or `quic://` endpoints) on all inter-node links
- [ ] Set `verify_name_on_connect: true` (this is the default; do not override it)
- [ ] Enable mTLS (`enable_mtls: true`) for cryptographic client identity
- [ ] Set `close_link_on_expiration: true` to enforce certificate lifetimes
- [ ] Restrict link protocols to encrypted transports only (`protocols: ["tls", "quic"]`)
- [ ] Enable ACL (`access_control.enabled: true`)
- [ ] Set `default_permission: "deny"`
- [ ] Define explicit allow rules for every expected message type and key expression
- [ ] Disable multicast scouting (`scouting.multicast.enabled: false`) if not needed, or restrict it to trusted interfaces
- [ ] Disable the admin space (`adminspace.enabled: false`) or restrict it with ACL rules covering `@/**`
- [ ] Protect private key files with filesystem permissions (`chmod 600`)
- [ ] Rotate certificates before expiration
- [ ] Never use `zids` in ACL subjects for production security decisions
- [ ] Implement application-layer payload encryption if intermediate routers must not see payload content
---

## See Also
- [configuration.md](configuration.md) — Full configuration reference including TLS and ACL fields
- [deployment.md](deployment.md) — Deploying secured routers and peer networks
- [transports.md](transports.md) — TLS and QUIC transport security options
