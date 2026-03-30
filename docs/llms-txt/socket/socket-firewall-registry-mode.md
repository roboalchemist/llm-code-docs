# Source: https://docs.socket.dev/docs/socket-firewall-registry-mode.md

# Socket Firewall: Registry Mode

Registry Mode Overview

# Socket Registry Firewall

Enterprise-grade security proxy that protects package registries by scanning packages with Socket's security API in real-time to block malicious packages before they reach your systems.

## Overview

Socket Registry Firewall runs as a Docker container that acts as a **security-scanning registry proxy**. Package managers are configured to use the firewall as their registry endpoint. The firewall intercepts all package requests, checks them against the Socket.dev security API, and blocks malicious packages before they can be installed.

**Request Flow:**

```
Developer / CI
      |
      v
Socket Registry Firewall  --->  Socket.dev API (security check)
      |
      v
Upstream Registry (npmjs.org, pypi.org, etc.)
```

**How it works:**

1. Client requests package from firewall
2. Firewall extracts package name/version
3. Firewall checks Socket API for security issues
4. If safe → proxy to upstream and return package
5. If malicious → return `403 Forbidden` with reason

## Supported Ecosystems

| Registry | Ecosystem          | Upstream URL                  |
| -------- | ------------------ | ----------------------------- |
| npm      | JavaScript/Node.js | `registry.npmjs.org`          |
| PyPI     | Python             | `pypi.org`                    |
| Maven    | Java/Kotlin/Scala  | `repo1.maven.org`             |
| Cargo    | Rust               | `crates.io`                   |
| RubyGems | Ruby               | `rubygems.org`                |
| OpenVSX  | VS Code Extensions | `open-vsx.org`                |
| NuGet    | .NET               | `nuget.org`                   |
| Go       | Go Modules         | `proxy.golang.org`            |
| Conda    | Python/R/Data Sci  | `repo.anaconda.com/pkgs/main` |

All ecosystems support both metadata parsing and direct download protection.

## Deployment Topologies

Socket Registry Firewall supports three deployment topologies depending on where it sits in your package supply chain:

### 1. Downstream Deployment (Client-Facing)

The firewall sits **between developers/CI and the registry** (public or private). Most common deployment.

```
Developer / CI  --->  Socket Firewall  --->  Public Registry (npmjs.org)
                                        --->  Private Registry (Artifactory/Nexus)
```

**Use when:**

* You want to protect developer workstations and CI pipelines directly
* You control package manager configuration (registry URLs)
* You want to block malicious packages before they reach any machine
* You don't have a centralized registry mirror

**Configuration:**

```yaml
# Default mode - generates API paths for clients
# No special config_mode needed
path_routing:
  enabled: true
  domain: firewall.company.com
  routes:
    - path: /npm
      upstream: https://registry.npmjs.org
      registry: npm
```

**Client configuration:**

```bash
npm config set registry https://firewall.company.com/npm/
pip config set global.index-url https://firewall.company.com/pypi/simple
```

