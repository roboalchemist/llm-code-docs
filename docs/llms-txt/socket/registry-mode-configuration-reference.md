# Source: https://docs.socket.dev/docs/registry-mode-configuration-reference.md

# Configuration Reference

# Configuration Reference

Complete reference for Socket Registry Firewall configuration options. All options can be set in `socket.yml` or overridden via environment variables.

## Configuration File (`socket.yml`)

The firewall reads configuration from `/app/socket.yml` inside the container. Mount your config file:

```yaml
volumes:
  - ./socket.yml:/app/socket.yml:ro
```

***

## Core Socket Settings

```yaml
socket:
  # Socket.dev API endpoint (required)
  api_url: https://api.socket.dev
  
  # Behavior when Socket API is unreachable
  fail_open: true            # true = allow packages (default), false = block all
  
  # Console log level (controls which messages appear in logs)
  log_level: info            # error, warn, info (default), debug
  
  # Corporate egress proxy for all upstream connections
  outbound_proxy: http://proxy.company.com:3128
  no_proxy: localhost,127.0.0.1,internal.company.com
  
  # SSL verification for Socket API calls
  api_ssl_verify: false      # Verify SSL for Socket API (default: false)
  api_ssl_ca_cert: /path/to/corporate-ca.crt  # Custom CA cert
  
  # SSL verification for upstream registry connections
  upstream_ssl_verify: false # Verify SSL for upstream registries (default: false, inherits api_ssl_verify)
  upstream_ssl_ca_cert: /path/to/upstream-ca.crt  # Custom CA for upstreams
  
  # Request behavior
  request_id_header: X-Socket-Request-ID  # Custom request ID header name
  
  # Client auth gate (require clients to present a Bearer token)
  bearer_token: my-secret-token   # Literal value (default type is "string")
  # bearer_token_type: env        # Set to "env" if bearer_token is an env var name
```

**Environment variables:**

```bash
SOCKET_SECURITY_API_TOKEN=your-api-key  # Required (scopes: packages:list, entitlements:list)
SOCKET_API_URL=https://api.socket.dev
SOCKET_FAIL_OPEN=true
SOCKET_LOG_LEVEL=info
SOCKET_OUTBOUND_PROXY=http://proxy:3128
SOCKET_NO_PROXY=localhost,127.0.0.1
SOCKET_BEARER_TOKEN=my-secret-token     # Client auth gate (alternative to socket.bearer_token in YAML)
```

***

## Client Auth Gate (`bearer_token`)

Optional feature to require all inbound requests to present a valid `Authorization: Bearer <token>` header. When configured, requests without a matching token receive a `401 Unauthorized` response.

### Configuration

```yaml
socket:
  # Option 1: Literal token (default — bearer_token_type is "string")
  bearer_token: my-secret-token

  # Option 2: Read token from an environment variable
  bearer_token: SOCKET_AUTH_TOKEN       # Name of the env var (NOT the value)
  bearer_token_type: env                # Tells config tool to resolve the env var
```

| Setting             | Values          | Default   | Description                                                        |
| ------------------- | --------------- | --------- | ------------------------------------------------------------------ |
| `bearer_token`      | string          | *(empty)* | The token value, or env var name when `bearer_token_type` is `env` |
| `bearer_token_type` | `string`, `env` | `string`  | How to interpret `bearer_token`                                    |

Or via environment variable (works without any YAML config):

```bash
SOCKET_BEARER_TOKEN=my-secret-token
```

### Behavior

* **All requests** (except `/health`) must include `Authorization: Bearer <token>` matching the configured value
* Unauthenticated or mismatched requests receive `401` with `WWW-Authenticate: Bearer` header and JSON error body
* The `/health` endpoint is **exempt** from auth — always accessible without a token
* When auth succeeds, the client's `Authorization` header is **stripped** and NOT forwarded upstream. Upstream auth is handled separately via `upstream_token` if configured
* Auth failures are logged (tokens are never logged)

### Interaction with `upstream_token`

| `bearer_token` | `upstream_token` | Behavior                                            |
| :------------: | :--------------: | :-------------------------------------------------- |
|        —       |         —        | Client auth passes through to upstream (default)    |
|       set      |         —        | Client must match; **no** auth forwarded upstream   |
|        —       |        set       | No inbound gate; upstream gets token from env var   |
|       set      |        set       | Client must match; upstream gets token from env var |

***

## Upstream Auth Token (`upstream_token`)

Inject a `Bearer` token on all upstream (firewall → registry) requests for a specific route. The token value comes from an environment variable — the YAML config specifies only the **env var name**, so secrets never appear in config files.

### Configuration

Supported on both path-based routes and domain-based registries:

```yaml
# Path-based routing
path_routing:
  routes:
    - path: /pypi
      upstream: https://private-pypi.company.com
      registry: pypi
      upstream_token: PYPI_AUTH_TOKEN        # env var name → value used as Bearer token

    - path: /npm
      upstream: https://private-npm.company.com
      registry: npm
      upstream_token: NPM_AUTH_TOKEN

# Domain-based routing
registries:
  pypi:
    domains:
      - pypi.company.com
    upstream: https://private-pypi.company.com
    upstream_token: PYPI_AUTH_TOKEN           # same behavior for domain routes
```

Set the actual token value as an environment variable on the container:

```bash
# Bearer token (no colon in value)
PYPI_AUTH_TOKEN=my-secret-pypi-token

# Basic auth (user:password format — auto-detected by the colon)
NPM_AUTH_TOKEN=deploy-user:s3cret-passw0rd
```

| Setting          | Values | Default   | Description                                                                          |
| ---------------- | ------ | --------- | ------------------------------------------------------------------------------------ |
| `upstream_token` | string | *(empty)* | Name of an environment variable containing the auth credential for upstream requests |

### Auth Scheme Auto-Detection

The firewall inspects the **value** of the env var at startup to choose the HTTP auth scheme:

| Env var value                  | Detected scheme | Authorization header sent                   |
| :----------------------------- | :-------------- | :------------------------------------------ |
| `my-token-string` (no `:`)     | Bearer          | `Authorization: Bearer my-token-string`     |
| `user:password` (contains `:`) | Basic           | `Authorization: Basic dXNlcjpwYXNzd29yZA==` |

This is fully automatic — no additional configuration needed.

### Behavior

* When `upstream_token` is set for a route, every upstream request on that route includes the auto-detected `Authorization` header — replacing any client-sent Authorization header
* Routes without `upstream_token` pass the client's Authorization header through unchanged (default behavior)
* The env var name must match `[A-Za-z_][A-Za-z0-9_]*` (standard env var naming)
* Token values are **pre-resolved at worker startup** for performance (no per-request `os.getenv()` overhead)
* Token values are **never logged** — only the env var name appears in init logs as `<redacted>`
* If the env var is empty or not set, a warning is logged and no Authorization header is injected

### Security Notes

* Token values exist only in environment variables and process memory — never in config files or logs
* Each route can have a different token, enabling per-registry credential isolation
* Works independently from `bearer_token` (inbound client auth gate) — see interaction table above

***

## Response Tracking Headers

The firewall adds tracking headers to responses for downstream observability and end-to-end request correlation.

### Request ID Header

Every response includes a request ID header for tracking. The header name is configurable via `socket.request_id_header` in `socket.yml` (default: `X-Socket-Request-ID`). The same header is also sent to upstream registries and the Socket API for end-to-end correlation.

```yaml
socket:
  request_id_header: X-Socket-Request-ID  # Default value; customize as needed
```

