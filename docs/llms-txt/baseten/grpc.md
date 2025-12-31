# Source: https://docs.baseten.co/development/model/grpc.md

# gRPC 🆕

> Invoke your model over gRPC.

## Overview

gRPC is a high-performance, open-source remote procedure call (RPC) framework that uses HTTP/2 for transport and Protocol Buffers for serialization. Unlike traditional HTTP APIs, gRPC provides strong type safety, high performance, and built-in support for streaming and bidirectional communication.

**Why use gRPC with Baseten?**

* **Type safety**: Protocol Buffers ensure strong typing and contract validation between client and server
* **Ecosystem integration**: Easily integrate Baseten with existing gRPC-based services
* **Streaming support**: Built-in support for server streaming, client streaming, and bidirectional streaming
* **Language interoperability**: Generate client libraries for multiple programming languages from a single `.proto` file

## gRPC on Baseten

gRPC support in Baseten is implemented using [Custom Servers](/development/model/custom-server). Unlike standard Truss models that use the `load()`, and `predict()` methods, gRPC models run their own server process that handles gRPC requests directly.

This approach gives developers full control over the gRPC server implementation.

For this to work, you must first package your gRPC server code into a Docker image.
Once that is done, you can set up your Truss `config.yaml` to configure your deployment
and push the server to Baseten.

## Setup

### Installation

1. **Install Truss:**
   ```bash  theme={"system"}
   pip install --upgrade truss
   ```

2. **Install Protocol Buffer compiler:**
   ```bash  theme={"system"}
   # On macOS
   brew install protobuf

   # On Ubuntu/Debian
   sudo apt-get install protobuf-compiler

   # On other systems, see: https://protobuf.dev/getting-started/
   ```

3. **Install gRPC tools:**
   ```bash  theme={"system"}
   pip install grpcio-tools
   ```

### Protocol Buffer Definition

Your gRPC service starts with a `.proto` file that defines the service interface and message types. Create an `example.proto` file in your project root:

```protobuf example.proto theme={"system"}
syntax = "proto3";

package example;

// The greeting service definition
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name
message HelloRequest {
  string name = 1;
}

// The response message containing the greeting
message HelloReply {
  string message = 1;
}
```

#### Generate Protocol Buffer Code

Generate the Python code from your `.proto` file:

```bash  theme={"system"}
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --proto_path . example.proto
```

