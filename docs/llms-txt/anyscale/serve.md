# Source: https://docs.anyscale.com/runtime/serve.md

# Ray Serve on the Anyscale Runtime

[View Markdown](/runtime/serve.md)

# Ray Serve on the Anyscale Runtime

This page provides an overview of Ray Serve on Anyscale.

Anyscale recommends using workspaces to develop Ray Serve applications. See [Develop a Ray Serve application](/runtime/serve/develop.md).

You deploy Ray Serve applications to production using Anyscale services. See [What are Anyscale services?](/services.md).

## What is Ray Serve?[​](#what-is "Direct link to What is Ray Serve?")

Ray Serve is a scalable model serving library for building online inference applications. Ray Serve is framework agnostic, so you can use a single toolkit to serve everything from deep learning models built with frameworks like PyTorch, TensorFlow, and Keras, to Scikit-Learn models, to arbitrary Python business logic. The flexibility of Ray Serve allows you to bring model optimization such as TensorRT, vLLM, and DeepSpeed. Ray Serve ensures effortless scaling across heterogeneous machines and provides flexible scheduling support to maximize hardware utilization.

Ray Serve is particularly well suited for model composition and many model serving, enabling you to build a complex inference service consisting of multiple ML models and business logic all in Python code. Some of the most valuable features Ray Serve has to offer include:

| Feature                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Model composition](https://docs.ray.io/en/latest/serve/model_composition.html)                     | Compose many individual models and business logic that are often required for building AI applications. You can scale each of these components independently.                                                                                                                                                                                                           |
| [Model multiplexing](https://docs.ray.io/en/latest/serve/model-multiplexing.html)                   | Enable efficient utilization of cloud resources by multiplexing models inside a pool of deployment replicas. This feature is useful in cases where you have many models with similar shape, but different weights, that you invoke sparsely.                                                                                                                            |
| [Multiple applications](https://docs.ray.io/en/latest/serve/multi-app.html)                         | Configure separate applications with their own deployment replicas that you can deploy or upgrade separately. Multi-app support is particularly powerful for use cases with many independent models deployed within one cluster to maximize hardware utilization. You can easily add, delete, or update models in one application without affecting other applications. |
| [Autoscaling](https://docs.ray.io/en/latest/serve/autoscaling-guide.html)                           | Ray Serve supports dynamically scaling the resources for a model up and down by adjusting the number of replicas.                                                                                                                                                                                                                                                       |
| [Resource allocation](https://docs.ray.io/en/latest/serve/resource-allocation.html)                 | Ray Serve supports a flexible resource allocation model, including fractional GPUs, that enables you to serve models on limited hardware resources.                                                                                                                                                                                                                     |
| [Dynamic request batching](https://docs.ray.io/en/latest/serve/tutorials/batch.html)                | Improve throughput without sacrificing latency goals.                                                                                                                                                                                                                                                                                                                   |
| [Ray Serve LLMs](https://docs.ray.io/en/latest/serve/llm/serving-llms.html)                         | Accommodating the needs of more complex AI models, Ray Serve has features like [streaming responses](https://docs.ray.io/en/latest/serve/http-guide.html#streaming-responses), making it the best way to deploy generative AI and LLM applications.                                                                                                                     |
| [FastAPI integration](https://docs.ray.io/en/latest/serve/http-guide.html#fastapi-http-deployments) | You can optionally use FastAPI to control HTTP handling logic. When you build your application with FastAPI, the Anyscale console includes a link to FastAPI documentation that lets you run sample queries against your defined routes.                                                                                                                                |

Find more information in the [Ray Serve documentation](https://docs.ray.io/en/latest/serve/index.html).

## Anyscale Runtime optimizations for Ray Serve[​](#anyscale-runtime-optimizations-for-ray-serve "Direct link to Anyscale Runtime optimizations for Ray Serve")

The following table provides an overview of Ray Serve features in the Anyscale Runtime:

| Feature                            | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Fast autoscaling and model loading | [Fast model loading](/services/fast-loading.md) combined with startup time optimizations improve auto-scaling and cluster startup capabilities. In certain [experiments](https://www.anyscale.com/blog/autoscale-large-ai-models-faster), the end-to-end scaling time for Llama-3-70B is 5.1x faster on Anyscale compared to open-source Ray.                                        |
| High-throughput serving            | Anyscale provides additional optimizations to achieve up to 54% higher queries-per-second and up to 3x streaming tokens per second for high traffic serving use cases. See [High-throughput serving](#high-throughput).                                                                                                                                                              |
| Observability                      | Anyscale provides custom metric dashboards, [log search](/monitoring/accessing-logs.md), [tracing](/monitoring/tracing.md), and [alerting](/monitoring/custom-dashboards-and-alerting.md), for comprehensive observability into your production services. You can [export](/monitoring/exporting-logs.md) logs, metrics, and traces to your observability tooling like Datadog, etc. |
| Multi availability zone services   | Anyscale enables availability-zone aware scheduling of Ray Serve replicas to provide higher redundancy to availability zone failures.                                                                                                                                                                                                                                                |
| Containerized runtime environments | You can configure [different container images](/services/multi-app.md#multi-container-apps) for different Ray Serve deployments allowing you to manage dependencies per model.                                                                                                                                                                                                       |

Anyscale services add additional optimizations such as zero-downtime incremental rollouts and support for serving multiple versions of a service. See [What are Anyscale services?](/services.md).

## High-throughput serving[​](#high-throughput "Direct link to High-throughput serving")

Anyscale recommends enabling high-throughput serving for all supported Ray Serve applications. See [Unsupported patterns](#unsupported).

note

This feature is available on Ray 2.51.0 or later as a beta release for Anyscale clouds on AWS virtual machines. Contact [Anyscale support](mailto:support@anyscale.com) with questions or feedback, or to request enablement for cloud resources backed by Google Cloud or Kubernetes.

Enabling high-throughput serving provides up to 54% higher queries-per-second and up to 3x streaming tokens per second compared to standard Ray Serve configurations.

### Enable high-throughput serving[​](#enable "Direct link to Enable high-throughput serving")

To enable high-throughput serving, add the following environment variable to the containerfile used to build the container image for your Anyscale service:

```
ENV RAY_SERVE_THROUGHPUT_OPTIMIZED=1
```

See [Custom images on Anyscale](/container-image/custom-image.md) for information about building custom container images.

Anyscale recommends testing services with this optimization enabled in workspaces before deploying to production. See [Workspaces](/platform/workspaces.md).

### Unsupported patterns[​](#unsupported "Direct link to Unsupported patterns")

Don't enable high-throughput serving if your Ray Serve application uses any of the following patterns.

#### Blocking operations in request path[​](#blocking-ops "Direct link to Blocking operations in request path")

High-throughput serving runs your request handling code and Ray Serve's internal code on the same event loop for better performance. This requires that all code in your request path uses `async` operations to avoid blocking the event loop.

Use `async def` for all deployment methods and `await` for I/O operations:

```
from ray import serve
import aiohttp

@serve.deployment
class MyAPI:
    async def __call__(self, request):
        # Non-blocking async operation
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.example.com/data") as resp:
                data = await resp.json()
        return {"result": data}
```

Don't use blocking operations such as synchronous file I/O, blocking database calls, or synchronous HTTP requests. Using `async` operations ensures that a single request doesn't block other requests. See [Design considerations](/runtime/serve/develop.md#design-considerations) for more patterns on structuring Ray Serve applications.

#### Model multiplexing on ingress deployments[​](#multiplexing "Direct link to Model multiplexing on ingress deployments")

High-throughput serving doesn't support model multiplexing on ingress deployments. You can still use model multiplexing on downstream deployments.

See [Pattern: Model multiplexing with high-throughput serving](/runtime/serve/develop.md#multiplexing-pattern) for the recommended pattern for structuring applications that use model multiplexing with high-throughput serving.

#### Passing large objects between deployments[​](#object-refs "Direct link to Passing large objects between deployments")

By default, high-throughput serving serializes objects passed between deployments using gRPC. For applications that pass large objects such as tensors or datasets between deployments, you must explicitly enable pass-by-reference for each deployment handle call:

```
from ray import serve
from ray.serve.handle import DeploymentHandle

@serve.deployment
class Pipeline:
    def __init__(self, preprocessor: DeploymentHandle):
        self.preprocessor = preprocessor.options(
            _by_reference=True
        )
    
    async def __call__(self, data):
        # Enable pass-by-reference for large objects.
        processed = await self.preprocessor.process.remote(data)
        return processed
```

Without `_by_reference=True`, Ray Serve serializes large objects, which can cause performance degradation or out-of-memory errors.

#### Other unsupported patterns[​](#other-unsupported "Direct link to Other unsupported patterns")

The following patterns aren't supported with high-throughput serving:

* **gRPC services**: Services using `grpc_options` in the service config. See [Use gRPC with Anyscale services](/services/grpc.md).
* **Scale-to-zero on ingress**: The ingress deployment must have `min_replicas` greater than 1. See [Best practices for replica configuration](/services/scale.md#best-practices).
* **WebSocket connections**: Real-time bidirectional communication isn't supported.

### How it works[​](#how-it-works "Direct link to How it works")

High-throughput serving enables multiple optimizations including the following:

* gRPC for inter-deployment communication.
* Shared event loop for user code and Ray Serve framework code.
* Log buffering to reduce I/O overhead.

note

Log buffering batches logs during normal operations to increase throughput. Error-level logs are still written immediately, so observability for error conditions isn't affected.

For technical details, see the [Ray Serve performance documentation](https://docs.ray.io/en/latest/serve/advanced-guides/performance.html#enable-throughput-optimized-serving).