| Header                | Present On    | Description                                                                                               |
| --------------------- | ------------- | --------------------------------------------------------------------------------------------------------- |
| `X-Socket-Request-ID` | All responses | Unique request identifier (nginx `$request_id`). Header name configurable via `socket.request_id_header`. |

### Decision Headers

Security-checked requests (package downloads) include additional headers indicating the firewall's decision. Passthrough requests (metadata, checksums, default routes) do **not** include decision headers.

| Header                    | Present On                      | Values / Description                                                                                                                                                       |
| ------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `X-Socket-Decision`       | Security-checked responses      | `allowed` — Package passed security checks. `blocked` — Package blocked by security policy. `fail_open` — Socket API unavailable, package allowed due to fail-open policy. |
| `X-Socket-Block-Reason`   | Blocked responses (403)         | Comma-separated alert titles that caused the block (e.g., `malware,typosquat`).                                                                                            |
| `X-Socket-Warn-Reason`    | Allowed responses with warnings | Comma-separated alert titles with warn-level severity.                                                                                                                     |
| `X-Socket-Monitor-Reason` | Allowed responses with monitors | Comma-separated alert titles with monitor-level severity.                                                                                                                  |

**Examples:**

Blocked package:

```
HTTP/1.1 403 Forbidden
X-Socket-Request-ID: a1b2c3d4e5f6...
X-Socket-Decision: blocked
X-Socket-Block-Reason: malware,typosquat
```

Allowed package with warnings:

```
HTTP/1.1 200 OK
X-Socket-Request-ID: a1b2c3d4e5f6...
X-Socket-Decision: allowed
X-Socket-Warn-Reason: protestware
```

Allowed package (no alerts):

```
HTTP/1.1 200 OK
X-Socket-Request-ID: a1b2c3d4e5f6...
X-Socket-Decision: allowed
```

Passthrough request (metadata/checksums):

```
HTTP/1.1 200 OK
X-Socket-Request-ID: a1b2c3d4e5f6...
```

***

## Ports

```yaml
ports:
  http: 8080     # HTTP port (redirects to HTTPS)
  https: 8443    # HTTPS port
```

**Environment variables:**

```bash
HTTP_PORT=8080
HTTPS_PORT=8443
```

***

## Deployment Mode

Controls path generation for different deployment topologies:

```yaml
# Default (downstream) - Client → Firewall → Registry
# Generates API paths for package manager clients
# No config_mode needed

# Upstream mode - Registry → Firewall → Public
# Generates direct paths for registry-to-registry communication
config_mode: upstream

# Middle mode - Registry → Firewall → Registry
# Generates both API and direct paths for multi-tier registries
config_mode: middle
```

| Mode       | Use When                        | Paths Generated | URL Rewriting |
| ---------- | ------------------------------- | --------------- | ------------- |
| (default)  | Client → FW → Registry          | API paths       | Yes           |
| `upstream` | Private Registry → FW → Public  | Direct paths    | Yes           |
| `middle`   | Private Registry → FW → Private | Both API+Direct | No (proxy)    |

**Environment variable:**

```bash
CONFIG_MODE=upstream  # or 'middle'
```

***

***

## Path-Based Routing

All registries behind a single domain with path prefixes. Recommended for most deployments.

```yaml
path_routing:
  enabled: true
  domain: firewall.company.com
  
  routes:
    - path: /npm
      upstream: https://registry.npmjs.org
      registry: npm
      mode: rewrite  # 'rewrite' (default) or 'proxy'
      
    - path: /pypi
      upstream: https://pypi.org
      registry: pypi
      mode: rewrite
      
    - path: /maven
      upstream: https://repo1.maven.org/maven2
      registry: maven
      
    - path: /cargo
      upstream: https://index.crates.io
      registry: cargo
      
    - path: /rubygems
      upstream: https://rubygems.org
      registry: rubygems
      
    - path: /openvsx
      upstream: https://open-vsx.org
      registry: openvsx
      
    - path: /nuget
      upstream: https://api.nuget.org
      registry: nuget
      
    - path: /go
      upstream: https://proxy.golang.org
      registry: go
      
    - path: /conda
      upstream: https://repo.anaconda.com/pkgs/main
      registry: conda
```

### URL Rewrite Scheme

Control the URL scheme used when rewriting metadata URLs.

```yaml
path_routing:
  enabled: true
  domain: firewall.company.com
  rewrite_scheme: https            # Scheme for upstream connections (default: https)
  client_rewrite_scheme: http      # Scheme for client-facing URLs (optional)
```

| Field                   | Default                    | Description                                            |
| ----------------------- | -------------------------- | ------------------------------------------------------ |
| `rewrite_scheme`        | `https`                    | Scheme used for upstream connections and URL rewriting |
| `client_rewrite_scheme` | (same as `rewrite_scheme`) | Scheme used in rewritten URLs returned to clients      |

**Use case:** When the firewall terminates SSL but clients connect via HTTP:

```yaml
path_routing:
  rewrite_scheme: https             # Upstream connections use HTTPS
  client_rewrite_scheme: http       # Rewritten URLs use HTTP for clients
```

The firewall also respects `X-Forwarded-Proto` and `X-Forwarded-Scheme` headers as fallbacks when `rewrite_scheme` is not set.

**Environment variables:**

```bash
PATH_ROUTING_REWRITE_SCHEME=https
PATH_ROUTING_CLIENT_REWRITE_SCHEME=http
```

***

### Route Options

| Field      | Required | Description                           | Values                       |
| ---------- | -------- | ------------------------------------- | ---------------------------- |
| `path`     | Yes      | URL path prefix (must start with `/`) | `/npm`, `/pypi`, etc.        |
| `upstream` | Yes      | Upstream registry URL                 | HTTPS URL                    |
| `registry` | Yes      | Registry type/ecosystem               | npm, pypi, maven, etc.       |
| `mode`     | No       | URL rewriting mode                    | `rewrite` (default), `proxy` |

### Route Mode: rewrite vs proxy

**`mode: rewrite` (default)** - Rewrites package URLs to point back through the firewall:

* Use for: Downstream, Upstream deployments
* URL in metadata → `https://firewall.company.com/npm/package.tgz`
* Clients fetch packages through firewall

**`mode: proxy`** - Passes URLs through unchanged:

* Use for: Middle deployments (Registry → FW → Registry)
* URL in metadata → `../../packages/package.tgz` (relative) or original upstream URL
* Downstream registry resolves relative URLs
* Required when using `config_mode: middle`

***

## External Routes File

For 50+ routes or dynamic route management, use an external file:

```yaml
path_routing:
  enabled: true
  domain: firewall.company.com
  routes_file: /config/routes.yml
```

**routes.yml format:**

```yaml
routes:
  - path: /npm-public
    upstream: https://registry.npmjs.org
    registry: npm
  - path: /npm-internal
    upstream: https://nexus.company.com/repository/npm-internal
    registry: npm
  # ... many more routes
```

Mount the routes file:

```yaml
volumes:
  - ./routes.yml:/config/routes.yml:ro
```

***

## Auto-Discovery (Artifactory/Nexus)

Automatically sync routes from your artifact manager. Routes update on interval without restarting the firewall!

```yaml
path_routing:
  enabled: true
  domain: firewall.company.com
  mode: artifactory  # or 'nexus'
  
  private_registry:
    api_url: https://artifactory.company.com/artifactory
    api_key: your-artifactory-api-key    # Token auth (takes precedence)
    # OR use basic auth with separate fields:
    username: admin                      # Basic auth username
    password: secret                     # Basic auth password
    interval: 5m                         # Auto-sync interval (e.g., 30s, 5m, 1h)
    ignore_ssl_errors: false             # Disable verification of SSL when connecting to the Private Registry
    include_pattern: ".*"                 # Include all repos (default)
    exclude_pattern: "(tmp|test)-.*"      # Exclude temp/test repos
    supported_ecosystems_only: true      # Skip unsupported package types (default: true)
```

