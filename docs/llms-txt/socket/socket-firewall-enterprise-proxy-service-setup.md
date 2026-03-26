# Source: https://docs.socket.dev/docs/socket-firewall-enterprise-proxy-service-setup.md

# Enterprise Proxy Service Setup

Socket Firewall can run as a persistent service, making it ideal for Docker deployments, CI/CD pipeline integration, and environments where you need manual proxy configuration. In service mode, the proxy server runs continuously.

## Running the proxy service

Run Socket Firewall as a persistent service:

```bash
# Required environment variables for service mode
# Required scopes: packages, entitlements:list
export SOCKET_API_KEY=sktsec_your_api_key_here_api
export SFW_HOSTNAME=your.proxy.hostname
export SFW_CA_CERT_PATH=/path/to/ca.crt
export SFW_CA_KEY_PATH=/path/to/ca.key

# See the full list of configuration options in the documentation below

sfw --service
```

**Note:** You need to generate a CA certificate and private key before running in service mode. See [Generating Keys](socket-firewall-enterprise-generating-keys) for instructions on creating your CA keypair.

**Note:** These environment variables are only required for service mode. In wrapper mode, the CLI handles configuration automatically, requiring only the `SOCKET_API_KEY`.

## Docker Deployment

We've provided a [docker image](https://hub.docker.com/r/socketdev/socket-firewall) as a simple way to get started: `socketdev/socket-firewall`. This can be incorporated into your preferred container-management solution or pulled directly:

```shell
docker pull socketdev/socket-firewall
```

Here is an example `Dockerfile` for building and running Socket Firewall in your environment:

```
FROM debian:bullseye-slim

# netcat/curl included for healthcheck and fetching binaries
RUN apt-get update \
    && apt-get install -y netcat-openbsd curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN mkdir -p /app/certs /run/secrets

# Make sure the binary matches the host architecture
ADD https://github.com/SocketDev/firewall-release/releases/latest/download/sfw-linux-x86_64 ./sfw
RUN chmod +x ./sfw
RUN mv ./sfw /usr/local/bin/sfw

COPY ./ca.crt /app/certs/ca.crt
COPY ./ca.key /app/certs/ca.key

ENV SFW_HTTP_PORT=80
ENV SFW_HTTPS_PORT=443
EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/usr/local/bin/sfw", "--service"] 
```

It can be built like so:

```bash
docker build -t socket-firewall:latest -f Dockerfile .
```

Alternately, this Docker Compose file can be used as a starting point:

```yaml
name: socket-firewall
services:
  firewall:
    build:
      context: .
      dockerfile: ./Dockerfile
    ports:
      - "80:80"
      - "443:443"
    environment:
      - SFW_HOSTNAME=your.proxy.hostname
      - SFW_CA_CERT_PATH=/app/certs/ca.crt
      - SFW_CA_KEY_PATH=/app/certs/ca.key
    volumes:
      # You need to generate these and provide in PEM format; see
      # Generating Keys documentation for instructions.
      - path/to/socketFirewallCa.crt:/app/certs/ca.crt:ro
      - path/to/socketFirewallCa.key:/app/certs/ca.key:ro
    secrets:
      - dot-env-secrets
    healthcheck:
      test: ["CMD", "nc", "-w", "1", "-z", "localhost", "443"]
      interval: 5s
      timeout: 2s
      retries: 5

secrets:
  dot-env-secrets:
    # Should include your SOCKET_API_KEY as an entry in dotenv format
    # Required scopes: packages, entitlements:list
    file: ./.env.secrets
```

## Configuration

For detailed information about all configuration options, see the [Configuration](socket-firewall-enterprise-configuration) documentation.

## Blocked requests

When Socket Firewall blocks a package manager's request, it will:

* return a `403` response
* include a response body with a human-readable explanation for what happened
* add a `X-Block-Reason` header containing a comma-delimited list of reasons for the block

## Verify service is functioning correctly

After standing up the service, you should confirm that the service is healthy and ready to filter network traffic from package managers.

You can accomplish this in the terminal:

```
curl -v \
  --proxy https://your-firewall-host:443 \
  --proxy-cacert path/to/socketFirewallCa.crt \
  --cacert path/to/socketFirewallCa.crt \
  https://registry.npmjs.org/lodash/-/lodash-1.0.0.tgz
  -o output.tgz
```

**Important:** You should make sure to pick a package URL that you know will be filtered based on your Socket org preferences.

If the CA is configured correctly, if the service is running, and if Socket determines the package should be blocked, you'll see output similar to the following:

```
* Host your-firewall-host:443 was resolved.
* IPv6: (none)
* IPv4: x.x.x.x
*   Trying x.x.x.x:443...
* Connected to your-firewall-host (x.x.x.x) port 443
* ALPN: curl offers http/1.1
* (304) (OUT), TLS handshake, Client hello (1):
*  CAfile: /path/to/socketFirewallCa.crt
*  CApath: none
* (304) (IN), TLS handshake, Server hello (2):
* (304) (IN), TLS handshake, Unknown (8):
* (304) (IN), TLS handshake, Certificate (11):
* (304) (IN), TLS handshake, CERT verify (15):
* (304) (IN), TLS handshake, Finished (20):
* (304) (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / AEAD-AES256-GCM-SHA384 / [blank] / UNDEF
* ALPN: server accepted http/1.1
* Proxy certificate:
*  subject: CN=your-firewall-host
*  start date: Aug 24 02:02:23 2025 GMT
*  expire date: Aug 24 02:02:23 2026 GMT
*  subjectAltName: host "your-firewall-host" matched cert's "your-firewall-host"
*  issuer: CN=Socket Security CA; O=Socket Security
*  SSL certificate verify ok.
* CONNECT tunnel: HTTP/1.1 negotiated
* allocate connect buffer
* Establish HTTP proxy tunnel to registry.npmjs.org:443
> CONNECT registry.npmjs.org:443 HTTP/1.1
> Host: registry.npmjs.org:443
> User-Agent: curl/8.7.1
> Proxy-Connection: Keep-Alive
>
< HTTP/1.1 200 Connection Established
<
* CONNECT phase completed
* CONNECT tunnel established, response 200
* ALPN: curl offers h2,http/1.1
* (304) (OUT), TLS handshake, Client hello (1):
* (304) (IN), TLS handshake, Server hello (2):
* (304) (IN), TLS handshake, Unknown (8):
* (304) (IN), TLS handshake, Certificate (11):
* (304) (IN), TLS handshake, CERT verify (15):
* (304) (IN), TLS handshake, Finished (20):
* (304) (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / AEAD-CHACHA20-POLY1305-SHA256 / [blank] / UNDEF
* ALPN: server did not agree on a protocol. Uses default.
* Server certificate:
*  subject: CN=registry.npmjs.org
*  start date: Aug 24 02:08:28 2025 GMT
*  expire date: Aug 24 02:08:28 2026 GMT
*  subjectAltName: host "registry.npmjs.org" matched cert's "registry.npmjs.org"
*  issuer: CN=Socket Security CA; O=Socket Security
*  SSL certificate verify ok.
* using HTTP/1.x
> GET /lodash/-/lodash-1.0.0.tgz HTTP/1.1
> Host: registry.npmjs.org
> User-Agent: curl/8.7.1
> Accept: */*
>
* Request completely sent off
< HTTP/1.1 403 Forbidden
< Content-Type: text/plain
< Connection: close
< X-Block-Reason: npm package 'lodash@1.0.0' was blocked
<
* Closing connection
Package blocked for violating organization security policy
```