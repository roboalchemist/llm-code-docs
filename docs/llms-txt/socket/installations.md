# Source: https://docs.socket.dev/docs/installations.md

# Installations

# Installation Guide

Socket Registry Firewall can be deployed using two installation methods:

1. **Pre-built Docker Image** (Recommended) - Pull and run the official image from Docker Hub
2. **Tarball Installation** - Build your own image using the firewall tarball for custom deployments

## Method 1: Pre-built Docker Image (Recommended)

The simplest way to deploy Socket Registry Firewall. Best for most users who have internet access and can pull from Docker Hub.

### Prerequisites

* Docker 20.10+ and Docker Compose 2.0+
* Socket.dev API key with scopes: `packages:list`, `entitlements:list`
* Internet connectivity to pull from Docker Hub

### Quick Start

#### 1. Get Socket API Key

1. Sign up at [Socket.dev](https://socket.dev/)
2. Go to [Settings → API Keys](https://socket.dev/dashboard/organization/settings/api-keys)
3. Create API key with required scopes: `packages:list`, `entitlements:list`

#### 2. Set API Token

```bash
# Create .env file
cat > .env <<EOF
SOCKET_SECURITY_API_TOKEN=your-api-key-here
EOF
```

Or export directly:

```bash
export SOCKET_SECURITY_API_TOKEN=your-api-key-here
```

#### 3. Create Configuration

Create `socket.yml`:

```yaml
socket:
  api_url: https://api.socket.dev

ports:
  http: 8080
  https: 8443

path_routing:
  enabled: true
  domain: sfw.company.com
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

nginx:
  worker_processes: 2
  worker_connections: 4096
```

#### 4. Create Docker Compose File

Create `docker-compose.yml`:

```yaml
services:
  socket-firewall:
    image: socketdev/socket-registry-firewall:latest
    ports:
      - "8080:8080"   # HTTP (redirects to HTTPS)
      - "8443:8443"   # HTTPS
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

#### 5. Generate SSL Certificates

```bash
mkdir -p ssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ssl/privkey.pem \
  -out ssl/fullchain.pem \
  -subj "/CN=sfw.company.com" \
  -addext "subjectAltName=DNS:sfw.company.com,DNS:localhost"
chmod 644 ssl/fullchain.pem ssl/privkey.pem
```

#### 6. Start the Firewall

```bash
docker pull socketdev/socket-registry-firewall:latest
docker compose up -d
```

#### 7. Verify

```bash
# Check health endpoint
curl -fk https://localhost:8443/health
# Expected: {"status":"healthy","version":"1.x.x"}

# View logs
docker compose logs -f socket-firewall
```

***

## Method 2: Tarball Installation

Build your own Docker image using Socket's firewall tarball. Ideal for custom base images or security requirements that mandate building from source in your own registry.

### When to Use Tarball Installation

* **Custom base images** - Need specific OpenResty version or OS distribution
* **Security requirements** - Must build and scan images in your own CI/CD pipeline
* **Custom modifications** - Need to add monitoring agents, security tools, or custom configurations
* **Private registries** - Push built images to your internal container registry

### Prerequisites

1. **Tarball file** - Download from [github.com/SocketDev/socket-registry-firewall](https://github.com/SocketDev/socket-registry-firewall/releases)
   * Choose the correct architecture: `socket-firewall-{version}.amd64.tgz` (x86\_64) or `socket-firewall-{version}.arm64.tgz` (ARM64/M1/M2)
2. **OpenResty base image** - Compatible with `openresty/openresty:1.27.1.2-11-alpine` or similar
3. **Entrypoint script** - Download from the [Github Repository](https://github.com/SocketDev/socket-registry-firewall/blob/main/entrypoint.sh)
4. Docker build tools and permissions

### Installation Steps

#### 1. Download Required Files

```bash
# Download tarball and entrypoint for your architecture
# Replace {version} and {arch} with your values
wget https://github.com/SocketDev/socket-registry-firewall/releases/download/v{version}/socket-firewall-{version}.{arch}.tgz
wget https://github.com/SocketDev/socket-registry-firewall/blob/main/entrypoint.sh

# Make entrypoint executable
chmod +x entrypoint.sh
```

#### 2. Create Dockerfile

Create a `Dockerfile` in your project directory:

```dockerfile
FROM openresty/openresty:1.27.1.2-11-alpine

# Copy and extract the Socket Firewall tarball
# Replace with your actual tarball filename
COPY socket-firewall-1.1.94.amd64.tgz /app/install/socket-firewall.tgz
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh \
  && tar -xzf /app/install/socket-firewall.tgz -C /

# Install basic dependencies
RUN apk add --no-cache curl ca-certificates git openssl bash && \
    # Prefer IPv4 over IPv6 to avoid upstream IPv6 connection attempts
    printf 'precedence ::ffff:0:0/96  100\n' >> /etc/gai.conf || true

# Install lua-resty libraries
RUN cd /tmp && \
    # Install lua-resty-http
    git clone https://github.com/ledgetech/lua-resty-http.git && \
    cd lua-resty-http && \
    cp -r lib/resty/* /usr/local/openresty/lualib/resty/ && \
    cd /tmp && \
    # Install lua-resty-openssl (needed for HTTPS)
    git clone https://github.com/fffonion/lua-resty-openssl.git && \
    cd lua-resty-openssl && \
    cp -r lib/resty/* /usr/local/openresty/lualib/resty/ && \
    cd /tmp && \
    # Install lua-resty-redis (needed for Redis caching)
    git clone https://github.com/openresty/lua-resty-redis.git && \
    cd lua-resty-redis && \
    cp lib/resty/redis.lua /usr/local/openresty/lualib/resty/ && \
    cd / && \
    rm -rf /tmp/lua-resty-http /tmp/lua-resty-openssl /tmp/lua-resty-redis

WORKDIR /app

ENTRYPOINT ["/app/entrypoint.sh"]
```

**Important**: Update the tarball filename in the `COPY` line to match your downloaded file.

#### 3. Create Docker Compose File

Create `docker-compose.yml`:

```yaml
services:
  socket-firewall:
    build:
      context: .
      dockerfile: Dockerfile
    image: my-registry.company.com/socket-firewall:latest
    ports:
      - "8080:8080"   # HTTP (redirects to HTTPS)
      - "8443:8443"   # HTTPS
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

#### 4. Create Configuration

Create `socket.yml` (same format as pre-built image):

```yaml
socket:
  api_url: https://api.socket.dev

ports:
  http: 8080
  https: 8443

path_routing:
  enabled: true
  domain: sfw.company.com
  routes:
    - path: /npm
      upstream: https://registry.npmjs.org
      registry: npm
    - path: /pypi
      upstream: https://pypi.org
      registry: pypi

nginx:
  worker_processes: 2
  worker_connections: 4096
```

#### 5. Build and Start

```bash
# Build the image
docker compose build

# (Optional) Push to private registry
docker tag my-registry.company.com/socket-firewall:latest \
  my-registry.company.com/socket-firewall:1.1.94
docker push my-registry.company.com/socket-firewall:latest
docker push my-registry.company.com/socket-firewall:1.1.94

# Start the firewall
docker compose up -d

# View logs
docker compose logs -f socket-firewall
```

#### 6. Verify

```bash
# Check health endpoint
curl -fk https://localhost:8443/health

# Expected response:
# {"status":"healthy","version":"1.1.94"}

# Check startup logs
docker compose logs socket-firewall | grep -i "socket firewall"
```

### Tarball Contents

The Socket Firewall tarball includes:

* `/usr/local/bin/socket-proxy-config-tool` - Configuration generation CLI
* `/usr/local/openresty/lualib/socket/*.lua` - Lua modules for package parsing and security checks
* `/usr/local/openresty/nginx/conf/snippets/` - Nginx configuration templates
* Supporting files for all 9 ecosystems (npm, PyPI, Maven, Cargo, RubyGems, OpenVSX, NuGet, Go, Conda)

All files extract to standard OpenResty paths, making the tarball compatible with any OpenResty-based image.

### Customization Options

When using tarball installation, you can:

* **Use different base images** - Change `FROM` to use specific OpenResty versions or distributions (Alpine, Debian, Ubuntu)
* **Add security tools** - Layer in vulnerability scanners, monitoring agents, or compliance tools
* **Modify dependencies** - Pin specific versions of lua-resty libraries
* **Custom entrypoint logic** - Add initialization scripts or health checks
* **Multi-stage builds** - Use multi-stage Dockerfiles to minimize final image size

***

## Troubleshooting

### Pre-built Image Issues

**Container won't start:**

```bash
# Check logs
docker compose logs socket-firewall

# Verify API token is set
docker compose exec socket-firewall env | grep SOCKET_SECURITY_API_TOKEN

# Test config generation
docker compose exec socket-firewall socket-proxy-config-tool generate --config /app/socket.yml
```

**Health check failing:**

```bash
# Check nginx is running
docker compose exec socket-firewall ps aux | grep nginx

# Test SSL certificate
docker compose exec socket-firewall openssl s_client -connect localhost:8443 < /dev/null

# Check port binding
docker compose ps
```

### Tarball Build Issues

**Build fails on tarball extraction:**

```bash
# Verify tarball integrity
tar -tzf socket-firewall-1.1.94.amd64.tgz | head

# Check file permissions
ls -la socket-firewall-1.1.94.amd64.tgz
```

**Lua library installation fails:**

```bash
# Test git connectivity
docker run --rm openresty/openresty:1.27.1.2-11-alpine \
  sh -c "apk add git && git clone https://github.com/ledgetech/lua-resty-http.git"
```

**Architecture mismatch:**

```bash
# Check your system architecture
uname -m
# x86_64 → use amd64 tarball
# aarch64 or arm64 → use arm64 tarball

# Pull matching base image
docker pull --platform linux/amd64 openresty/openresty:1.27.1.2-11-alpine
# or
docker pull --platform linux/arm64 openresty/openresty:1.27.1.2-11-alpine
```

## Support

* **Documentation**: [https://docs.socket.dev](https://docs.socket.dev)
* **GitHub Releases**: [https://github.com/SocketDev/socket-registry-firewall/releases](https://github.com/SocketDev/socket-registry-firewall/releases)
* **Email**: [support@socket.dev](mailto:support@socket.dev)