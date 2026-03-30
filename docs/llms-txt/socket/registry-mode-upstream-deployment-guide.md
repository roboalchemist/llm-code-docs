# Source: https://docs.socket.dev/docs/registry-mode-upstream-deployment-guide.md

# Upstream Deployment Guide

Deploy the Socket Registry Firewall **between your private registry mirror (Artifactory/Nexus) and the public internet**. The firewall scans every package your mirror fetches before it enters your internal network.

```
Developer / CI  --->  Artifactory / Nexus  --->  Socket Firewall  --->  Public Registry
```

## When to Use Upstream Deployment

* You have a centralized Artifactory or Nexus instance that all developers already use
* You don't want to change any developer-side package manager configurations
* You want a single enforcement point — every package entering your org is scanned once
* Your mirror caches packages, so most installs don't hit the firewall at all after initial fetch

## How It Works

1. Artifactory/Nexus is configured to use the Socket Firewall as its remote/proxy upstream
2. When a developer requests a package not yet cached, Artifactory fetches it through the firewall
3. The firewall checks the package against the Socket.dev API
4. If safe: the package flows through to Artifactory, which caches it and serves it to the developer
5. If malicious: the firewall returns `403 Forbidden`, Artifactory reports the fetch failure

Cached packages are served directly from Artifactory without hitting the firewall, so the firewall only scans new or updated packages.

## Prerequisites

* Docker and Docker Compose on the firewall host
* Socket.dev API key with scopes: `packages:list`, `entitlements:list`
* Admin access to Artifactory or Nexus to reconfigure remote repository upstreams
* Network connectivity: Artifactory/Nexus must be able to reach the firewall host

## Step 1: Deploy the Firewall

### Set API Token

```bash
export SOCKET_SECURITY_API_TOKEN=your-api-key-here
```

### Create Configuration

The upstream deployment uses path-based routing so Artifactory/Nexus can reach all registries through a single firewall endpoint.

Create `socket.yml`:

```yaml
socket:
  api_url: https://api.socket.dev

ports:
  http: 8080
  https: 8443

path_routing:
  enabled: true
  domain: socket-firewall.internal.company.com
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
    - path: /cargo
      upstream: https://index.crates.io
      registry: cargo
    - path: /rubygems
      upstream: https://rubygems.org
      registry: rubygems
    - path: /nuget
      upstream: https://api.nuget.org
      registry: nuget
    - path: /go
      upstream: https://proxy.golang.org
      registry: go
    - path: /openvsx
      upstream: https://open-vsx.org
      registry: openvsx
    - path: /conda
      upstream: https://repo.anaconda.com/pkgs/main
      registry: conda

nginx:
  worker_processes: 2
  worker_connections: 4096
```

