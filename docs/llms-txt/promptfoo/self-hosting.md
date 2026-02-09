# Source: https://www.promptfoo.dev/docs/usage/self-hosting/

# Self-hosting Promptfoo

Promptfoo provides a basic Docker image that allows you to host a server that stores evals. This guide covers various deployment methods.

Self-hosting enables you to:

- Share evals to a private instance
- Run evals in your CI/CD pipeline and aggregate results
- Keep sensitive data off your local machine

## Enterprise Customers

If you are an enterprise customer, please do not install this version. Contact us instead for credentials for the enterprise image.

The self-hosted app is an Express server serving the web UI and API.

## Method 1: Using Pre-built Docker Images (Recommended Start)

Get started quickly using a pre-built image.

### 1. Pull the Image

Pull the latest image or pin to a specific version (e.g., `0.109.1`):

```bash
# Pull latest
docker pull ghcr.io/promptfoo/promptfoo:latest

# Or pull a specific version
# docker pull ghcr.io/promptfoo/promptfoo:0.109.1
```

### 2. Run the Container

Run the container, mapping a local directory for data persistence:

```bash
docker run -d \
  --name promptfoo_container \
  -p 3000:3000 \
  -v /path/to/local_promptfoo:/home/promptfoo/.promptfoo \
  -e OPENAI_API_KEY=sk-abc123 \
  ghcr.io/promptfoo/promptfoo:latest
```

**Key Parameters:**

- **`-d`**: Run in detached mode (background).
- **`--name promptfoo_container`**: Assign a name to the container.
- **`-p 3000:3000`**: Map host port 3000 to container port 3000.
- **`-v /path/to/local_promptfoo:/home/promptfoo/.promptfoo`**: **Crucial for persistence.** Maps the container's data directory (`/home/promptfoo/.promptfoo`, containing `promptfoo.db`) to your local filesystem. Replace `/path/to/local_promptfoo` with your preferred host path (e.g., `./promptfoo_data`). **Data will be lost if this volume mapping is omitted.**
- **`-e OPENAI_API_KEY=sk-abc123`**: Example of setting an environment variable. Add necessary API keys here so users can run evals directly from the web UI. Replace `sk-abc123` with your actual key.

Access the UI at `http://localhost:3000`.

## Method 2: Using Docker Compose

For managing multi-container setups or defining configurations declaratively, use Docker Compose.

### 1. Create `docker-compose.yml`

Create a `docker-compose.yml` file in your project directory:

```yaml
version: 3.8

services:
  promptfoo_container: # Consistent service and container name
    image: ghcr.io/promptfoo/promptfoo:latest # Or pin to a specific version tag
    ports:
      - 3000:3000 # Map host port 3000 to container port 3000
    volumes:
      # Map host directory to container data directory for persistence
      # Create ./promptfoo_data on your host first!
      - ./promptfoo_data:/home/promptfoo/.promptfoo
    environment:
      # Optional: Adjust chunk size for large evals (See Troubleshooting)
      - PROMPTFOO_SHARE_CHUNK_SIZE=10
      # Add other necessary environment variables (e.g., API keys)
      - OPENAI_API_KEY=your_key_here
      # Example: Google API Key
      # - GOOGLE_API_KEY=your_google_key_here
    # Optional: Define a named volume managed by Docker (alternative to host path mapping)
    # volumes:
    #   promptfoo_data:
    #     driver: local
    # If using a named volume, change the service volume mapping to:
    #     volumes:
    #       - promptfoo_data:/home/promptfoo/.promptfoo
```

**Using Host Paths vs. Named Volumes**

The example above uses a host path mapping (`./promptfoo_data:/home/promptfoo/.promptfoo`) which clearly maps to a directory you create. Alternatively, you can use Docker named volumes (uncomment the `volumes:` section and adjust the service `volumes:`).

### 2. Create Host Directory (if using host path)

If you used `./promptfoo_data` in the `volumes` mapping, create it:

```bash
mkdir -p ./promptfoo_data
```

### 3. Run with Docker Compose

Start the container in detached mode:

```bash
docker compose up -d
```

Stop the container (data remains in `./promptfoo_data` or the named volume):

```bash
docker compose stop
```

Stop and remove the container (data remains):

```bash
docker compose down
```

## Method 3: Using Kubernetes with Helm

Helm support is currently experimental. Please report any issues you encounter.

Deploy promptfoo to Kubernetes using the provided Helm chart located within the main promptfoo repository.

**info**

Keep `replicaCount: 1` (the default) as the self-hosted server uses a local SQLite database and in-memory job queue that cannot be shared across replicas.

### Prerequisites

