# Zenoh Security Documentation

## Table of Contents

1. [Security Overview](#1-security-overview)
2. [Threat Model](#2-threat-model)
3. [Transport Security (TLS and QUIC)](#3-transport-security-tls-and-quic)
4. [Mutual TLS (mTLS)](#4-mutual-tls-mtls)
5. [Authentication](#5-authentication)
6. [Access Control Lists (ACL)](#6-access-control-lists-acl)
7. [Example Secure Configurations](#7-example-secure-configurations)
8. [Security Hardening Checklist](#8-security-hardening-checklist)

---

## 1. Security Overview

Zenoh provides security controls at two distinct layers:

| Layer | Mechanism | Protects Against |
|---|---|---|
| Transport | TLS / QUIC | Eavesdropping, tampering, impersonation |
| Application | ACL rules | Unauthorized publish, subscribe, query |
| Authentication | mTLS / username+password | Unauthenticated connections |

These layers are independent and composable. You may use TLS without ACL, ACL without TLS, or both together for defense in depth.

Zenoh does **not** currently provide end-to-end payload encryption above the transport layer. If a message passes through a router, the router sees the plaintext payload. See [Section 2](#2-threat-model) for full threat model details.

---

## 2. Threat Model

### 2.1 What Zenoh Secures

- **Confidentiality of data in transit**: TLS and QUIC encrypt all bytes on the wire between two directly connected endpoints.
- **Integrity of data in transit**: TLS and QUIC provide cryptographic message authentication, preventing undetected tampering.
- **Peer authentication**: mTLS allows both sides of a connection to verify each other's identity using certificates before exchanging any application data.
- **Message-level access control**: The ACL engine evaluates every message (put, delete, subscribe declaration, query, reply, queryable declaration, liveliness) against configured rules before it is processed or forwarded.

### 2.2 What Zenoh Does NOT Secure

- **End-to-end encryption**: A zenoh router that bridges two TLS sessions decrypts traffic at the transport level. The router sees plaintext payloads. If the router is untrusted, it can read all data passing through it.
- **Key expression confidentiality in router metadata**: Even with TLS, routers exchange routing metadata (declarations of subscriptions, queryables, and liveliness tokens) that includes key expressions. An observer with access to the router's internal state or admin space can enumerate the key expressions in use.
- **Payload-level authorization**: ACL rules match on key expressions, not on payload content. A subject authorized to publish on `sensors/**` can publish any payload on that key expression.
- **Scouting traffic**: UDP multicast scouting messages (used for peer discovery) are not encrypted or authenticated. On untrusted networks, disable multicast scouting and use explicit endpoint configuration.
- **ZID authenticity**: A zenoh node's ZID (node identifier) is a self-asserted value. Unless verified through an out-of-band mechanism (such as mTLS certificate binding), ZID-based ACL subjects should not be relied upon for security enforcement in production.

### 2.3 Trusted Network Assumptions

Zenoh was designed with the assumption that the network fabric can range from fully trusted (a single-host loopback) to fully untrusted (the public internet). The appropriate security configuration depends on your deployment:

| Deployment | Recommended Controls |
|---|---|
| Single host, loopback only | No TLS required; consider ACL if multiple processes should be isolated |
| Private LAN, controlled access | ACL sufficient; TLS optional but recommended |
| Private LAN, mixed clients | TLS + ACL; mTLS for strong client identity |
| Across the internet or cloud | TLS or QUIC mandatory; mTLS strongly recommended; ACL required |
| Router bridges two untrusted segments | TLS on both sides; ACL to limit forwarding scope |

---

## 3. Transport Security (TLS and QUIC)

### 3.1 How Transport Security Works in Zenoh

Zenoh wraps its binary framing protocol inside a standard TLS 1.2/1.3 session (for `tls://` endpoints) or a QUIC session (for `quic://` endpoints). The security properties of both are equivalent from a configuration standpoint. The same certificate and key files are used for both transports; the configuration keys are under `transport.link.tls`.

When a connection is made:
1. The connecting side (client) verifies the listening side's (server's) certificate against the configured root CA.
2. Optionally, the server verifies the client's certificate (mTLS — see [Section 4](#4-mutual-tls-mtls)).
3. A session key is negotiated. All subsequent zenoh frames are encrypted.

### 3.2 Certificate Requirements

You need the following artifacts:

| Artifact | Purpose | Config Key |
|---|---|---|
| Root CA certificate (PEM) | Trust anchor for verifying the peer's certificate | `transport.link.tls.root_ca_certificate` |
| Server/listener private key (PEM) | Proves the listener's identity | `transport.link.tls.listen_private_key` |
| Server/listener certificate (PEM) | Presented to connecting clients | `transport.link.tls.listen_certificate` |
| Client/connector private key (PEM) | Required only for mTLS | `transport.link.tls.connect_private_key` |
| Client/connector certificate (PEM) | Required only for mTLS | `transport.link.tls.connect_certificate` |

Certificates must be in PEM format. Self-signed CA certificates are supported; zenoh does not require certificates to be issued by a public CA.

### 3.3 Generating a Self-Signed CA and Server Certificate

The following commands use OpenSSL to create a minimal PKI suitable for a private zenoh deployment.

```bash
# 1. Generate a root CA key and self-signed certificate (valid 10 years)
openssl req -x509 -newkey rsa:4096 -days 3650 -nodes \
  -keyout ca.key \
  -out ca.pem \
  -subj "/CN=zenoh-ca"

# 2. Generate a server (router/listener) key and certificate signing request
openssl req -newkey rsa:4096 -nodes \
  -keyout router.key \
  -out router.csr \
  -subj "/CN=router.zenoh.example.com"

# 3. Sign the server certificate with the CA (valid 1 year)
openssl x509 -req -days 365 \
  -in router.csr \
  -CA ca.pem \
  -CAkey ca.key \
  -CAcreateserial \
  -out router.pem

# 4. (For mTLS) Generate a client key and certificate
openssl req -newkey rsa:4096 -nodes \
  -keyout client.key \
  -out client.csr \
  -subj "/CN=sensor-node-1"

openssl x509 -req -days 365 \
  -in client.csr \
  -CA ca.pem \
  -CAkey ca.key \
  -CAcreateserial \
  -out client.pem
```

### 3.4 TLS Configuration Reference

All TLS parameters live under `transport.link.tls` in the JSON5 config file.

```json5
transport: {
  link: {
    tls: {
      // Path to the PEM file of the CA used to validate the remote peer's certificate.
      // On a router acting as a TLS listener, this CA is used to validate connecting
      // clients (only relevant when enable_mtls is true).
      // On a node acting as a TLS connector, this CA is used to validate the server.
      // If null on a router listener, the system/WebPKI trust store is used.
      root_ca_certificate: "/etc/zenoh/certs/ca.pem",

      // Private key for the TLS listener (the router's server-side identity).
      listen_private_key: "/etc/zenoh/certs/router.key",

      // Certificate presented by the TLS listener to connecting clients.
      listen_certificate: "/etc/zenoh/certs/router.pem",

      // Set to true to require and validate client certificates (mTLS).
      enable_mtls: false,

      // Private key used when this node connects to a TLS listener.
      // Required when enable_mtls is true on the remote listener.
      connect_private_key: null,

      // Certificate presented when this node connects to a TLS listener.
      // Required when enable_mtls is true on the remote listener.
      connect_certificate: null,

      // When true (default), the CN or SAN in the server certificate must
      // match the hostname used in the connect endpoint URI.
      // Set to false only for testing with IP addresses and no SAN.
      // WARNING: setting this to false in production removes server identity verification.
      verify_name_on_connect: true,

      // When true, zenoh will terminate TLS/QUIC links when the remote
      // certificate's expiry time is reached. Requires mTLS to disconnect clients.
      close_link_on_expiration: false,
    },
  },
},
```

### 3.5 Minimal TLS Example: Router Listener

```json5
// router-tls.json5
// A zenoh router that listens on TLS port 7447.
// Connecting clients must trust the same CA but do not need client certs (no mTLS).
{
  mode: "router",

  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },

  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/certs/ca.pem",
        listen_private_key:  "/etc/zenoh/certs/router.key",
        listen_certificate:  "/etc/zenoh/certs/router.pem",
        enable_mtls: false,
        verify_name_on_connect: true,
      },
    },
  },
}
```

### 3.6 Minimal TLS Example: Connecting Peer or Client

```json5
// client-tls.json5
// A zenoh client or peer that connects to the TLS router above.
{
  mode: "client",

  connect: {
    endpoints: ["tls/router.zenoh.example.com:7447"],
  },

  transport: {
    link: {
      tls: {
        // The client only needs the CA cert to verify the router's identity.
        root_ca_certificate: "/etc/zenoh/certs/ca.pem",
        verify_name_on_connect: true,
      },
    },
  },
}
```

### 3.7 QUIC Configuration

QUIC endpoints use the `quic/` scheme. All TLS configuration keys under `transport.link.tls` apply equally to QUIC connections. There is no separate QUIC-specific configuration block.

```json5
// quic-router.json5
{
  mode: "router",

  listen: {
    endpoints: ["quic/0.0.0.0:7448"],
  },

  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/certs/ca.pem",
        listen_private_key:  "/etc/zenoh/certs/router.key",
        listen_certificate:  "/etc/zenoh/certs/router.pem",
        enable_mtls: true,
        verify_name_on_connect: true,
      },
    },
  },
}
```

### 3.8 Hostname Verification

When `verify_name_on_connect` is `true` (the default), the CN or Subject Alternative Name (SAN) in the server certificate must match the hostname in the connect endpoint URI.

- If you connect to `tls/router.zenoh.example.com:7447`, the server certificate must have `CN=router.zenoh.example.com` or a SAN of `DNS:router.zenoh.example.com`.
- If you connect using an IP address (e.g., `tls/192.168.1.10:7447`), the certificate must have a SAN of `IP:192.168.1.10`.
- Setting `verify_name_on_connect: false` disables this check. **Do not use this in production.** It makes TLS vulnerable to certificate substitution attacks where any certificate signed by your CA can impersonate any server.

### 3.9 Certificate Expiry Handling

By default, zenoh does not disconnect active links when a certificate expires. The certificate is verified at connection establishment time only. To enforce periodic re-authentication:

```json5
transport: {
  link: {
    tls: {
      close_link_on_expiration: true,
    },
  },
},
```

When `close_link_on_expiration` is `true`, zenoh monitors the expiry time of the remote certificate chain and closes the link when that time is reached. Note: for a **listener** to disconnect a **client** on expiration, mTLS must be enabled (`enable_mtls: true`), because the listener only has a client certificate to inspect when mTLS is in use.

---

## 4. Mutual TLS (mTLS)

### 4.1 What mTLS Adds

Standard TLS only proves the server's identity to the client. Mutual TLS additionally requires the client to present a certificate, which the server verifies against its configured CA. This provides:

- Strong client authentication that does not rely on passwords or IP addresses.
- The ability to use `cert_common_names` in ACL subjects, binding access control decisions to the identity embedded in the certificate.
- Protection against rogue clients connecting with valid network access but no certificate.

### 4.2 Enabling mTLS on the Listener

Set `enable_mtls: true` on the router or peer that listens:

```json5
transport: {
  link: {
    tls: {
      root_ca_certificate: "/etc/zenoh/certs/ca.pem",
      listen_private_key:  "/etc/zenoh/certs/router.key",
      listen_certificate:  "/etc/zenoh/certs/router.pem",

      // Require client certificates signed by root_ca_certificate.
      enable_mtls: true,
    },
  },
},
```

### 4.3 Configuring the Connecting Side for mTLS

The connecting node must present its own certificate and private key:

```json5
transport: {
  link: {
    tls: {
      root_ca_certificate: "/etc/zenoh/certs/ca.pem",

      // Client certificate and key presented to the mTLS listener.
      connect_private_key: "/etc/zenoh/certs/client.key",
      connect_certificate:  "/etc/zenoh/certs/client.pem",

      verify_name_on_connect: true,
    },
  },
},
```

### 4.4 Using Certificate Common Names in ACL

Once mTLS is configured, the Common Name (CN) field from the client's certificate is available as a subject attribute in ACL rules. This allows per-client or per-role access control without managing separate usernames and passwords.

For example, if a client certificate was issued with `CN=sensor-node-1`, you can reference that in subjects:

```json5
access_control: {
  enabled: true,
  default_permission: "deny",
  subjects: [
    {
      id: "sensor-nodes",
      cert_common_names: ["sensor-node-1", "sensor-node-2"],
    },
  ],
  // ... rules and policies defined below
}
```

See [Section 6](#6-access-control-lists-acl) for full ACL documentation.

---

## 5. Authentication

### 5.1 Username and Password Authentication

Zenoh supports username/password authentication on unicast transports. This is configured under `transport.auth.usrpwd`.

**On the authenticating listener (router)**, provide a dictionary file that maps usernames to passwords:

```json5
transport: {
  auth: {
    usrpwd: {
      // Path to a file containing username:password pairs, one per line.
      // This acts as the credential store for verifying connecting clients.
      dictionary_file: "/etc/zenoh/users.txt",
    },
  },
},
```

The `users.txt` file format is one `username:password` entry per line:

```
alice:s3cr3tpassword
bob:another-password
sensor1:device-credential
```

**On the connecting client**, provide credentials directly in the config:

```json5
transport: {
  auth: {
    usrpwd: {
      user: "sensor1",
      password: "device-credential",
    },
  },
},
```

**Important security notes for username/password authentication:**

- Passwords are transmitted during the session establishment handshake. Always combine username/password authentication with TLS to protect credentials in transit. Using username/password on a plaintext TCP connection exposes credentials to any network observer.
- Usernames can be referenced in ACL `subjects` entries using the `usernames` field (see [Section 6.3](#63-subjects)).
- If both `user` and `dictionary_file` are set on the same node, the node can both present credentials and validate them from others.

### 5.2 Certificate-Based Authentication (via mTLS)

Certificate-based authentication is provided by the mTLS mechanism described in [Section 4](#4-mutual-tls-mtls). It is generally preferred over username/password for the following reasons:

- Private keys are never transmitted over the network.
- Certificate revocation and expiry provide lifecycle management.
- The CN from the certificate integrates directly with the ACL `cert_common_names` subject attribute.

### 5.3 Combining Authentication Methods

Username/password and certificate-based authentication can be used simultaneously. A subject in the ACL can require both a matching certificate CN and a matching username, providing layered identity verification:

```json5
subjects: [
  {
    id: "privileged-operator",
    cert_common_names: ["ops-client"],
    usernames: ["operator-alice"],
    // A connection must present a cert with CN=ops-client AND
    // authenticate with username=operator-alice to match this subject.
  },
],
```

---

## 6. Access Control Lists (ACL)

### 6.1 ACL Overview and Data Model

The zenoh ACL system evaluates every message against a set of rules before allowing it to be processed or forwarded. The evaluation model has five components:

```
Subjects  →  Policies  →  Rules  →  [messages × flows × key_exprs]  →  permission
```

| Component | Description |
|---|---|
| **Subject** | Identifies who is sending or receiving a message (by interface, cert CN, username, protocol, or ZID) |
| **Rule** | Specifies which message types on which key expressions are affected, and the permission (allow/deny) |
| **Policy** | Binds one or more rules to one or more subjects |
| **default_permission** | The permission applied to any message not matched by any policy |
| **Flow** | Whether the rule applies to messages coming in (ingress) or going out (egress) |

### 6.2 Enabling ACL and Setting Default Permission

```json5
access_control: {
  // Must be true for any ACL rules to take effect.
  enabled: true,

  // "deny" or "allow".
  // "deny": block everything not explicitly allowed (recommended for production).
  // "allow": permit everything not explicitly denied (useful for selective filtering).
  default_permission: "deny",

  rules:    [ /* ... */ ],
  subjects: [ /* ... */ ],
  policies: [ /* ... */ ],
},
```

**When `enabled` is `false`**, ACL is entirely bypassed regardless of the rules configured. All messages are allowed.

**`default_permission: "deny"`** is the safe default for production. Nothing passes unless a rule explicitly allows it. This prevents new key expressions or message types from silently becoming accessible when software is updated.

**`default_permission: "allow"`** is useful when you want to block only specific key expressions or message types while permitting everything else. This is the correct choice for ACL-only deployments on trusted networks where you want to prevent accidental data leakage to a specific key expression range.

### 6.3 Subjects

A subject identifies a class of remote peer. Each subject has a unique `id` and can match connections based on any combination of the following attributes:

| Attribute | Type | Description |
|---|---|---|
| `interfaces` | list of strings | Network interface names (e.g., `"eth0"`, `"wlan0"`) through which the connection arrives |
| `cert_common_names` | list of strings | CN field values from mTLS client certificates |
| `usernames` | list of strings | Usernames from username/password authentication |
| `link_protocols` | list of strings | Transport protocol of the link (`"tcp"`, `"tls"`, `"quic"`, `"udp"`, `"ws"`, etc.) |
| `zids` | list of strings | ZID of the remote zenoh node (see warning below) |

**Matching semantics within a subject:** When multiple attributes are specified, a connection must match ALL specified attributes (logical AND). When multiple values are listed within one attribute, the connection must match ANY of them (logical OR across values within the list, then AND across attribute types).

For example:
```json5
{
  "id": "example-subject",
  "interfaces": ["eth0", "eth1"],
  "cert_common_names": ["trusted-device"],
}
// Matches connections arriving on eth0 OR eth1
// AND presenting a certificate with CN=trusted-device.
// Internally: (interface="eth0" || interface="eth1") && CN="trusted-device"
```

**Empty subject (wildcard):** A subject with no attributes matches all connections:
```json5
{ "id": "everyone" }
```

**ZID warning:** ZIDs are self-asserted by the remote node. They are not backed by a cryptographic authentication mechanism in the ACL system. Use ZIDs in subjects only for prototyping or in combination with mTLS. Do not rely solely on `zids` for security enforcement in production.

### 6.4 Message Types (Actions)

ACL rules apply to the following message types, which correspond to zenoh API operations:

| Message type string | Triggered by |
|---|---|
| `"put"` | `session.put(key, payload)` |
| `"delete"` | `session.delete(key)` |
| `"declare_subscriber"` | `session.declare_subscriber(key)` |
| `"query"` | `session.get(key, ...)` |
| `"reply"` | A queryable responding to a query |
| `"declare_queryable"` | `session.declare_queryable(key)` |
| `"liveliness_token"` | `session.liveliness().declare_token(key)` |
| `"liveliness_query"` | `session.liveliness().get(key)` |
| `"declare_liveliness_subscriber"` | `session.liveliness().declare_subscriber(key)` |

### 6.5 Flows

Each rule can be scoped to one or both of:

| Flow | Description |
|---|---|
| `"ingress"` | Messages received by this node from a remote peer |
| `"egress"` | Messages sent by this node to a remote peer |

This distinction is important for routers. A router that receives a `put` on a key expression and forwards it to subscribers sees:
- An **ingress** `put` from the publisher side.
- An **egress** `put` toward each subscriber side.

Restricting the egress flow prevents forwarding to a class of subscribers. Restricting the ingress flow prevents accepting publications from a class of publishers.

### 6.6 Rules

A rule specifies:
- A unique `id`.
- A list of `messages` (message types the rule applies to).
- A list of `flows` (ingress and/or egress).
- A `permission` (`"allow"` or `"deny"`).
- A list of `key_exprs` (zenoh key expressions that the rule matches).

```json5
rules: [
  {
    "id": "allow-sensor-data-put",
    "messages": ["put", "delete"],
    "flows": ["ingress"],
    "permission": "allow",
    "key_exprs": ["sensors/**"],
  },
  {
    "id": "allow-sensor-subscribe",
    "messages": ["declare_subscriber"],
    "flows": ["egress"],
    "permission": "allow",
    "key_exprs": ["sensors/**"],
  },
],
```

Key expressions in rules follow zenoh's key expression syntax, including wildcards `*` (single level) and `**` (multi-level).

### 6.7 Policies

Policies bind rules to subjects. Each policy entry lists:
- One or more `rules` (by their IDs).
- One or more `subjects` (by their IDs).

The policy means: "for connections matching any of these subjects, apply all of these rules."

```json5
policies: [
  {
    "id": "sensor-policy",
    "rules":    ["allow-sensor-data-put"],
    "subjects": ["sensor-nodes"],
  },
],
```

### 6.8 ACL Evaluation Order

For a given message on a given connection:
1. Find all policies where the connection matches one of the listed subjects.
2. From those policies, collect all associated rules.
3. Find rules that match the message type, flow, and key expression.
4. If any matching rule has `permission: "deny"`, the message is **denied**.
5. If any matching rule has `permission: "allow"` (and none deny), the message is **allowed**.
6. If no rules match, apply `default_permission`.

Explicit deny takes precedence over explicit allow from different policies. This means you can use a wildcard-allow rule for broad access and layer specific deny rules for sensitive key expressions.

---

## 7. Example Secure Configurations

### 7.1 Minimal TLS (Server-Side Only, No mTLS, No ACL)

This is the simplest configuration that encrypts traffic. Suitable for trusted clients on an untrusted network where client identity verification is not required.

**Router config (`router-minimal-tls.json5`):**

```json5
{
  mode: "router",

  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },

  // Disable UDP multicast scouting when operating over untrusted networks.
  scouting: {
    multicast: {
      enabled: false,
    },
  },

  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/certs/ca.pem",
        listen_private_key:  "/etc/zenoh/certs/router.key",
        listen_certificate:  "/etc/zenoh/certs/router.pem",
        enable_mtls: false,
        verify_name_on_connect: true,
        close_link_on_expiration: true,
      },
    },
  },
}
```

**Client config (`client-minimal-tls.json5`):**

```json5
{
  mode: "client",

  connect: {
    endpoints: ["tls/router.zenoh.example.com:7447"],
  },

  scouting: {
    multicast: {
      enabled: false,
    },
  },

  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/certs/ca.pem",
        verify_name_on_connect: true,
      },
    },
  },
}
```

---

### 7.2 Full mTLS with ACL (Recommended for Production)

This configuration:
- Encrypts all traffic with TLS.
- Requires client certificates (mTLS) so each client has a verified identity.
- Denies everything by default.
- Allows sensor nodes (identified by cert CN) to publish sensor data.
- Allows dashboard nodes (identified by cert CN) to subscribe to sensor data and issue queries.

**Router config (`router-mtls-acl.json5`):**

```json5
{
  mode: "router",

  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },

  scouting: {
    multicast: {
      enabled: false,
    },
  },

  transport: {
    link: {
      tls: {
        root_ca_certificate: "/etc/zenoh/certs/ca.pem",
        listen_private_key:  "/etc/zenoh/certs/router.key",
        listen_certificate:  "/etc/zenoh/certs/router.pem",

        // Require all clients to present a certificate signed by ca.pem.
        enable_mtls: true,

        verify_name_on_connect: true,
        close_link_on_expiration: true,
      },
    },
  },

  access_control: {
    enabled: true,
    // Default deny: nothing is permitted unless explicitly allowed.
    default_permission: "deny",

    subjects: [
      {
        // Sensor nodes identified by their certificate CN.
        // These nodes publish readings, they should not be able to subscribe or query.
        "id": "sensor-nodes",
        "cert_common_names": ["sensor-node-1", "sensor-node-2", "sensor-node-3"],
      },
      {
        // Dashboard nodes that consume sensor data.
        "id": "dashboard-nodes",
        "cert_common_names": ["dashboard-primary", "dashboard-backup"],
      },
      {
        // Administrative clients connecting on the loopback interface.
        "id": "local-admin",
        "interfaces": ["lo", "lo0"],
      },
    ],

    rules: [
      {
        // Sensor nodes may publish (put/delete) to the sensors key space.
        "id": "sensor-publish",
        "messages": ["put", "delete"],
        "flows": ["ingress"],
        "permission": "allow",
        "key_exprs": ["sensors/**"],
      },
      {
        // Dashboard nodes may subscribe to sensor data.
        "id": "dashboard-subscribe",
        "messages": ["declare_subscriber"],
        "flows": ["egress"],
        "permission": "allow",
        "key_exprs": ["sensors/**"],
      },
      {
        // Dashboard nodes may query historical or aggregated sensor data.
        "id": "dashboard-query",
        "messages": ["query"],
        "flows": ["ingress"],
        "permission": "allow",
        "key_exprs": ["sensors/**", "analytics/**"],
      },
      {
        // Allow queryable declarations so storage/analytics services can register.
        "id": "declare-queryable-analytics",
        "messages": ["declare_queryable"],
        "flows": ["ingress"],
        "permission": "allow",
        "key_exprs": ["analytics/**"],
      },
      {
        // Replies flow back to the querying dashboard.
        "id": "allow-replies",
        "messages": ["reply"],
        "flows": ["egress"],
        "permission": "allow",
        "key_exprs": ["sensors/**", "analytics/**"],
      },
      {
        // Local admin has full access to everything.
        "id": "admin-full-access",
        "messages": [
          "put", "delete", "declare_subscriber",
          "query", "reply", "declare_queryable",
          "liveliness_token", "liveliness_query", "declare_liveliness_subscriber"
        ],
        "flows": ["ingress", "egress"],
        "permission": "allow",
        "key_exprs": ["**"],
      },
    ],

    policies: [
      {
        "id": "sensor-policy",
        "rules":    ["sensor-publish"],
        "subjects": ["sensor-nodes"],
      },
      {
        "id": "dashboard-policy",
        "rules":    ["dashboard-subscribe", "dashboard-query", "allow-replies"],
        "subjects": ["dashboard-nodes"],
      },
      {
        "id": "queryable-policy",
        "rules":    ["declare-queryable-analytics"],
        "subjects": ["dashboard-nodes"],
      },
      {
        "id": "admin-policy",
        "rules":    ["admin-full-access"],
        "subjects": ["local-admin"],
      },
    ],
  },
}
```

**Sensor node client config (`sensor-client-mtls.json5`):**

```json5
{
  mode: "client",

  connect: {
    endpoints: ["tls/router.zenoh.example.com:7447"],
  },

  scouting: {
    multicast: {
      enabled: false,
    },
  },