# Source: https://docs.socket.dev/docs/artifactory-configuration.md

# Artifactory Configuration

# Artifactory Integration Guide

Complete guide for integrating Socket Registry Firewall with JFrog Artifactory. Supports auto-discovery of repositories and all three deployment topologies.

## Overview

Socket Registry Firewall integrates with Artifactory to protect package ingestion and distribution. The firewall can automatically discover and sync repository configurations from Artifactory, eliminating manual route configuration.

**Supported Artifactory repository types:**

* npm
* PyPI
* Maven
* Cargo
* RubyGems
* NuGet
* Go
* Conda (experimental)

***

## Deployment Topologies

### 1. Upstream Deployment (Most Common)

Artifactory remote repositories pull packages through the firewall. Developers and CI use Artifactory directly.

```
Developer / CI  --->  Artifactory  --->  Socket Firewall  --->  Public Registry
                      (caching)                                   (npmjs.org, pypi.org)
```

**Benefits:**

* Single enforcement point
* No developer config changes needed
* Artifactory caches packages (most installs don't hit firewall)
* Centralized security for entire organization

**Use when:**

* You already have Artifactory deployed
* Developers are already configured to use Artifactory
* You want to protect package ingestion from public registries

[See Upstream Deployment Setup →](#upstream-deployment-setup)

***

### 2. Downstream Deployment

Developers and CI point at the firewall, which proxies to Artifactory (which may or may not have its own upstream).

```
Developer / CI  --->  Socket Firewall  --->  Artifactory  --->  Public/Internal Registry
```

**Benefits:**

* Protect developer workstations directly
* Works with Artifactory virtual repos or local repos
* Can layer on top of existing Artifactory setup

**Use when:**

* You want to protect specific teams or projects
* You have Artifactory hosting internal packages
* You want an additional security layer beyond Artifactory

[See Downstream Deployment Setup →](#downstream-deployment-setup)

***

### 3. Middle Deployment (Multi-Tier)

Firewall sits between two Artifactory instances (e.g., On-Premise → Production, Regional → Central).

```
On-Premise Artifactory  --->  Socket Firewall  --->  Artifactory Production
(Virtual Repo)                                       (Remote Repo)
```

**Benefits:**

* Scan packages flowing between internal registries
* Supports Artifactory virtual repos aggregating remote repos
* Protects multi-tier Artifactory topologies

**Use when:**

* You have multiple Artifactory instances (On-Premise/Prod, Regional/Central)
* Packages flow between Artifactory instances
* You need to scan internal package distribution

[See Middle Deployment Setup →](#middle-deployment-setup)

***

## Auto-Discovery Configuration

Socket Firewall can automatically discover all Artifactory remote repositories and create firewall routes without manual configuration.

### Basic Auto-Discovery

```yaml
path_routing:
  enabled: true
  domain: socket-firewall.company.com
  mode: artifactory
  
  private_registry:
    api_url: https://artifactory.company.com/artifactory
    api_key: your-artifactory-api-key  # Or use env var ARTIFACTORY_API_KEY
    interval: 5m  # Auto-sync every 5 minutes
```

Routes are discovered from Artifactory and updated automatically. No need to manually define each route!

### Advanced Auto-Discovery

```yaml
path_routing:
  enabled: true
  domain: socket-firewall.company.com
  mode: artifactory
  
  private_registry:
    api_url: https://artifactory.company.com/artifactory
    api_key: your-artifactory-api-key    # Token auth (takes precedence)
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

1. Firewall calls Artifactory REST API: `GET /api/repositories`
2. Filters for supported repository types: `VIRTUAL`, `REMOTE`, `LOCAL`, `FEDERATED`, `DISTRIBUTION`
3. Parses repository list and extracts:
   * Repository key (name)
   * Package type (npm, pypi, maven, etc.)
   * Repository type (`REMOTE`, `VIRTUAL`, `LOCAL`, `FEDERATED`, `DISTRIBUTION`)
4. Creates firewall routes:
   * Path: `/artifactory/api/{package-type}/{repo-key}/` (Artifactory-compatible path)
   * Upstream: Remote URL from repository config
   * Registry: Package type
5. Generates nginx configuration with discovered routes
6. Repeats on interval, adding/removing routes as repositories change

### Service Account Permissions for Auto-Discovery

Auto-discovery calls the Artifactory REST API to list repositories. The service account used for authentication needs **read-only** access to the repository listing endpoint.

**API endpoint used:** `GET /api/repositories`

This endpoint returns the key, package type, repository type, and URL of every repository the authenticated user can see. No write operations are performed — the firewall only reads repository metadata to generate routes.

#### Minimum-Privilege Setup (Recommended)

Create a dedicated service account with the minimum permissions required:

1. **Create a group** in Artifactory:
   * Go to **Administration → Identity & Access → Groups → New Group**
   * **Group Name**: `socket-firewall-discovery`
   * **Auto Join**: No

2. **Create a permission target**:
   * Go to **Administration → Identity & Access → Permissions → New Permission**
   * **Name**: `socket-firewall-read`
   * **Resources → Repositories**: Select **Any Repository** (or only the repositories you want the firewall to discover)
   * **Groups**: Add `socket-firewall-discovery` with **Read** permission only
   * Do **not** grant Deploy, Annotate, Delete, or Manage
   * **Save**

3. **Create a local user**:
   * Go to **Administration → Identity & Access → Users → New User**
   * **Username**: `socket-firewall`
   * **Status**: Enabled
   * **Groups**: Add to `socket-firewall-discovery`
   * **Save**

4. **Generate an API key** (preferred over password):

   * Log in as the new user
   * Go to **Edit Profile → API Key → Generate**
   * Use this key as `api_key` in `socket.yml`

   Alternatively, generate an **Access Token** (Artifactory 7.x+):

   * Go to **Administration → Identity & Access → Access Tokens → Generate Token**
   * **Token Scope**: User `socket-firewall`
   * Use the token as `api_key` in `socket.yml`

#### Artifactory Permission Reference

| Permission | Purpose                                   | Required?       |
| ---------- | ----------------------------------------- | --------------- |
| Read       | Read/list repositories and their metadata | **Yes**         |
| Deploy     | Upload artifacts                          | No — not needed |
| Annotate   | Add/modify properties on artifacts        | No — not needed |
| Delete     | Delete artifacts or repositories          | No — not needed |
| Manage     | Administer permissions and settings       | No — not needed |

> **Note (Artifactory Cloud / SaaS):** If you use Artifactory Cloud (JFrog Platform), the same permissions apply. Use a scoped **Access Token** with read-only permissions. Navigate to **Administration → Identity & Access → Access Tokens** to generate one.

#### Verifying Permissions

Test that the service account can list repositories:

```bash
# Using API key
curl -H "X-JFrog-Art-Api: your-api-key" \
  https://artifactory.company.com/artifactory/api/repositories

# Using basic auth (username:password)
curl -u "socket-firewall:password" \
  https://artifactory.company.com/artifactory/api/repositories

# Using Access Token (Artifactory 7.x+)
curl -H "Authorization: Bearer your-access-token" \
  https://artifactory.company.com/artifactory/api/repositories

# Expected: JSON array of repository objects
# [{"key": "npm-remote", "type": "REMOTE", "packageType": "npm", "url": "..."}, ...]
```

If the response is `401 Unauthorized`, the API key or token is invalid. If it returns `403 Forbidden`, the user lacks the Read permission on repositories. If it returns an empty list, the permission target may be scoped too narrowly — ensure it includes the repositories you want to discover.

***

## Upstream Deployment Setup

Protect package ingestion by pointing Artifactory remote repos at the firewall.

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
  mode: artifactory  # Auto-discovery
  
  private_registry:
    api_url: https://artifactory.company.com/artifactory
    api_key: ${ARTIFACTORY_API_KEY}
    interval: 5m
    exclude_pattern: "(tmp|test)-.*"

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
      - ARTIFACTORY_API_KEY=${ARTIFACTORY_API_KEY}
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

### Step 2: Configure Artifactory Remote Repositories

Point each Artifactory remote repository to the firewall instead of the public registry.

#### npm Remote Repository

1. Go to **Administration → Artifactory → Repositories → Remote**
2. Edit your npm remote repository (e.g., `npm-remote`)
3. Change **URL** from `https://registry.npmjs.org` to:
   ```
   https://socket-firewall.internal.company.com:8443/npm
   ```
4. If using self-signed certs:
   * Uncheck **Verify SSL Certificate**
   * Or add firewall's CA to Artifactory's trust store
5. **Save**

#### PyPI Remote Repository

1. Edit your PyPI remote repository (e.g., `pypi-remote`)
2. Change **URL** to:
   ```
   https://socket-firewall.internal.company.com:8443/pypi
   ```
3. **Save**

#### Maven Remote Repository

1. Edit your Maven remote repository (e.g., `maven-central`)
2. Change **URL** to:
   ```
   https://socket-firewall.internal.company.com:8443/maven
   ```
3. Under **Advanced**, set:
   * **Store Artifacts Locally**: Yes
   * **Synchronize Properties**: Whatever you prefer
4. **Save**

#### Other Ecosystems

Repeat for Cargo, RubyGems, NuGet, Go using the corresponding paths:

* Cargo: `https://socket-firewall.internal.company.com:8443/cargo`
* RubyGems: `https://socket-firewall.internal.company.com:8443/rubygems`
* NuGet: `https://socket-firewall.internal.company.com:8443/nuget`
* Go: `https://socket-firewall.internal.company.com:8443/go`

### Step 3: Test

**Test npm:**

```bash
# Developers use Artifactory as normal
npm config set registry https://artifactory.company.com/artifactory/api/npm/npm-remote/
npm install lodash

# Check firewall logs
docker compose logs socket-firewall | grep lodash
```

**Test PyPI:**

```bash
pip config set global.index-url https://artifactory.company.com/artifactory/api/pypi/pypi-remote/simple
pip install requests

docker compose logs socket-firewall | grep requests
```

### Step 4: Verify Auto-Discovery

Check that the firewall discovered your Artifactory repositories:

```bash
# View discovered routes
docker compose exec socket-firewall cat /app/discovered-routes.yml

# Check logs for discovery events
docker compose logs socket-firewall | grep "Discovered.*repositories"
```

***

## Downstream Deployment Setup

Developers point at the firewall, which proxies to Artifactory.

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
    # Point to Artifactory virtual or remote repos
    - path: /npm
      upstream: https://artifactory.company.com/artifactory/api/npm/npm-virtual
      registry: npm
      
    - path: /pypi
      upstream: https://artifactory.company.com/artifactory/api/pypi/pypi-virtual
      registry: pypi
```

**Client configuration:**

```bash
# Developers point at firewall instead of Artifactory
npm config set registry https://firewall.company.com/npm/
pip config set global.index-url https://firewall.company.com/pypi/simple
```

***

## Middle Deployment Setup

Firewall sits between two Artifactory instances. Supports virtual repos aggregating remote repos.

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
    # On-Premise Artifactory virtual repo → Prod Artifactory remote repo
    - path: /pypi
      upstream: https://artifactory-prod.company.com/artifactory/api/pypi/pypi-remote
      registry: pypi
      mode: proxy  # IMPORTANT - passes URLs unchanged
      
    - path: /npm
      upstream: https://artifactory-prod.company.com/artifactory/api/npm/npm-remote
      registry: npm
      mode: proxy
```

**On-Premise Artifactory Configuration:**

1. Create virtual repository in on-premise Artifactory
2. Add remote repository pointing to firewall:
   * Remote URL: `https://socket-firewall.internal.company.com:8443/pypi`
3. Virtual repo aggregates this remote

**Why `mode: proxy` is required:**

* Production Artifactory returns relative URLs like `../../packages/xyz/file.tar.gz`
* `mode: proxy` passes these URLs through unchanged
* On-premise Artifactory resolves relative URLs against its own base path
* `mode: rewrite` would break this by rewriting URLs to firewall paths

***

## Troubleshooting

### Artifactory Can't Reach Firewall

**Symptom:** Artifactory shows connection errors when fetching packages

**Check:**

```bash
# From Artifactory server, test connectivity
curl -k https://socket-firewall.internal.company.com:8443/health

# Check DNS resolution
nslookup socket-firewall.internal.company.com

# Check firewall from Artifactory
ping socket-firewall.internal.company.com
```

**Solution:**

* Verify DNS record points to firewall host
* Ensure firewall ports (8080/8443) are accessible from Artifactory
* Check firewall rules/security groups

### SSL Certificate Errors

**Symptom:** Artifactory logs show SSL verification errors

**Option 1 - Trust firewall cert in Artifactory:**

```bash
# Copy firewall cert to Artifactory server
scp ssl/fullchain.pem artifactory-server:/tmp/socket-firewall.crt

# Add to Artifactory's Java trust store
keytool -import -alias socket-firewall \
  -keystore $JAVA_HOME/lib/security/cacerts \
  -file /tmp/socket-firewall.crt \
  -storepass changeit

# Restart Artifactory
```

**Option 2 - Disable SSL verification (testing only):**

* In Artifactory remote repo settings, uncheck "Verify SSL Certificate"

### Auto-Discovery Not Finding Repositories

**Check Artifactory API access:**

```bash
# Test API connectivity
curl -H "X-JFrog-Art-Api: your-api-key" \
  https://artifactory.company.com/artifactory/api/repositories

# Should return JSON list of repositories
```

**Check firewall logs:**

```bash
docker compose logs socket-firewall | grep -i discovery
docker compose logs socket-firewall | grep -i artifactory
```

**Common issues:**

* API key lacks permissions (needs "Read" on repositories)
* `api_url` incorrect (should end with `/artifactory`, not include `/api`)
* Network connectivity from firewall to Artifactory

### Virtual Repo Doubled URLs

**Symptom:** Artifactory virtual repos return URLs like `/artifactory/api/pypi/pypi-virtual/artifactory/api/pypi/pypi-remote/packages/...`

**Solution:** Use `config_mode: middle` and `mode: proxy`:

```yaml
config_mode: middle
path_routing:
  routes:
    - path: /pypi
      upstream: https://artifactory.company.com/artifactory/api/pypi/pypi-remote
      registry: pypi
      mode: proxy  # Critical - prevents URL rewriting
```

### Package Downloads Failing

**Check firewall is blocking correctly:**

```bash
# Try to install known malicious package
npm install some-malicious-package

# Check firewall logs for block
docker compose logs socket-firewall | grep -i block
```

**Check firewall is allowing correct packages:**

```bash
# Install known safe package
npm install lodash

# Should succeed - check logs
docker compose logs socket-firewall | grep lodash
```

***

## Best Practices

### Repository Naming

Use consistent naming in Artifactory to simplify filtering:

* `npm-public` - Public npm registry
* `npm-internal` - Internal npm packages
* `pypi-public` - Public PyPI registry
* `pypi-internal` - Internal Python packages

Then use filters:

```yaml
include_pattern: ".*-public"  # Only protect public-facing repos
exclude_pattern: ".*-internal"  # Don't scan internal packages
```

### Caching Strategy

**Artifactory caching + Firewall caching = Maximum efficiency:**

1. Artifactory caches packages after first fetch
2. Firewall caches security results for 24h (default)
3. Subsequent installs hit Artifactory cache (never reach firewall)
4. New packages hit firewall once, then cached by both

**Result:** Minimal latency overhead after initial fetch

### Monitoring

**Monitor both Artifactory and Firewall:**

Artifactory:

* Monitor remote repository health
* Check artifact download counts
* Review failed download requests

Firewall:

* Monitor block events (malicious packages)
* Check API error rates
* Review cache hit rates

**Splunk integration (recommended):**

```yaml
splunk:
  enabled: true
  hec_url: https://splunk.company.com:8088/services/collector/event
  hec_token: ${SPLUNK_HEC_TOKEN}
  index: security
  source: socket-firewall-artifactory
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

3. **Artifactory remote repo** points to load balancer VIP

### Security Hardening

1. **Use proper TLS certificates** (not self-signed in production)
2. **Rotate API keys** regularly
3. **Limit Artifactory API key permissions** to read-only repositories
4. **Use `fail_open: false`** in production for maximum security
5. **Monitor and alert** on block events

***

## Reference

### Artifactory Remote Repository Configuration

| Setting                 | Value                                                  |
| ----------------------- | ------------------------------------------------------ |
| Repository Key          | `npm-remote`, `pypi-remote`, etc.                      |
| Package Type            | npm, pypi, maven, etc.                                 |
| URL                     | `https://socket-firewall.company.com:8443/{ecosystem}` |
| Verify SSL              | No (if using self-signed)                              |
| Store Artifacts Locally | Yes (recommended)                                      |

### Firewall Configuration Summary

| Topology   | config\_mode | route mode | URL Rewriting |
| ---------- | ------------ | ---------- | ------------- |
| Upstream   | `upstream`   | `rewrite`  | Yes           |
| Downstream | (default)    | `rewrite`  | Yes           |
| Middle     | `middle`     | `proxy`    | No            |

### Supported Package Types

| Artifactory Format | Firewall Registry | Notes                          |
| ------------------ | ----------------- | ------------------------------ |
| npm                | `npm`             | Full support                   |
| pypi               | `pypi`            | Full support                   |
| maven              | `maven`           | Full support                   |
| cargo              | `cargo`           | Full support                   |
| gems               | `rubygems`        | Full support                   |
| nuget              | `nuget`           | Full support                   |
| go                 | `go`              | Full support                   |
| conda              | `conda`           | Experimental - treated as PyPI |

<br />