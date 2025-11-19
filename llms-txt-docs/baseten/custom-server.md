# Source: https://docs.baseten.co/development/model/custom-server.md

# Deploy Custom servers from Docker Images

> A config.yaml is all you need

If you have an existing API server packaged in a **Docker image**—whether an open-source server like [vLLM](https://github.com/vllm-project/vllm) or a custom-built image—you can deploy it on Baseten **with just a `config.yaml` file**.

<Info>
  Custom servers also support WebSocket deployments. For WebSocket-specific configuration, see [WebSockets documentation](/development/model/websockets#websocket-usage-with-custom-servers).
</Info>

## 1. Configuring a Custom Server in `config.yaml`

Define a **Docker-based server** by adding `docker_server`:

```yaml config.yaml theme={"system"}
base_image:
  image: vllm/vllm-openai:latest
docker_server:
  start_command: vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --port 8000 --max-model-len 1024
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /v1/chat/completions
  server_port: 8000
```

### Key Configurations

| Field                | Required | Description                                                                                                                                                                                                                                         |
| -------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_command`      | ✅        | Command to start the server                                                                                                                                                                                                                         |
| `predict_endpoint`   | ✅        | Endpoint for serving requests (only one per model). This maps your server's inference endpoint to Baseten's prediction endpoint                                                                                                                     |
| `server_port`        | ✅        | Port where the server runs                                                                                                                                                                                                                          |
| `readiness_endpoint` | ✅        | Used for [Kubernetes readiness probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/#readiness-probe) to determine when the container is ready to accept traffic. This must match an endpoint on your server |
| `liveness_endpoint`  | ✅        | Used for [Kubernetes liveness probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/#liveness-probe) to determine if the container **needs to be restarted**. This must match an endpoint on your server      |

### Understanding Readiness vs. Liveness

Both probes run continuously after your container starts, but serve different purposes:

* **Readiness probe**: Answers "Can I handle requests right now?" When it fails, Kubernetes stops sending traffic to the container (but doesn't restart it). Use this to prevent traffic during startup or temporary unavailability.

* **Liveness probe**: Answers "Am I healthy enough to keep running?" When it fails, Kubernetes restarts the container. Use this to recover from deadlocks or hung processes.

For most servers, using the same endpoint (like `/health`) for both is sufficient—as long as it accurately reflects whether your server can handle requests. The key difference is the action taken: readiness controls traffic routing, while liveness controls container lifecycle.

**Initial delays**: Both probes wait before starting checks to allow your server time to start up. See [Custom health checks](/development/model/custom-health-checks) for configuration details.

### Important: Docker Image Requirements

**Container file system**: The `/app` directory is used internally by Baseten. The model container runs as a nonroot user on some configurations, but `/app` and `/tmp` directories are still writable.

<Warning>
  **Image caching**: When using tags like `:latest`, Baseten may not detect changes in the image and may use the cached copy instead. If you update an image with the same tag, Baseten might not detect the change and will reload the cached version. To avoid this, use **image digests** instead of tags when referencing updated images:

  ```yaml  theme={"system"}
  base_image:
    image: your-registry/your-image@sha256:abc123def456...
  ```

  This ensures Baseten always pulls the exact version you specify.
</Warning>

### Endpoint Mapping

<Tip>
  While `predict_endpoint` is required, you can still access any route in your server using the [sync](https://docs.baseten.co/inference/calling-your-model#sync-api-endpoints) endpoint.
</Tip>

**Mapping Rules:**

| Baseten Endpoint                             | Maps To                       | Description                            |
| -------------------------------------------- | ----------------------------- | -------------------------------------- |
| `environments/{production}/predict`          | `predict_endpoint` route      | Default endpoint for model predictions |
| `environments/{production}/sync/{any/route}` | `/{any/route}` in your server | Access any route in your server        |

**Example:** If you set `predict_endpoint: /my/custom/route`:

| Baseten Endpoint                                 | Maps To            |
| ------------------------------------------------ | ------------------ |
| `environments/{production}/predict`              | `/my/custom/route` |
| `environments/{production}/sync/my/custom/route` | `/my/custom/route` |
| `environments/{production}/sync/my/other/route`  | `/my/other/route`  |

## 2. Example: Running a vLLM Server

This example deploys **Meta-Llama-3.1-8B-Instruct** using **vLLM** on an **L4 GPU**, with `/health` as the readiness and liveness probe.

```yaml config.yaml theme={"system"}
base_image:
  image: vllm/vllm-openai:latest
docker_server:
  start_command: sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct --port 8000 --max-model-len 1024"
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /v1/chat/completions
  server_port: 8000
resources:
  accelerator: L4
model_name: vllm-model-server
secrets:
  hf_access_token: null
runtime:
  predict_concurrency: 128
```

<Tip>
  vLLM's /health endpoint is used to determine when the server is ready or needs
  restarting.
</Tip>

<Info>More examples available in Truss examples repo.</Info>

## 3. Installing custom Python packages

To install additional Python dependencies, add a `requirements.txt` file to your Truss.

#### Example: Infinity embedding model server

```yaml config.yaml theme={"system"}
base_image:
  image: python:3.11-slim
docker_server:
  start_command: sh -c "infinity_emb v2 --model-id BAAI/bge-small-en-v1.5"
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /embeddings
  server_port: 7997
resources:
  accelerator: L4
  use_gpu: true
model_name: infinity-embedding-server
requirements:
  - infinity-emb[all]
environment_variables:
  hf_access_token: null
```

## 4. Accessing secrets in custom servers

To use **API keys or other secrets**, first store them in Baseten. Baseten can then inject secrets into your container. They will be available at `/secrets/{secret_name}`.

#### Example: Accessing a Hugging Face token

Add secrets with placeholder values in `config.yaml`:

```yaml config.yaml theme={"system"}
secrets:
  hf_access_token: null
```

<Warning>Never store actual secret values in `config.yaml`. Store secrets in the [workspace settings](https://app.baseten.co/settings/secrets).</Warning>

Then, inside your server's `start_command` or application code, read secrets from the `/secrets` directory:

```sh  theme={"system"}
HF_TOKEN=$(cat /secrets/hf_access_token)
```

Or in your application code:

```python  theme={"system"}
# Python example
with open('/secrets/hf_access_token', 'r') as f:
    hf_token = f.read().strip()
```

<Info>More on secrets management [here](/development/model/secrets).</Info>