This generates the necessary Python files (`example_pb2.py` and `example_pb2_grpc.py`) for your gRPC service. For more information about Protocol Buffers, see the [official documentation](https://protobuf.dev/).

### Model Implementation

Create your gRPC server implementation in a file called `model.py`. Here's a basic example:

```python model.py theme={"system"}
import grpc
from concurrent import futures
import time
import example_pb2
import example_pb2_grpc

from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_health.v1.health import HealthServicer


class GreeterServicer(example_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        response = example_pb2.HelloReply()
        response.message = f"Hello, {request.name}!"
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    example_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    # The gRPC health check service must be used in order for Baseten
    # to consider the gRPC server healthy.
    health_servicer = HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    health_servicer.set(
        "example.GreeterService", health_pb2.HealthCheckResponse.SERVING
    )

    # Ensure the server runs on port 50051
    server.add_insecure_port("[::]:50051")

    server.start()
    print("gRPC server started on port 50051")

    # Keep the server running
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop(0)


if __name__ == "__main__":
    serve()
```

## Deployment

### Step 1: Create a Dockerfile

Since gRPC on Baseten requires a custom server setup, you'll need to create a `Dockerfile` that bundles your gRPC server code and dependencies. Here's a basic skeleton:

```dockerfile Dockerfile theme={"system"}
FROM debian:latest

RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python3 -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model.py ./model.py
COPY example_pb2.py example_pb2_grpc.py ./

EXPOSE 8080

CMD ["python", "model.py"]

```

Create a `requirements.txt` file with your gRPC dependencies:

```txt requirements.txt theme={"system"}
grpcio
grpcio-health-checking
grpcio-tools
protobuf
```

### Step 2: Build and Push Docker Image

Build and push your Docker image to a container registry:

```bash  theme={"system"}
docker build -t your-registry/truss-grpc-demo:latest . --platform linux/amd64
docker push your-registry/truss-grpc-demo:latest
```

<Tip>
  Replace `your-registry` with your actual container registry (e.g., Docker Hub, Google Container Registry, AWS ECR). You can create a Docker Hub container registry by [following their documentation](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-registry/#try-it-out).
</Tip>

### Step 3: Configure Your Truss

Update your `config.yaml` to use the custom Docker image and configure the gRPC server:

```yaml config.yaml theme={"system"}
model_name: "gRPC Model Example"
base_image:
  image: your-registry/truss-grpc-demo:latest
docker_server:
  start_command: python model.py
  # 50051 is the only supported server port.
  server_port: 50051
  # Note that the _endpoint fields are ignored for gRPC models.
  predict_endpoint: /
  readiness_endpoint: /
  liveness_endpoint: /
resources:
  accelerator: L4  # or your preferred GPU
  use_gpu: true
runtime:
  transport:
    kind: "grpc"
```

### Step 4: Deploy with Truss

Deploy your model using the Truss CLI. You need to use the `--promote` or `--publish` flags, since gRPC models aren't supported in the development environment.

```bash  theme={"system"}
truss push --promote
```

For more detailed information about Truss deployment, see the [truss push documentation](/reference/cli/truss/push).

## Calling Your Model

### Using a gRPC Client

Once deployed, you can call your model using any gRPC client. Here's an example Python client:

```python client.py theme={"system"}
import grpc
import example_pb2
import example_pb2_grpc


def run():
    channel = grpc.secure_channel(
        "model-{MODEL_ID}.grpc.api.baseten.co:443",
        grpc.ssl_channel_credentials(),
    )

    stub = example_pb2_grpc.GreeterStub(channel)

    request = example_pb2.HelloRequest(name="World")

    metadata = [
        ("baseten-authorization", "Api-Key {API_KEY}"),
        ("baseten-model-id", "model-{MODEL_ID}"),
    ]

    response = stub.SayHello(request, metadata=metadata)
    print(response.message)


if __name__ == "__main__":
    run()


```

### Inference for specific environments and deployments

If you want to perform inference against a specific environment or deployment,
you can do so by adding headers to your gRPC calls:

**Target a specific environment:**

```python  theme={"system"}
metadata = [
    ('authorization', 'Api-Key YOUR_API_KEY'),
    ('baseten-model-id', 'model-{YOUR_MODEL_ID}'),
    ('x-baseten-environment', 'staging'),
]
```

**Target a specific deployment ID:**

```python  theme={"system"}
metadata = [
    ('authorization', 'Api-Key YOUR_API_KEY'),
    ('baseten-model-id', 'model-{YOUR_MODEL_ID}'),
    ('x-baseten-deployment', 'your-deployment-id'),
]
```

### Testing Your Deployment

Run your client to test the deployed model:

```bash  theme={"system"}
python client.py
```

# Full Example

See this [Github repository](https://github.com/basetenlabs/truss-examples/tree/main/grpc) for a full example.

# Scaling and  Monitoring

## Scaling

While many gRPC requests follow the traditional request-response pattern, gRPC also supports
bidirectional streaming and long-lived connections. The implication of this is that
a single long-lived connection, even if no data is being sent, will count
against the concurrency target for the deployment.

## Promotion

Just like with HTTP, you can promote a gRPC deployment to an environment via the REST API or UI.

When promoting a gRPC deployment, new connections will be routed to the new deployment, but existing
connections will remain connected to the current deployment until a termination happens.
Depending on the length of the connection, this could result in old deployments taking longer to scale down
than for HTTP deployments.

# Monitoring

Just like with HTTP deployment, with gRPC, we offer metrics on the performance
of the deployment.

## Inference volume

Inference volume is tracked as the number of RPCs per minute. These
metrics are published *after* the request is complete.

See [gRPC status codes](https://grpc.io/docs/guides/status-codes/) for a full list
of codes.

## End-to-end response time

Measured at different percentiles (p50, p90, p95, p99):

End-to-end response time includes cold starts, queuing, and inference (excludes client-side latency). Reflects real-world performance.
