# Source: https://docs.socket.dev/docs/nexus-configuration.md

# Nexus Configuration

# Nexus Integration Guide

Complete guide for integrating Socket Registry Firewall with Sonatype Nexus Repository Manager. Supports auto-discovery of proxy, group, and hosted repositories and all three deployment topologies.

## Overview

Socket Registry Firewall integrates with Nexus Repository Manager to protect package ingestion and distribution. The firewall can automatically discover and sync proxy repository configurations from Nexus, eliminating manual route configuration.

**Supported Nexus repository formats:**

* npm
* PyPI
* maven2
* cargo
* rubygems
* nuget
* go
* conda

***

## Deployment Topologies

### 1. Upstream Deployment (Most Common)

Nexus proxy repositories pull packages through the firewall. Developers and CI use Nexus directly.

```
Developer / CI  --->  Nexus  --->  Socket Firewall  --->  Public Registry
                    (caching)                              (npmjs.org, pypi.org)
```

**Benefits:**

* Single enforcement point
* No developer config changes needed
* Nexus caches packages (most installs don't hit firewall)
* Centralized security for entire organization

**Use when:**

* You already have Nexus Repository Manager deployed
* Developers are already configured to use Nexus
* You want to protect package ingestion from public registries

[See Upstream Deployment Setup →](#upstream-deployment-setup)

***

### 2. Downstream Deployment

Developers and CI point at the firewall, which proxies to Nexus (which may host internal packages or proxy to public registries).

```
Developer / CI  --->  Socket Firewall  --->  Nexus  --->  Public/Internal Registry
```

**Benefits:**

* Protect developer workstations directly
* Works with Nexus proxy, group, or hosted repos
* Can layer on top of existing Nexus setup

**Use when:**

* You want to protect specific teams or projects
* You have Nexus hosting internal packages
* You want an additional security layer beyond Nexus

[See Downstream Deployment Setup →](#downstream-deployment-setup)

***

### 3. Middle Deployment (Multi-Tier)

Firewall sits between two Nexus instances (e.g., Development → Production, Regional → Central).

```
Nexus Dev  --->  Socket Firewall  --->  Nexus Production
(Proxy)                                  (Hosted/Proxy)
```

**Benefits:**

* Scan packages flowing between internal registries
* Supports multi-tier Nexus deployments
* Protects internal package distribution

**Use when:**

* You have multiple Nexus instances (Dev/Prod, Regional/Central)
* Packages flow between Nexus instances
* You need to scan internal package distribution

[See Middle Deployment Setup →](#middle-deployment-setup)

***

## Auto-Discovery Configuration

Socket Firewall can automatically discover Nexus proxy, group, and hosted repositories and create firewall routes without manual configuration.

### Basic Auto-Discovery

```yaml
path_routing:
  enabled: true
  domain: socket-firewall.company.com
  mode: nexus
  
  private_registry:
    api_url: https://nexus.company.com
    api_key: your-nexus-api-token  # Or use env var NEXUS_API_TOKEN
    interval: 5m  # Auto-sync every 5 minutes
```

Routes are discovered from Nexus and updated automatically. No need to manually define each route!

### Advanced Auto-Discovery

```yaml
path_routing:
  enabled: true
  domain: socket-firewall.company.com
  mode: nexus
  
  private_registry:
    api_url: https://nexus.company.com
    api_key: your-nexus-api-token        # Token auth (takes precedence)
    # OR use basic auth with separate fields:
    username: admin                      # Basic auth username
    password: secret                     # Basic auth password
    interval: 5m                         # Sync interval (30s, 5m, 1h, etc.)
    ignore_ssl_errors: true              # Disable verification of SSL when connecting to the Private Registry
    include_pattern: "^(npm|pypi|maven)-.*"      # Only npm/pypi/maven repos
    exclude_pattern: "(tmp|test|snapshot)-.*"     # Exclude temp/test repos
    supported_ecosystems_only: true      # Skip unsupported package types (default: true)
```

### How Auto-Discovery Works

1. Firewall calls Nexus REST API: `GET /service/rest/v1/repositories`
2. Filters for `proxy`, `group`, and `hosted` repository types
3. Parses repository list and extracts:
   * Repository name
   * Format (npm, pypi, maven2, etc.)
   * Remote URL
4. Creates firewall routes:
   * Path: `/repository/{repo-name}/` (Nexus-compatible path)
   * Upstream: Remote URL from repository config
   * Registry: Inferred from format
5. Generates nginx configuration with discovered routes
6. Repeats on interval, adding/removing routes as repositories change

### Configuration Options for Auto-Discovery

```yaml
private_registry:
  api_url: https://nexus.company.com        # Nexus base URL (required)
  api_key: your-api-token                   # API token (takes precedence)
  # OR use basic auth with separate fields:
  username: admin                            # Basic auth username
  password: secret                           # Basic auth password
  interval: 5m                              # Sync interval (default: 5m)
  ignore_ssl_errors: true                   # Disable verification of SSL when connecting to the Private Registry (default: false)
  include_pattern: ".*"                      # Regex to include repos (default: all)
  exclude_pattern: "(tmp|test)-.*"           # Regex to exclude repos (default: none)
  supported_ecosystems_only: true           # Skip unsupported package types (default: true)
```

The `api_key` can also be provided via the `PRIVATE_REGISTRY_KEY` environment variable.

**Authentication priority:** `api_key` (or `PRIVATE_REGISTRY_KEY` env var) takes precedence. If `api_key` is not set, `username` and `password` are combined as `username:password` for basic auth.

### Service Account Permissions for Auto-Discovery

Auto-discovery calls the Nexus REST API to list repositories. The service account used for authentication needs **read-only** access to the repository listing endpoint.

**API endpoint used:** `GET /service/rest/v1/repositories`

This endpoint returns the name, format, type, and URL of every repository the authenticated user can see. No write operations are performed — the firewall only reads repository metadata to generate routes.

#### Minimum-Privilege Setup (Recommended)

Create a dedicated service account with the minimum permissions required:

1. **Create a role** in Nexus:
   * Go to **Administration → Security → Roles → Create Role → Nexus Role**
   * **Role ID**: `socket-firewall-discovery`
   * **Role Name**: Socket Firewall Discovery
   * **Privileges**: Add **`nx-repository-view-*-*-browse`** and **`nx-repository-view-*-*-read`**
   * These privileges grant read-only visibility into all repositories. To restrict to specific formats, replace the first wildcard (e.g., `nx-repository-view-npm-*-browse` for npm only)
   * **Save**

2. **Create a local user**:
   * Go to **Administration → Security → Users → Create Local User**
   * **ID**: `socket-firewall`
   * **Status**: Active
   * **Roles**: Assign only `socket-firewall-discovery`
   * **Save**

3. **Generate an API token** (preferred over password):
   * Log in as the new user
   * Go to **Profile → User Token → Access user token**
   * Use the `nameCode:passCode` as `api_key` in `socket.yml`

#### Nexus Privilege Reference

| Privilege                       | Purpose                                      | Required?       |
| ------------------------------- | -------------------------------------------- | --------------- |
| `nx-repository-view-*-*-browse` | Browse repository contents in the UI and API | **Yes**         |
| `nx-repository-view-*-*-read`   | Read repository metadata via REST API        | **Yes**         |
| `nx-repository-view-*-*-edit`   | Modify repository contents                   | No — not needed |
| `nx-repository-admin-*-*-*`     | Repository administration                    | No — not needed |
| `nx-apikey-all`                 | Manage API keys                              | No — not needed |

#### Verifying Permissions

Test that the service account can list repositories:

```bash
# Using token auth (nameCode:passCode)
curl -u "nameCode:passCode" \
  https://nexus.company.com/service/rest/v1/repositories

# Using API token (Bearer)
curl -H "Authorization: Bearer your-token" \
  https://nexus.company.com/service/rest/v1/repositories

# Expected: JSON array of repository objects
# [{"name": "npm-proxy", "format": "npm", "type": "proxy", "url": "..."}, ...]
```

If the response is `403 Forbidden`, the account is missing the `nx-repository-view` privileges. If it returns an empty list, the account may have browse privileges scoped to specific repositories — widen the scope or use wildcard privileges.

***

## Upstream Deployment Setup

Protect package ingestion by pointing Nexus proxy repos at the firewall.

### Step 1: Deploy Socket Firewall

**socket.yml:**

```yaml
socket:
  api_url: https://api.socket.dev

ports:
  http: 8080
  https: 8443

# Upstream mode - generates direct paths for registry-to-registry
config_mode: upstream

path_routing:
  enabled: true
  domain: socket-firewall.internal.company.com
  mode: nexus  # Auto-discovery
  
  private_registry:
    api_url: https://nexus.company.com
    api_key: ${NEXUS_API_KEY}
    interval: 5m
    exclude_pattern: "(tmp|test|snapshot)-.*"

nginx:
  worker_processes: 4
  worker_connections: 8192
```

**docker-compose.yml:**

```yaml
services:
  socket-firewall:
    image: socketdev/socket-registry-firewall:latest
    ports:
      - "8080:8080"
      - "8443:8443"
    environment:
      - SOCKET_SECURITY_API_TOKEN=${SOCKET_SECURITY_API_TOKEN}
      - NEXUS_API_KEY=${NEXUS_API_KEY}
    volumes:
      - ./socket.yml:/app/socket.yml:ro
      - ./ssl:/etc/nginx/ssl
    restart: unless-stopped
```

**Start:**

```bash
docker compose up -d
curl -k https://socket-firewall.internal.company.com:8443/health
```

### Step 2: Configure Nexus Proxy Repositories

Point each Nexus proxy repository to the firewall instead of the public registry.

#### npm Proxy Repository

1. Go to **Administration → Repository → Repositories**
2. Click on your npm proxy repository (e.g., `npm-proxy`)
3. Under **Proxy**, change **Remote storage** URL from `https://registry.npmjs.org` to:
   ```
   https://socket-firewall.internal.company.com:8443/npm
   ```
4. Under **HTTP** (if using self-signed certs):
   * Uncheck **Block outbound connections on unproxied ports**
   * Select **Allow** or add exception for firewall
5. **Save**

#### PyPI Proxy Repository

1. Click on your PyPI proxy repository (e.g., `pypi-proxy`)
2. Change **Remote storage** URL to:
   ```
   https://socket-firewall.internal.company.com:8443/pypi
   ```
3. **Save**

#### Maven Proxy Repository

1. Click on your Maven proxy repository (e.g., `maven-central`)
2. Change **Remote storage** URL to:
   ```
   https://socket-firewall.internal.company.com:8443/maven
   ```
3. Under **Storage**:
   * **Version policy**: Release (or Mixed if needed)
   * **Layout policy**: Permissive (recommended)
4. **Save**

#### Other Ecosystems

Repeat for other formats using corresponding paths:

* Cargo: `https://socket-firewall.internal.company.com:8443/cargo`
* RubyGems: `https://socket-firewall.internal.company.com:8443/rubygems`
* NuGet: `https://socket-firewall.internal.company.com:8443/nuget`
* Go: `https://socket-firewall.internal.company.com:8443/go`
* Conda: `https://socket-firewall.internal.company.com:8443/conda`

### Step 3: Disable SSL Verification (Self-Signed Certs Only)

If using self-signed certificates, configure Nexus to trust them:

**Option 1 - Disable SSL verification per repository (testing only):**

1. Edit proxy repository
2. Under **HTTP**, check **Block fetching over HTTP**
3. Uncheck **Verify TLS/SSL certificate** (or add exception)

**Option 2 - Add firewall CA to Nexus trust store (recommended):**

```bash
# Copy firewall cert to Nexus server
scp ssl/fullchain.pem nexus-server:/tmp/socket-firewall.crt

# Add to Java trust store (Nexus runs on JVM)
keytool -import -alias socket-firewall \
  -keystore /path/to/nexus/jre/lib/security/cacerts \
  -file /tmp/socket-firewall.crt \
  -storepass changeit

# Restart Nexus
systemctl restart nexus
```

### Step 4: Test

**Test npm:**

```bash
# Developers use Nexus as normal
npm config set registry https://nexus.company.com/repository/npm-proxy/
npm install lodash

# Check firewall logs
docker compose logs socket-firewall | grep lodash
```

**Test PyPI:**

```bash
pip config set global.index-url https://nexus.company.com/repository/pypi-proxy/simple
pip install requests

docker compose logs socket-firewall | grep requests
```

### Step 5: Verify Auto-Discovery

Check that the firewall discovered your Nexus repositories:

```bash
# View discovered routes
docker compose exec socket-firewall cat /app/discovered-routes.yml

# Check logs for discovery events
docker compose logs socket-firewall | grep "Discovered.*repositories"
```

***

## Downstream Deployment Setup

Developers point at the firewall, which proxies to Nexus.

**socket.yml:**

```yaml
socket:
  api_url: https://api.socket.dev

ports:
  http: 8080
  https: 8443

# Default mode (downstream) - generates API paths for clients

path_routing:
  enabled: true
  domain: firewall.company.com
  
  routes:
    # Point to Nexus group or proxy repos
    - path: /npm
      upstream: https://nexus.company.com/repository/npm-group
      registry: npm
      
    - path: /pypi
      upstream: https://nexus.company.com/repository/pypi-group
      registry: pypi
```

**Client configuration:**

```bash
# Developers point at firewall instead of Nexus
npm config set registry https://firewall.company.com/npm/
pip config set global.index-url https://firewall.company.com/pypi/simple
```

***

## Middle Deployment Setup

Firewall sits between two Nexus instances.

**socket.yml:**

```yaml
socket:
  api_url: https://api.socket.dev

ports:
  http: 8080
  https: 8443

# Middle mode - generates both API and direct paths, no URL rewriting
config_mode: middle

path_routing:
  enabled: true
  domain: socket-firewall.internal.company.com
  
  routes:
    # Dev Nexus proxy → Prod Nexus proxy
    - path: /pypi
      upstream: https://nexus-prod.company.com/repository/pypi-proxy
      registry: pypi
      mode: proxy  # IMPORTANT - passes URLs unchanged
      
    - path: /npm
      upstream: https://nexus-prod.company.com/repository/npm-proxy
      registry: npm
      mode: proxy
```

**Dev Nexus Configuration:**

1. Create proxy repository in Dev Nexus
2. Set Remote storage URL to firewall:
   * Remote URL: `https://socket-firewall.internal.company.com:8443/pypi`
3. Developers use Dev Nexus

**Why `mode: proxy` is required:**

* Production Nexus returns relative URLs like `../../packages/xyz/file.tar.gz`
* `mode: proxy` passes these URLs through unchanged
* Dev Nexus resolves relative URLs against its own base path
* `mode: rewrite` would break this by rewriting URLs to firewall paths

***

## Nexus Authentication

### Generate API Token

1. Log in to Nexus web UI as admin
2. Click profile icon (top right) → **User Token**
3. Click **Access user token**
4. Enter admin password
5. Copy the **Name Code** (username) and **Pass Code** (password)
6. Use as API key: `Name Code:Pass Code` (base64 encoded)

Or use the REST API:

```bash
# Get user token
curl -u admin:admin123 -X GET \
  https://nexus.company.com/service/rest/v1/security/user-token

# Returns:
# {
#   "nameCode": "abc123",
#   "passCode": "xyz789"
# }

# Use in firewall config as: abc123:xyz789
```

### Using Basic Auth

You can authenticate with basic auth using separate `username` and `password` fields:

```yaml
private_registry:
  api_url: https://nexus.company.com
  username: admin
  password: admin123
```

Alternatively, you can combine them in the `api_key` field:

```yaml
private_registry:
  api_url: https://nexus.company.com
  api_key: admin:admin123   # username:password format
```

**Authentication priority:** `api_key` (or `PRIVATE_REGISTRY_KEY` env var) takes precedence over `username`/`password`.

**Security recommendation**: Use API token instead of password for automation.

***

## Troubleshooting

### Nexus Can't Reach Firewall

**Symptom:** Nexus shows "Remote Unavailable" errors in repository health checks

**Check:**

```bash
# From Nexus server, test connectivity
curl -k https://socket-firewall.internal.company.com:8443/health

# Check DNS resolution
nslookup socket-firewall.internal.company.com

# Test HTTP connectivity
curl -v -k https://socket-firewall.internal.company.com:8443/npm/lodash
```

**Solution:**

* Verify DNS record points to firewall host
* Ensure firewall ports (8080/8443) are accessible from Nexus
* Check firewall rules/security groups
* Verify no corporate proxy is interfering

### SSL Certificate Errors

**Symptom:** Nexus logs show SSL handshake failures or certificate errors

**Option 1 - Add firewall cert to Nexus Java trust store:**

```bash
# Find Nexus Java home
ls -la /opt/sonatype/nexus/jre  # or check JAVA_HOME

# Import cert
keytool -import -alias socket-firewall \
  -keystore /opt/sonatype/nexus/jre/lib/security/cacerts \
  -file /path/to/fullchain.pem \
  -storepass changeit

# Restart Nexus
systemctl restart nexus
```

**Option 2 - Disable SSL verification (testing only):**

* In proxy repository settings, uncheck "Verify TLS/SSL certificate"

### Auto-Discovery Not Finding Repositories

**Check Nexus API access:**

```bash
# Test API connectivity
curl -u admin:admin123 \
  https://nexus.company.com/service/rest/v1/repositories

# Should return JSON list of repositories
```

**Check firewall logs:**

```bash
docker compose logs socket-firewall | grep -i discovery
docker compose logs socket-firewall | grep -i nexus
```

**Common issues:**

* API token/credentials incorrect
* User lacks permissions (needs admin or role with repository read access)
* `api_url` incorrect (should be base Nexus URL, not including `/service/rest`)
* Network connectivity from firewall to Nexus

### Empty Package Lists

**Symptom:** `npm search` or `pip search` returns empty results through Nexus

**Cause:** Nexus metadata cache not populated yet

**Solution:**

1. Trigger initial metadata download in Nexus:
   * Go to **Administration → Repository → Repositories → (your proxy repo)**
   * Click **Rebuild Index** or wait for scheduled task
2. Wait for Nexus to fetch and cache metadata (can take several minutes for npm/pypi)
3. Retry search

### Maven Artifacts Not Found

**Symptom:** Maven builds fail to find artifacts from Nexus proxy

**Check Nexus maven proxy settings:**

1. **Version policy**: Set to "Mixed" (or "Release" for central)
2. **Layout policy**: Set to "Permissive"
3. **Content Disposition**: Set to "Inline"

**Check firewall logs:**

```bash
docker compose logs socket-firewall | grep maven
docker compose logs socket-firewall | grep -i error
```

### Package Downloads Slow

**Symptom:** Package installs through Nexus → Firewall are slower than expected

**Optimization steps:**

1. **Check Nexus blob store** - Ensure adequate disk space for caching
2. **Tune Nexus cache** - Increase negative cache TTL in proxy repo settings
3. **Enable firewall Redis cache**:
   ```yaml
   redis:
     enabled: true
     host: redis
     ttl: 86400
   ```
4. **Increase firewall workers**:
   ```yaml
   nginx:
     worker_processes: 8
     worker_connections: 16384
   ```

***

## Best Practices

### Repository Naming

Use consistent naming in Nexus to simplify filtering:

* `npm-proxy` - Proxy to public npm registry
* `npm-hosted` - Internal npm packages
* `npm-group` - Group combining proxy + hosted
* `pypi-proxy` - Proxy to public PyPI
* `pypi-hosted` - Internal Python packages

Then use filters in firewall:

```yaml
include_pattern: ".*-proxy"   # Only protect proxy repos
exclude_pattern: ".*-hosted"  # Don't scan internal packages
```

### Caching Strategy

**Nexus caching + Firewall caching = Maximum efficiency:**

1. Nexus caches packages after first fetch
2. Firewall caches security results for 24h (default)
3. Subsequent installs hit Nexus cache (never reach firewall)
4. New packages hit firewall once, then cached by both

**Result:** Minimal latency overhead after initial fetch

**Configure Nexus cache:**

* Negative cache TTL: 1440 minutes (1 day)
* Metadata max age: 1440 minutes
* Enable "Not found cache"

### Monitoring

**Monitor both Nexus and Firewall:**

Nexus:

* Repository health checks (green = healthy)
* Blob store usage
* Component download counts
* Failed proxy requests

Firewall:

* Block events (malicious packages blocked)
* API error rates
* Cache hit rates
* Request latency

**Splunk integration (recommended):**

```yaml
splunk:
  enabled: true
  hec_url: https://splunk.company.com:8088/services/collector/event
  hec_token: ${SPLUNK_HEC_TOKEN}
  index: security
  source: socket-firewall-nexus
```

**Webhook integration (any HTTP endpoint):**

```yaml
webhook:
  enabled: true
  url: https://siem.company.com/api/events
  auth_header: "Bearer ${WEBHOOK_TOKEN}"
  on_block: true
  on_warn: true
```

### High Availability

**For production deployments:**

1. **Multiple firewall instances** with shared Redis cache:
   ```yaml
   services:
     socket-firewall-1:
       # ... firewall config
     socket-firewall-2:
       # ... firewall config
     redis:
       # ... shared Redis
   ```

2. **Load balancer** in front of firewall instances

3. **Nexus proxy repos** point to load balancer VIP

4. **Nexus HA** (if using Nexus 3 Pro):
   * Deploy Nexus in HA configuration
   * All nodes point proxy repos to firewall load balancer

### Security Hardening

1. **Use proper TLS certificates** (not self-signed in production)
2. **Rotate API tokens** regularly (Nexus → Security → User Tokens)
3. **Limit Nexus API user permissions** to read-only repositories
4. **Use `fail_open: false`** in production for maximum security
5. **Monitor and alert** on block events
6. **Enable Nexus audit logging** for compliance

***

## Reference

### Nexus Proxy Repository Configuration

| Setting              | Value                                                  |
| -------------------- | ------------------------------------------------------ |
| Name                 | `npm-proxy`, `pypi-proxy`, etc.                        |
| Format               | npm, pypi, maven2, etc.                                |
| Remote storage       | `https://socket-firewall.company.com:8443/{ecosystem}` |
| TLS/SSL verification | Disabled (if self-signed) or add cert to trust store   |
| Negative cache TTL   | 1440 minutes (recommended)                             |

### Firewall Configuration Summary

| Topology   | config\_mode | route mode | URL Rewriting |
| ---------- | ------------ | ---------- | ------------- |
| Upstream   | `upstream`   | `rewrite`  | Yes           |
| Downstream | (default)    | `rewrite`  | Yes           |
| Middle     | `middle`     | `proxy`    | No            |

### Supported Repository Formats

| Nexus Format | Firewall Registry | Notes                          |
| ------------ | ----------------- | ------------------------------ |
| npm          | `npm`             | Full support                   |
| pypi         | `pypi`            | Full support                   |
| maven2       | `maven`           | Full support                   |
| cargo        | `cargo`           | Full support                   |
| rubygems     | `rubygems`        | Full support                   |
| nuget        | `nuget`           | Full support                   |
| go           | `go`              | Full support                   |
| conda        | `conda`           | Experimental - treated as PyPI |

### Nexus REST API Endpoints

| Endpoint                               | Purpose                 |
| -------------------------------------- | ----------------------- |
| `/service/rest/v1/repositories`        | List all repositories   |
| `/service/rest/v1/security/user-token` | Generate API token      |
| `/service/rest/v1/repositories/{name}` | Get specific repository |
| `/service/rest/v1/status`              | Nexus health status     |

<br />