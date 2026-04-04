# Zenoh REST and Web Server Plugins

Zenoh ships two HTTP bridge plugins that map between standard HTTP and the zenoh protocol. They serve different purposes and have different capability profiles:

| | REST Plugin (`zenoh-plugin-rest`) | Web Server Plugin (`zenoh-plugin-webserver`) |
|---|---|---|
| Methods | GET, PUT, DELETE, POST, PATCH | GET only |
| Source | Bundled in `zenoh` repo | Separate `zenoh-plugin-webserver` repo |
| Activation | `--rest-http-port` CLI flag or config | Config only |
| Streaming | Server-Sent Events (SSE) | Multipart (`multipart/x-mixed-replace`) |
| Wildcards | Supported in key expressions | Not allowed |
| Default interface | `[::]` (dual-stack IPv6/IPv4) | `0.0.0.0` (IPv4) |
| CORS | Always `Access-Control-Allow-Origin: *` | Not set |
| Primary use case | General-purpose REST API bridge | Serving static sites via zenoh storages |

---

## Table of Contents

- [REST Plugin (`zenoh-plugin-rest`)](#rest-plugin-zenoh-plugin-rest)
  - [What It Does](#what-it-does)
  - [Activation](#activation)
  - [Configuration Options](#configuration-options)
  - [URL-to-Key-Expression Mapping](#url-to-key-expression-mapping)
  - [Query Parameters (Selectors)](#query-parameters-selectors)
  - [Response Formats](#response-formats)
  - [Content-Type → Zenoh Encoding Mapping (PUT)](#content-type-zenoh-encoding-mapping-put)
  - [Server-Sent Events (SSE)](#server-sent-events-sse)
  - [CORS](#cors)
  - [Authentication and TLS](#authentication-and-tls)
  - [Example Configurations](#example-configurations)
  - [curl Examples](#curl-examples)
- [Web Server Plugin (`zenoh-plugin-webserver`)](#web-server-plugin-zenoh-plugin-webserver)
  - [What It Does](#what-it-does)
  - [Activation](#activation)
  - [Configuration Options](#configuration-options)
  - [URL-to-Key-Expression Mapping](#url-to-key-expression-mapping)
  - [Content-Type Response](#content-type-response)
  - [Multipart Streaming](#multipart-streaming)
  - [Example Configuration](#example-configuration)
  - [curl Examples](#curl-examples)
- [Choosing Between the Two Plugins](#choosing-between-the-two-plugins)
- [Troubleshooting](#troubleshooting)
  - [Address Already in Use](#address-already-in-use)
  - [Permission Denied (Linux, port < 1024)](#permission-denied-linux-port-1024)
  - [REST Plugin Returns `[]` (Empty Array)](#rest-plugin-returns-empty-array)
  - [SSE Connection Drops After 10 Seconds](#sse-connection-drops-after-10-seconds)
  - [WebServer Returns 400 for URL with `*`](#webserver-returns-400-for-url-with)

## REST Plugin (`zenoh-plugin-rest`)

### What It Does

The REST plugin exposes a full HTTP API that bridges to zenoh operations:

- **HTTP GET** → `session.get()` — queries zenoh key expressions, collects replies, returns JSON array
- **HTTP PUT** → `session.put()` — publishes a value to a zenoh key expression
- **HTTP DELETE** → `session.delete()` — deletes a key from zenoh storages
- **HTTP PATCH** — mapped to `session.put()` (same as PUT)
- **HTTP POST** — mapped to `session.get()` (same as GET); any request body is passed as the query payload
- **HTTP GET with `Accept: text/event-stream`** → `session.declare_subscriber()` — opens an SSE stream for real-time updates

The plugin is statically linked into `zenohd` and is always present; it must be activated explicitly.

### Activation

Via CLI flag (simplest):

```bash
zenohd --rest-http-port 8000
```

Via configuration file:

```json5
{
  plugins: {
    rest: {
      http_port: 8000,
    }
  }
}
```

### Configuration Options

All options live under `plugins.rest` in the zenoh config file.

#### `http_port` (required)

**Type:** integer or string
**Default:** none (must be specified)
**Valid values:**
- Integer port number: `8000` — binds to `[::]` (all interfaces, dual-stack IPv4/IPv6)
- String port only: `"8000"` — same as integer form
- String `"ip:port"`: `"127.0.0.1:8000"` — binds to a specific interface

When given as an integer or bare port string, the default bind interface is `[::]` which accepts both IPv4 and IPv6 connections.

```json5
// Bind on all interfaces, port 8000
http_port: 8000

// Bind only on localhost
http_port: "127.0.0.1:8000"

// IPv6 loopback
http_port: "[::1]:8000"
```

#### `work_thread_num` (optional)

**Type:** integer
**Default:** `2`
**Valid values:** any positive integer
**Effect:** Number of Tokio worker threads. Only takes effect when running as a dynamic plugin (`.so`/`.dylib`); when statically linked into `zenohd`, the router's existing runtime is reused.

```json5
work_thread_num: 4
```

#### `max_block_thread_num` (optional)

**Type:** integer
**Default:** `50`
**Valid values:** any positive integer
**Effect:** Maximum number of blocking threads in the Tokio runtime. Same dynamic-plugin-only caveat as `work_thread_num`.

```json5
max_block_thread_num: 100
```

#### Internal fields (`__path__`, `__required__`, `__config__`, `__plugin__`)

These are zenoh plugin-loader metadata fields, not REST-specific config:
- `__required__: true` — causes `zenohd` to panic if the plugin fails to load (default: false)
- `__config__: "./path/to/config.json5"` — loads additional config from a file, merging it in
- `__path__` — explicit path to the plugin `.so`/`.dylib` (bypasses automatic search)

### URL-to-Key-Expression Mapping

The HTTP path is stripped of its leading `/` and used directly as a zenoh key expression:

```
HTTP path              →  Zenoh key expression
/robot/arm/position    →  robot/arm/position
/sensors/**            →  sensors/**
/foo/bar               →  foo/bar
/                      →  (empty string)
```

**Special cases:**

- `@/local` → `@/<router-zid>` (resolves to the local router's admin space)
- `@/local/<suffix>` → `@/<router-zid>/<suffix>`

**Wildcards:** The REST plugin accepts wildcards (`*`, `**`) in URLs. The URL `GET /sensors/**` issues a fanout query matching all keys under `sensors/`.

**URL encoding:** Standard percent-encoding applies. The path is taken verbatim after stripping the leading slash; no additional escaping is performed.

### Query Parameters (Selectors)

URL query parameters are passed as-is to the zenoh selector. This allows full use of zenoh's selector parameter syntax:

| Parameter | Meaning | Example |
|-----------|---------|---------|
| `_time` | Time-range selector for historical queries | `?_time=[now(-1h)..now()]` |
| `_raw` | Return raw bytes instead of JSON | `?_raw` |
| Any other key=value | Passed to the queryable as selector parameters | `?format=compact` |

**Consolidation behavior:**
- If the query string contains a `_time` range, consolidation mode is set to `None` (all replies returned, including duplicates across time)
- Otherwise, consolidation mode is `Latest` (one reply per key, newest wins)

### Response Formats

The response format is controlled by the `Accept` request header:

| `Accept` header | Response format |
|----------------|-----------------|
| `application/json` (default) | JSON array of samples |
| `text/html` | `<dl>` definition list of key/value pairs |
| `text/event-stream` | SSE stream (does not query — subscribes instead) |
| Anything else | JSON array |

**`?_raw` parameter:** Overrides Accept header. Returns the raw payload bytes of the first reply, with `Content-Type` set to the zenoh encoding of that sample. Useful when the value is already a known content type (image, PDF, etc.).

**JSON sample format:**

```json
[
  {
    "key": "robot/arm/position",
    "value": {"x": 1.0, "y": 2.0, "z": 3.0},
    "encoding": "application/json",
    "timestamp": "2024-01-15T10:30:00Z/1"
  }
]
```

Value encoding rules:
- `application/json`, `text/json`, `text/json5` — deserialized directly as JSON; falls back to base64 if not valid JSON
- `text/plain`, `zenoh/string` — included as a JSON string; falls back to base64 if not valid UTF-8
- All other encodings — base64-encoded string

### Content-Type → Zenoh Encoding Mapping (PUT)

On PUT requests, the `Content-Type` request header is read and mapped to a zenoh `Encoding`:

```bash
# PUT with text/plain encoding
curl -X PUT -H "Content-Type: text/plain" -d "hello world" http://localhost:8000/my/key

# PUT with application/json encoding
curl -X PUT -H "Content-Type: application/json" -d '{"x": 1}' http://localhost:8000/my/key

# PUT with custom encoding
curl -X PUT -H "Content-Type: application/octet-stream" --data-binary @file.bin http://localhost:8000/my/key
```

If no `Content-Type` is provided, zenoh uses its default encoding.

### Server-Sent Events (SSE)

To subscribe to a zenoh key expression and receive a real-time stream of publications, send a GET request with `Accept: text/event-stream`. The plugin upgrades the connection to an SSE stream and internally calls `session.declare_subscriber()`.

**URL pattern:**

```
GET /<key-expression>
Accept: text/event-stream
```

**Event format:**

Each publication arrives as an SSE event:

```
event: PUT
data: {"key":"sensors/temp","value":"23.5","encoding":"zenoh/string","timestamp":"..."}

event: DELETE
data: {"key":"sensors/temp","value":null,"encoding":"zenoh/bytes","timestamp":null}
```

- `event` field = sample kind (`PUT` or `DELETE`, uppercase — the server uses `SampleKind::to_string()` which returns uppercase)
- `data` field = JSON-encoded `JSONSample` object (same format as query responses)

**Connection lifecycle:**
- The subscription lives as long as the HTTP connection is open
- On disconnection (client closes, network error, or 10-second send timeout), the subscriber is undeclared automatically
- Browsers with `EventSource` reconnect automatically on disconnect

**JavaScript example:**

```javascript
const source = new EventSource("http://localhost:8000/sensors/temperature");

source.addEventListener("PUT", (e) => {
  const sample = JSON.parse(e.data);
  console.log(`${sample.key} = ${sample.value} (${sample.encoding})`);
});

source.addEventListener("DELETE", (e) => {
  const sample = JSON.parse(e.data);
  console.log(`Deleted: ${sample.key}`);
});

source.onerror = (e) => {
  console.error("SSE connection error", e);
  // EventSource reconnects automatically
};
```

### CORS

The REST plugin always responds with:

```
Access-Control-Allow-Origin: *
```

This means any web page can make requests to the REST API without CORS preflight issues. It is hardcoded and cannot be disabled via configuration.

### Authentication and TLS

The REST plugin has no built-in authentication or TLS support. Options for securing it:

**Option 1: Reverse proxy with nginx**

```nginx
server {
    listen 443 ssl;
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        # Require bearer token
        if ($http_authorization != "Bearer my-secret-token") {
            return 401;
        }
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
    }
}
```

**Option 2: Reverse proxy with Caddy**

```caddyfile
:443 {
    tls /path/to/cert.pem /path/to/key.pem
    basicauth /* {
        admin $2a$14$... # bcrypt hash
    }
    reverse_proxy localhost:8000
}
```

**Option 3: Bind to localhost only**

If the REST API is only accessed by local processes or a trusted sidecar:

```json5
http_port: "127.0.0.1:8000"
```

### Example Configurations

**Basic REST API on port 8000:**

```json5
{
  plugins_loading: {
    enabled: true,
  },
  plugins: {
    rest: {
      http_port: 8000,
    }
  }
}
```

**REST API bound to specific interface, required, with thread tuning:**

```json5
{
  plugins_loading: {
    enabled: true,
  },
  plugins: {
    rest: {
      __required__: true,
      http_port: "192.168.1.10:8080",
      work_thread_num: 4,
      max_block_thread_num: 200,
    }
  }
}
```

**REST + storage for persistent key-value store:**

```json5
{
  plugins_loading: {
    enabled: true,
  },
  plugins: {
    rest: {
      http_port: 8000,
    },
    storage_manager: {
      volumes: {
        memory: {}
      },
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

### curl Examples

**GET — query a key expression:**

```bash
# Returns JSON array of all matching samples
curl http://localhost:8000/robot/arm/position
```

**GET — multiple values with wildcard:**

```bash
curl http://localhost:8000/sensors/**
```

**GET — with time-range selector (historical query):**

```bash
# Query samples from the last hour (requires a storage with time-series support)
curl "http://localhost:8000/sensors/temperature?_time=[now(-1h)..now()]"
```

**GET — raw bytes (no JSON wrapping):**

```bash
# Returns raw payload with original Content-Type
curl "http://localhost:8000/images/logo.png?_raw" -o logo.png
```

**GET — HTML format:**

```bash
curl -H "Accept: text/html" http://localhost:8000/demo/
```

**GET — SSE stream:**

```bash
# Streams events until interrupted
curl -H "Accept: text/event-stream" http://localhost:8000/sensors/temperature
```

**PUT — publish a string value:**

```bash
curl -X PUT \
  -H "Content-Type: text/plain" \
  -d "hello world" \
  http://localhost:8000/my/key
```

**PUT — publish JSON:**

```bash
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"temperature": 23.5, "unit": "celsius"}' \
  http://localhost:8000/sensors/temp/reading
```

**PUT — publish binary file:**

```bash
curl -X PUT \
  -H "Content-Type: application/octet-stream" \
  --data-binary @firmware.bin \
  http://localhost:8000/devices/robot1/firmware
```

**DELETE — remove a key:**

```bash
curl -X DELETE http://localhost:8000/my/key
```

**Admin space — query router info:**

```bash
# Get local router admin info
curl "http://localhost:8000/@/local/**"

# Get all routers in the system
curl "http://localhost:8000/@/**"
```

---

## Web Server Plugin (`zenoh-plugin-webserver`)

### What It Does

The Web Server plugin implements a read-only HTTP server that maps URL paths to zenoh key expressions and returns the values. It is designed primarily for serving static website content stored in zenoh backends (file system, database, etc.).

- **HTTP GET** → `session.get()` — fetches a single resource by key expression
- **HTTP GET with `?_method=SUB`** → `session.declare_subscriber()` — streams a multipart response
- No PUT, DELETE, or POST support

The plugin is in a separate repository (`zenoh-plugin-webserver`) and must be installed separately.

### Activation

The plugin is loaded automatically by `zenohd` when present in the plugins search path and configured:

```json5
{
  plugins_loading: {
    enabled: true,
  },
  plugins: {
    webserver: {
      http_port: 8080,
    }
  }
}
```

### Configuration Options

#### `http_port` (required)

**Type:** integer or string
**Default:** none (must be specified)
**Valid values:**
- Integer port number: `8080` — binds to `0.0.0.0` (all IPv4 interfaces)
- String port only: `"8080"` — same as integer form
- String `"ip:port"`: `"127.0.0.1:8080"` — binds to a specific interface

Unlike the REST plugin, the default interface is `0.0.0.0` (IPv4 only, not dual-stack).

```json5
http_port: 8080
http_port: "0.0.0.0:8080"
http_port: "127.0.0.1:8080"
```

#### `work_thread_num` (optional)

**Type:** integer
**Default:** `2`
**Effect:** Same as REST plugin — Tokio worker threads, dynamic-plugin-only.

#### `max_block_thread_num` (optional)

**Type:** integer
**Default:** `50`
**Effect:** Same as REST plugin — blocking thread cap, dynamic-plugin-only.

### URL-to-Key-Expression Mapping

The leading `/` is stripped from the URL path, and the remainder is used as the zenoh key expression:

```
HTTP path              →  Zenoh key expression
/my-site/index.html    →  my-site/index.html
/my-site/css/style.css →  my-site/css/style.css
/                      →  index.html  (directory index auto-append)
/my-site/              →  my-site/index.html
```

**Directory index behavior:**
- If the path ends with `/` or is empty, `index.html` is automatically appended
- If the exact KE has no result but `<ke>/index.html` does, the server returns an HTTP 301 redirect to `<url>/`
- This mirrors conventional web server directory index behavior

**Wildcard restriction:** Unlike the REST plugin, wildcards (`*`, `**`) are not allowed in URLs. A request containing `*` returns HTTP 400 with the message: `"The URL must correspond to 1 resource only (i.e. zenoh key expressions not supported)"`.

**Query string → zenoh selector:** URL query parameters are forwarded to zenoh as selector parameters. For example, `GET /my-site/data?_time=[now(-1h)..now()]` issues the zenoh query `my-site/data?_time=[now(-1h)..now()]`.

### Content-Type Response

The `Content-Type` of HTTP responses is derived from the zenoh encoding of the returned sample. For example, if a value was stored with encoding `text/html`, the HTTP response will have `Content-Type: text/html`. If the encoding cannot be parsed as a MIME type, the fallback is `application/octet-stream`.

### Multipart Streaming

To receive a live stream of updates for a key expression, append `?_method=SUB` to the URL:

```
GET /sensors/temperature?_method=SUB
```

The server subscribes to the key expression and streams updates as a `multipart/x-mixed-replace` response. Each part has the format:

```
--boundary
Content-Type: <encoding>

<raw payload bytes>
```

This format is supported by some browsers natively (for images) and is widely used for MJPEG streams. Unlike SSE, it streams raw bytes rather than JSON.

**10-second timeout:** If no message can be sent within 10 seconds (e.g., client buffer full), the subscription is dropped and the connection closed.

### Example Configuration

**Static website served via File System backend:**

```json5
{
  plugins_loading: {
    enabled: true,
  },
  plugins: {
    webserver: {
      http_port: 8080,
    },
    storage_manager: {
      volumes: {
        fs: {}
      },
      storages: {
        my_site: {
          key_expr: "my-site/**",
          strip_prefix: "my-site",
          volume: {
            id: "fs",
            dir: "my-site",
            read_only: true
          }
        }
      }
    }
  }
}
```

With this config, files in `~/.zenoh/zbackend_fs/my-site/` are browsable at `http://localhost:8080/my-site/`.

**REST API (port 8000) + Web Server (port 8080) together:**

```json5
{
  plugins_loading: {
    enabled: true,
  },
  plugins: {
    rest: {
      http_port: 8000,
    },
    webserver: {
      http_port: 8080,
    },
    storage_manager: {
      volumes: {
        memory: {}
      },
      storages: {
        all: {
          key_expr: "**",
          volume: { id: "memory" }
        }
      }
    }
  }
}
```

### curl Examples

**GET a specific resource:**

```bash
curl http://localhost:8080/my-site/index.html
```

**GET with time selector:**

```bash
curl "http://localhost:8080/sensors/temperature?_time=[now(-5m)..now()]"
```

**Stream live updates (multipart):**

```bash
# Streams until interrupted; each frame separated by --boundary
curl "http://localhost:8080/sensors/temperature?_method=SUB"
```

---

## Choosing Between the Two Plugins

Use the **REST plugin** when:
- You need write operations (PUT, DELETE) from HTTP clients
- You want SSE for real-time browser subscriptions with JSON payloads
- You need wildcard queries (e.g., `GET /sensors/**` to read all sensors at once)
- You are building a general-purpose REST API over zenoh

Use the **Web Server plugin** when:
- You are serving static content (HTML, CSS, JS, images) stored in zenoh backends
- You want conventional web server behavior (directory index, Content-Type from encoding, 301 redirects)
- You need multipart streaming (MJPEG camera feeds, etc.)
- You explicitly want to prevent write operations from HTTP clients

Both plugins can run simultaneously on different ports in the same `zenohd` instance.

---

## Troubleshooting

### Address Already in Use

```
ERROR zenoh_plugin_webserver Unable to start http server for WebServer plugin : Os { code: 48, kind: AddrInUse, message: "Address already in use" }
```

Another process is using the configured port. Either stop the other process or change `http_port` in the plugin config.

### Permission Denied (Linux, port < 1024)

```
ERROR Unable to start http server for WebServer plugin : Os { code: 13, kind: PermissionDenied, message: "Permission denied" }
```

Linux restricts ports 0–1023 to root. Solutions:
- Use a port number above 1024 (e.g., `8000`, `8080`)
- Run `zenohd` with `sudo`
- Use `setcap CAP_NET_BIND_SERVICE` on the `zenohd` binary

### REST Plugin Returns `[]` (Empty Array)

No queryables or storages are responding to the key expression. Verify:
1. A storage is configured with a matching `key_expr`
2. The key has been written (PUT) at least once
3. The key expression in the URL matches the storage's `key_expr`

### SSE Connection Drops After 10 Seconds

The 10-second timeout fires when the server cannot send a message to the HTTP client within that window — specifically when the client's TCP buffer is full (back-pressure). It is **not** an idle timeout triggered by absence of publications. If no messages are published, the subscription stays open indefinitely. The timeout indicates a slow or unresponsive client, not an infrequently-updated key.

### WebServer Returns 400 for URL with `*`

Wildcards are not supported in the Web Server plugin. Use the REST plugin instead if you need to query multiple keys at once.

## See Also

- [Plugin Storage Manager Guide](plugin-storage-manager-guide.md) — the storage manager that provides queryable data served by the REST plugin
- [Key Expressions Guide](key-expressions-guide.md) — wildcard key expression syntax supported in REST plugin URLs
- [Config Connect Listen](config-connect-listen.md) — how the router hosting the REST plugin is reached by external HTTP clients