- A Kubernetes cluster (e.g., Minikube, K3s, GKE, EKS, AKS)
- Helm v3 installed (`brew install helm` or see [Helm docs](https://helm.sh/docs/intro/install/))
- `kubectl` configured to connect to your cluster
- Git installed

### Installation

1. **Clone the promptfoo Repository:**

   If you haven't already, clone the main promptfoo repository:

   ```bash
   git clone https://github.com/promptfoo/promptfoo.git
   cd promptfoo
   ```

2. **Install the Chart:**

   From the root of the cloned repository, install the chart using its local path. Provide a release name (e.g., `my-promptfoo`):

   ```bash
   # Install using the default values
   helm install my-promptfoo ./helm/chart/promptfoo
   ```

### Configuration

The Helm chart uses PersistentVolumeClaims (PVCs) for data persistence. By default, it creates a PVC named `promptfoo` requesting 1Gi of storage using the default StorageClass.

Customize the installation using a `values.yaml` file or `--set` flags.

**Example (`my-values.yaml`):**

```yaml
# Configure sharing to your self-hosted instance
sharing:
  apiBaseUrl: http://your-server:3000
  appBaseUrl: http://your-server:3000

# Optional: Specify a StorageClass if the default is not suitable
# storageClassName: my-ssd-storage

# Optional: Define a named volume managed by Docker (alternative to host path mapping)
# volumes:
#   promptfoo_data:
#     driver: local
# If using a named volume, change the service volume mapping to:
#     volumes:
#       - promptfoo_data:/home/promptfoo/.promptfoo

# Set the sharing target URL in this order (highest priority first):
# - Config file (`.promptfoo` directory)
# - Environment variables (`PROMPTFOO_REMOTE_API_BASE_URL` and `PROMPTFOO_REMOTE_APP_BASE_URL`)
# - Cloud configuration (set via `promptfoo auth login`)
# - Default promptfoo cloud URLs

# Example configuration:
# ui-providers.yaml
# Simple provider IDs
# - openai:gpt-5.1-mini
# - anthropic:messages:claude-sonnet-4-5-20250929

# With labels and defaults
# - id: openai:gpt-5.1
#   label: GPT-5.1 (Company Approved)
#   config:
#     temperature: 0.7
#     max_tokens: 4096

# Custom HTTP provider with env var credentials
# - id: http://llm-gateway.company.com/v1
#   label: Internal Gateway
#   config:
#     method: POST
#     headers:
#       Authorization: Bearer {{ env.INTERNAL_API_KEY }}
```

**Docker deployment:**

```bash
docker run -d \
  --name promptfoo_container \
  -p 3000:3000 \
  -v ./my_custom_data:/app/data \
  -e PROMPTFOO_CONFIG_DIR=/app/data \
  ghcr.io/promptfoo/promptfoo:latest
```

**Kubernetes ConfigMap:**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: promptfoo-providers
data:
  ui-providers.yaml:
    providers:
      - openai:gpt-5.1
      - anthropic:messages:claude-sonnet-4-5-20250929

apiVersion: apps/v1
kind: Deployment
metadata:
  name: promptfoo
spec:
  template:
    spec:
      containers:
        - name: promptfoo
          image: promptfoo/promptfoo:latest
          volumeMounts:
            - name: config
              mountPath: /home/promptfoo/.promptfoo-ui-providers.yaml
              subPath: ui-providers.yaml
      volumes:
        - name: config
          configMap: promptfoo-providers
```

**Behavior Changes**

When `ui-providers.yaml` exists:

- Only configured providers shown (replaces default ~600 providers)
- "Reference Local Provider" button hidden in eval creator
- Configuration is cached - restart required after changes: `docker restart promptfoo_container`

**Security - Credentials**

**DO NOT store API keys in ui-providers.yaml**. Use environment variables with Nunjucks syntax:

```yaml
# ui-providers.yaml
providers:
  - id: http://internal-api.com/v1
    config:
      headers:
        Authorization: Bearer {{ env.INTERNAL_API_KEY }}
```

**Pass via environment**

```bash
docker run -e INTERNAL_API_KEY=your-key ....
```

For Kubernetes, use Secrets (not ConfigMaps) for sensitive data.

**Configuration fields:**

```yaml
providers:
  - id: string # Required - Provider identifier
    label: string # Optional - Display name
    config: # Optional - Default settings
      temperature: number # 0.0-2.0
      max_tokens: number
      # HTTP providers
      method: string # POST, GET, etc.
      headers: object # Custom headers
      # Cloud providers
      region: string # AWS region, etc.
```

**Provider ID formats:**

- **OpenAI:** `openai:gpt-5.1`, `openai:gpt-5.1-mini`
- **Anthropic:** `anthropic:messages:claude-sonnet-4-5-20250929`
- **AWS Bedrock:** `bedrock:us.anthropic.claude-sonnet-4-5-20250929-v1:0`
- **Azure OpenAI:** `azureopenai:chat:deployment-name`
- **Custom HTTP:** `http://your-api.com/v1` or `https://...`

See [Provider Documentation](https://www.promptfoo.dev/docs/providers/) for complete list.

**Troubleshooting:**

**Providers not updating:** Restart required after config changes.

```bash
docker restart promptfoo_container
# or: docker compose restart
# or: kubectl rollout restart deployment/promptfoo
```

**Providers missing:** Check logs for validation errors:

```bash
docker logs promptfoo_container | grep "Invalid provider"
```

Common issues: missing `id` field, invalid provider ID format, YAML syntax errors.

**Config not detected:** Verify file location and permissions:

```bash
docker exec promptfoo_container ls -la /home/promptfoo/.promptfoo/
docker exec promptfoo_container cat /home/promptfoo/.promptfoo/ui-providers.yaml
```

File must be named `ui-providers.yaml` or `ui-providers.yml` (case-sensitive on Linux).

## Deploying Behind a Reverse Proxy with Base Path

To serve promptfoo at a URL prefix (e.g., `https://example.com/promptfoo/`), rebuild the Docker image with `VITE_PUBLIC_BASENAME` and configure your reverse proxy to strip the prefix.

### Build the Image

```bash
docker build --build-arg VITE_PUBLIC_BASENAME=/promptfoo -t my-promptfoo .
```

### Nginx Configuration

```nginx
location /promptfoo/ {
    proxy_pass http://localhost:3000/;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

### Traefik Configuration

```yaml
http:
  routers:
    promptfoo:
      rule: PathPrefix(`/promptfoo`)
      middlewares:
        - strip-promptfoo
      service: promptfoo
  middlewares:
    strip-promptfoo:
      stripPrefix:
        prefixes:
          - /promptfoo
  services:
    promptfoo:
      loadBalancer:
        servers:
          - url: http://promptfoo:3000
```

The `VITE_PUBLIC_BASENAME` build argument configures the frontend to use the correct paths for routing, API calls, and WebSocket connections.

## Specifications

### Client Requirements (Running `promptfoo` CLI)

- **OS**: Linux, macOS, Windows
- **CPU**: 2+ cores, 2.0GHz+ recommended
- **GPU**: Not required
- **RAM**: 4 GB+
- **Storage**: 10 GB+
- **Dependencies**: Node.js v20+, npm

### Server Requirements (Hosting the Web UI/API)

The server component is optional; you can run evals locally or in CI/CD without it.

**Host Machine:**

- **OS**: Any OS capable of running Docker/Kubernetes
- **CPU**: 4+ cores recommended
- **RAM**: 8GB+ (16GB recommended for heavy use)
- **Storage**: 100GB+ recommended for container volumes and database (SSD recommended for database volume)

## Troubleshooting

### Lost Data After Container Restart

**Problem**: Evals disappear after `docker compose down` or container restarts.

**Solution**: This indicates missing or incorrect volume mapping. Ensure your `docker run` command or `docker-compose.yml` correctly maps a host directory or named volume to `/home/promptfoo/.promptfoo` (or your `PROMPTFOO_CONFIG_DIR` if set) inside the container. Review the `volumes:` section in the examples above.

### Results Not Appearing in Self-Hosted UI

**Problem**: Running `promptfoo eval` stores results locally instead of showing them in the self-hosted UI.

**Solution**:

1. By default, `promptfoo eval` stores results locally (run `promptfoo view` to view them)
2. To upload results to your self-hosted instance, run `promptfoo share` after eval
3. Configure your self-hosted instance using ONE of these methods:

   **Option A: Environment Variables (temporary)**

   ```bash
   export PROMPTFOO_REMOTE_API_BASE_URL=http://your-server:3000
   export PROMPTFOO_REMOTE_APP_BASE_URL=http://your-server:3000
   ```

   **Option B: Config File (permanent - recommended)**

   ```yaml
   # promptfooconfig.yaml
   sharing:
     apiBaseUrl: http://your-server:3000
     appBaseUrl: http://your-server:3000
   ```

   Replace `your-server` with your actual server address (e.g., `192.168.1.100`, `promptfoo.internal.company.com`, etc.)

   Then run: `promptfoo eval` followed by `promptfoo share`

**What to Expect**

After running `promptfoo share`, you should see output like:

```
View results: http://192.168.1.100:3000/eval/abc-123-def
```

This URL points to your self-hosted instance, not the local viewer.

## See Also

- [Configuration Reference](https://www.promptfoo.dev/docs/configuration/reference/)
- [Command Line Interface](https://www.promptfoo.dev/docs/usage/command-line/)
- [Sharing Results](https://www.promptfoo.dev/docs/usage/sharing/)