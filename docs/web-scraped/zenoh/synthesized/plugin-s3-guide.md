# Zenoh S3 Backend Plugin Guide

The `zenoh-backend-s3` plugin implements durable storage for the Zenoh router using any S3-compatible object storage service. Key/value publications made via zenoh are stored as S3 objects and returned on queries.

**Library name:** `libzenoh_backend_s3`
**Version:** 1.7.2 (paired with zenoh 1.7.2)
**Capability:** Durable persistence, latest-value history

---

## Table of Contents

- [Compatible Services](#compatible-services)
  - [AWS S3 (official)](#aws-s3-official)
  - [MinIO (self-hosted, S3-compatible)](#minio-self-hosted-s3-compatible)
  - [Ceph Object Gateway (RGW)](#ceph-object-gateway-rgw)
  - [Google Cloud Storage (S3-compatible mode)](#google-cloud-storage-s3-compatible-mode)
  - [Other S3-compatible services](#other-s3-compatible-services)
- [Configuration Reference](#configuration-reference)
  - [Volume-Level Options](#volume-level-options)
  - [Storage-Level Options (inside `volume: { ... }`)](#storage-level-options-inside-volume)
  - [Storage-Level Options (top-level, alongside `volume:`)](#storage-level-options-top-level-alongside-volume)
- [Object Naming: How Zenoh KEs Map to S3 Keys](#object-naming-how-zenoh-kes-map-to-s3-keys)
  - [Special Key: `@@none_key@@`](#special-key-none_key)
  - [Key Mapping Table](#key-mapping-table)
  - [S3 Key Naming Constraints](#s3-key-naming-constraints)
- [Timestamp Preservation in S3 Object Metadata](#timestamp-preservation-in-s3-object-metadata)
  - [Metadata Key Names](#metadata-key-names)
  - [Encoding Preservation](#encoding-preservation)
  - [Implications for `_time` Selector](#implications-for-_time-selector)
- [Authentication](#authentication)
  - [Explicit Credentials (access_key / secret_key)](#explicit-credentials-access_key-secret_key)
  - [IAM Role / Instance Profile (AWS-only)](#iam-role-instance-profile-aws-only)
  - [Environment Variable Overrides](#environment-variable-overrides)
  - [MinIO-Specific Auth](#minio-specific-auth)
- [Example Configurations](#example-configurations)
  - [1. AWS S3 with Explicit Credentials](#1-aws-s3-with-explicit-credentials)
  - [2. AWS S3 with Explicit Credentials (Required)](#2-aws-s3-with-explicit-credentials-required)
  - [3. MinIO Self-Hosted Instance](#3-minio-self-hosted-instance)
  - [4. MinIO with TLS (HTTPS)](#4-minio-with-tls-https)
  - [5. Google Cloud Storage (S3-Compatible Mode)](#5-google-cloud-storage-s3-compatible-mode)
- [Runtime Configuration via Admin Space](#runtime-configuration-via-admin-space)
  - [Add a Volume](#add-a-volume)
  - [Add a Storage](#add-a-storage)
  - [Test with REST API](#test-with-rest-api)
- [Code Examples](#code-examples)
  - [Rust: Publish and Query via S3 Storage](#rust-publish-and-query-via-s3-storage)
  - [Python: Publish and Query via S3 Storage](#python-publish-and-query-via-s3-storage)
- [Installation](#installation)
  - [Pre-built Packages](#pre-built-packages)
  - [Building from Source](#building-from-source)
- [Architecture Notes](#architecture-notes)
  - [Persistence and History](#persistence-and-history)
  - [Concurrency](#concurrency)
  - [Force Path Style](#force-path-style)

## Compatible Services

### AWS S3 (official)
The primary target. Specify `region` in the volume config; the endpoint is resolved automatically from the region name. Use standard AWS credential patterns (config file, environment variables, or `private: { access_key, secret_key }`).

### MinIO (self-hosted, S3-compatible)
Fully supported. Specify `url` pointing to your MinIO server instead of (or in addition to) `region`. MinIO ignores the region value, so it can be omitted. TLS support via custom CA certificate is documented below.

### Ceph Object Gateway (RGW)
Supported via S3-compatibility mode. Provide `url` pointing to the RGW endpoint. Ceph RGW uses virtual-hosted-style or path-style URLs; the plugin always uses **path-style** (`force_path_style = true`), which is compatible with both Ceph and MinIO.

### Google Cloud Storage (S3-compatible mode)
GCS offers an S3-compatible XML API at `https://storage.googleapis.com`. Use `url: "https://storage.googleapis.com"` and provide HMAC credentials (`access_key` / `secret_key`) generated in the GCS console under Cloud Storage > Settings > Interoperability.

### Other S3-compatible services
Any service that implements the AWS S3 API with path-style access (the plugin sets `force_path_style = true`) should work. Provide the `url` of the endpoint and credentials as `access_key` / `secret_key`.

---

## Configuration Reference

Configuration is split into two layers:

- **Volume config** (`plugins.storage_manager.volumes.s3`): shared settings for the S3 connection (endpoint, region, TLS). One volume per region/endpoint.
- **Storage config** (`plugins.storage_manager.storages.<name>.volume`): per-storage settings (bucket, credentials, closure behavior).

### Volume-Level Options

#### `region`
- **Type:** string
- **Default:** `"us-east-1"` (applied internally if omitted; AWS requires a valid region)
- **Valid values:** Any AWS region name, e.g. `"us-east-1"`, `"eu-west-1"`, `"ap-northeast-1"`. See [AWS S3 endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html).
- **Required for AWS:** Yes — determines the endpoint URL when `url` is not specified.
- **Required for MinIO/Ceph/GCS:** No — these services ignore it.
- **Example:** `region: "eu-west-1"`

#### `url`
- **Type:** string (URL)
- **Default:** none (AWS endpoint resolver is used based on `region`)
- **Required for MinIO/Ceph/GCS:** Yes — must point to your service endpoint.
- **Required for AWS:** No — omit to let the SDK resolve from `region`.
- **Example:** `url: "http://localhost:9000"` (MinIO), `url: "https://storage.googleapis.com"` (GCS)

#### `tls` (volume-level, optional)
Enables HTTPS for connections to the S3 server. Shared by all storages under this volume. Contains a `private` sub-object with:

- **`tls.private.root_ca_certificate_file`**
  - **Type:** string (file path)
  - **Default:** none (only system/WebPKI CAs are trusted)
  - **Purpose:** Path to a PEM-format CA certificate file. Used when your S3 server uses a self-signed or private CA (common with MinIO TLS). The plugin merges this CA with the built-in WebPKI roots.
  - **Example:** `root_ca_certificate_file: "/home/user/certs/minica.pem"`

- **`tls.private.root_ca_certificate_base64`**
  - **Type:** string (base64-encoded PEM)
  - **Default:** none
  - **Purpose:** Inline alternative to `root_ca_certificate_file`. Useful when embedding config in environments without file access.
  - **Example:** `root_ca_certificate_base64: "LS0tLS1CRUdJTi..."`
  - **Note:** Only one of `root_ca_certificate_file` or `root_ca_certificate_base64` should be specified.

### Storage-Level Options (inside `volume: { ... }`)

#### `bucket`
- **Type:** string
- **Default:** none — **required**
- **Purpose:** The S3 bucket name this storage is associated with. Each storage maps to exactly one bucket.
- **Constraints:** Must be a valid S3 bucket name (3–63 lowercase alphanumeric characters or hyphens, no underscores, no uppercase). See [S3 bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html).
- **Example:** `bucket: "zenoh-telemetry"`

#### `reuse_bucket`
- **Type:** boolean
- **Default:** `false`
- **Purpose:** Controls behavior when the storage starts and the bucket already exists (and is owned by you).
  - `false`: startup fails if the bucket already exists
  - `true`: attach to the existing bucket without error
- **Example:** `reuse_bucket: true`

#### `read_only`
- **Type:** boolean
- **Default:** `false`
- **Purpose:** When `true`, the storage handles only GET (query) requests. PUT and DELETE operations are rejected with a warning.
- **Example:** `read_only: false`

#### `on_closure`
- **Type:** string enum
- **Default:** `"do_nothing"`
- **Valid values:**
  - `"do_nothing"` — when the storage is removed, the S3 bucket is left intact with all its objects
  - `"destroy_bucket"` — when the storage is removed, all objects in the bucket are deleted and then the bucket itself is deleted
- **Note:** `"destroy_bucket"` requires `plugins.adminspace.permissions.write = true` in the zenoh router config.
- **Example:** `on_closure: "do_nothing"`

#### `private.access_key`
- **Type:** string
- **Default:** none — **required**
- **Purpose:** AWS access key ID (or MinIO/GCS HMAC key ID). Placed inside a `private: { }` block to prevent the value from appearing in public admin-space queries.
- **Example:** `access_key: "AKIAIOSFODNN7EXAMPLE"`

#### `private.secret_key`
- **Type:** string
- **Default:** none — **required**
- **Purpose:** AWS secret access key (or MinIO/GCS HMAC secret). Must be inside `private: { }`.
- **Example:** `secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"`

### Storage-Level Options (top-level, alongside `volume:`)

These are standard zenoh storage manager options:

#### `key_expr`
- **Type:** zenoh key expression string
- **Default:** none — **required**
- **Purpose:** The key expression this storage subscribes to. All publications matching this expression are stored.
- **Example:** `key_expr: "sensors/**"`

#### `strip_prefix`
- **Type:** string (key expression prefix)
- **Default:** none
- **Purpose:** The prefix to strip from incoming keys before converting to S3 object keys. Must be a prefix of `key_expr`. This is the storage-manager level concept; the stripped remainder becomes the S3 object key (optionally further prefixed by a `path_prefix` if one were configured, though the S3 backend derives `path_prefix` directly from `strip_prefix`).
- **Constraint:** Must be a valid prefix of `key_expr`. If it does not match, the storage fails to start.
- **Example:** `strip_prefix: "sensors"` — publication to `sensors/room1/temp` is stored as `room1/temp`

---

## Object Naming: How Zenoh KEs Map to S3 Keys

The S3 backend uses a two-step conversion:

1. The `strip_prefix` value is stripped from the incoming zenoh key expression.
2. The remaining suffix becomes the S3 object key.

The plugin always uses **path-style access** (`force_path_style = true`), meaning the bucket name is part of the URL path, not the hostname. This ensures compatibility with MinIO, Ceph, and other non-AWS services.

Leading `/` characters are trimmed from keys for compatibility between AWS S3 and MinIO.

### Special Key: `@@none_key@@`

The plugin uses the internal sentinel value `@@none_key@@` as the S3 object key when the storage receives `None` for the key (i.e., when there is no key to store). This prevents empty-key errors at the S3 API level.

### Key Mapping Table

Assume `key_expr: "sensors/**"` and `strip_prefix: "sensors"`:

| Zenoh KE (published)     | S3 object key           |
|--------------------------|-------------------------|
| `sensors/room1/temp`     | `room1/temp`            |
| `sensors/room1/humidity` | `room1/humidity`        |
| `sensors/outdoor`        | `outdoor`               |
| `sensors`                | `@@none_key@@`          |

Assume `key_expr: "s3/example/*"` and `strip_prefix: "s3/example"`:

| Zenoh KE (published) | S3 object key |
|----------------------|---------------|
| `s3/example/test`    | `test`        |
| `s3/example/a/b`     | `a/b`         |
| `s3/example`         | `@@none_key@@`|

### S3 Key Naming Constraints

S3 keys can contain most Unicode characters. Zenoh key expressions use `/` as a hierarchy separator and `*`/`**` as wildcards. After stripping the prefix:
- The `/` hierarchy separator is preserved as-is in S3 keys (S3 natively supports `/` as a pseudo-directory delimiter).
- Wildcard characters (`*`, `**`) in the `key_expr` are allowed in the _subscription pattern_ but will never appear in stored keys, since actual publications have concrete keys.

---

## Timestamp Preservation in S3 Object Metadata

Every PUT operation stores the zenoh timestamp in the S3 object's user-defined metadata. This metadata is written as a key-value pair attached to the S3 object and is retrieved on GET operations to reconstruct the full `StoredData` including the original timestamp.

### Metadata Key Names

| Metadata key          | Status    | Purpose                                    |
|-----------------------|-----------|--------------------------------------------|
| `zenoh-timestamp`     | Current   | Stores the zenoh `uhlc` timestamp string   |
| `timestamp_uhlc`      | Deprecated | Legacy key; read as fallback if `zenoh-timestamp` is absent |

**Why two keys?** NGINX's default configuration (`underscores_in_headers off`) drops HTTP headers that contain underscores. The old key `timestamp_uhlc` was therefore invisible when the S3 service sat behind NGINX. The new key `zenoh-timestamp` uses a hyphen and passes through NGINX correctly.

**Fallback read logic:** On `get_all_entries` (used for storage reconciliation), the plugin reads `zenoh-timestamp` first and falls back to `timestamp_uhlc` if absent. Note: for individual GET queries, the plugin requires `zenoh-timestamp` to be present; it does not fall back to `timestamp_uhlc` in that code path.

### Encoding Preservation

The value encoding is stored as the S3 object's `Content-Encoding` HTTP header. On GET, the `content_encoding()` value is read back and converted to a zenoh `Encoding`. If absent, `Encoding::default()` is used.

### Implications for `_time` Selector

The zenoh storage manager uses timestamps to reconcile storage replicas and answer time-filtered queries (`?_time=...`). Because timestamps are stored in S3 metadata, `get_all_entries` must perform a `HeadObject` call per object to retrieve timestamps — this is an O(n) operation over the bucket's object count. For large buckets this can be slow; consider scoping storages to bounded key expression subtrees.

---

## Authentication

### Explicit Credentials (access_key / secret_key)

Place credentials in the `private:` block inside the storage's `volume:` section. The `private:` block prevents credentials from appearing in zenoh admin-space queries.

```json5
volume: {
  id: "s3",
  bucket: "my-bucket",
  private: {
    access_key: "AKIAIOSFODNN7EXAMPLE",
    secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  },
}
```

Credentials can also be placed outside `private:` (directly in `volume:`), but the plugin will emit a warning asking you to move them into `private:`.

### IAM Role / Instance Profile (AWS-only)

**Important:** The current plugin implementation (`src/config.rs`) requires `access_key` and `secret_key` to be explicitly provided — it returns an initialization error if they are missing. The plugin does not support the AWS SDK's default credential chain (IAM roles, IMDS, environment variable fallback) out of the box.

To use environment-based credentials or IAM roles, you must still supply `access_key` and `secret_key` in the config (even as empty strings), but this will cause the SDK to use those literal values rather than checking IMDS. The workaround is to supply actual credentials from the IAM role as environment variables and also set matching values in the config — or patch the source to make credentials optional.

### Environment Variable Overrides

Note: Because the plugin explicitly sets credentials from config and overrides the AWS SDK's default provider chain, standard AWS environment variables (`AWS_ACCESS_KEY_ID`, etc.) do **not** override the config values at runtime. The credentials from the config file take precedence.

### MinIO-Specific Auth

MinIO uses the same S3 API credential scheme. The `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD` you set when starting MinIO correspond to `access_key` and `secret_key` in the zenoh config. Additional MinIO users/service accounts can be created in the MinIO console and their access/secret keys used directly.

---

## Example Configurations

### 1. AWS S3 with Explicit Credentials

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        s3: {
          // AWS region — endpoint resolved automatically
          region: "us-east-1",
        },
      },
      storages: {
        sensor_storage: {
          key_expr: "sensors/**",
          strip_prefix: "sensors",
          volume: {
            id: "s3",
            bucket: "my-zenoh-sensors",
            reuse_bucket: true,
            read_only: false,
            on_closure: "do_nothing",
            private: {
              access_key: "AKIAIOSFODNN7EXAMPLE",
              secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            },
          },
        },
      },
    },
    rest: { http_port: 8000 },
  },
}
```

### 2. AWS S3 with Explicit Credentials (Required)

The current plugin implementation requires `access_key` and `secret_key` in all cases. Even when using EC2 IAM roles or EKS IRSA, you must supply the credentials explicitly:

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        s3: {
          region: "us-west-2",
        },
      },
      storages: {
        telemetry_storage: {
          key_expr: "telemetry/**",
          strip_prefix: "telemetry",
          volume: {
            id: "s3",
            bucket: "zenoh-telemetry-prod",
            reuse_bucket: true,
            read_only: false,
            on_closure: "do_nothing",
            // Credentials are required — provide actual values here.
            // IAM role / default credential chain is not supported.
            private: {
              access_key: "AKIAIOSFODNN7EXAMPLE",
              secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            },
          },
        },
      },
    },
  },
}
```

Run the router:
```bash
zenohd -c zenoh.json5
```

### 3. MinIO Self-Hosted Instance

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        s3: {
          // MinIO endpoint — region is ignored by MinIO but required by the SDK
          url: "http://localhost:9000",
          // region can be omitted; "us-east-1" is used internally as a placeholder
        },
      },
      storages: {
        minio_storage: {
          key_expr: "data/**",
          strip_prefix: "data",
          volume: {
            id: "s3",
            bucket: "zenoh-data",
            reuse_bucket: true,
            read_only: false,
            on_closure: "do_nothing",
            private: {
              // MinIO root user / service account credentials
              access_key: "AKIAIOSFODNN7EXAMPLE",
              secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            },
          },
        },
      },
    },
    rest: { http_port: 8000 },
  },
}
```

Start MinIO with Docker:
```bash
docker run -p 9000:9000 -p 9090:9090 \
  --user $(id -u):$(id -g) \
  --name minio \
  -e 'MINIO_ROOT_USER=AKIAIOSFODNN7EXAMPLE' \
  -e 'MINIO_ROOT_PASSWORD=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY' \
  -v ${HOME}/minio/data:/data \
  quay.io/minio/minio server data --console-address ':9090'
```

### 4. MinIO with TLS (HTTPS)

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        s3: {
          // HTTPS endpoint
          url: "https://minio.internal:9000",
          tls: {
            private: {
              // Path to the CA that signed the MinIO server certificate
              root_ca_certificate_file: "/home/user/certs/minica.pem",
              // Or inline as base64:
              // root_ca_certificate_base64: "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t..."
            },
          },
        },
      },
      storages: {
        secure_storage: {
          key_expr: "secure/**",
          strip_prefix: "secure",
          volume: {
            id: "s3",
            bucket: "zenoh-secure",
            reuse_bucket: true,
            read_only: false,
            on_closure: "do_nothing",
            private: {
              access_key: "AKIAIOSFODNN7EXAMPLE",
              secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            },
          },
        },
      },
    },
  },
}
```

Generate TLS certificates with minica:
```bash
minica --domains minio.internal
# Produces: minio.internal/cert.pem, minio.internal/key.pem, minica.pem
# Rename for MinIO: cert.pem -> public.crt, key.pem -> private.key
```

Start MinIO with TLS:
```bash
docker run -p 9000:9000 -p 9090:9090 \
  --user $(id -u):$(id -g) \
  --name minio \
  -e 'MINIO_ROOT_USER=AKIAIOSFODNN7EXAMPLE' \
  -e 'MINIO_ROOT_PASSWORD=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY' \
  -v ${HOME}/minio/data:/data \
  -v ${HOME}/minio/certs:/certs \
  quay.io/minio/minio server data --certs-dir certs --console-address ':9090'
```

### 5. Google Cloud Storage (S3-Compatible Mode)

```json5
{
  plugins: {
    storage_manager: {
      volumes: {
        s3: {
          // GCS S3-compatible XML API endpoint
          url: "https://storage.googleapis.com",
          region: "us-central1",
        },
      },
      storages: {
        gcs_storage: {
          key_expr: "gcs/**",
          strip_prefix: "gcs",
          volume: {
            id: "s3",
            bucket: "my-zenoh-gcs-bucket",
            reuse_bucket: true,
            read_only: false,
            on_closure: "do_nothing",
            private: {
              // GCS HMAC keys from Cloud Storage > Settings > Interoperability
              access_key: "GOOGTS7C7FUP2AIRVJTE2BCDKINBTES3HC2GY5CBFJDCQ2SYHV6A6XXVIGISK7MKJ",
              secret_key: "bGoa+V7g/yqDXvKRqq+JTFn4uQZbPiQJo4pf9RzJ",
            },
          },
        },
      },
    },
  },
}
```

---

## Runtime Configuration via Admin Space

Storages can be added, inspected, or removed at runtime via the zenoh admin space (requires the REST plugin and `adminspace.permissions.write = true`).

### Add a Volume

```bash
curl -X PUT \
  -H 'content-type:application/json' \
  -d '{
    url: "http://localhost:9000",
    private: {
      access_key: "AKIAIOSFODNN7EXAMPLE",
      secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    }
  }' \
  http://localhost:8000/@/local/router/config/plugins/storage_manager/volumes/s3
```

### Add a Storage

```bash
curl -X PUT \
  -H 'content-type:application/json' \
  -d '{
    key_expr: "s3/example/*",
    strip_prefix: "s3/example",
    volume: {
      id: "s3",
      bucket: "zenoh-bucket",
      reuse_bucket: false,
      region: "eu-west-3",
      on_closure: "do_nothing",
      private: {
        access_key: "AKIAIOSFODNN7EXAMPLE",
        secret_key: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
      }
    }
  }' \
  http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/s3_storage
```

### Test with REST API

```bash
# Publish a value (stored in S3)
curl -X PUT \
  -H 'content-type:application/json' \
  -d '{"sensor": "temperature", "value": 22.5}' \
  http://localhost:8000/s3/example/room1

# Query the stored value
curl http://localhost:8000/s3/example/room1

# Delete the stored value
curl -X DELETE http://localhost:8000/s3/example/room1

# Remove the storage (triggers on_closure behavior)
curl -X DELETE \
  'http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/s3_storage'

# Remove the volume
curl -X DELETE \
  'http://localhost:8000/@/local/router/config/plugins/storage_manager/volumes/s3'
```

---

## Code Examples

### Rust: Publish and Query via S3 Storage

```rust
use zenoh::bytes::Encoding;

#[tokio::main]
async fn main() -> zenoh::Result<()> {
    // Open session connected to a zenoh router with S3 backend configured
    let mut config = zenoh::Config::default();
    config.insert_json5("connect/endpoints", r#"["tcp/localhost:7447"]"#).unwrap();
    let session = zenoh::open(config).await?;

    // Publish a value — the router's S3 storage will persist it
    session
        .put("sensors/room1/temp", "22.5")
        .encoding(Encoding::TEXT_PLAIN)
        .await?;

    println!("Published temperature reading.");

    // Query the stored value
    let replies = session
        .get("sensors/room1/temp")
        .await?;

    while let Ok(reply) = replies.recv_async().await {
        match reply.result() {
            Ok(sample) => {
                println!(
                    "Retrieved: {} = {:?}",
                    sample.key_expr(),
                    sample.payload()
                );
            }
            Err(err) => eprintln!("Error: {:?}", err),
        }
    }

    session.close().await?;
    Ok(())
}
```

### Python: Publish and Query via S3 Storage

```python
import zenoh
import time

def main():
    conf = zenoh.Config()
    # Connect to a zenoh router with S3 backend configured
    session = zenoh.open(conf)

    # Publish a value — stored in S3 by the router
    session.put("sensors/room1/temp", b"22.5")
    print("Published temperature reading.")

    time.sleep(0.1)  # Allow propagation

    # Query the stored value
    replies = session.get("sensors/room1/temp")
    for reply in replies:
        if reply.ok:
            sample = reply.ok
            print(f"Retrieved: {sample.key_expr} = {bytes(sample.payload.to_bytes()).decode()}")
        else:
            print(f"Error: {reply.err}")

    session.close()

if __name__ == "__main__":
    main()
```

---

## Installation

### Pre-built Packages

**Linux Debian:**
```bash
echo "deb [trusted=yes] https://download.eclipse.org/zenoh/debian-repo/ /" \
  | sudo tee -a /etc/apt/sources.list > /dev/null
sudo apt update
sudo apt install zenoh-backend-s3
```

**Manual (all platforms):**
Download from `https://download.eclipse.org/zenoh/zenoh-backend-s3/latest/`, extract the `.zip` for your platform, and place `libzenoh_backend_s3` in `~/.zenoh/lib/` or alongside `zenohd`.

### Building from Source

```bash
# Match the exact Rust version used to build your zenohd
zenohd --version  # shows rustc version
rustup default <rustc-version>

cargo build --release --all-targets
```

Place the resulting library in `~/.zenoh/lib/`:
```bash
ln -s $(pwd)/target/release/libzenoh_backend_s3.dylib ~/.zenoh/lib/
# On Linux: libzenoh_backend_s3.so
```

> **Warning:** The Rust ABI is not stable. The backend must be compiled with the exact same `rustc` version as `zenohd`. A mismatch causes a `SIGSEGV` crash at load time.

---

## Architecture Notes

### Persistence and History

The S3 backend declares:
- **Persistence:** `Durable` — values survive router restarts
- **History:** `Latest` — only the most recent value per key is retained (S3 does not natively version by key expression; each PUT overwrites the existing object at that key)

### Concurrency

The plugin runs two Tokio worker threads with up to 50 blocking threads. When loaded as a dynamic plugin (no ambient Tokio runtime), it creates its own `tokio::Runtime`. All S3 API calls are async, wrapped with the `await_task!` macro to handle both standalone and plugin contexts.

### Force Path Style

The plugin always constructs S3 requests using path-style URLs (`/<bucket>/<key>`) rather than virtual-hosted-style (`<bucket>.s3.amazonaws.com/<key>`). This is required for MinIO and Ceph compatibility. AWS S3 supports both styles; path-style is being deprecated for new buckets on AWS but continues to work.

## See Also

- [Plugin Storage Manager Guide](plugin-storage-manager-guide.md) — the storage manager plugin that loads and manages S3 storages
- [Storage Backends Guide](storage-backends-guide.md) — when to choose S3 vs RocksDB, filesystem, or InfluxDB