### Create Docker Compose File

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
    healthcheck:
      test: ["CMD", "curl", "-fk", "https://localhost:8443/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### DNS

Create a DNS record for `socket-firewall.internal.company.com` pointing to the firewall host. This must be resolvable from your Artifactory/Nexus server.

### Start

```bash
docker pull socketdev/socket-registry-firewall
docker compose up -d
curl -k https://socket-firewall.internal.company.com:8443/health
```

## Step 2: Configure Artifactory

Reconfigure each remote repository in Artifactory to fetch through the Socket Firewall instead of directly from the public registry.

### npm Remote Repository

1. Go to **Administration > Repositories > Remote**
2. Edit your npm remote repository (e.g., `npm-remote`)
3. Change **URL** from `https://registry.npmjs.org` to:
   ```
   https://socket-firewall.internal.company.com:8443/npm
   ```
4. If using self-signed certs, uncheck **Verify SSL** or add the firewall's CA to Artifactory's trust store
5. Save

### PyPI Remote Repository

1. Edit your PyPI remote repository (e.g., `pypi-remote`)
2. Change **URL** to:
   ```
   https://socket-firewall.internal.company.com:8443/pypi
   ```
3. Save

### Maven Remote Repository

1. Edit your Maven remote repository (e.g., `maven-remote`)
2. Change **URL** to:
   ```
   https://socket-firewall.internal.company.com:8443/maven
   ```
3. Save

Repeat for Cargo, RubyGems, NuGet, and Go as needed.

## Step 2 (Alternative): Configure Nexus

### npm Proxy Repository

1. Go to **Administration > Repository > Repositories**
2. Edit your npm proxy repository
3. Change **Remote storage** URL to:
   ```
   https://socket-firewall.internal.company.com:8443/npm
   ```
4. Under **HTTP** settings, disable SSL verification if using self-signed certs
5. Save

### PyPI Proxy Repository

1. Edit your PyPI proxy repository
2. Change **Remote storage** URL to:
   ```
   https://socket-firewall.internal.company.com:8443/pypi
   ```
3. Save

### Maven Proxy Repository

1. Edit your Maven proxy repository
2. Change **Remote storage** URL to:
   ```
   https://socket-firewall.internal.company.com:8443/maven
   ```
3. Save

Repeat for other ecosystems as needed.

## Step 3: SSL/TLS Setup

The connection between Artifactory/Nexus and the Socket Firewall should be trusted.

### Option A: Use Proper Certificates (Recommended)

Place your organization's certificates in the firewall's `ssl/` directory:

```bash
cp /path/to/cert.pem ssl/fullchain.pem
cp /path/to/key.pem ssl/privkey.pem
```

### Option B: Trust Self-Signed Certs in Artifactory

**Artifactory:**

1. Download the firewall's certificate:
   ```bash
   openssl s_client -connect socket-firewall.internal.company.com:8443 \
     -servername socket-firewall.internal.company.com </dev/null 2>/dev/null \
     | openssl x509 > firewall-cert.pem
   ```
2. Import into Artifactory:
   * Go to **Administration > Security > Certificates**
   * Add the `firewall-cert.pem` certificate

**Nexus:**

1. Import the firewall cert into the Java truststore:
   ```bash
   keytool -import -alias socket-firewall \
     -file firewall-cert.pem \
     -keystore /opt/sonatype/nexus/etc/ssl/truststore.jks
   ```
2. Restart Nexus

### Option C: Disable SSL Verification (Testing Only)

In Artifactory, uncheck "Verify SSL" on each remote repository.

In Nexus, uncheck "Use the Nexus truststore" and disable SSL verification in HTTP settings.

## Step 4: Verify

### Test the Pipeline

Trigger a cache miss to force Artifactory/Nexus to fetch through the firewall:

```bash
# Clear the cached package in Artifactory/Nexus first, then:

# npm
npm install some-uncached-package

# pip
pip install some-uncached-package

# Maven — build a project with a dependency not yet in your mirror
mvn install
```

### Check Firewall Logs

```bash
# Verify traffic is flowing through the firewall
docker compose logs -f socket-firewall

# Look for blocked packages
docker compose logs socket-firewall | grep -i block

# Look for successful proxied requests
docker compose logs socket-firewall | grep "200"
```

### Test Blocking

Install a known malicious or typosquat package to verify the firewall blocks it:

```bash
# npm — typosquat example
npm install lodahs
# Artifactory should report a fetch failure
```

Check the firewall logs for the block event.

## Corporate Proxy

If the firewall host sits behind a corporate egress proxy:

```yaml
socket:
  outbound_proxy: http://proxy.company.com:3128
  no_proxy: localhost,127.0.0.1,internal.company.com
```

If the corporate proxy performs MITM TLS inspection:

```yaml
socket:
  outbound_proxy: http://proxy.company.com:3128
  api_ssl_verify: true
  api_ssl_ca_cert: /path/to/corporate-ca.crt
```

## Performance Considerations

In upstream deployments, the firewall only processes **cache misses** from your registry mirror. This means:

* Traffic volume is significantly lower than downstream deployments
* The firewall only scans each package version once (the mirror caches subsequent requests)
* A smaller instance (1-2 CPU, 1-2 GB) is often sufficient
* Redis caching on the firewall side is less critical since the mirror itself caches

### Recommended Sizing

| Mirror Size          | Firewall Resources | Notes               |
| -------------------- | ------------------ | ------------------- |
| Small (\< 50 devs)   | 1 CPU / 1 GB       | Handles \~30 req/s  |
| Medium (50-500 devs) | 2 CPU / 2 GB       | Handles \~60 req/s  |
| Large (500+ devs)    | 4 CPU / 4 GB       | Handles \~100 req/s |

These are conservative — remember the mirror absorbs most traffic.

## Fail-Open Considerations

In upstream deployment, fail-open behavior is especially important:

```yaml
socket:
  fail_open: true   # Allow packages if Socket API is down (default)
```

If `fail_open: false`, a Socket API outage will prevent your registry mirror from fetching **any** new packages. This blocks all developers who need uncached packages. Consider:

* **fail\_open: true** for availability-critical environments
* **fail\_open: false** only if security requirements outweigh availability risk
* Monitor the Socket API health endpoint and alert on failures

## Monitoring

### Health Check

```bash
curl -k https://socket-firewall.internal.company.com:8443/health
```

### Key Metrics to Watch

* **Block events**: Packages blocked by security policy
* **Upstream latency**: Time to reach public registries through the firewall
* **Error rate**: Failed requests (may indicate connectivity or config issues)
* **Cache hit rate** (Artifactory/Nexus side): High cache hit rate means less firewall traffic

### Splunk Integration

```yaml
splunk:
  enabled: true
  hec_url: https://splunk.company.com:8088/services/collector/event
  hec_token: your-splunk-hec-token
  index: security
  source: socket-firewall
```

## Troubleshooting

### Artifactory/Nexus Can't Reach Firewall

```bash
# From the Artifactory/Nexus host:
curl -kI https://socket-firewall.internal.company.com:8443/health

# Check DNS resolution
nslookup socket-firewall.internal.company.com

# Check firewall ports
nc -zv socket-firewall.internal.company.com 8443
```

### Packages Fail to Download

```bash
# Check firewall logs for the request
docker compose logs socket-firewall | grep "<package-name>"

# Check if it was blocked
docker compose logs socket-firewall | grep -i block

# Test upstream connectivity from the firewall container
docker compose exec socket-firewall curl -I https://registry.npmjs.org
```

### SSL Errors Between Artifactory and Firewall

```bash
# Test the TLS connection
openssl s_client -connect socket-firewall.internal.company.com:8443 \
  -servername socket-firewall.internal.company.com

# Verify certificate matches expected domain
openssl s_client -connect socket-firewall.internal.company.com:8443 \
  </dev/null 2>/dev/null | openssl x509 -noout -subject -dates
```