### Artifactory Auto-Discovery

Discovers repositories in Artifactory and creates firewall routes automatically.

**Supported repository types:**

* npm
* pypi
* maven
* cargo
* rubygems
* nuget
* go
* conda (experimental support)

**Example discovered routes:**

```
/npm-public       → https://registry.npmjs.org
/pypi-public      → https://pypi.org
/maven-central    → https://repo1.maven.org/maven2
/cargo-crates     → https://index.crates.io
```

### Nexus Auto-Discovery

Discovers proxy, group, and hosted repositories in Nexus and creates firewall routes automatically.

```yaml
path_routing:
  mode: nexus
  private_registry:
    api_url: https://nexus.company.com
    api_key: your-nexus-api-token
    interval: 5m
```

**Supported repository formats:**

* npm
* pypi
* maven2
* cargo
* rubygems
* nuget
* go
* conda

**Route naming:** Routes are named after the repository name in Nexus (e.g., `/npm-proxy`, `/pypi-proxy`)

### Auto-Discovery Configuration Options

All auto-discovery settings are configured in `socket.yml` under `path_routing.private_registry`:

```yaml
private_registry:
  api_url: https://artifactory.company.com    # Repository manager base URL (required)
  api_key: your-api-key                       # API key/token (takes precedence)
  # OR use basic auth with separate fields:
  username: admin                              # Basic auth username
  password: secret                             # Basic auth password
  interval: 5m                                # Sync interval (default: 5m)
  ignore_ssl_errors: false                    # Disable SSL cert verification (default: false)
  include_pattern: ".*"                        # Regex to include repos (default: all)
  exclude_pattern: "(tmp|test)-.*"             # Regex to exclude repos (default: none)
  supported_ecosystems_only: true             # Skip unsupported package types (default: true)
```

The `api_key` can also be provided via the `PRIVATE_REGISTRY_KEY` environment variable.

**Authentication priority:** `api_key` (or `PRIVATE_REGISTRY_KEY` env var) takes precedence. If `api_key` is not set, `username` and `password` are combined as `username:password` for basic auth.

***

***

## Domain-Based Routing

Each registry gets its own subdomain. Requires multiple DNS records (or wildcard DNS) and certificates (or wildcard cert).

```yaml
registries:
  npm:
    domains: [npm.company.com]
    upstream: https://registry.npmjs.org  # Optional - defaults to public registry
    
  pypi:
    domains: [pypi.company.com, python.company.com]  # Multiple domains supported
    upstream: https://pypi.org
    
  maven:
    domains: [maven.company.com]
    
  cargo:
    domains: [cargo.company.com]
    
  rubygems:
    domains: [rubygems.company.com]
    
  openvsx:
    domains: [vsx.company.com]
    
  nuget:
    domains: [nuget.company.com]
    
  go:
    domains: [go.company.com]
    
  conda:
    domains: [conda.company.com]
```

**Client usage:**

```bash
npm config set registry https://npm.company.com/
pip config set global.index-url https://pypi.company.com/simple
```

**DNS requirements:**\
Each domain needs an A or CNAME record pointing to the firewall host.

**SSL requirements:**\
Either provide individual certs for each domain, or use a wildcard cert (`*.company.com`).

***

## Caching

### Local In-Memory Cache (Default)

```yaml
cache:
  ttl: 600  # Freshness window in seconds (10 minutes default)
```

Cached results are stored in nginx shared memory. Fresh for `ttl` seconds, then becomes stale but is retained for revalidation.

**Environment variable:**

```bash
SOCKET_CACHE_TTL=600
```

### Redis Cache (Distributed)

For multi-instance deployments or persistent caching across restarts:

```yaml
redis:
  enabled: true
  host: redis.company.com
  port: 6379
  password: your-redis-password  # Optional
  db: 0  # Redis database number (default: 0)
  ttl: 86400   # Stale window in seconds (24 hours default)
  
  # SSL/TLS settings
  ssl: true
  ssl_verify: true
  ssl_ca_cert: /path/to/redis-ca.pem
  ssl_client_cert: /path/to/client-cert.pem  # For mTLS
  ssl_client_key: /path/to/client-key.pem   # For mTLS
  ssl_server_name: redis.company.com  # SNI hostname
```

**Stale-while-revalidate behavior:**

* **Fresh zone** (0 to `cache.ttl` seconds): Return cached value immediately
* **Stale zone** (`cache.ttl` to `redis.ttl` seconds): Revalidate with Socket API, fallback to stale on error
* **Expired** (after `redis.ttl`): Key removed by Redis, fetch fresh from Socket API

**Environment variables:**

```bash
REDIS_ENABLED=true
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=secret
REDIS_DB=0
REDIS_TTL=86400
REDIS_SSL=true
REDIS_SSL_VERIFY=true
```

***

## Nginx Performance

```yaml
nginx:
  worker_processes: 2        # Number of worker processes (match CPU cores)
  worker_connections: 4096   # Max concurrent connections per worker
```

### Resource-Based Recommendations

| Resources        | worker\_processes | worker\_connections | Est. Throughput |
| ---------------- | ----------------- | ------------------- | --------------- |
| 1 CPU / 1 GB RAM | 1                 | 512                 | \~30 req/s      |
| 2 CPU / 2 GB RAM | 2                 | 1024                | \~60 req/s      |
| 4 CPU / 4 GB RAM | 4                 | 4096                | \~100 req/s     |
| 8 CPU / 8 GB RAM | 8                 | 8192                | \~170 req/s     |
| 16 CPU / 16 GB   | 16                | 16384               | \~300 req/s     |

**Environment variables:**

```bash
WORKER_PROCESSES=2
WORKER_CONNECTIONS=4096
```

***

## Proxy Timeouts

Configure timeouts for upstream registry connections:

```yaml
proxy:
  connect_timeout: 60  # Seconds to establish connection
  send_timeout: 60     # Seconds to send request
  read_timeout: 60     # Seconds to read response
  
  # Buffer sizes (advanced)
  buffer_size: 4k      # Initial buffer for response headers
  buffers_count: 8     # Number of buffers for response body
  buffers_size: 4k     # Size of each buffer
  busy_buffers_size: 8k  # Buffers that can be sent to client while reading
```

**For large packages (e.g., Maven artifacts > 100MB):**

```yaml
proxy:
  connect_timeout: 120
  send_timeout: 300
  read_timeout: 300
```

**Environment variables:**

```bash
PROXY_CONNECT_TIMEOUT=60
PROXY_SEND_TIMEOUT=60
PROXY_READ_TIMEOUT=60
```

***

***

## Metadata Filtering

> **Requires version 1.1.108 or higher.**

Remove blocked or warned package versions from registry metadata responses before clients see them, preventing installation attempts of unsafe packages entirely. Supports all 9 ecosystems with ecosystem-appropriate filtering granularity.

```yaml
metadata_filtering:
  enabled: true
  filter_blocked: true              # Remove blocked/error packages from metadata
  filter_warn: false                # Keep warned packages visible (show warnings only)
  include_unchecked_versions: true  # Include versions not yet checked by Socket (default: true)
  max_versions: 100                 # Max versions to check per package (default: 100, newest first)
  cache_ttl: 3600                   # Cache TTL for metadata PURL lookups (default: 3600s = 1 hour)
  batch_size: 4000                  # Max PURLs per batch (Socket API limit ~4K)
```

### Options

