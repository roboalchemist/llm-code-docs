# Source: https://docs.socket.dev/docs/registry-mode-setup-downstream.md

# Downstream Deployment Guide

Deploy the Socket Registry Firewall **between developers/CI and the package registry**. Developers and CI systems point their package managers at the firewall instead of directly at the public or private registry.

```
Developer / CI  --->  Socket Firewall  --->  Public Registry (npmjs.org, pypi.org, etc.)
                                        --->  Private Registry (Artifactory / Nexus)
```

## Prerequisites

* Docker and Docker Compose
* Socket.dev API key with scopes: `packages:list`, `entitlements:list`
* DNS or `/etc/hosts` entry for the firewall domain (for path-based routing)

## Step 1: Set Your API Token

```bash
export SOCKET_SECURITY_API_TOKEN=your-api-key-here
```

Or create a `.env` file:

```bash
cat > .env <<EOF
SOCKET_SECURITY_API_TOKEN=your-api-key-here
EOF
```

## Step 2: Create Configuration

Create `socket.yml` with path-based routing (recommended for most setups):

Be sure to set the `domain` value to the domain you intend to host the firewall on.

```yaml
socket:
  api_url: https://api.socket.dev

ports:
  http: 8080
  https: 8443

path_routing:
  enabled: true
  domain: sfw.your_company.com
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

Include only the registries you need.

### Alternative: Domain-Based Routing

If you prefer separate domains per registry:

```yaml
registries:
  npm:
    domains: [npm.company.com]
  pypi:
    domains: [pypi.company.com]
  maven:
    domains: [maven.company.com]
```

Each domain needs a DNS record pointing to the firewall.

## Step 3: Create Docker Compose File

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

## Step 4: DNS / Host Entry

For path-based routing, the firewall domain must resolve to the firewall host.

**Local testing** (add to `/etc/hosts`):

```bash
sudo sh -c 'printf "127.0.0.1   sfw.your_company.com\n::1         sfw.your_company.com\n" >> /etc/hosts'
```

**Production**: Create a DNS A/CNAME record for `sfw.your_company.com` pointing to the firewall host.

## Step 5: Generate SSL Certificates

The firewall requires SSL certs at `/etc/nginx/ssl/` inside the container. Generate them on the host **before** starting the container — the container process may not have write permissions to the mounted volume.

### Self-Signed (Development/Testing)

```bash
mkdir -p ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/privkey.pem \
  -out ssl/fullchain.pem \
  -subj "/CN=sfw.your_company.com" \
  -addext "subjectAltName=DNS:sfw.your_company.com,DNS:localhost"
chmod 644 ssl/fullchain.pem ssl/privkey.pem
```

## Trusting Self-Signed Certificates

If using self-signed certs, trust them on client machines:

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

### Custom Certificates (Production)

```bash
mkdir -p ssl
cp /path/to/cert.pem ssl/fullchain.pem
cp /path/to/key.pem ssl/privkey.pem
chmod 644 ssl/fullchain.pem ssl/privkey.pem
```

### Generate Self-Signed with Custom SANs

```bash
mkdir -p ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/privkey.pem \
  -out ssl/fullchain.pem \
  -subj "/CN=*.company.com" \
  -addext "subjectAltName=DNS:sfw.company.com,DNS:npm.company.com,DNS:pypi.company.com"
```

## Step 6: DNS / Host Entry

For path-based routing, the firewall domain must resolve to the firewall host.

**Local testing** (add to `/etc/hosts`):

```bash
sudo sh -c 'printf "127.0.0.1   sfw.your_company.com\n::1         sfw.your_company.com\n" >> /etc/hosts'
```

**Production**: Create a DNS A/CNAME record for `sfw.your_company.com` pointing to the firewall host.

## Step 7: Start the Firewall

```bash
docker pull socketdev/socket-registry-firewall
docker compose up -d
```

Verify it's running:

```bash
curl -k https://localhost:8443/health
# Expected: {"status":"healthy","version":"..."}
```

## Step 8: Configure Package Managers

### npm

```bash
npm config set registry http://sfw.your_company.com:8080/npm/
npm config set strict-ssl false  # only for self-signed certs
```

Test:

```bash
npm install lodash --loglevel verbose   # should succeed
npm install lodahs                       # should be blocked (typosquat)
```

### pip

```bash
pip config set global.index-url https://sfw.your_company.com:8443/pypi/simple
pip config set global.trusted-host "sfw.your_company.com"  # only for self-signed certs
```

Test:

```bash
pip install requests
```

### Maven

Add to `~/.m2/settings.xml`:

```xml
<settings>
  <mirrors>
    <mirror>
      <id>socket-firewall</id>
      <url>https://sfw.your_company.com:8443/maven</url>
      <mirrorOf>*</mirrorOf>
    </mirror>
  </mirrors>
