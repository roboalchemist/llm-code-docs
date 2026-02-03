# Source: https://docs.baseten.co/development/model/custom-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy custom Docker images

> Deploy custom Docker images to run inference servers like vLLM, SGLang, Triton, or any containerized application.

When you write a `Model` class, Truss uses the
[Truss server base image](https://hub.docker.com/r/baseten/truss-server-base/tags)
by default. However, you can deploy pre-built containers.

In this guide, you will learn how to set the your configuration file to run a
custom Docker image and deploy it to Baseten using Truss.

## Configuration

To deploy a custom Docker image, set
[`base_image`](/reference/truss-configuration#base-image-image) to your image
and use the `docker_server` argument to specify how to run it.

```yaml config.yaml theme={"system"}
base_image:
  image: your-registry/your-image:latest
docker_server:
  start_command: your-server-start-command
  server_port: 8000
  predict_endpoint: /predict
  readiness_endpoint: /health
  liveness_endpoint: /health
```

* `image`: The Docker image to use.
* `start_command`: The command to start the server.
* `server_port`: The port to listen on.
* `predict_endpoint`: The endpoint to forward requests to.
* `readiness_endpoint`: The endpoint to check if the server is ready.
* `liveness_endpoint`: The endpoint to check if the server is alive.

<Warning>
  Port 8080 is reserved by Baseten's internal reverse proxy. If your server binds to port 8080, the deployment fails with `[Errno 98] address already in use`.
</Warning>

For the full list of fields, see the
[configuration reference](/reference/truss-configuration#docker_server).

<Accordion title="Endpoint mapping">
  While `predict_endpoint` maps your server's inference route to Baseten's
  `/predict` endpoint, you can access any route in your server using the
  [sync endpoint](/inference/calling-your-model#sync-api-endpoints).

  | Baseten endpoint                            | Maps to                       |
  | ------------------------------------------- | ----------------------------- |
  | `/environments/production/predict`          | Your `predict_endpoint` route |
  | `/environments/production/sync/{any/route}` | `/{any/route}` in your server |

  **Example:** If you set `predict_endpoint: /v1/chat/completions`:

  | Baseten endpoint                          | Maps to                |
  | ----------------------------------------- | ---------------------- |
  | `/environments/production/predict`        | `/v1/chat/completions` |
  | `/environments/production/sync/v1/models` | `/v1/models`           |
</Accordion>

## Deploy Ollama

This example deploys [Ollama](https://ollama.com/) with the TinyLlama model
using a custom Docker image. Ollama is a popular lightweight LLM inference
server, similar to vLLM or SGLang. TinyLlama is small enough to run on a CPU.

### 1. Create the config

Create a `config.yaml` file with the following configuration:

```yaml config.yaml theme={"system"}
model_name: ollama-tinyllama
base_image:
  image: python:3.11-slim
build_commands:
  - curl -fsSL https://ollama.com/install.sh | sh
docker_server:
  start_command: sh -c "ollama serve & sleep 5 && ollama pull tinyllama && wait"
  readiness_endpoint: /api/tags
  liveness_endpoint: /api/tags
  predict_endpoint: /api/generate
  server_port: 11434
resources:
  cpu: "4"
  memory: 8Gi
```

The `base_image` field specifies the Docker image to use as your starting
point, in this case a lightweight Python image. The `build_commands` section
installs Ollama into the container at build time. You can also use this to
install model weights or other dependencies.

The `start_command` launches the Ollama server, waits for it to initialize, and
then pulls the TinyLlama model.

The `readiness_endpoint` and `liveness_endpoint`
both point to `/api/tags`, which returns successfully when Ollama is running.
The `predict_endpoint` maps Baseten's `/predict` route to Ollama's
`/api/generate` endpoint.

Finally, declare your resource requirements. This example only needs 4 CPUs and
8GB of memory. For a complete list of resource options, see the
[Resources](/deployment/resources) page.

### 2. Deploy

To deploy the model, use the following:

```sh  theme={"system"}
truss push --publish
```

This will build the Docker image and deploy it to Baseten.
Once the `readiness_endpoint` and `liveness_endpoint` are successful, the model will be ready to use.

### 3. Run inference

Ollama uses OpenAI API compatible endpoints to run inference and calls
`/api/generate` to generate text. Since you mapped the `/predict` route to
Ollama's `/api/generate` endpoint, you can run inference by calling the
`/predict` endpoint.

<Tabs>
  <Tab title="Truss CLI">
    To run inference with Truss, use the `predict` command:

    ```sh  theme={"system"}
    truss predict -d '{"model": "tinyllama", "prompt": "Write a short story about a robot dreaming", "options": {"num_predict": 50}}'
    ```
  </Tab>

  <Tab title="cURL">
    To run inference with cURL, use the following command:

    ```sh  theme={"system"}
    curl -s -X POST "https://model-MODEL_ID.api.baseten.co/development/predict" \
      -H "Authorization: Api-Key $BASETEN_API_KEY" \
      -d '{"model": "tinyllama", "prompt": "Write a short story about a robot dreaming", "options": {"num_predict": 50}}' \
      | jq -j '.response'
    ```
  </Tab>

  <Tab title="Python">
    To run inference with Python, use the following:

    ```python  theme={"system"}
    import os
    import requests

    model_id = "MODEL_ID"
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    response = requests.post(
        f"https://model-{model_id}.api.baseten.co/development/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "model": "tinyllama",
            "prompt": "Write a short story about a robot dreaming",
            "options": {"num_predict": 50},
        },
    )
    print(response.json()["response"])
    ```
  </Tab>
</Tabs>

The following is an example of its response:

```output  theme={"system"}
It was a dreary, grey day when the robots started to dream. 
They had been programmed to think like humans, but it wasn't until they began to dream that they realized just how far apart they actually were.
```

Congratulations! You have successfully deployed and ran inference on a custom Docker image.

## Next steps

* [Private registries](/development/model/private-registries) — Pull images from AWS ECR, Google Artifact Registry, or Docker Hub
* [Secrets](/development/model/secrets#custom-docker-images) — Access API keys and tokens in your container
* [WebSockets](/development/model/websockets#websocket-usage-with-custom-servers) — Enable WebSocket connections
* [vLLM](/examples/vllm), [SGLang](/examples/sglang), [TensorRT-LLM](/examples/tensorrt-llm) — Deploy LLMs with popular inference servers
