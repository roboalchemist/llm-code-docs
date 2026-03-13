# Source: https://docs.dify.ai/en/self-host/troubleshooting/docker-issues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Docker Issues

## Network & Connectivity

### 502 Bad Gateway

Nginx is forwarding to wrong container IPs. Get current container IPs:

```bash  theme={null}
docker ps -q | xargs -n 1 docker inspect --format '{{ .Name }}: {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
```

Find these lines:

```
/docker-web-1: 172.19.0.5
/docker-api-1: 172.19.0.7
```

Update `dify/docker/nginx/conf.d`:

* Replace `http://api:5001` with `http://172.19.0.7:5001`
* Replace `http://web:3000` with `http://172.19.0.5:3000`

Restart nginx or reload configuration. Note: IPs change on container restart.

### Cannot access localhost services

Docker containers can't reach host services via `127.0.0.1`. Use your machine's local network IP instead.

Example: For OpenLLM running on host, configure Dify with `http://192.168.1.100:port` (your actual local IP).

### Page loads forever with CORS errors

Domain/URL changes cause cross-origin issues. Update in `docker-compose.yml`:

* `CONSOLE_API_URL` - Backend URL for console API
* `CONSOLE_WEB_URL` - Frontend URL for console web
* `SERVICE_API_URL` - Service API URL
* `APP_API_URL` - WebApp API backend URL
* `APP_WEB_URL` - WebApp URL

## Mounting & Volumes

### Nginx configuration mount failure

Error:

```
Error mounting "/run/desktop/mnt/host/d/Documents/docker/nginx/nginx.conf" to rootfs at "/etc/nginx/nginx.conf": not a directory
```

Clone the complete project and run from docker directory:

```bash  theme={null}
git clone https://github.com/langgenius/dify.git
cd dify/docker
docker compose up -d
```

### Port conflicts

Port 80 already in use? Either:

1. Stop the conflicting service (usually Apache/Nginx):
   ```bash  theme={null}
   sudo service nginx stop
   sudo service apache2 stop
   ```

2. Or change port mapping in `docker-compose.yaml`:
   ```yaml  theme={null}
   ports:
     - "8080:80"  # Map to different port
   ```

## Container Management

### View background shell outputs

List running shells:

```bash  theme={null}
docker exec -it docker-api-1 ls /tmp/shells/
```

Check shell output:

```bash  theme={null}
docker exec -it docker-api-1 cat /tmp/shells/[shell-id]/output.log
```

### Container restart issues

After system reboot, containers may fail to connect. Ensure proper startup order:

```bash  theme={null}
docker compose down
docker compose up -d
```

Wait for all services to be healthy before accessing.

## SSRF Proxy

The `ssrf_proxy` container prevents Server-Side Request Forgery attacks.

### Customize proxy rules

Edit `docker/volumes/ssrf_proxy/squid.conf` to add ACL rules:

```
# Block access to sensitive internal IP
acl restricted_ip dst 192.168.101.19
acl localnet src 192.168.101.0/24

http_access deny restricted_ip
http_access allow localnet
http_access deny all
```

Restart the proxy container after changes.

### Why is SSRF\_PROXY needed?

Prevents services from making unauthorized requests to internal network resources. The proxy intercepts and filters all outbound requests from sandboxed services.


Built with [Mintlify](https://mintlify.com).