See: **[Downstream Deployment Guide](https://docs.socket.dev/docs/registry-mode-setup-downstream)**

***

### 2. Upstream Deployment (Registry-Facing)

The firewall sits **between your private registry mirror and the public internet**. The registry pulls packages through the firewall.

```
Developer / CI  --->  Artifactory / Nexus  --->  Socket Firewall  --->  Public Registry
```

**Use when:**

* You already have a centralized Artifactory/Nexus instance
* You don't want to change developer-side package manager configs
* You want a single enforcement point for all package ingestion
* Your mirror caches packages (most installs don't hit firewall after first fetch)

**Configuration:**

```yaml
# Generates direct paths for registry-to-registry communication
config_mode: upstream
path_routing:
  enabled: true
  domain: socket-firewall.internal.company.com
  routes:
    - path: /npm
      upstream: https://registry.npmjs.org
      registry: npm
      mode: rewrite  # Default - rewrites URLs for caching
```

**Artifactory configuration:**

```
# Point Artifactory remote repo to firewall
Remote URL: https://socket-firewall.internal.company.com/npm
```

See: **[Upstream Deployment Guide](https://docs.socket.dev/docs/registry-mode-upstream-deployment-guide)**

***

### 3. Middle Deployment (Registry-to-Registry)

The firewall sits **between two private registries** (e.g., on-premise Artifactory → Production Artifactory). Both API and direct paths are generated, and URLs are passed through unchanged.

```
On-Premise Artifactory  --->  Socket Firewall  --->  Artifactory Production
      ^                                              ^
      |                                              |
  Virtual Repo                                 Remote Repo
```

**Use when:**

* You have multiple Artifactory/Nexus instances (On-Premise → Prod, Regional → Central)
* Downstream registry needs to resolve relative URLs
* You want to scan packages flowing between internal registries
* You need both metadata inspection and direct download protection

**Configuration:**

```yaml
# Generates both API and direct paths with no URL rewriting
config_mode: middle
path_routing:
  enabled: true
  domain: socket-firewall.internal.company.com
  routes:
    - path: /pypi
      upstream: https://artifactory-prod.company.com/artifactory/api/pypi/pypi-remote
      registry: pypi
      mode: proxy  # IMPORTANT - passes URLs unchanged
```

**Key differences from upstream:**

* `mode: proxy` - No URL rewriting (downstream registry resolves relative URLs)
* `config_mode: middle` - Generates both API and direct paths
* Supports Artifactory virtual repos aggregating remote repos

See: **[Artifactory Guide](https://docs.socket.dev/docs/artifactory-configuration)** and **[Nexus Guide](https://docs.socket.dev/docs/nexus-configuration)** for details

***

## Deployment Topology Comparison

| Feature               | Downstream                   | Upstream                    | Middle                                |
| --------------------- | ---------------------------- | --------------------------- | ------------------------------------- |
| **Firewall position** | Client → FW → Registry       | Registry → FW → Public      | Registry → FW → Registry              |
| **Client config**     | Points to firewall           | Points to existing registry | Points to existing registry           |
| **config\_mode**      | Not set (default/downstream) | `upstream`                  | `middle`                              |
| **route mode**        | `rewrite` (default)          | `rewrite` (default)         | `proxy` (required)                    |
| **URL rewriting**     | Yes - to firewall paths      | Yes - for caching           | No - pass through unchanged           |
| **Best for**          | Direct client protection     | Centralized enforcement     | Multi-tier registries                 |
| **Examples**          | Dev workstations, CI/CD      | Artifactory remote repos    | On-Premise → Prod, Regional → Central |

## Key Features

✅ **Real-time Security** - Blocks malicious packages before installation using Socket.dev's security API\
✅ **Multi-Ecosystem** - Supports all 9 major package ecosystems\
✅ **Flexible Topologies** - Downstream, upstream, or middle deployments\
✅ **Flexible Routing** - Domain-based or path-based routing\
✅ **Auto-Discovery** - Sync routes from Artifactory/Nexus automatically\
✅ **High Performance** - Intelligent caching with stale-while-revalidate (local or Redis)\
✅ **Enterprise Ready** - Outbound proxy support, custom CAs, Splunk integration, webhook events\
✅ **Production Proven** - Fail-open/closed modes, health checks, comprehensive logging

## Routing Strategies

### Path-Based Routing (Recommended)

All registries share a single domain with path prefixes. Requires only one DNS record and one SSL certificate.

```yaml
path_routing:
  enabled: true
  domain: firewall.company.com
  routes:
    - path: /npm
      upstream: https://registry.npmjs.org
      registry: npm
    - path: /pypi
      upstream: https://pypi.org
      registry: pypi
    - path: /maven
      upstream: https://repo1.maven.org/maven2
      registry: maven
```

**Client usage:**

```bash
npm config set registry https://firewall.company.com/npm/
pip config set global.index-url https://firewall.company.com/pypi/simple
```

### Domain-Based Routing

Each registry gets its own subdomain. Requires multiple DNS records and certificates (or wildcard cert).

```yaml
registries:
  npm:
    domains: [npm.company.com]
  pypi:
    domains: [pypi.company.com]
  maven:
    domains: [maven.company.com]
```

**Client usage:**

```bash
npm config set registry https://npm.company.com/
pip config set global.index-url https://pypi.company.com/simple
```

### Auto-Discovery (Artifactory/Nexus)

Automatically sync repository routes from your artifact manager. No manual route configuration needed!

```yaml
path_routing:
  enabled: true
  domain: firewall.company.com
  mode: artifactory  # or 'nexus'
  
  private_registry:
    api_url: https://artifactory.company.com/artifactory
    api_key: your-artifactory-api-key
    interval: 5m              # Auto-sync every 5 minutes
    ignore_ssl_errors: false  # Disable SSL cert verification (default: false)
    include_pattern: ".*"     # Include all repos
    exclude_pattern: "(tmp|test)-.*"  # Exclude temp/test repos
```

Routes update automatically when you add/remove repositories in Artifactory/Nexus!

See: **[Artifactory Guide](https://docs.socket.dev/docs/artifactory-configuration)** | **[Nexus Guide](https://docs.socket.dev/docs/nexus-configuration)** for details

## Caching Strategy

The firewall uses **stale-while-revalidate** caching to minimize API calls and ensure high performance:

* **Fresh zone** (default 600s): Cached results returned immediately
* **Stale zone** (up to 24h): Revalidate with Socket API, fallback to stale on error
* **Redis support**: For distributed deployments with multiple firewall instances

```yaml
cache:
  ttl: 600        # Fresh window (10 minutes)

redis:
  enabled: true
  host: redis.company.com
  port: 6379
  ttl: 86400      # Stale window (24 hours)
```

## Fail-Safe Behavior

Control what happens when the Socket API is unavailable:

```yaml
socket:
  fail_open: true   # Allow packages if API is down (default - prioritizes availability)
  # fail_open: false  # Block all packages if API is down (prioritizes security)
```

**Recommendation**: Use `fail_open: true` for development/CI environments, `fail_open: false` for production registries.

## Getting Started

1. **[Installation Guide](https://docs.socket.dev/docs/installations)** - Pre-built image or tarball installation
2. **Choose your topology:**
   * **[Downstream Deployment](https://docs.socket.dev/docs/registry-mode-setup-downstream)** - Protect developers and CI directly
   * **[Upstream Deployment](https://docs.socket.dev/docs/registry-mode-upstream-deployment-guide)** - Protect registry mirror ingestion
   * **[Artifactory Integration](https://docs.socket.dev/docs/artifactory-configuration)** - Auto-discovery and configuration
   * **[Nexus Integration](https://docs.socket.dev/docs/nexus-configuration)** - Auto-discovery and configuration
3. **[Configuration Reference](./Configuration/)** - Full config options, environment variables, SSL, Redis, Splunk

## Common Use Cases

### Use Case 1: Protect Developer Workstations

**Topology**: Downstream\
**Setup**: Developers configure npm/pip/mvn to point at firewall\
**Benefit**: Block malicious packages before they reach developer machines

[See Downstream Guide →](https://docs.socket.dev/docs/registry-mode-setup-downstream)

### Use Case 2: Centralized Protection with Artifactory

**Topology**: Upstream\
**Setup**: Artifactory remote repos point to firewall\
**Benefit**: Single enforcement point, no developer config changes

[See Artifactory Guide →](https://docs.socket.dev/docs/artifactory-configuration)

### Use Case 3: Nexus Repository Manager

**Topology**: Upstream\
**Setup**: Nexus proxy repos point to firewall\
**Benefit**: Protect package ingestion without client changes

[See Nexus Guide →](https://docs.socket.dev/docs/nexus-configuration)

### Use Case 4: Multi-Tier Artifactory (On-Premise → Production)

**Topology**: Middle\
**Setup**: On-premise Artifactory virtual repo → Firewall → Production Artifactory\
**Benefit**: Scan packages flowing between internal registries

[See Artifactory Guide - Middle Deployment →](https://docs.socket.dev/docs/artifactory-configuration#middle-deployment-setup)

## Architecture

```
┌────────────────┐
│  Client / CI   │
└───────┬────────┘
        │
        v
┌────────────────────────────────┐
│   Socket Registry Firewall     │
│  ┌──────────────────────────┐  │
│  │  Package Parser (Lua)    │  │  Extract package name/version
│  └──────────┬───────────────┘  │
│             v                  │
│  ┌──────────────────────────┐  │
│  │  Socket Client (Lua)     │◄─┼─► Socket.dev API
│  │  + Redis Cache           │  │    (security check)
│  └──────────┬───────────────┘  │
│             v                  │
│  ┌──────────────────────────┐  │
│  │  Upstream Proxy (nginx)  │  │  Forward safe packages
│  └──────────┬───────────────┘  │
└─────────────┼──────────────────┘
              v
    ┌──────────────────┐
    │ Upstream Registry│
    │ (npmjs.org, etc.)│
    └──────────────────┘
```

**Components:**

* **Package Parsers** - Ecosystem-specific Lua modules that extract package identifiers from requests
* **Socket Client** - Communicates with Socket.dev API, manages caching
* **Upstream Proxy** - NGINX reverse proxy that forwards requests to upstream registries
* **Config Tool** - Generates NGINX configurations from `socket.yml`

## Documentation

* **[Installation Guide](https://docs.socket.dev/docs/installations)** - Pre-built Docker image and tarball installation
* **[Downstream Deployment](https://docs.socket.dev/docs/registry-mode-setup-downstream)** - Protect developers and CI directly
* **[Upstream Deployment](https://docs.socket.dev/docs/registry-mode-upstream-deployment-guide)** - Protect registry mirror ingestion
* **[Artifactory Integration](./Artifactory/)** - Auto-discovery, upstream/middle deployment
* **[Nexus Integration](https://docs.socket.dev/docs/nexus-configuration)** - Auto-discovery, upstream/middle deployment
* **[Configuration Reference](https://docs.socket.dev/docs/registry-mode-configuration-reference)** - All config options, environment variables, SSL, Redis, Splunk

## Support

* **Documentation**: [https://docs.socket.dev](https://docs.socket.dev)
* **Tarball Releases**: [https://github.com/SocketDev/socket-registry-firewall](https://github.com/SocketDev/socket-registry-firewall)
* **Email**: [support@socket.dev](mailto:support@socket.dev)