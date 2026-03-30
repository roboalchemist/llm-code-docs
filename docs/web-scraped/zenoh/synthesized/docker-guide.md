# Zenoh Docker Deployment Guide

This guide covers running zenoh components in Docker: the router, storage backends,
and ROS 2 bridges. All official images are published on Docker Hub under the
`eclipse/` namespace.

---

## Table of Contents

- [Official Docker Images](#official-docker-images)
- [Quick Start: Zenoh Router](#quick-start-zenoh-router)
  - [Key Ports](#key-ports)
- [docker-compose: Router with Filesystem Backend](#docker-compose-router-with-filesystem-backend)
- [Connecting Applications to a Containerised Router](#connecting-applications-to-a-containerised-router)
  - [From the Host Machine](#from-the-host-machine)
  - [From Another Container (Same Compose Network)](#from-another-container-same-compose-network)
  - [Network Mode Considerations](#network-mode-considerations)
- [Multi-Container Setup](#multi-container-setup)
- [Router + InfluxDB Storage Backend](#router-influxdb-storage-backend)
- [ROS 2 Bridge in Docker](#ros-2-bridge-in-docker)
- [Configuration via Volume Mount](#configuration-via-volume-mount)
- [Environment Variables](#environment-variables)
- [Health Check](#health-check)
- [Kubernetes Deployment](#kubernetes-deployment)
  - [Basic Deployment](#basic-deployment)
  - [Service: ClusterIP vs NodePort vs LoadBalancer](#service-clusterip-vs-nodeport-vs-loadbalancer)
  - [ConfigMap for Router Configuration](#configmap-for-router-configuration)
- [Production Considerations](#production-considerations)
  - [Resource Limits](#resource-limits)
  - [Persistent Storage for Backends](#persistent-storage-for-backends)
  - [TLS Termination](#tls-termination)
  - [Logging](#logging)
- [Sources](#sources)

## Official Docker Images

| Image | Docker Hub | Tags |
|---|---|---|
| `eclipse/zenoh` | https://hub.docker.com/r/eclipse/zenoh | `latest`, `main` (nightly) |
| `eclipse/zenoh-bridge-dds` | https://hub.docker.com/r/eclipse/zenoh-bridge-dds | `latest`, `main` |
| `eclipse/zenoh-bridge-ros2dds` | https://hub.docker.com/r/eclipse/zenoh-bridge-ros2dds | `latest`, `main` |
| `eclipse/zenoh-bridge-ros1` | https://hub.docker.com/r/eclipse/zenoh-bridge-ros1 | `latest`, `main` |

All images ship multi-arch manifests covering `linux/amd64` and `linux/arm64`.

---

## Quick Start: Zenoh Router

Pull and run a standalone zenoh router with the REST plugin exposed:

```bash
docker pull eclipse/zenoh:latest

docker run --init -d \
  --name zenoh-router \
  -p 7447:7447/tcp \
  -p 7446:7446/udp \
  -p 8000:8000 \
  eclipse/zenoh:latest
```

Verify the router is up via the REST API health endpoint:

```bash
curl http://localhost:8000/@/local/router/
```

### Key Ports

| Port | Protocol | Purpose |
|---|---|---|
| `7447` | TCP | Zenoh session transport (peer/client connections) |
| `7446` | UDP | Zenoh scouting / multicast discovery |
| `8000` | TCP | REST plugin HTTP interface (optional) |

---

## docker-compose: Router with Filesystem Backend

The filesystem backend stores zenoh key/values on disk. Mount a host directory
as the storage root.

```yaml
# docker-compose.yml
version: "3.9"

services:
  zenoh:
    image: eclipse/zenoh:latest
    restart: unless-stopped
    ports:
      - 7447:7447/tcp
      - 7446:7446/udp
      - 8000:8000
    volumes:
      - ./zenoh_config:/root/.zenoh        # config files (e.g. DEFAULT_CONFIG.json5)
      - ./zenoh_filesystem:/filesystem     # filesystem backend storage root
    environment:
      - RUST_LOG=info
      - ZENOH_BACKEND_FS_ROOT=/filesystem
    networks:
      - zenoh-nw

networks:
  zenoh-nw:
    driver: bridge
```

Start with `docker-compose up -d`.

---

## Connecting Applications to a Containerised Router

### From the Host Machine

Client applications on the host connect to the published port:

```python
# Python
import zenoh
conf = zenoh.Config()
conf.insert_json5("connect/endpoints", '["tcp/localhost:7447"]')
session = zenoh.open(conf)
```

```rust
// Rust
let mut config = zenoh::Config::default();
config.insert_json5("connect/endpoints", r#"["tcp/localhost:7447"]"#).unwrap();
let session = zenoh::open(config).await.unwrap();
```

### From Another Container (Same Compose Network)

Reference the service name as the hostname:

```python
conf.insert_json5("connect/endpoints", '["tcp/zenoh:7447"]')
```

### Network Mode Considerations

- **Bridge networking** (default): Publish ports explicitly (`-p 7447:7447/tcp`).
  UDP multicast scouting does not traverse bridge networks — set explicit
  `connect/endpoints` in client config instead of relying on scouting.
- **Host networking** (`--net host`, Linux only): Full multicast scouting works.
  Required for DDS/ROS 2 bridges (see below). Not supported on Docker Desktop
  for macOS or Windows.

---

## Multi-Container Setup

Router + application container sharing a network, with the REST API available
for external tooling:

```yaml
# docker-compose.yml
version: "3.9"

services:
  zenoh:
    image: eclipse/zenoh:latest
    restart: unless-stopped
    ports:
      - 7447:7447/tcp
      - 7446:7446/udp
      - 8000:8000
    environment:
      - RUST_LOG=info
    networks:
      - zenoh-nw

  my-app:
    image: my-zenoh-app:latest
    depends_on:
      - zenoh
    environment:
      - ZENOH_ROUTER=tcp/zenoh:7447
    networks:
      - zenoh-nw

networks:
  zenoh-nw:
    driver: bridge
```

The application container reads `ZENOH_ROUTER` and passes it to the zenoh
`connect/endpoints` config key at startup.

---

## Router + InfluxDB Storage Backend

```yaml
# docker-compose.yml
version: "3.9"

services:
  influxdb:
    image: influxdb:latest
    restart: unless-stopped
    ports:
      - 8086:8086
    volumes:
      - influxdb-volume:/var/lib/influxdb
    networks:
      - zenoh-nw

  zenoh:
    image: eclipse/zenoh:latest
    restart: unless-stopped
    ports:
      - 7447:7447/tcp
      - 7446:7446/udp
      - 8000:8000
    volumes:
      - ./zenoh_config:/root/.zenoh
    environment:
      - RUST_LOG=info
    networks:
      - zenoh-nw

volumes:
  influxdb-volume:

networks:
  zenoh-nw:
    driver: bridge
```

After starting, add the InfluxDB storage volume via the REST admin space:

```bash
# Add influxdb volume plugin
curl -X PUT -H 'content-type:application/json' \
  -d '{"url":"http://influxdb:8086"}' \
  http://localhost:8000/@/local/router/config/plugins/storage_manager/volumes/influxdb

# Create a storage
curl -X PUT -H 'content-type:application/json' \
  -d '{"key_expr":"demo/**","volume":{"id":"influxdb","db":"zenoh_demo","create_db":true}}' \
  http://localhost:8000/@/local/router/config/plugins/storage_manager/storages/demo
```

---

## ROS 2 Bridge in Docker

The `zenoh-bridge-ros2dds` image connects a ROS 2 DDS domain to zenoh.

> **Important**: DDS uses UDP multicast, which does not work between a container
> and its host on Docker's bridge network. Use `--net host` on Linux. This flag
> is not supported on Docker Desktop for macOS or Windows — on those platforms
> run the bridge natively.

```bash
# Pull the image
docker pull eclipse/zenoh-bridge-ros2dds:latest

# Run with host networking so DDS multicast reaches ROS 2 nodes on the host
docker run --init --net host eclipse/zenoh-bridge-ros2dds:latest
```

The bridge accepts the same CLI flags as the native binary:

```bash
docker run --init --net host eclipse/zenoh-bridge-ros2dds:latest \
  --rest-http-port 8001 \
  -e tcp/my-zenoh-router:7447
```

**DDS bridge** (older, for ROS 2 with explicit DDS configuration):

```bash
docker pull eclipse/zenoh-bridge-dds:latest
docker run --init --net host eclipse/zenoh-bridge-dds:latest
```

---

## Configuration via Volume Mount

Mount a `DEFAULT_CONFIG.json5` to customise the router at startup:

```bash
docker run --init -d \
  --name zenoh-router \
  -p 7447:7447/tcp \
  -p 8000:8000 \
  -v $(pwd)/my_config.json5:/root/.zenoh/DEFAULT_CONFIG.json5:ro \
  eclipse/zenoh:latest
```

Example minimal config enabling the REST plugin and setting the router mode:

```json5
// my_config.json5
{
  mode: "router",
  listen: {
    endpoints: ["tcp/0.0.0.0:7447"]
  },
  plugins: {
    rest: { http_port: 8000 }
  }
}
```

---

## Environment Variables

| Variable | Purpose | Example |
|---|---|---|
| `RUST_LOG` | Log verbosity for the zenoh process | `info`, `debug`, `zenoh=debug` |
| `ZENOH_BACKEND_FS_ROOT` | Root directory for filesystem backend | `/filesystem` |

Zenoh itself does not expose a `ZENOH_CONFIG` env var — configuration is
supplied via the mounted `DEFAULT_CONFIG.json5` or CLI flags (`-c config.json5`).

---

## Health Check

The REST plugin (`http_port: 8000`) provides a lightweight liveness endpoint:

```bash
# Returns JSON info about the local router — use as a liveness probe
curl --fail --max-time 5 http://localhost:8000/@/local/router/
```

Docker `HEALTHCHECK` example:

```dockerfile
HEALTHCHECK --interval=15s --timeout=5s --retries=3 \
  CMD curl --fail --silent http://localhost:8000/@/local/router/ || exit 1
```

Kubernetes liveness probe:

```yaml
livenessProbe:
  httpGet:
    path: /@/local/router/
    port: 8000
  initialDelaySeconds: 10
  periodSeconds: 15
  timeoutSeconds: 5
  failureThreshold: 3
```

---

## Kubernetes Deployment

### Basic Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: zenoh-router
  labels:
    app: zenoh-router
spec:
  replicas: 1
  selector:
    matchLabels:
      app: zenoh-router
  template:
    metadata:
      labels:
        app: zenoh-router
    spec:
      containers:
        - name: zenoh-router
          image: eclipse/zenoh:latest
          ports:
            - containerPort: 7447
              protocol: TCP
              name: zenoh-tcp
            - containerPort: 7446
              protocol: UDP
              name: zenoh-udp
            - containerPort: 8000
              protocol: TCP
              name: rest-api
          env:
            - name: RUST_LOG
              value: "info"
          resources:
            requests:
              cpu: "100m"
              memory: "64Mi"
            limits:
              cpu: "500m"
              memory: "256Mi"
          livenessProbe:
            httpGet:
              path: /@/local/router/
              port: 8000
            initialDelaySeconds: 10
            periodSeconds: 15
          volumeMounts:
            - name: zenoh-config
              mountPath: /root/.zenoh
              readOnly: true
      volumes:
        - name: zenoh-config
          configMap:
            name: zenoh-config
```

### Service: ClusterIP vs NodePort vs LoadBalancer

| Type | Use Case |
|---|---|
| `ClusterIP` | In-cluster only — zenoh clients run as pods in the same namespace |
| `NodePort` | External clients on the same LAN, or during development |
| `LoadBalancer` | Cloud deployments requiring external TCP access |

```yaml
apiVersion: v1
kind: Service
metadata:
  name: zenoh-router
spec:
  selector:
    app: zenoh-router
  type: ClusterIP          # Change to NodePort or LoadBalancer as needed
  ports:
    - name: zenoh-tcp
      port: 7447
      targetPort: 7447
      protocol: TCP
    - name: rest-api
      port: 8000
      targetPort: 8000
      protocol: TCP
```

> Note: UDP port 7446 (scouting) is typically not exposed via K8s Services.
> Pods connect to the router by setting `connect/endpoints` explicitly rather
> than relying on multicast scouting.

### ConfigMap for Router Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: zenoh-config
data:
  DEFAULT_CONFIG.json5: |
    {
      mode: "router",
      listen: { endpoints: ["tcp/0.0.0.0:7447"] },
      plugins: { rest: { http_port: 8000 } }
    }
```

---

## Production Considerations

### Resource Limits

Zenoh is written in Rust and is memory-efficient. Typical sizing for a router
handling moderate pub/sub traffic:

- CPU: 100m request / 500m limit
- Memory: 64Mi request / 256Mi limit

Throughput-intensive deployments (millions of msg/s) benefit from higher CPU
limits and pinning to dedicated nodes.

### Persistent Storage for Backends

Mount named volumes for InfluxDB, RocksDB, or filesystem backend data to
survive container restarts:

```yaml
volumes:
  - influxdb-data:/var/lib/influxdb   # InfluxDB
  - zenoh-rocksdb:/rocksdb-data       # RocksDB backend
  - zenoh-fs:/filesystem              # Filesystem backend
```

### TLS Termination

For external-facing deployments, terminate TLS at an ingress (e.g., NGINX, HAProxy)
in front of port 7447, or configure zenoh's native TLS:

```json5
// In DEFAULT_CONFIG.json5
{
  listen: {
    endpoints: ["tls/0.0.0.0:7447"]
  },
  transport: {
    unicast: {
      tls: {
        server_certificate: "/certs/server.pem",
        server_private_key: "/certs/server_key.pem",
        root_ca_certificate: "/certs/ca.pem"
      }
    }
  }
}
```

Mount the certificate files via a Kubernetes Secret:

```yaml
volumeMounts:
  - name: zenoh-tls
    mountPath: /certs
    readOnly: true
volumes:
  - name: zenoh-tls
    secret:
      secretName: zenoh-tls-certs
```

### Logging

Set `RUST_LOG=info` for production. Use `RUST_LOG=zenoh=debug` to debug routing
or session establishment issues without overwhelming log volume.

---

## Sources

- `eclipse/zenoh` Docker image: https://hub.docker.com/r/eclipse/zenoh
- `eclipse/zenoh-bridge-ros2dds`: https://hub.docker.com/r/eclipse/zenoh-bridge-ros2dds
- `eclipse/zenoh-bridge-dds`: https://hub.docker.com/r/eclipse/zenoh-bridge-dds
- Storage backend compose examples: zenoh-backend-filesystem and zenoh-backend-influxdb repos
- DDS UDP multicast Docker limitation: moby/moby#23659, moby/libnetwork#2397

## See Also

- [Config Connect Listen](config-connect-listen.md) — how to configure explicit endpoints (needed because multicast scouting doesn't work in Docker bridge networks)
- [Scouting Guide](scouting-guide.md) — scouting mechanisms and why Docker bridge networks require static endpoints
- [Node Types Guide](node-types-guide.md) — router, peer, and client deployment patterns illustrated by the Docker examples
