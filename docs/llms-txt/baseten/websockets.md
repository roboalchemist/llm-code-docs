# Source: https://docs.baseten.co/development/model/websockets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# WebSockets 🆕

> Enable real-time, streaming, bidirectional communication using WebSockets for Truss models and Chainlets.

## Overview

WebSockets provide a persistent, full-duplex communication channel between clients and server-side models or chains. Full duplex means that chunks of data can be sent client→server and server→client simultaneously and repeatedly.

This guide covers how to implement WebSocket-based interactions for Truss models and Chains/Chainlets.

Unlike traditional request-response models, WebSockets allow continuous data exchange without reopening connections. This is useful for real-time applications, streaming responses, and maintaining lightweight interactions. Example applications could be real-time audio transcription, AI phone calls or agents with turn-based interactions. WebSockets are also useful for situations where you want to manage some state on the server-side, and you want requests that are part of the same "session" to always be routed to the replica that maintains that state.

## WebSocket Usage in Truss Models

In Truss models, WebSockets replace the conventional request/response flow: a single `websocket` method handles all processing and input/output communication goes through the WebSocket object (not arguments and return values). There are no separate `preprocess`, `predict`, and `postprocess` methods anymore, but you can still implement `load`.

1. **Initialize your Truss**:

```bash  theme={"system"}
truss init websocket-model
```

For more detailed information about this command, refer to the [truss init documentation](reference/cli/truss/init).

2. Replace the `predict` method with a `websocket` method to your Truss in `model/model.py`. For example:

```python  theme={"system"}
import fastapi

class Model:
    async def websocket(self, websocket: fastapi.WebSocket):
        try:
            while True:
                message = await websocket.receive_text()
                await websocket.send_text(f"WS obtained: {message}")
        except fastapi.WebSocketDisconnect:
            pass
```

3. Set `runtime.transport.kind=websocket` in `config.yaml`:

```yaml  theme={"system"}
...
runtime:
  transport:
    kind: websocket
```

### Key Points

* Continuous message exchange occurs in a loop until client disconnection. You can also decide to close the connection server-side if a certain condition is reached
  * This is done by calling `websocket.close()`
* WebSockets enable bidirectional streaming, avoiding the need for multiple HTTP requests (or return values).
* You must not implement any of the traditional methods `predict`, `preprocess`, or `postprocess`.
* The WebSocket object passed to the `websocket` method has already accepted the connection, so you must not call `websocket.accept()` on it. You may close the connection though at the end of your processing. If you don’t close it explicitly, it will be closed after exiting your `websocket` method.

### Invocation

