# Zenoh TLS/Encryption & Access Control Guide

## Table of Contents

- [Overview](#overview)
- [Part 1: TLS Setup](#part-1-tls-setup)
  - [Configuration Location](#configuration-location)
  - [TLS Config Field Reference](#tls-config-field-reference)
  - [Self-Signed Certificates](#self-signed-certificates)
  - [CA-Signed Certificates (Existing CA)](#ca-signed-certificates-existing-ca)
  - [TLS Server Configuration (Router/Peer as Listener)](#tls-server-configuration-routerpeer-as-listener)
  - [TLS Client Configuration (Peer as Connector)](#tls-client-configuration-peer-as-connector)
  - [mTLS (Mutual TLS)](#mtls-mutual-tls)
  - [QUIC Security](#quic-security)
  - [Certificate Rotation](#certificate-rotation)
- [Part 2: User/Password Authentication](#part-2-userpassword-authentication)
  - [Configuration](#configuration)
- [Part 3: ACL (Access Control Lists)](#part-3-acl-access-control-lists)
  - [Configuration Structure](#configuration-structure)
  - [Rules](#rules)
  - [Subjects](#subjects)
  - [Subject Type Details](#subject-type-details)
  - [Policies](#policies)
  - [Rule Priority](#rule-priority)
  - [Key Expression Matching in ACL](#key-expression-matching-in-acl)
  - [ACL Working Examples](#acl-working-examples)
- [Part 4: Combining TLS and ACL in Python](#part-4-combining-tls-and-acl-in-python)
- [Part 5: ACL Performance Tips](#part-5-acl-performance-tips)
- [Quick Reference](#quick-reference)
  - [TLS Config Snippet (Server with mTLS)](#tls-config-snippet-server-with-mtls)
  - [TLS Config Snippet (Client with mTLS)](#tls-config-snippet-client-with-mtls)
  - [Minimal ACL (Deny All Except Loopback)](#minimal-acl-deny-all-except-loopback)
  - [Certificate Generation One-Liner (Dev/Test Only)](#certificate-generation-one-liner-devtest-only)

## Overview

Zenoh provides two orthogonal security mechanisms:

1. **TLS/mTLS** — encrypts transport-layer connections and authenticates peers via certificates
2. **ACL (Access Control Lists)** — filters which messages, key-expressions, and operations are permitted at the router/peer level

These can be used independently or combined: TLS for wire encryption and peer identity, ACL for fine-grained data-plane authorization.

**Supported transports:**
- `tls/...` — TLS over TCP (explicit TLS transport)
- `quic/...` — QUIC (TLS 1.3 mandatory, always encrypted)
- `tcp/...`, `udp/...`, `ws/...` — unencrypted (ACL still applies)

---

## Part 1: TLS Setup

### Configuration Location

All TLS settings live under `transport.link.tls` in your `config.json5`:

```json5
transport: {
  link: {
    tls: {
      root_ca_certificate:     null,   // path to CA cert
      listen_private_key:      null,   // server/listener private key
      listen_certificate:      null,   // server/listener certificate
      enable_mtls:             false,  // enable mutual TLS
      connect_private_key:     null,   // client/connector private key
      connect_certificate:     null,   // client/connector certificate
      verify_name_on_connect:  true,   // hostname verification
      close_link_on_expiration: false, // disconnect on cert expiry
      // so_rcvbuf: 65536,             // TCP read buffer (bytes)
      // so_sndbuf: 65536,             // TCP write buffer (bytes)
    }
  }
}
```

### TLS Config Field Reference

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `root_ca_certificate` | `string \| null` | `null` | Path to CA certificate file (PEM). Used to validate the remote peer's certificate. If `null` on a router-mode node, the system's built-in WebPKI roots are used (validates public CA-signed certs). |
| `listen_private_key` | `string \| null` | `null` | Path to the private key (PEM) used by the **listening** side (server role). Required when accepting `tls://` connections. |
| `listen_certificate` | `string \| null` | `null` | Path to the certificate (PEM) used by the **listening** side. Must match `listen_private_key`. |
| `enable_mtls` | `bool \| null` | `false` | Enable mutual TLS (mTLS). When `true`, the server demands that connecting clients also present a certificate. Clients must set `connect_private_key` and `connect_certificate`. |
| `connect_private_key` | `string \| null` | `null` | Path to the private key (PEM) used by the **connecting** side (client role). Required for mTLS. |
| `connect_certificate` | `string \| null` | `null` | Path to the certificate (PEM) used by the **connecting** side. Required for mTLS. |
| `verify_name_on_connect` | `bool \| null` | `true` | When `true`, verifies the server's hostname matches its certificate's CN or SAN. Setting to `false` disables hostname verification — dangerous in production, useful for self-signed certs in development. |
| `close_link_on_expiration` | `bool \| null` | `false` | When `true`, the link is automatically disconnected when the remote certificate chain expires. For listeners to disconnect clients on expiry, mTLS must be enabled. |
| `so_rcvbuf` | `u32 \| null` | null (OS default) | TCP receive buffer size in bytes for TLS links. |
| `so_sndbuf` | `u32 \| null` | null (OS default) | TCP send buffer size in bytes for TLS links. |

**Base64 inline variants** (for embedding certs/keys directly in config instead of files):

| Field | Notes |
|-------|-------|
| `root_ca_certificate_base64` | Base64-encoded PEM of the CA cert. Mutually exclusive with `root_ca_certificate`. Excluded from serialized output (contains secret). |
| `listen_private_key_base64` | Base64-encoded PEM of the listener private key. |
| `listen_certificate_base64` | Base64-encoded PEM of the listener cert. |
| `connect_private_key_base64` | Base64-encoded PEM of the connector private key. |
| `connect_certificate_base64` | Base64-encoded PEM of the connector cert. |

---

### Self-Signed Certificates

Use self-signed certs for local/private deployments where you control both sides.

#### Step 1: Create the Certificate Authority

```bash
# Generate CA key
openssl genrsa -out ca.key 4096

# Generate CA certificate (valid 10 years)
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt \
  -subj "/C=US/O=My Zenoh Network/CN=Zenoh CA"
```

#### Step 2: Create the Server Certificate

```bash
# Generate server key
openssl genrsa -out server.key 2048

# Create CSR with SAN extension (required for modern TLS; CN alone is not enough)
openssl req -new -key server.key -out server.csr \
  -subj "/C=US/O=My Zenoh Network/CN=zenoh-router.local" \
  -config <(cat <<EOF
[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[v3_req]
subjectAltName = @alt_names
[alt_names]
DNS.1 = zenoh-router.local
DNS.2 = localhost
IP.1 = 127.0.0.1
IP.2 = 192.168.1.100
EOF
)

# Sign the server certificate with your CA
openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out server.crt \
  -extensions v3_req \
  -extfile <(cat <<EOF
[v3_req]
subjectAltName = @alt_names
[alt_names]
DNS.1 = zenoh-router.local
DNS.2 = localhost
IP.1 = 127.0.0.1
IP.2 = 192.168.1.100
EOF
)
```

**Common mistake:** Omitting the SAN extension. Modern TLS clients (including Rust's `rustls`) reject certificates that only specify the hostname in `CN` without a matching `subjectAltName`. You will get a `CertificateVerificationFailure` or `InvalidCertificate` error at connection time.

#### Step 3: Create a Client Certificate (for mTLS)

```bash
# Generate client key
openssl genrsa -out client.key 2048

# Create client CSR — CN becomes the identity used in ACL cert_common_names
openssl req -new -key client.key -out client.csr \
  -subj "/C=US/O=My Zenoh Network/CN=robot-arm-1"

# Sign with the same CA
openssl x509 -req -days 365 -in client.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out client.crt
```

#### Step 4: Verify Certificate Chain

```bash
# Verify server cert is signed by CA
openssl verify -CAfile ca.crt server.crt

# Verify client cert is signed by CA
openssl verify -CAfile ca.crt client.crt

# Check the SAN entries on server cert
openssl x509 -in server.crt -text -noout | grep -A4 "Subject Alternative Name"

# Check expiration dates
openssl x509 -in server.crt -noout -dates
openssl x509 -in client.crt -noout -dates
```

---

### CA-Signed Certificates (Existing CA)

If you have an existing internal CA or use Let's Encrypt:

```bash
# Using Let's Encrypt (for public hostnames)
certbot certonly --standalone -d zenoh-router.example.com

# Resulting files:
# /etc/letsencrypt/live/zenoh-router.example.com/fullchain.pem  → listen_certificate
# /etc/letsencrypt/live/zenoh-router.example.com/privkey.pem    → listen_private_key
# root_ca_certificate: leave null (Let's Encrypt uses public WebPKI roots)
```

For an internal CA signed cert:

```bash
# Generate a CSR from your server
openssl req -new -key server.key -out server.csr \
  -subj "/CN=zenoh-router.corp.example.com" \
  -addext "subjectAltName=DNS:zenoh-router.corp.example.com"

# Submit CSR to your CA (procedure varies)
# Receive signed cert: server.crt

# Config: set root_ca_certificate to your CA's root cert
# so connecting peers can validate the server's certificate
```

---

### TLS Server Configuration (Router/Peer as Listener)

Save as `router-config.json5`:

```json5
{
  mode: "router",

  listen: {
    endpoints: [
      "tls/0.0.0.0:7447",
    ],
  },

  transport: {
    link: {
      tls: {
        // CA used to verify connecting clients (needed for mTLS)
        root_ca_certificate: "/etc/zenoh/certs/ca.crt",

        // Server identity
        listen_private_key: "/etc/zenoh/certs/server.key",
        listen_certificate:  "/etc/zenoh/certs/server.crt",

        // mTLS: require clients to present certs
        enable_mtls: true,

        verify_name_on_connect: true,
        close_link_on_expiration: false,
      }
    }
  }
}
```

### TLS Client Configuration (Peer as Connector)

Save as `client-config.json5`:

```json5
{
  mode: "peer",

  connect: {
    endpoints: [
      "tls/zenoh-router.local:7447",
    ],
  },

  transport: {
    link: {
      tls: {
        // CA to verify the server's certificate
        root_ca_certificate: "/etc/zenoh/certs/ca.crt",

        // Client identity (required if mTLS is enabled on the server)
        connect_private_key: "/etc/zenoh/certs/client.key",
        connect_certificate:  "/etc/zenoh/certs/client.crt",

        verify_name_on_connect: true,
      }
    }
  }
}
```

**Code example — Rust:**

```rust
use zenoh::Config;

fn main() -> zenoh::Result<()> {
    let mut config = Config::from_file("client-config.json5")?;
    let session = zenoh::open(config).res()?;
    let publisher = session.declare_publisher("demo/data").res()?;
    publisher.put("hello over TLS").res()?;
    Ok(())
}
```

**Code example — Python:**

```python
import zenoh

config = zenoh.Config.from_file("client-config.json5")
with zenoh.open(config) as session:
    pub = session.declare_publisher("demo/data")
    pub.put("hello over TLS")
```

---

### mTLS (Mutual TLS)

mTLS requires both sides to authenticate with certificates. This is the prerequisite for using `cert_common_names` in ACL rules.

**What mTLS requires:**

- **Server side:** `enable_mtls: true`, `root_ca_certificate` set (to validate client certs), `listen_private_key` + `listen_certificate` set
- **Client side:** `connect_private_key` + `connect_certificate` set (signed by the same CA the server trusts)

**How zenoh uses client cert CN for ACL:**
When a client connects with mTLS, zenoh extracts the `CN` (Common Name) from the client's certificate. This CN is the value you reference in the `cert_common_names` field of ACL subjects. For example, if the client cert has `CN=robot-arm-1`, you can write an ACL subject with `"cert_common_names": ["robot-arm-1"]`.

**Complete mTLS config pair:**

Server (`server-mtls.json5`):
```json5
{
  mode: "router",
  listen: {
    endpoints: ["tls/0.0.0.0:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate: "/certs/ca.crt",
        listen_private_key:  "/certs/server.key",
        listen_certificate:  "/certs/server.crt",
        enable_mtls:         true,
        verify_name_on_connect: true,
      }
    }
  },
  access_control: {
    enabled: true,
    default_permission: "deny",
    rules: [
      {
        id: "robot-arm-1-pub",
        messages: ["put", "delete"],
        flows: ["ingress"],
        permission: "allow",
        key_exprs: ["robot/arm1/**"],
      }
    ],
    subjects: [
      {
        id: "robot-arm-1",
        cert_common_names: ["robot-arm-1"],
      }
    ],
    policies: [
      {
        rules: ["robot-arm-1-pub"],
        subjects: ["robot-arm-1"],
      }
    ]
  }
}
```

Client (`client-robot-arm-1.json5`):
```json5
{
  mode: "peer",
  connect: {
    endpoints: ["tls/zenoh-router.local:7447"],
  },
  transport: {
    link: {
      tls: {
        root_ca_certificate:  "/certs/ca.crt",
        connect_private_key:  "/certs/robot-arm-1.key",
        connect_certificate:  "/certs/robot-arm-1.crt",
        verify_name_on_connect: true,
      }
    }
  }
}
```

---

### QUIC Security

QUIC **always uses TLS 1.3** — there is no plaintext QUIC mode. This means every `quic://` connection is encrypted by design, with no extra configuration required to enable encryption.

**QUIC endpoint:**
```json5
listen: {
  endpoints: ["quic/0.0.0.0:7447"],
}
```

**QUIC cert config** uses the same `transport.link.tls` section as TCP TLS — there is no separate QUIC-specific cert configuration:

```json5
transport: {
  link: {
    tls: {
      root_ca_certificate: "/certs/ca.crt",
      listen_private_key:  "/certs/server.key",
      listen_certificate:  "/certs/server.crt",
      enable_mtls:         true,        // also applies to QUIC
      connect_private_key: "/certs/client.key",
      connect_certificate: "/certs/client.crt",
    }
  }
}
```

**Differences from TCP TLS:**
- QUIC is UDP-based; `so_sndbuf`/`so_rcvbuf` TCP buffer options do not apply to QUIC links
- QUIC connections use TLS 1.3 exclusively (TCP TLS supports 1.2+)
- `cert_common_names` in ACL subjects works identically for QUIC
- mTLS is supported for QUIC with the same `enable_mtls` flag

---

### Certificate Rotation

Zenoh does **not** support live hot-reload of TLS certificates without restart. To rotate certificates:

1. Replace the cert/key files on disk with the new ones (keep the same file paths)
2. Restart the zenoh router or peer process

The `close_link_on_expiration` option provides automatic disconnection when a peer's certificate chain expires:

```json5
tls: {
  close_link_on_expiration: true,
  // Note: for a listener to disconnect clients, mTLS must be enabled
  enable_mtls: true,
}
```

When `close_link_on_expiration: true`:
- The link is disconnected when the remote certificate's expiration time is reached
- The zenoh session will attempt reconnection (subject to normal reconnection logic)
- On reconnect, the peer must present a new valid certificate

**Rotation workflow:**
```bash
# 1. Generate new certificate (before old one expires)
openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out server.crt.new ...

# 2. Atomically replace the old cert
mv server.crt.new /etc/zenoh/certs/server.crt

# 3. Restart zenoh
systemctl restart zenohd
# or for a peer process: send SIGTERM and let the orchestrator restart it
```

---

## Part 2: User/Password Authentication

In addition to TLS, zenoh supports username/password authentication for connecting peers. This provides an identity mechanism usable in ACL rules without requiring PKI.

### Configuration

```json5
transport: {
  auth: {
    usrpwd: {
      // Single user mode: specify credentials inline
      user: "zenoh_sensor_01",
      password: "s3cr3tpass",

      // OR: multi-user mode via dictionary file (overrides user/password above)
      // dictionary_file: "/etc/zenoh/users.txt",
    }
  }
}
```

**Dictionary file format** (`/etc/zenoh/users.txt`):
```
zenoh_sensor_01:s3cr3tpass
zenoh_robot_arm:another_secret
zenoh_admin:admin_pass
```

The `user` and `password` fields and the dictionary file are mutually exclusive in practice — `dictionary_file` takes precedence when set.

**Using username in ACL subjects:**

```json5
access_control: {
  enabled: true,
  default_permission: "deny",
  rules: [
    {
      id: "sensor-pub",
      messages: ["put"],
      flows: ["ingress"],
      permission: "allow",
      key_exprs: ["sensors/**"],
    }
  ],
  subjects: [
    {
      id: "sensor-nodes",
      usernames: ["zenoh_sensor_01", "zenoh_sensor_02"],
    }
  ],
  policies: [
    {
      rules: ["sensor-pub"],
      subjects: ["sensor-nodes"],
    }
  ]
}
```

---

## Part 3: ACL (Access Control Lists)

### Configuration Structure

ACL is configured under the `access_control` key. It is **disabled by default**.

```json5
access_control: {
  enabled: true,                   // false = ACL entirely skipped
  default_permission: "deny",      // "deny" (secure default) or "allow"
  rules: [ ... ],
  subjects: [ ... ],
  policies: [ ... ],
}
```

**Top-level fields:**

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `enabled` | `bool` | `false` | Master switch. If `false`, all ACL logic is bypassed. |
| `default_permission` | `"allow" \| "deny"` | `"deny"` | Fallback permission when no rule matches. If omitted or left empty, treated as `"deny"`. |
| `rules` | `array` | `null` | List of `AclConfigRule` objects defining permissions. |
| `subjects` | `array` | `null` | List of `AclConfigSubjects` objects identifying peers. |
| `policies` | `array` | `null` | Binds rules to subjects. |

---

### Rules

Each rule specifies what operations are allowed or denied on which key expressions.

**Rule fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `string` | Yes | Unique identifier within the `rules` list. Referenced by `policies`. |
| `key_exprs` | `string[]` | Yes | Zenoh key expressions to match. Supports `*`, `**`, and DSL operators. Must not be empty. |
| `messages` | `string[]` | Yes | Message types this rule applies to (see below). Must not be empty. |
| `flows` | `string[]` | No | `"egress"` and/or `"ingress"`. If omitted, applies to both flows. |
| `permission` | `"allow" \| "deny"` | Yes | What to do when this rule matches. |

**Complete message type list:**

| Config value | What it covers |
|--------------|----------------|
| `"put"` | `session.put()` and publisher `.put()` operations |
| `"delete"` | `session.delete()` operations |
| `"declare_subscriber"` | `session.declare_subscriber()` — the subscription declaration, not the received data |
| `"query"` | `session.get()` queries |
| `"reply"` | Replies sent by queryables in response to queries |
| `"declare_queryable"` | `session.declare_queryable()` — the queryable declaration |
| `"liveliness_token"` | `session.liveliness().declare_token()` |
| `"declare_liveliness_subscriber"` | `session.liveliness().declare_subscriber()` |
| `"liveliness_query"` | `session.liveliness().get()` |

**Flows — Ingress vs Egress:**

At a given zenoh node:

- **`ingress`**: Messages arriving at this node from a remote peer. Use `ingress` rules to control what remote peers can inject into this node.
- **`egress`**: Messages leaving this node toward a remote peer. Use `egress` rules to control what this node sends out.

For most ACL use cases, `ingress` is the most security-critical direction — it prevents unauthorized peers from publishing or subscribing. `egress` rules can be used for data-leak prevention (e.g., blocking certain key expressions from being forwarded to external peers).

**Performance tip:** Omitting the `flows` field (applying to both) triggers two checks per message. Specifying a single flow halves the ACL overhead for that rule.

---

### Subjects

Subjects identify which peers a policy applies to.

**Subject fields:**

| Field | Type | Description |
|-------|------|-------------|
| `id` | `string` | Unique identifier within `subjects`. Referenced by `policies`. |
| `interfaces` | `string[]` | Local network interface names (e.g., `"lo"`, `"eth0"`, `"en0"`). Messages from/to peers reachable via these interfaces match. |
| `cert_common_names` | `string[]` | CN from the peer's TLS certificate. Requires mTLS. |
| `usernames` | `string[]` | Username from user/password auth. |
| `link_protocols` | `string[]` | Transport protocols: `"tcp"`, `"udp"`, `"tls"`, `"quic"`, `"ws"`, `"serial"`, `"unixsock-stream"`, `"unixpipe"`, `"vsock"`. |
| `zids` | `string[]` | Zenoh session IDs (128-bit hex strings). **See ZID warning below.** |

**Subject combination logic:**

Within a subject, items in the **same list** are OR'd; items **across different lists** are AND'd. The internal filter is the Cartesian product of the lists:

```json5
{
  "id": "example",
  "interfaces": ["lo0", "en0"],
  "cert_common_names": ["my-robot"],
  "usernames": ["admin", "operator"],
  // Expands to:
  // (interface=lo0 AND cn=my-robot AND username=admin) OR
  // (interface=lo0 AND cn=my-robot AND username=operator) OR
  // (interface=en0 AND cn=my-robot AND username=admin) OR
  // (interface=en0 AND cn=my-robot AND username=operator)
}
```

A subject with **no fields** is a wildcard matching all peers:

```json5
{ "id": "everyone" }
```

---

### Subject Type Details

#### `interface` — Network Interface Name

Identifies peers by the local network interface through which they communicate.

- **Valid values:** Any interface name visible in `ip link` or `ifconfig` output: `"lo"`, `"lo0"`, `"eth0"`, `"en0"`, `"wlan0"`, etc.
- **Semantics:** The interface name is the *local* interface, not the remote peer's interface.
- **No interface match:** Peers connected via protocols without an interface (e.g., some WebSocket connections) match a subject with no `interfaces` field, but not a subject with an explicit `interfaces` list.

```json5
{
  "id": "internal-only",
  "interfaces": ["lo", "lo0"],  // loopback — local connections only
}
```

#### `cert_common_names` — TLS Client Certificate CN

Identifies peers by the Common Name in their TLS client certificate.

- **Requires:** mTLS enabled (`enable_mtls: true`) on this node, and the connecting peer must present a certificate signed by a trusted CA.
- **Value:** The CN string from the peer certificate, e.g., `"robot-arm-1"`, `"dashboard.corp.example.com"`.
- **Case-sensitive:** Matched as an exact string.

```json5
{
  "id": "trusted-robots",
  "cert_common_names": ["robot-arm-1", "robot-arm-2", "robot-base"],
}
```

#### `usernames` — Username/Password Auth

Identifies peers by their authentication username.

- **Requires:** User/password auth configured in `transport.auth.usrpwd`.
- **Value:** The username string as configured.

```json5
{
  "id": "admin-users",
  "usernames": ["admin", "superuser"],
}
```

#### `link_protocols` — Transport Protocol

Identifies peers by the transport protocol used for the link.

- **Valid values:** `"tcp"`, `"udp"`, `"tls"`, `"quic"`, `"ws"`, `"serial"`, `"unixsock-stream"`, `"unixpipe"`, `"vsock"`
- **Use case:** Apply stricter rules to unencrypted protocols, or trust TLS/QUIC peers more.

```json5
{
  "id": "encrypted-peers",
  "link_protocols": ["tls", "quic"],
}
```

#### `zids` — Zenoh Session ID

**⚠️ WARNING: ZID-based rules are fragile and should not be used in production.**

ZIDs are 128-bit hex identifiers assigned to each zenoh session. They change on every restart (unless you explicitly configure a static `id` in the config). A ZID-based ACL rule breaks every time the target peer restarts.

- **ZIDs are not authenticated:** Any peer can claim any ZID. ZIDs are only trustworthy if you use dedicated dynamic mechanisms that track transport open/close events to add/remove ZIDs to the ACL. Static ZID rules in the config file are prototype-only.
- **Recommended alternatives:** Use `cert_common_names` (mTLS) or `usernames` for persistent peer identity.

If you must use ZIDs for prototyping:

```json5
{
  "id": "specific-peer",
  "zids": ["38a4829bce9166ee1234567890abcdef"],
  // NOTE: This will break when the peer restarts with a new ZID
}
```

---

### Policies

Policies bind rules to subjects:

```json5
"policies": [
  {
    "id": "optional-policy-id",      // optional, must be unique if provided
    "rules": ["rule-id-1", "rule-id-2"],
    "subjects": ["subject-id-1", "subject-id-2"],
  }
]
```

A single policy can reference multiple rules and multiple subjects. The rules apply to all listed subjects.

---

### Rule Priority

For each authorization request, the evaluation order is:

```
explicit deny  >  explicit allow  >  default_permission
```

Pseudocode:
```rust
fn is_allowed(key_expr, flow, message, subject) -> bool {
    if default_permission == deny {
        // Must match an allow rule AND not match a deny rule
        !deny_ketree.matches(key_expr) && allow_ketree.matches(key_expr)
    } else {
        // default_permission == allow
        // Only blocked if it matches an explicit deny rule
        !deny_ketree.matches(key_expr)
    }
}
```

**Key implications:**

1. An explicit `deny` rule always wins over any `allow` rule.
2. When `default_permission: "deny"`, messages need an explicit allow rule to pass. Explicit deny rules are still useful (they fire before the allow check is even made).
3. When `default_permission: "allow"`, you only need deny rules for things to block. Explicit allow rules are ignored in this mode (they are redundant).

---

### Key Expression Matching in ACL

ACL rules use Zenoh key expression matching. A request key-expression **must be a subset of** (or equal to) the rule's key-expression to match. Being a superset does **not** match.

| Request KE | Rule KE | Match | Reason |
|------------|---------|-------|--------|
| `test/demo/a` | `test/demo/a` | ✓ | exact match |
| `test/demo/a` | `test/demo/*` | ✓ | subset of wildcard |
| `test/demo/a` | `**` | ✓ | subset of global wildcard |
| `test/**` | `test/demo/a` | ✗ | superset, not subset |
| `test/demo/*` | `test/*/a` | ✗ | partial overlap only |

**Practical implications:**
- Allow rule `sensors/**` will allow `sensors/temp/room1` (subset) ✓
- Allow rule `sensors/**` will **not** match a request for `sensors/**` itself (superset of `sensors/a`) ✗
- Deny rule `admin/**` + `default_permission: allow` blocks `admin/config` but not `**` (if a subscriber tries to subscribe to everything)

---

### ACL Working Examples

#### Example 1: Read-Only Namespace (Subscribers Allowed, Publishers Denied)

Scenario: Allow any peer to subscribe to `telemetry/**`, but only trusted nodes can publish.

```json5
access_control: {
  enabled: true,
  default_permission: "deny",
  rules: [
    {
      id: "sub-telemetry",
      messages: ["declare_subscriber"],
      flows: ["ingress"],
      permission: "allow",
      key_exprs: ["telemetry/**"],
    },
    {
      id: "pub-telemetry",
      messages: ["put", "delete"],
      flows: ["ingress"],
      permission: "allow",
      key_exprs: ["telemetry/**"],
    },
  ],
  subjects: [
    { "id": "any-peer" },                            // wildcard — all peers
    { "id": "trusted-publishers", "interfaces": ["eth0"] },  // internal net
  ],
  policies: [
    {
      rules: ["sub-telemetry"],
      subjects: ["any-peer"],
    },
    {
      rules: ["pub-telemetry"],
      subjects: ["trusted-publishers"],
    },
  ]
}
```

#### Example 2: Namespace Segregation (Multi-Robot)

Scenario: Each robot can only pub/sub on its own namespace. No cross-robot data leakage.

Certificates issued with CNs: `robot-a`, `robot-b`.

```json5
// Router config with mTLS + namespace isolation
transport: {
  link: {
    tls: {
      root_ca_certificate: "/certs/ca.crt",
      listen_private_key:  "/certs/router.key",
      listen_certificate:  "/certs/router.crt",
      enable_mtls: true,
    }
  }
},
access_control: {
  enabled: true,
  default_permission: "deny",
  rules: [
    {
      id: "robot-a-access",
      messages: ["put", "delete", "declare_subscriber", "query", "reply", "declare_queryable"],
      permission: "allow",
      key_exprs: ["robot/a/**"],
    },
    {
      id: "robot-b-access",
      messages: ["put", "delete", "declare_subscriber", "query", "reply", "declare_queryable"],
      permission: "allow",
      key_exprs: ["robot/b/**"],
    },
  ],
  subjects: [
    { "id": "robot-a", "cert_common_names": ["robot-a"] },
    { "id": "robot-b", "cert_common_names": ["robot-b"] },
  ],
  policies: [
    { rules: ["robot-a-access"], subjects: ["robot-a"] },
    { rules: ["robot-b-access"], subjects: ["robot-b"] },
  ]
}
```

#### Example 3: Per-Interface Access Control

Scenario: Nodes on the internal `eth0` interface get full access. Nodes on external-facing `eth1` can only read sensor data.

```json5
access_control: {
  enabled: true,
  default_permission: "deny",
  rules: [
    {
      id: "internal-full-access",
      messages: ["put", "delete", "declare_subscriber", "query", "reply",
                 "declare_queryable", "liveliness_token", "declare_liveliness_subscriber"],
      flows: ["ingress", "egress"],
      permission: "allow",
      key_exprs: ["**"],
    },
    {
      id: "external-read-sensors",
      messages: ["declare_subscriber"],
      flows: ["ingress"],
      permission: "allow",
      key_exprs: ["sensors/**"],
    },
  ],
  subjects: [
    { "id": "internal-net", "interfaces": ["eth0"] },
    { "id": "external-net", "interfaces": ["eth1"] },
  ],
  policies: [
    { rules: ["internal-full-access"],  subjects: ["internal-net"] },
    { rules: ["external-read-sensors"], subjects: ["external-net"] },
  ]
}
```

#### Example 4: mTLS + Cert CN Based Rules

Scenario: A fleet of sensors authenticates via certificates. Sensors can publish but not query. A dashboard can query but not publish.

```json5
// Generate certs: CN=sensor-fleet, CN=dashboard-service
access_control: {
  enabled: true,
  default_permission: "deny",
  rules: [
    {
      id: "sensor-publish",
      messages: ["put"],
      flows: ["ingress"],
      permission: "allow",
      key_exprs: ["sensors/**", "actuators/feedback/**"],
    },
    {
      id: "dashboard-query",
      messages: ["query", "declare_subscriber"],
      flows: ["ingress"],
      permission: "allow",
      key_exprs: ["sensors/**", "actuators/**"],
    },
  ],
  subjects: [
    { "id": "sensors",   "cert_common_names": ["sensor-fleet"] },
    { "id": "dashboard", "cert_common_names": ["dashboard-service"] },
  ],
  policies: [
    { rules: ["sensor-publish"],  subjects: ["sensors"] },
    { rules: ["dashboard-query"], subjects: ["dashboard"] },
  ]
}
```

#### Example 5: Full Deny-by-Default with Explicit Allow List

Scenario: Zero-trust configuration. Everything is denied unless explicitly listed.

```json5
access_control: {
  enabled: true,
  default_permission: "deny",
  rules: [
    {
      id: "allow-all-on-loopback",
      messages: ["put", "delete", "declare_subscriber", "query", "reply",
                 "declare_queryable", "liveliness_token",
                 "declare_liveliness_subscriber", "liveliness_query"],
      flows: ["ingress", "egress"],
      permission: "allow",
      key_exprs: ["**"],
    },
    {
      id: "allow-telemetry-sub",
      messages: ["declare_subscriber"],
      flows: ["ingress"],
      permission: "allow",
      key_exprs: ["telemetry/**"],
    },
    {
      id: "allow-telemetry-pub",
      messages: ["put"],
      flows: ["ingress"],
      permission: "allow",
      key_exprs: ["telemetry/**"],
    },
    {
      // Explicit deny wins over allow — blocks admin space from external
      id: "deny-admin",
      messages: ["put", "delete", "declare_subscriber", "query"],
      flows: ["ingress", "egress"],
      permission: "deny",
      key_exprs: ["@/**"],
    },
  ],
  subjects: [
    { "id": "loopback",           "interfaces": ["lo", "lo0"] },
    { "id": "sensor-publishers",  "cert_common_names": ["sensor-node"] },
    { "id": "sensor-subscribers", "cert_common_names": ["consumer-node"] },
    { "id": "all-peers" },   // wildcard for deny-admin
  ],
  policies: [
    { rules: ["allow-all-on-loopback"], subjects: ["loopback"] },
    { rules: ["allow-telemetry-pub"],   subjects: ["sensor-publishers"] },
    { rules: ["allow-telemetry-sub"],   subjects: ["sensor-subscribers"] },
    { rules: ["deny-admin"],            subjects: ["all-peers"] },
  ]
}
```

---

## Part 4: Combining TLS and ACL in Python

Full working example of a publisher connecting with TLS and subject to ACL:

**Router config** (`router.json5`):

```json5
{
  mode: "router",
  listen: { endpoints: ["tls/0.0.0.0:7447"] },
  transport: {
    link: {
      tls: {
        root_ca_certificate: "/tmp/certs/ca.crt",
        listen_private_key:  "/tmp/certs/server.key",
        listen_certificate:  "/tmp/certs/server.crt",
        enable_mtls: true,
      }
    }
  },
  access_control: {
    enabled: true,
    default_permission: "deny",
    rules: [
      {
        id: "pub-demo",
        messages: ["put"],
        flows: ["ingress"],
        permission: "allow",
        key_exprs: ["demo/**"],
      },
      {
        id: "sub-demo",
        messages: ["declare_subscriber"],
        flows: ["ingress"],
        permission: "allow",
        key_exprs: ["demo/**"],
      },
    ],
    subjects: [{ "id": "demo-client", "cert_common_names": ["demo-client"] }],
    policies: [{ rules: ["pub-demo", "sub-demo"], subjects: ["demo-client"] }],
  }
}
```

**Publisher** (`tls_publisher.py`):

```python
import zenoh

config = zenoh.Config.from_file("client.json5")  # has connect_private_key / connect_certificate
with zenoh.open(config) as session:
    pub = session.declare_publisher("demo/hello")
    pub.put("hello from mTLS client")
    print("Published!")
```

**Subscriber** (`tls_subscriber.py`):

```python
import zenoh
import time

def on_data(sample):
    print(f"Received: {sample.key_expr} = {sample.payload.to_string()}")

config = zenoh.Config.from_file("client.json5")
with zenoh.open(config) as session:
    sub = session.declare_subscriber("demo/**", on_data)
    print("Subscribed, waiting...")
    time.sleep(10)
```

---

## Part 5: ACL Performance Tips

From the official RFC:

1. **Use exact keys over wildcards** when possible. `sensors/temp/room1` is faster than `sensors/*/room1` or `sensors/**`.
2. **Minimize key expression depth.** `a/b/c` is faster than `a/b/c/d/e/f` (deeper KeTrees = more traversal).
3. **Specify a single flow** per rule when only one direction is relevant. Using both flows doubles the check cost.
4. **Keep rule lists specific.** Only include the message types your scenario actually uses. Don't enumerate all 9 message types if you only need `put` and `declare_subscriber`.
5. **Wildcards and DSL operators** (`$*`, `$**`) are significantly slower than verbatim keys or simple `*`/`**`. Avoid them in hot paths.
6. **Verbatims (`@...` prefix)** are okay — they require an exact match on the verbatim portion, which is fast.

---

## Quick Reference

### TLS Config Snippet (Server with mTLS)

```json5
transport: { link: { tls: {
  root_ca_certificate: "/certs/ca.crt",
  listen_private_key:  "/certs/server.key",
  listen_certificate:  "/certs/server.crt",
  enable_mtls:         true,
  verify_name_on_connect: true,
  close_link_on_expiration: false,
}}}
```

### TLS Config Snippet (Client with mTLS)

```json5
transport: { link: { tls: {
  root_ca_certificate: "/certs/ca.crt",
  connect_private_key: "/certs/client.key",
  connect_certificate: "/certs/client.crt",
  verify_name_on_connect: true,
}}}
```

### Minimal ACL (Deny All Except Loopback)

```json5
access_control: {
  enabled: true,
  default_permission: "deny",
  rules: [{
    id: "allow-loopback-all",
    messages: ["put","delete","declare_subscriber","query","reply","declare_queryable"],
    permission: "allow",
    key_exprs: ["**"],
  }],
  subjects: [{ "id": "lo", "interfaces": ["lo", "lo0"] }],
  policies: [{ rules: ["allow-loopback-all"], subjects: ["lo"] }],
}
```

### Certificate Generation One-Liner (Dev/Test Only)

```bash
# CA
openssl req -new -x509 -days 3650 -newkey rsa:4096 -keyout ca.key -out ca.crt \
  -nodes -subj "/CN=dev-ca"

# Server (with SAN)
openssl req -new -newkey rsa:2048 -keyout server.key -out server.csr \
  -nodes -subj "/CN=localhost" \
  -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"
openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out server.crt -copy_extensions copy

# Client (identity = robot-node)
openssl req -new -newkey rsa:2048 -keyout client.key -out client.csr \
  -nodes -subj "/CN=robot-node"
openssl x509 -req -days 365 -in client.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out client.crt
```

(`-addext` and `-copy_extensions copy` require OpenSSL 1.1.1+. If you see `unknown option`, upgrade OpenSSL or use the separate config file approach shown earlier.)

## See Also

- [ACL Guide](acl-guide.md) — access control lists that use mTLS certificate CNs as subject identifiers; complements transport-layer encryption
- [Config Connect Listen](config-connect-listen.md) — the `tls://` and `quic://` endpoint formats that activate the TLS config documented here
- [Config Transport Link RX TCP](config-transport-link-rx-tcp.md) — the `transport.link.tls` section with the field-level reference for TLS configuration