| Field                        | Default | Description                                                                 |
| ---------------------------- | ------- | --------------------------------------------------------------------------- |
| `enabled`                    | `false` | Enable metadata filtering                                                   |
| `filter_blocked`             | `true`  | Remove packages with `block` or `error` actions from metadata               |
| `filter_warn`                | `false` | Remove packages with `warn` actions from metadata                           |
| `include_unchecked_versions` | `true`  | Keep versions not yet scanned by Socket (`false` = strict security posture) |
| `max_versions`               | `100`   | Max versions to check per package (newest first; older versions kept as-is) |
| `cache_ttl`                  | `3600`  | Cache TTL in seconds for metadata PURL lookups (separate from download TTL) |
| `batch_size`                 | `4000`  | Max PURLs per Socket API batch call (\~4K API limit)                        |

### How It Works

1. Client requests package metadata (e.g., `npm install lodash`, `pip install requests`)
2. Firewall fetches the full metadata response from the upstream registry
3. Extracts all package versions/artifacts and builds [Package URLs (PURLs)](https://github.com/package-url/purl-spec)
4. Calls the Socket API in batches to check security status of each version
5. Removes blocked (and optionally warned) versions from the response
6. Returns sanitized metadata to the client

When filtering is disabled, responses stream through unchanged with no buffering.

### Supported Ecosystems

**Per-artifact filtering** — individual artifacts within a version can be selectively removed:

| Ecosystem | Metadata Format                                        | Notes                                                                     |
| --------- | ------------------------------------------------------ | ------------------------------------------------------------------------- |
| **PyPI**  | HTML (PEP 503) and JSON (PEP 691) `/simple/{package}/` | Filters tar.gz, wheels, eggs, zips independently                          |
| **Maven** | HTML directory listings and `maven-metadata.xml`       | Filters by classifier and extension (e.g., `?classifier=sources&ext=jar`) |

**Per-version filtering** — if any artifact is blocked, the entire version is removed:

| Ecosystem    | Metadata Format                                                 | Notes                                               |
| ------------ | --------------------------------------------------------------- | --------------------------------------------------- |
| **npm**      | Package JSON (`/{package}`)                                     | Filters `versions`, `dist-tags`, and `time` objects |
| **NuGet**    | Registration catalog JSON (`/v3/registration5-gz-semver2/`)     | Removes entries from catalog pages                  |
| **RubyGems** | CompactIndex (`/info/{gem}`) and JSON API (`/api/v1/versions/`) | Line-based and JSON array formats                   |
| **Cargo**    | Sparse index NDJSON (`/{2-chars}/{2-chars}/{crate}`)            | One version per NDJSON line                         |
| **Go**       | `/@v/list` (newline-separated) and `/@latest` (JSON)            | Source-only, no binary artifacts                    |
| **Conda**    | `repodata.json` (`packages` and `packages.conda` objects)       | Uses PyPI PURLs (Socket API fallback)               |
| **OpenVSX**  | Extension detail JSON (`/api/{namespace}/{extension}`)          | Single .vsix per version                            |

### Use Cases

* Prevent accidental installation of malicious or vulnerable packages
* Remove flagged packages from search results and dependency resolution
* Enforce strict security posture by excluding unchecked versions (`include_unchecked_versions: false`)
* Pre-warm the PURL cache from metadata lookups, speeding up subsequent download checks

### Environment Variables

```bash
METADATA_FILTERING_ENABLED=true
METADATA_FILTER_BLOCKED=true
METADATA_FILTER_WARN=false
METADATA_INCLUDE_UNCHECKED_VERSIONS=true
METADATA_MAX_VERSIONS=100
METADATA_CACHE_TTL=3600
METADATA_FILTER_BATCH_SIZE=4000
```

***

## Per-Ecosystem `recentlyPublished` Override

> **Requires version 1.1.134 or higher.**

Control which ecosystems enforce the `recentlyPublished` alert at its API-assigned severity (typically `error`/`block`). For ecosystems **not** in the list, `recentlyPublished` alerts are automatically downgraded from `error`/`block` to `warn`, allowing the package through with a warning instead of blocking it.

This is useful when you want strict `recentlyPublished` enforcement for high-risk ecosystems (e.g., npm) while allowing recently published packages through for lower-risk ecosystems.

```yaml
socket:
  # Enforce recentlyPublished blocking only for npm and pypi;
  # all other ecosystems downgrade recentlyPublished to warn
  recently_published_enabled_ecosystems:
    - npm
    - pypi
```

### Options

| Field                                   | Default      | Description                                                                                                                                                           |
| --------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `recently_published_enabled_ecosystems` | `[]` (empty) | List of ecosystems where `recentlyPublished` alerts are enforced at their API-assigned severity. Ecosystems not listed have `recentlyPublished` downgraded to `warn`. |

### Valid Ecosystem Values

`npm`, `pypi`, `maven`, `cargo`, `rubygems`, `nuget`, `go`, `conda`, `openvsx`

### Behavior

| Configuration                 | Effect                                                                                              |
| ----------------------------- | --------------------------------------------------------------------------------------------------- |
| Empty or omitted              | `recentlyPublished` is downgraded to `warn` for **all** ecosystems (default)                        |
| One or more ecosystems listed | `recentlyPublished` is enforced (blocks) for listed ecosystems; downgraded to `warn` for all others |
| All ecosystems listed         | `recentlyPublished` is enforced (blocks) for every ecosystem                                        |

When a `recentlyPublished` alert is downgraded:

* The package is **allowed** through (not blocked)
* A warning is logged with the original and downgraded action
* The `X-Socket-Warn-Reason` response header includes `recentlyPublished`
* Splunk, webhook, and telemetry events reflect the downgraded `warn` action

### Examples

**Block recentlyPublished only for npm:**

```yaml
socket:
  recently_published_enabled_ecosystems:
    - npm
```

**Block recentlyPublished for npm, pypi, and maven:**

```yaml
socket:
  recently_published_enabled_ecosystems:
    - npm
    - pypi
    - maven
```

**Enforce recentlyPublished for all ecosystems (no downgrade):**

```yaml
socket:
  recently_published_enabled_ecosystems:
    - npm
    - pypi
    - maven
    - cargo
    - rubygems
    - nuget
    - go
    - conda
    - openvsx
```

### Environment Variable

```bash
RECENTLY_PUBLISHED_ENABLED_ECOSYSTEMS=npm,pypi   # Comma-separated list
```

***

## Splunk Integration

Forward security events to Splunk HTTP Event Collector (HEC):

```yaml
splunk:
  enabled: true
  hec_url: https://splunk.company.com:8088/services/collector/event
  hec_token: your-splunk-hec-token
  index: security           # Splunk index name (optional, no default)
  source: socket-firewall   # Splunk source name
  sourcetype: socket:firewall:event  # Splunk sourcetype (default: socket:firewall:event)
  
  # SSL settings
  ssl_verify: true
  ssl_ca_cert: /path/to/splunk-ca.pem
  
  # Event batching
  batch_size: 1            # Events per batch (default: 1)
```

**Event types logged:**

* Package blocks (malicious/supply-chain attacks)
* Package warnings
* API errors
* Cache hits/misses
* Request/response metadata

**Example Splunk event:**

```json
{
  "time": 1709078400,
  "event": {
    "event_type": "package_check",
    "purl": "pkg:npm/malicious-package@1.0.0",
    "decision": "blocked",
    "action": "block",
    "response_code": 403,
    "upstream_status": null,
    "block_source": "download",
    "block_reason": "Known Malware",
    "warn_reason": "",
    "repo": "npm-remote",
    "client_ip": "203.0.113.10",
    "user_agent": "npm/8.19.2",
    "request_id": "abc123xyz",
    "upstream_host": "registry.npmjs.org",
    "source_path": "/repository/npm/malicious-package/-/malicious-package-1.0.0.tgz",
    "cached": false,
    "stale": false,
    "socket_api_response_code": 403,
    "purl_check_latency_ms": 142,
    "private_registry_request_id": "ecb06b92c7f89c93:ecb06b92c7f89c93:0000000000000000:0",
    "reason": "security_policy",
    "alerts": [
      {"type": "knownMalware", "severity": "critical", "category": "security", "action": "error"}
    ],
    "alert_count": 1,
    "blocked_alerts": [
      {"type": "knownMalware", "severity": "critical", "category": "security", "action": "error"}
    ],
    "blocked_alert_count": 1,
    "score": 0.1,
    "versions": {}
  },
  "source": "socket-firewall",
  "sourcetype": "socket:firewall:event"
}
```

**Environment variables:**

```bash
SPLUNK_ENABLED=true
SPLUNK_HEC_URL=https://splunk.company.com:8088/services/collector/event
SPLUNK_HEC_TOKEN=your-token
SPLUNK_SOURCE=socket-firewall
```

***

## Unified Event Fields

All three event systems — **console logging** (`[SOCKET_DECISION]`), **Splunk HEC**, and **Socket telemetry** — share the same core event fields built by a single function. This guarantees consistent observability regardless of which system is consuming the events.

### Core Fields (all systems)

| Field                         | Type           | Description                                                                                              |
| ----------------------------- | -------------- | -------------------------------------------------------------------------------------------------------- |
| `request_id`                  | string         | Unique request identifier for correlation                                                                |
| `purl`                        | string         | Package URL (e.g., `pkg:npm/lodash@4.17.21`)                                                             |
| `decision`                    | string         | `"blocked"` or `"allowed"`                                                                               |
| `action`                      | string         | Overall severity: `"block"`, `"warn"`, `"monitor"`, `"ignore"`                                           |
| `response_code`               | number         | HTTP status code sent to client (e.g., 200 or 403)                                                       |
| `upstream_status`             | number or null | HTTP status from upstream registry (null for blocked packages)                                           |
| `source_path`                 | string         | Request URI path                                                                                         |
| `upstream_host`               | string or null | Upstream registry hostname                                                                               |
| `upstream_path`               | string or null | Upstream registry request path                                                                           |
| `repo`                        | string or null | Route/repository name (from `socket_route_name`)                                                         |
| `client_ip`                   | string         | Client IP address                                                                                        |
| `user_agent`                  | string         | Client User-Agent header                                                                                 |
| `socket_api_response_code`    | number         | Socket API HTTP status (200 allowed, 403 blocked)                                                        |
| `cached`                      | boolean        | Whether result was served from cache                                                                     |
| `stale`                       | boolean        | Whether cached value was stale (revalidation attempted)                                                  |
| `block_source`                | string or null | `"download"` (artifact check) or `"metadata"` (metadata filtering)                                       |
| `block_reason`                | string         | Comma-separated alert titles for block/error alerts                                                      |
| `warn_reason`                 | string         | Comma-separated alert titles for warn alerts                                                             |
| `api_error`                   | string or null | Error message if Socket API call failed                                                                  |
| `purl_check_latency_ms`       | number or null | Milliseconds to check package via Socket API                                                             |
| `private_registry_request_id` | string or null | Trace/request ID from private registry (Jaeger `uber-trace-id` or `X-Request-Id` from Artifactory/Nexus) |

### Platform-Specific Fields

**Splunk HEC** adds these fields on top of the core:

| Field                 | Type   | Description                                                                  |
| --------------------- | ------ | ---------------------------------------------------------------------------- |
| `event_type`          | string | Always `"package_check"`                                                     |
| `reason`              | string | Result reason string from Socket API                                         |
| `alerts`              | array  | Structured array of alert objects (`type`, `severity`, `category`, `action`) |
| `alert_count`         | number | Total number of alerts                                                       |
| `blocked_alerts`      | array  | Structured array of blocked/error alert objects                              |
| `blocked_alert_count` | number | Number of blocked/error alerts                                               |
| `score`               | number | Package security score                                                       |
| `versions`            | object | Component versions from `.versions` file                                     |

**Socket telemetry** adds these fields on top of the core:

| Field                     | Type   | Description                                   |
| ------------------------- | ------ | --------------------------------------------- |
| `input_purl`              | string | Decoded PURL sent for readability             |
| `event_sender_created_at` | string | HTTP date timestamp                           |
| `socket_client_version`   | string | Socket client library version                 |
| `event_type`              | string | Always `"firewall_package_encountered"`       |
| `event_category`          | string | Always `"proactive"`                          |
| `registryFqdn`            | string | Registry hostname from request                |
| `machine_id`              | string | SHA256-based machine identifier               |
| `parser_name`             | string | Ecosystem parser name                         |
| `parser_version`          | string | Ecosystem parser version                      |
| `artifact_purl`           | string | Decoded PURL for the artifact                 |
| `alert_action`            | string | Alias for `action`                            |
| `client_action`           | string | Alias for `action`                            |
| `purlCheckLatencyMs`      | number | Alias for `purl_check_latency_ms` (camelCase) |
| `versions`                | object | Component versions from `.versions` file      |

**SOCKET\_DECISION** (`[SOCKET_DECISION]` JSON log line) includes the core fields plus:

| Field            | Type   | Description                                     |
| ---------------- | ------ | ----------------------------------------------- |
| `monitor_reason` | string | Comma-separated alert titles for monitor alerts |

***

## Webhook Events

Send package decision events to any HTTP endpoint. Useful for custom dashboards, alerting systems, or SIEM integrations beyond Splunk.

```yaml
webhook:
  enabled: true
  url: https://siem.company.com/api/events
  auth_header: "Bearer your-api-token"  # Authorization header (optional)
  ssl_verify: false                     # Verify TLS certificate (default: false)
  timeout: 5000                         # Request timeout in ms (default: 5000)
  on_block: true                        # Fire on block decisions (default: true)
  on_warn: true                         # Fire on warn decisions (default: true)
  on_monitor: true                      # Fire on monitor decisions (default: true)
  on_ignore: true                       # Fire on ignore decisions (default: true)
```

| Field         | Default | Description                                     |
| ------------- | ------- | ----------------------------------------------- |
| `enabled`     | `false` | Enable webhook event delivery                   |
| `url`         | (none)  | Webhook endpoint URL (required when enabled)    |
| `auth_header` | (none)  | Value for the `Authorization` header (optional) |
| `ssl_verify`  | `false` | Verify TLS certificate of webhook endpoint      |
| `timeout`     | `5000`  | HTTP request timeout in milliseconds            |
| `on_block`    | `true`  | Send events for blocked packages                |
| `on_warn`     | `true`  | Send events for warned packages                 |
| `on_monitor`  | `true`  | Send events for monitored packages              |
| `on_ignore`   | `true`  | Send events for ignored packages                |

Events are delivered asynchronously (non-blocking) and include all core event fields:

```json
{
  "event_type": "package_decision",
  "timestamp": 1709078400.123,
  "request_id": "abc123xyz",
  "purl": "pkg:npm/malicious-package@1.0.0",
  "decision": "blocked",
  "action": "block",
  "response_code": 403,
  "upstream_status": null,
  "block_source": "download",
  "block_reason": "Known Malware",
  "warn_reason": "",
  "client_ip": "203.0.113.10",
  "user_agent": "npm/8.19.2",
  "repo": "npm-remote",
  "source_path": "/repository/npm/malicious-package/-/malicious-package-1.0.0.tgz",
  "upstream_host": "registry.npmjs.org",
  "cached": false,
  "stale": false,
  "socket_api_response_code": 403,
  "purl_check_latency_ms": 142,
  "private_registry_request_id": "ecb06b92c7f89c93:ecb06b92c7f89c93:0000000000000000:0"
}
```

**Environment variables:**

```bash
WEBHOOK_ENABLED=true
WEBHOOK_URL=https://siem.company.com/api/events
WEBHOOK_AUTH_HEADER="Bearer your-api-token"
WEBHOOK_SSL_VERIFY=false
WEBHOOK_TIMEOUT=5000
WEBHOOK_ON_BLOCK=true
WEBHOOK_ON_WARN=true
WEBHOOK_ON_MONITOR=true
WEBHOOK_ON_IGNORE=true
```

***

## Log Level

Controls which messages appear in console output. The default level is `info`, which shows all security decisions. Splunk HEC events, Socket telemetry events, and webhook deliveries are **always sent** regardless of log level — this setting only affects console (stderr) output.

```yaml
socket:
  log_level: info  # error, warn, info (default), debug
```

| Level   | Console Output                                                                       |
| ------- | ------------------------------------------------------------------------------------ |
| `error` | Only block/error decisions (`[SOCKET_DECISION]` at ERR level)                        |
| `warn`  | Block/error + warn decisions                                                         |
| `info`  | All decisions including monitor/ignore (default)                                     |
| `debug` | All decisions + verbose debug traces (automatically enables `debug_logging_enabled`) |

### SOCKET\_DECISION Log Level Mapping

Each security decision action maps to a specific log level:

| Action          | Log Level | When Visible                         |
| --------------- | --------- | ------------------------------------ |
| `block`/`error` | ERR       | Always (all log levels)              |
| `warn`          | WARN      | `log_level: warn` or lower           |
| `monitor`       | INFO      | `log_level: info` or lower (default) |
| `ignore`        | INFO      | `log_level: info` or lower (default) |

### Integration with Debug Logging

Setting `log_level: debug` automatically enables `debug_logging_enabled`, which provides verbose HTTP request/response header logging. You can also enable debug logging independently via `socket.debug_logging_enabled: true` without changing the log level.

**Environment variable:**

```bash
SOCKET_LOG_LEVEL=info  # error, warn, info (default), debug
```

***

## Debug Logging

Enable verbose request/response header logging for troubleshooting. Disabled by default.

```yaml
socket:
  debug_logging_enabled: false              # Enable debug logging (default: false)
  debug_user_agent_filter: "*artifactory*"  # Glob pattern to match user-agents (optional)
```

| Field                     | Default | Description                                                      |
| ------------------------- | ------- | ---------------------------------------------------------------- |
| `debug_logging_enabled`   | `false` | Enable verbose HTTP header logging                               |
| `debug_user_agent_filter` | (none)  | Glob pattern to limit debug logging to matching user-agents only |

When `debug_user_agent_filter` is set, only requests whose `User-Agent` header matches the glob pattern will produce debug log output. The match is case-insensitive. Standard glob syntax is supported (`*` matches any characters, `?` matches a single character).

**Examples:**

```yaml
# Log all requests
socket:
  debug_logging_enabled: true

# Log only Artifactory traffic
socket:
  debug_logging_enabled: true
  debug_user_agent_filter: "*artifactory*"

# Log only npm client traffic  
socket:
  debug_logging_enabled: true
  debug_user_agent_filter: "npm/*"
```

**Environment variables:**

```bash
SOCKET_DEBUG_LOGGING_ENABLED=true
SOCKET_DEBUG_USER_AGENT_FILTER="*artifactory*"
```

***

## Health Check Logging

The firewall exposes a `/health` endpoint on every server block (default, per-registry, and path-routing). Health check requests are **automatically excluded from console output** to prevent log noise from load balancers and Kubernetes probes.

### What is suppressed

| Log source                    | Suppressed? | How                                                         |
| ----------------------------- | ----------- | ----------------------------------------------------------- |
| nginx access log              | Yes         | `access_log off;` on every `/health` location block         |
| Debug logging (`[DEBUG]`)     | Yes         | `should_debug_log()` returns `false` for `/health` requests |
| Splunk HEC / Socket telemetry | N/A         | Health checks do not trigger security decisions             |

### Health check response

```
GET /health HTTP/1.1

HTTP/1.1 200 OK
Content-Type: text/plain
Server: SocketFirewall/1.2.3

SocketFirewall/1.2.3 - Health OK
```

Per-registry and path-routing health endpoints include additional context:

```
SocketFirewall/1.2.3 - Health OK - npm (npm.company.com)
SocketFirewall/1.2.3 - Health OK - path-routing (firewall.company.com)
```

No configuration is required — health check log suppression is always active.

***

## Decision Log (SOCKET\_DECISION)

Every package security check emits a `[SOCKET_DECISION]` JSON log entry for audit and observability. These entries appear in the firewall's standard error log.

**Example log entry:**

```
[error] [REQUEST_ID: abc123] [SOCKET_DECISION] {"request_id":"abc123","purl":"pkg:npm/malicious-package@1.0.0","decision":"blocked","action":"block","response_code":403,"upstream_status":null,"source_path":"/npm/malicious-package/-/malicious-package-1.0.0.tgz","upstream_host":"registry.npmjs.org","repo":"npm","client_ip":"10.0.0.5","socket_api_response_code":200,"cached":false,"stale":false,"block_source":"download","block_reason":"malware,typosquat","warn_reason":"","api_error":null}
```

### Decision Log Fields

| Field                         | Type        | Description                                                                |
| ----------------------------- | ----------- | -------------------------------------------------------------------------- |
| `request_id`                  | string      | Unique request identifier                                                  |
| `purl`                        | string      | Package URL (decoded, e.g., `pkg:npm/lodash@4.17.21`)                      |
| `decision`                    | string      | `"allowed"` or `"blocked"`                                                 |
| `action`                      | string      | Overall severity: `block`, `warn`, `monitor`, `ignore`, `error`            |
| `response_code`               | number      | HTTP status returned to client (`200` or `403`)                            |
| `upstream_status`             | number/null | HTTP status from upstream registry (null for blocked requests)             |
| `source_path`                 | string      | Request URI path                                                           |
| `upstream_host`               | string/null | Upstream registry hostname                                                 |
| `repo`                        | string/null | Route name (e.g., `npm`, `pypi-remote`)                                    |
| `client_ip`                   | string/null | Client IP address                                                          |
| `socket_api_response_code`    | number      | HTTP status from Socket API response                                       |
| `cached`                      | boolean     | Whether the result was served from cache                                   |
| `stale`                       | boolean     | Whether the cached result was stale (revalidation attempted)               |
| `block_source`                | string/null | `"download"` (artifact check) or `"metadata"` (filtering)                  |
| `block_reason`                | string      | Comma-separated alert titles that caused a block                           |
| `warn_reason`                 | string      | Comma-separated alert titles at warn level                                 |
| `api_error`                   | string/null | Error message if Socket API call failed                                    |
| `private_registry_request_id` | string/null | Trace/request ID from private registry (`uber-trace-id` or `X-Request-Id`) |

### Log Level by Action

| Action               | Log Level | When                                          |
| -------------------- | --------- | --------------------------------------------- |
| `block` / `error`    | ERROR     | Package blocked or API error in fail-closed   |
| `warn`               | WARN      | Package has warn-level alerts (still allowed) |
| `monitor` / `ignore` | NOTICE    | Package allowed with monitor alerts or clean  |

### Filtering Logs

```bash
# All security decisions
docker compose logs socket-firewall | grep SOCKET_DECISION

# Only blocked packages
docker compose logs socket-firewall | grep SOCKET_DECISION | grep '"decision":"blocked"'

# Decisions for a specific package
docker compose logs socket-firewall | grep SOCKET_DECISION | grep 'lodash'

# Metadata filtering decisions
docker compose logs socket-firewall | grep SOCKET_DECISION | grep '"block_source":"metadata"'
```

***

## Access Log Format

The firewall uses a custom access log format that includes timing, upstream, and authentication fields for operational monitoring.

**Log format:**

```
$remote_addr - $remote_user [$time_local] "$request_method $request_uri $server_protocol"
  $status $body_bytes_sent "$http_referer"
  "$http_user_agent" "$http_x_forwarded_for"
  rt=$request_time
  upstream=$upstream_addr us=$upstream_status ut=$upstream_response_time
  auth=$sanitized_authorization
  req=$request_id trace=$sent_http_x_trace_id
```

### Access Log Fields

| Field       | Description                                                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `rt=`       | Total request time in seconds (includes upstream + processing)                                                                   |
| `upstream=` | Upstream server address (IP:port)                                                                                                |
| `us=`       | Upstream HTTP status code                                                                                                        |
| `ut=`       | Upstream response time in seconds                                                                                                |
| `auth=`     | Authorization header (redacted to `[REDACTED]` for security)                                                                     |
| `req=`      | NGINX-generated unique request ID (32-char hex, correlates with `[REQUEST_ID: ...]` in Lua logs)                                 |
| `trace=`    | Upstream registry trace ID (`uber-trace-id` or `X-Request-Id` from upstream response), also sent as `X-Trace-Id` response header |

Query parameters are stripped from logged URIs to prevent sensitive data leakage.

### Access Log Buffering

Control log output buffering with `access_log_buffer`:

```yaml
nginx:
  access_log_buffer: 64k      # Default — buffer 64k before flushing
  # access_log_buffer: off    # Disable buffering (flush every line)
  # access_log_buffer: 256k   # Larger buffer for high-throughput
```

| Value  | Behavior                                                  |
| ------ | --------------------------------------------------------- |
| `64k`  | Default. Buffers up to 64k before flushing to stdout      |
| `off`  | Disables buffering — each log line is written immediately |
| `256k` | Larger buffer for high-throughput deployments             |

Set `access_log_buffer: off` when you need real-time log output (e.g., debugging, streaming to log aggregators).

***

## SSL/TLS Certificates

Certificates are stored in `/etc/nginx/ssl` inside the container. Mount from host:

```yaml
volumes:
  - ./ssl:/etc/nginx/ssl
```

### Required Files

| File                | Purpose                                  | Permissions |
| ------------------- | ---------------------------------------- | ----------- |
| `ssl/fullchain.pem` | Certificate chain (cert + intermediates) | 644         |
| `ssl/privkey.pem`   | Private key                              | 644         |

### Auto-Generated Certificates

The firewall generates self-signed certs on first run if none exist. Located at `/etc/nginx/ssl/`.

### Custom Certificates (Production)

Place your organization's certificates in the `ssl/` directory on the host:

```bash
mkdir -p ssl
cp /path/to/cert.pem ssl/fullchain.pem
cp /path/to/key.pem ssl/privkey.pem
chmod 644 ssl/fullchain.pem ssl/privkey.pem
```

### Generate Self-Signed Certificates

**Single domain:**

```bash
mkdir -p ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/privkey.pem \
  -out ssl/fullchain.pem \
  -subj "/CN=firewall.company.com" \
  -addext "subjectAltName=DNS:firewall.company.com,DNS:localhost"
chmod 644 ssl/fullchain.pem ssl/privkey.pem
```

**Wildcard (multiple subdomains):**

```bash
mkdir -p ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/privkey.pem \
  -out ssl/fullchain.pem \
  -subj "/CN=*.company.com" \
  -addext "subjectAltName=DNS:*.company.com,DNS:company.com,DNS:localhost"
chmod 644 ssl/fullchain.pem ssl/privkey.pem
```

### Trust Self-Signed Certificates

**macOS:**

```bash
sudo security add-trusted-cert -d -r trustRoot \
  -k /Library/Keychains/System.keychain ssl/fullchain.pem
```

**Linux:**

```bash
sudo cp ssl/fullchain.pem /usr/local/share/ca-certificates/socket-firewall.crt
sudo update-ca-certificates
```

**Windows:**

```powershell
Import-Certificate -FilePath ssl\fullchain.pem -CertStoreLocation Cert:\LocalMachine\Root
```

***

***

## Environment Variables Reference

All configuration can be overridden via environment variables. Useful for Docker/Kubernetes deployments.

### Core Settings

```bash
# Required
SOCKET_SECURITY_API_TOKEN=your-api-key        # Socket.dev API key

# Socket API
SOCKET_API_URL=https://api.socket.dev         # Default
SOCKET_FAIL_OPEN=true                         # Allow on API error (default: true)
SOCKET_CACHE_TTL=600                          # Freshness window (seconds)

# Ports
HTTP_PORT=8080                                # HTTP port
HTTPS_PORT=8443                               # HTTPS port

# Deployment mode
CONFIG_MODE=upstream                          # 'upstream' or 'middle'

# SSL verification
SOCKET_API_SSL_VERIFY=false                   # Verify Socket API SSL (default: false)
SOCKET_API_SSL_CA_CERT=/path/to/ca.crt       # Custom Socket API CA
SOCKET_UPSTREAM_SSL_VERIFY=false             # Verify upstream registry SSL (default: false, inherits api_ssl_verify)
SOCKET_UPSTREAM_SSL_CA_CERT=/path/to/ca.crt  # Custom upstream CA

# Corporate proxy
SOCKET_OUTBOUND_PROXY=http://proxy:3128      # Egress proxy
SOCKET_NO_PROXY=localhost,127.0.0.1          # No-proxy exceptions

# Request tracking
SOCKET_REQUEST_ID_HEADER=X-Socket-Request-ID # Request ID header name (default)

# Log level
SOCKET_LOG_LEVEL=info                        # Console log level (error/warn/info/debug)

# Debug logging
SOCKET_DEBUG_LOGGING_ENABLED=false           # Enable debug logging
SOCKET_DEBUG_USER_AGENT_FILTER="*pattern*"   # Glob filter for user-agent
```

### Redis

```bash
REDIS_ENABLED=true                            # Enable Redis
REDIS_HOST=redis.company.com                  # Redis hostname
REDIS_PORT=6379                               # Redis port
REDIS_PASSWORD=secret                         # Redis password
REDIS_DB=0                                    # Redis database number
REDIS_TTL=86400                               # Stale window (seconds)

# Redis SSL
REDIS_SSL=true                                # Enable SSL
REDIS_SSL_VERIFY=true                         # Verify Redis SSL
REDIS_SSL_CA_CERT=/path/to/redis-ca.pem      # Redis CA cert
REDIS_SSL_SERVER_NAME=redis.company.com       # SNI hostname
```

### Nginx Performance

```bash
WORKER_PROCESSES=2                            # nginx worker processes
WORKER_CONNECTIONS=4096                       # Connections per worker
```

### Proxy Timeouts

```bash
PROXY_CONNECT_TIMEOUT=60                      # Connection timeout (seconds)
PROXY_SEND_TIMEOUT=60                         # Send timeout
PROXY_READ_TIMEOUT=60                         # Read timeout
```

### Auto-Discovery

Auto-discovery is configured via `socket.yml` under `path_routing.private_registry` (see above).
The `api_key` can also be provided via the `PRIVATE_REGISTRY_KEY` environment variable.

### Metadata Filtering

```bash
METADATA_FILTERING_ENABLED=true               # Enable filtering (v1.1.108+)
METADATA_FILTER_BLOCKED=true                  # Filter blocked packages
METADATA_FILTER_WARN=false                    # Filter warned packages
METADATA_INCLUDE_UNCHECKED_VERSIONS=true      # Keep unchecked versions
METADATA_MAX_VERSIONS=100                     # Max versions to check per package
METADATA_CACHE_TTL=3600                       # Cache TTL for metadata lookups (seconds)
METADATA_FILTER_BATCH_SIZE=4000               # Max PURLs per batch
```

### Per-Ecosystem Alert Override

```bash
RECENTLY_PUBLISHED_ENABLED_ECOSYSTEMS=npm,pypi  # Enforce recentlyPublished blocking for these ecosystems (v1.1.134+)
```

### Splunk

```bash
SPLUNK_ENABLED=true                           # Enable Splunk
SPLUNK_HEC_URL=https://splunk.company.com:8088/services/collector/event
SPLUNK_HEC_TOKEN=your-hec-token              # Splunk HEC token
SPLUNK_INDEX=security                         # Splunk index (optional)
SPLUNK_SOURCE=socket-firewall                 # Splunk source
SPLUNK_SOURCETYPE=socket:firewall:event       # Splunk sourcetype (default: socket:firewall:event)
SPLUNK_SSL_VERIFY=true                        # Verify Splunk SSL
SPLUNK_BATCH_SIZE=1                           # Events per batch (default: 1)
```

### Webhook

```bash
WEBHOOK_ENABLED=true                          # Enable webhook
WEBHOOK_URL=https://siem.company.com/api/events  # Webhook endpoint URL
WEBHOOK_AUTH_HEADER="Bearer token"             # Authorization header (optional)
WEBHOOK_SSL_VERIFY=false                      # Verify TLS (default: false)
WEBHOOK_TIMEOUT=5000                          # Timeout in ms (default: 5000)
WEBHOOK_ON_BLOCK=true                         # Fire on block (default: true)
WEBHOOK_ON_WARN=true                          # Fire on warn (default: true)
WEBHOOK_ON_MONITOR=true                       # Fire on monitor (default: true)
WEBHOOK_ON_IGNORE=true                        # Fire on ignore (default: true)
```

***

## Docker Compose Examples

### Minimal Configuration

```yaml
services:
  socket-firewall:
    image: socketdev/socket-registry-firewall:latest
    ports:
      - "8080:8080"
      - "8443:8443"
    environment:
      - SOCKET_SECURITY_API_TOKEN=${SOCKET_SECURITY_API_TOKEN}
    volumes:
      - ./socket.yml:/app/socket.yml:ro
      - ./ssl:/etc/nginx/ssl
    restart: unless-stopped
```

### Full Configuration with Redis

```yaml
services:
  socket-firewall:
    image: socketdev/socket-registry-firewall:latest
    ports:
      - "8080:8080"
      - "8443:8443"
    environment:
      # Core
      - SOCKET_SECURITY_API_TOKEN=${SOCKET_SECURITY_API_TOKEN}
      - SOCKET_FAIL_OPEN=true
      - SOCKET_CACHE_TTL=600
      
      # Redis
      - REDIS_ENABLED=true
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - REDIS_PASSWORD=${REDIS_PASSWORD}
      - REDIS_TTL=86400
      
      # Performance
      - WORKER_PROCESSES=4
      - WORKER_CONNECTIONS=8192
      
      # Corporate proxy
      - SOCKET_OUTBOUND_PROXY=http://proxy.company.com:3128
      - SOCKET_NO_PROXY=localhost,127.0.0.1
      
    volumes:
      - ./socket.yml:/app/socket.yml:ro
      - ./ssl:/etc/nginx/ssl
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-fk", "https://localhost:8443/health"]
      interval: 30s
      timeout: 10s
      retries: 3
    depends_on:
      - redis

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis-data:/data
    restart: unless-stopped

volumes:
  redis-data:
```

### With Splunk Integration

```yaml
services:
  socket-firewall:
    image: socketdev/socket-registry-firewall:latest
    ports:
      - "8080:8080"
      - "8443:8443"
    environment:
      - SOCKET_SECURITY_API_TOKEN=${SOCKET_SECURITY_API_TOKEN}
      
      # Splunk
      - SPLUNK_ENABLED=true
      - SPLUNK_HEC_URL=https://splunk.company.com:8088/services/collector/event
      - SPLUNK_HEC_TOKEN=${SPLUNK_HEC_TOKEN}
      - SPLUNK_INDEX=security
      - SPLUNK_SOURCE=socket-firewall
      
    volumes:
      - ./socket.yml:/app/socket.yml:ro
      - ./ssl:/etc/nginx/ssl
    restart: unless-stopped
```

***

## Health Checks

The firewall exposes a health endpoint at `/health`:

```bash
curl -k https://localhost:8443/health
```

**Response:**

```
SocketFirewall/1.1.94 - Health OK - npm (registry.npmjs.org)
```

The response is plain text (`Content-Type: text/plain`) and includes the firewall version, registry name, and domain.

**HTTP status codes:**

* `200 OK` - Firewall is healthy
* `503 Service Unavailable` - Firewall is unhealthy (configuration error)

**Docker healthcheck:**

```yaml
healthcheck:
  test: ["CMD", "curl", "-fk", "https://localhost:8443/health"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 10s
```

***

## Complete Configuration Example

**socket.yml:**

```yaml
# Core Socket settings
socket:
  api_url: https://api.socket.dev
  fail_open: true
  outbound_proxy: http://proxy.company.com:3128
  no_proxy: localhost,127.0.0.1,internal.company.com
  api_ssl_verify: false
  api_ssl_ca_cert: /etc/ssl/certs/corporate-ca.crt
  upstream_ssl_verify: false

# Ports
ports:
  http: 8080
  https: 8443

# Deployment mode
config_mode: upstream

# Path-based routing with auto-discovery
path_routing:
  enabled: true
  domain: socket-firewall.company.com
  mode: artifactory
  
  private_registry:
    api_url: https://artifactory.company.com/artifactory
    api_key: ${ARTIFACTORY_API_KEY}
    interval: 5m
    exclude_pattern: "(tmp|test|snapshot)-.*"

# Caching
cache:
  ttl: 600

redis:
  enabled: true
  host: redis.company.com
  port: 6380
  password: ${REDIS_PASSWORD}
  ttl: 86400
  ssl: true
  ssl_verify: true
  ssl_ca_cert: /etc/redis/ssl/ca-cert.pem

# Performance
nginx:
  worker_processes: 8
  worker_connections: 16384

proxy:
  connect_timeout: 120
  send_timeout: 300
  read_timeout: 300

# Advanced features (v1.1.108+)
metadata_filtering:
  enabled: true
  filter_blocked: true
  filter_warn: false
  include_unchecked_versions: true
  max_versions: 100
  cache_ttl: 3600
  batch_size: 4000

# Per-ecosystem recentlyPublished override (v1.1.134+)
# recently_published_enabled_ecosystems:
#   - npm
#   - pypi

splunk:
  enabled: true
  hec_url: https://splunk.company.com:8088/services/collector/event
  hec_token: ${SPLUNK_HEC_TOKEN}
  index: security
  source: socket-firewall
  sourcetype: socket:firewall:event
  ssl_verify: true
```