</settings>
```

Test:

```bash
mvn install -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true
```

### Gradle

Edit `settings.gradle`:

```groovy
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.PREFER_SETTINGS)
    repositories {
        maven { url "https://sfw.your_company.com:8443/maven" }
    }
}
```

### Cargo

```bash
# In .cargo/config.toml
[registries.socket]
index = "https://sfw.your_company.com:8443/cargo"
```

### Go

```bash
export GOPROXY=https://sfw.your_company.com:8443/go,direct
export GONOSUMCHECK=*  # only for self-signed certs
```

### RubyGems

```bash
gem sources --add https://sfw.your_company.com:8443/rubygems/ --remove https://rubygems.org/
# or in Gemfile:
source "https://sfw.your_company.com:8443/rubygems/"
```

### NuGet

```bash
dotnet nuget add source https://sfw.your_company.com:8443/nuget/v3/index.json -n socket-firewall
```

## Downstream with Private Registry Mirrors

If developers pull from an Artifactory or Nexus instance (not public registries), point the firewall's upstream at your private mirror:

```yaml
path_routing:
  enabled: true
  domain: sfw.your_company.com
  routes:
    - path: /npm
      upstream: https://artifactory.company.com/artifactory/api/npm/npm-remote
      registry: npm
    - path: /pypi
      upstream: https://artifactory.company.com/artifactory/api/pypi/pypi-remote/simple
      registry: pypi
    - path: /maven
      upstream: https://artifactory.company.com/artifactory/maven-remote
      registry: maven
```

Developers hit the firewall, the firewall scans and proxies to Artifactory, Artifactory fetches from the public registry.

```
Developer  --->  Socket Firewall  --->  Artifactory  --->  Public Registry
```

### Auto-Discovery

For large Artifactory/Nexus deployments with many repositories, use auto-discovery to sync routes automatically:

```yaml
path_routing:
  enabled: true
  domain: sfw.your_company.com
  mode: artifactory  # or 'nexus'

  private_registry:
    api_url: https://artifactory.company.com/artifactory
    api_key: your-artifactory-api-key
    interval: 5m
    include_pattern: ".*"
    exclude_pattern: "(tmp|test)-.*"
```

Routes update automatically when repositories are added or removed.

<br />

```bash
mkdir -p ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/privkey.pem \
  -out ssl/fullchain.pem \
  -subj "/CN=*.company.com" \
  -addext "subjectAltName=DNS:sfw.company.com,DNS:npm.company.com,DNS:pypi.company.com"
```

## Monitoring

### Health Check

```bash
curl -k https://localhost:8443/health
```

### Logs

```bash
docker compose logs -f socket-firewall          # all logs
docker compose logs socket-firewall | grep -i block   # blocked packages
docker compose logs socket-firewall | grep -i error   # errors
```

### Splunk Integration

```yaml
splunk:
  enabled: true
  hec_url: https://splunk.company.com:8088/services/collector/event
  hec_token: your-splunk-hec-token
  index: security
  source: socket-firewall
```

### Webhook Integration

Send decision events to any HTTP endpoint:

```yaml
webhook:
  enabled: true
  url: https://siem.company.com/api/events
  auth_header: "Bearer your-api-token"
  on_block: true
  on_warn: true
```

## Troubleshooting

### Container Won't Start

```bash
docker compose logs socket-firewall
docker compose exec socket-firewall env | grep SOCKET
docker compose exec socket-firewall socket-proxy-config-tool generate --config /app/socket.yml
```

### Package Install Fails

```bash
docker compose logs socket-firewall | grep -i block    # check if blocked by policy
curl -kI https://localhost:8443/health                  # verify firewall is up
docker compose exec socket-firewall curl -I https://registry.npmjs.org  # test upstream
```

### Firewall Not Blocking

```bash
docker compose exec socket-firewall env | grep SOCKET_SECURITY_API_TOKEN  # verify token
docker compose exec socket-firewall curl https://api.socket.dev/v0/health  # verify API access
cat socket.yml | grep fail_open  # check fail-open setting
```