Using `websocat` ([get it](https://github.com/vi/websocat)), you can call the model like this:

```bash  theme={"system"}
websocat -H="Authorization: Api-Key $BASETEN_API_KEY" \
   wss://model-{MODEL_ID}.api.baseten.co/environments/production/websocket
Hello # Your input.
WS obtained: Hello # Echoed from model.
# ctrl+c to close connection.
```

<Note>
  The path you use depends on which environment or deployment of the model you'd like to call.

  * Environment: `wss://model-{MODEL_ID}.api.baseten.co/environments/{ENVIRONMENT_NAME}/websocket`.
  * Deployment: `wss://model-{MODEL_ID}.api.baseten.co/deployment/{DEPLOYMENT_NAME}/websocket`.

  See [Reference](reference/inference-api/predict-endpoints/environments-websocket) for the full details.
</Note>

## WebSocket Usage in Chains/Chainlets

For Chains, WebSockets are wrapped in a reduced API object `WebSocketProtocol`. All processing happens in the `run_remote` method as usual. But inputs as well as outputs (or “return values”) are sent through the WebSocket object using async `send_{X}` and `receive_{X}` methods (there are variants for `text`, `bytes` and `json)`. As a convenience, there's also a `receive` method that can passthrough both `str` and `bytes` types.

### Implementation Example

```python  theme={"system"}
import fastapi
import truss_chains as chains

class Dependency(chains.ChainletBase):
    async def run_remote(self, name: str) -> str:
        return f"Hello from dependency, {name}."

@chains.mark_entrypoint
class WSEntrypoint(chains.ChainletBase):
    def __init__(self, dependency=chains.depends(Dependency)):
        self._dependency = dependency

    async def run_remote(self, websocket: chains.WebSocketProtocol) -> None:
        try:
            while True:
                message = await websocket.receive_text()
                if message == "dep":
                    response = await self._dependency.run_remote("WSEntrypoint")
                else:
                    response = f"You said: {message}"
                await websocket.send_text(response)
        except fastapi.WebSocketDisconnect:
            print("Disconnected.")
```

### Key Points

* WebSocket interactions in Chains must follow `WebSocketProtocol` (it is essentially the same as `fastapi.Websocket`, but you cannot accept the connection, because inside the Chainlet, the connection will be already accepted).
* No other arguments are allowed in `run_remote()` when using WebSockets.
* The return type must be `None` (if you return data to the client, send it through the WebSocket itself).
* WebSockets can only be used only in the *entrypoint*, not in dependencies.
* Unlike for truss models it is not needed to explicitly set `runtime.transport.kind` .

### Invocation

Using `websocat` ([get it](https://github.com/vi/websocat)), you can call the chain like this:

```bash  theme={"system"}
websocat -H="Authorization: Api-Key $BASETEN_API_KEY" \
   wss://chain-{CHAIN_ID}.api.baseten.co/environments/production/websocket
```

<Note>
  Similarly to models, WebSocket chains can also be invoked either via deployment or environment.

  See [Reference](/reference/inference-api/predict-endpoints/environments-websocket) for the full details.
</Note>

## WebSocket Usage with Custom Servers

You can deploy WebSocket servers using **custom Docker images** with the `docker_server` configuration. This approach is useful when you have an existing WebSocket server packaged in a Docker container or need specific runtime environments.

### Configuration

To deploy a WebSocket server using a custom Docker image, configure your `config.yaml` as follows:

```yaml config.yaml theme={"system"}
base_image:
  image: bryanzhang2/custom_ws:v0.0.4
docker_server:
  start_command: /app/server
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /v1/websocket
  server_port: 8081
model_name: custom_ws
runtime:
  transport:
    kind: "websocket"
```

### Key Configurations for WebSocket Custom Servers

* `predict_endpoint` (**required**) – The WebSocket endpoint path (e.g., `/v1/websocket`, `/ws`)
* `runtime.transport.kind` (**required**) – Must be set to `"websocket"`
* `start_command` (**required**) – Command to start your WebSocket server
* `readiness_endpoint` (**required**) – Health check endpoint for Kubernetes readiness probes
* `liveness_endpoint` (**required**) – Health check endpoint for Kubernetes liveness probes

### Invocation

Using `websocat`, you can connect to your custom WebSocket server:

```bash  theme={"system"}
websocat -H="Authorization: Api-Key $BASETEN_API_KEY" \
   wss://model-{MODEL_ID}.api.baseten.co/environments/production/websocket
```

The WebSocket connection will be routed to your custom server's `predict_endpoint` path.

<Info>
  For more details on custom server deployment, see [Custom servers documentation](/development/model/custom-server).
</Info>

# Deployment and Concurrency Considerations

### Scheduling

The WebSocket scaling algorithm will schedule new WebSocket connections to the least-utilized replica until all replicas are at `maxConcurrency - 1` concurrent WebSocket  connections, at which point the total number of replicas will be incremented, until the `maxReplica` setting is hit.

Scale-down occurs when the number of replicas is greater than `minReplica` , and there are replicas with 0 concurrent connections. At this point, we begin scaling down idle replicas one-by-one.

Some other scheduling factors to consider when using WebSockets:

* Resource utilization: Standard HTTP requests are stateless and allow Baseten to optimize replica utilization and autoscaling. With WebSockets, long-lived connections are tied to specific replicas and count against your concurrency targets—even if underutilized. It's your responsibility to manage connection efficiency.
* Stateful complexity: WebSocket handlers often assume server-side state. This adds complexity around connection lifecycle management (e.g., handling unexpected disconnects, cleanup, reconnection logic).

### Lifetime guarantees

WebSockets are guaranteed to last a minimum of *1 hour*. In reality, a single WebSocket connection should be able to continue for much longer, but this is the guarantee that we provide in order to ensure that we can make changes to our system at a reasonable rate (including restarting and moving internal services as needed).

### Concurrency changes

When scaling concurrency down, existing WebSockets will be allowed to continue until they complete, even if it means that a replica indefinitely has a greater number of ongoing connections than the max concurrency setting.

For instance, suppose:

* You have a concurrency setting of 10, and currently have 10 websocket connections active on a replica.
* Then, you change the concurrency setting to 5.

In this case, Baseten will not force any of the ongoing connections to close as a result of the concurrency change. They will be allowed to continue and close naturally (unless the 1 hour minimum has passed, and an internal restart is required).

### Promotion

Just like with HTTP, you can promote a WebSocket model or chain to an environment via the REST API or UI.

When promoting a WebSocket model or chain, new connections will be routed to the new deployment, but existing
connections will remain connected to the current deployment until a termination happens.
Depending on the length of the connection, this could result in old deployments taking longer to scale down
than for HTTP deployments.

### Maximum message size

As a hard limit, we enforce a 100MiB maximum message size for any individual message sent over a websocket. This means that both clients and models are limited to 100MiB for *each* outgoing message, though *there is no overall limit on the cumulative data that can be sent over a websocket*.

# Monitoring

Just like with HTTP deployment, with WebSockets, we offer metrics on the performance
of the deployment.

## Inference volume

Inference volume is tracked as the number of connections per minute. These
metrics are published *after* the connection is closed, so these include the
status that the connection was closed with.

See [WebsSocket connection close codes](https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent/code) for a full list.

## End-to-end connection duration

Measured at different percentiles (p50, p90, p95, p99):

End-to-end connection duration is tracked as the duration of the connection. Just
like connections/minute, this is tracked after connections are closed.

## Connection input and output size

Measured at different percentiles (p50, p90, p95, p99):

* **Connection input size:** Bytes sent by the client to the server for the duration of the connection.
* **Connection output size:** Bytes sent by the client to the server for the duration of the connection.
