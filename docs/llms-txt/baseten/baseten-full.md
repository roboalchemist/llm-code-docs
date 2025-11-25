# Baseten Documentation

Source: https://docs.baseten.co/llms-full.txt

---

# How Baseten works
Source: https://docs.baseten.co/concepts/howbasetenworks

Baseten is a platform for building, serving, and scaling AI models in production.

It supports multiple entry points depending on your workflow—whether you're deploying a dedicated model, calling an open-source LLM via our Model API, or training from scratch.

**At the core is the Baseten Inference Stack:** performant model runtimes on top of Inference optimized infrastructure. Instead of managing infrastructure, scaling policies, and performance optimization, you can focus on building and iterating on your AI-powered applications.

***

## Dedicated deployments

This is the primary workflow for teams deploying custom, open-source, or fine-tuned models with full control.

Baseten’s deployment stack is structured around four key pillars:

### Development

Package any model using Truss, our open-source framework for defining dependencies, hardware, and custom logic—no Docker required. For more advanced use cases, build compound inference systems using Chains, orchestrating multiple models, APIs, and processing steps.

<CardGroup cols={2}>
  <Card title="Developing a model" href="/development/model" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c320f770ea283b7d13e89533d202016d" data-og-width="956" width="956" data-og-height="458" height="458" data-path="images/how-baseten-works-truss.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=23b6782ea9c86030a14db14c36075704 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3d04a8c7770d8f8d9f2d52f9063d01e2 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=d33af8a0f99292fad4285ff2e5483d65 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b411bb63f8f7fe75b87238373cb57a36 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=ead28695833c12dc1d5bf1a69416215c 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e8e8158fb146440aa46530fb4d88d539 2500w">
    Package and deploy any AI/ML model as an API with Truss or a Custom Server.
  </Card>

  <Card title="Developing a Chain" href="/development/chain" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=672e515bad1fd2888cc65381c5a5010c" data-og-width="956" width="956" data-og-height="458" height="458" data-path="images/how-baseten-works-chains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8f1be4c10da7f8ca84c726152936cd75 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=70a1a3e26bb1429518857a1195eced27 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b1e97197db352d3b68b0c02f5c61ae27 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=454929ec2319e4f64eaded013e5d58a0 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=7a720c4d02fc41515678a7dfd189bc55 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=4455e2b78247363a9ca0564a628a1aee 2500w">
    Build multi-model workflows by chaining models, pre/post-processing, and
    business logic.
  </Card>
</CardGroup>

### Deployment

Deploy models to dedicated, autoscaling infrastructure. Use Environments for controlled versioning, rollouts, and promotion between staging and production. Support includes scale-to-zero, canary deploys, and structured model management.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=833c7f33c3a39b50502326b9cec14090" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=85501a364b60a6f564dfbdfb79af9038 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=bc9e92a71bc5bc07b8a712e8583f00b8 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=687778fd0bf01755091841abba9f2c16 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=12ca03f794ef57bb9b92d87ece692527 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=cea81f5e83fad83853169baae69d24b7 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=17a1fbe9a5dd58f733b350400a9acfe7 2500w" />

### Inference

Serve synchronous, asynchronous, and streaming predictions with configurable execution controls. Optimize for latency, throughput, or cost depending on your application’s needs.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=eac4b2c5cb0945c753d3a1353da65bed" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/inference.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=d999899a70e25aaa499b50585acd5d0a 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=61e98026b32c791687eb620f9f12d736 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=31e8c1b82ed6c1735b9a15ac5f3c0d66 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8f7fce9302b66c76e132fd4420118524 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c76330ea0c581db8514aa776ed5cb529 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=cf13be55ca64546fabf0e55cf3ad6255 2500w" />

### Observability

Monitor model health and performance with real-time metrics, logs, and detailed request traces. Export data to observability tools like Datadog or Prometheus. Debug behavior with full visibility into inputs, outputs, and errors.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=a81bbd59a02719c6814e62fdbfa89ec3" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/observability.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=15a3fb2106b5f51cd50b261131541f01 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1aa2af207e9f007781838fbd8ca63f50 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=90b0499c358c033b78985f2e08386e2e 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e6dfb73381b1ac4f70a7299f473c2fe7 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=537db025cbccafe7f54dbe0d99c736fe 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=daf4644abc87786401d3959d0f05d7d7 2500w" />

This full-stack infrastructure, from packaging to observability, is powered by the **Baseten Inference Stack**: performant model runtimes, cross-cloud availability, and seamless developer workflows.

***

## Model APIs

[Model APIs](/development/model-apis/overview) offer a fast, reliable path to production for LLM-powered features. Use OpenAI-compatible endpoints to call performant open-source models like Llama 4, DeepSeek, and Qwen, with support for structured outputs and tool calling.

If your code already works with OpenAI’s SDKs, it’ll work with Baseten—no wrappers or rewrites required.

***

## Training

[Baseten Training](/training/overview) provides scalable infrastructure for running containerized training jobs. Define your code, environment, and compute resources; manage checkpoints and logs; and transition seamlessly from training to deployment.

Organize work with TrainingProjects and track reproducible runs via TrainingJobs. Baseten supports any framework, from PyTorch to custom setups, with centralized artifact and job management.

***

## Summary

* Use [Dedicated Deployments](/development/concepts) to run and scale production-grade models with full control.
* Use [Model APIs](/development/model-apis/overview) to quickly build LLM-powered features without managing infrastructure.
* Use [Training](/training/overview) to run reproducible training jobs and productionize your own models.

Each product is built on the same core: reliable infrastructure, strong developer ergonomics, and a focus on operational excellence.


# Why Baseten
Source: https://docs.baseten.co/concepts/whybaseten

Baseten delivers fast, scalable AI/ML inference with enterprise-grade security and reliability—whether in our cloud or yours.

<img noZoom src="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/why-baseten.png?fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=c40bb99430c86f6b6da6d32767c9b86e" data-og-width="1446" width="1446" data-og-height="828" height="828" data-path="images/why-baseten.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/why-baseten.png?w=280&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=20238e37ad89da2c6063745b437f05b7 280w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/why-baseten.png?w=560&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=bfcd9dd6b0fb7fe547bfb060876ec87c 560w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/why-baseten.png?w=840&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=d8e8116ce0b3e9c2978d8e14285fdc26 840w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/why-baseten.png?w=1100&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=d7f3ac8ec4ea64b861ff665734246100 1100w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/why-baseten.png?w=1650&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=849a009a35bba9b5a7e1d323395d1c30 1650w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/why-baseten.png?w=2500&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=ed84669856c850977b20e85ac41c30f9 2500w" />

## Mission-critical inference

Built for high-performance workloads, our platform optimizes inference performance across modalities, from state-of-the-art transcription to blazing-fast LLMs.
Built-in autoscaling, model performance optimizations, and deep observability tools ensure efficiency without complexity.
Trusted by top ML teams serving their products to millions of users, Baseten accelerates time to market for AI-driven products by building on four key pillars of inference: performance, infrastructure, tooling, and expertise.

#### Model performance

Baseten’s model performance engineers apply the latest research and custom engine optimizations in production, so you get low latency and high throughput out of the box.
Production-grade support for critical features, like speculative decoding and LoRA swapping, is baked into our platform.

#### Cloud-native infrastructure

[Deploy](/deployment/concepts) and [scale models](/deployment/autoscaling) across clusters, regions, and clouds with five nines reliability.
We built all the orchestration and optimized the network routing to ensure global scalability without the operational complexity.

#### Model management tooling

Love your development ecosystem, with deep [observability](/observability/metrics) and easy-to-use tools for deploying, managing, and iterating on models in production.
Quickly serve open-source and custom models, ultra-low-latency compound AI systems, and custom Docker servers in our cloud or yours.

#### Forward deployed engineering

Baseten’s expert engineers work as an extension of your team, customizing deployments for your target performance, quality, and cost-efficiency metrics.
Get hands-on support with deep inference-specific expertise and 24/7 on-call availability.

#### Model training and finetuning, all in one platform

Baseten Training provides a fast, scalable, and flexible platform for training and finetuning models. Deploy checkpoints immediately with the click of a button
to run end to end evals and seemlessly launch to prod.


# Autoscaling
Source: https://docs.baseten.co/deployment/autoscaling

Autoscaling dynamically adjusts the number of active replicas to **handle variable traffic** while minimizing idle compute costs.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f867eb7ccef178bae2fd11117365bebb" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-autoscaling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b88950b4dd0eb765a37d74991ce29062 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f0b5d2412ebf1a9117c165f9b5711f18 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5eb7a1b115bd723b732d5889382742df 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=74fb3e685e86eddade1e04ef92b9e424 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b9c25eb323072c47121cde1c20c12a44 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=61671a961d7da633fb3a95ab4becd92c 2500w" />

## Configuring autoscaling

Autoscaling settings are **per deployment** and are inherited when promoting a model to production unless overridden.

Configure autoscaling through:

* **UI** → Manage settings in your Baseten workspace.
* **API** → Use the **[autoscaling API](/reference/management-api/deployments/autoscaling)**.

### Replica Scaling

Each deployment scales within a configured range of replicas:

* **Minimum replicas** → The lowest number of active replicas.
  * Default: `0` (scale to zero).
  * Maximum value: Cannot exceed the **maximum replica count**.
* **Maximum replicas** → The upper limit of active replicas.
  * Default: `1`.
  * Max: `10` by default (contact support to increase).

When first deployed, the model starts with `1` replica (or the **minimum count**, if higher). As traffic increases, additional replicas **scale up** until the **maximum count** is reached. When traffic decreases, replicas **scale down** to match demand.

***

## Autoscaler settings

The **autoscaler logic** is controlled by three key parameters:

* **Autoscaling window** → Time window for traffic analysis before scaling up/down. Default: 60 seconds.
* **Scale down delay** → Time before an unused replica is removed. Default: 900 seconds (15 minutes).
* **Concurrency target** → Number of requests a replica should handle before scaling. Default: 1 request.
* **Target Utilization Percentage** → Target percentage of filled concurrency slots. Default: 70%.

A **short autoscaling window** with a **longer scale-down delay** is recommended for **fast upscaling** while maintaining capacity during temporary dips.

The **target utilization percentage** determines the amount of headroom available. A higher number means less headroom and more
usage on each replica, where a lower number means more headroom and buffer for traffic spikes.

***

## Autoscaling behavior

### Scaling Up

When the **average requests per active replica** exceed the **concurrency target** within the **autoscaling window**, more replicas are created until:

* The **concurrency target is met**, or
* The **maximum replica count** is reached.

Note here that the amount of headroom is determined by the **target utilization percentage**. For example, with a concurrency target of 10 requests and a
target utilization percentage of 70%, scaling will begin when the average requests per active replica exceeds 7.

### Scaling Down

When traffic drops below the **concurrency target**, excess replicas are flagged for removal. The **scale-down delay** ensures that replicas are not removed prematurely:

* If traffic **spikes again before the delay ends**, replicas remain active.
* If the **minimum replica count** is reached, no further scaling down occurs.

***

## Scale to zero

If you're just testing your model or anticipate light and inconsistent traffic, scale to zero can save you substantial amounts of money.

Scale to zero means that when a deployed model is not receiving traffic, it scales down to zero replicas. When the model is called, Baseten spins up a new instance to serve model requests.

To turn on scale to zero, just set a deployment's minimum replica count to zero. Scale to zero is enabled by default in the standard autoscaling config.

<Note>
  Models that have not received any traffic for more than **two weeks** will be
  automatically deactivated. These models will need to be activated manually
  before they can serve requests again. For **production deployments this threshold
  is two months**.
</Note>

***

## Cold starts

A **cold start** is the time required to **initialize a new replica** when scaling up. Cold starts impact:

* **Scaled-to-zero deployments** → The first request must wait for a new replica to start.
* **Scaling events** → When traffic spikes and a deployment requires more replicas.

### Cold Start Optimizations

**Network accelerator**

Baseten speeds up model loading from **Hugging Face, CloudFront, S3, and OpenAI** using parallelized **byte-range downloads**, reducing cold start delays.

**Cold start pods**

Baseten pre-warms specialized **cold start pods** to accelerate loading times. These pods appear in logs as `[Coldboost]`.

```md Example coldboost log line theme={"system"}
Oct 09 9:20:25pm [Coldboost] Completed model.load() execution in 12650 ms
```

**Model Image streaming and optimization**

To further reduce initialization latency, Baseten uses **image streaming** to optimize container startup.

1. **Initial non-optimized image:**
   When a model is first deployed, a standard image is built without optimization. During this stage, the runtime monitors which parts of the image are accessed during startup and inference.

2. **Call graph–based optimization:**
   Baseten analyzes the model’s call graph to identify which layers, weights, and binaries are actually needed during initialization. This information drives creation of an **optimized image**.

3. **Prefetch and lazy fetch:**
   The optimized image is split into two content groups:
   * **Prefetched content:** Frequently accessed layers and dependencies are loaded eagerly at container start.
   * **Lazy-fetched content:** Less critical data is fetched on demand, reducing initial I/O overhead.

4. **Streaming-enabled image pull:**
   Images optimized through this process are streamed into the node filesystem during startup, allowing the model to begin loading before the entire image is downloaded.
   Pulling an optimized image appears in logs as:

   ```md Example streaming image pull log line theme={"system"}
   Successfully pulled streaming-enabled image in 15.851s. Image size: 32 GB.
   ```

***

## Autoscaling for development deployments

Development deployments have **fixed autoscaling constraints** to optimize for **live reload workflows**:

* **Min replicas:** `0`
* **Max replicas:** `1`
* **Autoscaling window:** `60 seconds`
* **Scale down delay:** `900 seconds (15 min)`
* **Concurrency target:** `1 request`

To enable full autoscaling, **promote the deployment and environment** like production.


# Concepts
Source: https://docs.baseten.co/deployment/concepts



Baseten provides a flexible and scalable infrastructure for deploying and managing machine learning models. This page introduces key concepts - [deployments](/deployment/deployments), [environments](/deployment/environments) , [resources](/deployment/resources) , and [autoscaling](/deployment/autoscaling) — that shape how models are served, tested, and optimized for performance and cost efficiency.

## Deployments

[Deployments](/deployment/deployments) define how models are served, scaled, and updated. They optimize resource use with autoscaling, scaling to zero, and controlled traffic shifts while ensuring minimal downtime. Deployments can be deactivated to pause resource usage or deleted permanently when no longer needed.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=833c7f33c3a39b50502326b9cec14090" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=85501a364b60a6f564dfbdfb79af9038 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=bc9e92a71bc5bc07b8a712e8583f00b8 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=687778fd0bf01755091841abba9f2c16 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=12ca03f794ef57bb9b92d87ece692527 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=cea81f5e83fad83853169baae69d24b7 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployments.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=17a1fbe9a5dd58f733b350400a9acfe7 2500w" />

## Environments

[Environments](/deployment/environments) group deployments, providing stable endpoints and autoscaling to manage model release cycles. They enable structured testing, controlled rollouts, and seamless transitions between staging and production. Each environment maintains its own settings and metrics, ensuring reliable and scalable deployments.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e922f3e12c24577d6594ca58f80431ee" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-environments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=210053dfe7b0d3398f261f1105ac6bf9 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3a7e2675275ae1f78ac5fe83330e926c 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=874b4335f21d8939c58dcd2c2b978c8c 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=09f864b743a3921b713612d54ed9708b 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=a6397fff11d9c0edfd8103f44b8b501e 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=23a5dd05c6ee1ab42cecb3698098cbb3 2500w" />

## Resources

[Resources](/deployment/resources) define the hardware allocated to a model server, balancing performance and cost. Choosing the right instance type ensures efficient inference without unnecessary overhead. Resources can be set before deployment in Truss or adjusted later in the model dashboard to match workload demands.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=028f7b8a7c5e1d92f0b55f2eec8aad11" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-resources.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5bc11192879c6aa199388df6c531a5a0 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=acbafbbe854fa0701fc63f47ab84a8f0 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5d677c56115318ebfb994e554a1f657c 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b1fd3e5c69b2b965884044cb6975d2c6 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5ed48475146334e0a2fc56f11511d599 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c8045c2ee7a60d89a940119536d71005 2500w" />

## Autoscaling

[Autoscaling](/deployment/autoscaling) dynamically adjusts model resources to handle traffic fluctuations efficiently while minimizing costs. Deployments scale between a defined range of replicas based on demand, with settings for concurrency, scaling speed, and scale-to-zero for low-traffic models. Optimizations like network acceleration and cold start pods ensure fast response times even when scaling up from zero.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f867eb7ccef178bae2fd11117365bebb" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-autoscaling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b88950b4dd0eb765a37d74991ce29062 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f0b5d2412ebf1a9117c165f9b5711f18 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5eb7a1b115bd723b732d5889382742df 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=74fb3e685e86eddade1e04ef92b9e424 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b9c25eb323072c47121cde1c20c12a44 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-autoscaling.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=61671a961d7da633fb3a95ab4becd92c 2500w" />


# Deployments
Source: https://docs.baseten.co/deployment/deployments

Deploy, manage, and scale machine learning models with Baseten

A **deployment** in Baseten is a **containerized instance of a model** that serves inference requests via an API endpoint. Deployments exist independently but can be **promoted to an environment** for structured access and scaling.

Every deployment is **automatically wrapped in a REST API**. Once deployed, models can be queried with a simple HTTP request:

```python  theme={"system"}
import requests

resp = requests.post(
    "https://model-{modelID}.api.baseten.co/deployment/[{deploymentID}]/predict",
    headers={"Authorization": "Api-Key YOUR_API_KEY"},
    json={'text': 'Hello my name is {MASK}'},
)

print(resp.json())
```

[Learn more about running inference on your deployment](/inference/calling-your-model)

***

# Development deployment

A **development deployment** is a mutable instance designed for rapid iteration. It is always in the **development state** and cannot be renamed or detached from it.

Key characteristics:

* **Live reload** enables direct updates without redeployment.
* **Single replica, scales to zero** when idle to conserve compute resources.
* **No autoscaling or zero-downtime updates.**
* **Can be promoted** to create a persistent deployment.

Once promoted, the development deployment transitions to a **deployment** and can optionally be promoted to an environment.

***

# Environments & Promotion

Environments provide **logical isolation** for managing deployments but are **not required** for a deployment to function. A deployment can be executed independently or promoted to an environment for controlled traffic allocation and scaling.

* The **production environment** exists by default.
* **Custom environments** (e.g., staging) can be created for specific workflows.
* **Promoting a deployment does not modify its behavior**, only its routing and lifecycle management.

## Canary deployments

Canary deployments support **incremental traffic shifting** to a new deployment, mitigating risk during rollouts.

* Traffic is routed in **10 evenly distributed stages** over a configurable time window.
* Traffic only begins to shift once the new deployment reaches the min replica count of the current production model.
* Autoscaling dynamically adjusts to real-time demand.
* Canary rollouts can be enabled or canceled via the UI or [REST API](/reference/management-api/environments/update-an-environments-settings).

***

# Managing Deployments

## Naming deployments

By default, deployments of a model are named `deployment-1`, `deployment-2`, and so forth sequentially. You can instead give deployments custom names via two methods:

1. While creating the deployment, using a [command line argument in truss push](/reference/sdk/truss#deploying-a-model).
2. After creating the deployment, in the model management page within your Baseten dashboard.

Renaming deployments is purely aesthetic and does not affect model management API paths, which work via model and deployment IDs.

## Deactivating a deployment

A deployment can be deactivated to suspend inference execution while preserving configuration.

* **Remains visible in the dashboard.**
* **Consumes no compute resources** but can be reactivated anytime.
* **API requests return a 404 error while deactivated.**

For demand-driven deployments, consider [autoscaling with scale to zero](/reference/management-api/deployments/autoscaling/updates-a-deployments-autoscaling-settings).

## Deleting deployments

Deployments can be **permanently deleted**, but production deployments must be replaced before deletion.

* **Deleted deployments are purged from the dashboard** but retained in usage logs.
* **All associated compute resources are released.**
* **API requests return a 404 error post-deletion.**

<Warning>
  Deletion is irreversible — use deactivation if retention is required.
</Warning>


# Environments
Source: https://docs.baseten.co/deployment/environments

Manage your model’s release cycles with environments.

Environments provide structured management for deployments, ensuring controlled rollouts, stable endpoints, and autoscaling. They help teams stage, test, and release models without affecting production traffic.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e922f3e12c24577d6594ca58f80431ee" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-environments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=210053dfe7b0d3398f261f1105ac6bf9 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3a7e2675275ae1f78ac5fe83330e926c 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=874b4335f21d8939c58dcd2c2b978c8c 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=09f864b743a3921b713612d54ed9708b 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=a6397fff11d9c0edfd8103f44b8b501e 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-environments.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=23a5dd05c6ee1ab42cecb3698098cbb3 2500w" />

Deployments can be promoted to an environment (e.g., "staging") to validate outputs before moving to production, allowing for safer model iteration and evaluation.

***

## Using Environments to manage deployments

Environments support **structured validation** before promoting a deployment, including:

* **Automated tests & evaluations**
* **Manual testing in pre-production**
* **Gradual traffic shifts with canary deployments**
* **Shadow serving for real-world analysis**

Promoting a deployment ensures it inherits **environment-specific scaling and monitoring settings**, such as:

* **Dedicated API endpoint** → [Predict API Reference](/reference/inference-api/overview#predict-endpoints)
* **Autoscaling controls** → Scale behavior is managed per environment.
* **Traffic ramp-up** → Enable [canary rollouts](/deployment/deployments#canary-deployments).
* **Monitoring & Metrics** → [Export environment metrics](/observability/export-metrics/overview).

A **production environment** operates like any other environment but has restrictions:

* **It cannot be deleted** unless the entire model is removed.
* **You cannot create additional environments named "production."**

***

## Creating custom environments

In addition to the standard **production** environment, you can create as many custom environments as needed. There are two ways to create a custom environment:

1. In the model management page on the Baseten dashboard.
2. Via the [create environment endpoint](/reference/management-api/environments/create-an-environment) in the model management API.

***

## Promoting deployments to environments

When a deployment is promoted, Baseten follows a **three-step process**:

1. A **new deployment** is created with a unique deployment ID.
2. The deployment **initializes resources** and becomes active.
3. The new deployment **replaces the existing deployment** in that environment.

* If there was **no previous deployment, default autoscaling settings** are applied.
* If a **previous deployment existed**, the new one **inherits autoscaling settings**, and the old deployment is **demoted and scales to zero**.

### Promoting a Published Deployment

If a **published deployment** (not a development deployment) is promoted:

* Its **autoscaling settings are updated** to match the environment.
* If **inactive**, it must be **activated** before promotion.

Previous deployments are **demoted but remain in the system**, retaining their **deployment ID and scaling behavior**.

***

## Deploying directly to an environment

You can **skip development stage** and deploy directly to an environment by specifying `--environment` in `truss push`:

```sh  theme={"system"}
cd my_model/
truss push --environment {environment_name}
```

<Note>Only one active promotion per environment is allowed at a time.</Note>

***

## Accessing environments in your code

The **environment name** is available in `model.py` via the `environment` keyword argument:

```python  theme={"system"}
def __init__(self, **kwargs):
    self._environment = kwargs["environment"]
```

To ensure the **environment variable remains updated**, enable\*\* "Re-deploy when promoting" \*\*in the UI or via the [REST API](/reference/management-api/environments/update-an-environments-settings). This guarantees the environment is fully initialized after a promotion.

***

## Deleting environments

Environments can be deleted, **except for production**. To remove a **production deployment**, first **promote another deployment to production** or delete the entire model.

* **Deleted environments are removed from the overview** but remain in billing history.
* **They do not consume resources** after deletion.
* **API requests to a deleted environment return a 404 error.**

<Warning>Deletion is permanent - consider deactivation instead.</Warning>


# Resources
Source: https://docs.baseten.co/deployment/resources

Manage and configure model resources

Every AI/ML model on Baseten runs on an **instance**, a dedicated set of hardware allocated to the model server. Selecting the right instance type ensures **optimal performance** while controlling **compute costs**.

* **Insufficient resources** → Slow inference or failures.
* **Excess resources** → Higher costs without added benefit.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=028f7b8a7c5e1d92f0b55f2eec8aad11" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/deployment-resources.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5bc11192879c6aa199388df6c531a5a0 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=acbafbbe854fa0701fc63f47ab84a8f0 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5d677c56115318ebfb994e554a1f657c 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b1fd3e5c69b2b965884044cb6975d2c6 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5ed48475146334e0a2fc56f11511d599 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/deployment-resources.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c8045c2ee7a60d89a940119536d71005 2500w" />

## Instance type resource components

* **Instance** → The allocated hardware for inference.
* **vCPU** → Virtual CPU cores for general computing.
* **RAM** → Memory available to the CPU.
* **GPU** → Specialized hardware for accelerated ML workloads.
* **VRAM** → Dedicated GPU memory for model execution.

***

# Configuring model resources

Resources can be defined **before deployment** in Truss or **adjusted later** via the Baseten UI.

### Defining resources in Truss

Define resource requirements in `config.yaml` before running `truss push`. Any changes after deployment will not impact previous deployments. Running `truss push` again will create a new deployment using the resources specified in the `config.yaml`.

<Info>
  The only exception is the **development** deployment. It will be redeployed with the new specified resources.
</Info>

**Example (Stable Diffusion XL):**

```yaml config.yaml theme={"system"}
resources:
  accelerator: L4
  cpu: "4"
  memory: 16Gi
  use_gpu: true
```

Baseten provisions the **smallest instance that meets the specified constraints**:

* \*\*cpu: "3" or "4" → \*\*Maps to a 4-core instance.
* \*\*cpu: "5" to "8" → \*\*Maps to an 8-core instance.

<Info>
  `Gi` in `resources.memory` refers to **Gibibytes**, which are slightly larger
  than **Gigabytes**.
</Info>

### Updating resources in the Baseten UI

Once deployed, resource configurations can only be updated **through the Baseten UI**. Changing the instance type will deploy a new copy of the deployment using the new specified instance type.

<Info>
  Like when running `truss push`, the **development** deployment will be redeployed with the new specified instance type.
</Info>

For a list of available instance types, see the [instance type reference](/deployment/resources#instance-type-reference).

***

# Instance Type Reference

Specs and benchmarks for every Baseten instance type.

Choosing the right instance for model inference means balancing performance and cost. This page lists all available instance types on Baseten to help you deploy and serve models effectively.

## CPU-only Instances

Cost-effective options for lighter workloads. No GPU.

* **Starts at**: \$0.00058/min
* **Best for**: Transformers pipelines, small QA models, text embeddings

| Instance | \$/min    | vCPU | RAM    |
| -------- | --------- | ---- | ------ |
| 1×2      | \$0.00058 | 1    | 2 GiB  |
| 1×4      | \$0.00086 | 1    | 4 GiB  |
| 2×8      | \$0.00173 | 2    | 8 GiB  |
| 4×16     | \$0.00346 | 4    | 16 GiB |
| 8×32     | \$0.00691 | 8    | 32 GiB |
| 16×64    | \$0.01382 | 16   | 64 GiB |

**Example workloads:**

* `1x2`: Text classification (e.g., Truss quickstart)
* `4x16`: LayoutLM Document QA
* `4x16+`: Sentence Transformers embeddings on larger corpora

## GPU Instances

Accelerated inference for LLMs, diffusion models, and Whisper.

| Instance       | \$/min    | vCPU | RAM      | GPU                    | VRAM    |
| -------------- | --------- | ---- | -------- | ---------------------- | ------- |
| T4x4x16        | \$0.01052 | 4    | 16 GiB   | NVIDIA T4              | 16 GiB  |
| T4x8x32        | \$0.01504 | 8    | 32 GiB   | NVIDIA T4              | 16 GiB  |
| T4x16x64       | \$0.02408 | 16   | 64 GiB   | NVIDIA T4              | 16 GiB  |
| L4x4x16        | \$0.01414 | 4    | 16 GiB   | NVIDIA L4              | 24 GiB  |
| L4:2x4x16      | \$0.04002 | 24   | 96 GiB   | 2 NVIDIA L4s           | 48 GiB  |
| L4:4x48x192    | \$0.08003 | 48   | 192 GiB  | 4 NVIDIA L4s           | 96 GiB  |
| A10Gx4x16      | \$0.02012 | 4    | 16 GiB   | NVIDIA A10G            | 24 GiB  |
| A10Gx8x32      | \$0.02424 | 8    | 32 GiB   | NVIDIA A10G            | 24 GiB  |
| A10Gx16x64     | \$0.03248 | 16   | 64 GiB   | NVIDIA A10G            | 24 GiB  |
| A10G:2x24x96   | \$0.05672 | 24   | 96 GiB   | 2 NVIDIA A10Gs         | 48 GiB  |
| A10G:4x48x192  | \$0.11344 | 48   | 192 GiB  | 4 NVIDIA A10Gs         | 96 GiB  |
| A10G:8x192x768 | \$0.32576 | 192  | 768 GiB  | 8 NVIDIA A10Gs         | 188 GiB |
| V100x8x61      | \$0.06120 | 16   | 61 GiB   | NVIDIA V100            | 16 GiB  |
| A100x12x144    | \$0.10240 | 12   | 144 GiB  | 1 NVIDIA A100          | 80 GiB  |
| A100:2x24x288  | \$0.20480 | 24   | 288 GiB  | 2 NVIDIA A100s         | 160 GiB |
| A100:3x36x432  | \$0.30720 | 36   | 432 GiB  | 3 NVIDIA A100s         | 240 GiB |
| A100:4x48x576  | \$0.40960 | 48   | 576 GiB  | 4 NVIDIA A100s         | 320 GiB |
| A100:5x60x720  | \$0.51200 | 60   | 720 GiB  | 5 NVIDIA A100s         | 400 GiB |
| A100:6x72x864  | \$0.61440 | 72   | 864 GiB  | 6 NVIDIA A100s         | 480 GiB |
| A100:7x84x1008 | \$0.71680 | 84   | 1008 GiB | 7 NVIDIA A100s         | 560 GiB |
| A100:8x96x1152 | \$0.81920 | 96   | 1152 GiB | 8 NVIDIA A100s         | 640 GiB |
| H100           | \$0.10833 | -    | -        | 1 NVIDIA H100          | 80 GiB  |
| H100:2         | \$0.21667 | -    | -        | 2 NVIDIA H100s         | 160 GiB |
| H100:4         | \$0.43333 | -    | -        | 4 NVIDIA H100s         | 320 GiB |
| H100:8         | \$0.86667 | -    | -        | 8 NVIDIA H100s         | 640 GiB |
| H100MIG        | \$0.06250 | -    | -        | Fractional NVIDIA H100 | 40 GiB  |

## GPU Details & Workloads

### T4

Turing-series GPU

* 2,560 CUDA / 320 Tensor cores
* 16 GiB VRAM
* **Best for:** Whisper, small LLMs like StableLM 3B

### L4

Ada Lovelace-series GPU

* 7,680 CUDA / 240 Tensor cores
* 24 GiB VRAM, 300 GiB/s
* 24 GiB VRAM, 300 GiB/s
* 121 TFLOPS (fp16)
* **Best for**: Stable Diffusion XL
* **Limit**: Not suitable for LLMs due to bandwidth

### A10G

Ampere-series GPU

* 9,216 CUDA / 288 Tensor cores
* 24 GiB VRAM, 600 GiB/s
* 70 TFLOPS (fp16)
* **Best for**: Mistral 7B, Whisper, Stable Diffusion/SDXL

### V100

Volta-series GPU

* 16 GiB VRAM
* **Best for**: Legacy workloads needing V100-specific support

### A100

Ampere-series GPU

* 6,912 CUDA / 432 Tensor cores
* 80 GiB VRAM, 1.94 TB/s
* 312 TFLOPS (fp16)
* **Best for**: Mixtral, Llama 2 70B (2 A100s), Falcon 180B (5 A100s), SDXL

### H100

Hopper-series GPU

* 16,896 CUDA / 640 Tensor cores
* 80 GiB VRAM, 3.35 TB/s
* 990 TFLOPS (fp16)
* **Best for**: Mixtral 8x7B, Llama 2 70B (2×H100), SDXL

### H100MIG

Fractional H100 (3/7 compute, ½ memory)

* 7,242 CUDA cores, 40 GiB VRAM
* 1.675 TB/s bandwidth
* **Best for**: Efficient LLM inference at lower cost than A100


# Binary IO
Source: https://docs.baseten.co/development/chain/binaryio

Performant serialization of numeric data

Numeric data or audio/video are most efficiently transmitted as bytes.

Other representations such as JSON or base64 encoding lose precision, add
significant parsing overhead and increase message sizes (e.g. \~33% increase
for base64 encoding).

Chains extends the JSON-centred pydantic ecosystem with two ways how you can
include binary data: numpy array support and raw bytes.

## Numpy `ndarray` support

<Tip>
  Once you have your data represented as a numpy array, you can easily (and
  often without copying) convert it to `torch`, `tensorflow` or other common
  numeric library's objects.
</Tip>

To include numpy arrays in a pydantic model, chains has a special field type
implementation `NumpyArrayField`. For example:

```python  theme={"system"}
import numpy as np
import pydantic

from truss_chains import pydantic_numpy


class DataModel(pydantic.BaseModel):
    some_numbers: pydantic_numpy.NumpyArrayField
    other_field: str
    ...


numbers = np.random.random((3, 2))
data = DataModel(some_numbers=numbers, other_field="Example")
print(data)
# some_numbers=NumpyArrayField(shape=(3, 2), dtype=float64, data=[
#   [0.39595027 0.23837526]
#   [0.56714894 0.61244946]
#   [0.45821942 0.42464844]])
# other_field='Example'
```

`NumpyArrayField` is a wrapper around the actual numpy array. Inside your
python code, you can work with its `array` attribute:

```python  theme={"system"}
data.some_numbers.array += 10
# some_numbers=NumpyArrayField(shape=(3, 2), dtype=float64, data=[
#   [10.39595027 10.23837526]
#   [10.56714894 10.61244946]
#   [10.45821942 10.42464844]])
# other_field='Example'
```

The interesting part is, how it serializes when making communicating between
Chainlets or with a client.
It can work in two modes: JSON and binary.

### Binary

As a JSON alternative that supports byte data, Chains uses `msgpack` (with
`msgpack_numpy`) to serialize the dict representation.

For Chainlet-Chainlet RPCs this is done automatically for you by enabling binary
mode of the dependency Chainlets, see
[all options](/reference/sdk/chains#truss-chains-depends):

```python  theme={"system"}
import truss_chains as chains


class Worker(chains.ChainletBase):
    async def run_remote(self, data: DataModel) -> DataModel:
        data.some_numbers.array += 10
        return data


class Consumer(chains.ChainletBase):

    def __init__(self, worker=chains.depends(Worker, use_binary=True)):
        self._worker = worker

    async def run_remote(self):
        numbers = np.random.random((3, 2))
        data = DataModel(some_numbers=numbers, other_field="Example")
        result = await self._worker.run_remote(data)
```

Now the data is transmitted in a fast and compact way between Chainlets
which often gives performance increases.

### Binary client

If you want to send such data as input to a chain or parse binary output
from a chain, you have to add the `msgpack` serialization client-side:

```python  theme={"system"}
import requests
import msgpack
import msgpack_numpy

msgpack_numpy.patch()  # Register hook for numpy.

# Dump to "python" dict and then to binary.
data_dict = data.model_dump(mode="python")
data_bytes = msgpack.dumps(data_dict)

# Set binary content type in request header.
headers = {
    "Content-Type": "application/octet-stream", "Authorization": ...
}

response = requests.post(url, data=data_bytes, headers=headers)
response_dict = msgpack.loads(response.content)
response_model = ResponseModel.model_validate(response_dict)
```

The steps of dumping from a pydantic model and validating the response dict
into a pydantic model can be skipped, if you prefer working with raw dicts
on the client.

<Tip>
  The implementation of `NumpyArrayField` only needs `pydantic`, no other Chains
  dependencies. So you can take that implementation code in isolation and
  integrate it in your client code.
</Tip>

<Warning>
  Some version combinations of `msgpack` and `msgpack_numpy` give errors, we
  know that `msgpack = ">=1.0.2"` and `msgpack-numpy = ">=0.4.8"` work.
</Warning>

### JSON

The JSON-schema to represent the array is a dict of `shape (tuple[int]), 
dtype (str), data_b64 (str)`. E.g.

```python  theme={"system"}
print(data.model_dump_json())
'{"some_numbers":{"shape":[3,2],"dtype":"float64", "data_b64":"30d4/rnKJEAsvm...'
```

The base64 data corresponds to `np.ndarray.tobytes()`.

To get back to the array from the JSON string, use the model's
`model_validate_json` method.

As discussed in the beginning, this schema is not performant for numeric data
and only offered as a compatibility layer (JSON does not allow bytes) -
generally prefer the binary format.

# Simple `bytes` fields

It is possible to add a `bytes` field to a pydantic model used in a chain,
or as a plain argument to `run_remote`. This can be useful to include
non-numpy data formats such as images or audio/video snippets.

In this case, the "normal" JSON representation does not work and all
involved requests or Chainlet-Chainlet-invocations must use binary mode.

The same steps as for arrays [above](#binary-client) apply: construct dicts
with `bytes` values and keys corresponding to the `run_remote` argument
names or the field names in the pydantic model. Then use `msgpack` to
serialize and deserialize those dicts.

Don't forget to add `Content-type` headers and that `response.json()` will
not work.


# Concepts
Source: https://docs.baseten.co/development/chain/concepts

Glossary of Chains concepts and terminology

## Chainlet

A Chainlet is the basic building block of Chains. A Chainlet is a Python class
that specifies:

* A set of compute resources.
* A Python environment with software dependencies.
* A typed interface [
  `run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets)
  for other Chainlets to call.

This is the simplest possible Chainlet — only the
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets) method is
required — and we can layer in other concepts to create a more capable Chainlet.

```python  theme={"system"}
import truss_chains as chains


class SayHello(chains.ChainletBase):

    async def run_remote(self, name: str) -> str:
        return f"Hello, {name}"
```

You can modularize your code by creating your own chainlet sub-classes,
refer to our [subclassing guide](/development/chain/subclassing).

### Remote configuration

Chainlets are meant for deployment as remote services. Each Chainlet specifies
its own requirements for compute hardware (CPU count, GPU type and count, etc)
and software dependencies (Python libraries or system packages). This
configuration is built into a Docker image automatically as part of the
deployment process.

When no configuration is provided, the Chainlet will be deployed on a basic
instance with one vCPU, 2GB of RAM, no GPU, and a standard set of Python and
system packages.

Configuration is set using the
[`remote_config`](/reference/sdk/chains#remote-configuration) class variable
within the Chainlet:

```python  theme={"system"}
import truss_chains as chains


class MyChainlet(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            pip_requirements=["torch==2.3.0", ...]
        ),
        compute=chains.Compute(gpu="H100", ...),
        assets=chains.Assets(secret_keys=["hf_access_token"], ...),
    )
```

See the
[remote configuration reference](/reference/sdk/chains#remote-configuration)
for a complete list of options.

### Initialization

Chainlets are implemented as classes because we often want to set up expensive
static resources once at startup and then re-use it with each invocation of the
Chainlet. For example, we only want to initialize an AI model and download its
weights once then re-use it every time we run inference.

We do this setup in `__init__()`, which is run exactly once when the Chainlet is
deployed or scaled up.

```python  theme={"system"}
import truss_chains as chains


class PhiLLM(chains.ChainletBase):
    def __init__(self) -> None:
        import torch
        import transformers

        self._model = transformers.AutoModelForCausalLM.from_pretrained(
            PHI_HF_MODEL,
            torch_dtype=torch.float16,
            device_map="auto",
        )

        self._tokenizer = transformers.AutoTokenizer.from_pretrained(
            PHI_HF_MODEL,
        )
```

Chainlet initialization also has two important features: context and dependency
injection of other Chainlets, explained below.

#### Context (access information)

You can add
[
`DeploymentContext`](/reference/sdk/chains#class-truss-chains-deploymentcontext)
object as an optional argument to the `__init__`-method of a Chainlet.
This allows you to use secrets within your Chainlet, such as using
a `hf_access_token` to access a gated model on Hugging Face (note that when
using secrets, they also need to be added to the `assets`).

```python  theme={"system"}
import truss_chains as chains


class MistralLLM(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        ...
    assets = chains.Assets(secret_keys=["hf_access_token"], ...),
    )

    def __init__(
        self,
        # Adding the `context` argument, allows us to access secrets
        context: chains.DeploymentContext = chains.depends_context(),
    ) -> None:
        import transformers

        # Using the secret from context to access a gated model on HF
        self._model = transformers.AutoModelForCausalLM.from_pretrained(
            "mistralai/Mistral-7B-Instruct-v0.2",
            use_auth_token=context.secrets["hf_access_token"],
        )
```

#### Depends (call other Chainlets)

The Chains framework uses the
[`chains.depends()`](/reference/sdk/chains#truss-chains-depends) function in
Chainlets' `__init__()` method to track the dependency relationship between
different Chainlets within a Chain.

This syntax, inspired by dependency injection, is used to translate local Python
function calls into calls to the remote Chainlets in production.

Once a dependency Chainlet is added with
[`chains.depends()`](/reference/sdk/chains#truss-chains-depends), its
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets) method can
call this dependency Chainlet, e.g. below `HelloAll` we can make calls to
`SayHello`:

```python  theme={"system"}
import truss_chains as chains


class HelloAll(chains.ChainletBase):

    def __init__(self, say_hello_chainlet=chains.depends(SayHello)) -> None:
        self._say_hello = say_hello_chainlet

    async def run_remote(self, names: list[str]) -> str:
        output = []
        for name in names:
            output.append(self._say_hello.run_remote(name))
        return "\n".join(output)
```

## Run remote (chaining Chainlets)

The `run_remote()` method is run each time the Chainlet is called. It is the
sole public interface for the Chainlet (though you can have as many private
helper functions as you want) and its inputs and outputs must have type
annotations.

In `run_remote()` you implement the actual work of the Chainlet, such as model
inference or data chunking:

```python  theme={"system"}
import truss_chains as chains


class PhiLLM(chains.ChainletBase):
    async def run_remote(self, messages: Messages) -> str:
        import torch

        model_inputs = await self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = await self._tokenizer(model_inputs, return_tensors="pt")
        input_ids = inputs["input_ids"].to("cuda")
        with torch.no_grad():
            outputs = await self._model.generate(
                input_ids=input_ids, **self._generate_args)
            output_text = await self._tokenizer.decode(
                outputs[0], skip_special_tokens=True)
        return output_text
```

We recommend implementing this as an `async` method and using async APIs for
doing all the work (e.g. downloads, vLLM or TRT inference).

It is possible to stream results back, see our
[streaming guide](/development/chain/streaming).

<Tip>
  If `run_remote()` makes calls to other Chainlets, e.g. invoking a dependency
  Chainlet for each element in a list, you can benefit from concurrent
  execution, by making the `run_remote()` an `async` method and starting the
  calls as concurrent tasks
  `asyncio.ensure_future(self._dep_chainlet.run_remote(...))`.
</Tip>

## Entrypoint

The entrypoint is called directly from the deployed Chain's API endpoint and
kicks off the entire chain. The entrypoint is also responsible for returning the
final result back to the client.

Using the
[`@chains.mark_entrypoint`](/reference/sdk/chains#truss-chains-mark-entrypoint)
decorator, one Chainlet within a file is set as the entrypoint to the chain.

```python  theme={"system"}
@chains.mark_entrypoint
class HelloAll(chains.ChainletBase):
```

Optionally you can also set a Chain display name (not to be confused with
Chainlet display name) with this decorator:

```python  theme={"system"}
@chains.mark_entrypoint("My Awesome Chain")
class HelloAll(chains.ChainletBase):
```

## I/O and `pydantic` data types

To make orchestrating multiple remotely deployed services possible, Chains
relies heavily on typed inputs and outputs. Values must be serialized to a safe
exchange format to be sent over the network.

The Chains framework uses the type annotations to infer how data should be
serialized and currently is restricted to types that are JSON compatible. Types
can be:

* Direct type annotations for simple types such as `int`, `float`,
  or `list[str]`.
* Pydantic models to define a schema for nested data structures or multiple
  arguments.

An example of pydantic input and output types for a Chainlet is given below:

```python  theme={"system"}
import enum
import pydantic


class Modes(enum.Enum):
    MODE_0 = "MODE_0"
    MODE_1 = "MODE_1"


class SplitTextInput(pydantic.BaseModel):
    data: str
    num_partitions: int
    mode: Modes


class SplitTextOutput(pydantic.BaseModel):
    parts: list[str]
    part_lens: list[int]
```

Refer to the [pydantic docs](https://docs.pydantic.dev/latest/) for more
details on how
to define custom pydantic data models.

Also refer to the [guide](/development/chain/binaryio) about efficient integration
of binary and numeric data.

## Chains compared to Truss

<Accordion title="Tips for Truss users" icon="lightbulb">
  Chains is an alternate SDK for packaging and deploying AI models. It carries over many features and concepts from Truss and gives you access to the benefits of Baseten (resource provisioning, autoscaling, fast cold starts, etc), but it is not a 1-1 replacement for Truss.

  Here are some key differences:

  * Rather than running `truss init` and creating a Truss in a directory, a Chain
    is a single file, giving you more flexibility for implementing multi-step
    model inference. Create an example with `truss chains init`.
  * Configuration is done inline in typed Python code rather than in a
    `config.yaml` file.
  * While Chainlets are converted to Truss models when run on Baseten,
    `Chainlet != TrussModel`.

  Chains is designed for compatibility and incremental adoption, with a stub
  function for wrapping existing deployed models.
</Accordion>


# Deploy
Source: https://docs.baseten.co/development/chain/deploy

Deploy your Chain on Baseten

Deploying a Chain is an atomic action that deploys every Chainlet
within the Chain. Each Chainlet specifies its own remote
environment — hardware resources, Python and system dependencies, autoscaling
settings.

### Development

The default behavior for pushing a chain is to create a development deployment:

```sh  theme={"system"}
truss chains push ./my_chain.py
```

Where `my_chain.py` contains the entrypoint Chainlet for your Chain.

Development deployments are intended for testing and can't scale past one
replica. Each time you make a development deployment, it overwrites the existing
development deployment.

Development deployments support rapid iteration with `watch` - see [above
guide](/development/chain/watch).

### 🆕 Environments

To deploy a Chain to an environment, run:

```sh  theme={"system"}
truss chains push ./my_chain.py --environment {env_name}
```

Environments are intended for live traffic and have access to full
autoscaling settings. Each time you deploy to an environment, a new deployment is
created. Once the new deployment is live, it replaces the previous deployment,
which is relegated to the published deployments list.
[Learn more](/deployment/environments) about environments.


# Architecture & Design
Source: https://docs.baseten.co/development/chain/design

How to structure your Chainlets

A Chain is composed of multiple connected Chainlets working together to perform
a task.

For example, the Chain in the diagram below takes a large audio file as input.
Then it splits it into smaller chunks, transcribes each chunk in parallel
(reducing the end-to-end latency), and finally aggregates and returns the
results.

<Frame>
  <img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=135870ba1fc2e86cf319815eafe14441" data-og-width="1280" width="1280" data-og-height="155" height="155" data-path="development/chain/images/audio-transcription.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=349246b63271305875316013222b8c90 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3cd50bb5fff404036b210ff33feebc53 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=839c92448e904237050e9dc56f19a1e7 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5ed90d4e49b2a27c35f35706cf53cfa7 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=35ab233489e8de235bf7cd390ba5963d 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=ed9e02564abf1e48ec71fdd4c60fd034 2500w" />
</Frame>

To build an efficient Chain, we recommend drafting your high level
structure as a flowchart or diagram. This can help you identifying
parallelizable units of work and steps that need different (model/hardware)
resources.

If one Chainlet creates many "sub-tasks" by calling other dependency
Chainlets (e.g. in a loop over partial work items),
these calls should be done as `aynscio`-tasks that run concurrently.
That way you get the most out of the parallelism that Chains offers. This
design pattern is extensively used in the
[audio transcription example](/examples/chains-audio-transcription).

<Warning>
  While using `asyncio` is essential for performance, it can also be tricky.
  Here are a few caveats to look out for:

  * Executing operations in an async function that block the event loop for
    more than a fraction of a second. This hinders the "flow" of processing
    requests concurrently and starting RPCs to other Chainlets. Ideally use
    native async APIs. Frameworks like vLLM or triton server offer such APIs,
    similarly file downloads can be made async and you might find
    [`AsyncBatcher`](https://github.com/hussein-awala/async-batcher) useful.
    If there is no async support, consider running blocking code in a
    thread/process pool (as an attribute of a Chainlet).
  * Creating async tasks (e.g. with `asyncio.ensure_future`) does not start
    the task *immediately*. In particular, when starting several tasks in a loop,
    `ensure_future` must be alternated with operations that yield to the event
    loop that, so the task can be started. If the loop is not `async for` or
    contains other `await` statements, a "dummy" await can be added, for example
    `await asyncio.sleep(0)`. This allows the tasks to be started concurrently.
</Warning>


# Engine Builder Models
Source: https://docs.baseten.co/development/chain/engine-builder-models

Engine Builder models are pre-trained models that are optimized for specific inference tasks.

Baseten's [Engine Builder](/development/model/performance/engine-builder-overview) enables the deployment of optimized model inference engines. Currently, it supports TensorRT-LLM. Truss Chains allows seamless integration of these engines into structured workflows. This guide provides a quick entry point for Chains users.

## LLama 7B Example

Use the `EngineBuilderLLMChainlet` baseclass to configure an LLM engine. The additional `engine_builder_config` field specifies model architecture, repository, and runtime parameters and more, the full options are detailed in the [Engine Builder configuration guide](/development/model/performance/engine-builder-config).

```python  theme={"system"}
import truss_chains as chains
from truss.base import trt_llm_config, truss_config

class Llama7BChainlet(chains.EngineBuilderLLMChainlet):
    remote_config = chains.RemoteConfig(
        compute=chains.Compute(gpu=truss_config.Accelerator.H100),
        assets=chains.Assets(secret_keys=["hf_access_token"]),
    )
    engine_builder_config = truss_config.TRTLLMConfiguration(
        build=trt_llm_config.TrussTRTLLMBuildConfiguration(
            base_model=trt_llm_config.TrussTRTLLMModel.LLAMA,
            checkpoint_repository=trt_llm_config.CheckpointRepository(
                source=trt_llm_config.CheckpointSource.HF,
                repo="meta-llama/Llama-3.1-8B-Instruct",
            ),
            max_batch_size=8,
            max_seq_len=4096,
            tensor_parallel_count=1,
        )
    )
```

## Differences from Standard Chainlets

* No `run_remote` implementation: Unlike regular Chainlets, `EngineBuilderLLMChainlet` does not require users to implement `run_remote()`. Instead, it automatically wires into the deployed engine’s API. All LLM Chainlets have the same function signature: `chains.EngineBuilderLLMInput` as input and a stream (`AsyncIterator`) of strings as output. Likewise `EngineBuilderLLMChainlet`s can only be used as dependencies, but not have dependencies themselves.
* No `run_local` ([guide](/development/chain/localdev)) and `watch` ([guide](/development/chain/watch)) Standard Chains support a local debugging mode and watch. However, when using `EngineBuilderLLMChainlet`, local execution is not available, and testing must be done after deployment.
  For a faster dev loop of the rest of your chain (everything except the engine builder chainlet) you can substitute those chainlets with stubs like you can do for an already deployed truss model \[[guide](/development/chain/stub)].

## Integrate the Engine Builder Chainlet

After defining an `EngineBuilderLLMInput` like `Llama7BChainlet` above, you can use it as a dependency in other conventional chainlets:

```python  theme={"system"}
from typing import AsyncIterator
import truss_chains as chains

@chains.mark_entrypoint
class TestController(chains.ChainletBase):
    """Example using the Engine Builder Chainlet in another Chainlet."""

    def __init__(self, llm=chains.depends(Llama7BChainlet)) -> None:
        self._llm = llm

    async def run_remote(self, prompt: str) -> AsyncIterator[str]:
        messages = [{"role": "user", "content": prompt}]
        llm_input = chains.EngineBuilderLLMInput(messages=messages)
        async for chunk in self._llm.run_remote(llm_input):
            yield chunk

```


# Error Handling
Source: https://docs.baseten.co/development/chain/errorhandling

Understanding and handling Chains errors

Error handling in Chains follows the principle that the root cause "bubbles
up" until the entrypoint - which returns an error response. Similarly to how
python stack traces contain all the layers from where an exception was raised
up until the main function.

Consider the case of a Chain where the entrypoint calls `run_remote` of a
Chainlet named `TextToNum` and this in turn invokes `TextReplicator`. The
respective `run_remote` methods might also use other helper functions that
appear in the call stack.

Below is an example stack trace that shows how the root cause (a
`ValueError`) is propagated up to the entrypoint's `run_remote` method (this
is what you would see as an error log):

```
Chainlet-Traceback (most recent call last):
  File "/packages/itest_chain.py", line 132, in run_remote
    value = self._accumulate_parts(text_parts.parts)
  File "/packages/itest_chain.py", line 144, in _accumulate_parts
    value += self._text_to_num.run_remote(part)
ValueError: (showing chained remote errors, root error at the bottom)
├─ Error in dependency Chainlet `TextToNum`:
│   Chainlet-Traceback (most recent call last):
│     File "/packages/itest_chain.py", line 87, in run_remote
│       generated_text = self._replicator.run_remote(data)
│   ValueError: (showing chained remote errors, root error at the bottom)
│   ├─ Error in dependency Chainlet `TextReplicator`:
│   │   Chainlet-Traceback (most recent call last):
│   │     File "/packages/itest_chain.py", line 52, in run_remote
│   │       validate_data(data)
│   │     File "/packages/itest_chain.py", line 36, in validate_data
│   │       raise ValueError(f"This input is too long: {len(data)}.")
╰   ╰   ValueError: This input is too long: 100.
```

## Exception handling and retries

Above stack trace is what you see if you don't catch the exception. It is
possible to add error handling around each remote Chainlet invocation.

Chains tries to raise the same exception class on the *caller* Chainlet as was
raised in the *dependency* Chainlet.

* Builtin exceptions (e.g. `ValueError`) always work.
* Custom or third-party exceptions (e.g. from `torch`) can be only raised
  in the caller if they are included in the dependencies of the caller as
  well. If the exception class cannot be resolved, a
  `GenericRemoteException` is raised instead.

Note that the *message* of re-raised exceptions is the concatenation
of the original message and the formatted stack trace of the dependency
Chainlet.

In some cases it might make sense to simply retry a remote invocation (e.g.
if it failed due to some transient problems like networking or any "flaky"
parts). `depends` can be configured with additional
[options](/reference/sdk/chains#truss-chains-depends) for that.

Below example shows how you can add automatic retries and error handling for
the call to `TextReplicator` in `TextToNum`:

```python  theme={"system"}
import truss_chains as chains


class TextToNum(chains.ChainletBase):

    def __init__(
        self,
        replicator: TextReplicator = chains.depends(TextReplicator, retries=3),
    ) -> None:
        self._replicator = replicator
    
    async def run_remote(self, data: ...):
        try:
            generated_text = await self._replicator.run_remote(data)
        except ValueError:
            ...  # Handle error.

```

## Stack filtering

The stack trace is intended to show the user implemented code in
`run_remote` (and user implemented helper functions). Under the
hood, the calls from one Chainlet to another go through an HTTP
connection, managed by the Chains framework. And each Chainlet itself is
run as a FastAPI server with several layers of request handling code "above".

In order to provide concise, readable stacks, all of this non-user code is
filtered out.


# Your first Chain
Source: https://docs.baseten.co/development/chain/getting-started

Build and deploy two example Chains

This quickstart guide contains instructions for creating two Chains:

1. A simple CPU-only “hello world”-Chain.
2. A Chain that implements Phi-3 Mini and uses it to write poems.

## Prerequisites

To use Chains, install a recent Truss version and ensure pydantic is v2:

```bash  theme={"system"}
pip install --upgrade truss 'pydantic>=2.0.0'
```

<Accordion title="Help for setting up a clean development environment">
  Truss requires python `>=3.8,<3.13`. To set up a fresh development environment,
  you can use the following commands, creating a environment named `chains_env`
  using `pyenv`:

  ```bash  theme={"system"}
  curl https://pyenv.run | bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  source ~/.bashrc
  pyenv install 3.11.0
  ENV_NAME="chains_env"
  pyenv virtualenv 3.11.0 $ENV_NAME
  pyenv activate $ENV_NAME
  pip install --upgrade truss 'pydantic>=2.0.0'
  ```
</Accordion>

To deploy Chains remotely, you also need a
[Baseten account](https://app.baseten.co/signup).
It is handy to export your API key to the current shell session or permanently in your `.bashrc`:

```bash ~/.bashrc theme={"system"}
export BASETEN_API_KEY="nPh8..."
```

## Example: Hello World

Chains are written in Python files. In your working directory,
create `hello_chain/hello.py`:

```sh  theme={"system"}
mkdir hello_chain
cd hello_chain
touch hello.py
```

In the file, we'll specify a basic Chain. It has two Chainlets:

* `HelloWorld`, the entrypoint, which handles the input and output.
* `RandInt`, which generates a random integer. It is used a as a dependency
  by `HelloWorld`.

Via the entrypoint, the Chain takes a maximum value and returns the string "
Hello World!" repeated a
variable number of times.

```python hello.py theme={"system"}
import random
import truss_chains as chains


class RandInt(chains.ChainletBase):
    async def run_remote(self, max_value: int) -> int:
        return random.randint(1, max_value)


@chains.mark_entrypoint
class HelloWorld(chains.ChainletBase):
    def __init__(self, rand_int=chains.depends(RandInt, retries=3)) -> None:
        self._rand_int = rand_int

    async def run_remote(self, max_value: int) -> str:
        num_repetitions = await self._rand_int.run_remote(max_value)
        return "Hello World! " * num_repetitions
```

### The Chainlet class-contract

Exactly one Chainlet must be marked as the entrypoint with
the [`@chains.mark_entrypoint`](/reference/sdk/chains#truss-chains-mark-entrypoint)
decorator. This Chainlet is responsible for
handling public-facing input and output for the whole Chain in response to an
API call.

A Chainlet class has a single public method,
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets), which is
the API
endpoint for the entrypoint Chainlet and the function that other Chainlets can
use as a dependency. The
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets)
method must be fully type-annotated
with <Tooltip tip="E.g. `int`, `str`, `list[float]`">primitive python
types</Tooltip>
or <Tooltip tip="They have builtin JSON serialization.">[pydantic models](https://docs.pydantic.dev/latest/)</Tooltip>.

Chainlets cannot be <Tooltip tip="I.e. creating instances like `chainlet = RandInt()` in arbitrary locations in your code.">naively</Tooltip> instantiated. The only correct usages are:

1. Make one Chainlet depend on another one via the
   [`chains.depends()`](/reference/sdk/chains#truss-chains-depends) directive
   as an `__init__`-argument as shown above for the `RandInt` Chainlet.
2. In the [local debugging mode](/development/chain/localdev#test-a-chain-locally).

Beyond that, you can structure your code as you like, with private methods,
imports from other files, and so forth.

<Warning>
  Keep in mind that Chainlets are intended for distributed, replicated, remote
  execution, so using global variables, global state, and certain Python
  features like importing modules dynamically at runtime should be avoided as
  they may not work as intended.
</Warning>

### Deploy your Chain to Baseten

To deploy your Chain to Baseten, run:

```bash  theme={"system"}
truss chains push hello.py
```

The deploy command results in an output like this:

```
                  ⛓️   HelloWorld - Chainlets  ⛓️
╭──────────────────────┬─────────────────────────┬─────────────╮
│ Status               │ Name                    │ Logs URL    │
├──────────────────────┼─────────────────────────┼─────────────┤
│  💚 ACTIVE           │ HelloWorld (entrypoint) │ https://... │
├──────────────────────┼─────────────────────────┼─────────────┤
│  💚 ACTIVE           │ RandInt (dep)           │ https://... │
╰──────────────────────┴─────────────────────────┴─────────────╯
Deployment succeeded.
You can run the chain with:
curl -X POST 'https://chain-.../run_remote' \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '<JSON_INPUT>'
```

Wait for the status to turn to `ACTIVE` and test invoking your Chain (replace
`$INVOCATION_URL` in below command):

```bash  theme={"system"}
curl -X POST $INVOCATION_URL \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -d '{"max_value": 10}'
# "Hello World! Hello World! Hello World! "
```

## Example: Poetry with LLMs

Our second example also has two Chainlets, but is somewhat more complex and
realistic. The Chainlets are:

* `PoemGenerator`, the entrypoint, which handles the input and output and
  orchestrates calls to the LLM.
* `PhiLLM`, which runs inference on Phi-3 Mini.

This Chain takes a list of words and returns a poem about each word, written by
Phi-3. Here's the architecture:

<Frame>
  <img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f6d5826651ed54b5464edb18e21112d4" data-og-width="971" width="971" data-og-height="118" height="118" data-path="development/chain/images/poems.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=94a069566ed45a94e144cd5b5d82289e 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=fe60b7bdd7c7b113547a915c773aad60 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1e8f723e57f205675dbfde2014e320a5 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=6cf0e32c25402c8628de88e29ff0b4f4 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=441a6836e2430a400929d66cd532f80c 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/poems.svg?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f5ef9b81e5e444b95485c61a06b5e171 2500w" />
</Frame>

We build this Chain in a new working directory (if you are still inside
`hello_chain/`, go up one level with `cd ..` first):

```sh  theme={"system"}
mkdir poetry_chain
cd poetry_chain
touch poems.py
```

<Tip>
  A similar end-to-end code example, using Mistral as an LLM, is available in
  the [examples
  repo](https://github.com/basetenlabs/model/tree/main/truss-chains/examples/mistral).
</Tip>

### Building the LLM Chainlet

The main difference between this Chain and the previous one is that we now have
an LLM that needs a GPU and more complex dependencies.

Copy the following code into `poems.py`:

```python poems.py theme={"system"}
import asyncio
from typing import List

import pydantic
import truss_chains as chains
from truss import truss_config

PHI_HF_MODEL = "microsoft/Phi-3-mini-4k-instruct"
# This configures to cache model weights from the hunggingface repo
# in the docker image that is used for deploying the Chainlet.
PHI_CACHE = truss_config.ModelRepo(
    repo_id=PHI_HF_MODEL, allow_patterns=["*.json", "*.safetensors", ".model"]
)


class Messages(pydantic.BaseModel):
    messages: List[dict[str, str]]


class PhiLLM(chains.ChainletBase):
    # `remote_config` defines the resources required for this chainlet.
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            # The phi model needs some extra python packages.
            pip_requirements=[
                "accelerate==0.30.1",
                "einops==0.8.0",
                "transformers==4.41.2",
                "torch==2.3.0",
            ]
        ),
        # The phi model needs a GPU and more CPUs.
        compute=chains.Compute(cpu_count=2, gpu="T4"),
        # Cache the model weights in the image
        assets=chains.Assets(cached=[PHI_CACHE]),
    )

    def __init__(self) -> None:
        # Note the imports of the *specific* python requirements are
        # pushed down to here. This code will only be executed on the
        # remotely deployed Chainlet, not in the local environment,
        # so we don't need to install these packages in the local
        # dev environment.
        import torch
        import transformers

        self._model = transformers.AutoModelForCausalLM.from_pretrained(
            PHI_HF_MODEL,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        self._tokenizer = transformers.AutoTokenizer.from_pretrained(
            PHI_HF_MODEL,
        )
        self._generate_args = {
            "max_new_tokens"      : 512,
            "temperature"         : 1.0,
            "top_p"               : 0.95,
            "top_k"               : 50,
            "repetition_penalty"  : 1.0,
            "no_repeat_ngram_size": 0,
            "use_cache"           : True,
            "do_sample"           : True,
            "eos_token_id"        : self._tokenizer.eos_token_id,
            "pad_token_id"        : self._tokenizer.pad_token_id,
        }

    async def run_remote(self, messages: Messages) -> str:
        import torch

        model_inputs = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._tokenizer(model_inputs, return_tensors="pt")
        input_ids = inputs["input_ids"].to("cuda")
        with torch.no_grad():
            outputs = self._model.generate(
                input_ids=input_ids, **self._generate_args)
            output_text = self._tokenizer.decode(
                outputs[0], skip_special_tokens=True)
        return output_text
```

### Building the entrypoint

Now that we have an LLM, we can use it in a poem generator Chainlet. Add the
following code to `poems.py`:

```python poems.py theme={"system"}
import asyncio


@chains.mark_entrypoint
class PoemGenerator(chains.ChainletBase):
    def __init__(self, phi_llm: PhiLLM = chains.depends(PhiLLM)) -> None:
        self._phi_llm = phi_llm

    async def run_remote(self, words: list[str]) -> list[str]:
        tasks = []
        for word in words:
            messages = Messages(
                messages=[
                    {
                        "role"   : "system",
                        "content": (
                            "You are poet who writes short, "
                            "lighthearted, amusing poetry."
                        ),
                    },
                    {"role": "user", "content": f"Write a poem about {word}"},
                ]
            )
            tasks.append(
                asyncio.ensure_future(self._phi_llm.run_remote(messages)))
            await asyncio.sleep(0)  # Yield to event loop, to allow starting tasks.

        return list(await asyncio.gather(*tasks))
```

Note that we use `asyncio.ensure_future` around each RPC to the LLM chainlet.
This makes the current python process start these remote calls concurrently,
i.e. the next call is started before the previous one has finished and we can
minimize our overall runtime. In order to await the results of all calls,
`asyncio.gather` is used which gives us back normal python objects.
If the LLM is hit with many concurrent requests, it can auto-scale up (if
autoscaling is configured). More advanced LLM models have batching capabilities,
so for those even a single instance can serve concurrent request.

### Deploy your Chain to Baseten

To deploy your Chain to Baseten, run:

```bash  theme={"system"}
truss chains push poems.py
```

Wait for the status to turn to `ACTIVE` and test invoking your Chain (replace
`$INVOCATION_URL` in below command):

```bash  theme={"system"}
curl -X POST $INVOCATION_URL \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '{"words": ["bird", "plane", "superman"]}'
#[[
#"<s> [INST] Generate a poem about: bird [/INST] In the quiet hush of...</s>",
#"<s> [INST] Generate a poem about: plane [/INST] In the vast, boundless...</s>",
#"<s> [INST] Generate a poem about: superman [/INST] In the realm where...</s>"
#]]
```


# Invocation
Source: https://docs.baseten.co/development/chain/invocation

Call your deployed Chain

Once your Chain is deployed, you can call it via its API endpoint. Chains use
the same inference API as models:

* [Environment endpoint](/reference/inference-api/predict-endpoints/environments-run-remote)
* [Development endpoint](/reference/inference-api/predict-endpoints/development-run-remote)
* [Endpoint by ID](/reference/inference-api/predict-endpoints/deployment-run-remote)

Here's an example which calls the development deployment:

```python call_chain.py theme={"system"}
import requests
import os

# From the Chain overview page on Baseten
# E.g. "https://chain-<CHAIN_ID>.api.baseten.co/development/run_remote"
CHAIN_URL = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
# JSON keys and types match the `run_remote` method signature.
data = {...}

resp = requests.post(
    CHAIN_URL,
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data,
)

print(resp.json())
```

### How to pass chain input

The data schema of the inference request corresponds to the function
signature of [`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets)
in your entrypoint Chainlet.

For example, for the Hello Chain, `HelloAll.run_remote()`:

```python  theme={"system"}
async def run_remote(self, names: list[str]) -> str:
```

You'd pass the following JSON payload:

```json  theme={"system"}
{ "names": ["Marius", "Sid", "Bola"] }
```

I.e. the keys in the JSON record, match the argument names and values
match the types of`run_remote.`

### Async chain inference

Like Truss models, Chains support async invocation. The [guide for
models](/inference/async) applies largely - in particular for how to wrap the
input and set up the webhook to process results.

The following additional points are chains specific:

* Use chain-based URLS:
  * `https://chain-{chain}.api.baseten.co/production/async_run_remote`
  * `https://chain-{chain}.api.baseten.co/development/async_run_remote`
  * `https://chain-{chain}.api.baseten.co/deployment/{deployment}/async_run_remote`.
  * `https://chain-{chain}.api.baseten.co/environments/{env_name}/async_run_remote`.
* Only the entrypoint is invoked asynchronously. Internal Chainlet-Chainlet
  calls run synchronously.


# Local Development
Source: https://docs.baseten.co/development/chain/localdev

Iterating, Debugging, Testing, Mocking

Chains are designed for production in replicated remote deployments. But
alongside that production-ready power, we offer great local development and
deployment experiences.

<Accordion title="The 6 principles behind Chains">
  Chains exists to help you build multi-step, multi-model pipelines. The
  abstractions that Chains introduces are based on six opinionated principles:
  three for architecture and three for developer experience.

  **Architecture principles**

  <Steps>
    <Step title="Atomic components">
      Each step in the pipeline can set its own hardware requirements and
      software dependencies, separating GPU and CPU workloads.
    </Step>

    <Step title="Modular scaling">
      Each component has independent autoscaling parameters for targeted
      resource allocation, removing bottlenecks from your pipelines.
    </Step>

    <Step title="Maximum composability">
      Components specify a single public interface for flexible-but-safe
      composition and are reusable between projects
    </Step>
  </Steps>

  **Developer experience principles**

  <Steps>
    <Step title="Type safety and validation" stepNumber="4">
      Eliminate entire taxonomies of bugs by writing typed Python code and
      validating inputs, outputs, module initializations, function signatures,
      and even remote server configurations.
    </Step>

    <Step title="Local debugging" stepNumber="5">
      Seamless local testing and cloud deployments: test Chains locally with
      support for mocking the output of any step and simplify your cloud
      deployment loops by separating large model deployments from quick
      updates to glue code.
    </Step>

    <Step title="Incremental adoption" stepNumber="6">
      Use Chains to orchestrate existing model deployments, like pre-packaged
      models from Baseten’s model library, alongside new model pipelines built
      entirely within Chains.
    </Step>
  </Steps>
</Accordion>

Locally, a Chain is just Python files in a source tree. While that gives you a
lot of flexibility in how you structure your code, there are some constraints
and rules to follow to ensure successful distributed, remote execution in
production.

<Tip>
  The best thing you can do while developing locally with Chains is to run your
  code frequently, even if you do not have a  `__main__` section: the Chains
  framework runs various validations at
  <Tooltip tip="i.e. just executing the Chainlet class definitions, but not 
  running their implementation code yet.">module initialization</Tooltip> to help
  you catch issues early.

  Additionally, running `mypy` and fixing reported type errors can help you
  find problems early in a rapid feedback loop, before attempting a (much
  slower) deployment.
</Tip>

<Tip>
  Complementary to the purely local development Chains also has a "watch" mode,
  like Truss, see the [watch guide](/development/chain/watch).
</Tip>

## Test a Chain locally

Let's revisit our "Hello World" Chain:

```python hello_chain/hello.py theme={"system"}
import asyncio
import truss_chains as chains


# This Chainlet does the work
class SayHello(chains.ChainletBase):

    async def run_remote(self, name: str) -> str:
        return f"Hello, {name}"


# This Chainlet orchestrates the work
@chains.mark_entrypoint
class HelloAll(chains.ChainletBase):

    def __init__(self, say_hello_chainlet=chains.depends(SayHello)) -> None:
        self._say_hello = say_hello_chainlet

    async def run_remote(self, names: list[str]) -> str:
        tasks = []
        for name in names:
            tasks.append(asyncio.ensure_future(
                self._say_hello.run_remote(name)))
        
        return "\n".join(await asyncio.gather(*tasks))


# Test the Chain locally
if __name__ == "__main__":
    with chains.run_local():
        hello_chain = HelloAll()
        result = asyncio.get_event_loop().run_until_complete(
            hello_chain.run_remote(["Marius", "Sid", "Bola"]))
        print(result)
```

When the `__main__()` module is run, local instances of the Chainlets are
created, allowing you to test functionality of your chain just by executing the
Python file:

```bash  theme={"system"}
cd hello_chain
python hello.py
# Hello, Marius
# Hello, Sid
# Hello, Bola
```

## Mock execution of GPU Chainlets

Using `run_local()` to run your code locally requires that your development
environment have the compute resources and dependencies that each Chainlet
needs. But that often isn't possible when building with AI models.

Chains offers a workaround, mocking, to let you test the coordination and
business logic of your multi-step inference pipeline without worrying about
running the model locally.

The second example in the [getting started guide](/development/chain/getting-started)
implements a Truss Chain for generating poems with Phi-3.

This Chain has two Chainlets:

1. The `PhiLLM` Chainlet, which can run on NVIDIA GPUs such as the L4.
2. The `PoemGenerator` Chainlet, which easily runs on a CPU.

If you have an NVIDIA T4 under your desk, good for you. For the rest of us, we
can mock the `PhiLLM` Chainlet that is infeasible to run locally so that we can
quickly test the `PoemGenerator` Chainlet.

To do this, we define a mock Phi-3 model in our `__main__` module and give it
a [`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets) method that
produces a test output that matches the output type we expect from the real
Chainlet. Then, we inject an instance of this mock Chainlet into our Chain:

```python poems.py theme={"system"}
if __name__ == "__main__":
    class FakePhiLLM:
        async def run_remote(self, prompt: str) -> str:
            return f"Here's a poem about {prompt.split(" ")[-1]}"


    with chains.run_local():
        poem_generator = PoemGenerator(phi_llm=FakePhiLLM())
        result = asyncio.get_event_loop().run_until_complete(
            poem_generator.run_remote(words=["bird", "plane", "superman"]))
        print(result)
```

And run your Python file:

```bash  theme={"system"}
python poems.py
# ['Here's a poem about bird', 'Here's a poem about plane', 'Here's a poem about superman']
```

### Typing of mocks

You may notice that the argument `phi_llm` expects a type `PhiLLM`, while we
pass an instance of `FakePhiLLM`. These aren't the same, which is formally a
type error.

However, this works at runtime because we constructed `FakePhiLLM` to
implement the same *protocol* as the real thing. We can make this explicit by
defining a `Protocol` as a type annotation:

```python  theme={"system"}
from typing import Protocol


class PhiProtocol(Protocol):
    def run_remote(self, data: str) -> str:
        ...
```

and changing the argument type in `PoemGenerator`:

```python  theme={"system"}
@chains.mark_entrypoint
class PoemGenerator(chains.ChainletBase):
    def __init__(self, phi_llm: PhiProtocol = chains.depends(PhiLLM)) -> None:
        self._phi_llm = phi_llm
```

This is a bit more work and not needed to execute the code, but it shows how
typing consistency can be achieved - if desired.


# Overview
Source: https://docs.baseten.co/development/chain/overview



Chains is a framework for building robust, performant multi-step and multi-model
inference pipelines and deploying them to production. It addresses the common
challenges of managing latency, cost and dependencies for complex workflows,
while leveraging Truss’ existing battle-tested performance, reliability and
developer toolkit.

<video autoPlay muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/animation.mp4?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=79e3b77431748c2b54674fcb2ab94133" data-path="development/chain/images/animation.mp4" />

# User Guides

Guides focus on specific features and use cases. Also refer to
[getting started](/development/chain/getting-started) and
[general concepts](/development/chain/concepts).

<CardGroup cols={3}>
  <Card title="Design" icon="chart-network" iconType="light" href="/development/chain/design">
    How to structure your Chainlets, concurrency, file structure
  </Card>

  <Card title="Local Dev" icon="flask" iconType="light" href="/development/chain/localdev">
    Iterating, Debugging, Testing, Mocking
  </Card>

  <Card title="Deploy" icon="rocket" iconType="light" href="/development/chain/deploy">
    Deploy your Chain on Baseten
  </Card>

  <Card title="Invocation" icon="circle-play" iconType="light" href="/development/chain/invocation">
    Call your deployed Chain
  </Card>

  <Card title="Watch" icon="rotate" iconType="light" href="/development/chain/watch">
    Live-patch deployed code
  </Card>

  <Card title="Subclassing" icon="sitemap" iconType="light" href="/development/chain/subclassing">
    Modularize and re-use Chainlet implementations
  </Card>

  <Card title="Streaming" icon="wind" iconType="light" href="/development/chain/streaming">
    Streaming outputs, reducing latency, SSEs
  </Card>

  <Card title="Binary IO" icon="binary" iconType="light" href="/development/chain/binaryio">
    Performant serialization of numeric data
  </Card>

  <Card title="Error Propagation" icon="triangle-exclamation" iconType="light" href="/development/chain/errorhandling">
    Understanding and handling Chains errors
  </Card>

  <Card title="Truss Integration" icon="cube" iconType="light" href="/development/chain/stub">
    Integrate deployed Truss models with stubs
  </Card>
</CardGroup>

## From model to system

Some models are actually pipelines (e.g. invoking a LLM involves sequentially
tokenizing the input, predicting the next token, and then decoding the predicted
tokens). These pipelines generally make sense to bundle together in a monolithic
deployment because they have the same dependencies, require the same compute
resources, and have a robust ecosystem of tooling to improve efficiency and
performance in a single deployment.
Many other pipelines and systems do not share these properties. Some examples
include:

* Running multiple different models in sequence.
* Chunking/partitioning a set of files and concatenating/organizing results.
* Pulling inputs from or saving outputs to a database or vector store.

Each step in these workflows has different hardware requirements, software
dependencies, and scaling needs so it doesn’t make sense to bundle them in a
monolithic deployment. That’s where Chains comes in!

## Six principles behind Chains

Chains exists to help you build multi-step, multi-model pipelines. The
abstractions that Chains introduces are based on six opinionated principles:
three for architecture and three for developer experience.

**Architecture principles**

<Steps>
  <Step title="Atomic components">
    Each step in the pipeline can set its own hardware requirements and
    software dependencies, separating GPU and CPU workloads.
  </Step>

  <Step title="Modular scaling">
    Each component has independent autoscaling parameters for targeted
    resource allocation, removing bottlenecks from your pipelines.
  </Step>

  <Step title="Maximum composability">
    Components specify a single public interface for flexible-but-safe
    composition and are reusable between projects
  </Step>
</Steps>

**Developer experience principles**

<Steps>
  <Step title="Type safety and validation" stepNumber="4">
    Eliminate entire taxonomies of bugs by writing typed Python code and
    validating inputs, outputs, module initializations, function signatures,
    and even remote server configurations.
  </Step>

  <Step title="Local debugging" stepNumber="5">
    Seamless local testing and cloud deployments: test Chains locally with
    support for mocking the output of any step and simplify your cloud
    deployment loops by separating large model deployments from quick
    updates to glue code.
  </Step>

  <Step title="Incremental adoption" stepNumber="6">
    Use Chains to orchestrate existing model deployments, like pre-packaged
    models from Baseten’s model library, alongside new model pipelines built
    entirely within Chains.
  </Step>
</Steps>

## Hello World with Chains

Here’s a simple Chain that says “hello” to each person in a list of provided
names:

```python hello_chain/hello.py theme={"system"}
import asyncio
import truss_chains as chains


# This Chainlet does the work.
class SayHello(chains.ChainletBase):

    async def run_remote(self, name: str) -> str:
        return f"Hello, {name}"


# This Chainlet orchestrates the work.
@chains.mark_entrypoint
class HelloAll(chains.ChainletBase):

    def __init__(self, say_hello_chainlet=chains.depends(SayHello)) -> None:
        self._say_hello = say_hello_chainlet

    async def run_remote(self, names: list[str]) -> str:
        tasks = []
        for name in names:
            tasks.append(asyncio.ensure_future(
                self._say_hello.run_remote(name)))

        return "\n".join(await asyncio.gather(*tasks))
```

This is a toy example, but it shows how Chains can be used to separate
preprocessing steps like chunking from workload execution steps. If SayHello
were an LLM instead of a simple string template, we could do a much more complex
action for each person on the list.

## What to build with Chains

<AccordionGroup>
  <Accordion title="RAG: retrieval-augmented generation" icon="book">
    Connect to a vector databases and augment LLM results with additional
    context information without introducing overhead to the model inference
    step.

    Try it yourself: [RAG Chain](/examples/chains-build-rag).
  </Accordion>

  <Accordion title="Chunked Audio Transcription and high-throughput pipelines" icon="forward-fast">
    Transcribe large audio files by splitting them into smaller chunks and
    processing them in parallel — we've used this approach to process 10-hour
    files in minutes.

    Try it yourself: [Audio Transcription Chain](/examples/chains-audio-transcription).
  </Accordion>

  <Accordion title="Efficient multi-model pipelines" icon="hand-holding-dollar">
    Build powerful experiences wit optimal scaling in each step like:

    * AI phone calling (transcription + LLM + speech synthesis)
    * Multi-step image generation (SDXL + LoRAs + ControlNets)
    * Multimodal chat (LLM + vision + document parsing + audio)

    Since each stage runs on its hardware with independent auto-scaling,
    you can achieve better hardware utilization and save costs.
  </Accordion>
</AccordionGroup>

Get started by
[building and deploying your first chain](/development/chain/getting-started).


# Streaming
Source: https://docs.baseten.co/development/chain/streaming

Streaming outputs, reducing latency, SSEs

Streaming outputs is useful for returning partial results to the client, before
all data has been processed.

For example LLM text generation happens in incremental text chunks, so the
beginning of the reply can already be sent to the client before the whole
prediction is complete.
Similarly, transcribing audio to text happens in \~30 second chunks and the
first ones can be returned before all completed.

In general, this does not reduce the overall processing time (still the same
amount of work must be done), but the initial latency to get some response
can be reduced significantly.

In some cases it might even reduce overall time, when streaming results
internally in a Chain, allows to start subsequent processing steps sooner -
i.e. pipelining the operations in a more efficient way.

# Low-level streaming

Low-level, streaming works by sending byte chunks (unicode strings will be
implicitly encoded) via HTTP. The most primitive way of doing this in Chains
is by implementing `run_remote` as a bytes- or string-iterator, e.g.:

```python  theme={"system"}
from typing import AsyncIterator
import truss_chains as chains


class Streamlet(chains.ChainletBase):

    async def run_remote(self, inputs: ...) -> AsyncIterator[str]:
        async for text_chunk in make_incremental_outputs(inputs):
            yield text_chunk
```

You are free to chose what data to represent in the byte/string chunks, it
could be raw text generated by an LLM, it could be JSON string, bytes or
anything else.

# Server-sent events (SSEs)

A possible choice is to generate chunks that comply with the
[specification](https://html.spec.whatwg.org/multipage/server-sent-events.html)
of server-sent events.

Concretely, sending JSON strings with `data`, `event` and potentially
other fields and content-type `text/event-stream` .

However, the SSE specification is not opinionated regarding what exactly is
encoded in `data` and what `event`-types exist - you have to make up your schema
that is useful for the client that consumes the data.

# Pydantic and Chainlet-Chainlet-streams

<Info>
  While above low-level streaming is stable, the following helper APIs for typed
  streaming are only stable for intra-Chain streaming.

  If you want to use them for end clients, please reach out to Baseten support,
  so we can discuss the stable solutions.
</Info>

Unlike above "raw" stream example, Chains takes the general opinion that
input and output types should be definite, so that divergence and type
errors can be avoided.

Just like you type-annotate Chainlet inputs and outputs in the non-streaming
case, and use pydantic to manage more complex data structures, we built
tooling to bring the same benefits to streaming.

## Headers and footers

This also helps to solve another challenge of streaming: you might want to
send data of different kinds at the beginning or end of a stream than in
the "main" part.

For example if you transcribe an audio file, you might want
to send many transcription segments in a stream and at the end send some
aggregate information such as duration, detected languages etc.

We model typed streaming like this:

* \[optionally] send a chunk that conforms to the schema of a `Header` pydantic
  model.
* Send 0 to N chunks each conforming to the schema of an `Item` pydantic
  model.
* \[optionally] send a chunk that conforms to the schema of a `Footer` pydantic
  model.

## APIs

### StreamTypes

To have a single source of truth for the types that can be shared between
the producing Chainlet and the consuming client (either a Chainlet in the
Chain or an external client), the chains framework uses a `StreamType`-object:

```python  theme={"system"}
import pydantic
from truss_chains import streaming


class MyDataChunk(pydantic.BaseModel):
    words: list[str]


STREAM_TYPES = streaming.stream_types(
    MyDataChunk, header_type=..., footer_type=...)
```

Note that header and footer types are optional and can be left out:

```python  theme={"system"}
STREAM_TYPES = streaming.stream_types(MyDataChunk)
```

### StreamWriter

Use the `STREAM_TYPES` to create a matching stream writer:

```python  theme={"system"}
from typing import AsyncIterator
import pydantic
import truss_chains as chains
from truss_chains import streaming


class MyDataChunk(pydantic.BaseModel):
    words: list[str]


STREAM_TYPES = streaming.stream_types(MyDataChunk)


class Streamlet(chains.ChainletBase):

    async def run_remote(self, inputs: ...) -> AsyncIterator[bytes]:
        stream_writer = streaming.stream_writer(STREAM_TYPES)
        async for item in make_pydantic_items(inputs):
            yield stream_writer.yield_item(item)
```

If your stream types have header or footer types, corresponding
`yield_header` and `yield_footer` methods are available on the writer.

The writer serializes the pydantic data to `bytes`, so you can also
efficiently represent numeric data (see the
[binary IO guide](/development/chain/binaryio)).

### StreamReader

To consume the stream on either another Chainlet or in the external client, a
matching `StreamReader` is created form your `StreamTypes`. Besides the
types, you connect the reader to the bytes generator that you obtain from the
remote invocation of the streaming Chainlet:

```python  theme={"system"}
import truss_chains as chains
from truss_chains import streaming


class Consumer(chains.ChainletBase):

    def __init__(self, streamlet=chains.depends(Streamlet)):
        self._streamlet = streamlet

    async def run_remote(self, data: ...):
        byte_stream = self._streamlet.run_remote(data)
        reader = streaming.stream_reader(STREAM_TYPES, byte_stream)
        chunks = []
        async for data in reader.read_items():
            chunks.append(data)
```

If you use headers or footers, the reader has async `read_header` and
`read_footer` methods.

<Info>
  Note that the stream can only be consumed once and you have to consume
  header, items and footer in order.
</Info>

<Tip>
  The implementation of `StreamReader` only needs `pydantic`, no other Chains
  dependencies. So you can take that implementation code in isolation and
  integrate it in your client code.
</Tip>


# Truss Integration
Source: https://docs.baseten.co/development/chain/stub

Integrate deployed Truss models with stubs

Chains can be combined with existing Truss models using Stubs.

A Stub acts as a substitute (client-side proxy) for a remotely deployed
dependency, either a Chainlet or a Truss model. The Stub performs the remote
invocations as if it were local by taking care of the transport layer,
authentication, data serialization and retries.

Stubs can be integrated into Chainlets by passing in a URL of the deployed
model. They also require
[`context`](/development/chain/concepts#context-access-information) to be initialized
(for authentication).

```python  theme={"system"}
import truss_chains as chains


class LLMClient(chains.StubBase):

    async def run_remote(self, prompt: str) -> str:
        # Call the deployed model
        resp = await self.predict_async(inputs={
            "messages": [{"role": "user", "content": prompt}],
            "stream"  : False
        })
        # Return a string with the model output
        return resp["output"]


LLM_URL = ...
    
    
class MyChainlet(chains.ChainletBase):

    def __init__(
        self,
        context: chains.DeploymentContext = chains.depends_context(),
    ):
        self._llm = LLMClient.from_url(LLM_URL, context)
```

There are various ways how you can make a call to the other deployment:

* Input as JSON dict (like above) or pydantic model.
* Automatic parsing of the response into an pydantic model using the
  `output_model` argument.
* `predict_async` (recommended) or `predict_async`.
* Streaming responses using `predict_async_stream` which returns an async
  bytes iterator.
* Customized with `RPCOptions`.

See the
[StubBase reference](/reference/sdk/chains#class-truss-chains-stubbase)
for all APIS.


# Subclassing
Source: https://docs.baseten.co/development/chain/subclassing

Modularize and re-use Chainlet implementations

Sometimes you want to write one "main" implementation of a complicated inference
task, but then re-use it for similar variations. For example:

* Deploy it on different hardware and with different concurrency.
* Replace a dependency (e.g. silence detection in audio files) with a
  different implementation of that step - while keeping all other processing
  the same.
* Deploy the same inference flow, but exchange the model weights used. E.g. for
  a large and small version of an LLM or different model weights fine-tuned to\
  domains.
* Add an adapter to convert between a different input/output schema.

In all of those cases, you can create lightweight subclasses of your main
chainlet.

Below are some example code snippets - they can all be combined with each other!

### Example base class

```python  theme={"system"}
import asyncio
import truss_chains as chains


class Preprocess2x(chains.ChainletBase):
    async def run_remote(self, number: int) -> int:
        return 2 * number


class MyBaseChainlet(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        compute=chains.Compute(cpu_count=1, memory="100Mi"),
        options=chains.ChainletOptions(enable_b10_tracing=True),
    )

    def __init__(self, preprocess=chains.depends(Preprocess2x)):
        self._preprocess = preprocess

    async def run_remote(self, number: int) -> float:
        return 1.0 / await self._preprocess.run_remote(number)


# Assert base behavior.
with chains.run_local():
    chainlet = MyBaseChainlet()
    result = asyncio.get_event_loop().run_until_complete(chainlet.run_remote(4))
    assert result == 1 / (4 * 2)
```

### Adapter for different I/O

The base class `MyBaseChainlet` works with integer inputs and returns floats. If
you want to reuse the computation, but provide an alternative interface (e.g.
for a different client with different request/response schema), you can create
a subclass which does the I/O conversion. The actual computation is delegated to
the base classes above.

```python  theme={"system"}
class ChainletStringIO(MyBaseChainlet):
    async def run_remote(self, number: str) -> str:
        return str(await super().run_remote(int(number)))


# Assert new behavior.
with chains.run_local():
    chainlet_string_io = ChainletStringIO()
    result = asyncio.get_event_loop().run_until_complete(
        chainlet_string_io.run_remote("4"))
    assert result == "0.125"
```

### Chain with substituted dependency

The base class `MyBaseChainlet` uses preprocessing that doubles the input. If
you want to use a different variant of preprocessing - while keeping
`MyBaseChainlet.run_remote` and everything else as is - you can define a shallow
subclass of `MyBaseChainlet` where you use a different dependency
`Preprocess8x`, which multiplies by 8 instead of 2.

```python  theme={"system"}
class Preprocess8x(chains.ChainletBase):
    async def run_remote(self, number: int) -> int:
        return 8 * number


class Chainlet8xPreprocess(MyBaseChainlet):
    def __init__(self, preprocess=chains.depends(Preprocess8x)):
        super().__init__(preprocess=preprocess)


# Assert new behavior.
with chains.run_local():
    chainlet_8x_preprocess = Chainlet8xPreprocess()
    result = asyncio.get_event_loop().run_until_complete(
        chainlet_8x_preprocess.run_remote(4))
    assert result == 1 / (4 * 8)
```

### Override remote config.

If you want to re-deploy a chain, but change some deployment options, e.g. run
on different hardware, you can create a subclass and override `remote_config`.

```python  theme={"system"}
class Chainlet16Core(MyBaseChainlet):
    remote_config = chains.RemoteConfig(
        compute=chains.Compute(cpu_count=16, memory="100Mi"),
        options=chains.ChainletOptions(enable_b10_tracing=True),
    )

```

<Warning>
  Be aware that `remote_config` is a class variable. In the example above we
  created a completely new `RemoteConfig` value, because changing fields
  *inplace* would also affect the base class.

  If you want to share config between the base class and subclasses, you can
  define them in additional variables e.g. for the image:

  ```python  theme={"system"}

  DOCKER_IMAGE = chains.DockerImage(pip_requirements=[...], ...)


  class MyBaseChainlet(chains.ChainletBase):
      remote_config = chains.RemoteConfig(docker_image=DOCKER_IMAGE, ...)


  class Chainlet16Core(MyBaseChainlet):
      remote_config = chains.RemoteConfig(docker_image=DOCKER_IMAGE, ...)
  ```
</Warning>


# Watch
Source: https://docs.baseten.co/development/chain/watch

Live-patch deployed code

The [watch command](/reference/cli/chains/chains-cli#watch) (`truss chains watch`) combines
the best of local development and full deployment. `watch` lets you run on an
exact copy of the production hardware and interface but gives you live code
patching that lets you test changes in seconds without creating a new
deployment.

To use `truss chains watch`:

1. Push a chain in development mode (i.e. `publish` and `promote` flags are
   false).
2. Run the watch command `truss chains watch SOURCE`. You can also add the
   `watch` option to the `push` command and combine both to a single step.
3. Each time you edit a file and save the changes, the watcher patches the
   remote deployments. Updating the deployments might take a moment, but is
   generally *much* faster than creating a new deployment.
4. You can call the chain with test data via `cURL` or the playground dialogue
   in the UI and observe the result and logs.
5. Iterate steps 3. and 4. until your chain behaves in the desired way.

### Selective Watch

Some large ML models might have a slow cycle time to reload (e.g. if the
weights are huge). For this case, we provide a "selective" watch option. For
example if your chain has such a heavy model Chainlet and other Chainlets
that contain only business logic, you can iterate on those, while not patching
and reloading the heavy model Chainlet.

<Warning>
  This feature is really useful for advanced use case, but must be used with
  caution.
  If you change the code of a Chainlet not watched, in particular I/O types,
  you get an inconsistent deployment.
</Warning>

Add the Chainlet names you want to watch as a comma separated list:

```shell  theme={"system"}
truss chains watch ... --experimental-chainlet-names=ChainletA,ChainletB
```


# Concepts
Source: https://docs.baseten.co/development/concepts



Baseten provides two core development workflows: [developing a model with Truss](/development/model/) and orchestrating models with [Chains](/development/chain/). Both are building blocks for production-grade ML systems, but they solve different problems.

<CardGroup cols={2}>
  <Card title="Developing a model with Truss" href="/development/model" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c320f770ea283b7d13e89533d202016d" data-og-width="956" width="956" data-og-height="458" height="458" data-path="images/how-baseten-works-truss.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=23b6782ea9c86030a14db14c36075704 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3d04a8c7770d8f8d9f2d52f9063d01e2 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=d33af8a0f99292fad4285ff2e5483d65 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b411bb63f8f7fe75b87238373cb57a36 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=ead28695833c12dc1d5bf1a69416215c 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-truss.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e8e8158fb146440aa46530fb4d88d539 2500w">
    Package and deploy any AI/ML model as an API with Truss or a Custom Server.
  </Card>

  <Card title="Developing a Chain" href="/development/chain" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=672e515bad1fd2888cc65381c5a5010c" data-og-width="956" width="956" data-og-height="458" height="458" data-path="images/how-baseten-works-chains.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8f1be4c10da7f8ca84c726152936cd75 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=70a1a3e26bb1429518857a1195eced27 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=b1e97197db352d3b68b0c02f5c61ae27 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=454929ec2319e4f64eaded013e5d58a0 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=7a720c4d02fc41515678a7dfd189bc55 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/how-baseten-works-chains.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=4455e2b78247363a9ca0564a628a1aee 2500w">
    Orchestrate multiple models and logic, enabling complex inference workflows.
  </Card>
</CardGroup>

## Truss vs. Chains: When to use each

### Developing a model with Truss

[Truss](/development/model/overview) is the open-source package you use to turn any ML model into a production-ready API on Baseten - without needing to learn Docker or build custom infrastructure.

**Use Truss when:**

* **You’re deploying a single model.** Whether it’s a fine-tuned transformer, diffusion model, or traditional classifier, Truss helps you package it with code, configuration, and system requirements to deploy at scale.

* **You want flexibility across tools and frameworks.** Build with your preferred model frameworks (e.g. **PyTorch**, **transformers**, **diffusers**), inference engines (e.g. **TensorRT-LLM**, **SGLang**, **vLLM**), and serving technologies (like **Triton**) as well as [any package](/development/model/configuration) installable via `pip` or `apt`.

* **You need control over how your model runs.** Define pre- and post-processing, batching, logging, and custom inference logic. Truss gives you full access to environment settings and dependencies, versioned and deployable.

* **You want to keep development local and reproducible.** Develop locally in a containerized environment that mirrors production, test confidently, and ship your model without surprises.

### Orchestrating with Chains

[Chains](/development/chain/overview) are for building inference workflows that span multiple steps, models, or tools. You define a sequence of steps — like routing, transformation, or chaining outputs — and run them as a single unit.

**Use Chains when:**

* **You’re combining multiple models or tools.**
  For example, running a vector search + LLM pipeline, or combining OCR, classification, and validation steps.

* **You want visibility into intermediate steps.**
  Chains let you debug and monitor each part of the workflow, retry failed steps, and trace outputs with ease — something that’s much harder with a single model endpoint.

* **You’re using orchestration libraries like LangChain or LlamaIndex.**
  Chains integrate natively with these frameworks, while still allowing you to insert your own logic or wrap Truss models as steps.


# Deprecation
Source: https://docs.baseten.co/development/model-apis/deprecation

Overview of Baseten’s deprecation policy for Model APIs.

## Deprecation Process

As open source models advance rapidly, we prioritize serving the highest quality models and deprecate specific Model APIs when stronger alternatives are available. When a model is selected for deprecation we follow the below process:

1. **Announcement**
   * Deprecations are announced \~2 weeks prior to the deprecation date
   * Updated documentation identifying the model to be deprecated along with a recommended replacement
   * Affected users will be contacted via email
2. **Transition**
   * The deprecating model will remain fully functional until the final deprecation date. Following the initial deprecation announcement users have \~2 weeks to transition. There are two options:
     1. Migrate to a dedicated deployment with the deprecated model weights [contact us](https://www.baseten.co/talk-to-us/deprecation-inquiry/)
     2. Shift the Model API model ID to an active model (we provide a recommendation in the deprecation announcement)
3. **Deprecation date**
   * The model ID for the deprecated model will become inactive and return an error for all requests
   * Changelog notification of deprecation with a recommended replacement

## Planned Deprecations

There are no planned deprecations at this time.


# Using Model APIs on Baseten
Source: https://docs.baseten.co/development/model-apis/overview

Use Baseten's OpenAI-compatible Model APIs for LLMs, including structured outputs and tool calling.

Baseten provides **OpenAI-compatible API endpoints** for all available Model APIs. This means you can use standard OpenAI client libraries—no wrappers, no rewrites, no surprises. If your code already works with OpenAI, it'll work with Baseten.

This guide walks you through getting started, making your first call, and using advanced features like structured outputs and tool calling.

## Prerequisites

Before you begin, make sure you have:

1. A [Baseten account](https://app.baseten.co/signup/)
2. An [API key](https://app.baseten.co/settings/api_keys)
3. The [OpenAI client library](https://platform.openai.com/docs/libraries) for your language of choice

## Supported models

Baseten currently offers several high-performing open-source LLMs as [Models APIs](https://app.baseten.co/model-apis/create):

* **OpenAI GPT OSS 120B** (slug: `openai/gpt-oss-120b`)
* **Qwen3 235B 2507** (slug: `Qwen/Qwen3-235B-A22B-Instruct-2507`)
* **Qwen3 Coder 480B** (slug: `Qwen/Qwen3-Coder-480B-A35B-Instruct`)
* **Kimi K2 0905** (slug: `moonshotai/Kimi-K2-Instruct-0905`)
* **Deepseek V3.1** (slug: `deepseek-ai/DeepSeek-V3.1`)
* **Deepseek R1 0528** (slug: `deepseek-ai/DeepSeek-R1-0528`)
* **Deepseek V3 0324** (slug: `deepseek-ai/DeepSeek-V3-0324`)
* **Z AI GLM4.6** (slug: `zai-org/GLM-4.6`)
* **Kimi K2 Thinking** (slug: `moonshotai/Kimi-K2-Thinking`)

Please update the `model` in the examples below to the slug of the model you'd like to test.

## Make your first API call

<Tabs>
  <Tab title="Python">
    ```python  theme={"system"}
    client = OpenAI(
        base_url="https://inference.baseten.co/v1",
        api_key=os.environ.get("BASETEN_API_KEY")
    )

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Your question here"}
        ]
    )

    print(response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```jsx  theme={"system"}
    const client = new OpenAI({
        baseURL: "https://inference.baseten.co/v1",
        apiKey: process.env.BASETEN_API_KEY,
    });

    // Use the client
    try {
        const response = await client.chat.completions.create({
            model: "deepseek-ai/DeepSeek-V3-0324",
            messages: [
                { role: "system", content: "You are a helpful assistant." },
                { role: "user", content: "Hello, how are you?" },
            ],
        })
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={"system"}
    curl https://inference.baseten.co/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '{
          "model": "deepseek-ai/DeepSeek-V3-0324",
          "messages": [{ "role": "user", "content": "Your content here" }],
          "stream": true,
          "max_tokens": 10
        }'
    echo # Add a newline for cleaner output
    ```
  </Tab>
</Tabs>

## Request parameters

Model APIs support all commonly used [OpenAI ChatCompletions](https://platform.openai.com/docs/api-reference/chat) parameters, including:

* `model`: Slug of the model you want to call (see below)
* `messages`: Array of message objects (`role` + `content`)
* `temperature`: Controls randomness (0-2, default 1)
* `max_tokens`: Maximum number of tokens to generate
* `stream`: Boolean to enable streaming responses

## Structured outputs

To get structured JSON output from the model, you can use the `response_format` parameter. Set `response_format={"type": "json_object"}` to enable JSON mode. For more complex schemas, you can define a JSON schema.

Let's say you want to extract specific information from a user's query, like a name and an email address.

<Tabs>
  <Tab title="Python">
    ```python  theme={"system"}
    client = OpenAI(
        base_url="https://inference.baseten.co/v1",
        api_key=os.environ.get("BASETEN_API_KEY")
    )

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324", # Or any other supported model
        messages=[
            {"role": "system", "content": "You are an expert at extracting information."},
            {"role": "user", "content": "My name is Jane Doe and my email is jane.doe@example.com. I\'d like to know more about your services."}
        ],
        response_format={
            "type": "json_object",
            "json_schema": {
                "name": "user_details",
                "description": "User contact information",
                "schema": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The user\'s full name"
                        },
                        "email": {
                            "type": "string",
                            "description": "The user\'s email address"
                        }
                    },
                    "required": ["name", "email"]
                },
                "strict": True # Enforce schema adherence
            }
        }
    )

    output = json.loads(response.choices[0].message.content)
    print(output)
    # Expected output:
    # {
    #   "name": "Jane Doe",
    #   "email": "jane.doe@example.com"
    # }
    ```
  </Tab>

  <Tab title="JavaScript">
    ```jsx  theme={"system"}
    const client = new OpenAI({
        baseURL: "https://inference.baseten.co/v1",
        apiKey: process.env.BASETEN_API_KEY,
    });

    // Use the client for structured output
    try {
        const response = await client.chat.completions.create({
            model: "deepseek-ai/DeepSeek-V3-0324",
            messages: [
                { role: "system", content: "You are an expert at extracting information." },
                { role: "user", content: "My name is Jane Doe and my email is jane.doe@example.com. I'd like to know more about your services." },
            ],
            response_format: {
                type: "json_object",
                json_schema: {
                    name: "user_details",
                    description: "User contact information",
                    schema: {
                        type: "object",
                        properties: {
                            name: { 
                                type: "string", 
                                description: "The user's full name" 
                            },
                            email: { 
                                type: "string", 
                                description: "The user's email address" 
                            }
                        },
                        required: ["name", "email"]
                    },
                    strict: true
                }
            }
        })
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={"system"}
    curl -s "https://inference.baseten.co/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d @- << EOF
    {
    "model": "deepseek-ai/DeepSeek-V3-0324",
    "messages": [
    {"role": "system", "content": "You are an expert at extracting information."},
    {"role": "user", "content": "My name is Jane Doe and my email is jane.doe@example.com. I'd like to know more about your services."}
    ],
    "response_format": {
    "type": "json_object",
    "json_schema": {
      "name": "user_details",
      "description": "User contact information",
      "schema": {
        "type": "object",
        "properties": {
          "name": { "type": "string", "description": "The user's full name" },
          "email": { "type": "string", "description": "The user's email address" }
        },
        "required": ["name", "email"]
      },
      "strict": true
    }
    }
    }
    EOF

    echo # Add a newline for cleaner output
    ```
  </Tab>
</Tabs>

When `strict: true` is specified within the `json_schema`, the model is constrained to produce output that strictly adheres to the provided schema. If the model cannot or will not produce output that matches the schema, it may return an error or a refusal.

## Tool calling

<Warning>
  **Model compatibility note:** We recommend using **Deepseek V3** for tool calling functionality. We do not recommend using *Deepseek R1* for tool calling as the model was not post-trained for tool calling.
</Warning>

Tool calling is fully supported. Simply define a list of tools and pass them via the `tools` parameter:

* `type`: The type of tool to call. Currently, the only supported value is `function`.
* `function`: A dictionary with the following keys:
  * `name`: The name of the function to be called
  * `description`: A description of what the function does
  * `parameters`: A JSON Schema object describing the function parameters

```python  theme={"system"}
# Example list of tools
{
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the weather for a location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "City and state"
            }
          },
          "required": ["location"]
        }
      }
    }
  ]
}
```

Here's how you might implement tool calling:

<Tabs>
  <Tab title="Python">
    ```python  theme={"system"}
    client = OpenAI(
        base_url="https://inference.baseten.co/v1",
        api_key=os.environ.get("BASETEN_API_KEY")
    )

    # Define the message and available tools
    messages = [{"role": "user", "content": "What's the weather like in Boston?"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {"type": "string", "description": "City name"},
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                    },
                    "required": ["location"]
                }
            }
        }
    ]

    # Make the initial request
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    # Process tool calls if any
    if response.choices[0].message.tool_calls:
        # Get the function call details
        tool_call = response.choices[0].message.tool_calls[0]
        function_args = json.loads(tool_call.function.arguments)
        
        # Call the function and get the result
        function_response = get_weather(location=function_args.get("location"))
        
        # Add function response to conversation
        messages.append(response.choices[0].message)
        messages.append({
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": tool_call.function.name,
            "content": function_response
        })
        
        # Get the final response with the function result
        final_response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=messages
        )
        print(final_response.choices[0].message.content)
    ```
  </Tab>

  <Tab title="JavaScript">
    ```jsx  theme={"system"}
    const client = new OpenAI({
        baseURL: "https://inference.baseten.co/v1",
        apiKey: process.env.BASETEN_API_KEY,
    });

    // Make initial request with tools
    const response = await client.chat.completions.create({
        model: "deepseek-ai/DeepSeek-V3-0324",
        messages: [{ role: "user", content: "What's the weather like in Boston?" }],
        tools: [{
            type: "function",
            function: {
                name: "get_weather",
                description: "Get the current weather",
                parameters: {
                    type: "object",
                    properties: {
                        location: { type: "string", description: "City name" }
                    },
                    required: ["location"]
                }
            }
        }]
    });

    // Process tool calls if any
    if (response.choices[0].message.tool_calls) {
        const toolCall = response.choices[0].message.tool_calls[0];
        const args = JSON.parse(toolCall.function.arguments);
        
        // Call function and get result
        const functionResponse = getWeather(args.location);
        
        // Submit function result back to model
        const messages = [
            { role: "user", content: "What's the weather like in Boston?" },
            response.choices[0].message,
            { tool_call_id: toolCall.id, role: "tool", name: "get_weather", content: functionResponse }
        ];
        
        const finalResponse = await client.chat.completions.create({
            model: "deepseek-ai/DeepSeek-V3-0324",
            messages: messages
        })
    ```
  </Tab>

  <Tab title="cURL">
    ```bash  theme={"system"}
    curl -s "https://inference.baseten.co/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '{
    "model": "deepseek-ai/DeepSeek-V3-0324",
    "messages": [{"role": "user", "content": "What'\''s the weather like in Boston?"}],
    "tools": [{
      "type": "function",
      "function": {
        "name": "get_weather",
        "description": "Get the current weather",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {"type": "string", "description": "City name"}
          },
          "required": ["location"]
        }
      }
    }]
    }')

    # Extract tool call details
    TOOL_CALL_ID=$(
    # If we have a tool call, prepare the weather data and send it back
    if [ -n "$TOOL_CALL_ID" ]; then
    WEATHER_DATA='{"location":"Boston","temperature":"72","forecast":"sunny"}'

    # Send the function result back to the API
    FINAL_RESPONSE=$(curl -s "https://inference.baseten.co/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '{
      "model": "deepseek-ai/DeepSeek-V3-0324",
      "messages": [
        {"role": "user", "content": "What'\''s the weather like in Boston?"},
        {"role": "assistant", "content": null, "tool_calls": [{"id": "'$TOOL_CALL_ID'", "type": "function", "function": {"name": "get_weather", "arguments": "{\"location\":\"Boston\"}"}}]},
        {"role": "tool", "tool_call_id": "'$TOOL_CALL_ID'", "name": "get_weather", "content": "'$WEATHER_DATA'"}
      ]
    }')

    # Print the final response
    fi
    ```
  </Tab>
</Tabs>

## Error Handling

The API returns standard HTTP error codes:

* `400`: Bad request (malformed input)
* `401`: Unauthorized (invalid or missing API key)
* `402`: Payment required
* `404`: Model not found
* `429`: Rate limit exceeded
* `500`: Internal server error

Check the response body for specific error details and suggested resolutions.

## Migrating from OpenAI

To migrate from OpenAI to Baseten's OpenAI-compatible API, you need to make these changes to your existing code:

1. Replace your OpenAI API key with your Baseten API key
2. Change the base URL to `https://inference.baseten.co/v1.`
3. Update model names to match Baseten-supported slugs.


# Rate Limits & Budgets
Source: https://docs.baseten.co/development/model-apis/rate-limits-and-budgets

Learn about rate limits for Baseten's Model APIs and how to set usage budgets to control costs.

## Rate Limits

To ensure fair use and system stability, Baseten enforces two rate limits:

* **Request rate limits** — maximum number of API requests per minute
* **Token rate limits** — maximum number of tokens processed per minute (input + output combined)

Default limits vary based on your account status.

| Account                  |                                         RPM |                                         TPM |
| :----------------------- | ------------------------------------------: | ------------------------------------------: |
| **Starter** (unverified) |                                          15 |                                     100,000 |
| **Starter** (verified)   |                                         120 |                                     500,000 |
| **Business**             |                                         120 |                                   1,000,000 |
| **Enterprise**           | [Custom](https://www.baseten.co/talk-to-us) | [Custom](https://www.baseten.co/talk-to-us) |

<Warning>
  If you exceed these limits, the API will return a `429 Too Many Requests`
  error. Request a higher rate limit by [contacting us](https://www.baseten.co/talk-to-us/increase-rate-limits/).
</Warning>

### Requesting higher limits

If you have high volume, are a verified customer, and need more headroom, you can [contact us](https://www.baseten.co/talk-to-us/increase-rate-limits/) to request a rate limit increase.

***

## Setting budgets

Setting a budget allows you to control your Model API usage and avoid unexpected costs. Usage budgets apply only to Model APIs (not dedicated deployments). Your team will be notified by email at 75%, 90%, and 100% of budget.

### Enforcing budgets

When setting a budget, you can choose to enforce it or not.

* **If you choose to enforce it**, requests will be rejected once the budget is reached.
* **If you choose not to enforce it**, you will be notified at 75%, 90%, and 100% of budget and you'll be responsible for any costs incurred over the budget.


# b10cache 🆕
Source: https://docs.baseten.co/development/model/b10cache

Persist data across replicas or deployments

<Warning>
  ### Early Access

  Please contact our [support team](mailto:support@baseten.co) for access to b10cache.
</Warning>

Deployments sometimes have cache or other files that are useful to other replicas. Using `torch.compile` results in a cache that can speed up future `torch.compile` on the same function. This can speed up other replicas' cold start times.

**These files can be stored via b10cache**. b10cache is a volume mounted over the network onto each of your pods. There are two ways files can be stored:

#### 1. `/cache/org/`

This directory is shared, and can be written to or accessed by every pod you deploy. Simply move a file into here and it will be accessible.

#### 2. `/cache/model/`

This directory is shared by every pod within the scope of your deployment. This is excellent for keeping filesystems clean and limiting access.

<Danger>
  ### Not a persistent object storage

  While b10cache is very reliable, it should not be used as a persistent object storage or database. **It should be considered a cache** that can be shared by deployments, meaning there should always be a fallback plan if the b10cache path does not exist.
</Danger>

See two features built on b10cache:

1. [*model cache*](/development/model/model-cache)
2. [*torch compile cache*](/development/model/torch-compile-cache)


# Base Docker images
Source: https://docs.baseten.co/development/model/base-images

A guide to configuring a base image for your truss

Truss uses containerized environments to ensure consistent model execution across deployments. While the default Truss image works for most cases, you may need a custom base image to meet specific package or system requirements.

## Setting a base image in`config.yaml`

Specify a custom base image in `config.yaml`:

```yaml config.yaml theme={"system"}
base_image:
  image: <image_name:tag>
  python_executable_path: <path-to-python>
```

* `image`: The Docker image to use.
* `python_executable_path`: The path to the Python binary inside the container.

### Example: NVIDIA NeMo Model

Using a custom image to deploy [NVIDIA NeMo TitaNet](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/titanet_large) model:

```yaml config.yaml theme={"system"}
base_image:
  image: nvcr.io/nvidia/nemo:23.03
  python_executable_path: /usr/bin/python
apply_library_patches: true
requirements:
  - PySoundFile
resources:
  accelerator: T4
  cpu: 2500m
  memory: 4512Mi
  use_gpu: true
secrets: {}
system_packages:
  - python3.8-venv
```

## Using Private Base Images

If your base image is private, ensure that you have configured your model to use a [private registry](/development/model/private-registries)

## Creating a custom base image

You can build a new base image using Truss’s base images as a foundation. Available images are listed on [Docker Hub](https://hub.docker.com/r/baseten/truss-server-base/tags).

#### Example: Customizing a Truss Base Image

```Dockerfile Dockerfile theme={"system"}
FROM baseten/truss-server-base:3.11-gpu-v0.7.16
RUN pip uninstall cython -y
RUN pip install cython==0.29.30
```

#### Building & Pushing Your Custom Image

Ensure Docker is installed and running. Then, build, tag, and push your image:

```sh  theme={"system"}
docker build -t my-custom-base-image:0.1 .
docker tag my-custom-base-image:0.1 your-docker-username/my-custom-base-image:0.1
docker push your-docker-username/my-custom-base-image:0.1
```


# Custom build commands
Source: https://docs.baseten.co/development/model/build-commands

How to run your own docker commands during the build stage

The `build_commands` feature allows you to **run custom Docker commands** during the **build stage**, enabling **advanced caching**, **dependency management**, **and environment setup**.

**Use Cases:**

* Clone GitHub repositories
* Install dependencies
* Create directories
* Pre-download model weights

## 1. Using Build Commands in `config.yaml`

Add `build_commands` to your `config.yaml`:

```yaml  theme={"system"}
build_commands:
  - git clone https://github.com/comfyanonymous/ComfyUI.git
  - cd ComfyUI && git checkout b1fd26fe9e55163f780bf9e5f56bf9bf5f035c93 && pip install -r requirements.txt
model_name: Build Commands Demo
python_version: py310
resources:
  accelerator: A100
  use_gpu: true
```

**What happens?**

* The GitHub repository is cloned.
* The specified commit is checked out.
* Dependencies are installed.
* **Everything is cached at build time**, reducing deployment cold starts.

## 2. Creating Directories in Your Truss

Use `build_commands` to **create directories** directly in the container.

```yaml  theme={"system"}
build_commands:
  - git clone https://github.com/comfyanonymous/ComfyUI.git
  - cd ComfyUI && mkdir ipadapter
  - cd ComfyUI && mkdir instantid
```

<Info>Useful for **large codebases** requiring additional structure.</Info>

## 3. Caching Model Weights Efficiently

<Warning>For large weights (10GB+), use `model_cache` or `external_data`.</Warning>

For smaller weights, **use** `wget` in `build_commands`:

```yaml  theme={"system"}
build_commands:
  - git clone https://github.com/comfyanonymous/ComfyUI.git
  - cd ComfyUI && pip install -r requirements.txt
  - cd ComfyUI/models/controlnet && wget -O control-lora-canny-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-canny-rank256.safetensors
  - cd ComfyUI/models/controlnet && wget -O control-lora-depth-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors
model_name: Build Commands Demo
python_version: py310
resources:
  accelerator: A100
  use_gpu: true
system_packages:
  - wget
```

**Why use this?**

* **Reduces startup time** by **preloading model weights** during the build stage.
* **Ensures availability** without runtime downloads.

## 4. Running Any Shell Command

The `build_commands` feature lets you execute **any** shell command as if running it locally, with the benefit of **caching the results** at build time.

**Key Benefits:**

* **Reduces cold starts** by caching dependencies & data.
* **Ensures reproducibility** across deployments.
* **Optimizes environment setup** for fast execution.


# Your first model
Source: https://docs.baseten.co/development/model/build-your-first-model

Build and deploy your first model

This quickstart guide shows you how to build and deploy your first model,
using Baseten's Truss framework.

## Prerequisites

To use Truss, install a recent Truss version and ensure pydantic is v2:

```bash  theme={"system"}
pip install --upgrade truss 'pydantic>=2.0.0'
```

<Accordion title="Help for setting up a clean development environment">
  Truss requires python `>=3.8,<3.13`. To set up a fresh development environment,
  you can use the following commands, creating a environment named `truss_env`
  using `pyenv`:

  ```bash  theme={"system"}
  curl https://pyenv.run | bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  source ~/.bashrc
  pyenv install 3.11.0
  ENV_NAME="truss_env"
  pyenv virtualenv 3.11.0 $ENV_NAME
  pyenv activate $ENV_NAME
  pip install --upgrade truss 'pydantic>=2.0.0'
  ```
</Accordion>

To deploy Truss remotely, you also need a
[Baseten account](https://app.baseten.co/signup).
It is handy to export your API key to the current shell session or permanently in your `.bashrc`:

```bash ~/.bashrc theme={"system"}
export BASETEN_API_KEY="nPh8..."
```

## Initialize your model

Truss is a tool that helps you package your model code and configuration, and ship it to Baseten for deployment, testing, and scaling.

To create your first model, you can use the `truss init` command.

```bash  theme={"system"}
$ truss init hello-world
? 📦 Name this model: HelloWorld
Truss HelloWorld was created in ~/hello-world
```

This will create a new directory called `hello-world` with the following files:

* `config.yaml` - A configuration file for your model.
* `model/model.py` - A Python file that contains your model code
* `packages/` - A folder to hold any dependencies your model needs
* `data/` - A folder to hold any data your model needs

For this example, we'll focus on the `config.yaml` file and the `model.py` file.

### `config.yaml`

The `config.yaml` file is used to configure dependencies, resources, and
other settings for your model.

Let's take a look at the contents:

```yaml config.yaml theme={"system"}
build_commands: []
environment_variables: {}
external_package_dirs: []
model_metadata: {}
model_name: HelloWorld
python_version: py311
requirements: []
resources:
  accelerator: null
  cpu: '1'
  memory: 2Gi
  use_gpu: false
secrets: {}
system_packages: []
```

Some key fields to note:

* `requirements`: This is a list of `pip` packages that will be installed when
  your model is deployed.
* `resources`: This is where you can specify the resources your model will use.
* `secrets`: This is where you can specify any secrets your model will need, such as
  HuggingFace API keys.

See the [Configuration](/development/model/configuration) page for more information on the `config.yaml` file.

### `model.py`

Next, let's take a look at the `model.py` file.

```python  theme={"system"}
class Model:
    def __init__(self, **kwargs):
        pass

    def load(self):
        pass

    def predict(self, model_input):
        return model_input 
```

In Truss models, we expect users to provide a Python class with the following methods:

* `__init__`: This is the constructor.
* `load`: This is called at model startup, and should include any setup logic, such as weight downloading or initialization
* `predict`: This is the method that is called during inference.

## Deploy your model

To deploy your model, you can use the `truss push` command.

```bash  theme={"system"}
$ truss push
```

This will deploy your model to Baseten.

## Invoke your model

After deploying your model, you can invoke it with the invocation URL provided:

```bash  theme={"system"}
$ curl -X POST https://model-{model-id}.api.baseten.co/development/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -d '"some text"'
"some text"
```

## A Real Example

To show a slightly more complex example, let's deploy a text classification model
from HuggingFace!

In this example, we'll use the `transformers` library to load a pre-trained model,
from HuggingFace, and use it to classify the given text.

### `config.yaml`

To deploy this model, we need to add a few more dependencies to our `config.yaml` file.

```yaml config.yaml theme={"system"}
requirements:
  - transformers
  - torch
```

### `model.py`

Next, let's change our `model.py` file to use the `transformers` library to load the model,
and then use it to predict the sentiment of a given text.

```python model.py theme={"system"}
from transformers import pipeline

class Model:
    def __init__(self, **kwargs):
        pass

    def load(self):
        self._model = pipeline("text-classification")

    def predict(self, model_input):
        return self._model(model_input)
```

## Running inference

Similarly to our previous example, we can deploy this model using `truss push`

```bash  theme={"system"}
$ truss push
```

And then invoke it using the invocation URL on Baseten.

```bash  theme={"system"}
$ curl -X POST https://model-{model-id}.api.baseten.co/development/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -d '{"text": "some text"}'
```

## Next steps

Now that you've deployed your first model, you can learn more about more
options for [configuring your model](/development/model/configuration),
and [implementing your model](/development/model/implementation).


# Python driven configuration for models 🆕
Source: https://docs.baseten.co/development/model/code-first-development

Use code-first development tools to streamline model production.

<Info> This feature is still in beta. </Info>

In addition to our normal YAML configuration, we support configuring your model using pure Python. This offers the following benefits:

* **Typed configuration via Python code** with IDE autocomplete, instead of a separate `yaml` configuration file
* **Simpler directory structure** that IDEs support for module resolution

In this guide, we go through deploying a simple Model using this new framework.

### Step 1: Initializing your project

We leverage traditional `truss init` functionality with a new flag to create the directory structure:

```bash  theme={"system"}
truss init my-new-model --python-config
```

### Step 2: Write your model

To build a model with this new framework, we require two things:

* A class that inherits from `baseten.ModelBase`, which will serve as the entrypoint when invoking `/predict`
* A `predict` method with type hints

That’s it! The following is a contrived example of a complete model that will keep a running total of user provided input:

```python my_model.py theme={"system"}
import truss_chains as baseten


class RunningTotalCalculator(baseten.ModelBase):
    def __init__(self):
        self._running_total = 0

    async def predict(self, increment: int) -> int:
        self._running_total += increment
        return self._running_total
```

### Step 3: Deploy, patch, and public your model

In order to deploy the first version of your new model, you can run:

```bash  theme={"system"}
truss push my_model.py
```

Please note that `push` (as well as all other commands below) will require that you pass the path to the file containing the model as the final argument.

This new workflow also supports patching, so you can quickly iterate during development without building new images every time.

```bash  theme={"system"}
truss watch my_model.py
```

### Model Configuration

Models can configure requirements for compute hardware (CPU count, GPU type and count, etc) and software dependencies (Python libraries or system packages) via the [`remote_config`](/reference/sdk/chains#remote-configuration) class variable within the model:

```python my_model.py theme={"system"}
class RunningTotalCalculator(baseten.ModelBase):
    remote_config: baseten.RemoteConfig = baseten.RemoteConfig(
        compute=baseten.Compute(cpu_count=4, memory="1Gi", gpu="T4", gpu_count=2)
    )

    ...
```

See the [remote configuration reference](/reference/sdk/chains#remote-configuration) for a complete list of options.

### Context (access information)

You can add [`DeploymentContext`](/reference/sdk/chains#class-truss-chains-deploymentcontext) object as an optional final argument to the **`__init__`**-method of a Model. This allows you to use secrets within your Model, but note that they’ll also need to be added to the **`assets`**.

We only expose secrets to the model that were explicitly requested in `assets` to comply with best security practices.

```python my_model.py theme={"system"}
class RunningTotalCalculator(baseten.ModelBase):
    remote_config: baseten.RemoteConfig = baseten.RemoteConfig(
        ...
        assets=baseten.Assets(secret_keys=["token"])
    )

    def __init__(self, context: baseten.DeploymentContext = baseten.depends_context()):
        ...
        self._token = context.secrets["token"]

```

### Packages

If you want to include modules in your model, you can easily create them from the root of the project:

```bash  theme={"system"}
my-new-model/
    module_1/
	    submodule/
		    script.py
    module_2/
	    another_script.py
    my_model.py
```

With this file structure, you would import in `my_model.py` as follows:

```python my_model.py theme={"system"}
import truss_chains as baseten

from module_1.submodule import script
from module_2 import another_script

class RunningTotalCalculator(baseten.ModelBase):
    ....
```

### Known Limitations

* RemoteConfig does *not* support all the options exposed by the traditional `config.yaml`. If you’re excited about this new development experience but need a specific feature ported over, please reach out to us!
* This new framework does not support `preprocess` or `postprocess` hooks. We typically recommend inlining functionality from those functions if easy, or utilizing `chains` if the needs are more complex.


# Configuration
Source: https://docs.baseten.co/development/model/configuration

How to configure your model.

ML models often have dependencies on external libraries, data,
and other resources. These models also typically have particular
hardware configurations.

In this guide, we'll cover the basics of how to configure your model
to specify this information.

Configuration for models is specified in the `config.yaml` file. Here are some
of the common configuration options:

# Environment variables

You can specify environment variables to be set in the model serving environment
using the `environment_variables` key.

```yaml config.yaml theme={"system"}
environment_variables:
  MY_ENV_VAR: my_value
```

# Python Packages

Python packages can be specified in two ways in the `config.yaml` file:

1. `requirements`: A list of Python packages to install.
2. `requirements_file`: A requirements.txt file to install pip packages from.

For example, if you have a simple list of packages, you can specify them as follows:

```yaml config.yaml theme={"system"}
requirements:
  - package_name
  - package_name2
```

Note that you can pin versions using the `==` operator.

```yaml config.yaml theme={"system"}
requirements:
  - package_name==1.0.0
  - package_name2==2.0.0
```

If you need more control over the installation process and want to use
different pip options or repositories, you can specify a `requirements_file`
instead.

```yaml config.yaml theme={"system"}
requirements_file: ./requirements.txt
```

# System Packages

Truss also has support for installing apt-installable Debian packages. to
add system packages to your model serving environment, add the following to
your `config.yaml` file:

```yaml config.yaml theme={"system"}
system_packages:
  - package_name
  - package_name2
```

For a more concrete examples,

```yaml config.yaml theme={"system"}
system_packages:
  - tesseract-ocr
```

# Resources

Another key part of configuring your model is specifying hardware resources needed.
You can use the `resources` key to specify these. For a CPU model, your resources
configuration might look something like:

```yaml config.yaml theme={"system"}
resources:
  accelerator: null
  cpu: "1"
  memory: 2Gi
  use_gpu: false
```

For a GPU model, your resources configuration might look like:

```yaml config.yaml theme={"system"}
resources:
  accelerator: "L4"
```

When you push your model, it will be assigned an instance type matching the
specifications required.

See the [Resources](/deployment/resources) page for more information on
options available.

# Advanced configuration

There are numerous other options for configuring your model. See some
of the other guides:

* [Secrets](/development/model/secrets)
* [Data](/development/model/data-directory)
* [Custom Build Commands](/development/model/build-commands)
* [Base Docker Images](/development/model/base-images)
* [Custom Servers](/development/model/custom-server)
* [Custom Health Checks](/development/model/custom-health-checks)


# Custom health checks 🆕
Source: https://docs.baseten.co/development/model/custom-health-checks

Customize the health of your deployments.

**Why use custom health checks?**

* **Control traffic and restarts** by configuring failure thresholds to suit your needs.
* **Define replica health with custom logic** (e.g. fail after a certain number of 500s or a specific CUDA error).

By default, health checks run every 10 seconds to verify that each replica of your deployment is running successfully and can receive requests. If a health check fails for an extended period, one or both of the following actions may occur:

* Traffic is immediately stopped from reaching the failing replica.
* The failing replica is restarted.

The thresholds for each of these actions are configurable.

**Understanding readiness vs. liveness**: Baseten uses two types of Kubernetes health probes. The **readiness probe** determines when to stop traffic (controlled by `stop_traffic_threshold_seconds`), while the **liveness probe** determines when to restart the container (controlled by `restart_threshold_seconds`). Both probes check the same health endpoint, but serve different purposes: readiness controls traffic routing, while liveness controls container lifecycle.

Custom health checks can be implemented in two ways:

1. [**Configuring thresholds**](#configuring-health-checks) for when health check failures should stop traffic to or restart a replica.
2. [**Writing custom health check logic**](#writing-custom-health-checks) to define how replica health is determined.

## Configuring health checks

### Parameters

You can customize the behavior of health checks on your deployments by setting the following parameters:

<ParamField body="stop_traffic_threshold_seconds" type="integer" default={1800}>
  The duration that health checks must continuously fail before traffic to the failing replica is stopped.

  `stop_traffic_threshold_seconds` must be between `30` and `1800` seconds, inclusive.
</ParamField>

<ParamField body="restart_check_delay_seconds" type="integer" default={0}>
  How long to wait before running health checks.

  `restart_check_delay_seconds` must be between `0` and `1800` seconds, inclusive.
</ParamField>

<ParamField body="restart_threshold_seconds" type="integer" default={1800}>
  The duration that health checks must continuously fail before triggering a restart of the failing replica.

  `restart_threshold_seconds` must be between `30` and `1800` seconds, inclusive.

  <Note> The combined value of `restart_check_delay_seconds` and `restart_threshold_seconds` must not exceed `1800` seconds. </Note>
</ParamField>

### Model and custom server deployments

Configure health checks in your `config.yaml`.

```yaml config.yaml theme={"system"}
runtime:
  health_checks:
    restart_check_delay_seconds: 60 # Waits 60 seconds after deployment before starting health checks
    restart_threshold_seconds: 300 # Triggers a restart if health checks fail for 5 minutes
    stop_traffic_threshold_seconds: 600 # Stops traffic if health checks fail for 10 minutes
```

You can also specify custom health check endpoints for custom servers. [See here](/development/model/custom-server#1-configuring-a-custom-server-in-config-yaml) for more details.

### Chains

Use `remote_config` to configure health checks for your chainlet classes.

```python chain.py theme={"system"}
class CustomHealthChecks(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        options=chains.ChainletOptions(
            health_checks=truss_config.HealthChecks(
                restart_check_delay_seconds=30,     # Waits 30 seconds before starting health checks
                restart_threshold_seconds=120,      # Restart replicas after 2 minutes of failure
                stop_traffic_threshold_seconds=300, # Stop traffic after 5 minutes of failure
            )
        )
    )
```

## Writing custom health checks

You can write custom health checks in both **model deployments** and **chain deployments**.

<Info>
  {" "}

  Custom health checks are currently not supported in development deployments.{" "}
</Info>

{" "}

### Custom health checks in models

```python model.py theme={"system"}
class Model:
    def is_healthy(self) -> bool:
        # Add custom health check logic for your model here
		pass
```

### Custom health checks in chains

Health checks can be customized for each chainlet in your chain.

```python chain.py theme={"system"}
@chains.mark_entrypoint
class CustomHealthChecks(chains.ChainletBase):
    def is_healthy(self) -> bool:
        # Add custom health check logic for your chainlet here
        pass
```

## Health checks in action

### Identifying 5xx errors

You might create a custom health check to identify 5xx errors like the following:

```python model.py theme={"system"}
class Model:
    def __init__(self):
        ...
        self._is_healthy = True

    def load(self):
        # Perform load
        # Your custom health check won't run until after load completes
        ...

    def is_healthy(self):
        return self._is_healthy

    def predict(self, input):
        try:
            # Perform inference
            ...
        except Some5xxError:
            self._is_healthy = False
            raise
```

Custom health check failures are indicated by the following log:

```md Example health check failure log line theme={"system"}
Jan 27 10:36:03pm md2pg Health check failed.
```

Deployment restarts due to health check failures are indicated by the following log:

```md Example restart log line theme={"system"}
Jan 27 12:02:47pm zgbmb Model terminated unexpectedly. Exit code: 0, reason: Completed, restart count: 1
```

## FAQs

### Is there a rule of thumb for configuring thresholds for stopping traffic and restarting?

It depends on your health check implementation. If your health check relies on conditions that only change during inference (e.g., `_is_healthy` is set in `predict`), restarting before stopping traffic is generally better, as it allows recovery without disrupting traffic.

Stopping traffic first may be preferable if a failing replica is actively degrading performance or causing inference errors, as it prevents the failing replica from affecting the overall deployment while allowing time for debugging or recovery.

### When should I configure `restart_check_delay_seconds`?

Configure `restart_check_delay_seconds` to allow replicas sufficient time to initialize after deployment or a restart. This delay helps reduce unnecessary restarts, particularly for services with longer startup times.

### Why am I seeing two health check failure logs in my logs?

These refer to two separate health checks we run every 10 seconds:

* One to determine when to stop traffic to a replica.
* The other to determine when to restart a replica.

### Does stopped traffic or replica restarts affect autoscaling?

Yes, both can impact autoscaling. If traffic stops or replicas restart, the remaining replicas handle more load. If the load exceeds the concurrency target during the autoscaling window, additional replicas are spun up. Similarly, when traffic stabilizes, excess replicas are scaled down after the scale down delay. [See here](/deployment/autoscaling#autoscaling-behavior) for more details on autoscaling.

### How does billing get affected?

You are billed for the uptime of your deployment. This includes the time a replica is running, even if it is failing health checks, until it scales down.

### Will failing health checks cause my deployment to stay up forever?

No. If your deployment is configured with a scale down delay and the minimum number of replicas is set to 0, the replicas will scale down once the model is no longer receiving traffic for the duration of the scale down delay. This applies even if the replicas are failing health checks. [See here](/deployment/autoscaling#scale-to-zero) for more details on autoscaling.

### What happens when my deployment is loading?

When your deployment is loading, your custom health check will not be running. Once `load()` is completed, we'll start using your custom `is_healthy()` health check.


# Deploy Custom servers from Docker Images
Source: https://docs.baseten.co/development/model/custom-server

A config.yaml is all you need

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


# Data and storage
Source: https://docs.baseten.co/development/model/data-directory

Load model weights without Hugging Face or S3

Model files, such as weights, can be **large** (often **multiple GBs**). Truss supports **multiple ways** to load them efficiently:

* **Public Hugging Face models** (default)
* **Bundled directly in Truss**

### 1. Bundling model weights in Truss

Store model files **inside Truss** using the `data/` directory.

**Example: Stable Diffusion 2.1 Truss structure**

```pssql  theme={"system"}
data/
    scheduler/
        scheduler_config.json
    text_encoder/
        config.json
        diffusion_pytorch_model.bin
    tokenizer/
        merges.txt
        tokenizer_config.json
        vocab.json
    unet/
        config.json
        diffusion_pytorch_model.bin
    vae/
        config.json
        diffusion_pytorch_model.bin
    model_index.json
```

**Access bundled files in `model.py`:**

```python  theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self._data_dir = kwargs["data_dir"]

    def load(self):
        self.model = StableDiffusionPipeline.from_pretrained(
            str(self._data_dir),
            revision="fp16",
            torch_dtype=torch.float16,
        ).to("cuda")
```

<Warning>
  Limitation: Large weights increase deployment size, making it slower. Consider
  cloud storage instead.
</Warning>

## 2. Loading private model weights from S3

If using **private S3 storage**, first **configure secure authentication**.

### Step 1: Define AWS secrets in `config.yaml`

```yaml  theme={"system"}
secrets:
  aws_access_key_id: null
  aws_secret_access_key: null
  aws_region: null # e.g., us-east-1
  aws_bucket: null
```

<Warning>
  Do not store actual credentials here. Add them securely to [Baseten secrets
  manager](https://app.baseten.co/settings/secrets).
</Warning>

### Step 2: Authenticate with AWS in `model.py`

```python  theme={"system"}
import boto3

def __init__(self, **kwargs):
    self._config = kwargs.get("config")
    secrets = kwargs.get("secrets")
    self.s3_client = boto3.client(
        "s3",
        aws_access_key_id=secrets["aws_access_key_id"],
        aws_secret_access_key=secrets["aws_secret_access_key"],
        region_name=secrets["aws_region"],
    )
    self.s3_bucket = secrets["aws_bucket"]
```

### Step 3: Deploy

```sh  theme={"system"}
truss push
```


# Deploy and iterate
Source: https://docs.baseten.co/development/model/deploy-and-iterate

Deploy your model and quickly iterate on it.

In [Your First Model](/development/model/build-your-first-model), we walked through
how to deploy a basic model to Baseten. If you are trying to rapidly make changes
and iterate on your model, you'll notice that there is quite a bit of time between
running `truss push` and when the changes are reflected on Baseten.

Also, a lot of models require special hardware that you may not immediately have
access to.

To solve this problem, we have a feature called **Truss Watch**, that allows you to
live reload your model as you work.

# Truss Watch

To make use of `truss watch`, start by deploying your model:

```bash  theme={"system"}
$ truss push
```

By default, this will deploy a "development" version of your model. This means that the model
has a live reload server attached to it and supports hot reloading. To get the hot reload
loop working, simply run `truss watch` afterwards:

```bash  theme={"system"}
$ truss watch
```

Now, if you make changes to your model, you'll see them reflected in the model logs!

You can now happily iterate on your model without having to go through the entire
build & deploy loop between each change.

# Ready for Production?

Once you've iterated on your model, and you're ready to deploy it to production,
you can use the `truss push --publish` command. This will deploy a "published"
version of your model

```bash  theme={"system"}
truss push --publish
```

Note that development models have slightly worse performance, and have more
limited scaling properites, so it's highly recommend to not use these for
any production use-case.


# Access model environments
Source: https://docs.baseten.co/development/model/environments

A guide to leveraging environments in your models

Model environments help configure behavior based on **deployment stage** (e.g., production vs. staging). You can access the environment details via `kwargs` in the `Model` class.

## 1. Retrieve Environment Variables

Access the environment in `__init__`:

```python  theme={"system"}
def __init__(self, **kwargs):
    self._environment = kwargs["environment"]
```

## 2. Configure Behavior Based on Environment

Use environment variables in the `load` function:

```python  theme={"system"}
def load(self):
    if self._environment.get("name") == "production":
        # Production setup
        self.setup_sentry()
        self.setup_logging(level="INFO")
        self.load_production_weights()
    else:
        # Default setup for staging or development deployments
        self.setup_logging(level="DEBUG")
        self.load_default_weights()
```

**Why use this?**

* **Customize logging levels**
* **Load environment-specific model weights**
* **Enable monitoring tools (e.g., Sentry)**


# gRPC 🆕
Source: https://docs.baseten.co/development/model/grpc

Invoke your model over gRPC.

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


# Implementation
Source: https://docs.baseten.co/development/model/implementation

How to implement your model.

In this section, we'll cover how to implement the actual logic for your model.

As was mentioned in [Your First Model](/development/model/build-your-first-model), the
logic for the model itself is specified in a `model/model.py` file. To recap, the simplest
directory structure for a model is:

```
model/
  model.py
config.yaml
```

It's expected that the `model.py` file contains a class with particular methods:

```python model.py theme={"system"}
class Model:
  def __init__(self):
    pass

  def load(self):
    pass

  def predict(self, input_data):
    pass
```

* The `__init__` method is used to initialize the `Model` class, and allows you to read
  in configuration parameters and other information.
* The `load` method is where you define the logic for initializing the model. This might
  include downloading model weights, or loading them onto a GPU.
* The `predict` method is where you define the logic for inference.

In the next sections, we'll cover each of these methods in more detail.

## **init**

As mentioned above, the `__init__` method is used to initialize the `Model` class, and allows you to
read in configuration parameters and runtime information.

The simplest signature for `__init__` is:

```python model.py theme={"system"}
def __init__(self):
  pass
```

If you need more information, however, you have the option to define your **init** method
such that it accepts the following parameters:

```python model.py theme={"system"}
def __init__(self, config: dict, data_dir: str, secrets: dict, environment: str):
  pass
```

* `config`: A dictionary containing the config.yaml for the model.
* `data_dir`: A string containing the path to the data directory for the model.
* `secrets`: A dictionary containing the secrets for the model. Note that at runtime,
  these will be populated with the actual values as stored on Baseten.
* `environment`: A string containing the environment for the model, if the model has been
  deployed to an environment.

You can then make use of these parameters in the rest of your model but saving these as
attributes:

```python model.py theme={"system"}
def __init__(self, config: dict, data_dir: str, secrets: dict, environment: str):
  self._config = config
  self._data_dir = data_dir
  self._secrets = secrets
  self._environment = environment
```

## load

The `load` method is where you define the logic for initializing the model. As
mentioned before, this might include downloading model weights or loading them
onto the GPU.

`load`, unlike the other method mentioned, does not accept any parameters:

```python model.py theme={"system"}
def load(self):
  pass
```

After deploying your model, the deployment will not be considered "Ready" until `load` has
completed successfully. Note that there is a **timeout of 30 minutes** for this, after which,
if `load` has not completed, the deployment will be marked as failed.

## predict

The `predict` method is where you define the logic for performing inference.

The simplest signature for `predict` is:

```python model.py theme={"system"}
def predict(self, input_data) -> str:
  return "Hello"
```

The return type of `predict` must be JSON-serializable, so it can be:

* `dict`
* `list`
* `str`

If you would like to return a more strictly typed object, you can return a
`Pydantic` object.

```python model.py theme={"system"}
from pydantic import BaseModel

class Result(BaseModel):
  value: str
```

You can then return an instance of this model from `predict`:

```python model.py theme={"system"}
def predict(self, input_data) -> Prediction:
  return Result(value="Hello")
```

### Streaming

In addition to supporting a single request/response cycle, Truss also supports streaming.

See the [Streaming](/development/model/streaming) guide for more information.

### Async vs. Sync

Note that the `predict` method is synchronous by default. However, if your model inference
depends on APIs require `asyncio`, `predict` can also be written as a coroutine.

```python model.py theme={"system"}
import asyncio

async def predict(self, input_data) -> dict:
    # Async logic here

    await asyncio.sleep(1)
    return {"value": "Hello"}
```

<Warning>
  If you are using `asyncio` in your `predict` method, be sure not to perform any blocking
  operations, such as a synchronous file download. This can result in degraded performance.
</Warning>


# Cached weights 🆕
Source: https://docs.baseten.co/development/model/model-cache

Accelerate cold starts and availability by prefetching and caching your weights.

<Tip>
  ### What is a "cold start"?

  "Cold start" is a term used to describe the time taken when a request is received when the model is scaled to 0 until it is ready to handle the first request. This process is a critical factor in allowing your deployments to be responsive to traffic while maintaining your SLAs and lowering your costs.
  To optimize cold starts, we will go over the following stategies: Downloading them in a background thread in Rust that runs during the module import, caching weights in a distributed filesystem, and moving weights into the docker image.

  In practice, this reduces the cold start for large models to just a few seconds. For example, Stable Diffusion XL can take a few minutes to boot up without caching. With caching, it takes just under 10 seconds.
</Tip>

## Enabling Caching + Prefetching for a Model

To enable caching, simply add `model_cache` to your `config.yaml` with a valid `repo_id`. The `model_cache` has a few key configurations:

* `repo_id` (required): The repo name from Hugging Face or bucket/container from GCS, S3, or Azure.
* `revision` (required for Hugging Face): The revision of the huggingface repo, such as the sha or branch name such as `refs/pr/1` or `main`. Not needed for GCS, S3, or Azure.
* `use_volume`: Boolean flag to determine if the weights are downloaded to the Baseten Distributed Filesystem at runtime (recommended) or bundled into the container image (legacy, not recommended).
* `volume_folder`: string, folder name under which the model weights appear. Setting it to `my-llama-model` will mount the repo to `/app/model_cache/my-llama-model` at runtime.
* `allow_patterns`: Only cache files that match specified patterns. Utilize Unix shell-style wildcards to denote these patterns.
* `ignore_patterns`: Conversely, you can also denote file patterns to ignore, hence streamlining the caching process.
* `runtime_secret_name`: The name of your secret containing the credentials for a private repository or bucket, such as a `hf_access_token` or `gcs_service_account`.
* `kind`: The storage provider type for the model weights.
  * `"hf"` (default): Hugging Face
  * `"gcs"`: Google Cloud Storage
  * `"s3"`: AWS S3
  * `"azure"`: Azure Blob Storage

Here is an example of a well written `model_cache` for Stable Diffusion XL. Note how it only pulls the model weights that it needs using `allow_patterns`.

```yaml config.yaml theme={"system"}
model_cache:
  - repo_id: madebyollin/sdxl-vae-fp16-fix
    revision: 207b116dae70ace3637169f1ddd2434b91b3a8cd
    use_volume: true
    volume_folder: sdxl-vae-fp16
    allow_patterns:
      - config.json
      - diffusion_pytorch_model.safetensors
  - repo_id: stabilityai/stable-diffusion-xl-base-1.0
    revision: 462165984030d82259a11f4367a4eed129e94a7b
    use_volume: true
    volume_folder: stable-diffusion-xl-base
    allow_patterns:
      - "*.json"
      - "*.fp16.safetensors"
      - sd_xl_base_1.0.safetensors
  - repo_id: stabilityai/stable-diffusion-xl-refiner-1.0
    revision: 5d4cfe854c9a9a87939ff3653551c2b3c99a4356
    use_volume: true
    volume_folder: stable-diffusion-xl-refiner
    allow_patterns:
      - "*.json"
      - "*.fp16.safetensors"
      - sd_xl_refiner_1.0.safetensors
```

Many Hugging Face repos have model weights in different formats (`.bin`, `.safetensors`, `.h5`, `.msgpack`, etc.). You only need one of these most of the time. To minimize cold starts, ensure that you only cache the weights you need.

<Tip>
  ### What is weight "pre-fetching"?

  With `model_cache`, weights are pre-fetched by downloading your weights ahead of time in a dedicated Rust thread.
  This means, you can perform all kinds of preparation work (importing libraries, jit compilation of torch/triton modules), until you need access to the files.
  In practice, executing statements like `import tensorrt_llm` typically take 10–15 seconds. By that point, the first 5–10GB of the weights will have already been downloaded.
</Tip>

To use the `model_cache` config with truss,  we require you to actively interact with the `lazy_data_resolver`.
Before using any of the downloaded files, you must call the `lazy_data_resolver.block_until_download_complete()`. This will block until all files in the `/app/model_cache` directory are downloaded & ready to use.
This call must be either part of your `__init__` or `load` implementation.

```python model.py theme={"system"}
# <- download is invoked before here.
import torch # this line usually takes 2-5 seconds.
import tensorrt_llm # this line usually takes 10-15 seconds
import onnxruntime # this line usually takes 5-10 seconds

class Model:
    """example usage of `model_cache` in truss"""
    def __init__(self, *args, **kwargs):
        # `lazy_data_resolver` is passed as keyword-argument in init
        self._lazy_data_resolver = kwargs["lazy_data_resolver"]

    def load(self):
        # work that does not require the download may be done beforehand
        random_vector = torch.randn(1000)
        # important to collect the download before using any incomplete data
        self._lazy_data_resolver.block_until_download_complete()
        # after the call, you may use the /app/model_cache directory and the contents
        torch.load(
            "/app/model_cache/stable-diffusion-xl-base/model.fp16.safetensors"
        )
```

## Private Repositories/Cloud Storage

### Private Hugging Face repositories 🤗

For any public Hugging Face repo, you don't need to do anything else. Adding the `model_cache` key with an appropriate `repo_id` should be enough.

However, if you want to deploy a model from a gated repo like [Llama 2](https://huggingface.co/meta-llama/Llama-2-70b-chat-hf) to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get Hugging Face API Key">
    [Grab an API key](https://huggingface.co/settings/tokens) from Hugging Face with `read` access. Make sure you have access to the model you want to serve.
  </Step>

  <Step title="Add it to Baseten Secrets Manager">
    Paste your API key in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, such as `hf_access_token`. You can read more about secrets [here](/development/model/secrets).
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, add the secret key under `runtime_secret_name`:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: your-org/your-private-repo
      runtime_secret_name: hf_access_token
    ```
  </Step>
</Steps>

If you run into any issues, run through all the steps above again and make sure you did not misspell the name of the repo or secret name, or paste an incorrect API key.

### Private GCS Buckets

If you want to deploy a model from a private GCS bucket to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get GCS Service Account Key">
    Create a [service account key](https://cloud.google.com/iam/docs/keys-create-delete#creating) in your GCS account for the project which contains the model weights.
  </Step>

  <Step title="Add it to Baseten Secrets Manager">
    Paste the contents of the `service_account.json` in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, e.g. `gcs_service_account`. You can read more about secrets [here](/development/model/secrets).

    At a minimum, you should have these credentials:

    ```json gcs_service_account theme={"system"}
      {
        "private_key_id": "xxxxxxx",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMI",
        "client_email": "b10-some@xxx-example.iam.gserviceaccount.com"
      }
    ```
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, make sure to add the `runtime_secret_name` to your `model_cache` matching the above secret name:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: gs://your-private-bucket
      use_volume: true
      volume_folder: your-model-weights
      runtime_secret_name: gcs_service_account
      kind: "gcs"
    ```
  </Step>
</Steps>

It's easy to make a mistake in any of these steps. If you run into issues, you're encouraged to go through the steps again just in case. Please contact [Baseten support](mailto:support@baseten.co) if you continue to experience issues.

### Private S3 Buckets

If you want to deploy a model from a private S3 bucket to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get S3 credentials">
    [Get the your `access_key_id` and `secret_access_key`](https://aws.amazon.com/blogs/security/how-to-find-update-access-keys-password-mfa-aws-management-console/) in your AWS account for the bucket that contains the model weights.
  </Step>

  <Step title="Add them to Baseten Secrets Manager">
    Paste the following `json` in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, e.g. `aws_secret_json`. You can read more about secrets [here](/development/model/secrets).

    ```json aws_secret_json theme={"system"}
      {
        "access_key_id": "XXXXX",
        "secret_access_key": "xxxxx/xxxxxx",
        "region": "us-west-2"
      }
    ```
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, make sure to add the `runtime_secret_name` to your `model_cache` matching the above secret name:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: s3://your-private-bucket
      use_volume: true
      volume_folder: your-model-weights
      runtime_secret_name: aws_secret_json
      kind: "s3"
    ```
  </Step>
</Steps>

It's easy to make a mistake in any of these steps. If you run into issues, you're encouraged to go through the steps again just in case. Please contact [Baseten support](mailto:support@baseten.co) if you continue to experience issues.

### Private Azure Containers

If you want to deploy a model from a private Azure container to Baseten, there are a few steps you need to take:

<Steps>
  <Step title="Get Azure credentials">
    [Get the your `account_key`](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-get-info?tabs=portal#get-a-connection-string-for-the-storage-account) in your Azure account with the container that has the model weights.
  </Step>

  <Step title="Add them to Baseten Secrets Manager">
    Paste the following `json` in your [secrets manager in Baseten](https://app.baseten.co/settings/secrets) under the specified key, e.g. `azure_secret_json`. You can read more about secrets [here](/development/model/secrets).

    ```json azure_secret_json theme={"system"}
      {
          "account_key": "xxxxx",
      }
    ```
  </Step>

  <Step title="Update Config">
    In your Truss's `config.yaml`, make sure to add the `runtime_secret_name` to your `model_cache` matching the above secret name:

    ```yaml config.yaml theme={"system"}
    model_cache:
    - repo_id: az://your-private-container
      use_volume: true
      volume_folder: your-model-weights
      runtime_secret_name: azure_secret_json
      kind: "azure"
    ```
  </Step>
</Steps>

It's easy to make a mistake in any of these steps. If you run into issues, you're encouraged to go through the steps again just in case. Please contact [Baseten support](mailto:support@baseten.co) if you continue to experience issues.

## `model_cache` within Chains

To use `model_cache` for [chains](/development/chain/getting-started) - use the `Assets` specifier. In the example below, we will download `llama-3.2-1B`.
As this model is a gated huggingface model, we are setting the mounting token as part of the assets `chains.Assets(..., secret_keys=["hf_access_token"])`.
The model is quite small - in many cases, we will be able to download the model while `from transformers import pipeline` and `import torch` are running.

```python chain_cache.py theme={"system"}
import random
import truss_chains as chains

try:
    # imports on global level for PoemGeneratorLM, to save time during the download.
    from transformers import pipeline
    import torch
except ImportError:
    # RandInt does not have these dependencies.
    pass

class RandInt(chains.ChainletBase):
    async def run_remote(self, max_value: int) -> int:
        return random.randint(1, max_value)

@chains.mark_entrypoint
class PoemGeneratorLM(chains.ChainletBase):
    from truss import truss_config
    LLAMA_CACHE = truss_config.ModelRepo(
        repo_id="meta-llama/Llama-3.2-1B-Instruct",
        revision="c4219cc9e642e492fd0219283fa3c674804bb8ed",
        use_volume=True,
        volume_folder="llama_mini",
        ignore_patterns=["*.pth", "*.onnx"]
    )
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            # The phi model needs some extra python packages.
            pip_requirements=[
                "transformers==4.48.0",
                "torch==2.6.0",
            ]
        ),
        compute=chains.Compute(
            gpu="L4"
        ),
        # The phi model needs a GPU and more CPUs.
        # compute=chains.Compute(cpu_count=2, gpu="T4"),
        # Cache the model weights in the image
        assets=chains.Assets(cached=[LLAMA_CACHE], secret_keys=["hf_access_token"]),
    )
    # <- Download happens before __init__ is called.
    def __init__(self, rand_int=chains.depends(RandInt, retries=3)) -> None:
        self._rand_int = rand_int
        print("loading cached llama_mini model")
        self.pipeline = pipeline(
            "text-generation",
            model=f"/app/model_cache/llama_mini",
        )

    async def run_remote(self, max_value: int = 3) -> str:
        num_repetitions = await self._rand_int.run_remote(max_value)
        print("writing poem with num_repetitions", num_repetitions)
        poem = str(self.pipeline(
            text_inputs="Write a beautiful and descriptive poem about the ocean. Focus on its vastness, movement, and colors.",
            max_new_tokens=150,
            do_sample=True,
            return_full_text=False,
            temperature=0.7,
            top_p=0.9,
        )[0]['generated_text'])
        return poem * num_repetitions
```

## `model_cache` for custom servers

If you are not using Python's `model.py` and [custom servers](/development/model/custom-server) such as [vllm](/examples/vllm), TEI or [sglang](/examples/sglang),
you are required to use the `truss-transfer-cli` command, to force population of the `/app/model_cache` location. The command will block until the weights are downloaded.

Here is an example for how to use text-embeddings-inference on a L4 to populate a jina embeddings model from huggingface into the model\_cache.

```yaml config.yaml theme={"system"}
base_image:
  image: baseten/text-embeddings-inference-mirror:89-1.6
docker_server:
  liveness_endpoint: /health
  predict_endpoint: /v1/embeddings
  readiness_endpoint: /health
  server_port: 7997
  # using `truss-transfer-cli` to download the weights to `cached_model`
  start_command: bash -c "truss-transfer-cli && text-embeddings-router --port 7997
    --model-id /app/model_cache/my_jina --max-client-batch-size 128 --max-concurrent-requests
    128 --max-batch-tokens 16384 --auto-truncate"
model_cache:
- repo_id: jinaai/jina-embeddings-v2-base-code
  revision: 516f4baf13dec4ddddda8631e019b5737c8bc250
  use_volume: true
  volume_folder: my_jina
  ignore_patterns: ["*.onnx"]
model_metadata:
  example_model_input:
    encoding_format: float
    input: text string
    model: model
model_name: TEI-jinaai-jina-embeddings-v2-base-code-truss-example
resources:
  accelerator: L4
```

## Optimizing cache hits and access time futher with b10cache enabled

<Warning>
  Requires `use_volume: true` and [b10cache](/development/model/b10cache) enabled. Without b10cache enabled, scaling the model with download the weights again.
</Warning>

To further reduce weights loading time, we can enable Baseten's Distributed Filesystem (b10cache) for your account.
You can validate that this is enabled for your account by viewing the logs of your deployment.

```
[2025-09-10 01:04:35] [INFO ] b10cache is enabled.
[2025-09-10 01:04:35] [INFO ] Symlink created successfully. Skipping download for /app/model_cache/cached_model/model.safetensors
```

<Tip>
  Once b10cache is active, we will skip downloads that are cached in the distributed filesystem of the region your deployment is running in.
  b10cache acts like a content delivery network: Initial cache misses are populating the filesystem, unused files are garbage collected 4 days after their last usage.
  Once b10cache is active, it will pull from the fastest source. If another pod is active on the same physical node, artifacts may be hot-cached, and shared among your deployments.
  Downloads are fully isolated from other organizations. Modifying downloaded artifacts inplace / without copy is not recommended.
</Tip>

If b10cache is not available for your account, we will provision the model\_cache with a optimized download from HuggingFace.co.
The download is parallellized, achieving typical download speeds of greater than 1GB/s on a 10Gbit ethernet connection.
If you want to enable b10cache, feel free to reach out to our support.


# Developing a Model on Baseten
Source: https://docs.baseten.co/development/model/overview

This page introduces the key concepts and workflow you'll use to package, configure, and iterate on models using Baseten’s developer tooling.

Baseten makes it easy to go from a trained machine learning model to a fully-deployed, production-ready API. You’ll use Truss—our open-source model packaging tool—to containerize your model code and configuration, and ship it to Baseten for deployment, testing, and scaling.

## What does it mean to develop a model?

In Baseten, developing a model means:

1. [Packaging your model code and weights](/development/model/implementation):
   Wrap your trained model into a structured project that includes your inference logic and dependencies.

2. [Configuring the model environment](/development/model/configuration):
   Define everything needed to run your model—from Python packages to system dependencies and secrets.

3. [Deploying and iterating quickly](/development/model/deploy-and-iterate):
   Push your model to Baseten in development mode and make live edits with instant feedback.

Once your model works the way you want, you can promote it to [production](/deployment/environments), ready for live traffic.

## Development flow on Baseten

Here’s what the typical model development loop looks like:

1. **Initialize a new model project** using the Truss CLI.

2. **Add your model logic** to a Python class (model.py), specifying how to load and run inference.

3. **Configure dependencies** in a YAML or Python config.

4. **Deploy the model** in development mode using truss push.

5. **Iterate fast** with truss watch—live-reload your dev deployment as you make changes.

6. **Test and tune** the model until it’s production-ready.

7. **Promote the model** to production when you’re ready to scale.

<Frame>
  <img src="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/user-workflow.png?fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=df89988292282d68e9935d114b51aaa0" data-og-width="3044" width="3044" data-og-height="724" height="724" data-path="images/user-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/user-workflow.png?w=280&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=a395805a347b57629d3afc9eb56493a0 280w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/user-workflow.png?w=560&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=c29be1657bb6d62a36b21f13a7dfe13f 560w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/user-workflow.png?w=840&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=1d622675190444d25854dc3287d1e171 840w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/user-workflow.png?w=1100&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=95642ffbb4a3e28aca22198536b7b7e1 1100w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/user-workflow.png?w=1650&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=67c2cce9acec4e04b09375b2569507e3 1650w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/user-workflow.png?w=2500&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=a987524997f71289cda701fe9a8566ec 2500w" />
</Frame>

<Note>
  **Note:** Truss runs your model in a standardized container without needing
  Docker installed locally. It also gives you a fast developer loop and a
  consistent way to configure and serve models.
</Note>

## What is Truss?

Truss is the tool you use to:

* **Scaffold a new model project**
* **Serve models locally or in the cloud**
* **Package your code, config, and model files**
* **Push to Baseten for deployment**

You can think of it as the developer toolkit for building and managing model servers—built specifically for machine learning workflows.

With Truss, you can create a containerized model server **without needing to learn Docker**, and define everything about how your model runs: Python and system packages, GPU settings, environment variables, and custom inference logic. It gives you a fast, reproducible dev loop—test changes locally or in a remote environment that mirrors production.

Truss is **flexible enough to support a wide range of ML stacks**, including:

* Model frameworks like **PyTorch**, **transformers**, and **diffusers**
* [Inference engines](development/model/performance/concepts) like **TensorRT-LLM**, **SGLang**, **vLLM**
* Serving technologies like **Triton**
* Any package installable with `pip` or `apt`

We'll use Truss throughout this guide, but the focus will stay on **how you develop models**, not just how Truss works.

## From model to server: the key components

When you develop a model on Baseten, you define:

* A `Model` **class**: This is where your model is loaded, preprocessed, run, and the results returned.
* A **configuration file** (`config.yaml` or Python config): Defines the runtime environment, dependencies, and deployment settings.
* Optional **extra assets**, like model weights, secrets, or external packages.

These components together form a **Truss**, which is what you deploy to Baseten.

Truss simplifies and standardizes model packaging for seamless deployment. It encapsulates model code, dependencies, and configurations into a **portable, reproducible structure**, enabling efficient development, scaling, and optimization.

## Development vs. other deployments

The only special deployment is **development**.

* **Development deployment**
  Meant for iteration and testing. It supports [live-reloading](/development/model/deploy-and-iterate#truss-watch) for quick feedback loops and will only scale to **one replica**, no autoscaling.
* **All others deployments**
  Stable, autoscaled, and ready for live traffic but **don't support live-reloading**.

You’ll use the dev deployment to build and test, then promote it to an environment like **staging** or **production** once you're satisfied.


# Concepts
Source: https://docs.baseten.co/development/model/performance/concepts

Improve your latency and throughput

Model performance means optimizing every layer of your model serving infrastructure to balance four goals:

1. **Latency**: on a per-request basis, how quickly does each user get output from the model?
2. **Throughput**: how many requests or users can the deployment handle at once?
3. **Cost**: how much does a standardized unit of work (e.g. 1M tokens from an LLM) cost?
4. **Quality**: does your model consistently deliver high-quality output after optimization?

## Model performance tooling

<Card title="TensorRT-LLM Engine Builder" icon="train-tram" iconType="duotone" href="/development/model/performance/engine-builder-overview">
  Baseten's TensorRT-LLM engine builder simplifies and automates the process of
  using TensorRT-LLM for development and production.
</Card>

## Full-stack model performance

### Model and GPU selection

Two of the highest-impact choices for model performance come before the optimization process: picking the best model size and implementation and picking the right GPU to run it on.

<AccordionGroup>
  <Accordion title="Model selection" icon="robot-astromech">
    *Tradeoff: Latency/Throughput/Cost vs Quality*

    The biggest factor in your latency, throughput, cost, and quality is what model you use. Before you jump into optimizing a foundation model, consider:

    * Can you use a smaller size, like Llama 8B instead of 70B? Can you fine-tune the smaller model for your use case?
    * Can you use a different model, like [SDXL Lightning](https://www.baseten.co/library/sdxl-lightning/) instead of SDXL?
    * Can you use a different implementation, like [Faster Whisper](https://github.com/basetenlabs/truss-examples/tree/main/whisper/faster-whisper-v3) instead of Whisper?

    Usually, model selection is bound by quality. For example SDXL Lightning makes images incredibly quickly, but they may not be detailed enough for your use case.

    Experiment with alternative models to see if they can reset your performance expectations while meeting your quality bar.
  </Accordion>

  <Accordion title="GPU selection" icon="server">
    *Tradeoff: Latency/Throughput vs Cost*

    The minimum requirement for a GPU instance is that it must have enough VRAM to load model weights with headroom left for inference.

    It often makes sense to use a more powerful (but more expensive) GPU than the minimum requirement, especially if you have ambitious latency goals and/or high utilization.

    For example, you might choose:

    * (Multiple) H100 GPUs for [deployments optimized with TensorRT/TensorRT-LLM](https://www.baseten.co/blog/unlocking-the-full-power-of-nvidia-h100-gpus-for-ml-inference-with-tensorrt/)
    * H100 MIGs for [high-throughput deployments of smaller models like Llama 3 8B and SDXL](https://www.baseten.co/blog/using-fractional-h100-gpus-for-efficient-model-serving/)
    * L4 GPUs for autoscaling Whisper deployments

    The [GPU instance reference](/deployment/resources#choosing-the-right-instance-type) lists all available options.
  </Accordion>
</AccordionGroup>

### GPU-level optimizations

Our first goal is to get the best possible performance out of a single GPU or GPU cluster.

<AccordionGroup>
  <Accordion title="Inference engine" icon="train-tram">
    *Benefit: Latency/Throughput/Cost*

    You can just use `transformers` and `pytorch` out of the box to serve your model. But best-in-class performance comes from using a dedicated inference engine, like:

    1. [TensorRT](https://developer.nvidia.com/tensorrt)/[TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM), maintained by NVIDIA
    2. [vLLM](https://github.com/vllm-project/vllm), an independent open source project
    3. [TGI](https://github.com/huggingface/text-generation-inference), maintained by Hugging Face

    We [often recommend TensorRT/TensorRT-LLM](https://www.baseten.co/blog/high-performance-ml-inference-with-nvidia-tensorrt/) for best performance. The easiest way to get started with TensorRT-LLM is our [TRT-LLM engine builder](/development/model/performance/engine-builder-overview).
  </Accordion>

  <Accordion title="Inference server" icon="train-track">
    *Benefit: Latency/Throughput*

    In addition to an optimized inference engine, you need an inference server to handle requests and supply features like in-flight batching.

    Baseten runs a modified version of Triton for compatible model deployments. Other models use `TrussServer`, a capable general-purpose model inference server built into Truss.
  </Accordion>

  <Accordion title="Quantization" icon="minimize">
    *Tradeoff: Latency/Throughput/Cost vs Quality*

    By default, model inference happens in `fp16`, meaning that model weights and other values are represented as 16-bit floating-point numbers.

    Through a process called [post-training quantization](https://www.baseten.co/blog/fp8-efficient-model-inference-with-8-bit-floating-point-numbers/), you can instead run inference in a different format, like `fp8`, `int8`, or `int4`. This has massive benefits: more teraFLOPS at lower precision means lower latency, smaller numbers being retrieved from VRAM means higher throughput, and smaller model weights means saving on cost and potentially using fewer GPUs.

    However, quantization can affect output quality. Thoroughly review quantized model outputs by hand and with standard checks like perplexity to ensure that the output of the quantized model matches the original.

    We've had a lot of success with [fp8 for faster inference without quality loss](https://www.baseten.co/blog/33-faster-llm-inference-with-fp8-quantization/) and encourage experimenting with quantization, especially when using the TRT-LLM engine builder.
  </Accordion>

  <Accordion title="Model-level optimizations" icon="snake">
    *Tradeoff: Latency/Throughput/Cost vs Quality*

    There are a number of exciting cutting-edge techniques for model inference that can massively improve latency and/or throughput for a model. For example, LLMs can use Speculative Decoding or Medusa to generate multiple tokens per forward pass, improving TPS.

    When using a new technique to improve model performance, always run real-world benchmarks and carefully validate output quality to ensure the performance improvements aren't undermining the model's usefulness.
  </Accordion>

  <Accordion title="Batching (GPU concurrency)" icon="object-group">
    *Tradeoff: Latency vs Throughput/Cost*

    Batch size is how many requests are processed concurrently on the GPU. It is a direct tradeoff between latency and throughput:

    * Increase batch size to improve throughput and cost
    * Reduce batch size to improve latency
  </Accordion>
</AccordionGroup>

### Infrastructure-level optimizations

Once we squeeze as much TPS as possible out of the GPU, we scale that out horizontally with infrastructure optimization.

<AccordionGroup>
  <Accordion title="Autoscaling" icon="layer-group">
    *Tradeoff: Latency/Throughput vs Cost*

    If traffic to a deployment is high enough, even an optimized model server won't be able to keep up. By creating replicas, you keep latency consistent for all users.

    Learn more about [autoscaling model replicas](/deployment/autoscaling).
  </Accordion>

  <Accordion title="Replica-level concurrency" icon="object-ungroup">
    *Tradeoff: Latency vs Throughput/Cost*

    Replica-level concurrency sets the number of requests that can be sent to the model server at one time. This is different from the on-GPU concurrency as your model server may perform pre- and post-processing tasks on CPU.

    Replica-level concurrency should always be greater than or equal to on-device concurrency (batch size).
  </Accordion>

  <Accordion title="Network latency" icon="globe">
    *Tradeoff: Latency vs Cost*

    If your GPU is in us-east-1 and your customer is in Australia, it doesn't matter how much you've optimized TTFT — your real-world latency will be terrible.

    Region-specific deployments are available on a per-customer basis. Contact us at [support@baseten.co](mailto:support@baseten.co) to discuss your needs.
  </Accordion>
</AccordionGroup>

### Application-level optimizations

There are also application-level steps that you can take to make sure you're getting the most value from your optimized endpoint.

<AccordionGroup>
  <Accordion title="Good prompts" icon="lightbulb">
    *Benefits: Latency, Quality*

    Every token an LLM doesn't have to process or generate is a token that you don't have to wait for or pay for.

    Prompt engineering can be as simple as saying "be concise" or as complex as making sure your RAG system returns the minimum number of highly-relevant retrievals.
  </Accordion>

  <Accordion title="Consistent sequence shapes" icon="shapes">
    *Benefits: Latency, Throughput*

    When using TensorRT-LLM, make sure that your input and output sequences are a consistent length. The inference engine is built for a specific number of tokens, and going outside of those sequence shapes will hurt performance.
  </Accordion>

  <Accordion title="Chains for multi-step inference" icon="link">
    *Benefits: Latency, Cost*

    The only thing running on your GPU should be the AI model. Other tasks like retrievals, secondary models, and business logic should be deployed and scaled separately to avoid bottlenecks.

    Use [Chains](/development/chain/overview) for performant multi-step and multi-model inference.
  </Accordion>

  <Accordion title="Session reuse during inference" icon="terminal">
    *Benefit: Latency*

    Use sessions rather than individual requests to avoid unnecessary network latency. See [inference documentation](/inference/concepts) for details.
  </Accordion>
</AccordionGroup>


# Request concurrency
Source: https://docs.baseten.co/development/model/performance/concurrency

A guide to setting concurrency for your model

Configuring concurrency optimizes **model performance**, balancing **throughput** and **latency**.

In Baseten & Truss, concurrency is managed at **two levels**:

1. **Concurrency Target** – Limits the number of requests **sent** to a single replica.
2. **Predict Concurrency** – Limits how many requests the predict function handles **inside the model container**.

## 1. Concurrency Target

* **Set in the Baseten UI** – Defines how many requests a single replica can process at once.
* **Triggers autoscaling** – If all replicas hit the concurrency target, additional replicas spin up.

**Example:**

* **Concurrency Target = 2, Single Replica**
* **5 requests arrive** → 2 are processed immediately, **3 are queued**.
* If max replicas aren't reached, **autoscaling spins up a new replica**.

## 2. Predict Concurrency

* **Set in** `config.yaml` – Controls how many requests can be **processed by** predict simultaneously.
* **Protects GPU resources** – Prevents multiple requests from overloading the GPU.

### Configuring Predict Concurrency

```yaml config.yaml theme={"system"}
model_name: "My model with concurrency limits"
runtime:
  predict_concurrency: 2  # Default is 1
```

### How It Works Inside a Model Pod

1. **Requests arrive** → All begin preprocessing (e.g., downloading images from S3).
2. **Predict runs on GPU** → Limited by `predict_concurrency`.
3. **Postprocessing begins** → Can run while other requests are still in inference.

## When to Use Predict Concurrency

* ✅ **Protect GPU resources** – Prevent multiple requests from degrading performance.
* ✅ **Allow parallel preprocessing/postprocessing** – I/O tasks can continue even when inference is blocked.

<Warning>Ensure `Concurrency Target` is set high enough to send enough requests to the container.</Warning>


# Engine builder configuration
Source: https://docs.baseten.co/development/model/performance/engine-builder-config

Configure your TensorRT-LLM inference engine

This reference lists every configuration option for the TensorRT-LLM Engine Builder. These options are used in `config.yaml`, such as for this Llama 3.1 8B example:

```yaml config.yaml theme={"system"}
model_name: Llama 3.1 8B Engine
resources:
  accelerator: H100:1
secrets:
  hf_access_token: "set token in baseten workspace"
trt_llm:
  build:
    base_model: decoder
    checkpoint_repository:
      repo: meta-llama/Llama-3.1-8B-Instruct
      source: HF
```

## `trt_llm.build`

TRT-LLM engine build configuration. TensorRT-LLM attempts to build a highly optimized network based on input shapes representative of your workload.

### `base_model`

The base model architecture of your model checkpoint. Supported architectures include:

* `decoder` - for CausalLM such as `Llama/Mistral/Qwen3ForCausalLM`
* `encoder` - for `Bert/Roberta/LLamaForSequenceClassification`, sentence-transformer models, embedding models

### `checkpoint_repository`

Specification of the model checkpoint to be leveraged for engine building. E.g.

```yaml  theme={"system"}
checkpoint_repository:
  source: HF | GCS | REMOTE_URL
  repo: meta-llama/Llama-3.1-8B-Instruct | gs://bucket_name | https://your-checkpoint.com/model.tar.gz
  revision: main  # Optional, only applicable to HF models
```

To configure access to private model checkpoints, [register secrets in your Baseten workspace](/observability/secrets#best-practices-for-secrets), namely the `hf_access_token` or `trt_llm_gcs_service_account` secrets with a valid service account json for HuggingFace or GCS, respectively.

#### `checkpoint_repository.source`

Source where the checkpoint is stored. This should contain assets as if using git clone with lfs for a Hugging Face repository.
This includes the tokenizer files, remote code and safetensor files and any json file related to configuration.
For GCS/REMOTE\_URL, we require the files to be organized in the same folder structured to a huggingface transformers repository.
Supported sources include:

* `HF` (HuggingFace)
* `GCS` (Google Cloud Storage)
* `REMOTE_URL` A tarball containing your checkpoint. **Important**: the archive must unpack with all required files (e.g., `config.json`) at the root level. For example, `config.json` should be directly in the tarball, not nested under a subdirectory like `model_name/config.json`.

#### `checkpoint_repository.repo`

Checkpoint repository name, bucket, or url.

#### `checkpoint_repository.revision`

(default: `"main"`)

The specific model version to use. It can be a branch name, a tag name, or a commit id. This field is only applicable to HF (HuggingFace) models.

### `max_batch_size`

(default: `256`)

Maximum number of input sequences to pass through the engine concurrently. Batch size and throughput share a direct relation, whereas batch size and single request latency share an indirect relation.
Tune this value according to your SLAs and latency budget.

### `max_seq_len`

(default: max\_position\_embeddings from the model repo)

Defines the maximum sequence length (context) of single request​.

### `max_num_tokens`

(default: `8192`)

Defines the maximum number of batched input tokens after padding is removed in each batch. Tuning this value more efficiently allocates memory to KV cache and executes more requests together.

### `max_prompt_embedding_table_size`

(default: `0`)

Maximum prompt embedding table size for [prompt tuning](https://developer.nvidia.com/blog/an-introduction-to-large-language-models-prompt-engineering-and-p-tuning/).

### `num_builder_gpus`

(default: `auto`)

Number of GPUs to be used at build time, defaults to configured `resource.accelerator` count – useful for FP8 quantization in particular, when more GPU memory is required at build time relative to memory usage at inference.

### `plugin_configuration`

Config for inserting plugin nodes into network graph definition for execution of user-defined kernels.

#### `plugin_configuration.paged_kv_cache`

(default: `True`)

Decompose KV cache into page blocks. Read more about what this does [here](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/advanced/gpt-attention.md#paged-kv-cache).

#### `plugin_configuration.use_paged_context_fmha`

(default: `True`)

Utilize paged context for fused multihead attention. This configuration is necessary to enable KV cache reuse. Read more about this configuration [here](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/advanced/kv-cache-reuse.md#how-to-enable-kv-cache-reuse).

#### `plugin_configuration.use_fp8_context_fmha`

(default: `False`)

Utilize FP8 quantization for context fused multihead attention to accelerate attention. To use this configuration, also set `plugin_configuration.use_paged_context_fmha`. Recommended: true
Read more about when to enable this [here](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/advanced/gpt-attention.md#fp8-context-fmha).

### `quantization_type`

(default: `no_quant`)

Quantization format with which to build the engine. Supported formats include:

* `no_quant` (meaning bf16 or fp16 depending on `torch_dtype` in the huggingface repo)
* `fp8` (sm 89+)
* `fp8_kv` (sm 89+)
* `fp4` (sm 100+)
* `fp4_kv` (sm 100+)

Additionally, refer to the hardware and quantization technique [support matrix](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html).

### `strongly_typed`

(default: `False`)

Whether to build the engine using strong typing, enabling TensorRT's optimizer to statically infer intermediate tensor types which can speed up build time for some formats.
Automatically typed is always enabled for fp4 and fp8 engines.
Weak typing enables the optimizer to elect tensor types, which may result in a faster runtime. For more information refer to TensorRT documentation [here](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html#strong-vs-weak-typing).

### `tensor_parallel_count`

(default: `1`)

Tensor parallelism count. For more information refer to NVIDIA documentation [here](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/features/parallelisms.html#tensor-parallelism).

### `speculator`

(default: `None`)

Config for inserting optional speculative decoding options.

#### Speculation with lookahead decoding

Speculation with lookahead decoding can be used by any model and does not require training.
The implemenation is based on the work at [lmsys.](https://lmsys.org/blog/2023-11-21-lookahead-decoding/)
We currently disallow performing structured generation and tool-calling with this optimization.

```yaml  theme={"system"}
model_name: Llama-3.1-8B-Instruct (lookahead decoding)
resources:
  accelerator: H100
  use_gpu: true
trt_llm:
  build:
    base_model: llama
    checkpoint_repository:
      repo: meta-llama/Llama-3.1-8B-Instruct
      source: HF
    max_batch_size: 32
    quantization_type: fp8_kv
    speculator:
      speculative_decoding_mode: LOOKAHEAD_DECODING
      windows_size: 7
      ngram_size: 5
      verification_set_size: 7
  runtime:
    kv_cache_free_gpu_mem_fraction: 0.62
```

#### `speculator.lookahead_ngram_size`, `speculator.lookahead_windows_size`, `speculator.lookahead_verification_set_size`

Usage of ngram size, window size, verification\_set\_size in the lookahead algorithm.

* `windows_size` is the Jacobi window size, meaning number of n-grams in lookahead branch that explores future draft tokens.
* `ngram_size` is the n-gram size, meaning the maximum number of draft tokens accepted per iteration.
* `verification_set_size` is the maximum number of n-grams considered for verification, meaning the number of draft token beam hypotheses.

A good default value could be \[5,5,5]. Often, lookahead\_verification\_set\_size is set to lookahead\_windows\_size.
`lookahead_ngram_size` is often increased when the generated tokens are simlar to contents of the prompt, and decreased if dissimilar.

### `lora_adapters`

(default: `None`)

A mapping from LoRA names to checkpoint repositories.
For example.

```yaml  theme={"system"}
checkpoint_repository:
  repo: meta-llama/Llama-2-13b-hf
  source: HF
lora_adapters:
  lora1:
    repo: hfl/chinese-llama-2-lora-13b
    source: HF
```

See [`checkpoint_repository`](/development/model/performance/engine-builder-config#checkpoint-repository) for details on how to configure checkpoint repositories.

Lora naming:
In addition to specifying the LoRAs here, you need to specify the [`served_model_name`](/development/model/performance/engine-builder-config#served-model-name) that is used to refer to the base model.
The `served_model_name` is required for deploying LoRAs.
The LoRA name (in the example above, this is "lora1") is used to query the model using the specified LoRA.

Lora sizes:
For optimal experience wrt efficency and stability we recommend inference with homogenious adapters (all the adapters have the same ranks and target the same modules).

## `trt_llm.runtime`

TRT-LLM engine runtime configuration.

### `kv_cache_free_gpu_mem_fraction`

(default: `0.9`)

Used to control the fraction of free gpu memory allocated for the KV cache. For more information, refer to the documentation [here](https://nvidia.github.io/TensorRT-LLM/performance/performance-tuning-guide/useful-runtime-flags.html#max-tokens-in-paged-kv-cache-and-kv-cache-free-gpu-memory-fraction).
If you are using DRAFT\_TOKENS\_EXTERNAL, we recommend to lower this, depending on the draft model size.

### `enable_chunked_context`

(default: `True`)

Enables chunked context, increasing the chance of batch processing between context and generation phase – which may be useful to increase throughput.
Note that one must set `plugin_configuration.use_paged_context_fmha: True` in order to leverage this feature.

### `batch_scheduler_policy`

(default: `guaranteed_no_evict`)

Supported scheduler policies are as follows:

* `guaranteed_no_evict`
* `max_utilization`

`guaranteed_no_evict` ensures that an in progress request is never evicted by reserving KV cache space for the maximum possible tokens that can be returned for a request.
`max_utilization` packs as many requests as possible during scheduling, which may increase throughput at the expense of additional latency.
For more information refer to the NVIDIA documentation [here](https://nvidia.github.io/TensorRT-LLM/performance/performance-tuning-guide/useful-runtime-flags.html#capacity-scheduler-policy).

### `request_default_max_tokens`

(default: `None`)

Default server configuration for the maximum number of tokens to generate for a single sequence, if one is not provided in the request body.
Sensible settings depend on your use case, a general value to set can be around 1000 tokens.

### `served_model_name`

(default: `None`)

The name used to refer to the base model when using LoRAs.
At least one LoRA must be specified under [`lora_adapters`](/development/model/performance/engine-builder-config#lora-adapters) to use LoRAs.


# Engine control in Python
Source: https://docs.baseten.co/development/model/performance/engine-builder-customization

Use `model.py` to customize engine behavior

When you create a new Truss with `truss init`, it creates two files: `config.yaml` and `model/model.py`. While you configure the Engine Builder in `config.yaml`, you may use `model/model.py` to access and control the engine object during inference.

You have two options:

1. Delete the `model/model.py` file and your TensorRT-LLM engine will run according to its base spec.
2. Update the code to support TensorRT-LLM.

<Warning>
  You must either update `model/model.py` to pass `trt_llm` as an argument to the `__init__` method OR delete the file. Otherwise you will get an error on deployment as the default `model/model.py` file is not written for TensorRT-LLM.
</Warning>

The `engine` object is a property of the `trt_llm` argument and must be initialized in `__init__` to be accessed in `load()` (which runs once on server start-up) and `predict()` (which runs for each request handled by the server).

This example applies a chat template with the Llama 3.1 8B tokenizer to the model prompt:

```python model/model.py theme={"system"}
import orjson  # faster serialization/deserialization than built-in json
from typing import Any, AsyncIterator
from transformers import AutoTokenizer
from fastapi.responses import StreamingResponse

SSE_PREFIX = "data: "

class Model:
    def __init__(self, trt_llm, **kwargs) -> None:
        self._secrets = kwargs["secrets"]
        self._engine = trt_llm["engine"]
        self._model = None
        self._tokenizer = None

    def load(self) -> None:
        self._tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.1-8B-Instruct", token=self._secrets["hf_access_token"])

    async def predict(self, model_input: Any) -> Any:
        # Apply chat template to prompt
        model_input["prompt"] = self._tokenizer.apply_chat_template(model_input["prompt"], tokenize=False)
        response = await self._engine.predict(model_input)

        # If the response is streaming, post-process each chunk
        if isinstance(response, StreamingResponse):
            token_gen = response.body_iterator

            async def processed_stream():
                async for chunk in some_post_processing_function(token_gen):
                    yield chunk

            return StreamingResponse(processed_stream(), media_type="text/event-stream")

        # Otherwise, return the raw output
        else:
            return response

# --- Post-processing helpers for SSE ---

def parse_sse_chunk(chunk: bytes) -> dict | None:
    """Parses an SSE-formatted chunk and returns the JSON payload."""
    try:
        text = chunk.decode("utf-8").strip()
        if not text.startswith(SSE_PREFIX):
            return None
        return orjson.loads(text[len(SSE_PREFIX):])
    except Exception:
        return None

def format_sse_chunk(payload: dict) -> bytes:
    """Formats a JSON payload back into an SSE chunk."""
    return f"{SSE_PREFIX}".encode("utf-8") + orjson.dumps(payload) + b"\n\n"

def transform_payload(payload: dict) -> dict:
    """Add a new field to the SSE payload."""
    payload["my_new_field"] = "my_new_value"
    return payload

async def some_post_processing_function(
    token_gen: AsyncIterator[bytes]
) -> AsyncIterator[bytes]:
    """Post-process each SSE chunk in the stream."""
    async for chunk in token_gen:
        payload = parse_sse_chunk(chunk)
        if payload is None:
            yield chunk
            continue

        transformed = transform_payload(payload)
        yield format_sse_chunk(transformed)
```


# Engine builder overview
Source: https://docs.baseten.co/development/model/performance/engine-builder-overview

Deploy optimized model inference servers in minutes

If you have a foundation model like Llama 3 or a fine-tuned variant and want to create a low-latency, high-throughput model inference server, TensorRT-LLM via the Engine Builder is likely the tool for you.

TensorRT-LLM is an open source performance optimization toolbox created by NVIDIA. It helps you build TensorRT engines for large language models like Llama and Mistral as well as certain other models like Whisper and large vision models.

Baseten's TensorRT-LLM Engine Builder simplifies and automates the process of using TensorRT-LLM for development and production. All you need to do is write a few lines of configuration and an optimized model serving engine will be built automatically during the model deployment process.

## FAQs

### Where are the engines stored?

The engines are stored in Baseten but owned by the user — we're working on a mechanism for downloading them. In the meantime, reach out if you need access to an engine that you created using the Engine Builder.

### Does the Engine Builder support quantization?

Yes. The Engine Builder can perform post-training quantization during the building process. For supported options, see [quantization in the config reference](/development/model/performance/engine-builder-config#quantization-type).

### Can I customize the engine behavior?

For further control over the TensorRT-LLM engine during inference, use the `model/model.py` file to access the engine object at runtime. See [controlling engines with Python](/development/model/performance/engine-builder-customization) for details.


# Performance client
Source: https://docs.baseten.co/development/model/performance/performance-client

The **Baseten Performance Client** is a high-performance library for interacting with model endpoints, supporting **embeddings, reranking, and classification**. It is available for both **Python (pip)** and **Node.js (npm)**.

<Card title="View on GitHub" icon="github" horizontal href="https://github.com/basetenlabs/truss/tree/main/baseten-performance-client" />

Built in Rust and integrated with Python and Node.js, the client is optimized for **massive concurrent POST requests**. It releases the Python GIL while executing requests, enabling simultaneous sync and async usage.

In our [benchmarks](https://www.baseten.co/blog/your-client-code-matters-10x-higher-embedding-throughput-with-python-and-rust/), the Performance Client reached **1200+ requests per second** per client.

It can be used when **deploying on Baseten**, as well as **third-party providers** such as OpenAI and Mixedbread.

<img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8b1df45b528b98df2154736919de105c" alt="benchmarks" data-og-width="1200" width="1200" data-og-height="565" height="565" data-path="images/performance-client-diagram.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=7974921583e72f195778a892e0fa9af1 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=6c97fe1f29ba0ac098d247965943f2eb 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=de2c7b3177be0adba10dc5c032523d08 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=4545ef1bff98f1877d5c4adb4231d5ad 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=61697cd3af7479fac9e0bf497b538c82 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/performance-client-diagram.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5c407d6f55103b325ca7547b3f11902b 2500w" />

***

## Installation

### Python

```bash  theme={"system"}
pip install baseten_performance_client
```

### Node.js

```bash  theme={"system"}
npm install baseten-performance-client
```

## Getting Started

### Python

```python  theme={"system"}
from baseten_performance_client import PerformanceClient

client = PerformanceClient(
    base_url="https://model-yqv4yjjq.api.baseten.co/environments/production/sync",
    api_key="YOUR_API_KEY"
)
```

### Node.js

```javascript  theme={"system"}
const { PerformanceClient } = require("baseten-performance-client");

const client = new PerformanceClient(
  "https://model-yqv4yjjq.api.baseten.co/environments/production/sync",
  process.env.BASETEN_API_KEY
);
```

You can also use **OpenAI** or **Mixedbread** endpoints by replacing the `base_url`.

## Embeddings

The client provides efficient embedding requests with configurable batching, concurrency, and latency optimizations.

### Example (Python)

```python  theme={"system"}
texts = ["Hello world", "Example text", "Another sample"] * 10

response = client.embed(
    input=texts,
    model="my_model",
    batch_size=16,
    max_concurrent_requests=256,
    max_chars_per_request=10000,
    hedge_delay=15,
    timeout_s=360
)
```

**Advanced parameters**

* `max_chars_per_request`, `batch_size`: Packs/Batches requests by number of entries or character count, whatever limit is reached first. Useful for optimial distribution across all your replicas on baseten.
* `hedge_delay`: Send duplicate requests after a delay (≥0.2s) to reduce the p99.5 latency. After hedge\_delay (s) is met, your request will be cloned once and race the original request. Limited by a 5% budget. Default: disabled.
* `timeout_s`: Timeout on each request. Raised a request.TimeoutError once a single request can't be retried. 429 and 5xx errors are always retried.

Async usage is also supported:

```python  theme={"system"}
response = await client.async_embed(input=texts, model="my_model")
```

### Example (Node.js)

```javascript  theme={"system"}
const response = await client.embed(
  ["Hello world", "Example text", "Another sample"],
  "my_model"
);
```

## Batch POST

Use `batch_post` for sending POST requests to any URL.
Built for benchmarks (p90/p95/p99 timings). Useful for starting off massive batch tasks, or benchmarking the performance of individual requests, while retaining a capped concurrency.
Releasing the GIL during all calls - you can do work in parallel without impacting performance.

### Example (Python) - completions/chat completions

```python  theme={"system"}
# requires stream=false / non-sse response.
payloads = [
    {"model": "my_model", "prompt": "Batch request 1", stream="false"},
    {"model": "my_model", "input": "Batch request 2", stream="false"}
] * 10

response = client.batch_post(
    url_path="/v1/completions",
    payloads=payloads,
    max_concurrent_requests=96,
    timeout_s=720,
    hedge_delay=30,
)
responses = response.data # array with 20 dicts
# timings = response.individual_request_times # array with the time.time() for each request
```

### Example (Node.js)

```javascript  theme={"system"}
const payloads = [
  { model: "my_model", input: ["Batch request 1"] },
  { model: "my_model", input: ["Batch request 2"] },
];

const response = await client.batchPost("/v1/embeddings", payloads, 96);
```

***

## Reranking

Compatible with BEI and text-embeddings-inference.

### Example (Python)

```python  theme={"system"}
response = client.rerank(
    query="What is the best framework?",
    texts=["Doc 1", "Doc 2", "Doc 3"]
)
```

***

## Classification

Supports classification endpoints such as BEI or text-embeddings-inference.

### Example (Python)

```python  theme={"system"}
response = client.classify(inputs=[
    "This is great!",
    "I did not like it.",
    "Neutral experience."
])
```

***

## Error Handling

The client raises standard Python/Node.js errors:

* **HTTPError**: Authentication failures, 4xx/5xx responses.
* **ValueError**: Invalid inputs (e.g., empty list, invalid batch size).

Example:

```python  theme={"system"}
try:
    response = client.embed(input=["Hello"], model="my_model")
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
```

***

## More examples, contribute to the open-source libary or more detailed usage:

Check out the readme in in [Github truss repo: baseten-performance-client](https://github.com/basetenlabs/truss/tree/main/baseten-performance-client)


# Private Docker Registries
Source: https://docs.baseten.co/development/model/private-registries

A guide to configuring a private container registry for your truss

Truss uses containerized environments to ensure consistent model execution across deployments. When deploying a custom base image or a custom server from a private registry, you must grant Baseten access to download that image.

## AWS Elastic Cloud Registry (ECR)

AWS supports using either [service accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html), or [access tokens](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html#registry-auth-token) for short lived access for container registry authentication.

### AWS IAM Service accounts

To use an IAM service account for long-lived access, you can use the `AWS_IAM` authentication method in Truss.

1. Get an AWS\_ACCESS\_KEY\_ID and AWS\_SECRET\_ACCESS\_KEY from the AWS dashboard

2. Add these as [secrets](https://app.baseten.co/settings/secrets) in Baseten. These should be named `aws_access_key_id` and `aws_secret_access_key`
   respectively.

3. Choose the `AWS_IAM` authentication method when setting up your Truss. The `config.yaml` file should look something like this:

```
...
  base_image:
    image: <aws account id>.dkr.ecr.<region>.amazonaws.com/path/to/image
    docker_auth:
      auth_method: AWS_IAM
      registry: <aws account id>.dkr.ecr.<region>.amazonaws.com
  secrets:
    aws_access_key_id: null
    aws_secret_access_key: null
...
```

Note here that you need to specify the registry and image separately.

If you'd like to use different secret names besides the default, you can configure these using the
`aws_access_key_id_secret_name` and `aws_secret_access_key_secret_name` options
under `docker_auth`:

```
...
base_image:
  ...
  docker_auth:
    auth_method: AWS_IAM
    registry: <aws account id>.dkr.ecr.<region>.amazonaws.com
    aws_access_key_id_secret_name: custom_aws_access_key_secret
    aws_secret_access_key_secret_name: custom_aws_secret_key_secret
secrets:
  custom_aws_access_key_secret: null
  custom_aws_secret_key_secret: null

```

### Access Token

1. Get the a **Base64-encoded** secret:

```sh  theme={"system"}
PASSWORD=`aws ecr get-login-password --region {us-east-1}`
echo -n "AWS:$PASSWORD" | base64
```

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `DOCKER_REGISTRY_{aws account id}.dkr.ecr.{us-east-1}.amazonaws.com` with the `Base64-encoded secret` as the value.

3. Add the secret name to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```yaml config.yaml theme={"system"}
secrets:
  DOCKER_REGISTRY_{aws account id}.dkr.ecr.{us-east-1}.amazonaws.com: null
```

## Google Cloud Artifact Registry

GCP supports using either [access tokens](https://cloud.google.com/artifact-registry/docs/docker/authentication#token) for short lived access or [service accounts](https://cloud.google.com/iam/docs/service-account-overview) for container registry authentication.

### Service Account

1. Get your [service account key](https://cloud.google.com/artifact-registry/docs/docker/authentication#json-key) as a JSON key blob.

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `gcp-service-account` (or similar) with the JSON key blob as the value.

3. Add the secret name that you used to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```yaml config.yaml theme={"system"}
secrets:
  gcp-service-account: null
```

4. Configure the `docker_auth` section of your `base_image:` to ensure that the service account authentication method will be used.

```
base_image:
  ...
  docker_auth:
    auth_method: GCP_SERVICE_ACCOUNT_JSON
    secret_name: gcp-service-account
    registry: {us-west2}-docker.pkg.dev
```

Note that here, `secret_name` should match the name of the secret that is contains the JSON key blob.

### Access Token

1. Get your [access token](https://cloud.google.com/artifact-registry/docs/docker/authentication#token)

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `DOCKER_REGISTRY_{us-west2}-docker.pkg.dev` with the `Base64-encoded secret` as the value.

3. Add the secret name to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```yaml config.yaml theme={"system"}
secrets:
  DOCKER_REGISTRY_{us-west2}-docker.pkg.dev: null
```

## Docker Hub

1. Get the a **Base64-encoded** secret:

```sh  theme={"system"}
echo -n 'username:password' | base64
```

2. Add a new [secret](https://app.baseten.co/settings/secrets) to Baseten named `DOCKER_REGISTRY_https://index.docker.io/v1/` with the `Base64-encoded secret` as the value.

3. Add the secret name to the `secrets` section of the `config.yaml` to allow this model to access the secret when it is pushed.

```
Name: DOCKER_REGISTRY_https://index.docker.io/v1/
Token: <Base64-encoded secret>
```

Then, this to `config.yaml`:

```yaml config.yaml theme={"system"}
secrets:
  DOCKER_REGISTRY_https://index.docker.io/v1/: null
```


# Using request objects / cancellation
Source: https://docs.baseten.co/development/model/requests

Get more control by directly using the request object.

Truss processes client requests by extracting and validating payloads. For **advanced use cases**, you can access the raw request object to:

* **Customize payload deserialization** (e.g., binary protocol buffers).
* **Handle disconnections & cancel long-running predictions.**

<Tip>You can mix request objects with standard inputs or use requests exclusively for performance optimization.</Tip>

## Using Request Objects in Truss

You can define request objects in `preprocess`, `predict`, and `postprocess`:

```python  theme={"system"}
import fastapi

class Model:
    def preprocess(self, request: fastapi.Request):
        ...

    def predict(self, inputs, request: fastapi.Request):
        ...

    def postprocess(self, inputs, request: fastapi.Request):
        ...
```

### Rules for Using Requests

* The request must be **type-annotated** as `fastapi.Request`.
* If **only** requests are used, Truss **skips payload extraction** for better performance.
* If **both** request objects and standard inputs are used:
  * Request **must be the second argument**.
  * **Preprocessing transforms inputs**, but the request object remains unchanged.
  * `postprocess` cannot use only the request—it must receive the model’s output.
  * If `predict` only uses the request, `preprocess` cannot be used.

```python  theme={"system"}
import fastapi, asyncio, logging

class Model:
    async def predict(self, inputs, request: fastapi.Request):
        await asyncio.sleep(1)
        if await request.is_disconnected():
            logging.warning("Cancelled before generation.")
            return  # Cancel request on the model engine here.

        for i in range(5):
            await asyncio.sleep(1.0)
            logging.warning(i)
            yield str(i)  # Streaming response
            if await request.is_disconnected():
                logging.warning("Cancelled during generation.")
                return  # Cancel request on the model engine here.
```

<Tip>You must implement request cancellation at the model level, which varies by framework.</Tip>

## Cancelling Requests in Specific Frameworks

### TRT-LLM (Polling-Based Cancellation)

For **TensorRT-LLM**, use `response_iterator.cancel()` to terminate streaming requests:

```python  theme={"system"}
async for request_output in response_iterator:
    if await is_cancelled_fn():
        logging.info("Request cancelled. Cancelling Triton request.")
        response_iterator.cancel()
        return
```

<Note>See full example in [TensorRT-LLM Docs](https://developer.nvidia.com/tensorrt-llm).</Note>

### vLLM (Abort API)

For **vLLM**, use `engine.abort()` to stop processing:

```python  theme={"system"}
async for request_output in results_generator:
    if await request.is_disconnected():
        await engine.abort(request_id)
        return
```

<Note>See full example in [vLLM Docs](https://docs.vllm.ai/en/latest/dev/engine/async_llm_engine.html#vllm.AsyncLLMEngine.generate).</Note>

## Unsupported Request Features

* **Streaming file uploads** – Use URLs instead of embedding large data in the request.
* **Client-side headers** – Most headers are stripped; include necessary metadata in the payload.


# Custom Responses
Source: https://docs.baseten.co/development/model/responses

Get more control by directly creating the response object.

By default, Truss wraps prediction results into an HTTP response. For **advanced use cases**, you can create response objects manually to:

* **Control HTTP status codes.**
* **Use server-sent events (SSEs) for streaming responses.**

<Tip>You can return a response from predict or postprocess, but not both.</Tip>

## Returning Custom Response Objects

Any subclass of starlette.responses.Response is supported.

```python  theme={"system"}
import fastapi

class Model:
    def predict(self, inputs) -> fastapi.Response:
        return fastapi.Response(...)
```

<Tip>If `predict` returns a response, `postprocess` cannot be used.</Tip>

## Example: Streaming with SSEs

For **server-sent events (SSEs)**, use `StreamingResponse`:

```python  theme={"system"}
import time
from starlette.responses import StreamingResponse

class Model:
    def predict(self, model_input):
        def event_stream():
            while True:
                time.sleep(1)
                yield f"data: Server Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        return StreamingResponse(event_stream(), media_type="text/event-stream")
```

## Limitations

* **Response headers are not fully propagated** – include metadata in the response body.

<Info>
  Also see [Using Request Objects](/development/model/requests)
  for handling raw requests.
</Info>


# Security and secrets
Source: https://docs.baseten.co/development/model/secrets

Using secrets securely in your ML models

Truss allows you to securely manage **API keys**, **access tokens**, **passwords**, **and other secrets** without exposing them in code.

## 1. Define Secrets in `config.yaml`

Add secrets with **placeholder** values in `config.yaml`:

```yaml  theme={"system"}
secrets:
  hf_access_token: null
```

<Warning>Never store actual secret values in `config.yaml`. Store secrets in the [workspace settings](https://app.baseten.co/settings/secrets).</Warning>

## 2. Access Secrets in `model.py`

Secrets are passed as **keyword arguments** to the `Model` class:

```python  theme={"system"}
def __init__(self, **kwargs):
    self._secrets = kwargs["secrets"]
```

Use secrets inside load or predict:

```python  theme={"system"}
def load(self):
    self._model = pipeline(
        "fill-mask",
        model="baseten/docs-example-gated-model",
        use_auth_token=self._secrets["hf_access_token"]
    )
```

## 3. Store Secrets on Your Remote

* On **Baseten**, add secrets in the [workspace settings](https://app.baseten.co/settings/secrets).
* Use the **exact name** from `config.yaml` (case-sensitive).

## 4. Deploying with Secrets

By default, models have access to any secrets on a workspace.


# Streaming output
Source: https://docs.baseten.co/development/model/streaming

Streaming Output for LLMs

Streaming output significantly reduces wait time for generative AI models by returning results as they are generated instead of waiting for the full response.

## Why Streaming?

* ✅ **Faster response time** – Get initial results in under **1 second** instead of waiting **10+ seconds**.
* ✅ **Improved user experience** – Partial outputs are **immediately usable**.

This guide walks through **deploying Falcon 7B** with streaming enabled.

### 1. Initialize Truss

```sh  theme={"system"}
truss init falcon-7b && cd falcon-7b
```

### 2: Implement Model (Non-Streaming)

This first version loads the Falcon 7B model **without** streaming:

```python model/model.py theme={"system"}
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from typing import Dict

CHECKPOINT = "tiiuae/falcon-7b-instruct"
DEFAULT_MAX_NEW_TOKENS = 150
DEFAULT_TOP_P = 0.95

class Model:
    def __init__(self, **kwargs) -> None:
        self.tokenizer = None
        self.model = None

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)
        self.model = AutoModelForCausalLM.from_pretrained(
            CHECKPOINT, torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto"
        )

    def predict(self, request: Dict) -> Dict:
        prompt = request["prompt"]
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True, padding=True)
        input_ids = inputs["input_ids"].to("cuda")
        generation_config = GenerationConfig(temperature=1, top_p=DEFAULT_TOP_P, top_k=40)

        with torch.no_grad():
            return self.model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                pad_token_id=self.tokenizer.eos_token_id,
                max_new_tokens=DEFAULT_MAX_NEW_TOKENS,
            )
```

### 3. Add Streaming Support

To enable streaming, we:

* Use `TextIteratorStreamer` to stream tokens as they are generated.
* Run `generate()` in a **separate thread** to prevent blocking.
* Return a **generator** that streams results.

```python model/model.py theme={"system"}
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, TextIteratorStreamer
from threading import Thread
from typing import Dict

CHECKPOINT = "tiiuae/falcon-7b-instruct"

class Model:
    def __init__(self, **kwargs) -> None:
        self.tokenizer = None
        self.model = None

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained(CHECKPOINT)
        self.model = AutoModelForCausalLM.from_pretrained(
            CHECKPOINT, torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto"
        )

    def predict(self, request: Dict):
        prompt = request["prompt"]
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True, padding=True)
        input_ids = inputs["input_ids"].to("cuda")

        streamer = TextIteratorStreamer(self.tokenizer)
        generation_config = GenerationConfig(temperature=1, top_p=0.95, top_k=40)

        def generate():
            self.model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                pad_token_id=self.tokenizer.eos_token_id,
                max_new_tokens=150,
                streamer=streamer,
            )

        thread = Thread(target=generate)
        thread.start()

        def stream_output():
            for text in streamer:
                yield text
            thread.join()

        return stream_output()
```

### 4. Configure `config.yaml`

```yaml config.yaml theme={"system"}
model_name: falcon-streaming
requirements:
  - torch==2.0.1
  - peft==0.4.0
  - scipy==1.11.1
  - sentencepiece==0.1.99
  - accelerate==0.21.0
  - bitsandbytes==0.41.1
  - einops==0.6.1
  - transformers==4.31.0
resources:
  cpu: "4"
  memory: 16Gi
  use_gpu: true
  accelerator: L4
```

### 5. Deploy & Invoke

Deploy the model:

```sh  theme={"system"}
truss push
```

Invoke with:

```sh  theme={"system"}
truss predict -d '{"prompt": "Tell me about falcons", "do_sample": true}'
```


# Torch Compile Caching 🆕
Source: https://docs.baseten.co/development/model/torch-compile-cache

Accelerate cold starts by loading in previous compilation artifacts.

<Warning>
  ### Requires [b10cache](/development/model/b10cache) enabled
</Warning>

## Overview

PyTorch's `torch.compile` feature offers significant performance improvements for inference workloads, reducing inference time by up to 40%. However, this optimization comes with a trade-off: the initial compilation process adds considerable latency to cold starts, as the model must be compiled before serving its first inference request.

This compilation overhead becomes particularly problematic in production environments where:

* Models frequently scale up and down based on demand
* New pods are regularly spawned to handle traffic spikes
* Each new instance must repeat the compilation process from scratch

## Solution

Persist compilation artifacts across deployments and pod restarts, by storing them in [b10cache](/development/model/b10cache). When a new pod starts up, it can load previously compiled artifacts instead of recompiling from scratch. The library gracefully handles large scale ups, managing race conditions and ensuring fault-tolerance in the shared b10cache.

In practice, this strategy slashes compilation latencies to just around 5-20 seconds, depending on the model.

***

## Implementation Options

There are two different deployment patterns that benefit from torch compile caching:

<Tip>
  * **Truss Models**: `model.py` calling `torch.compile` ([Jump to](#truss-models-model-py))
  * **vLLM Servers**: vLLM custom server ([Jump to](#vllm-servers-cli-tool))
</Tip>

***

## Truss Models (`model.py`)

### API Reference

We expose two API calls that return an `OperationStatus` object to help you control program flow based on the result.

<Accordion title="load_compile_cache()">
  If you have previously saved compilation cache for this model, load it to speed up the compilation for the model on this pod.

  **Returns:**

  * `OperationStatus.SUCCESS` → successful load
  * `OperationStatus.SKIPPED` → if torch compilation artifacts already exist on the pod
  * `OperationStatus.ERROR` → general catch-all errors
  * `OperationStatus.DOES_NOT_EXIST` → if no cache file was found
</Accordion>

<Accordion title="save_compile_cache()">
  Save your model's torch compilation cache for future use. This should be called after running prompts to warm up your model and trigger compilation.

  **Returns:**

  * `OperationStatus.SUCCESS` → successful save
  * `OperationStatus.SKIPPED` → skipped because compile cache already exists in shared directory
  * `OperationStatus.ERROR` → general catch-all errors
</Accordion>

### Implementation Example

Here is an example of compile caching for Flux, an image generation model. Note how we save the result of `load_compile_cache` to inform on whether to `save_compile_cache`.

#### Step 1: Update `config.yaml`

Under requirements, add `b10-transfer`:

```yaml  theme={"system"}
requirements:
  - b10-transfer
```

#### Step 2: Update `model.py`

Import the library and use the two functions to speed up torch compilation time:

```python  theme={"system"}
from b10_transfer import load_compile_cache, save_compile_cache, OperationStatus

class Model:
    def load(self):
        self.pipe = FluxPipeline.from_pretrained(
            self.model_name, torch_dtype=torch.bfloat16, token=self.hf_access_token
        ).to("cuda")

        # Try to load compile cache
        cache_loaded: OperationStatus = load_compile_cache()

        if cache_loaded == OperationStatus.ERROR:
            logging.info("Run in eager mode, skipping torch compile")
        else:
            logging.info("Compiling the model for performance optimization")
            self.pipe.transformer = torch.compile(
                self.pipe.transformer, mode="max-autotune-no-cudagraphs", dynamic=False
            )

            self.pipe.vae.decode = torch.compile(
                self.pipe.vae.decode, mode="max-autotune-no-cudagraphs", dynamic=False
            )

            seed = random.randint(0, MAX_SEED)
            generator = torch.Generator().manual_seed(seed)
            start_time = time.time()
            # Warmup the model with dummy prompts, also triggering compilation
            self.pipe(
                prompt="dummy prompt",
                prompt_2=None,
                guidance_scale=0.0,
                max_sequence_length=256,
                num_inference_steps=4,
                width=1024,
                height=1024,
                output_type="pil",
                generator=generator
            )

            end_time = time.time()

            logging.info(
                f"Warmup completed in {(end_time - start_time)} seconds. "
                "This is expected to take a few minutes on the first run."
            )

            if cache_loaded != OperationStatus.SUCCESS:
                # Save compile cache for future runs
                outcome: OperationStatus = save_compile_cache()
```

<Note>
  See the [full example](https://github.com/basetenlabs/truss-examples/tree/main/flux/schnell).
</Note>

***

## vLLM Servers (CLI Tool)

### Overview

This should be used whenever using compile options with vLLM. On vLLM V1, compiling is the default behavior. This command line tool spawns a process that is completely automatic—it loads the compile cache if you have saved it before, and if not, it will save the compile cache.

### Implementation

There are two changes to make in `config.yaml`:

#### Step 1: Add Requirements

Under requirements, add `b10-transfer`:

```yaml  theme={"system"}
requirements:
  - b10-transfer
```

#### Step 2: Update Start Command

Under start command, add `b10-compile-cache &` right before the `vllm serve` call:

```yaml  theme={"system"}
start_command: "... b10-compile-cache & vllm serve ..."
```

<Note>
  See the [full example](https://github.com/basetenlabs/truss-examples/tree/main/mistral/mistral-small-3.1).
</Note>

***

## Advanced Configuration

<Accordion title="Parameter Overrides">
  The torch compile caching library supports several environment variables for fine-tuning behavior in production environments:

  ### Cache Directory Configuration

  **`TORCHINDUCTOR_CACHE_DIR`** (optional)

  * **Default**: `/tmp/torchinductor_<username>`
  * **Description**: Directory where PyTorch stores compilation artifacts locally
  * **Allowed prefixes**: `/tmp/`, `/cache/`, `~/.cache`
  * **Usage**: Set this if you need to customize where torch compilation artifacts are stored on the local filesystem

  **`B10FS_CACHE_DIR`** (optional)

  * **Default**: Derived from b10cache mount point + `/compile_cache`
  * **Description**: Directory in b10cache where compilation artifacts are persisted across deployments
  * **Usage**: Typically doesn't need to be changed as it's automatically configured based on your b10cache setup

  **`LOCAL_WORK_DIR`** (optional)

  * **Default**: `/app`
  * **Description**: Local working directory for temporary operations
  * **Allowed prefixes**: `/app/`, `/tmp/`, `/cache/`

  ### Performance and Resource Limits

  **`MAX_CACHE_SIZE_MB`** (optional)

  * **Default**: `1024` (1GB)
  * **Cap**: Limited by `MAX_CACHE_SIZE_CAP_MB` for safety
  * **Description**: Maximum size of a single cache archive in megabytes
  * **Usage**: Increase for larger models with extensive compilation artifacts, decrease to save storage

  **`MAX_CONCURRENT_SAVES`** (optional)

  * **Default**: `50`
  * **Cap**: Limited by `MAX_CONCURRENT_SAVES_CAP` for safety
  * **Description**: Maximum number of concurrent save operations allowed
  * **Usage**: Tune based on your deployment's concurrency requirements and storage performance

  ### Cleanup and Maintenance

  **`CLEANUP_LOCK_TIMEOUT_SECONDS`** (optional)

  * **Default**: `30`
  * **Cap**: Limited by `LOCK_TIMEOUT_CAP_SECONDS`
  * **Description**: Timeout for cleaning up stale lock files, to prevent deadlocks. They may occur when a replica holding the lock crashes.
  * **Usage**: Decrease if you're experiencing deadlocks in high-load scenarios

  **`CLEANUP_INCOMPLETE_TIMEOUT_SECONDS`** (optional)

  * **Default**: `60`
  * **Cap**: Limited by `INCOMPLETE_TIMEOUT_CAP_SECONDS`
  * **Description**: Timeout for cleaning up incomplete cache files
  * **Usage**: Increase for slower storage systems or larger cache files

  ### Example Configuration

  ```yaml  theme={"system"}
  # config.yaml
  environment_variables:
    MAX_CACHE_SIZE_MB: "2048"
    MAX_CONCURRENT_SAVES: "25"
    CLEANUP_LOCK_TIMEOUT_SECONDS: "45"
  ```

  <Note>
    Most users won't need to modify these settings. The defaults are optimized for typical production workloads. Only adjust these values if you're experiencing specific performance issues or have unusual deployment requirements.
  </Note>
</Accordion>

***

## Further Reading

To understand implementation details, read more [here](https://docs.pytorch.org/tutorials/recipes/torch_compile_caching_tutorial.html).


# WebSockets 🆕
Source: https://docs.baseten.co/development/model/websockets

Enable real-time, streaming, bidirectional communication using WebSockets for Truss models and Chainlets.

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

## Connection input & output size

Measured at different percentiles (p50, p90, p95, p99):

* **Connection input size:** Bytes sent by the client to the server for the duration of the connection.
* **Connection output size:** Bytes sent by the client to the server for the duration of the connection.


# Embeddings with BEI
Source: https://docs.baseten.co/examples/bei

Serve embedding, reranking, and classification models

Baseten Embeddings Inference is Baseten's solution for production grade inference on embedding, classification and reranking models using TensorRT-LLM.

With Baseten Embeddings Inference you get the following benefits:

* Lowest-latency inference across any embedding solution (vLLM, SGlang, Infinity, TEI, Ollama)<sup>1</sup>
* Highest-throughput inference across any embedding solution (vLLM, SGlang, Infinity, TEI, Ollama) - thanks to XQA kernels, FP8 and dynamic batching.<sup>2</sup>
* High parallelism: up to 1400 client embeddings per second
* Cached model weights for fast vertical scaling and high availability - no Hugging Face hub dependency at runtime
* Ahead-of-time compilation, memory allocation and fp8 post-training quantization

### Getting started with embedding models:

Embedding models are LLMs without a lm\_head for language generation.
Typical architectures that are supported for embeddings are `LlamaModel`, `BertModel`, `RobertaModel` or `Gemma2Model`, and contain the safetensors, config, tokenizer and sentence-transformer config files.
A good example is the repo [BAAI/bge-multilingual-gemma2](https://huggingface.co/BAAI/bge-multilingual-gemma2).

To deploy a model for embeddings, set the following config in your local directory.

```yaml config.yaml theme={"system"}
model_name: BEI-Linq-Embed-Mistral
resources:
  accelerator: H100_40GB
  use_gpu: true
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      # for a different model, change the repo to e.g. to "Salesforce/SFR-Embedding-Mistral"
      # "BAAI/bge-en-icl" or "BAAI/bge-m3"
      repo: "Linq-AI-Research/Linq-Embed-Mistral"
      revision: main
      source: HF
    # only Llama, Mistral and Qwen Models support quantization.
    # others, use: "quantization_type: no_quant"
    quantization_type: fp8
```

With `config.yaml` in your local directory, you can deploy the model to Baseten.

```bash  theme={"system"}
truss push --publish --promote
```

Deployed embedding models are OpenAI compatible without any additional settings.
You may use the client code below to consume the model.

```python  theme={"system"}
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    # add the deployment URL
    base_url="https://model-xxxxxx.api.baseten.co/environments/production/sync/v1"
)

embedding = client.embeddings.create(
    input=["Baseten Embeddings are fast.", "Embed this sentence!"],
    model="not-required"
)
```

### Example deployment of a classification, reranking and classification models

Besides embedding models, BEI deploys high-throughput rerank and classification models.
You can identify suitable architectures by their `ForSequenceClassification` suffix in the huggingface repo.
The use-case for these models is either Reward Modeling, Reranking documents in RAG or tasks like content moderation.

```yaml  theme={"system"}
model_name: BEI-mixedbread-rerank-large-v2-fp8
resources:
  accelerator: H100_40GB
  cpu: '1'
  memory: 10Gi
  use_gpu: true
trt_llm:
  build:
    base_model: encoder
    checkpoint_repository:
      repo: michaelfeil/mxbai-rerank-large-v2-seq
      revision: main
      source: HF
    # only Llama, Mistral and Qwen Models support quantization
    quantization_type: fp8
```

As OpenAI does not offer reranking or classification, we are sending a simple request to the endpoint.
Depending on the model, you might want to apply a specific prompt template first.

```python  theme={"system"}
import requests
import os

headers = {
    f"Authorization": f"Api-Key {os.environ['BASETEN_API_KEY']}"
}

# model specific prompt for mixedbread's reranker v2.
prompt = (
  "<|endoftext|><|im_start|>system\nYou are Qwen, created by Alibaba Cloud. You are a helpful assistant.\n<|im_end|>\n<|im_start|>user\n"
  "query: {query} \ndocument: {doc} \nYou are a search relevance expert who evaluates how well documents match search queries. For each query-document pair, carefully analyze the semantic relationship between them, then provide your binary relevance judgment (0 for not relevant, 1 for relevant).\nRelevance:<|im_end|>\n<|im_start|>assistant\n"
).format(query="What is Baseten?",doc="Baseten is a fast inference provider.")

requests.post(
    headers=headers,
    url="https://model-xxxxxx.api.baseten.co/environments/production/sync/predict",
    json={
        "inputs": prompt,
        "raw_scores": True,
    }
)
```

### Benchmarks and Performance optimizations

Embedding models on BEI are fast, and offer currently the fastest implementation for embeddings across all open-source and closed-source providers.
The team behind the implementation are the authors of [infinity](https://github.com/michaelfeil/infinity).
We recommend using fp8 quantization for LLama, Mistral and Qwen2 models on L4 or newer (L4, H100, H200 and B200).
Quality difference between fp8 and bfloat16 is often negligible - embedding models often retentain of >99% cosine simalarity between both presisions,
and reranking models retain the ranking order - despite a difference in the retained output.
For more details, check out the [technical launch post](https://www.baseten.co/blog/how-we-built-high-throughput-embedding-inference-with-tensorrt-llm/).

<Frame>
  <img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/bei-throughput.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=46c3aee1c00acb0a4b1cb375322f8050" data-og-width="3436" width="3436" data-og-height="2628" height="2628" data-path="images/bei-throughput.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/bei-throughput.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c7b18eaf46bf53ff032652ab3615b70b 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/bei-throughput.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=fa2ad40709ff9d7ab1a6a5e6e3559c39 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/bei-throughput.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f921e370210539ce5fb4fc56fbedb922 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/bei-throughput.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=268a8a4b9c30d9e128bfb8e899d51076 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/bei-throughput.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=2132c94a044cb85cff61b71cf8d64b1a 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/bei-throughput.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3a6f7ef261968fee930140e89faf15bd 2500w" />
</Frame>

The team at Baseten has additional options for sharing cached model weights across replicas - for very fast horizontal scaling.
Please contact us to enable this option.

### Deploy custom or fine-tuned models on BEI:

We support the deployment of of the below models, as well all finetuned variants of these models (same architecture & customized weights).
The following repositories are supported - this list is not exhaustive.

| Model Repository                                                                                              | Architecture                        | Function            |
| ------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------------- |
| [`Salesforce/SFR-Embedding-Mistral`](https://huggingface.co/Salesforce/SFR-Embedding-Mistral)                 | MistralModel                        | embedding           |
| [`BAAI/bge-m3`](https://huggingface.co/BAAI/bge-m3)                                                           | BertModel                           | embedding           |
| [`BAAI/bge-multilingual-gemma2`](https://huggingface.co/BAAI/bge-multilingual-gemma2)                         | Gemma2Model                         | embedding           |
| [`mixedbread-ai/mxbai-embed-large-v1`](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1)             | BertModel                           | embedding           |
| [`BAAI/bge-large-en-v1.5`](https://huggingface.co/BAAI/bge-large-en-v1.5)                                     | BertModel                           | embedding           |
| [`allenai/Llama-3.1-Tulu-3-8B-RM`](https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-RM)                     | LlamaForSequenceClassification      | classifier          |
| [`ncbi/MedCPT-Cross-Encoder`](https://huggingface.co/ncbi/MedCPT-Cross-Encoder)                               | BertForSequenceClassification       | reranker/classifier |
| [`SamLowe/roberta-base-go_emotions`](https://huggingface.co/SamLowe/roberta-base-go_emotions)                 | XLMRobertaForSequenceClassification | classifier          |
| [`mixedbread/mxbai-rerank-large-v2-seq`](https://huggingface.co/michaelfeil/mxbai-rerank-large-v2-seq)        | Qwen2ForSequenceClassification      | reranker/classifier |
| [`BAAI/bge-en-icl`](https://huggingface.co/BAAI/bge-en-icl)                                                   | LlamaModel                          | embedding           |
| [`BAAI/bge-reranker-v2-m3`](https://huggingface.co/BAAI/bge-reranker-v2-m3)                                   | BertForSequenceClassification       | reranker/classifier |
| [`Skywork/Skywork-Reward-Llama-3.1-8B-v0.2`](https://huggingface.co/Skywork/Skywork-Reward-Llama-3.1-8B-v0.2) | LlamaForSequenceClassification      | classifier          |
| [`Snowflake/snowflake-arctic-embed-l`](https://huggingface.co/Snowflake/snowflake-arctic-embed-l)             | BertModel                           | embedding           |
| [`nomic-ai/nomic-embed-code`](https://huggingface.co/nomic-ai/nomic-embed-code)                               | Qwen2Model                          | embedding           |

<sup>1</sup> measured on H100-HBM3 (bert-large-335M, for BAAI/bge-en-icl: 9ms)
<sup>2</sup> measured on H100-HBM3 (leading model architecture on MTEB, MistralModel-7B)


# Transcribe audio with Chains
Source: https://docs.baseten.co/examples/chains-audio-transcription

Process hours of audio in seconds using efficient chunking, distributed inference, and optimized GPU resources.

<Card title="View example on GitHub" horizontal icon="github" iconType="light" href="https://github.com/basetenlabs/truss-examples/tree/main/chains-examples/docs/audio-transcription" />

This guide walks through building an audio transcription pipeline using Chains. You'll break down large media files, distribute transcription tasks across autoscaling deployments, and leverage high-performance GPUs for rapid inference.

# 1. Overview

This Chain enables fast, high-quality transcription by:

* **Partitioning** long files (10+ hours) into smaller segments.
* **Detecting silence** to optimize split points.
* **Parallelizing inference** across multiple GPU-backed deployments.
* **Batching requests** to maximize throughput.
* **Using range downloads** for efficient data streaming.
* Leveraging `asyncio` for concurrent execution.

# 2. Chain Structure

Transcription is divided into two processing layers:

1. **Macro chunks:** Large segments (\~300s) split from the source media file. These are processed in parallel to handle massive files efficiently.
2. **Micro chunks:** Smaller segments (\~5–30s) extracted from macro chunks and sent to the Whisper model for transcription.

# 3. Implementing the Chainlets

## `Transcribe` (Entrypoint Chainlet)

Handles transcription requests and dispatches tasks to worker Chainlets.

Function signature:

```python  theme={"system"}
async def run_remote(
  self,
  media_url: str,
  params: data_types.TranscribeParams
) -> data_types.TranscribeOutput:
```

**Steps:**

* Validates that the media source supports **range downloads**.
* Uses **FFmpeg** to extract metadata and duration.
* Splits the file into **macro chunks**, optimizing split points at silent sections.
* Dispatches **macro chunk tasks** to the MacroChunkWorker for processing.
* Collects **micro chunk transcriptions**, merges results, and returns the final text.

**Example request:**

```bash  theme={"system"}
curl -X POST $INVOCATION_URL \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '<JSON_INPUT>'
```

```json  theme={"system"}
{
  "media_url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
  "params": {
    "micro_chunk_size_sec": 30,
    "macro_chunk_size_sec": 300
  }
}
```

## `MacroChunkWorker` (Processing Chainlet)

Processes **macro chunks** by:

* **Extracting** relevant time segments using **FFmpeg**.
* **Streaming audio** instead of downloading full files for low latency.
* **Splitting segments** at silent points.
* **Encoding** audio in base64 for efficient transfer.
* **Distributing micro chunks** to the Whisper model for transcription.

This Chainlet **runs in parallel** with multiple instances autoscaled dynamically.

## `WhisperModel` (Inference Model)

A separately deployed **Whisper** model Chainlet handles speech-to-text transcription.

* Deployed **independently** to allow fast iteration on business logic without redeploying the model.
* Used **across different Chains** or accessed directly as a standalone model.
* Supports **multiple environments** (e.g., dev, prod) using the same instance.

Whisper can also be deployed as a **standard Truss model**, separate from the Chain.

# 4. Optimizing Performance

Even for very large files, **processing time remains bounded** by parallel execution.

## Key performance tuning parameters:

* `micro_chunk_size_sec` → Balance GPU utilization and inference latency.
* `macro_chunk_size_sec` → Adjust chunk size for optimal parallelism.
* **Autoscaling settings** → Tune concurrency and replica counts for load balancing.

Example speedup:

```json  theme={"system"}
{
  "input_duration_sec": 734.26,
  "processing_duration_sec": 82.42,
  "speedup": 8.9
}
```

# 5. Deploy & Run the Chain

## Deploy WhisperModel first:

```bash  theme={"system"}
truss chains push whisper_chainlet.py
```

Copy the **invocation URL** and update `WHISPER_URL` in `transcribe.py`.

## Deploy the transcription Chain:

```bash  theme={"system"}
truss chains push transcribe.py
```

## Run transcription on a sample file:

```bash  theme={"system"}
curl -X POST $INVOCATION_URL \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '<JSON_INPUT>'
```

***

# Next Steps

* Learn more about [Chains](/development/chain/overview).
* Optimize GPU **autoscaling** for peak efficiency.
* Extend the pipeline with **custom business logic**.


# RAG pipeline with Chains
Source: https://docs.baseten.co/examples/chains-build-rag

Build a RAG (retrieval-augmented generation) pipeline with  Chains

[Learn more about Chains](/development/chain/overview)

## Prerequisites

To use Chains, install a recent Truss version and ensure pydantic is v2:

```bash  theme={"system"}
pip install --upgrade truss 'pydantic>=2.0.0'
```

<Accordion title="Help for setting up a clean development environment">
  Truss requires python `>=3.8,<3.13`. To set up a fresh development environment,
  you can use the following commands, creating a environment named `chains_env`
  using `pyenv`:

  ```bash  theme={"system"}
  curl https://pyenv.run | bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  source ~/.bashrc
  pyenv install 3.11.0
  ENV_NAME="chains_env"
  pyenv virtualenv 3.11.0 $ENV_NAME
  pyenv activate $ENV_NAME
  pip install --upgrade truss 'pydantic>=2.0.0'
  ```
</Accordion>

To deploy Chains remotely, you also need a
[Baseten account](https://app.baseten.co/signup).
It is handy to export your API key to the current shell session or permanently in your `.bashrc`:

```bash ~/.bashrc theme={"system"}
export BASETEN_API_KEY="nPh8..."
```

If you want to run this example in
[local debugging mode](/development/chain/localdev#test-a-chain-locally), you'll also need to
install chromadb:

```shell  theme={"system"}
pip install chromadb
```

The complete code used in this tutorial can also be found in the
[Chains examples repo](https://github.com/basetenlabs/models/tree/main/truss-chains/examples/rag).

# Overview

Retrieval-augmented generation (RAG) is a multi-model pipeline for generating
context-aware answers from LLMs.

There are a number of ways to build a RAG system. This tutorial shows a minimum
viable implementation with a basic vector store and retrieval function. It's
intended as a starting point to show how Chains helps you flexibly combine model
inference and business logic.

In this tutorial, we'll build a simple RAG pipeline for a hypothetical alumni
matching service for a university. The system:

1. Takes a bio with information about a new graduate
2. Uses a vector database to retrieve semantically similar bios of other alums
3. Uses an LLM to explain why the new graduate should meet the selected alums
4. Returns the writeup from the LLM

Let's dive in!

## Building the Chain

Create a file `rag.py` in a new directory with:

```sh  theme={"system"}
mkdir rag
touch rag/rag.py
cd rag
```

Our RAG Chain is composed of three parts:

* `VectorStore`, a Chainlet that implements a vector database with a retrieval
  function.
* `LLMClient`, a Stub for connecting to a deployed LLM.
* `RAG`, the entrypoint Chainlet that orchestrates the RAG pipeline and
  has `VectorStore` and `LLMClient` as dependencies.

We'll examine these components one by one and then see how they all work
together.

### Vector store Chainlet

A real production RAG system would use a hosted vector database with a massive
number of stored embeddings. For this example, we're using a small local vector
store built with `chromadb` to stand in for a more complex system.

The Chainlet has three parts:

* [`remote_config`](/reference/sdk/chains#remote-configuration), which
  configures a Docker image on deployment with dependencies.
* `__init__()`, which runs once when the Chainlet is spun up, and creates the
  vector database with ten sample bios.
* [`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets), which runs
  each time the Chainlet is called and is the sole public interface for the
  Chainlet.

```python rag/rag.py theme={"system"}
import truss_chains as chains


# Create a Chainlet to serve as our vector database.
class VectorStore(chains.ChainletBase):
    # Add chromadb as a dependency for deployment.
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            pip_requirements=["chromadb"]
        )
    )
    # Runs once when the Chainlet is deployed or scaled up.
    def __init__(self):
        # Import Chainlet-specific dependencies in init, not at the top of
        # the file.
        import chromadb
        self._chroma_client = chromadb.EphemeralClient()
        self._collection = self._chroma_client.create_collection(name="bios")
        # Sample documents are hard-coded for your convenience
        documents = [
            "Angela Martinez is a tech entrepreneur based in San Francisco. As the founder and CEO of a successful AI startup, she is a leading figure in the tech community. Outside of work, Angela enjoys hiking the trails around the Bay Area and volunteering at local animal shelters.",
            "Ravi Patel resides in New York City, where he works as a financial analyst. Known for his keen insight into market trends, Ravi spends his weekends playing chess in Central Park and exploring the city's diverse culinary scene.",
            "Sara Kim is a digital marketing specialist living in San Francisco. She helps brands build their online presence with creative strategies. Outside of work, Sara is passionate about photography and enjoys hiking the trails around the Bay Area.",
            "David O'Connor calls New York City his home and works as a high school teacher. He is dedicated to inspiring the next generation through education. In his free time, David loves running along the Hudson River and participating in local theater productions.",
            "Lena Rossi is an architect based in San Francisco. She designs sustainable and innovative buildings that contribute to the city's skyline. When she's not working, Lena enjoys practicing yoga and exploring art galleries.",
            "Akio Tanaka lives in Tokyo and is a software developer specializing in mobile apps. Akio is an avid gamer and enjoys attending eSports tournaments. He also has a passion for cooking and often experiments with new recipes in his spare time.",
            "Maria Silva is a nurse residing in New York City. She is dedicated to providing compassionate care to her patients. Maria finds joy in gardening and often spends her weekends tending to her vibrant flower beds and vegetable garden.",
            "John Smith is a journalist based in San Francisco. He reports on international politics and has a knack for uncovering compelling stories. Outside of work, John is a history buff who enjoys visiting museums and historical sites.",
            "Aisha Mohammed lives in Tokyo and works as a graphic designer. She creates visually stunning graphics for a variety of clients. Aisha loves to paint and often showcases her artwork in local exhibitions.",
            "Carlos Mendes is an environmental engineer in San Francisco. He is passionate about developing sustainable solutions for urban areas. In his leisure time, Carlos enjoys surfing and participating in beach clean-up initiatives."
        ]
        # Add all documents to the database
        self._collection.add(
            documents=documents,
            ids=[f"id{n}" for n in range(len(documents))]
        )

    # Runs each time the Chainlet is called
    async def run_remote(self, query: str) -> list[str]:
        # This call to includes embedding the query string.
        results = self._collection.query(query_texts=[query], n_results=2)
        if results is None or not results:
            raise ValueError("No bios returned from the query")
        if not results["documents"] or not results["documents"][0]:
            raise ValueError("Bios are empty")
        return results["documents"][0]
```

### LLM inference stub

Now that we can retrieve relevant bios from the vector database, we need to pass
that information to an LLM to generate our final output.

Chains can integrate previously deployed models using a Stub. Like Chainlets,
Stubs implement
[`run_remote()`](/development/chain/concepts#run-remote-chaining-chainlets), but as a call
to the deployed model.

For our LLM, we'll use Phi-3 Mini Instruct, a small-but-mighty open source LLM.

<Card title="Deploy Phi-3 Mini Instruct 4k" icon="rocket" iconType="duotone" href="https://www.baseten.co/library/phi-3-mini-4k-instruct/">
  One-click model deployment from Baseten's model library.
</Card>

While the model is deploying, be sure to note down the models' invocation URL from
the model dashboard for use in the next step.

To use our deployed LLM in the RAG Chain, we define a Stub:

```python rag/rag.py theme={"system"}
class LLMClient(chains.StubBase):
    # Runs each time the Stub is called
    async def run_remote(self, new_bio: str, bios: list[str]) -> str:
        # Use the retrieved bios to augment the prompt -- here's the "A" in RAG!
        prompt = f"""You are matching alumni of a college to help them make connections. Explain why the person described first would want to meet the people selected from the matching database.
        Person you're matching: {new_bio}
        People from database: {" ".join(bios)}"""
        # Call the deployed model.
        resp = await self._remote.predict_async(json_payload={
            "messages": [{"role": "user", "content": prompt}],
            "stream"  : False
        })
        return resp["output"][len(prompt) :].strip()
```

### RAG entrypoint Chainlet

The entrypoint to a Chain is the Chainlet that specifies the public-facing input
and output of the Chain and orchestrates calls to dependencies.

The `__init__` function in this Chainlet takes two new arguments:

* Add dependencies to any Chainlet with
  [`chains.depends()`](/reference/sdk/chains#truss-chains-depends). Only
  Chainlets, not Stubs, need to be added in this fashion.
* Use
  [`chains.depends_context()`](/reference/sdk/chains#truss-chains-depends-context)
  to inject a context object at runtime. This context object is required to
  initialize the `LLMClient` stub.
* Visit your [baseten workspace](https://app.baseten.co/models) to find your
  the URL of the previously deployed Phi-3 model and insert if as value
  for `LLM_URL`.

```python rag/rag.py theme={"system"}
# Insert the URL from the previously deployed Phi-3 model.
LLM_URL = ...

@chains.mark_entrypoint
class RAG(chains.ChainletBase):

    # Runs once when the Chainlet is spun up
    def __init__(
        self,
        # Declare dependency chainlets.
        vector_store: VectorStore = chains.depends(VectorStore),
        context: chains.DeploymentContext = chains.depends_context(),
    ):
        self._vector_store = vector_store
        # The stub needs the context for setting up authentication.
        self._llm = LLMClient.from_url(LLM_URL, context)

    # Runs each time the Chain is called
    async def run_remote(self, new_bio: str) -> str:
        # Use the VectorStore Chainlet for context retrieval.
        bios = await self._vector_store.run_remote(new_bio)
        # Use the LLMClient Stub for augmented generation.
        contacts = await self._llm.run_remote(new_bio, bios)
        return contacts
```

## Testing locally

Because our Chain uses a Stub for the LLM call, we can run the whole Chain
locally without any GPU resources.

Before running the Chainlet, make sure to set your Baseten API key as an
environment variable `BASETEN_API_KEY`.

```python rag/rag.py theme={"system"}
if __name__ == "__main__":
    import os
    import asyncio

    with chains.run_local(
        # This secret is needed even locally, because part of this chain
        # calls the separately deployed Phi-3 model. Only the Chainlets
        # actually run locally.
        secrets={"baseten_chain_api_key": os.environ["BASETEN_API_KEY"]}
    ):
        rag_client = RAG()
        result = asyncio.get_event_loop().run_until_complete(
            rag_client.run_remote(
                """
                Sam just moved to Manhattan for his new job at a large bank.
                In college, he enjoyed building sets for student plays.
                """
            )
        )
        print(result)
```

We can run our Chain locally:

```sh  theme={"system"}
python rag.py
```

After a few moments, we should get a recommendation for why Sam should meet the
alumni selected from the database.

## Deploying to production

Once we're satisfied with our Chain's local behavior, we can deploy it to
production on Baseten. To deploy the Chain, run:

```sh  theme={"system"}
truss chains push rag.py
```

This will deploy our Chain as a development deployment. Once the Chain is
deployed, we can call it from its API endpoint.

You can do this in the console with cURL:

```sh  theme={"system"}
curl -X POST 'https://chain-5wo86nn3.api.baseten.co/development/run_remote' \
    -H "Authorization: Api-Key $BASETEN_API_KEY" \
    -d '{"new_bio": "Sam just moved to Manhattan for his new job at a large bank.In college, he enjoyed building sets for student plays."}'
```

Alternatively, you can also integrate this in a Python application:

```python call_chain.py theme={"system"}
import requests
import os

# Insert the URL from the deployed rag chain. You can get it from the CLI
# output or the status page, e.g.
# "https://chain-6wgeygoq.api.baseten.co/production/run_remote".
RAG_CHAIN_URL = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

if not RAG_CHAIN_URL:
    raise ValueError("Please insert the URL for the RAG chain.")

resp = requests.post(
    RAG_CHAIN_URL,
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={"new_bio": new_bio},
)

print(resp.json())
```

When we're happy with the deployed Chain, we can promote it to production via
the UI or by running:

```sh  theme={"system"}
truss chains push --promote rag.py
```

Once in production, the Chain will have access to full autoscaling settings.
Both the development and production deployments will scale to zero when not in
use.


# Deploy a ComfyUI project
Source: https://docs.baseten.co/examples/comfyui

Deploy your ComfyUI workflow as an API endpoint

<Card title="View example on GitHub" horizontal icon="github" iconType="light" href="https://github.com/basetenlabs/truss-examples/tree/main/comfyui-truss" />

In this example, we'll deploy an **anime style transfer** ComfyUI workflow using truss.
This example won't require any Python code, but there are a few pre-requisites in order to get started.

Pre-Requisites:

1. Convert your ComfyUI workflow to an **API compatible JSON format**. The regular JSON format that is used to export Comfy workflows will not work here.
2. Have a list of the models your workflow requires along with URLs to where each model can be downloaded

## Setup

Clone the truss-examples repository and navigate to the `comfyui-truss` directory

```bash  theme={"system"}
git clone https://github.com/basetenlabs/truss-examples.git
cd truss-examples/comfyui-truss
```

This repository already contains all the files we need to deploy our ComfyUI workflow.
There are just two files we need to modify:

1. `config.yaml`
2. `data/comfy_ui_workflow.json`

## Setting up the `config.yaml`

```yaml  theme={"system"}
build_commands:
- git clone https://github.com/comfyanonymous/ComfyUI.git
- cd ComfyUI && git checkout b1fd26fe9e55163f780bf9e5f56bf9bf5f035c93 && pip install -r requirements.txt
- cd ComfyUI/custom_nodes && git clone https://github.com/LykosAI/ComfyUI-Inference-Core-Nodes --recursive && cd ComfyUI-Inference-Core-Nodes && pip install -e .[cuda12]
- cd ComfyUI/custom_nodes && git clone https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini --recursive && cd ComfyUI-Gemini && pip install -r requirements.txt
- cd ComfyUI/custom_nodes && git clone https://github.com/kijai/ComfyUI-Marigold --recursive && cd ComfyUI-Marigold && pip install -r requirements.txt
- cd ComfyUI/custom_nodes && git clone https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92 --recursive
- cd ComfyUI/custom_nodes && git clone https://github.com/Fannovel16/comfyui_controlnet_aux --recursive && cd comfyui_controlnet_aux && pip install -r requirements.txt
- cd ComfyUI/models/controlnet && wget -O control-lora-canny-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-canny-rank256.safetensors
- cd ComfyUI/models/controlnet && wget -O control-lora-depth-rank256.safetensors https://huggingface.co/stabilityai/control-lora/resolve/main/control-LoRAs-rank256/control-lora-depth-rank256.safetensors
- cd ComfyUI/models/checkpoints && wget -O dreamshaperXL_v21TurboDPMSDE.safetensors https://civitai.com/api/download/models/351306
- cd ComfyUI/models/loras && wget -O StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors https://huggingface.co/artificialguybr/StudioGhibli.Redmond-V2/resolve/main/StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors
environment_variables: {}
external_package_dirs: []
model_metadata: {}
model_name: Anime Style Transfer
python_version: py310
requirements:
  - websocket-client
  - accelerate
  - opencv-python
resources:
  accelerator: H100
  use_gpu: true
secrets: {}
system_packages:
  - wget
  - ffmpeg
  - libgl1-mesa-glx
```

The main part that needs to get filled out is under `build_commands`. Build commands are shell commands that get run during the build stage of the docker image.

In this example, the first two lines clone the ComfyUI repository and install the python requirements.
The latter commands install various custom nodes and models and place them in their respective directory within the ComfyUI repository.

## Modifying `data/comfy_ui_workflow.json`

The `comfy_ui_workflow.json` contains the entire ComfyUI workflow in an API compatible format. This is the workflow that will get executed by the ComfyUI server.

Here is the workflow we will be using for this example.

<Accordion title="Anime Style Transfer Workflow">
  ```json  theme={"system"}
  {
      "1": {
        "inputs": {
          "ckpt_name": "dreamshaperXL_v21TurboDPMSDE.safetensors"
        },
        "class_type": "CheckpointLoaderSimple",
        "_meta": {
          "title": "Load Checkpoint"
        }
      },
      "3": {
        "inputs": {
          "image": "{{input_image}}",
          "upload": "image"
        },
        "class_type": "LoadImage",
        "_meta": {
          "title": "Load Image"
        }
      },
      "4": {
        "inputs": {
          "text": [
            "160",
            0
          ],
          "clip": [
            "154",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "12": {
        "inputs": {
          "strength": 0.8,
          "conditioning": [
            "131",
            0
          ],
          "control_net": [
            "13",
            0
          ],
          "image": [
            "71",
            0
          ]
        },
        "class_type": "ControlNetApply",
        "_meta": {
          "title": "Apply ControlNet"
        }
      },
      "13": {
        "inputs": {
          "control_net_name": "control-lora-canny-rank256.safetensors"
        },
        "class_type": "ControlNetLoader",
        "_meta": {
          "title": "Load ControlNet Model"
        }
      },
      "15": {
        "inputs": {
          "strength": 0.8,
          "conditioning": [
            "12",
            0
          ],
          "control_net": [
            "16",
            0
          ],
          "image": [
            "18",
            0
          ]
        },
        "class_type": "ControlNetApply",
        "_meta": {
          "title": "Apply ControlNet"
        }
      },
      "16": {
        "inputs": {
          "control_net_name": "control-lora-depth-rank256.safetensors"
        },
        "class_type": "ControlNetLoader",
        "_meta": {
          "title": "Load ControlNet Model"
        }
      },
      "18": {
        "inputs": {
          "seed": 995352869972963,
          "denoise_steps": 4,
          "n_repeat": 10,
          "regularizer_strength": 0.02,
          "reduction_method": "median",
          "max_iter": 5,
          "tol": 0.001,
          "invert": true,
          "keep_model_loaded": true,
          "n_repeat_batch_size": 2,
          "use_fp16": true,
          "scheduler": "LCMScheduler",
          "normalize": true,
          "model": "marigold-lcm-v1-0",
          "image": [
            "3",
            0
          ]
        },
        "class_type": "MarigoldDepthEstimation",
        "_meta": {
          "title": "MarigoldDepthEstimation"
        }
      },
      "19": {
        "inputs": {
          "images": [
            "71",
            0
          ]
        },
        "class_type": "PreviewImage",
        "_meta": {
          "title": "Preview Image"
        }
      },
      "20": {
        "inputs": {
          "images": [
            "18",
            0
          ]
        },
        "class_type": "PreviewImage",
        "_meta": {
          "title": "Preview Image"
        }
      },
      "21": {
        "inputs": {
          "seed": 358881677137626,
          "steps": 20,
          "cfg": 7,
          "sampler_name": "dpmpp_2m_sde",
          "scheduler": "karras",
          "denoise": 0.7000000000000001,
          "model": [
            "154",
            0
          ],
          "positive": [
            "15",
            0
          ],
          "negative": [
            "4",
            0
          ],
          "latent_image": [
            "25",
            0
          ]
        },
        "class_type": "KSampler",
        "_meta": {
          "title": "KSampler"
        }
      },
      "25": {
        "inputs": {
          "pixels": [
            "70",
            0
          ],
          "vae": [
            "1",
            2
          ]
        },
        "class_type": "VAEEncode",
        "_meta": {
          "title": "VAE Encode"
        }
      },
      "27": {
        "inputs": {
          "samples": [
            "21",
            0
          ],
          "vae": [
            "1",
            2
          ]
        },
        "class_type": "VAEDecode",
        "_meta": {
          "title": "VAE Decode"
        }
      },
      "70": {
        "inputs": {
          "upscale_method": "lanczos",
          "megapixels": 1,
          "image": [
            "3",
            0
          ]
        },
        "class_type": "ImageScaleToTotalPixels",
        "_meta": {
          "title": "ImageScaleToTotalPixels"
        }
      },
      "71": {
        "inputs": {
          "low_threshold": 50,
          "high_threshold": 150,
          "resolution": 1024,
          "image": [
            "3",
            0
          ]
        },
        "class_type": "CannyEdgePreprocessor",
        "_meta": {
          "title": "Canny Edge"
        }
      },
      "123": {
        "inputs": {
          "images": [
            "27",
            0
          ]
        },
        "class_type": "PreviewImage",
        "_meta": {
          "title": "Preview Image"
        }
      },
      "131": {
        "inputs": {
          "text": [
            "159",
            0
          ],
          "clip": [
            "154",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "152": {
        "inputs": {
          "text": "{{prompt}}"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text_1"
        }
      },
      "154": {
        "inputs": {
          "lora_name": "StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors",
          "strength_model": 0.6,
          "strength_clip": 1,
          "model": [
            "1",
            0
          ],
          "clip": [
            "1",
            1
          ]
        },
        "class_type": "LoraLoader",
        "_meta": {
          "title": "Load LoRA"
        }
      },
      "156": {
        "inputs": {
          "text_1": [
            "152",
            0
          ],
          "text_2": [
            "158",
            0
          ]
        },
        "class_type": "ConcatText_Zho",
        "_meta": {
          "title": "✨ConcatText_Zho"
        }
      },
      "157": {
        "inputs": {
          "text": "StdGBRedmAF,Studio Ghibli,"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text _2"
        }
      },
      "158": {
        "inputs": {
          "text": "looking at viewer, anime artwork, anime style, key visual, vibrant, studio anime, highly detailed"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text _O"
        }
      },
      "159": {
        "inputs": {
          "text_1": [
            "156",
            0
          ],
          "text_2": [
            "157",
            0
          ]
        },
        "class_type": "ConcatText_Zho",
        "_meta": {
          "title": "✨ConcatText_Zho"
        }
      },
      "160": {
        "inputs": {
          "text": "photo, deformed, black and white, realism, disfigured, low contrast"
        },
        "class_type": "Text _O",
        "_meta": {
          "title": "Text _O"
        }
      }
    }
  ```
</Accordion>

**Important:**
If you look at the JSON file above, you'll notice we have templatized a few items using the **`{{handlebars}}`** templating style.

If there are any inputs in your ComfyUI workflow that should be variables such as input prompts, images, etc, you should templatize them using the handlebars format.

In this example workflow, there are two inputs:  **`{{input_image}}`** and **`{{prompt}}`**

When making an API call to this workflow, we will be able to pass in any variable for these two inputs.

## Deploying the Workflow to Baseten

Once you have both your `config.yaml` and `data/comfy_ui_workflow.json` filled out we can deploy this workflow just like any other model on Baseten.

1. `pip install truss --upgrade`
2. `truss push --publish`

## Running Inference

When you deploy the truss, it will spin up a new deployment in your Baseten account. Each deployment will expose a REST API endpoint which we can use to call this workflow.

```python  theme={"system"}
import requests
import os
import base64
from PIL import Image
from io import BytesIO

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
BASE64_PREAMBLE = "data:image/png;base64,"

def pil_to_b64(pil_img):
   buffered = BytesIO()
   pil_img.save(buffered, format="PNG")
   img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
   return img_str

def b64_to_pil(b64_str):
   return Image.open(BytesIO(base64.b64decode(b64_str.replace(BASE64_PREAMBLE, ""))))

values = {
 "prompt": "american Shorthair",
 "input_image": {"type": "image", "data": pil_to_b64(Image.open("/path/to/cat.png"))}
}

resp = requests.post(
   f"https://model-{model_id}.api.baseten.co/production/predict",
   headers={"Authorization": f"Api-Key {baseten_api_key}"},
   json={"workflow_values": values}
)

res = resp.json()
results = res.get("result")

for item in results:
   if item.get("format") == "png":
       data = item.get("data")
       img = b64_to_pil(data)
       img.save(f"pet-style-transfer-1.png")
```

If you recall, we templatized two variables in our workflow: `prompt` and `input_image`. In our API call we can specify the values for these two variables like so:

```json  theme={"system"}
values = {
 "prompt": "Maltipoo",
 "input_image": {"type": "image", "data": pil_to_b64(Image.open("/path/to/dog.png"))}
}
```

If your workflow contains more variables, simply add them to the dictionary above.

The API call returns an image in the form of a base64 string, which we convert to a PNG image.

<Frame>
  <img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=2c74f510d7b1c09d20a6ed1a189ee94f" data-og-width="2400" width="2400" data-og-height="981" height="981" data-path="images/pic-to-anime.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=64cc5319254a073201e30a7eaf8c1711 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=15d8f0484852d14155a190b5a21b7d32 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=155d16198263c8afe5bca85a97437455 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8b53df3d76801809aa7e6fe04feade1c 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1d6892ab6b39a445bdea9f4b9597ba41 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/pic-to-anime.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=130e8c15418e8c78f103c3a3ee453ffc 2500w" />
</Frame>


# Deploy your first model
Source: https://docs.baseten.co/examples/deploy-your-first-model

From model weights to API endpoint

This guide walks through packaging and deploying [Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct), a 3.8B parameter LLM, as a production-ready API endpoint.

We'll cover:

1. **Loading model weights** from Hugging Face
2. **Running inference** on a GPU
3. **Configuring dependencies and infrastructure**
4. **Iterating with live reload development**
5. **Deploying to production with autoscaling**

By the end, you’ll have an AI model running on scalable infrastructure, callable via an API.

## 1. Setup

Before you begin:

1. [Sign up](https://app.baseten.co/signup) or [sign in](https://app.baseten.co/login) to Baseten
2. Generate an [API key](https://app.baseten.co/settings/account/api_keys) and store it securely
3. Install [Truss](https://pypi.org/project/truss/), our model packaging framework

```sh  theme={"system"}
pip install --upgrade truss
```

<Tip>
  New accounts include free credits—this guide should use less than \$1 in GPU
  costs.
</Tip>

***

## 2. Create a Truss

A **Truss** packages your model into a **deployable container** with all dependencies and configurations.

Create a new Truss:

```sh  theme={"system"}
truss init phi-3-mini && cd phi-3-mini
```

When prompted, give your Truss a name like `Phi 3 Mini`.

You should see the following file structure:

```arduino  theme={"system"}
phi-3-mini/
  data/
  model/
    __init__.py
    model.py
  packages/
  config.yaml
```

You'll primarily edit `model/model.py` and `config.yaml`.

***

## 3. Load model weights

[Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) is available on Hugging Face. We’ll **load its weights using** transformers.

Edit `model/model.py`:

```python model/model.py theme={"system"}
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Model:
    def __init__(self, **kwargs):
        self._model = None
        self._tokenizer = None

    def load(self):
        self._model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct",
            device_map="cuda",
            torch_dtype="auto"
        )
        self._tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct"
        )
```

***

## 4. Implement Model Inference

Define how the model processes incoming requests by implementing the `predict()` function:

```python model/model.py theme={"system"}
class Model:
    ...
    def predict(self, request):
        messages = request.pop("messages")
        model_inputs = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._tokenizer(model_inputs, return_tensors="pt").to("cuda")
        with torch.no_grad():
            outputs = self._model.generate(input_ids=inputs["input_ids"], max_length=256)
        return {"output": self._tokenizer.decode(outputs[0], skip_special_tokens=True)}
```

This function:

* ✅ Accepts a list of messages
* ✅ Uses Hugging Face’s tokenizer
* ✅ Generates a response with max 256 tokens

***

## 5. Configure Dependencies & GPU

In `config.yaml`, define the **Python environment** and **compute resources**:

### Set Dependencies

```yaml config.yaml theme={"system"}
requirements:
  - six==1.17.0
  - accelerate==0.30.1
  - einops==0.8.0
  - transformers==4.41.2
  - torch==2.3.0
```

### Allocate a GPU

Phi-3-mini needs \~7.6GB VRAM. A T4 GPU (16GB VRAM) is a good choice.

```yaml config.yaml theme={"system"}
resources:
  accelerator: T4
  use_gpu: true
```

***

## 6. Deploy the Model

### 1. Get Your API Key

🔗 Generate an API Key

You can generate the API key from the Baseten UI. Click on the User icon at the top-right, then click API keys. Save your API-key, because we will use it in the next step.

### 2. Push Your Model to Baseten

```sh  theme={"system"}
truss push
```

Since this is a first-time deployment, `truss` will ask for your API-key and save it for future runs.

Monitor the deployment from [your Baseten dashboard](https://app.baseten.co/models/).

***

## 7. Call the Model API

After the deployment is complete, we can call the model API. First, store the Baseten API key as an environment variable:

```sh  theme={"system"}
export BASETEN_API_KEY=<your_api_key>
```

Below is the client code. Be sure to replace `model_id` from your deployment.

```python  theme={"system"}
import requests
import os

model_id = "your_model_id"
baseten_api_key = os.environ["BASETEN_API_KEY"]

resp = requests.post(
    f"https://model-{model_id}.api.baseten.co/development/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={"messages": ["What is AGI?"]}
)

print(resp.json())
```

***

## 8. Live Reload for Development

Avoid long deploy times when testing changes—use **live reload**:

```sh  theme={"system"}
truss watch
```

* Saves time by **patching only the updated code**
* Skips rebuilding Docker containers
* Keeps the model server running while iterating

Make changes to `model.py`, save, and test the API again.

## 9. Promote to Production

Once you're happy with the model, deploy it to production:

```sh  theme={"system"}
truss push --publish
```

This updates the **API endpoint** from:

* ❌ **Development**: /development/predict
* ✅ **Production**: /production/predict

```python  theme={"system"}
resp = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={
        "messages": [
            {"role": "user", "content": "What is AGI?"}
        ],
    }
)
```

***

## Next Steps

🚀 You’ve successfully packaged, deployed, and invoked an AI model with Truss!

Explore more:

* Learning more about [model serving with Truss](/development/model/overview).
* [Example implementations](https://github.com/basetenlabs/truss-examples) for dozens of open source models.
* [Inference examples](/inference/concepts) and [Baseten integrations](/inference/integrations).
* Using [autoscaling settings](/deployment/autoscaling) to spin up and down multiple GPU replicas.


# Dockerized model
Source: https://docs.baseten.co/examples/docker

Deploy any model in a pre-built Docker container

<Card title="View on GitHub" horizontal icon="github" href="https://github.com/basetenlabs/truss-examples/tree/main/custom-server/infinity-embedding-server" />

In this example, we deploy a dockerized model for [infinity embedding server](https://github.com/michaelfeil/infinity), a high-throughput, low-latency REST API server for serving vector embeddings.

# Setting up the `config.yaml`

To deploy a dockerized model, all you need is a `config.yaml`. It specifies how to build your Docker image, start the server, and manage resources. Let’s break down each section.

## Base Image

Sets the foundational Docker image to a lightweight Python 3.11 environment.

```yaml config.yaml theme={"system"}
base_image:
  image: python:3.11-slim
```

## Docker Server Configuration

Configures the server's startup command, health check endpoints, prediction endpoint, and the port on which the server will run.

```yaml config.yaml theme={"system"}
docker_server:
  start_command: sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) infinity_emb v2 --batch-size 64 --model-id BAAI/bge-small-en-v1.5 --revision main"
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /embeddings
  server_port: 7997
```

## Build Commands (Optional)

Pre-downloads model weights during the build phase to ensure the model is ready at container startup.

```yaml config.yaml theme={"system"}
build_commands: # optional step to download the weights of the model into the image
  - sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) infinity_emb v2 --preload-only --no-model-warmup --model-id BAAI/bge-small-en-v1.5 --revision main"
```

## Configure resources

Note that we need an L4 to run this model.

```yaml config.yaml theme={"system"}
resources:
  accelerator: L4
  use_gpu: true
```

## Requirements

Lists the Python package dependencies required for the infinity embedding server.

```yaml config.yaml theme={"system"}
requirements:
  - infinity-emb[all]==0.0.72
```

## Runtime Settings

Sets the server to handle up to 40 concurrent inferences to manage load efficiently.

```yaml config.yaml theme={"system"}
runtime:
  predict_concurrency: 40
```

## Environment Variables

Defines essential environment variables including the Hugging Face access token, request batch size, queue size limit, and a flag to disable tracking.

```yaml config.yaml theme={"system"}
environment_variables:
  hf_access_token: null
  # constrain api to at most 256 sentences per request, for better load-balancing
  INFINITY_MAX_CLIENT_BATCH_SIZE: 256
  # constrain model to a max backpressure of INFINITY_MAX_CLIENT_BATCH_SIZE * predict_concurrency = 10241 requests
  INFINITY_QUEUE_SIZE: 10241
  DO_NOT_TRACK: 1
```

# Deploy dockerized model

Deploy the model like you would other Trusses, with:

```bash  theme={"system"}
truss push infinity-embedding-server --publish
```


# Image generation
Source: https://docs.baseten.co/examples/image-generation

Building a text-to-image model with Flux Schnell

<Card title="View example on GitHub" horizontal icon="github" iconType="light" href="https://github.com/basetenlabs/truss-examples/tree/main/04-image-generation" />

In this example, we go through a Truss that serves a text-to-image model. We
use Flux Schnell, which is one of the highest performing text-to-image models out
there today.

# Set up imports and torch settings

In this example, we use the Hugging Face diffusers library to build our text-to-image model.

```python model/model.py theme={"system"}
import base64
import random
import logging
from io import BytesIO

import numpy as np
import torch
from diffusers import FluxPipeline
from PIL import Image

logging.basicConfig(level=logging.INFO)
MAX_SEED = np.iinfo(np.int32).max
```

# Define the `Model` class and load function

In the `load` function of the Truss, we implement logic involved in
downloading and setting up the model. For this model, we use the
`FluxPipeline` class in `diffusers` to instantiate our Flux pipeline,
and configure a number of relevant parameters.

See the [diffusers docs](https://huggingface.co/docs/diffusers/index) for details
on all of these parameters.

```python model/model.py theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self.pipe = None
        self.repo_id = "black-forest-labs/FLUX.1-schnell"

    def load(self):
        self.pipe = FluxPipeline.from_pretrained(self.repo_id, torch_dtype=torch.bfloat16).to("cuda")
```

This is a utility function for converting a PIL image to base64.

```python model/model.py theme={"system"}
    def convert_to_b64(self, image: Image) -> str:
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_b64

```

# Define the predict function

The `predict` function contains the actual inference logic. The steps here are:

* Setting up the generation params. These include things like the prompt, image width, image height, number of inference steps, etc.
* Running the Diffusion Pipeline
* Convert the resulting image to base64 and return it

```python model/model.py theme={"system"}
    def predict(self, model_input):
        seed = model_input.get("seed")
        prompt = model_input.get("prompt")
        prompt2 = model_input.get("prompt2")
        max_sequence_length = model_input.get(
            "max_sequence_length", 256
        )  # 256 is max for FLUX.1-schnell
        guidance_scale = model_input.get(
            "guidance_scale", 0.0
        )  # 0.0 is the only value for FLUX.1-schnell
        num_inference_steps = model_input.get(
            "num_inference_steps", 4
        )  # schnell is timestep-distilled
        width = model_input.get("width", 1024)
        height = model_input.get("height", 1024)
        if not math.isclose(guidance_scale, 0.0):
            logging.warning(
                "FLUX.1-schnell does not support guidance_scale other than 0.0"
            )
            guidance_scale = 0.0
        if not seed:
            seed = random.randint(0, MAX_SEED)
        if len(prompt.split()) > max_sequence_length:
            logging.warning(
                "FLUX.1-schnell does not support prompts longer than 256 tokens, truncating"
            )
            tokens = prompt.split()
            prompt = " ".join(tokens[: min(len(tokens), max_sequence_length)])
        generator = torch.Generator().manual_seed(seed)

        image = self.pipe(
            prompt=prompt,
            guidance_scale=guidance_scale,
            max_sequence_length=max_sequence_length,
            num_inference_steps=num_inference_steps,
            width=width,
            height=height,
            output_type="pil",
            generator=generator,
        ).images[0]

        b64_results = self.convert_to_b64(image)
        return {"data": b64_results}

```

# Setting up the `config.yaml`

Running Flux Schnell requires a handful of Python libraries, including
`diffusers`, `transformers`, and others.

```yaml config.yaml theme={"system"}
external_package_dirs: []
model_cache:
  - repo_id: black-forest-labs/FLUX.1-schnell
    allow_patterns:
      - "*.json"
      - "*.safetensors"
    ignore_patterns:
      - "flux1-schnell.safetensors"
model_metadata:
  example_model_input: {"prompt": 'black forest gateau cake spelling out the words "FLUX SCHNELL", tasty, food photography, dynamic shot'}
model_name: Flux.1-schnell
python_version: py311
requirements:
  - git+https://github.com/huggingface/diffusers.git@v0.32.2
  - transformers
  - accelerate
  - sentencepiece
  - protobuf
resources:
  accelerator: H100_40GB
  use_gpu: true
secrets: {}
system_packages:
  - ffmpeg
  - libsm6
  - libxext6
```

## Configuring resources for Flux Schnell

Note that we need an H100 40GB GPU to run this model.

```yaml config.yaml theme={"system"}
resources:
  accelerator: H100_40GB
  use_gpu: true
secrets: {}
```

## System Packages

Running diffusers requires `ffmpeg` and a couple other system
packages.

```yaml config.yaml theme={"system"}
system_packages:
  - ffmpeg
  - libsm6
  - libxext6
```

## Enabling Caching

Flux Schnell is a large model, and downloading it could take several minutes. This means
that the cold start time for this model is long. We can solve that by using our build
caching feature. This moves the model download to the build stage of your model--
caching the model will take about 15 minutes initially but you will get \~20s cold starts
subsequently.

To enable caching, add the following to the config:

```yaml  theme={"system"}
model_cache:
  - repo_id: black-forest-labs/FLUX.1-schnell
    allow_patterns:
      - "*.json"
      - "*.safetensors"
    ignore_patterns:
      - "flux1-schnell.safetensors"
```

# Deploy the model

Deploy the model like you would other Trusses, with:

```bash  theme={"system"}
truss push flux/schnell --publish
```

# Run an inference

Use a Python script to call the model once its deployed and parse its response. We parse the resulting base64-encoded string output into an actual image file: `output_image.jpg`.

```python infer.py theme={"system"}
import httpx
import os
import base64
from PIL import Image
from io import BytesIO

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

# Function used to convert a base64 string to a PIL image
def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str)))

data = {
  "prompt": 'red velvet cake spelling out the words "FLUX SCHNELL", tasty, food photography, dynamic shot'
}

# Call model endpoint
res = httpx.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Get output image
res = res.json()
output = res.get("data")

# Convert the base64 model output to an image
img = b64_to_pil(output)
img.save("output_image.jpg")
```


# Deepseek R1
Source: https://docs.baseten.co/examples/models/deepseek/deepseek-r1

A state-of-the-art 671B-parameter MoE LLM with o1-style reasoning licensed for commercial use

export const DeepSeekIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M21.7896 6.25856C21.5779 6.15323 21.4862 6.35453 21.3629 6.45731C21.3204 6.49043 21.2846 6.53375 21.2487 6.57282C20.9388 6.91002 20.5771 7.13086 20.1046 7.10453C19.4138 7.06546 18.8238 7.28629 18.3021 7.82479C18.1913 7.16058 17.823 6.76478 17.263 6.50997C16.9697 6.37747 16.673 6.24582 16.4672 5.95788C16.3238 5.75318 16.2847 5.5247 16.213 5.30047C16.1672 5.16457 16.1213 5.02612 15.9688 5.00319C15.8022 4.97686 15.7372 5.1187 15.6722 5.23762C15.4114 5.72345 15.3105 6.25856 15.3205 6.80045C15.343 8.02014 15.848 8.99182 16.8522 9.68236C16.9663 9.76135 16.9955 9.84119 16.9597 9.9567C16.8913 10.1945 16.8097 10.4256 16.738 10.6642C16.6922 10.8163 16.6238 10.8485 16.4638 10.7831C15.9232 10.5463 15.4322 10.2061 15.0172 9.78088C14.303 9.07761 13.6581 8.30129 12.8531 7.69314C12.6666 7.55267 12.475 7.41923 12.2789 7.29309C11.4581 6.48024 12.3873 5.81264 12.6022 5.73365C12.8272 5.65041 12.6797 5.36672 11.9531 5.37012C11.2264 5.37351 10.5615 5.62068 9.71397 5.95108C9.58804 6.00027 9.45846 6.03918 9.32648 6.06745C8.53452 5.91535 7.72455 5.88615 6.92403 5.98081C5.35322 6.15918 4.09908 6.91682 3.1766 8.2087C2.06829 9.76135 1.80746 11.5263 2.12662 13.3661C2.46245 15.306 3.4341 16.9122 4.92657 18.1675C6.47487 19.4696 8.25733 20.1075 10.2915 19.9852C11.5264 19.913 12.9022 19.744 14.453 18.4054C14.8447 18.6041 15.2547 18.6831 15.9364 18.7426C16.4613 18.7927 16.9663 18.7171 17.3572 18.6338C17.9696 18.5013 17.9271 17.9229 17.7063 17.8176C15.9105 16.9648 16.3047 17.3122 15.9455 17.0311C16.8588 15.9303 18.2338 14.7871 18.7721 11.083C18.8138 10.7882 18.778 10.6031 18.7721 10.3652C18.7688 10.2209 18.8013 10.1639 18.9638 10.1478C19.4146 10.1001 19.852 9.96309 20.2513 9.74436C21.4146 9.09629 21.8846 8.03289 21.9954 6.75713C22.0121 6.56178 21.9921 6.36133 21.7896 6.25856ZM11.6506 17.7403C9.9098 16.3456 9.06565 15.8861 8.71733 15.9057C8.39066 15.9261 8.44983 16.3057 8.5215 16.5537C8.59649 16.7984 8.69399 16.9665 8.83066 17.1814C8.92565 17.3233 8.99065 17.5348 8.73649 17.6936C8.17567 18.0469 7.20152 17.5747 7.15569 17.5518C6.02154 16.8706 5.0724 15.9719 4.40491 14.7429C3.75992 13.5597 3.38493 12.2908 3.32327 10.936C3.3066 10.6082 3.40076 10.4927 3.72076 10.4332C4.14084 10.3513 4.57126 10.3401 4.9949 10.4001C6.77153 10.6651 8.28317 11.4745 9.55148 12.7562C10.2748 13.4867 10.8223 14.359 11.3864 15.2117C11.9864 16.1172 12.6314 16.9801 13.4531 17.6868C13.7431 17.9348 13.9739 18.1234 14.1956 18.2618C13.5272 18.3383 12.4123 18.3553 11.6506 17.7403ZM12.4839 12.2704C12.4838 12.2282 12.4937 12.1866 12.5129 12.1492C12.532 12.1118 12.5598 12.0797 12.5939 12.0557C12.6279 12.0317 12.6672 12.0165 12.7083 12.0114C12.7494 12.0064 12.7911 12.0116 12.8297 12.0266C12.879 12.0446 12.9216 12.0779 12.9515 12.1217C12.9813 12.1656 12.9971 12.2178 12.9964 12.2712C12.9965 12.3057 12.9899 12.3399 12.9769 12.3717C12.964 12.4036 12.9449 12.4325 12.9208 12.4568C12.8968 12.481 12.8683 12.5002 12.8369 12.5131C12.8055 12.526 12.7719 12.5324 12.7381 12.532C12.7045 12.5321 12.6712 12.5254 12.6402 12.5122C12.6092 12.4991 12.5811 12.4798 12.5575 12.4554C12.5339 12.4311 12.5153 12.4021 12.5028 12.3704C12.4903 12.3386 12.4834 12.3046 12.4839 12.2704ZM15.0755 13.626C14.9089 13.6948 14.743 13.7542 14.5839 13.7619C14.3444 13.7704 14.1095 13.6942 13.9189 13.5461C13.6906 13.3508 13.5272 13.2421 13.4589 12.9023C13.4353 12.7363 13.4398 12.5674 13.4722 12.4029C13.5306 12.1251 13.4656 11.9468 13.2731 11.7854C13.1172 11.6529 12.9181 11.6164 12.6997 11.6164C12.625 11.6119 12.5524 11.5892 12.4881 11.5501C12.3964 11.5043 12.3214 11.3887 12.3931 11.246C12.4164 11.2002 12.5264 11.0881 12.5531 11.0677C12.8497 10.8961 13.1922 10.9522 13.5081 11.0813C13.8014 11.2036 14.0231 11.4278 14.3422 11.7455C14.668 12.1285 14.7272 12.2347 14.913 12.5218C15.0597 12.7469 15.193 12.9779 15.2839 13.2421C15.3397 13.4077 15.268 13.5427 15.0755 13.626Z" fill="#4D6BFE" />
</svg>} horizontal />;

<DeepSeekIconCard title="Deploy Deepseek R1" href="https://www.baseten.co/talk-to-us/deepseek/" />

# Example usage

DeepSeek-R1 is optimized using SGLang and uses an OpenAI-compatible API endpoint.

## Input

```python  theme={"system"}
import httpx
import os

MODEL_ID = "abcd1234"  # Replace with your model ID
DEPLOYMENT_ID = "abcd1234"  # [Optional] Replace with your deployment ID
API_KEY = os.environ["BASETEN_API_KEY"]

resp = httpx.post(
    f"https://model-{MODEL_ID}.api.baseten.co/environments/production/sync/v1/chat/completions",
    headers={"Authorization": f"Api-Key {API_KEY}"},
    json={
        "model": "deepseek_v3",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": "What weighs more, a pound of bricks or a pound of feathers?"},
        ],
        "max_tokens": 1024,
    },
    timeout=None
)

print(resp.json())
```

## Output

```json  theme={"system"}
{
  "id": "8456fe51db3548789f199cfb8c8efd35",
  "object": "text_completion",
  "created": 1735236968,
  "model": "/models/deepseek_r1",
  "choices": [
    {
      "index": 0,
      "text": "Let's think through this step by step...",
      "logprobs": null,
      "finish_reason": "stop",
      "matched_stop": 1
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "total_tokens": 240,
    "completion_tokens": 226,
    "prompt_tokens_details": null
  }
}
```


# DeepSeek-R1 Qwen 7B
Source: https://docs.baseten.co/examples/models/deepseek/deepseek-r1-qwen-7b

Qwen 7B fine-tuned for CoT reasoning capabilities with DeepSeek R1

export const DeepSeekIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M21.7896 6.25856C21.5779 6.15323 21.4862 6.35453 21.3629 6.45731C21.3204 6.49043 21.2846 6.53375 21.2487 6.57282C20.9388 6.91002 20.5771 7.13086 20.1046 7.10453C19.4138 7.06546 18.8238 7.28629 18.3021 7.82479C18.1913 7.16058 17.823 6.76478 17.263 6.50997C16.9697 6.37747 16.673 6.24582 16.4672 5.95788C16.3238 5.75318 16.2847 5.5247 16.213 5.30047C16.1672 5.16457 16.1213 5.02612 15.9688 5.00319C15.8022 4.97686 15.7372 5.1187 15.6722 5.23762C15.4114 5.72345 15.3105 6.25856 15.3205 6.80045C15.343 8.02014 15.848 8.99182 16.8522 9.68236C16.9663 9.76135 16.9955 9.84119 16.9597 9.9567C16.8913 10.1945 16.8097 10.4256 16.738 10.6642C16.6922 10.8163 16.6238 10.8485 16.4638 10.7831C15.9232 10.5463 15.4322 10.2061 15.0172 9.78088C14.303 9.07761 13.6581 8.30129 12.8531 7.69314C12.6666 7.55267 12.475 7.41923 12.2789 7.29309C11.4581 6.48024 12.3873 5.81264 12.6022 5.73365C12.8272 5.65041 12.6797 5.36672 11.9531 5.37012C11.2264 5.37351 10.5615 5.62068 9.71397 5.95108C9.58804 6.00027 9.45846 6.03918 9.32648 6.06745C8.53452 5.91535 7.72455 5.88615 6.92403 5.98081C5.35322 6.15918 4.09908 6.91682 3.1766 8.2087C2.06829 9.76135 1.80746 11.5263 2.12662 13.3661C2.46245 15.306 3.4341 16.9122 4.92657 18.1675C6.47487 19.4696 8.25733 20.1075 10.2915 19.9852C11.5264 19.913 12.9022 19.744 14.453 18.4054C14.8447 18.6041 15.2547 18.6831 15.9364 18.7426C16.4613 18.7927 16.9663 18.7171 17.3572 18.6338C17.9696 18.5013 17.9271 17.9229 17.7063 17.8176C15.9105 16.9648 16.3047 17.3122 15.9455 17.0311C16.8588 15.9303 18.2338 14.7871 18.7721 11.083C18.8138 10.7882 18.778 10.6031 18.7721 10.3652C18.7688 10.2209 18.8013 10.1639 18.9638 10.1478C19.4146 10.1001 19.852 9.96309 20.2513 9.74436C21.4146 9.09629 21.8846 8.03289 21.9954 6.75713C22.0121 6.56178 21.9921 6.36133 21.7896 6.25856ZM11.6506 17.7403C9.9098 16.3456 9.06565 15.8861 8.71733 15.9057C8.39066 15.9261 8.44983 16.3057 8.5215 16.5537C8.59649 16.7984 8.69399 16.9665 8.83066 17.1814C8.92565 17.3233 8.99065 17.5348 8.73649 17.6936C8.17567 18.0469 7.20152 17.5747 7.15569 17.5518C6.02154 16.8706 5.0724 15.9719 4.40491 14.7429C3.75992 13.5597 3.38493 12.2908 3.32327 10.936C3.3066 10.6082 3.40076 10.4927 3.72076 10.4332C4.14084 10.3513 4.57126 10.3401 4.9949 10.4001C6.77153 10.6651 8.28317 11.4745 9.55148 12.7562C10.2748 13.4867 10.8223 14.359 11.3864 15.2117C11.9864 16.1172 12.6314 16.9801 13.4531 17.6868C13.7431 17.9348 13.9739 18.1234 14.1956 18.2618C13.5272 18.3383 12.4123 18.3553 11.6506 17.7403ZM12.4839 12.2704C12.4838 12.2282 12.4937 12.1866 12.5129 12.1492C12.532 12.1118 12.5598 12.0797 12.5939 12.0557C12.6279 12.0317 12.6672 12.0165 12.7083 12.0114C12.7494 12.0064 12.7911 12.0116 12.8297 12.0266C12.879 12.0446 12.9216 12.0779 12.9515 12.1217C12.9813 12.1656 12.9971 12.2178 12.9964 12.2712C12.9965 12.3057 12.9899 12.3399 12.9769 12.3717C12.964 12.4036 12.9449 12.4325 12.9208 12.4568C12.8968 12.481 12.8683 12.5002 12.8369 12.5131C12.8055 12.526 12.7719 12.5324 12.7381 12.532C12.7045 12.5321 12.6712 12.5254 12.6402 12.5122C12.6092 12.4991 12.5811 12.4798 12.5575 12.4554C12.5339 12.4311 12.5153 12.4021 12.5028 12.3704C12.4903 12.3386 12.4834 12.3046 12.4839 12.2704ZM15.0755 13.626C14.9089 13.6948 14.743 13.7542 14.5839 13.7619C14.3444 13.7704 14.1095 13.6942 13.9189 13.5461C13.6906 13.3508 13.5272 13.2421 13.4589 12.9023C13.4353 12.7363 13.4398 12.5674 13.4722 12.4029C13.5306 12.1251 13.4656 11.9468 13.2731 11.7854C13.1172 11.6529 12.9181 11.6164 12.6997 11.6164C12.625 11.6119 12.5524 11.5892 12.4881 11.5501C12.3964 11.5043 12.3214 11.3887 12.3931 11.246C12.4164 11.2002 12.5264 11.0881 12.5531 11.0677C12.8497 10.8961 13.1922 10.9522 13.5081 11.0813C13.8014 11.2036 14.0231 11.4278 14.3422 11.7455C14.668 12.1285 14.7272 12.2347 14.913 12.5218C15.0597 12.7469 15.193 12.9779 15.2839 13.2421C15.3397 13.4077 15.268 13.5427 15.0755 13.626Z" fill="#4D6BFE" />
</svg>} horizontal />;

<DeepSeekIconCard title="Deploy DeepSeek-R1 Qwen 7B" href="https://app.baseten.co/deploy/deepseek-r1-qwen-7b" />

# Example usage

The fine-tuned version of Qwen is OpenAI compatible and can be called using the OpenAI client.

```python  theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "user", "content": "Which weighs more, a pound of bricks or a pound of feathers?"},
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

# JSON output

```json  theme={"system"}
["streaming", "output", "text"]
```


# Flux-Schnell
Source: https://docs.baseten.co/examples/models/flux/flux-schnell

Flux-Schnell is a state-of-the-art image generation model

export const BFLIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 20.683L12.01 2.5L24 20.683H21.767L12.009 5.878L3.471 18.806H15.593L16.832 20.683H0Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M8.069 16.724L10.142 13.609L12.216 16.724H8.069ZM18.24 20.683L12.572 11.976H14.749L20.435 20.683H18.24ZM19.74 11.676L21.87 8.48602L24 11.676H19.74Z" fill="black" />
</svg>} horizontal />;

<BFLIconCard title="Deploy Flux-Schnell" href="https://app.baseten.co/deploy/flux.1-schnell" />

## Example usage

The model accepts a `prompt` which is some text describing the image you want to generate. The output images tend to get better as you add more descriptive words to the prompt.

The output JSON object contains a key called `data` which represents the generated image as a base64 string.

### Input

```python  theme={"system"}
import httpx
import os
import base64
from PIL import Image
from io import BytesIO
# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
# Function used to convert a base64 string to a PIL image
def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str)))
data = {
  "prompt": 'red velvet cake spelling out the words "FLUX SCHNELL", tasty, food photography, dynamic shot'
}
# Call model endpoint
res = httpx.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)
# Get output image
res = res.json()
output = res.get("data")
# Convert the base64 model output to an image
img = b64_to_pil(output)
img.save("output_image.jpg")
```

### JSON output

```json  theme={"system"}
{
  "output": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAA..."
}
```


# Gemma 3 27B IT
Source: https://docs.baseten.co/examples/models/gemma/gemma-3-27b-it

Instruct-tuned open model by Google with excellent ELO/size tradeoff and vision capabilities

export const GoogleIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M23 12.245C23 11.34 22.925 10.68 22.764 9.995H12.224V14.078H18.41C18.286 15.092 17.613 16.62 16.116 17.647L16.095 17.783L19.427 20.313L19.657 20.335C21.779 18.417 23 15.593 23 12.245Z" fill="#4285F4" />
<path d="M12.225 23C15.255 23 17.799 22.022 19.658 20.335L16.116 17.647C15.168 18.295 13.896 18.747 12.225 18.747C10.8164 18.7471 9.44319 18.3063 8.29791 17.4863C7.15263 16.6664 6.29277 15.5084 5.83899 14.175L5.70699 14.186L2.24199 16.814L2.19699 16.938C4.04299 20.531 7.83499 23 12.225 23Z" fill="#34A853" />
<path d="M5.84 14.175C5.59404 13.4761 5.46662 12.7409 5.463 12C5.463 11.242 5.601 10.509 5.824 9.825L5.818 9.678L2.31 7.008L2.195 7.062C1.41079 8.58997 1.00119 10.2825 1 12C1 13.772 1.436 15.447 2.197 16.938L5.84 14.175Z" fill="#FBBC05" />
<path d="M12.225 5.253C14.333 5.253 15.754 6.145 16.565 6.891L19.732 3.86C17.787 2.088 15.255 1 12.225 1C7.83399 1 4.04299 3.469 2.19699 7.062L5.82699 9.825C6.28468 8.49166 7.14717 7.33445 8.29413 6.51484C9.44108 5.69522 10.8153 5.25409 12.225 5.253Z" fill="#EB4335" />
</svg>} horizontal />;

<GoogleIconCard title="Deploy Gemma 3 27B IT" href="https://app.baseten.co/deploy/gemma_3_27b_it" />

# Example usage

Gemma 3 is an OpenAI-compatible model and can be called using the OpenAI SDK in any language.

```python  theme={"system"}
from openai import OpenAI
import os

model_url = "" # Copy in from API pane in Baseten model dashboard

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url=model_url
)

# Chat completion
response_chat = client.chat.completions.create(
    model="",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://picsum.photos/id/237/200/300",
                },
            },
        ],
    }],
    temperature=0.3,
    max_tokens=512,
)
print(response_chat)
```

**JSON Output**

```json  theme={"system"}
{
  "id": "143",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "[Model output here]",
        "role": "assistant",
        "audio": null,
        "function_call": null,
        "tool_calls": null
      }
    }
  ],
  "created": 1741224586,
  "model": "",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": null,
  "usage": {
    "completion_tokens": 145,
    "prompt_tokens": 38,
    "total_tokens": 183,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  }
}
```


# Kokoro
Source: https://docs.baseten.co/examples/models/kokoro/kokoro

Kokoro is a frontier TTS model for its size of 82 million parameters (text in/audio out).

export const LibraryIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M3.33334 16.25C3.33334 15.6975 3.55283 15.1676 3.94353 14.7769C4.33423 14.3862 4.86413 14.1667 5.41667 14.1667H16.6667" stroke="#8999AC" stroke-width="1.33333" stroke-linecap="round" stroke-linejoin="round" />
<path d="M5.41667 1.66669H16.6667V18.3334H5.41667C4.86413 18.3334 4.33423 18.1139 3.94353 17.7232C3.55283 17.3325 3.33334 16.8026 3.33334 16.25V3.75002C3.33334 3.19749 3.55283 2.66758 3.94353 2.27688C4.33423 1.88618 4.86413 1.66669 5.41667 1.66669V1.66669Z" stroke="#8999AC" stroke-width="1.33333" stroke-linecap="round" stroke-linejoin="round" />
</svg>} horizontal />;

<LibraryIconCard title="Deploy Kokoro" href="https://app.baseten.co/deploy/kokoro" />

## Example usage

Kokoro uses the following request and response format:

```
request:
{"text": "Hello", "voice": "af", "speed": 1.0}

text: str = defaults to "Hi, I'm kokoro"
voice: str = defaults to "af", available options: "af", "af_bella", "af_sarah", "am_adam", "am_michael", "bf_emma", "bf_isabella", "bm_george", "bm_lewis", "af_nicole", "af_sky"
speed: float = defaults to 1.0. The speed of the audio generated

response:
{"base64": "base64 encoded bytestring"}
```

```python  theme={"system"}
import httpx
import base64

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

with httpx.Client() as client:
    # Make the API request
    resp = client.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {API_KEY}"},
        json={"text": "Hello world", "voice": "af", "speed": 1.0},
        timeout=None,
    )

# Get the base64 encoded audio
response_data = resp.json()
audio_base64 = response_data["base64"]

# Decode the base64 string
audio_bytes = base64.b64decode(audio_base64)

# Write to a WAV file
with open("output.wav", "wb") as f:
    f.write(audio_bytes)

print("Audio saved to output.wav")
```

**JSON Output**

```json  theme={"system"}
null
```


# Llama 3.3 70B Instruct
Source: https://docs.baseten.co/examples/models/llama/llama-3.3-70B-instruct

Llama 3.3 70B Instruct is a large language model that is optimized for instruction following.

export const MetaIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M4.13523 13.5079C4.13523 10.377 5.77224 7.10995 7.69395 7.10995C8.76157 7.10995 9.61566 7.72251 10.968 9.56021C9.68683 11.466 8.90391 12.623 8.90391 12.623C7.19573 15.2094 6.62633 15.7539 5.70107 15.7539C4.7758 15.822 4.13523 15.0052 4.13523 13.5079ZM15.3096 12.3508L14.0996 10.445C13.8149 9.96859 13.4591 9.49215 13.1744 9.08377C14.242 7.51832 15.0961 6.70157 16.1637 6.70157C18.2989 6.70157 20.0071 9.7644 20.0071 13.5759C20.0071 15.0052 19.5089 15.822 18.5125 15.822C17.516 15.822 17.1601 15.2094 15.3096 12.3508ZM12.2491 7.72251C10.6833 5.74869 9.33096 5 7.76512 5C4.4911 5 2 9.15183 2 13.5079C2 16.2304 3.35231 17.9319 5.62989 17.9319C7.2669 17.9319 8.40569 17.1832 10.5409 13.644C10.5409 13.644 11.395 12.1466 12.0356 11.1257C12.2491 11.466 12.4626 11.8063 12.6762 12.2147L13.6726 13.8482C15.5943 16.9791 16.6619 18 18.5836 18C20.79 18 22 16.2304 22 13.4398C21.9288 8.81152 19.3665 5 16.3061 5C14.669 5 13.3879 6.22513 12.2491 7.72251Z" fill="#0081FB" />
</svg>} horizontal />;

<MetaIconCard title="Deploy Llama 3.3 70B Instruct" href="https://app.baseten.co/deploy/llama-3-3-70b-instruct" />

# Example usage

Llama is OpenAI compatible and can be called using the OpenAI client.

```python  theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What was the role of Llamas in the Inca empire?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

**JSON Output**

```json  theme={"system"}
["streaming", "output", "text"]
```


# MARS6
Source: https://docs.baseten.co/examples/models/mars/MARS6

MARS6 is a frontier text-to-speech model by CAMB.AI with voice/prosody cloning capabilities in 10 languages. MARS6 must be licensed for commercial use, we can help!

export const MarsIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_631_10869)">
<path fill-rule="evenodd" clip-rule="evenodd" d="M8.63156 18.1049L8.57257 18.2142C8.49832 18.3766 8.47037 18.5619 8.50142 18.7515C8.58658 19.2656 9.07928 19.6143 9.60131 19.53C9.86988 19.487 10.0939 19.3379 10.2364 19.1336L10.3133 19.0025L10.8178 18.1398C10.8208 18.1325 10.8243 18.1256 10.8274 18.1183C10.8588 18.0512 10.8968 17.9881 10.9405 17.9296L11.846 16.3821L12.7455 17.9193C12.7926 17.9812 12.8332 18.0478 12.8669 18.1187C12.872 18.1299 12.8768 18.1411 12.8817 18.1523L13.3736 18.9931L13.4614 19.1431C13.6042 19.343 13.8256 19.4879 14.0899 19.5305C14.6123 19.6143 15.1046 19.2656 15.1902 18.752C15.2226 18.5568 15.1915 18.3654 15.1116 18.1991L15.0692 18.1205L13.7435 15.6581L13.5976 15.3873L13.5251 15.2528C13.3526 15.0061 13.1254 14.7988 12.8603 14.6488C12.562 14.4798 12.2155 14.3831 11.8469 14.3831C11.4773 14.3831 11.131 14.4803 10.8322 14.6496C10.5636 14.8018 10.3338 15.0125 10.1608 15.2643L9.95551 15.6457L8.63109 18.1062L8.63156 18.1049Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M1.72147 19.175L10.1396 9.01879C10.168 8.98181 10.1977 8.94614 10.2287 8.91132C10.6219 8.46725 11.201 8.18611 11.8471 8.18611C12.4935 8.18611 13.0732 8.46769 13.4668 8.91259C13.4969 8.94656 13.5258 8.98138 13.5533 9.01749L13.8638 9.39191L21.9453 19.1419L22.0374 19.2532C22.212 19.4337 22.4585 19.5468 22.7319 19.5468C23.2609 19.5468 23.6898 19.1247 23.6898 18.6041C23.6898 18.4142 23.633 18.2375 23.5347 18.0896L23.4523 17.9829L16.7682 9.31368L15.4 7.53915L15.2607 7.35903L13.8633 5.54626L13.5043 5.0807C13.4873 5.0605 13.4703 5.04073 13.4528 5.02095C13.0596 4.58463 12.4857 4.30951 11.8462 4.30951C11.2068 4.30951 10.6328 4.58463 10.2396 5.02095C10.2222 5.03986 10.2057 5.05963 10.189 5.07941L10.0846 5.21483L9.82908 5.54583L8.42857 7.36247L8.29277 7.53872L6.92165 9.31711L0.255963 17.9623L0.140661 18.1119C0.0515526 18.255 0 18.4235 0 18.6036C0 19.1243 0.428953 19.5464 0.957925 19.5464C1.24666 19.5464 1.50525 19.4209 1.68128 19.2223L1.72059 19.175H1.72147Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M10.0556 10.4893L4.29329 17.9627L4.17751 18.1127C4.08841 18.2558 4.03729 18.4243 4.03729 18.6045C4.03729 19.1251 4.46626 19.5472 4.99523 19.5472C5.28396 19.5472 5.54298 19.4212 5.71859 19.2227L5.75658 19.177L10.2649 13.7379C10.6572 13.3158 11.2219 13.0505 11.8492 13.0505C12.4769 13.0505 13.0417 13.3158 13.4339 13.7383L17.9138 19.1427L18.0055 19.2535C18.1803 19.4346 18.427 19.5472 18.7006 19.5472C19.2294 19.5472 19.6585 19.1251 19.6585 18.6045C19.6585 18.4149 19.6016 18.2378 19.5033 18.0903L19.4208 17.9834L13.4693 10.2641C13.4562 10.2495 13.4436 10.2353 13.43 10.2211C13.0377 9.80067 12.4747 9.53717 11.8492 9.53717C11.2219 9.53717 10.6572 9.80196 10.2649 10.2241C10.2531 10.237 10.2413 10.2499 10.2295 10.2632L10.0556 10.4893Z" fill="black" />
</g>
<defs>
<clipPath id="clip0_631_10869">
<rect width="24" height="16" fill="white" transform="translate(0 4)" />
</clipPath>
</defs>
</svg>} horizontal />;

<MarsIconCard title="Deploy MARS6" href="https://app.baseten.co/deploy/mars-6r-tts" />

## Example usage

This model requires at least four inputs:

1. `text`: The input text that needs to be spoken
2. `audio_ref`: An audio file containing the audio of a single person
3. `ref_text`: What is spoken in audio\_ref
4. `language`: The language code for the target language

The model will try to output an audio stream containing the speech in the reference audio's style. The output is by default an HTTP1.1 chunked encoding response of an encoded audio file using an ADTS AAC stream, but can be configured to stream using flac format, or to not stream at all and return the entire response as a base64 encoded flac file.

```
data = {"text": "The quick brown fox jumps over the lazy dog",
        "audio_ref": encoded_str,
        "ref_text": prompt_txt,
        "language": 'en-us', # Target language, in this case english.
        # "top_p": 0.7, # Optionally specify a top_p (default 0.7)
        # "temperature": 0.7, # Optionally specify a temperature (default 0.7)
        # "chunk_length": 200, # Optional text chunk length for splitting long pieces of input text. Default 200
        # "max_new_tokens": 0, # Optional limit on max number of new tokens, default is zero (unlimited)
        # "repetition_penalty": 1.5 # Optional rep penalty, default 1.5
}
```

## Input

```python  theme={"system"}
import base64
import time
import torchaudio
import requests
import IPython.display as ipd
import librosa, librosa.display
import torch
import io
from torchaudio.io import StreamReader

# Step 1: set endpoint url and api key:
url = "<YOUR PREDICTION ENDPOINT>"
headers = {"Authorization": "Api-Key <YOUR API KEY>"}

# Step 2: pick reference audio to clone, encode it as base64
file_path = "ref_debug.flac"  # any valid audio filepath, ideally between 6s-90s.
wav, sr = librosa.load(file_path, sr=None, mono=True, offset=0, duration=5)
io_data = io.BytesIO()
torchaudio.save(io_data, torch.from_numpy(wav)[None], sample_rate=sr, format="wav")
io_data.seek(0)
encoded_data = base64.b64encode(io_data.read())
encoded_str = encoded_data.decode("utf-8")
# OPTIONAL: specify the transcript of the reference/prompt (slightly speeds up inference, and may make it sound a bit better).
prompt_txt = None  # if unspecified, can be left as None

# Step 3: define other inference settings:
data = {
    "text": "The quick brown fox jumps over the lazy dog",
    "audio_ref": encoded_str,
    "ref_text": prompt_txt,
    "language": "en-us",  # Target language, in this case english.
    # "top_p": 0.7, # Optionally specify a top_p (default 0.7)
    # "temperature": 0.7, # Optionally specify a temperature (default 0.7)
    # "chunk_length": 200, # Optional text chunk length for splitting long pieces of input text. Default 200
    # "max_new_tokens": 0, # Optional limit on max number of new tokens, default is zero (unlimited)
    # "repetition_penalty": 1.5 # Optional rep penalty, default 1.5
    # stream: bool = True # whether to stream the response back as an HTTP1.1 chunked encoding response, or run to completion and return the base64 encoded file.
    # stream_format: str = "adts" # 'adts' or 'flac' for stream format. Default 'adts'
}

st = time.time()


class UnseekableWrapper:
    def __init__(self, obj):
        self.obj = obj

    def read(self, n):
        return self.obj.read(n)


# Step 4: Send the POST request (note the first request might be a bit slow, but following requests should be fast)
response = requests.post(url, headers=headers, json=data, stream=True, timeout=300)
streamer = StreamReader(UnseekableWrapper(response.raw))
streamer.add_basic_audio_stream(
    11025, buffer_chunk_size=3, sample_rate=44100, num_channels=1
)

# Step 4.1: check the header format of the returned stream response
for i in range(streamer.num_src_streams):
    print(streamer.get_src_stream_info(i))

# Step 5: stream the response back and decode it on-the-fly
audio_samples = []
for chunks in streamer.stream():
    audio_chunk = chunks[0]
    audio_samples.append(
        audio_chunk._elem.squeeze()
    )  # this is now just a (T,) float waveform, however you can set your own output format bove.
    print(
        f"Playing audio chunk of size {audio_chunk._elem.squeeze().shape} at {time.time() - st:.2f}s."
    )
    # If you wish, you can also play each chunk as you receive it, e.g. using IPython:
    # ipd.display(ipd.Audio(audio_chunk._elem.squeeze().numpy(), rate=44100, autoplay=True))

# Step 6: concatenate all the audio chunks and play the full audio (if you didn't play them on the fly above)
final_full_audio = torch.concat(audio_samples, dim=0)  # (T,) float waveform @ 44.1kHz
# ipd.display(ipd.Audio(final_full_audio.numpy(), rate=44100))
```

## Output

```json  theme={"system"}
{
    "reuslt": "base64 encoded audio data",\
}
```


# All MPNet Base V2
Source: https://docs.baseten.co/examples/models/microsoft/all-mpnet-base-v2

A text embedding model with a context window of 384 tokens and a dimensionality of 768 values.

export const MicrosoftIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M11.49 2H2V11.492H11.492V2H11.49Z" fill="#F25022" />
<path d="M22 2H12.508V11.492H22V2Z" fill="#7FBA00" />
<path d="M11.49 12.508H2V22H11.492V12.508H11.49Z" fill="#00A4EF" />
<path d="M22 12.508H12.508V22H22V12.508Z" fill="#FFB900" />
</svg>} horizontal />;

<MicrosoftIconCard title="Deploy All MPNet Base V2" href="https://app.baseten.co/deploy/all-mpnet-base-v2" />

## Example usage

This model takes a list of strings and returns a list of embeddings, where each embedding is a list of 768 floating-point number representing the semantic text embedding of the associated string.

Strings can be up to 384 tokens in length (approximately 280 words). If the strings are longer, they'll be truncated before being run through the embedding model.

```python  theme={"system"}
import requests
import os

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

data = {
    "text": ["I want to eat pasta", "I want to eat pizza"],
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Print the output of the model
print(res.json())
```

## JSON output

```json  theme={"system"}
[
  [0.2593194842338562, "...", -1.4059709310531616],
  [0.11028853803873062, "...", -0.9492666125297546]
]
```


# Nomic Embed v1.5
Source: https://docs.baseten.co/examples/models/nomic/nomic-embed-v1-5

SOTA text embedding model with variable dimensionality — outperforms OpenAI text-embedding-ada-002 and text-embedding-3-small models.

export const NomicIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_603_2944)">
<path d="M2.96725 16.2278V3.5H3.69541V20.4705H2.96725L0.782782 7.74262V20.4705H0.0546265V3.5H0.782782L2.96725 16.2278Z" fill="black" />
<path d="M7.40443 19.7326C7.60164 19.7326 7.76851 19.6635 7.90504 19.5251C8.05673 19.3867 8.13259 19.21 8.13259 18.9948V4.97569C8.13259 4.77586 8.05673 4.60677 7.90504 4.46842C7.76851 4.31471 7.60164 4.23785 7.40443 4.23785C7.19205 4.23785 7.0176 4.31471 6.88107 4.46842C6.74454 4.60677 6.67628 4.77586 6.67628 4.97569V18.9948C6.67628 19.21 6.74454 19.3867 6.88107 19.5251C7.0176 19.6635 7.19205 19.7326 7.40443 19.7326ZM7.40443 20.4705C6.99485 20.4705 6.64594 20.3321 6.3577 20.0554C6.08465 19.7633 5.94812 19.4099 5.94812 18.9948V4.97569C5.94812 4.57603 6.08465 4.23016 6.3577 3.9381C6.64594 3.64603 6.99485 3.5 7.40443 3.5C7.79885 3.5 8.14017 3.64603 8.4284 3.9381C8.71663 4.23016 8.86074 4.57603 8.86074 4.97569V18.9948C8.86074 19.4099 8.71663 19.7633 8.4284 20.0554C8.14017 20.3321 7.79885 20.4705 7.40443 20.4705Z" fill="black" />
<path d="M15.3003 3.5H16.0285V20.4705H15.3003V6.45139L13.48 13.8299L11.6596 6.45139V20.4705H10.9314V3.5H11.6596L13.48 10.8785L15.3003 3.5Z" fill="black" />
<path d="M18.1902 20.4705V3.5H18.9184V20.4705H18.1902Z" fill="black" />
<path d="M22.5365 20.4705C22.1268 20.4705 21.7779 20.3321 21.4897 20.0554C21.2166 19.7633 21.0802 19.4099 21.0802 18.9948V4.97569C21.0802 4.57603 21.2166 4.23016 21.4897 3.9381C21.7779 3.64603 22.1268 3.5 22.5365 3.5C22.9308 3.5 23.2722 3.64603 23.5604 3.9381C23.8487 4.23016 23.9928 4.57603 23.9928 4.97569V6.45139H23.2646V4.97569C23.2646 4.77586 23.1887 4.60677 23.037 4.46842C22.9004 4.31471 22.7336 4.23785 22.5365 4.23785C22.3241 4.23785 22.1496 4.31471 22.013 4.46842C21.8765 4.60677 21.8083 4.77586 21.8083 4.97569V18.9948C21.8083 19.21 21.8765 19.3867 22.013 19.5251C22.1496 19.6635 22.3241 19.7326 22.5365 19.7326C22.7336 19.7326 22.9004 19.6635 23.037 19.5251C23.1887 19.3867 23.2646 19.21 23.2646 18.9948V17.5191H23.9928V18.9948C23.9928 19.4099 23.8487 19.7633 23.5604 20.0554C23.2722 20.3321 22.9308 20.4705 22.5365 20.4705Z" fill="black" />
</g>
<defs>
<clipPath id="clip0_603_2944">
<rect width="24" height="17" fill="white" transform="translate(0 3.5)" />
</clipPath>
</defs>
</svg>} horizontal />;

<NomicIconCard title="Deploy Nomic Embed v1.5" href="https://app.baseten.co/deploy/nomic_embed_v1_5?_gl=1*dnaf1c*_gcl_au*MTYzMTk5MDI1OS4xNzM2NjM4OTMw" />

## Example usage

Nomic Embed v1.5 is a state of the art text embedding model with two special features:

* You can choose whether to optimize the embeddings for retrieval, search, clustering, or classification.
* You can trade off between cost and accuracy by choosing your own dimensionality thanks to Matryoshka Representation Learning.

Nomic Embed v1.5 takes the following parameters:

* `texts` the strings to embed.
* `task_type` the task to optimize the embedding for. Can be `search_document` (default), `search_query`, `clustering`, or `classification`.
* `dimensionality` the size of each output vector, any integer between `64` and `768` (default).

This code sample demonstrates embedding a set of sentences for retrieval with a dimensionality of 512.

```python  theme={"system"}
import requests
import os

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

data = {
    "texts": ["I want to eat pasta", "I want to eat pizza"],
    "task_type": "search_document",
    "dimensionality": 512
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Print the output of the model
print(res.json())
```

## JSON output

```json  theme={"system"}
[
  [-0.03811980411410332, "...", -0.023593541234731674],
  [-0.042617011815309525, "...", -0.0191882885992527]
]
```


# Overview
Source: https://docs.baseten.co/examples/models/overview

Browse our library of open source models that are ready to deploy behind an API endpoint in seconds.

export const QwenIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.604 1.33998C12.997 2.02998 13.388 2.72198 13.778 3.41498C13.7938 3.4427 13.8166 3.46573 13.8442 3.48171C13.8718 3.4977 13.9031 3.50608 13.935 3.50598H19.487C19.661 3.50598 19.809 3.61598 19.933 3.83298L21.387 6.40298C21.577 6.73998 21.627 6.88098 21.411 7.23998C21.151 7.66998 20.898 8.10398 20.651 8.53998L20.284 9.19798C20.178 9.39398 20.061 9.47798 20.244 9.70998L22.896 14.347C23.068 14.648 23.007 14.841 22.853 15.117C22.416 15.902 21.971 16.681 21.518 17.457C21.359 17.729 21.166 17.832 20.838 17.827C20.061 17.811 19.286 17.817 18.511 17.843C18.4944 17.8438 18.4783 17.8489 18.4641 17.8576C18.4499 17.8663 18.4382 17.8785 18.43 17.893C17.5358 19.4773 16.6342 21.0573 15.725 22.633C15.556 22.926 15.345 22.996 15 22.997C14.003 23 12.998 23.001 11.983 22.999C11.8885 22.9987 11.7957 22.9735 11.7141 22.9259C11.6325 22.8784 11.5648 22.8101 11.518 22.728L10.183 20.405C10.1752 20.3898 10.1633 20.3771 10.1486 20.3684C10.1339 20.3598 10.1171 20.3554 10.1 20.356H4.982C4.697 20.386 4.429 20.355 4.177 20.264L2.574 17.494C2.52659 17.412 2.50146 17.319 2.50111 17.2243C2.50076 17.1295 2.5252 17.0363 2.572 16.954L3.779 14.834C3.79619 14.804 3.80524 14.77 3.80524 14.7355C3.80524 14.7009 3.79619 14.667 3.779 14.637C3.15027 13.5485 2.52526 12.4578 1.904 11.365L1.114 9.96998C0.954 9.65998 0.941 9.47398 1.209 9.00498C1.674 8.19198 2.136 7.37998 2.596 6.56898C2.728 6.33498 2.9 6.23498 3.18 6.23398C4.04299 6.23035 4.906 6.23001 5.769 6.23298C5.7908 6.23281 5.81217 6.2269 5.83095 6.21584C5.84974 6.20478 5.86528 6.18896 5.876 6.16998L8.682 1.27498C8.72452 1.20052 8.78592 1.13857 8.86 1.09538C8.93409 1.0522 9.01825 1.02929 9.104 1.02898C9.628 1.02798 10.157 1.02898 10.687 1.02298L11.704 0.999982C12.045 0.996982 12.428 1.03198 12.604 1.33998ZM9.172 1.74298C9.16146 1.74298 9.15111 1.74574 9.14198 1.75101C9.13285 1.75628 9.12527 1.76386 9.12 1.77298L6.254 6.78798C6.24024 6.81162 6.22054 6.83124 6.19687 6.84493C6.17319 6.85861 6.14635 6.86587 6.119 6.86598H3.253C3.197 6.86598 3.183 6.89098 3.212 6.93998L9.022 17.096C9.047 17.138 9.035 17.158 8.988 17.159L6.193 17.174C6.15214 17.1726 6.11172 17.1828 6.07635 17.2033C6.04099 17.2238 6.0121 17.2538 5.993 17.29L4.673 19.6C4.629 19.678 4.652 19.718 4.741 19.718L10.457 19.726C10.503 19.726 10.537 19.746 10.561 19.787L11.964 22.241C12.01 22.322 12.056 22.323 12.103 22.241L17.109 13.481L17.892 12.099C17.8968 12.0904 17.9037 12.0833 17.9122 12.0784C17.9206 12.0734 17.9302 12.0708 17.94 12.0708C17.9498 12.0708 17.9594 12.0734 17.9678 12.0784C17.9763 12.0833 17.9832 12.0904 17.988 12.099L19.412 14.629C19.4227 14.6479 19.4382 14.6636 19.4571 14.6745C19.4759 14.6854 19.4973 14.6911 19.519 14.691L22.282 14.671C22.2891 14.671 22.2961 14.6692 22.3022 14.6657C22.3083 14.6622 22.3135 14.6571 22.317 14.651C22.3204 14.6449 22.3222 14.638 22.3222 14.631C22.3222 14.624 22.3204 14.6171 22.317 14.611L19.417 9.52498C19.4066 9.50798 19.401 9.48843 19.401 9.46848C19.401 9.44854 19.4066 9.42898 19.417 9.41198L19.71 8.90498L20.83 6.92798C20.854 6.88698 20.842 6.86598 20.795 6.86598H9.2C9.141 6.86598 9.127 6.83998 9.157 6.78898L10.591 4.28398C10.6017 4.26691 10.6074 4.24715 10.6074 4.22698C10.6074 4.20681 10.6017 4.18705 10.591 4.16998L9.225 1.77398C9.21978 1.76452 9.21209 1.75665 9.20276 1.75119C9.19344 1.74573 9.18281 1.7429 9.172 1.74298ZM15.462 9.76298C15.508 9.76298 15.52 9.78298 15.496 9.82298L14.664 11.288L12.051 15.873C12.0461 15.8819 12.0388 15.8893 12.03 15.8944C12.0212 15.8995 12.0112 15.9022 12.001 15.902C11.9909 15.9019 11.9809 15.8992 11.9721 15.8942C11.9634 15.8891 11.9561 15.8818 11.951 15.873L8.498 9.84098C8.478 9.80698 8.488 9.78898 8.526 9.78698L8.742 9.77498L15.464 9.76298H15.462Z" fill="url(#paint0_linear_631_10870)" />
<defs>
<linearGradient id="paint0_linear_631_10870" x1="0.999512" y1="0.999817" x2="2201.03" y2="0.999817" gradientUnits="userSpaceOnUse">
<stop stop-color="#00055F" stop-opacity="0.84" />
<stop offset="1" stop-color="#6F69F7" stop-opacity="0.84" />
</linearGradient>
</defs>
</svg>} horizontal />;

export const OpenAIIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_430_1585)">
<path d="M20.6862 10.1843C20.9129 9.51086 20.9914 8.79746 20.9162 8.09176C20.8411 7.38605 20.6142 6.70428 20.2506 6.09199C19.1446 4.19312 16.9218 3.2163 14.7511 3.6752C14.15 3.01567 13.3835 2.52377 12.5287 2.24889C11.6739 1.97402 10.7608 1.92585 9.88118 2.10922C9.00152 2.29259 8.18627 2.70105 7.51729 3.29358C6.84831 3.8861 6.34916 4.64183 6.06998 5.48486C5.36512 5.62745 4.69924 5.91681 4.11683 6.33358C3.53442 6.75036 3.0489 7.28496 2.69272 7.90165C1.57472 9.79744 1.82849 12.1889 3.3202 13.8153C3.09266 14.4884 3.01347 15.2017 3.08793 15.9075C3.16239 16.6132 3.38878 17.2951 3.75195 17.9076C4.85916 19.8072 7.0834 20.7839 9.25547 20.3244C9.73304 20.8549 10.3198 21.2787 10.9767 21.5676C11.6335 21.8566 12.3453 22.0039 13.0645 21.9999C15.2895 22.0019 17.2609 20.585 17.9404 18.4951C18.6452 18.3523 19.311 18.0628 19.8933 17.6461C20.4757 17.2293 20.9613 16.6949 21.3177 16.0783C22.4222 14.1858 22.1674 11.8073 20.6862 10.1843ZM13.0644 20.691C12.1762 20.6924 11.3159 20.3854 10.6343 19.8238L10.7543 19.7567L14.791 17.4582C14.8915 17.4001 14.9749 17.3172 15.033 17.2176C15.0912 17.1181 15.1221 17.0053 15.1227 16.8905V11.2763L16.8294 12.2502C16.8378 12.2544 16.8451 12.2605 16.8506 12.2681C16.8562 12.2756 16.8599 12.2843 16.8614 12.2935V16.9457C16.857 19.0124 15.1596 20.6868 13.0644 20.6911V20.691ZM4.90293 17.2532C4.45754 16.4946 4.29761 15.6053 4.45127 14.7419L4.5712 14.8128L8.61192 17.1112C8.71191 17.1691 8.82574 17.1996 8.94167 17.1996C9.05761 17.1996 9.17144 17.1691 9.27143 17.1112L14.2074 14.3043V16.248C14.207 16.258 14.2042 16.2678 14.1994 16.2767C14.1945 16.2855 14.1877 16.2932 14.1795 16.2991L10.0908 18.6252C8.27384 19.6577 5.95257 19.0438 4.90293 17.2532ZM3.83974 8.57987C4.28823 7.81633 4.99615 7.23395 5.83815 6.93583V11.6667C5.83663 11.781 5.86624 11.8937 5.9239 11.9928C5.98155 12.092 6.06514 12.1741 6.16593 12.2306L11.0779 15.0258L9.37133 15.9996C9.36209 16.0045 9.3518 16.007 9.34134 16.007C9.33089 16.007 9.3206 16.0045 9.31136 15.9996L5.2307 13.6774C3.41734 12.6407 2.7955 10.3526 3.83974 8.56012V8.57987ZM17.8605 11.793L12.9326 8.97015L14.6351 8.00031C14.6443 7.99548 14.6546 7.99295 14.6651 7.99295C14.6755 7.99295 14.6858 7.99548 14.6951 8.00031L18.7759 10.3264C19.3997 10.6815 19.9084 11.2044 20.2423 11.834C20.5762 12.4636 20.7217 13.1739 20.6618 13.882C20.6019 14.59 20.339 15.2667 19.9038 15.833C19.4687 16.3992 18.8792 16.8317 18.2043 17.0799V12.3487C18.2007 12.2346 18.1672 12.1234 18.107 12.0259C18.0467 11.9285 17.9618 11.8483 17.8605 11.793ZM19.5591 9.27371L19.4392 9.20273L15.4065 6.88461C15.3059 6.82638 15.1914 6.79568 15.0748 6.79568C14.9581 6.79568 14.8436 6.82638 14.743 6.88461L9.811 9.69144V7.74774C9.80998 7.73788 9.81167 7.72794 9.81589 7.71894C9.82011 7.70995 9.82671 7.70225 9.83498 7.69663L13.9156 5.37437C14.5411 5.01896 15.2562 4.84656 15.9773 4.87734C16.6984 4.90811 17.3957 5.14079 17.9877 5.54815C18.5797 5.95552 19.0419 6.52073 19.3201 7.17767C19.5984 7.83462 19.6813 8.55615 19.5591 9.25786V9.27371ZM8.87973 12.7194L7.17311 11.7495C7.16458 11.7444 7.15729 11.7376 7.15176 11.7294C7.14623 11.7212 7.14258 11.7119 7.14109 11.7022V7.06182C7.14204 6.34998 7.34841 5.65312 7.73607 5.0527C8.12373 4.45229 8.67666 3.97313 9.33021 3.67127C9.98375 3.3694 10.7109 3.25729 11.4267 3.34805C12.1424 3.43881 12.8172 3.72868 13.3721 4.18378L13.2522 4.25085L9.21542 6.54934C9.11496 6.60747 9.03155 6.69037 8.97339 6.78991C8.91523 6.88944 8.88432 7.00219 8.88369 7.11707L8.87973 12.7194ZM9.80704 10.7481L12.0053 9.49837L14.2074 10.7481V13.2476L12.0132 14.4975L9.81112 13.2476L9.80704 10.7481Z" fill="black" />
</g>
<defs>
<clipPath id="clip0_430_1585">
<rect width="20" height="20" fill="white" transform="translate(2 2)" />
</clipPath>
</defs>
</svg>} horizontal />;

export const MetaIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M4.13523 13.5079C4.13523 10.377 5.77224 7.10995 7.69395 7.10995C8.76157 7.10995 9.61566 7.72251 10.968 9.56021C9.68683 11.466 8.90391 12.623 8.90391 12.623C7.19573 15.2094 6.62633 15.7539 5.70107 15.7539C4.7758 15.822 4.13523 15.0052 4.13523 13.5079ZM15.3096 12.3508L14.0996 10.445C13.8149 9.96859 13.4591 9.49215 13.1744 9.08377C14.242 7.51832 15.0961 6.70157 16.1637 6.70157C18.2989 6.70157 20.0071 9.7644 20.0071 13.5759C20.0071 15.0052 19.5089 15.822 18.5125 15.822C17.516 15.822 17.1601 15.2094 15.3096 12.3508ZM12.2491 7.72251C10.6833 5.74869 9.33096 5 7.76512 5C4.4911 5 2 9.15183 2 13.5079C2 16.2304 3.35231 17.9319 5.62989 17.9319C7.2669 17.9319 8.40569 17.1832 10.5409 13.644C10.5409 13.644 11.395 12.1466 12.0356 11.1257C12.2491 11.466 12.4626 11.8063 12.6762 12.2147L13.6726 13.8482C15.5943 16.9791 16.6619 18 18.5836 18C20.79 18 22 16.2304 22 13.4398C21.9288 8.81152 19.3665 5 16.3061 5C14.669 5 13.3879 6.22513 12.2491 7.72251Z" fill="#0081FB" />
</svg>} horizontal />;

export const MarsIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_631_10869)">
<path fill-rule="evenodd" clip-rule="evenodd" d="M8.63156 18.1049L8.57257 18.2142C8.49832 18.3766 8.47037 18.5619 8.50142 18.7515C8.58658 19.2656 9.07928 19.6143 9.60131 19.53C9.86988 19.487 10.0939 19.3379 10.2364 19.1336L10.3133 19.0025L10.8178 18.1398C10.8208 18.1325 10.8243 18.1256 10.8274 18.1183C10.8588 18.0512 10.8968 17.9881 10.9405 17.9296L11.846 16.3821L12.7455 17.9193C12.7926 17.9812 12.8332 18.0478 12.8669 18.1187C12.872 18.1299 12.8768 18.1411 12.8817 18.1523L13.3736 18.9931L13.4614 19.1431C13.6042 19.343 13.8256 19.4879 14.0899 19.5305C14.6123 19.6143 15.1046 19.2656 15.1902 18.752C15.2226 18.5568 15.1915 18.3654 15.1116 18.1991L15.0692 18.1205L13.7435 15.6581L13.5976 15.3873L13.5251 15.2528C13.3526 15.0061 13.1254 14.7988 12.8603 14.6488C12.562 14.4798 12.2155 14.3831 11.8469 14.3831C11.4773 14.3831 11.131 14.4803 10.8322 14.6496C10.5636 14.8018 10.3338 15.0125 10.1608 15.2643L9.95551 15.6457L8.63109 18.1062L8.63156 18.1049Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M1.72147 19.175L10.1396 9.01879C10.168 8.98181 10.1977 8.94614 10.2287 8.91132C10.6219 8.46725 11.201 8.18611 11.8471 8.18611C12.4935 8.18611 13.0732 8.46769 13.4668 8.91259C13.4969 8.94656 13.5258 8.98138 13.5533 9.01749L13.8638 9.39191L21.9453 19.1419L22.0374 19.2532C22.212 19.4337 22.4585 19.5468 22.7319 19.5468C23.2609 19.5468 23.6898 19.1247 23.6898 18.6041C23.6898 18.4142 23.633 18.2375 23.5347 18.0896L23.4523 17.9829L16.7682 9.31368L15.4 7.53915L15.2607 7.35903L13.8633 5.54626L13.5043 5.0807C13.4873 5.0605 13.4703 5.04073 13.4528 5.02095C13.0596 4.58463 12.4857 4.30951 11.8462 4.30951C11.2068 4.30951 10.6328 4.58463 10.2396 5.02095C10.2222 5.03986 10.2057 5.05963 10.189 5.07941L10.0846 5.21483L9.82908 5.54583L8.42857 7.36247L8.29277 7.53872L6.92165 9.31711L0.255963 17.9623L0.140661 18.1119C0.0515526 18.255 0 18.4235 0 18.6036C0 19.1243 0.428953 19.5464 0.957925 19.5464C1.24666 19.5464 1.50525 19.4209 1.68128 19.2223L1.72059 19.175H1.72147Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M10.0556 10.4893L4.29329 17.9627L4.17751 18.1127C4.08841 18.2558 4.03729 18.4243 4.03729 18.6045C4.03729 19.1251 4.46626 19.5472 4.99523 19.5472C5.28396 19.5472 5.54298 19.4212 5.71859 19.2227L5.75658 19.177L10.2649 13.7379C10.6572 13.3158 11.2219 13.0505 11.8492 13.0505C12.4769 13.0505 13.0417 13.3158 13.4339 13.7383L17.9138 19.1427L18.0055 19.2535C18.1803 19.4346 18.427 19.5472 18.7006 19.5472C19.2294 19.5472 19.6585 19.1251 19.6585 18.6045C19.6585 18.4149 19.6016 18.2378 19.5033 18.0903L19.4208 17.9834L13.4693 10.2641C13.4562 10.2495 13.4436 10.2353 13.43 10.2211C13.0377 9.80067 12.4747 9.53717 11.8492 9.53717C11.2219 9.53717 10.6572 9.80196 10.2649 10.2241C10.2531 10.237 10.2413 10.2499 10.2295 10.2632L10.0556 10.4893Z" fill="black" />
</g>
<defs>
<clipPath id="clip0_631_10869">
<rect width="24" height="16" fill="white" transform="translate(0 4)" />
</clipPath>
</defs>
</svg>} horizontal />;

export const GoogleIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M23 12.245C23 11.34 22.925 10.68 22.764 9.995H12.224V14.078H18.41C18.286 15.092 17.613 16.62 16.116 17.647L16.095 17.783L19.427 20.313L19.657 20.335C21.779 18.417 23 15.593 23 12.245Z" fill="#4285F4" />
<path d="M12.225 23C15.255 23 17.799 22.022 19.658 20.335L16.116 17.647C15.168 18.295 13.896 18.747 12.225 18.747C10.8164 18.7471 9.44319 18.3063 8.29791 17.4863C7.15263 16.6664 6.29277 15.5084 5.83899 14.175L5.70699 14.186L2.24199 16.814L2.19699 16.938C4.04299 20.531 7.83499 23 12.225 23Z" fill="#34A853" />
<path d="M5.84 14.175C5.59404 13.4761 5.46662 12.7409 5.463 12C5.463 11.242 5.601 10.509 5.824 9.825L5.818 9.678L2.31 7.008L2.195 7.062C1.41079 8.58997 1.00119 10.2825 1 12C1 13.772 1.436 15.447 2.197 16.938L5.84 14.175Z" fill="#FBBC05" />
<path d="M12.225 5.253C14.333 5.253 15.754 6.145 16.565 6.891L19.732 3.86C17.787 2.088 15.255 1 12.225 1C7.83399 1 4.04299 3.469 2.19699 7.062L5.82699 9.825C6.28468 8.49166 7.14717 7.33445 8.29413 6.51484C9.44108 5.69522 10.8153 5.25409 12.225 5.253Z" fill="#EB4335" />
</svg>} horizontal />;

export const DeepSeekIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M21.7896 6.25856C21.5779 6.15323 21.4862 6.35453 21.3629 6.45731C21.3204 6.49043 21.2846 6.53375 21.2487 6.57282C20.9388 6.91002 20.5771 7.13086 20.1046 7.10453C19.4138 7.06546 18.8238 7.28629 18.3021 7.82479C18.1913 7.16058 17.823 6.76478 17.263 6.50997C16.9697 6.37747 16.673 6.24582 16.4672 5.95788C16.3238 5.75318 16.2847 5.5247 16.213 5.30047C16.1672 5.16457 16.1213 5.02612 15.9688 5.00319C15.8022 4.97686 15.7372 5.1187 15.6722 5.23762C15.4114 5.72345 15.3105 6.25856 15.3205 6.80045C15.343 8.02014 15.848 8.99182 16.8522 9.68236C16.9663 9.76135 16.9955 9.84119 16.9597 9.9567C16.8913 10.1945 16.8097 10.4256 16.738 10.6642C16.6922 10.8163 16.6238 10.8485 16.4638 10.7831C15.9232 10.5463 15.4322 10.2061 15.0172 9.78088C14.303 9.07761 13.6581 8.30129 12.8531 7.69314C12.6666 7.55267 12.475 7.41923 12.2789 7.29309C11.4581 6.48024 12.3873 5.81264 12.6022 5.73365C12.8272 5.65041 12.6797 5.36672 11.9531 5.37012C11.2264 5.37351 10.5615 5.62068 9.71397 5.95108C9.58804 6.00027 9.45846 6.03918 9.32648 6.06745C8.53452 5.91535 7.72455 5.88615 6.92403 5.98081C5.35322 6.15918 4.09908 6.91682 3.1766 8.2087C2.06829 9.76135 1.80746 11.5263 2.12662 13.3661C2.46245 15.306 3.4341 16.9122 4.92657 18.1675C6.47487 19.4696 8.25733 20.1075 10.2915 19.9852C11.5264 19.913 12.9022 19.744 14.453 18.4054C14.8447 18.6041 15.2547 18.6831 15.9364 18.7426C16.4613 18.7927 16.9663 18.7171 17.3572 18.6338C17.9696 18.5013 17.9271 17.9229 17.7063 17.8176C15.9105 16.9648 16.3047 17.3122 15.9455 17.0311C16.8588 15.9303 18.2338 14.7871 18.7721 11.083C18.8138 10.7882 18.778 10.6031 18.7721 10.3652C18.7688 10.2209 18.8013 10.1639 18.9638 10.1478C19.4146 10.1001 19.852 9.96309 20.2513 9.74436C21.4146 9.09629 21.8846 8.03289 21.9954 6.75713C22.0121 6.56178 21.9921 6.36133 21.7896 6.25856ZM11.6506 17.7403C9.9098 16.3456 9.06565 15.8861 8.71733 15.9057C8.39066 15.9261 8.44983 16.3057 8.5215 16.5537C8.59649 16.7984 8.69399 16.9665 8.83066 17.1814C8.92565 17.3233 8.99065 17.5348 8.73649 17.6936C8.17567 18.0469 7.20152 17.5747 7.15569 17.5518C6.02154 16.8706 5.0724 15.9719 4.40491 14.7429C3.75992 13.5597 3.38493 12.2908 3.32327 10.936C3.3066 10.6082 3.40076 10.4927 3.72076 10.4332C4.14084 10.3513 4.57126 10.3401 4.9949 10.4001C6.77153 10.6651 8.28317 11.4745 9.55148 12.7562C10.2748 13.4867 10.8223 14.359 11.3864 15.2117C11.9864 16.1172 12.6314 16.9801 13.4531 17.6868C13.7431 17.9348 13.9739 18.1234 14.1956 18.2618C13.5272 18.3383 12.4123 18.3553 11.6506 17.7403ZM12.4839 12.2704C12.4838 12.2282 12.4937 12.1866 12.5129 12.1492C12.532 12.1118 12.5598 12.0797 12.5939 12.0557C12.6279 12.0317 12.6672 12.0165 12.7083 12.0114C12.7494 12.0064 12.7911 12.0116 12.8297 12.0266C12.879 12.0446 12.9216 12.0779 12.9515 12.1217C12.9813 12.1656 12.9971 12.2178 12.9964 12.2712C12.9965 12.3057 12.9899 12.3399 12.9769 12.3717C12.964 12.4036 12.9449 12.4325 12.9208 12.4568C12.8968 12.481 12.8683 12.5002 12.8369 12.5131C12.8055 12.526 12.7719 12.5324 12.7381 12.532C12.7045 12.5321 12.6712 12.5254 12.6402 12.5122C12.6092 12.4991 12.5811 12.4798 12.5575 12.4554C12.5339 12.4311 12.5153 12.4021 12.5028 12.3704C12.4903 12.3386 12.4834 12.3046 12.4839 12.2704ZM15.0755 13.626C14.9089 13.6948 14.743 13.7542 14.5839 13.7619C14.3444 13.7704 14.1095 13.6942 13.9189 13.5461C13.6906 13.3508 13.5272 13.2421 13.4589 12.9023C13.4353 12.7363 13.4398 12.5674 13.4722 12.4029C13.5306 12.1251 13.4656 11.9468 13.2731 11.7854C13.1172 11.6529 12.9181 11.6164 12.6997 11.6164C12.625 11.6119 12.5524 11.5892 12.4881 11.5501C12.3964 11.5043 12.3214 11.3887 12.3931 11.246C12.4164 11.2002 12.5264 11.0881 12.5531 11.0677C12.8497 10.8961 13.1922 10.9522 13.5081 11.0813C13.8014 11.2036 14.0231 11.4278 14.3422 11.7455C14.668 12.1285 14.7272 12.2347 14.913 12.5218C15.0597 12.7469 15.193 12.9779 15.2839 13.2421C15.3397 13.4077 15.268 13.5427 15.0755 13.626Z" fill="#4D6BFE" />
</svg>} horizontal />;

export const BFLIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 20.683L12.01 2.5L24 20.683H21.767L12.009 5.878L3.471 18.806H15.593L16.832 20.683H0Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M8.069 16.724L10.142 13.609L12.216 16.724H8.069ZM18.24 20.683L12.572 11.976H14.749L20.435 20.683H18.24ZM19.74 11.676L21.87 8.48602L24 11.676H19.74Z" fill="black" />
</svg>} horizontal />;

## Featured models

<CardGroup cols={1}>
  <DeepSeekIconCard title="DeepSeek R1" href="/examples/models/deepseek/deepseek-r1" />

  <OpenAIIconCard title="Whisper V3" href="/examples/models/whisper/whisper-v3-fastest" />

  <QwenIconCard title="Qwen 2.5 32B Coder Instruct" href="/examples/models/qwen/qwen-2-5-32b-coder-instruct" />

  <MetaIconCard title="Llama 3.3 70B Instruct" href="/examples/models/llama/llama-3.3-70B-instruct" />

  <BFLIconCard title="flux-schnell" href="/examples/models/flux/flux-schnell" />

  <GoogleIconCard title="Gemma 3 27B IT" href="/examples/models/gemma/gemma-3-27b-it" />

  <MarsIconCard title="MARS6" href="/examples/models/mars/MARS6" />
</CardGroup>


# Qwen-2-5-32B-Coder-Instruct
Source: https://docs.baseten.co/examples/models/qwen/qwen-2-5-32b-coder-instruct

Qwen 2.5 32B Coder is an OpenAI-compatible model and can be called using the OpenAI SDK in any language.

export const QwenIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.604 1.33998C12.997 2.02998 13.388 2.72198 13.778 3.41498C13.7938 3.4427 13.8166 3.46573 13.8442 3.48171C13.8718 3.4977 13.9031 3.50608 13.935 3.50598H19.487C19.661 3.50598 19.809 3.61598 19.933 3.83298L21.387 6.40298C21.577 6.73998 21.627 6.88098 21.411 7.23998C21.151 7.66998 20.898 8.10398 20.651 8.53998L20.284 9.19798C20.178 9.39398 20.061 9.47798 20.244 9.70998L22.896 14.347C23.068 14.648 23.007 14.841 22.853 15.117C22.416 15.902 21.971 16.681 21.518 17.457C21.359 17.729 21.166 17.832 20.838 17.827C20.061 17.811 19.286 17.817 18.511 17.843C18.4944 17.8438 18.4783 17.8489 18.4641 17.8576C18.4499 17.8663 18.4382 17.8785 18.43 17.893C17.5358 19.4773 16.6342 21.0573 15.725 22.633C15.556 22.926 15.345 22.996 15 22.997C14.003 23 12.998 23.001 11.983 22.999C11.8885 22.9987 11.7957 22.9735 11.7141 22.9259C11.6325 22.8784 11.5648 22.8101 11.518 22.728L10.183 20.405C10.1752 20.3898 10.1633 20.3771 10.1486 20.3684C10.1339 20.3598 10.1171 20.3554 10.1 20.356H4.982C4.697 20.386 4.429 20.355 4.177 20.264L2.574 17.494C2.52659 17.412 2.50146 17.319 2.50111 17.2243C2.50076 17.1295 2.5252 17.0363 2.572 16.954L3.779 14.834C3.79619 14.804 3.80524 14.77 3.80524 14.7355C3.80524 14.7009 3.79619 14.667 3.779 14.637C3.15027 13.5485 2.52526 12.4578 1.904 11.365L1.114 9.96998C0.954 9.65998 0.941 9.47398 1.209 9.00498C1.674 8.19198 2.136 7.37998 2.596 6.56898C2.728 6.33498 2.9 6.23498 3.18 6.23398C4.04299 6.23035 4.906 6.23001 5.769 6.23298C5.7908 6.23281 5.81217 6.2269 5.83095 6.21584C5.84974 6.20478 5.86528 6.18896 5.876 6.16998L8.682 1.27498C8.72452 1.20052 8.78592 1.13857 8.86 1.09538C8.93409 1.0522 9.01825 1.02929 9.104 1.02898C9.628 1.02798 10.157 1.02898 10.687 1.02298L11.704 0.999982C12.045 0.996982 12.428 1.03198 12.604 1.33998ZM9.172 1.74298C9.16146 1.74298 9.15111 1.74574 9.14198 1.75101C9.13285 1.75628 9.12527 1.76386 9.12 1.77298L6.254 6.78798C6.24024 6.81162 6.22054 6.83124 6.19687 6.84493C6.17319 6.85861 6.14635 6.86587 6.119 6.86598H3.253C3.197 6.86598 3.183 6.89098 3.212 6.93998L9.022 17.096C9.047 17.138 9.035 17.158 8.988 17.159L6.193 17.174C6.15214 17.1726 6.11172 17.1828 6.07635 17.2033C6.04099 17.2238 6.0121 17.2538 5.993 17.29L4.673 19.6C4.629 19.678 4.652 19.718 4.741 19.718L10.457 19.726C10.503 19.726 10.537 19.746 10.561 19.787L11.964 22.241C12.01 22.322 12.056 22.323 12.103 22.241L17.109 13.481L17.892 12.099C17.8968 12.0904 17.9037 12.0833 17.9122 12.0784C17.9206 12.0734 17.9302 12.0708 17.94 12.0708C17.9498 12.0708 17.9594 12.0734 17.9678 12.0784C17.9763 12.0833 17.9832 12.0904 17.988 12.099L19.412 14.629C19.4227 14.6479 19.4382 14.6636 19.4571 14.6745C19.4759 14.6854 19.4973 14.6911 19.519 14.691L22.282 14.671C22.2891 14.671 22.2961 14.6692 22.3022 14.6657C22.3083 14.6622 22.3135 14.6571 22.317 14.651C22.3204 14.6449 22.3222 14.638 22.3222 14.631C22.3222 14.624 22.3204 14.6171 22.317 14.611L19.417 9.52498C19.4066 9.50798 19.401 9.48843 19.401 9.46848C19.401 9.44854 19.4066 9.42898 19.417 9.41198L19.71 8.90498L20.83 6.92798C20.854 6.88698 20.842 6.86598 20.795 6.86598H9.2C9.141 6.86598 9.127 6.83998 9.157 6.78898L10.591 4.28398C10.6017 4.26691 10.6074 4.24715 10.6074 4.22698C10.6074 4.20681 10.6017 4.18705 10.591 4.16998L9.225 1.77398C9.21978 1.76452 9.21209 1.75665 9.20276 1.75119C9.19344 1.74573 9.18281 1.7429 9.172 1.74298ZM15.462 9.76298C15.508 9.76298 15.52 9.78298 15.496 9.82298L14.664 11.288L12.051 15.873C12.0461 15.8819 12.0388 15.8893 12.03 15.8944C12.0212 15.8995 12.0112 15.9022 12.001 15.902C11.9909 15.9019 11.9809 15.8992 11.9721 15.8942C11.9634 15.8891 11.9561 15.8818 11.951 15.873L8.498 9.84098C8.478 9.80698 8.488 9.78898 8.526 9.78698L8.742 9.77498L15.464 9.76298H15.462Z" fill="url(#paint0_linear_631_10870)" />
<defs>
<linearGradient id="paint0_linear_631_10870" x1="0.999512" y1="0.999817" x2="2201.03" y2="0.999817" gradientUnits="userSpaceOnUse">
<stop stop-color="#00055F" stop-opacity="0.84" />
<stop offset="1" stop-color="#6F69F7" stop-opacity="0.84" />
</linearGradient>
</defs>
</svg>} horizontal />;

<QwenIconCard title="Deploy Qwen 2.5 32B Coder Instruct" href="https://app.baseten.co/deploy/qwen-2-5-32b-coder-instruct" />

## Example usage

```python  theme={"system"}
from openai import OpenAI
import os

model_url = "" # Copy in from API pane in Baseten model dashboard

client = OpenAI(
    api_key=os.environ['BASETEN_API_KEY'],
    base_url=model_url
)

# Chat completion
response_chat = client.chat.completions.create(
    model="",
    messages=[
        {"role": "user", "content": "Tell me a fun fact about Python."}
    ],
    temperature=0.3,
    max_tokens=100,
)
print(response_chat)
```

## JSON output

```json  theme={"system"}
{
  "id": "143",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "[Model output here]",
        "role": "assistant",
        "audio": null,
        "function_call": null,
        "tool_calls": null
      }
    }
  ],
  "created": 1741224586,
  "model": "",
  "object": "chat.completion",
  "service_tier": null,
  "system_fingerprint": null,
  "usage": {
    "completion_tokens": 145,
    "prompt_tokens": 38,
    "total_tokens": 183,
    "completion_tokens_details": null,
    "prompt_tokens_details": null
  }
}
```


# SDXL Lightning
Source: https://docs.baseten.co/examples/models/stable-diffusion/sdxl-lightning

A variant of Stable Diffusion XL that generates 1024x1024 px images in 4 UNet steps, enabling near real-time image creation.

export const LightningIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M14.944 18.587L13.24 18.142V10.01L15.064 9.54801C16.064 9.29401 16.904 9.08701 16.944 9.09501C16.976 9.09501 17 11.33 17 14.067V19.04L16.824 19.032C16.72 19.032 15.872 18.826 14.944 18.587Z" fill="#00C8D2" />
<path d="M7 16.5421C7 13.8061 7.024 11.5621 7.064 11.5621C7.096 11.5541 7.936 11.7621 8.944 12.0161L10.76 12.4771L10.744 16.5271L10.72 20.5761L9.088 20.9981C8.192 21.2281 7.352 21.4431 7.232 21.4671L7 21.5231V16.5421Z" fill="#3C8CFF" />
<path d="M19.24 12.477C19.24 3.44703 19.248 2.96203 19.384 3.00203C19.456 3.02603 20.168 3.20903 20.96 3.40803C21.752 3.61503 22.536 3.81303 22.704 3.85303L23 3.93303L22.984 12.493L22.96 21.061L21.336 21.475C20.448 21.705 19.608 21.912 19.48 21.945L19.24 22V12.477Z" fill="#78E6DC" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M1 12.509C1 7.83103 1.024 4.00403 1.064 4.00403C1.096 4.00403 1.936 4.21103 2.936 4.45803L4.76 4.91903V12.501C4.76 16.661 4.744 20.075 4.728 20.075C4.704 20.075 3.856 20.29 2.848 20.545L1 21.013V12.509Z" fill="#325AB4" />
</svg>} horizontal />;

<LightningIconCard title="Deploy SDXL Lightning" href="https://app.baseten.co/deploy/sdxl_lightning" />

# Example usage

The model accepts a single input, prompt, and returns a base64 string of the image as the key `result`.

This implementation uses the 4-step UNet checkpoint to balance speed and quality. You can [deploy your own version](https://github.com/basetenlabs/truss-examples/tree/main/stable-diffusion/sdxl-lightning) with either 2 steps for even faster results or 8 steps for even higher quality.

```python  theme={"system"}
import base64
import requests
import os

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
BASE64_PREAMBLE = "data:image/png;base64,"

data = {
    "prompt": "a picture of a rhino wearing a suit",
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Get output image
res = res.json()
img_b64 = res.get("result")
img = base64.b64decode(img_b64)

# Save the base64 string to a PNG
img_file = open("sdxl-output-1.png", "wb")
img_file.write(img)
img_file.close()
os.system("open sdxl-output-1.png")
```

**JSON Output**

```json  theme={"system"}
{
  "result": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAA..."
}
```


# Whisper V3
Source: https://docs.baseten.co/examples/models/whisper/whisper-v3-fastest

Whisper V3 is a fast and accurate speech recognition model.

export const OpenAIIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_430_1585)">
<path d="M20.6862 10.1843C20.9129 9.51086 20.9914 8.79746 20.9162 8.09176C20.8411 7.38605 20.6142 6.70428 20.2506 6.09199C19.1446 4.19312 16.9218 3.2163 14.7511 3.6752C14.15 3.01567 13.3835 2.52377 12.5287 2.24889C11.6739 1.97402 10.7608 1.92585 9.88118 2.10922C9.00152 2.29259 8.18627 2.70105 7.51729 3.29358C6.84831 3.8861 6.34916 4.64183 6.06998 5.48486C5.36512 5.62745 4.69924 5.91681 4.11683 6.33358C3.53442 6.75036 3.0489 7.28496 2.69272 7.90165C1.57472 9.79744 1.82849 12.1889 3.3202 13.8153C3.09266 14.4884 3.01347 15.2017 3.08793 15.9075C3.16239 16.6132 3.38878 17.2951 3.75195 17.9076C4.85916 19.8072 7.0834 20.7839 9.25547 20.3244C9.73304 20.8549 10.3198 21.2787 10.9767 21.5676C11.6335 21.8566 12.3453 22.0039 13.0645 21.9999C15.2895 22.0019 17.2609 20.585 17.9404 18.4951C18.6452 18.3523 19.311 18.0628 19.8933 17.6461C20.4757 17.2293 20.9613 16.6949 21.3177 16.0783C22.4222 14.1858 22.1674 11.8073 20.6862 10.1843ZM13.0644 20.691C12.1762 20.6924 11.3159 20.3854 10.6343 19.8238L10.7543 19.7567L14.791 17.4582C14.8915 17.4001 14.9749 17.3172 15.033 17.2176C15.0912 17.1181 15.1221 17.0053 15.1227 16.8905V11.2763L16.8294 12.2502C16.8378 12.2544 16.8451 12.2605 16.8506 12.2681C16.8562 12.2756 16.8599 12.2843 16.8614 12.2935V16.9457C16.857 19.0124 15.1596 20.6868 13.0644 20.6911V20.691ZM4.90293 17.2532C4.45754 16.4946 4.29761 15.6053 4.45127 14.7419L4.5712 14.8128L8.61192 17.1112C8.71191 17.1691 8.82574 17.1996 8.94167 17.1996C9.05761 17.1996 9.17144 17.1691 9.27143 17.1112L14.2074 14.3043V16.248C14.207 16.258 14.2042 16.2678 14.1994 16.2767C14.1945 16.2855 14.1877 16.2932 14.1795 16.2991L10.0908 18.6252C8.27384 19.6577 5.95257 19.0438 4.90293 17.2532ZM3.83974 8.57987C4.28823 7.81633 4.99615 7.23395 5.83815 6.93583V11.6667C5.83663 11.781 5.86624 11.8937 5.9239 11.9928C5.98155 12.092 6.06514 12.1741 6.16593 12.2306L11.0779 15.0258L9.37133 15.9996C9.36209 16.0045 9.3518 16.007 9.34134 16.007C9.33089 16.007 9.3206 16.0045 9.31136 15.9996L5.2307 13.6774C3.41734 12.6407 2.7955 10.3526 3.83974 8.56012V8.57987ZM17.8605 11.793L12.9326 8.97015L14.6351 8.00031C14.6443 7.99548 14.6546 7.99295 14.6651 7.99295C14.6755 7.99295 14.6858 7.99548 14.6951 8.00031L18.7759 10.3264C19.3997 10.6815 19.9084 11.2044 20.2423 11.834C20.5762 12.4636 20.7217 13.1739 20.6618 13.882C20.6019 14.59 20.339 15.2667 19.9038 15.833C19.4687 16.3992 18.8792 16.8317 18.2043 17.0799V12.3487C18.2007 12.2346 18.1672 12.1234 18.107 12.0259C18.0467 11.9285 17.9618 11.8483 17.8605 11.793ZM19.5591 9.27371L19.4392 9.20273L15.4065 6.88461C15.3059 6.82638 15.1914 6.79568 15.0748 6.79568C14.9581 6.79568 14.8436 6.82638 14.743 6.88461L9.811 9.69144V7.74774C9.80998 7.73788 9.81167 7.72794 9.81589 7.71894C9.82011 7.70995 9.82671 7.70225 9.83498 7.69663L13.9156 5.37437C14.5411 5.01896 15.2562 4.84656 15.9773 4.87734C16.6984 4.90811 17.3957 5.14079 17.9877 5.54815C18.5797 5.95552 19.0419 6.52073 19.3201 7.17767C19.5984 7.83462 19.6813 8.55615 19.5591 9.25786V9.27371ZM8.87973 12.7194L7.17311 11.7495C7.16458 11.7444 7.15729 11.7376 7.15176 11.7294C7.14623 11.7212 7.14258 11.7119 7.14109 11.7022V7.06182C7.14204 6.34998 7.34841 5.65312 7.73607 5.0527C8.12373 4.45229 8.67666 3.97313 9.33021 3.67127C9.98375 3.3694 10.7109 3.25729 11.4267 3.34805C12.1424 3.43881 12.8172 3.72868 13.3721 4.18378L13.2522 4.25085L9.21542 6.54934C9.11496 6.60747 9.03155 6.69037 8.97339 6.78991C8.91523 6.88944 8.88432 7.00219 8.88369 7.11707L8.87973 12.7194ZM9.80704 10.7481L12.0053 9.49837L14.2074 10.7481V13.2476L12.0132 14.4975L9.81112 13.2476L9.80704 10.7481Z" fill="black" />
</g>
<defs>
<clipPath id="clip0_430_1585">
<rect width="20" height="20" fill="white" transform="translate(2 2)" />
</clipPath>
</defs>
</svg>} horizontal />;

<OpenAIIconCard title="Deploy Whisper V3" href="https://www.baseten.co/talk-to-us/?ref=model-library-whisper&model=the%20world%27s%20fastest%20Whisper%20inference" />

# Example usage

Transcribe audio files at up to a 400x real-time factor — that's 1 hour of audio in under 9 seconds. This setup requires meaningful production traffic to be cost-effective, but at scale it's at least 80% cheaper than OpenAI. [Get in touch with us](https://www.baseten.co/talk-to-us/?ref=model-library-whisper\&model=the%20world%27s%20fastest%20Whisper%20inference) and we'll work with you to deploy a transcription pipeline that's customized to match your needs.

For quick deployments of Whisper suitable for shorter audio files and lower traffic volume, you can deploy Whisper V3 and Whisper V3 Turbo directly from the model library.

```python  theme={"system"}
import requests
import os

# Model ID for production deployment
model_id = ""
# Read secrets from environment variables
baseten_api_key = os.environ["BASETEN_API_KEY"]

# Call model endpoint
resp = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={
      "url": "https://www2.cs.uic.edu/~i101/SoundFiles/gettysburg10.wav",
    }
)

print(resp.content.decode("utf-8"))
```

**JSON Output**

```json  theme={"system"}
{
  "segments": [
    {
      "start": 0,
      "end": 9.8,
      "text": "Four score and seven years ago, our fathers brought forth on this continent a new nation, conceived in liberty and dedicated to the proposition that all men are created equal."
    }
  ],
  "language_code": "en"
}
```


# Building with Baseten
Source: https://docs.baseten.co/examples/overview



export const QwenIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12.604 1.33998C12.997 2.02998 13.388 2.72198 13.778 3.41498C13.7938 3.4427 13.8166 3.46573 13.8442 3.48171C13.8718 3.4977 13.9031 3.50608 13.935 3.50598H19.487C19.661 3.50598 19.809 3.61598 19.933 3.83298L21.387 6.40298C21.577 6.73998 21.627 6.88098 21.411 7.23998C21.151 7.66998 20.898 8.10398 20.651 8.53998L20.284 9.19798C20.178 9.39398 20.061 9.47798 20.244 9.70998L22.896 14.347C23.068 14.648 23.007 14.841 22.853 15.117C22.416 15.902 21.971 16.681 21.518 17.457C21.359 17.729 21.166 17.832 20.838 17.827C20.061 17.811 19.286 17.817 18.511 17.843C18.4944 17.8438 18.4783 17.8489 18.4641 17.8576C18.4499 17.8663 18.4382 17.8785 18.43 17.893C17.5358 19.4773 16.6342 21.0573 15.725 22.633C15.556 22.926 15.345 22.996 15 22.997C14.003 23 12.998 23.001 11.983 22.999C11.8885 22.9987 11.7957 22.9735 11.7141 22.9259C11.6325 22.8784 11.5648 22.8101 11.518 22.728L10.183 20.405C10.1752 20.3898 10.1633 20.3771 10.1486 20.3684C10.1339 20.3598 10.1171 20.3554 10.1 20.356H4.982C4.697 20.386 4.429 20.355 4.177 20.264L2.574 17.494C2.52659 17.412 2.50146 17.319 2.50111 17.2243C2.50076 17.1295 2.5252 17.0363 2.572 16.954L3.779 14.834C3.79619 14.804 3.80524 14.77 3.80524 14.7355C3.80524 14.7009 3.79619 14.667 3.779 14.637C3.15027 13.5485 2.52526 12.4578 1.904 11.365L1.114 9.96998C0.954 9.65998 0.941 9.47398 1.209 9.00498C1.674 8.19198 2.136 7.37998 2.596 6.56898C2.728 6.33498 2.9 6.23498 3.18 6.23398C4.04299 6.23035 4.906 6.23001 5.769 6.23298C5.7908 6.23281 5.81217 6.2269 5.83095 6.21584C5.84974 6.20478 5.86528 6.18896 5.876 6.16998L8.682 1.27498C8.72452 1.20052 8.78592 1.13857 8.86 1.09538C8.93409 1.0522 9.01825 1.02929 9.104 1.02898C9.628 1.02798 10.157 1.02898 10.687 1.02298L11.704 0.999982C12.045 0.996982 12.428 1.03198 12.604 1.33998ZM9.172 1.74298C9.16146 1.74298 9.15111 1.74574 9.14198 1.75101C9.13285 1.75628 9.12527 1.76386 9.12 1.77298L6.254 6.78798C6.24024 6.81162 6.22054 6.83124 6.19687 6.84493C6.17319 6.85861 6.14635 6.86587 6.119 6.86598H3.253C3.197 6.86598 3.183 6.89098 3.212 6.93998L9.022 17.096C9.047 17.138 9.035 17.158 8.988 17.159L6.193 17.174C6.15214 17.1726 6.11172 17.1828 6.07635 17.2033C6.04099 17.2238 6.0121 17.2538 5.993 17.29L4.673 19.6C4.629 19.678 4.652 19.718 4.741 19.718L10.457 19.726C10.503 19.726 10.537 19.746 10.561 19.787L11.964 22.241C12.01 22.322 12.056 22.323 12.103 22.241L17.109 13.481L17.892 12.099C17.8968 12.0904 17.9037 12.0833 17.9122 12.0784C17.9206 12.0734 17.9302 12.0708 17.94 12.0708C17.9498 12.0708 17.9594 12.0734 17.9678 12.0784C17.9763 12.0833 17.9832 12.0904 17.988 12.099L19.412 14.629C19.4227 14.6479 19.4382 14.6636 19.4571 14.6745C19.4759 14.6854 19.4973 14.6911 19.519 14.691L22.282 14.671C22.2891 14.671 22.2961 14.6692 22.3022 14.6657C22.3083 14.6622 22.3135 14.6571 22.317 14.651C22.3204 14.6449 22.3222 14.638 22.3222 14.631C22.3222 14.624 22.3204 14.6171 22.317 14.611L19.417 9.52498C19.4066 9.50798 19.401 9.48843 19.401 9.46848C19.401 9.44854 19.4066 9.42898 19.417 9.41198L19.71 8.90498L20.83 6.92798C20.854 6.88698 20.842 6.86598 20.795 6.86598H9.2C9.141 6.86598 9.127 6.83998 9.157 6.78898L10.591 4.28398C10.6017 4.26691 10.6074 4.24715 10.6074 4.22698C10.6074 4.20681 10.6017 4.18705 10.591 4.16998L9.225 1.77398C9.21978 1.76452 9.21209 1.75665 9.20276 1.75119C9.19344 1.74573 9.18281 1.7429 9.172 1.74298ZM15.462 9.76298C15.508 9.76298 15.52 9.78298 15.496 9.82298L14.664 11.288L12.051 15.873C12.0461 15.8819 12.0388 15.8893 12.03 15.8944C12.0212 15.8995 12.0112 15.9022 12.001 15.902C11.9909 15.9019 11.9809 15.8992 11.9721 15.8942C11.9634 15.8891 11.9561 15.8818 11.951 15.873L8.498 9.84098C8.478 9.80698 8.488 9.78898 8.526 9.78698L8.742 9.77498L15.464 9.76298H15.462Z" fill="url(#paint0_linear_631_10870)" />
<defs>
<linearGradient id="paint0_linear_631_10870" x1="0.999512" y1="0.999817" x2="2201.03" y2="0.999817" gradientUnits="userSpaceOnUse">
<stop stop-color="#00055F" stop-opacity="0.84" />
<stop offset="1" stop-color="#6F69F7" stop-opacity="0.84" />
</linearGradient>
</defs>
</svg>} horizontal />;

export const PyTorchIconCard = ({title, href}) => <Card title={title} href={href} icon={<img src="/images/PyTorch.png" alt="PyTorch" width="24" height="24" />} horizontal />;

export const OpenAIIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_430_1585)">
<path d="M20.6862 10.1843C20.9129 9.51086 20.9914 8.79746 20.9162 8.09176C20.8411 7.38605 20.6142 6.70428 20.2506 6.09199C19.1446 4.19312 16.9218 3.2163 14.7511 3.6752C14.15 3.01567 13.3835 2.52377 12.5287 2.24889C11.6739 1.97402 10.7608 1.92585 9.88118 2.10922C9.00152 2.29259 8.18627 2.70105 7.51729 3.29358C6.84831 3.8861 6.34916 4.64183 6.06998 5.48486C5.36512 5.62745 4.69924 5.91681 4.11683 6.33358C3.53442 6.75036 3.0489 7.28496 2.69272 7.90165C1.57472 9.79744 1.82849 12.1889 3.3202 13.8153C3.09266 14.4884 3.01347 15.2017 3.08793 15.9075C3.16239 16.6132 3.38878 17.2951 3.75195 17.9076C4.85916 19.8072 7.0834 20.7839 9.25547 20.3244C9.73304 20.8549 10.3198 21.2787 10.9767 21.5676C11.6335 21.8566 12.3453 22.0039 13.0645 21.9999C15.2895 22.0019 17.2609 20.585 17.9404 18.4951C18.6452 18.3523 19.311 18.0628 19.8933 17.6461C20.4757 17.2293 20.9613 16.6949 21.3177 16.0783C22.4222 14.1858 22.1674 11.8073 20.6862 10.1843ZM13.0644 20.691C12.1762 20.6924 11.3159 20.3854 10.6343 19.8238L10.7543 19.7567L14.791 17.4582C14.8915 17.4001 14.9749 17.3172 15.033 17.2176C15.0912 17.1181 15.1221 17.0053 15.1227 16.8905V11.2763L16.8294 12.2502C16.8378 12.2544 16.8451 12.2605 16.8506 12.2681C16.8562 12.2756 16.8599 12.2843 16.8614 12.2935V16.9457C16.857 19.0124 15.1596 20.6868 13.0644 20.6911V20.691ZM4.90293 17.2532C4.45754 16.4946 4.29761 15.6053 4.45127 14.7419L4.5712 14.8128L8.61192 17.1112C8.71191 17.1691 8.82574 17.1996 8.94167 17.1996C9.05761 17.1996 9.17144 17.1691 9.27143 17.1112L14.2074 14.3043V16.248C14.207 16.258 14.2042 16.2678 14.1994 16.2767C14.1945 16.2855 14.1877 16.2932 14.1795 16.2991L10.0908 18.6252C8.27384 19.6577 5.95257 19.0438 4.90293 17.2532ZM3.83974 8.57987C4.28823 7.81633 4.99615 7.23395 5.83815 6.93583V11.6667C5.83663 11.781 5.86624 11.8937 5.9239 11.9928C5.98155 12.092 6.06514 12.1741 6.16593 12.2306L11.0779 15.0258L9.37133 15.9996C9.36209 16.0045 9.3518 16.007 9.34134 16.007C9.33089 16.007 9.3206 16.0045 9.31136 15.9996L5.2307 13.6774C3.41734 12.6407 2.7955 10.3526 3.83974 8.56012V8.57987ZM17.8605 11.793L12.9326 8.97015L14.6351 8.00031C14.6443 7.99548 14.6546 7.99295 14.6651 7.99295C14.6755 7.99295 14.6858 7.99548 14.6951 8.00031L18.7759 10.3264C19.3997 10.6815 19.9084 11.2044 20.2423 11.834C20.5762 12.4636 20.7217 13.1739 20.6618 13.882C20.6019 14.59 20.339 15.2667 19.9038 15.833C19.4687 16.3992 18.8792 16.8317 18.2043 17.0799V12.3487C18.2007 12.2346 18.1672 12.1234 18.107 12.0259C18.0467 11.9285 17.9618 11.8483 17.8605 11.793ZM19.5591 9.27371L19.4392 9.20273L15.4065 6.88461C15.3059 6.82638 15.1914 6.79568 15.0748 6.79568C14.9581 6.79568 14.8436 6.82638 14.743 6.88461L9.811 9.69144V7.74774C9.80998 7.73788 9.81167 7.72794 9.81589 7.71894C9.82011 7.70995 9.82671 7.70225 9.83498 7.69663L13.9156 5.37437C14.5411 5.01896 15.2562 4.84656 15.9773 4.87734C16.6984 4.90811 17.3957 5.14079 17.9877 5.54815C18.5797 5.95552 19.0419 6.52073 19.3201 7.17767C19.5984 7.83462 19.6813 8.55615 19.5591 9.25786V9.27371ZM8.87973 12.7194L7.17311 11.7495C7.16458 11.7444 7.15729 11.7376 7.15176 11.7294C7.14623 11.7212 7.14258 11.7119 7.14109 11.7022V7.06182C7.14204 6.34998 7.34841 5.65312 7.73607 5.0527C8.12373 4.45229 8.67666 3.97313 9.33021 3.67127C9.98375 3.3694 10.7109 3.25729 11.4267 3.34805C12.1424 3.43881 12.8172 3.72868 13.3721 4.18378L13.2522 4.25085L9.21542 6.54934C9.11496 6.60747 9.03155 6.69037 8.97339 6.78991C8.91523 6.88944 8.88432 7.00219 8.88369 7.11707L8.87973 12.7194ZM9.80704 10.7481L12.0053 9.49837L14.2074 10.7481V13.2476L12.0132 14.4975L9.81112 13.2476L9.80704 10.7481Z" fill="black" />
</g>
<defs>
<clipPath id="clip0_430_1585">
<rect width="20" height="20" fill="white" transform="translate(2 2)" />
</clipPath>
</defs>
</svg>} horizontal />;

export const MetaIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M4.13523 13.5079C4.13523 10.377 5.77224 7.10995 7.69395 7.10995C8.76157 7.10995 9.61566 7.72251 10.968 9.56021C9.68683 11.466 8.90391 12.623 8.90391 12.623C7.19573 15.2094 6.62633 15.7539 5.70107 15.7539C4.7758 15.822 4.13523 15.0052 4.13523 13.5079ZM15.3096 12.3508L14.0996 10.445C13.8149 9.96859 13.4591 9.49215 13.1744 9.08377C14.242 7.51832 15.0961 6.70157 16.1637 6.70157C18.2989 6.70157 20.0071 9.7644 20.0071 13.5759C20.0071 15.0052 19.5089 15.822 18.5125 15.822C17.516 15.822 17.1601 15.2094 15.3096 12.3508ZM12.2491 7.72251C10.6833 5.74869 9.33096 5 7.76512 5C4.4911 5 2 9.15183 2 13.5079C2 16.2304 3.35231 17.9319 5.62989 17.9319C7.2669 17.9319 8.40569 17.1832 10.5409 13.644C10.5409 13.644 11.395 12.1466 12.0356 11.1257C12.2491 11.466 12.4626 11.8063 12.6762 12.2147L13.6726 13.8482C15.5943 16.9791 16.6619 18 18.5836 18C20.79 18 22 16.2304 22 13.4398C21.9288 8.81152 19.3665 5 16.3061 5C14.669 5 13.3879 6.22513 12.2491 7.72251Z" fill="#0081FB" />
</svg>} horizontal />;

export const MarsIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<g clip-path="url(#clip0_631_10869)">
<path fill-rule="evenodd" clip-rule="evenodd" d="M8.63156 18.1049L8.57257 18.2142C8.49832 18.3766 8.47037 18.5619 8.50142 18.7515C8.58658 19.2656 9.07928 19.6143 9.60131 19.53C9.86988 19.487 10.0939 19.3379 10.2364 19.1336L10.3133 19.0025L10.8178 18.1398C10.8208 18.1325 10.8243 18.1256 10.8274 18.1183C10.8588 18.0512 10.8968 17.9881 10.9405 17.9296L11.846 16.3821L12.7455 17.9193C12.7926 17.9812 12.8332 18.0478 12.8669 18.1187C12.872 18.1299 12.8768 18.1411 12.8817 18.1523L13.3736 18.9931L13.4614 19.1431C13.6042 19.343 13.8256 19.4879 14.0899 19.5305C14.6123 19.6143 15.1046 19.2656 15.1902 18.752C15.2226 18.5568 15.1915 18.3654 15.1116 18.1991L15.0692 18.1205L13.7435 15.6581L13.5976 15.3873L13.5251 15.2528C13.3526 15.0061 13.1254 14.7988 12.8603 14.6488C12.562 14.4798 12.2155 14.3831 11.8469 14.3831C11.4773 14.3831 11.131 14.4803 10.8322 14.6496C10.5636 14.8018 10.3338 15.0125 10.1608 15.2643L9.95551 15.6457L8.63109 18.1062L8.63156 18.1049Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M1.72147 19.175L10.1396 9.01879C10.168 8.98181 10.1977 8.94614 10.2287 8.91132C10.6219 8.46725 11.201 8.18611 11.8471 8.18611C12.4935 8.18611 13.0732 8.46769 13.4668 8.91259C13.4969 8.94656 13.5258 8.98138 13.5533 9.01749L13.8638 9.39191L21.9453 19.1419L22.0374 19.2532C22.212 19.4337 22.4585 19.5468 22.7319 19.5468C23.2609 19.5468 23.6898 19.1247 23.6898 18.6041C23.6898 18.4142 23.633 18.2375 23.5347 18.0896L23.4523 17.9829L16.7682 9.31368L15.4 7.53915L15.2607 7.35903L13.8633 5.54626L13.5043 5.0807C13.4873 5.0605 13.4703 5.04073 13.4528 5.02095C13.0596 4.58463 12.4857 4.30951 11.8462 4.30951C11.2068 4.30951 10.6328 4.58463 10.2396 5.02095C10.2222 5.03986 10.2057 5.05963 10.189 5.07941L10.0846 5.21483L9.82908 5.54583L8.42857 7.36247L8.29277 7.53872L6.92165 9.31711L0.255963 17.9623L0.140661 18.1119C0.0515526 18.255 0 18.4235 0 18.6036C0 19.1243 0.428953 19.5464 0.957925 19.5464C1.24666 19.5464 1.50525 19.4209 1.68128 19.2223L1.72059 19.175H1.72147Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M10.0556 10.4893L4.29329 17.9627L4.17751 18.1127C4.08841 18.2558 4.03729 18.4243 4.03729 18.6045C4.03729 19.1251 4.46626 19.5472 4.99523 19.5472C5.28396 19.5472 5.54298 19.4212 5.71859 19.2227L5.75658 19.177L10.2649 13.7379C10.6572 13.3158 11.2219 13.0505 11.8492 13.0505C12.4769 13.0505 13.0417 13.3158 13.4339 13.7383L17.9138 19.1427L18.0055 19.2535C18.1803 19.4346 18.427 19.5472 18.7006 19.5472C19.2294 19.5472 19.6585 19.1251 19.6585 18.6045C19.6585 18.4149 19.6016 18.2378 19.5033 18.0903L19.4208 17.9834L13.4693 10.2641C13.4562 10.2495 13.4436 10.2353 13.43 10.2211C13.0377 9.80067 12.4747 9.53717 11.8492 9.53717C11.2219 9.53717 10.6572 9.80196 10.2649 10.2241C10.2531 10.237 10.2413 10.2499 10.2295 10.2632L10.0556 10.4893Z" fill="black" />
</g>
<defs>
<clipPath id="clip0_631_10869">
<rect width="24" height="16" fill="white" transform="translate(0 4)" />
</clipPath>
</defs>
</svg>} horizontal />;

export const DeepSeekIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M21.7896 6.25856C21.5779 6.15323 21.4862 6.35453 21.3629 6.45731C21.3204 6.49043 21.2846 6.53375 21.2487 6.57282C20.9388 6.91002 20.5771 7.13086 20.1046 7.10453C19.4138 7.06546 18.8238 7.28629 18.3021 7.82479C18.1913 7.16058 17.823 6.76478 17.263 6.50997C16.9697 6.37747 16.673 6.24582 16.4672 5.95788C16.3238 5.75318 16.2847 5.5247 16.213 5.30047C16.1672 5.16457 16.1213 5.02612 15.9688 5.00319C15.8022 4.97686 15.7372 5.1187 15.6722 5.23762C15.4114 5.72345 15.3105 6.25856 15.3205 6.80045C15.343 8.02014 15.848 8.99182 16.8522 9.68236C16.9663 9.76135 16.9955 9.84119 16.9597 9.9567C16.8913 10.1945 16.8097 10.4256 16.738 10.6642C16.6922 10.8163 16.6238 10.8485 16.4638 10.7831C15.9232 10.5463 15.4322 10.2061 15.0172 9.78088C14.303 9.07761 13.6581 8.30129 12.8531 7.69314C12.6666 7.55267 12.475 7.41923 12.2789 7.29309C11.4581 6.48024 12.3873 5.81264 12.6022 5.73365C12.8272 5.65041 12.6797 5.36672 11.9531 5.37012C11.2264 5.37351 10.5615 5.62068 9.71397 5.95108C9.58804 6.00027 9.45846 6.03918 9.32648 6.06745C8.53452 5.91535 7.72455 5.88615 6.92403 5.98081C5.35322 6.15918 4.09908 6.91682 3.1766 8.2087C2.06829 9.76135 1.80746 11.5263 2.12662 13.3661C2.46245 15.306 3.4341 16.9122 4.92657 18.1675C6.47487 19.4696 8.25733 20.1075 10.2915 19.9852C11.5264 19.913 12.9022 19.744 14.453 18.4054C14.8447 18.6041 15.2547 18.6831 15.9364 18.7426C16.4613 18.7927 16.9663 18.7171 17.3572 18.6338C17.9696 18.5013 17.9271 17.9229 17.7063 17.8176C15.9105 16.9648 16.3047 17.3122 15.9455 17.0311C16.8588 15.9303 18.2338 14.7871 18.7721 11.083C18.8138 10.7882 18.778 10.6031 18.7721 10.3652C18.7688 10.2209 18.8013 10.1639 18.9638 10.1478C19.4146 10.1001 19.852 9.96309 20.2513 9.74436C21.4146 9.09629 21.8846 8.03289 21.9954 6.75713C22.0121 6.56178 21.9921 6.36133 21.7896 6.25856ZM11.6506 17.7403C9.9098 16.3456 9.06565 15.8861 8.71733 15.9057C8.39066 15.9261 8.44983 16.3057 8.5215 16.5537C8.59649 16.7984 8.69399 16.9665 8.83066 17.1814C8.92565 17.3233 8.99065 17.5348 8.73649 17.6936C8.17567 18.0469 7.20152 17.5747 7.15569 17.5518C6.02154 16.8706 5.0724 15.9719 4.40491 14.7429C3.75992 13.5597 3.38493 12.2908 3.32327 10.936C3.3066 10.6082 3.40076 10.4927 3.72076 10.4332C4.14084 10.3513 4.57126 10.3401 4.9949 10.4001C6.77153 10.6651 8.28317 11.4745 9.55148 12.7562C10.2748 13.4867 10.8223 14.359 11.3864 15.2117C11.9864 16.1172 12.6314 16.9801 13.4531 17.6868C13.7431 17.9348 13.9739 18.1234 14.1956 18.2618C13.5272 18.3383 12.4123 18.3553 11.6506 17.7403ZM12.4839 12.2704C12.4838 12.2282 12.4937 12.1866 12.5129 12.1492C12.532 12.1118 12.5598 12.0797 12.5939 12.0557C12.6279 12.0317 12.6672 12.0165 12.7083 12.0114C12.7494 12.0064 12.7911 12.0116 12.8297 12.0266C12.879 12.0446 12.9216 12.0779 12.9515 12.1217C12.9813 12.1656 12.9971 12.2178 12.9964 12.2712C12.9965 12.3057 12.9899 12.3399 12.9769 12.3717C12.964 12.4036 12.9449 12.4325 12.9208 12.4568C12.8968 12.481 12.8683 12.5002 12.8369 12.5131C12.8055 12.526 12.7719 12.5324 12.7381 12.532C12.7045 12.5321 12.6712 12.5254 12.6402 12.5122C12.6092 12.4991 12.5811 12.4798 12.5575 12.4554C12.5339 12.4311 12.5153 12.4021 12.5028 12.3704C12.4903 12.3386 12.4834 12.3046 12.4839 12.2704ZM15.0755 13.626C14.9089 13.6948 14.743 13.7542 14.5839 13.7619C14.3444 13.7704 14.1095 13.6942 13.9189 13.5461C13.6906 13.3508 13.5272 13.2421 13.4589 12.9023C13.4353 12.7363 13.4398 12.5674 13.4722 12.4029C13.5306 12.1251 13.4656 11.9468 13.2731 11.7854C13.1172 11.6529 12.9181 11.6164 12.6997 11.6164C12.625 11.6119 12.5524 11.5892 12.4881 11.5501C12.3964 11.5043 12.3214 11.3887 12.3931 11.246C12.4164 11.2002 12.5264 11.0881 12.5531 11.0677C12.8497 10.8961 13.1922 10.9522 13.5081 11.0813C13.8014 11.2036 14.0231 11.4278 14.3422 11.7455C14.668 12.1285 14.7272 12.2347 14.913 12.5218C15.0597 12.7469 15.193 12.9779 15.2839 13.2421C15.3397 13.4077 15.268 13.5427 15.0755 13.626Z" fill="#4D6BFE" />
</svg>} horizontal />;

export const BFLIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 20.683L12.01 2.5L24 20.683H21.767L12.009 5.878L3.471 18.806H15.593L16.832 20.683H0Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M8.069 16.724L10.142 13.609L12.216 16.724H8.069ZM18.24 20.683L12.572 11.976H14.749L20.435 20.683H18.24ZM19.74 11.676L21.87 8.48602L24 11.676H19.74Z" fill="black" />
</svg>} horizontal />;

These examples cover a variety of use cases on Baseten, from [deploying your first LLM](/examples/deploy-your-first-model) and [image generation](/examples/image-generation) to [transcription](/examples/chains-audio-transcription), [embeddings](/examples/bei), and [RAG pipelines](/examples/chains-build-rag). Whether you're optimizing inference with [TensorRT-LLM](/examples/tensorrt-llm) or deploying a model with [Truss](/development/model/overview), these guides help you build and scale efficiently.

## Featured examples

<CardGroup cols={2}>
  <Card title="Deploy your first model" href="/examples/deploy-your-first-model" />

  <Card title="Fast LLMs with TensorRT-LLM" href="/examples/tensorrt-llm" />

  <Card title="Run any LLM with vLLM" href="/examples/vllm" />

  <Card title="Deploy LLMs with SGLang" href="/examples/sglang" />

  <Card title="Transcribe audio with a Chain" href="/examples/chains-audio-transcription" />

  <Card title="Embeddings with BEI" href="/examples/bei" />
</CardGroup>

## Model library

For a **quick start**, explore the [model library](/examples/models/overview) with prebuilt, ready to deploy in one click models like DeepSeek, Llama, and Qwen.

<CardGroup cols={2}>
  <DeepSeekIconCard title="DeepSeek R1" href="/examples/models/deepseek/deepseek-r1" />

  {" "}

  <OpenAIIconCard title="Whisper V3" href="/examples/models/whisper/whisper-v3-fastest" />

  {" "}

  <QwenIconCard title="Qwen 2.5 32B Coder Instruct" href="/examples/models/qwen/qwen-2-5-32b-coder-instruct" />

  {" "}

  <MetaIconCard title="Llama 3.3 70B Instruct" href="/examples/models/llama/llama-3.3-70B-instruct" />

  {" "}

  <BFLIconCard title="flux-schnell" href="/examples/models/flux/flux-schnell" />

  {" "}

  <MarsIconCard title="MARS6" href="/examples/models/mars/MARS6" />
</CardGroup>

## Training

Train and fine-tune models with Baseten's scalable training infrastructure. From [fine-tuning large language models](/training/getting-started) to training custom models, our platform provides the tools and compute you need.

<CardGroup cols={2}>
  <OpenAIIconCard title="GPT OSS 20B with LoRA" href="https://github.com/basetenlabs/ml-cookbook/tree/main/examples/oss-gpt-20b-axolotl/training" />

  <MetaIconCard title="Llama 3.1 8B SFT" href="https://github.com/basetenlabs/ml-cookbook/tree/main/examples/llama-8b-lora-unsloth/training" />

  <QwenIconCard title="Long Context Qwen3-30B" href="https://github.com/basetenlabs/ml-cookbook/tree/main/recipes/sft/long_context" />

  <QwenIconCard title="Coding with Qwen3-8B" href="https://github.com/basetenlabs/ml-cookbook/tree/main/recipes/rl/ocaml_sepcialist" />
</CardGroup>

Our training infrastructure supports popular frameworks including VERL, Megatron, and Unsloth, as well as models trained directly with Hugging Face Transformers.


# Deploy LLMs with SGLang
Source: https://docs.baseten.co/examples/sglang

Optimized inference for LLMs with SGLang

Another great option for inference is [SGlang](#), which supports a wide range of models and performance optimizations. Besides TensorRT-LLM it is in many cases the state-of-the-art engine for serving LLMs.

## Example: Deploy Qwen 2.5 3B on an L4 via SGLang

This configuration serves [Qwen 2.5 3B](#) with SGLang on an L4 GPU. Running this model is fast and cheap, making it a good example for documentation, but the process of deploying it is very similar to larger models like [Llama 3.3 70B](#).

## Setup

Before you deploy a model, you'll need three quick setup steps.

<Steps>
  <Step title="Create an API key for your Baseten account">
    Create an [API key](https://app.baseten.co/settings/api_keys) and save it as an environment variable:

    ```sh  theme={"system"}
    export BASETEN_API_KEY="abcd.123456"
    ```
  </Step>

  <Step title="Add an access token for Hugging Face">
    Some models require that you accept terms and conditions on Hugging Face before deployment. To prevent issues:

    1. Accept the license for any gated models you wish to access, like [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct).
    2. Create a read-only [user access token](https://huggingface.co/docs/hub/en/security-tokens) from your Hugging Face account.
    3. Add the `hf_access_token` secret [to your Baseten workspace](https://app.baseten.co/settings/secrets).
  </Step>

  <Step title="Install Truss in your local development environment">
    Install the latest version of Truss, our open-source model packaging framework, as well as OpenAI's model inference SDK, with:

    ```sh  theme={"system"}
    pip install --upgrade truss openai
    ```
  </Step>
</Steps>

## Configuration

Start with an empty configuration file.

```sh  theme={"system"}
mkdir qwen-2-5-3b-engine
touch qwen-2-5-3b-engine/config.yaml
```

Below is an example for Qwen 2.5 3B. You can copy-paste it into the empty `config.yaml` we created above.

```yaml config.yaml theme={"system"}
model_metadata:
  example_model_input: # Loads sample request into Baseten playground
    messages:
      - role: system
        content: "You are a helpful assistant."
      - role: user
        content: "What does Tongyi Qianwen mean?"
    stream: true
    model: "baseten-sglang"
    max_tokens: 512
    temperature: 0.6
  tags:
    - openai-compatible
model_name: Qwen 2.5 3B SGLang
environment_variables:
  hf_access_token: null
base_image:
  image: lmsysorg/sglang:v0.4.4.post1-cu125
docker_server:
  start_command: sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) python3 -m sglang.launch_server --model-path Qwen/Qwen2.5-3B-Instruct --host 0.0.0.0 --port 8000"
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /v1/chat/completions
  server_port: 8000
resources:
  accelerator: L4
  use_gpu: true
runtime:
  predict_concurrency: 32
```

## Deployment

Pushing the model to Baseten kicks off a multi-stage deployment process.

```sh  theme={"system"}
truss push qwen-2-5-3b-engine --publish
```

Upon deployment, check your terminal logs or Baseten account to find the URL for the model server.

## Inference

This model is OpenAI compatible and can be called using the OpenAI client.

```python call_model.py theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What does Tongyi Qianwen mean?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

That's it! You have successfully deployed and called a model using SGLang.


# LLM with Streaming
Source: https://docs.baseten.co/examples/streaming

Building an LLM with streaming output

<Card title="View on GitHub" icon="github" horizontal href="https://github.com/basetenlabs/truss-examples/tree/main/qwen/qwen-7b-chat" />

In this example, we go through a Truss that serves the Qwen 7B Chat LLM, and streams the output to the client.

# Why Streaming?

For certain ML models, generations can take a long time. Especially with LLMs, a long output could take
10-20 seconds to generate. However, because LLMs generate tokens in sequence, useful output can be
made available to users sooner. To support this, in Truss, we support streaming output.

# Set up the imports

In this example, we use the HuggingFace transformers library to build a text generation model.

```python model/model.py theme={"system"}
from threading import Thread
from typing import Dict

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from transformers.generation import GenerationConfig
```

# Define the load function

In the `load` function of the Truss, we implement logic
involved in downloading the chat version of the Qwen 7B model and loading it into memory.

```python model/model.py theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self.model = None
        self.tokenizer = None

    def load(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "Qwen/Qwen-7B-Chat", trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            "Qwen/Qwen-7B-Chat", device_map="auto", trust_remote_code=True
        ).eval()
```

# Define the preprocess function

In the `preprocess` function of the Truss, we set up a `generate_args` dictionary with some generation arguments from the inference request to be used in the `predict` function.

```python model/model.py theme={"system"}
    def preprocess(self, request: dict) -> dict:
        generate_args = {
            "max_new_tokens": request.get("max_new_tokens", 512),
            "temperature": request.get("temperature", 0.5),
            "top_p": request.get("top_p", 0.95),
            "top_k": request.get("top_k", 40),
            "repetition_penalty": 1.0,
            "no_repeat_ngram_size": 0,
            "use_cache": True,
            "do_sample": True,
            "eos_token_id": self.tokenizer.eos_token_id,
            "pad_token_id": self.tokenizer.pad_token_id,
        }
        request["generate_args"] = generate_args
        return request
```

# Define the predict function

In the `predict` function of the Truss, we implement the actual
inference logic.

The two main steps are:

* Tokenize the input
* Call the model's `generate` function if we're not streaming the output, otherwise call the `stream` helper function

```python model/model.py theme={"system"}
    def predict(self, request: Dict):
        stream = request.pop("stream", False)
        prompt = request.pop("prompt")
        generation_args = request.pop("generate_args")
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.cuda()

        if stream:
            return self.stream(input_ids, generation_args)

        with torch.no_grad():
            output = self.model.generate(inputs=input_ids, **generation_args)
            return self.tokenizer.decode(output[0])
```

## Define the `stream` helper function

In this helper function, we'll instantiate the `TextIteratorStreamer` object, which we'll later use for
returning the LLM output to users.

```python model/model.py theme={"system"}
    def stream(self, input_ids: list, generation_args: dict):
        streamer = TextIteratorStreamer(self.tokenizer)
```

When creating the generation parameters, ensure to pass the `streamer` object
that we created previously.

```python model/model.py theme={"system"}
        generation_config = GenerationConfig(**generation_args)
        generation_kwargs = {
            "input_ids": input_ids,
            "generation_config": generation_config,
            "return_dict_in_generate": True,
            "output_scores": True,
            "max_new_tokens": generation_args["max_new_tokens"],
            "streamer": streamer,
        }
```

Spawn a thread to run the generation, so that it does not block the main
thread.

```python model/model.py theme={"system"}
        with torch.no_grad():
            # Begin generation in a separate thread
            thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
            thread.start()
```

In Truss, the way to achieve streaming output is to return a generator
that yields content. In this example, we yield the output of the `streamer`,
which produces output and yields it until the generation is complete.

We define this `inner` function to create our generator.

```python model/model.py theme={"system"}
            # Yield generated text as it becomes available
            def inner():
                for text in streamer:
                    yield text
                thread.join()
        return inner()
```

# Setting up the `config.yaml`

Running Qwen 7B requires torch, transformers,
and a few other related libraries.

```yaml config.yaml theme={"system"}
model_name: qwen-7b-chat
model_metadata:
  example_model_input:
    prompt: What is the meaning of life?
requirements:
  - accelerate==0.23.0
  - tiktoken==0.5.1
  - einops==0.6.1
  - scipy==1.11.3
  - transformers_stream_generator==0.0.4
  - peft==0.5.0
  - deepspeed==0.11.1
  - torch==2.0.1
  - transformers==4.32.0
```

## Configure resources for Qwen

We will use an L4 to run this model.

```yaml config.yaml theme={"system"}
resources:
  accelerator: L4
  cpu: "4"
  memory: 16Gi
  use_gpu: true
```

# Deploy Qwen 7B Chat

Deploy the model like you would other Trusses, with:

```bash  theme={"system"}
truss push qwen-7b-chat --publish
```


# Fast LLMs with TensorRT-LLM
Source: https://docs.baseten.co/examples/tensorrt-llm

Optimize LLMs for low latency and high throughput

To get the best performance, we recommend using our [TensorRT-LLM Engine Builder](#) when deploying LLMs. Models deployed with the Engine Builder are [OpenAI compatible](#), support [structured output](#) and [function calling](#), and offer deploy-time post-training quantization to FP8 with Hopper GPUs.

The Engine Builder supports LLMs from the following families, both foundation models and fine-tunes:

* Llama 3.0 and later (including DeepSeek-R1 distills)
* Qwen 2.5 and later (including Math, Coder, and DeepSeek-R1 distills)
* Mistral (all LLMs)

You can download preset Engine Builder configs for common models from the [model library](#).

<Note>
  The Engine Builder does not support vision-language models like [Llama 3.2 11B](#) or [Pixtral](#). For these models, we recommend [vLLM](/examples/vllm).
</Note>

## Example: Deploy Qwen 2.5 3B on an H100

This configuration builds an inference engine to serve [Qwen 2.5 3B](#) on an H100 GPU. Running this model is fast and cheap, making it a good example for documentation, but the process of deploying it is very similar to larger models like [Llama 3.3 70B](#).

## Setup

Before you deploy a model, you'll need three quick setup steps.

<Steps>
  <Step title="Create an API key for your Baseten account">
    Create an [API key](https://app.baseten.co/settings/api_keys) and save it as an environment variable:

    ```sh  theme={"system"}
    export BASETEN_API_KEY="abcd.123456"
    ```
  </Step>

  <Step title="Add an access token for Hugging Face">
    Some models require that you accept terms and conditions on Hugging Face before deployment. To prevent issues:

    1. Accept the license for any gated models you wish to access, like [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct).
    2. Create a read-only [user access token](https://huggingface.co/docs/hub/en/security-tokens) from your Hugging Face account.
    3. Add the `hf_access_token` secret [to your Baseten workspace](https://app.baseten.co/settings/secrets).
  </Step>

  <Step title="Install Truss in your local development environment">
    Install the latest version of Truss, our open-source model packaging framework, as well as OpenAI's model inference SDK, with:

    ```sh  theme={"system"}
    pip install --upgrade truss openai
    ```
  </Step>
</Steps>

## Configuration

Start with an empty configuration file.

```sh  theme={"system"}
mkdir qwen-2-5-3b-engine
touch qwen-2-5-3b-engine/config.yaml
```

This configuration file specifies model information and Engine Builder arguments. You can find dozens of examples in the [model library](#) as well as details on each config option in the [engine builder reference](#).

Below is an example for Qwen 2.5 3B.

```yaml config.yaml theme={"system"}
model_metadata:
  example_model_input: # Loads sample request into Baseten playground
    messages:
        - role: system
        content: "You are a helpful assistant."
        - role: user
        content: "What does Tongyi Qianwen mean?"
    stream: true
    max_tokens: 512
    temperature: 0.6  # Check recommended temperature per model
  repo_id: Qwen/Qwen2.5-3B-Instruct
model_name: Qwen 2.5 3B Instruct
python_version: py39
resources: # Engine Builder GPU cannot be changed post-deployment
  accelerator: H100
  use_gpu: true
secrets: {}
trt_llm:
  build:
    base_model: decoder 
    checkpoint_repository:
      repo: Qwen/Qwen2.5-3B-Instruct
      source: HF
    num_builder_gpus: 1
    quantization_type: no_quant # `fp8_kv` often recommended for large models
    max_seq_len: 32768 # option to very the max sequence length, e.g. 131072 for Llama models
    tensor_parallel_count: 1 # Set equal to number of GPUs
    plugin_configuration:
      use_paged_context_fmha: true
      use_fp8_context_fmha: false # Set to true when using `fp8_kv`
      paged_kv_cache: true
  runtime:
    batch_scheduler_policy: max_utilization
    enable_chunked_context: true
    request_default_max_tokens: 32768 # 131072 for Llama models
```

## Deployment

Pushing the model to Baseten kicks off a multi-stage build and deployment process.

```sh  theme={"system"}
truss push qwen-2-5-3b-engine --publish
```

Upon deployment, check your terminal logs or Baseten account to find the URL for the model server.

## Inference

This model is OpenAI compatible and can be called using the OpenAI client.

```python  theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What does Tongyi Qianwen mean?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

That's it! You have successfully deployed and called an LLM optimized with the TensorRT-LLM Engine Builder. Check the [model library](#) for more examples and the [engine builder reference](#) for details on each config option.


# Text to speech
Source: https://docs.baseten.co/examples/text-to-speech

Building a text-to-speech model with Kokoro

<Card title="View example on GitHub" horizontal icon="github" iconType="light" href="https://github.com/basetenlabs/truss-examples/tree/main/kokoro" />

In this example, we go through a Truss that serves Kokoro, a frontier text-to-speech model.

# Set up imports

We import necessary libraries and enable Hugging Face file transfers. We also download the NLTK tokenizer data.

```python model/model.py theme={"system"}
import logging
import os

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
import base64
import io
import sys
import time

import nltk
import numpy as np
import scipy.io.wavfile as wav
import torch
from huggingface_hub import snapshot_download
from nltk.tokenize import sent_tokenize

from models import build_model
from kokoro import generate

logger = logging.getLogger(__name__)

nltk.download("punkt")
```

# Downloading model weights

We need to prepare model weights by doing the following:

* Create a directory for the model data
* Download the Kokoro model from Hugging Face into the created model data directory
* Add the model data directory to the system path

```python model/model.py theme={"system"}
# Ensure data directory exists
os.makedirs("/app/data/Kokoro-82M", exist_ok=True)

# Download model
snapshot_download(
    repo_id="hexgrad/Kokoro-82M",
    repo_type="model",
    revision="c97b7bbc3e60f447383c79b2f94fee861ff156ac",
    local_dir="/app/data/Kokoro-82M",
    ignore_patterns=["*.onnx", "kokoro-v0_19.pth", "demo/"],
    max_workers=8,
)

# Add data_dir to the system path
sys.path.append("/app/data/Kokoro-82M")
```

# Define the `Model` class and `load` function

In the `load` function of the Truss, we download and set up the model. This `load` function handles setting up the device, loading the model weights, and loading the default voice. We also define the available voices.

```python model/model.py theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self._data_dir = kwargs["data_dir"]
        self.model = None
        self.device = None
        self.default_voice = None
        self.voices = None
        return

    def load(self):
        logger.info("Starting setup...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {self.device}")

        # Load model
        logger.info("Loading model...")
        model_path = "/app/data/Kokoro-82M/fp16/kokoro-v0_19-half.pth"
        logger.info(f"Model path: {model_path}")
        if not os.path.exists(model_path):
            logger.info(f"Error: Model file not found at {model_path}")
            raise FileNotFoundError(f"Model file not found at {model_path}")

        try:
            self.model = build_model(model_path, self.device)
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.info(f"Error loading model: {str(e)}")
            raise

        # Load default voice
        logger.info("Loading default voice...")
        voice_path = "/app/data/Kokoro-82M/voices/af.pt"
        if not os.path.exists(voice_path):
            logger.info(f"Error: Voice file not found at {voice_path}")
            raise FileNotFoundError(f"Voice file not found at {voice_path}")

        try:
            self.default_voice = torch.load(voice_path).to(self.device)
            logger.info("Default voice loaded successfully")
        except Exception as e:
            logger.info(f"Error loading default voice: {str(e)}")
            raise

        # Dictionary of available voices
        self.voices = {
            "default": "af",
            "bella": "af_bella",
            "sarah": "af_sarah",
            "adam": "am_adam",
            "michael": "am_michael",
            "emma": "bf_emma",
            "isabella": "bf_isabella",
            "george": "bm_george",
            "lewis": "bm_lewis",
            "nicole": "af_nicole",
            "sky": "af_sky",
        }
        return
```

# Define the `predict` function

The `predict` function contains the actual inference logic. The steps here are:

* Process input text and handle voice selection
* Chunk text for long inputs
* Generate audio
* Convert resulting audio to base64 and return it

```python model/model.py theme={"system"}
    def predict(self, model_input):
        # Run model inference here
        start = time.time()
        text = str(model_input.get("text", "Hi, I'm kokoro"))
        voice = str(model_input.get("voice", "af"))
        speed = float(model_input.get("speed", 1.0))
        logger.info(
            f"Text has {len(text)} characters. Using voice {voice} and speed {speed}."
        )
        if voice != "af":
            voicepack = torch.load(f"/app/data/Kokoro-82M/voices/{voice}.pt").to(
                self.device
            )
        else:
            voicepack = self.default_voice

        if len(text) >= 400:
            logger.info("Text is longer than 400 characters, splitting into sentences.")
            wavs = []

            def group_sentences(text, max_length=400):
                sentences = sent_tokenize(text)

                # Split long sentences
                while max([len(sent) for sent in sentences]) > max_length:
                    max_sent = max(sentences, key=len)
                    sentences_before = sentences[: sentences.index(max_sent)]
                    sentences_after = sentences[sentences.index(max_sent) + 1 :]
                    new_sentences = [
                        s.strip() + "." for s in max_sent.split(".") if s.strip()
                    ]
                    sentences = sentences_before + new_sentences + sentences_after

                return sentences

            sentences = group_sentences(text)
            logger.info(f"Processing {len(sentences)} chunks. Starting generation...")

            for sent in sentences:
                if sent.strip():
                    audio, _ = generate(
                        self.model, sent.strip(), voicepack, lang=voice[0], speed=speed
                    )
                    # Remove potential artifacts at the end
                    audio = audio[:-2000] if len(audio) > 2000 else audio
                    wavs.append(audio)

            # Concatenate all audio chunks
            audio = np.concatenate(wavs)
        else:
            logger.info("No splitting needed. Generating audio...")
            audio, _ = generate(self.model, text, voicepack, lang=voice[0], speed=speed)

        # Write audio to in-memory buffer
        buffer = io.BytesIO()
        wav.write(buffer, 24000, audio)
        wav_bytes = buffer.getvalue()
        duration_seconds = len(audio) / 24000
        logger.info(
            f"Generation took {time.time()-start} seconds to generate {duration_seconds:.2f} seconds of audio"
        )
        return {"base64": base64.b64encode(wav_bytes).decode("utf-8")}
```

# Setting up the `config.yaml`

Running Kokoro requires a handful of Python libraries, including `torch`, `transformers`, and others.

```yaml config.yaml theme={"system"}
build_commands:
- python3 -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
environment_variables: {}
model_metadata:
  example_model_input: {"text": "Kokoro is a frontier TTS model for its size of 82 million parameters (text in/audio out). On 25 Dec 2024, Kokoro v0.19 weights were permissively released in full fp32 precision under an Apache 2.0 license. As of 2 Jan 2025, 10 unique Voicepacks have been released, and a .onnx version of v0.19 is available.In the weeks leading up to its release, Kokoro v0.19 was the #1🥇 ranked model in TTS Spaces Arena. Kokoro had achieved higher Elo in this single-voice Arena setting over other models, using fewer parameters and less data. Kokoro's ability to top this Elo ladder suggests that the scaling law (Elo vs compute/data/params) for traditional TTS models might have a steeper slope than previously expected.", "voice": "af", "speed": 1.0}
model_name: kokoro
python_version: py311
requirements:
- torch==2.5.1
- transformers==4.48.0
- scipy==1.15.1
- phonemizer==3.3.0
- nltk==3.9.1
- numpy
- huggingface_hub[hf_transfer]
- hf_transfer==0.1.9
- munch==4.0.0
resources:
  accelerator: T4
  use_gpu: true
runtime:
  predict_concurrency: 1
secrets: {}
system_packages:
- espeak-ng
```

## Configuring resources for Kokoro

Note that we need an T4 GPU to run this model.

```yaml config.yaml theme={"system"}
resources:
  accelerator: T4
  use_gpu: true
```

## System Packages

Running Kokoro requires `espeak-ng` to synthesize speech output.

```yaml config.yaml theme={"system"}
system_packages:
- espeak-ng
```

# Deploy the model

Deploy the model like you would other Trusses by running the following command:

```bash  theme={"system"}
truss push kokoro --publish
```

# Run an inference

Use a Python script to call the deployed model and parse its response. In this example, the script sends text input to the model and saves the returned audio (decoded from base64) as a WAV file: `output.wav`.

```python infer.py theme={"system"}
import httpx
import base64

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

with httpx.Client() as client:
    # Make the API request
    resp = client.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={"text": "Hello world", "voice": "af", "speed": 1.0},
        timeout=None,
    )

# Get the base64 encoded audio
response_data = resp.json()
audio_base64 = response_data["base64"]

# Decode the base64 string
audio_bytes = base64.b64decode(audio_base64)

# Write to a WAV file
with open("output.wav", "wb") as f:
    f.write(audio_bytes)

print("Audio saved to output.wav")
```


# Run any LLM with vLLM
Source: https://docs.baseten.co/examples/vllm

Serve a wide range of models

Another great option for inference is [vLLM](#), which supports a wide range of models and performance optimizations.

## Example: Deploy Qwen 2.5 3B on an L4

This configuration serves [Qwen 2.5 3B](#) with vLLM on an L4 GPU. Running this model is fast and cheap, making it a good example for documentation, but the process of deploying it is very similar to larger models like [Llama 3.3 70B](#).

## Setup

Before you deploy a model, you'll need three quick setup steps.

<Steps>
  <Step title="Create an API key for your Baseten account">
    Create an [API key](https://app.baseten.co/settings/api_keys) and save it as an environment variable:

    ```sh  theme={"system"}
    export BASETEN_API_KEY="abcd.123456"
    ```
  </Step>

  <Step title="Add an access token for Hugging Face">
    Some models require that you accept terms and conditions on HuggingFace before deployment. To prevent issues:

    1. Accept the license for any gated models you wish to access, like [Llama 3.3](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct).
    2. Create a read-only [user access token](https://huggingface.co/docs/hub/en/security-tokens) from your Hugging Face account.
    3. Add the `hf_access_token` secret [to your Baseten workspace](https://app.baseten.co/settings/secrets).
  </Step>

  <Step title="Install Truss in your local development environment">
    Install the latest version of Truss, our open-source model packaging framework, as well as OpenAI's model inference SDK, with:

    ```sh  theme={"system"}
    pip install --upgrade truss openai
    ```
  </Step>
</Steps>

## Configuration

Start with an empty configuration file.

```sh  theme={"system"}
mkdir qwen-2-5-3b-engine
touch qwen-2-5-3b-engine/config.yaml
```

Below is an example for Qwen 2.5 3B. You can copy-paste it into the empty `config.yaml` we created above.

```yaml config.yaml theme={"system"}
model_metadata:
  engine_args:
    model: Qwen/Qwen2.5-3B-Instruct
  example_model_input: # Loads sample request into Baseten playground
    messages:
        - role: system
          content: "You are a helpful assistant."
        - role: user
          content: "What does Tongyi Qianwen mean?"
    stream: true
    max_tokens: 512
    temperature: 0.6
base_image:
  image: vllm/vllm-openai:v0.7.3
docker_server:
  start_command: sh -c "HF_TOKEN=$(cat /secrets/hf_access_token) vllm serve Qwen/Qwen2.5-3B-Instruct --enable-prefix-caching --enable-chunked-prefill"
  readiness_endpoint: /health
  liveness_endpoint: /health
  predict_endpoint: /v1/completions
  server_port: 8000
runtime:
  predict_concurrency: 256
resources:
  accelerator: L4
  use_gpu: true
environment_variables:
  hf_access_token: null
```

## Deployment

Pushing the model to Baseten kicks off a multi-stage deployment process.

```sh  theme={"system"}
truss push qwen-2-5-3b-engine --publish
```

Upon deployment, check your terminal logs or Baseten account to find the URL for the model server.

## Inference

This model is OpenAI compatible and can be called using the OpenAI client.

```python call_model.py theme={"system"}
import os
from openai import OpenAI

# https://model-XXXXXXX.api.baseten.co/environments/production/sync/v1
model_url = ""

client = OpenAI(
    base_url=model_url,
    api_key=os.environ.get("BASETEN_API_KEY"),
)

stream = client.chat.completions.create(
    model="Qwen/Qwen2.5-3B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What does Tongyi Qianwen mean?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

That's it! You have successfully deployed and called a model using vLLM.


# Async inference
Source: https://docs.baseten.co/inference/async

Run asynchronous inference on deployed models

Async requests are a "fire and forget" way of executing model inference requests. Instead of waiting for a response from a model, making an async request queues the request, and immediately returns with a request identifier. Optionally, async request results are sent via a `POST` request to a user-defined webhook upon completion.

Use async requests for:

* Long-running inference tasks that may otherwise hit request timeouts.
* Batched inference jobs.
* Prioritizing certain inference requests.

<Note>
  Async fast facts:

  * Async requests can be made to any model—**no model code changes necessary**.
  * Async requests can remain queued for up to 72 hours and run for up to 1 hour.
  * Async requests are **not** compatible with streaming model output.
  * Async request inputs and model outputs are **not** stored after an async request has been completed. Instead, model outputs will be sent to your webhook via a `POST` request.
</Note>

## Quick start

There are two ways to use async inference:

1. Provide a webhook endpoint where model outputs will be sent via a `POST` request. If providing a webhook, you can **use async inference on any model, without making any changes to your model code**.
2. Inside your Truss' `model.py`, save prediction results to cloud storage. If a webhook endpoint is provided, your model outputs will also be sent to your webhook.

Note that Baseten **does not** store model outputs. If you do not wish to use a webhook, your `model.py` must write model outputs to a cloud storage bucket or database as part of its implementation.

<Tabs>
  <Tab title="Quick start with webhook">
    <Steps>
      <Step title="Setup webhook endpoint">
        Set up a webhook endpoint for handling completed async requests. Since Baseten doesn't store model outputs, model outputs from async requests will be sent to your webhook endpoint.

        Before creating your first async request, try running a sample request against your webhook endpoint to ensure that it can consume async predict results properly. Check out [this example webhook test](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code#test_webhook.py).

        We recommend using [this Repl](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code) as a starting point.

        <iframe src="https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code?embed=true" width="100%" height="400" />
      </Step>

      <Step title="Schedule an async predict request">
        Call `/async_predict` on your model. The body of an `/async_predict` request includes the model input in `model_input` field, with the addition of a webhook endpoint (from the previous step) in the `webhook_endpoint` field.

        {" "}

        ```py Python theme={"system"}
        import requests
        import os

        model_id = ""  # Replace this with your model ID
        webhook_endpoint = ""  # Replace this with your webhook endpoint URL
        # Read secrets from environment variables
        baseten_api_key = os.environ["BASETEN_API_KEY"]

        # Call the async_predict endpoint of the production deployment
        resp = requests.post(
            f"https://model-{model_id}.api.baseten.co/production/async_predict",
            headers={"Authorization": f"Api-Key {baseten_api_key}"},
            json={
                "model_input": {"prompt": "hello world!"},
                "webhook_endpoint": webhook_endpoint
                # Optional fields for priority, max_time_in_queue_seconds, etc
            },
        )

        print(resp.json())
        ```

        Save the `request_id` from the `/async_predict` response to check its status or cancel it.

        ```json 201 theme={"system"}
        {
          "request_id": "9876543210abcdef1234567890fedcba"
        }
        ```

        See the [async inference API reference](/reference/inference-api/predict-endpoints/environments-async-predict) for more endpoint details.
      </Step>

      <Step title="Check async predict results">
        Using the `request_id` saved from the previous step, check the status of your async predict request:

        {" "}

        ```py Python theme={"system"}
        import requests
        import os

        model_id = ""
        request_id = ""
        # Read secrets from environment variables
        baseten_api_key = os.environ["BASETEN_API_KEY"]

        resp = requests.get(
            f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
            headers={"Authorization": f"Api-Key {baseten_api_key}"}
        )

        print(resp.json())
        ```

        Once your model has finished executing the request, the async predict result will be sent to your webhook in a `POST` request.

        ```json  theme={"system"}
        {
          "request_id": "9876543210abcdef1234567890fedcba",
          "model_id": "my_model_id",
          "deployment_id": "my_deployment_id",
          "type": "async_request_completed",
          "time": "2024-04-30T01:01:08.883423Z",
          "data": {
            "my_model_output": "hello world!"
          },
          "errors": []
        }
        ```
      </Step>

      <Step title="Secure your webhook">
        We strongly recommend securing the requests sent to your webhooks to validate that they are from Baseten.

        For instructions, see our [guide to securing async requests](/inference/async#securing-async-inference).
      </Step>
    </Steps>
  </Tab>

  <Tab title="Quick start with saving model outputs">
    <Steps>
      <Step title="Update your model to save prediction results">
        Update your Truss's `model.py` to save prediction results to cloud storage, such as S3 or GCS. We recommend implementing this in your model's `postprocess()` method, which will run on CPU after the prediction has completed.
      </Step>

      <Step title="Setup webhook endpoint">
        Optionally, set up a webhook endpoint so Baseten can notify you when your async request completes.

        Before creating your first async request, try running a sample request against your webhook endpoint to ensure that it can consume async predict results properly. Check out [this example webhook test](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code#test_webhook.py).

        We recommend using [this Repl](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code) as a starting point.

        <iframe src="https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code?embed=true" width="100%" height="400" />
      </Step>

      <Step title="Schedule an async predict request">
        Call `/async_predict` on your model. The body of an `/async_predict` request includes the model input in `model_input` field, with the addition of a webhook endpoint (from the previous step) in the `webhook_endpoint` field.

        {" "}

        ```py Python theme={"system"}
        import requests
        import os

        model_id = ""  # Replace this with your model ID
        webhook_endpoint = ""  # Replace this with your webhook endpoint URL
        # Read secrets from environment variables
        baseten_api_key = os.environ["BASETEN_API_KEY"]

        # Call the async_predict endpoint of the production deployment
        resp = requests.post(
            f"https://model-{model_id}.api.baseten.co/production/async_predict",
            headers={"Authorization": f"Api-Key {baseten_api_key}"},
            json={
                "model_input": {"prompt": "hello world!"},
                "webhook_endpoint": webhook_endpoint
                # Optional fields for priority, max_time_in_queue_seconds, etc
            },
        )

        print(resp.json())
        ```

        Save the `request_id` from the `/async_predict` response to check its status or cancel it.

        ```json 201 theme={"system"}
        {
          "request_id": "9876543210abcdef1234567890fedcba"
        }
        ```

        See the [async inference API reference](/reference/inference-api/predict-endpoints/environments-async-predict) for more endpoint details.
      </Step>

      <Step title="Check async predict results">
        Using the `request_id` saved from the previous step, check the status of your async predict request:

        {" "}

        ```py Python theme={"system"}
        import requests
        import os

        model_id = ""
        request_id = ""
        # Read secrets from environment variables
        baseten_api_key = os.environ["BASETEN_API_KEY"]

        resp = requests.get(
            f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
            headers={"Authorization": f"Api-Key {baseten_api_key}"}
        )

        print(resp.json())
        ```

        Once your model has finished executing the request, the async predict result will be sent to your webhook in a `POST` request.

        ```json  theme={"system"}
        {
          "request_id": "9876543210abcdef1234567890fedcba",
          "model_id": "my_model_id",
          "deployment_id": "my_deployment_id",
          "type": "async_request_completed",
          "time": "2024-04-30T01:01:08.883423Z",
          "data": {
            "my_model_output": "hello world!"
          },
          "errors": []
        }
        ```
      </Step>

      <Step title="Secure your webhook">
        We strongly recommend securing the requests sent to your webhooks to validate that they are from Baseten.

        For instructions, see our [guide to securing async requests](/inference/async#securing-async-inference).
      </Step>
    </Steps>
  </Tab>
</Tabs>

<Tip>
  **Chains**: this guide is written for Truss models, but
  [Chains](/development/chain/overview) support async inference likewise. An
  Chain entrypoint can be invoked via its `async_run_remote` endpoint, e.g.
  `https://chain-{chain_id}.api.baseten.co/production/async_run_remote`. The
  internal Chainlet-Chainlet call will still run synchronously.
</Tip>

## User guide

### Configuring the webhook endpoint

Configure your webhook endpoint to handle `POST` requests with [async predict results](/inference/async#processing-async-predict-results). We require that webhook endpoints use HTTPS.

We recommend running a sample request against your webhook endpoint to ensure that it can consume async predict results properly. Try running [this webhook test](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code#test_webhook.py).

For local development, we recommend using [this Repl](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code) as a starting point. This code validates the webhook request and logs the payload.

<iframe src="https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code?embed=true" width="100%" height="400" />

### Making async requests

<Tabs>
  <Tab title="Production deployment">
    ```py Python theme={"system"}
    import requests
    import os

    model_id = ""  # Replace this with your model ID
    webhook_endpoint = ""  # Replace this with your webhook endpoint URL
    # Read secrets from environment variables
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    # Call the async_predict endpoint of the production deployment
    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/production/async_predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "model_input": {"prompt": "hello world!"},
            "webhook_endpoint": webhook_endpoint
            # Optional fields for priority, max_time_in_queue_seconds, etc
        },
    )

    print(resp.json())
    ```
  </Tab>

  <Tab title="Development deployment">
    ```py Python theme={"system"}
    import requests
    import os

    model_id = ""  # Replace this with your model ID
    webhook_endpoint = ""  # Replace this with your webhook endpoint URL
    # Read secrets from environment variables
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    # Call the async_predict endpoint of the development deployment
    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/development/async_predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "model_input": {"prompt": "hello world!"},
            "webhook_endpoint": webhook_endpoint
            # Optional fields for priority, max_time_in_queue_seconds, etc
        },
    )

    print(resp.json())
    ```
  </Tab>

  <Tab title="Other published deployments">
    ```py Python theme={"system"}
    import requests
    import os

    model_id = ""  # Replace this with your model ID
    deployment_id = "" # Replace this with your deployment ID
    webhook_endpoint = ""  # Replace this with your webhook endpoint URL
    # Read secrets from environment variables
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    # Call the async_predict endpoint of the given deployment
    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "model_input": {"prompt": "hello world!"},
            "webhook_endpoint": webhook_endpoint
            # Optional fields for priority, max_time_in_queue_seconds, etc
        },
    )

    print(resp.json())
    ```
  </Tab>
</Tabs>

Create an async request by calling a model's `/async_predict` endpoint. See the [async inference API reference](/reference/inference-api/predict-endpoints/environments-async-predict) for more endpoint details.

### Getting and canceling async requests

<Tabs>
  <Tab title="Get async request details">
    <Info> You may get the status of an async request for up to 1 hour after the request has been completed. </Info>

    ```py Python theme={"system"}
    import requests
    import os

    model_id = ""
    request_id = ""
    # Read secrets from environment variables
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    resp = requests.get(
        f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
        headers={"Authorization": f"Api-Key {baseten_api_key}"}
    )

    print(resp.json())
    ```
  </Tab>

  <Tab title="Cancel async request">
    ```py Python theme={"system"}
    import requests
    import os

    model_id = ""
    request_id = ""
    # Read secrets from environment variables
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    resp = requests.delete(
        f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
        headers={"Authorization": f"Api-Key {baseten_api_key}"}
    )

    print(resp.json())
    ```
  </Tab>
</Tabs>

Manage async requests using the [get async request API endpoint](/reference/inference-api/status-endpoints/get-async-request-status) and the [cancel async request API endpoint](/reference/inference-api/predict-endpoints/cancel-async-request).

### Processing async predict results

Baseten does not store async predict results. Ensure that prediction outputs are either processed by your webhook, or saved to cloud storage in your model code (for example, in your model's `postprocess` method).

If a webhook endpoint was provided in the `/async_predict` request, the async predict results will be sent in a `POST` request to the webhook endpoint. Errors in executing the async prediction will be included in the `errors` field of the async predict result.

Async predict result schema:

* `request_id` (string): the ID of the completed async request. This matches the `request_id` field of the `/async_predict` response.
* `model_id` (string): the ID of the model that executed the request
* `deployment_id` (string): the ID of the deployment that executed the request
* `type` (string): the type of the async predict result. This will always be `"async_request_completed"`, even in error cases.
* `time` (datetime): the time in UTC at which the request was sent to the webhook
* `data` (dict or string): the prediction output
* `errors` (list): any errors that occurred in processing the async request

Example async predict result:

```json  theme={"system"}
{
  "request_id": "9876543210abcdef1234567890fedcba",
  "model_id": "my_model_id",
  "deployment_id": "my_deployment_id",
  "type": "async_request_completed",
  "time": "2024-04-30T01:01:08.883423Z",
  "data": {
    "my_model_output": "hello world!"
  },
  "errors": []
}
```

## Observability

Metrics for async request execution are available on the [Metrics tab](/observability/metrics#async-queue-metrics) of your model dashboard.

* Async requests are included in inference latency and volume metrics.
* A time in async queue chart displays the time an async predict request spent in the `QUEUED` state before getting processed by the model.
* A async queue size chart displays the current number of queued async predict requests.

<Frame caption="The time in async queue chart.">
  <img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1dad9805fe14469dcec6d4a34de6177d" data-og-width="1183" width="1183" data-og-height="674" height="674" data-path="images/async-metrics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=45f877ef07f77b697b8c32b29fd89ace 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=0eff92e843c7801b7fe1c708ae424df9 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=bac3852551a0194b12cdd376a3221a1d 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5c44d8f82786d4fd3511f9cbca34d1ea 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=47e9439cda73a7709776ad4a8c802562 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c4400b8e7eec5caaacd4dd23ba2f922f 2500w" />
</Frame>

# Securing async inference

Since async predict results are sent to a webhook available to anyone over the internet with the endpoint, you'll want to have some verification that these results sent to the webhook are actually coming from Baseten.

We recommend leveraging webhook signatures to secure webhook payloads and ensure they are from Baseten.

This is a two-step process:

1. Create a webhook secret.
2. Validate a webhook signature sent as a header along with the webhook request payload.

## Creating webhook secrets

Webhook secrets can be generated via the [Secrets tab](https://app.baseten.co/settings/secrets).

<Frame caption="Generate a webhook secret with the &#x22;Add webhook secret&#x22; button.">
  <img src="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=21bbb82f4d935acb8d2bef093976ee5c" data-og-width="1276" width="1276" data-og-height="387" height="387" data-path="images/webhook-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=280&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=6363c0d708393aae40a2dea2552fef05 280w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=560&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=9d8e6ca890928b6b17c06fc964c8d07d 560w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=840&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=35f91f3f4cf3ab3c91a23be8e65c20ac 840w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=1100&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=1eddd1a9b52b0d959bb7108772933973 1100w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=1650&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=42d2b29476c3e1e3ef2ac11b5f7eb73a 1650w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=2500&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=19a19ea3aec8c1d8854bf61f23c7893e 2500w" />
</Frame>

A webhook secret looks like:

```
whsec_AbCdEf123456GhIjKlMnOpQrStUvWxYz12345678
```

Ensure this webhook secret is saved securely. It can be viewed at any time and [rotated if necessary](/inference/async#creating-webhook-secrets) in the Secrets tab.

## Validating webhook signatures

If a webhook secret exists, Baseten will include a webhook signature in the `"X-BASETEN-SIGNATURE"` header of the webhook request so you can verify that it is coming from Baseten.

A Baseten signature header looks like:

`"X-BASETEN-SIGNATURE": "v1=signature"`

Where `signature` is an [HMAC](https://docs.python.org/3.12/library/hmac.html#module-hmac) generated using a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash function calculated over the whole async predict result and signed using a webhook secret.

If multiple webhook secrets are active, a signature will be generated using each webhook secret. In the example below, the newer webhook secret was used to create `newsignature` and the older (soon to expire) webhook secret was used to create `oldsignature`.

`"X-BASETEN-SIGNATURE": "v1=newsignature,v1=oldsignature"`

To validate a Baseten signature, we recommend the following. A full Baseten signature validation example can be found in [this Repl](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code#validation.py).

<Steps>
  <Step title="Compare timestamps">
    Compare the async predict result timestamp with the current time and decide if it was received within an acceptable tolerance window.

    ```python  theme={"system"}
    TIMESTAMP_TOLERANCE_SECONDS = 300

    # Check timestamp in async predict result against current time to ensure its within our tolerance
    if (datetime.now(timezone.utc) -
        async_predict_result.time).total_seconds() > TIMESTAMP_TOLERANCE_SECONDS:
      logging.error(
          f"Async predict result was received after {TIMESTAMP_TOLERANCE_SECONDS} seconds and is considered stale, Baseten signature was not validated."
      )
    ```
  </Step>

  <Step title="Recompute Baseten signature">
    Recreate the Baseten signature using webhook secret(s) and the async predict result.

    ```python  theme={"system"}
    WEBHOOK_SECRETS = [] # Add your webhook secrets here

    async_predict_result_json = async_predict_result.model_dump_json()

    # We recompute expected Baseten signatures with each webhook secret
    for webhook_secret in WEBHOOK_SECRETS:
      for actual_signature in baseten_signature.replace("v1=", "").split(","):
        expected_signature = hmac.digest(
            webhook_secret.encode("utf-8"),
            async_predict_result_json.encode("utf-8"),
            hashlib.sha256,
        ).hex()
    ```
  </Step>

  <Step title="Compare signatures">
    Compare the expected Baseten signature with the actual computed signature using [`compare_digest`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest), which will return a boolean representing whether the signatures are indeed the same.

    ```python  theme={"system"}
    hmac.compare_digest(expected_signature, actual_signature)
    ```
  </Step>
</Steps>

## Keeping webhook secrets secure

<Tip> We recommend periodically rotating webhook secrets. </Tip>

In the event that a webhook secret is exposed, you're able to rotate or remove it.

Rotating a secret in the UI will set the existing webhook secret to expire in 24 hours, and generate a new webhook secret. During this period, Baseten will include multiple signatures in the signature headers.

Removing webhook secrets could cause your signature validation to fail. Recreate a webhook secret after deleting and ensure your signature validation code is up to date with the new webhook secret.

## FAQs

### Can I run sync and async requests on the same model?

Yes, you can run both sync and async requests on the same model. Sync requests always take priority over async requests. Keep the following in mind:

* **Rate Limits**: Ensure you adhere to rate limits, as they apply to async requests. [Learn more](/reference/inference-api/predict-endpoints/environments-async-predict#rate-limits)
* **Concurrency**: Both sync and async requests count toward the total number of concurrent requests. [Learn more](/development/model/performance/concurrency)


# Call your model
Source: https://docs.baseten.co/inference/calling-your-model

Run inference on deployed models

Once deployed, your model is accessible via an [API endpoint](/reference/inference-api/overview). To make an inference request, you'll need:

* **Model ID**
* An [API key](https://app.baseten.co/settings/api_keys) for your Baseten account.
* **JSON-serializable model input**

## Predict API endpoints

Baseten provides multiple endpoints for different inference modes:

* [`/predict`](/reference/inference-api/overview#predict-endpoints) – Standard synchronous inference.
* [`/async_predict`](/reference/inference-api/overview#predict-endpoints) – Asynchronous inference for long-running tasks.

Endpoints are available for environments and all deployments. See the [API reference](/reference/inference-api/overview) for details.

## Sync API endpoints

Custom servers support both `predict` endpoints as well as a special `sync` endpoint. By using the `sync` endpoint you are able to call different routes in your custom server.

```
https://model-{model-id}.api.baseten.co/environments/{production}/sync/{route}
```

Here are a few example for the given example that show how the sync endpoint maps to the custom server's routes.

* `https://model-{model_id}.../sync/health` -> `/health`
* `https://model-{model_id}.../sync/items` -> `/items`
* `https://model-{model_id}.../sync/items/123` -> `/items/123`

## OpenAI SDK

When deploying a model with Engine Builder, you will get an OpenAI compatible server. If you are already using one of the OpenAI SDKs, you will simply need to update the base url to your Baseten model URL and include your Baseten API Key.

```python  theme={"system"}
import os
from openai import OpenAI

model_id = "abcdef" # TODO: replace with your model id
api_key = os.environ.get("BASETEN_API_KEY")
model_url = f"https://model-{model_id}.api.baseten.co/environments/production/sync/v1"

client = OpenAI(
    base_url=model_url,
    api_key=api_key,
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

## Alternative invocation methods

* **Truss CLI**: [`truss predict`](/reference/cli/truss/predict)
* **Model Dashboard**: "Playground" button in the Baseten UI


# Concepts
Source: https://docs.baseten.co/inference/concepts



<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=eac4b2c5cb0945c753d3a1353da65bed" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/inference.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=d999899a70e25aaa499b50585acd5d0a 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=61e98026b32c791687eb620f9f12d736 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=31e8c1b82ed6c1735b9a15ac5f3c0d66 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8f7fce9302b66c76e132fd4420118524 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c76330ea0c581db8514aa776ed5cb529 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=cf13be55ca64546fabf0e55cf3ad6255 2500w" />

Inference on Baseten is designed for flexibility, efficiency, and scalability. Models can be served [synchronously](/inference/calling-your-model), [asynchronously](/inference/async), or via [streaming](/inference/streaming) to meet different performance and latency needs.

* [Synchronously](/inference/calling-your-model) inference is ideal for low-latency, real-time responses.
* [Asynchronously](/inference/async) inference handles long-running tasks efficiently without blocking resources.
* [Streaming](/inference/streaming) inference delivers partial results as they become available for faster response times.

Baseten supports various input and output formats, including structured data, binary files, and function calls, making it adaptable to different workloads.


# Function calling (tool use)
Source: https://docs.baseten.co/inference/function-calling

Use an LLM to select amongst provided tools

<Note>
  Function calling requires an LLM deployed using the [TensorRT-LLM Engine
  Builder](/development/model/performance/engine-builder-overview).
</Note>

To use function calling:

1. Define a set of functions/tools in Python.
2. Pass the function set to the LLM with the `tools` argument.
3. Receive selected function(s) as output.

With function calling, it's essential to understand that **the LLM itself is not capable of executing the code in the function**. Instead, the LLM is used to suggest appropriate function(s), if they exist, based on the prompt. Any code execution must be handled outside of the LLM call – a great use for [chains](/development/chain/overview).

## Define functions in Python

Functions can be anything: API calls, ORM access, SQL queries, or just a script. It's essential that functions are well-documented; the LLM relies on the docstrings to select the correct function.

As a simple example, consider the four basic functions of a calculator:

```python  theme={"system"}
def multiply(a: float, b: float):
    """
    A function that multiplies two numbers

    Args:
        a: The first number to multiply
        b: The second number to multiply
    """
    return a * b

def divide(a: float, b: float):
    """
    A function that divides two numbers

    Args:
        a: The dividend
        b: The divisor
    """
    return a / b

def add(a: float, b: float):
    """
    A function that adds two numbers

    Args:
        a: The first number
        b: The second number
    """
    return a + b

def subtract(a: float, b: float):
    """
    A function that subtracts two numbers

    Args:
        a: The number to subtract from
        b: The number to subtract
    """
    return a - b
```

These functions must be serialized into LLM-accessible tools:

```python  theme={"system"}
from transformers.utils import get_json_schema

calculator_functions = {
    'multiply': multiply,
    'divide': divide,
    'add': add,
    'subtract': subtract
}

tools = [get_json_schema(f) for f in calculator_functions.values()]
```

## Pass functions to the LLM

The input spec for models like Llama 3.1 includes a `tools` key that we use to pass the functions:

```python  theme={"system"}
import json
import requests

payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What is 3.14+3.14?"},
    ],
    "tools": tools,  # tools are provided in the same format as OpenAI's API
    "tool_choice": "auto",  # auto is default - the model will choose whether or not to make a function call
}

MODEL_ID = ""
BASETEN_API_KEY = ""

resp = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=payload,
)
```

### tool\_choice: auto (default) – may return a function

The default `tool_choice` option, `auto`, leaves it up to the LLM whether to return one function, multiple functions, or no functions at all, depending on what the model feels is most appropriate based on the prompt.

### tool\_choice: required – will always return a function

The `required` option for `tool_choice` means that the LLM is guaranteed to chose at least one function, no matter what.

### tool\_choice: none – will always return a function

The `none` option for `tool_choice` means that the LLM will **not** return a function, and will instead produce ordinary text output. This is useful when you want to provide the full context of a conversation without adding and dropping the `tools` parameter call-by-call.

### tool\_choice: direct – will return a specified function

You can also pass a specific function directly into the call, which is guaranteed to be returned. This is useful if you want to hardcode specific behavior into your model call for testing or conditional execution.

```python  theme={"system"}
"tool_choice": {"type": "function", "function": {"name": "subtract"}}
```

## Receive function(s) as output

When the model returns functions, they'll be a list that can be parsed as follows:

```python  theme={"system"}
func_calls = json.loads(resp.text)

# In this example, we execute the first function (one of +-/*) on the provided parameters
func_call = func_calls[0]
calculator_functions[func_call["name"]](**func_call["parameters"])
```

After reading the LLM's selection, your execution environment can run the necessary functions. For more on combining LLMs with other logic, see the [chains documentation](/development/chain/overview).


# Integrations
Source: https://docs.baseten.co/inference/integrations

Integrate your models with tools like LangChain, LiteLLM, and more.

<CardGroup cols={2}>
  <Card title="Chainlit" icon="link" iconType="light" href="https://github.com/Chainlit/cookbook/tree/main/baseten-llama-2-chat">
    Build your own open-source ChatGPT with Baseten and Chainlit.
  </Card>

  <Card title="Cline" icon="robot" iconType="light" href="https://www.baseten.co/blog/from-prompt-to-production-baseten-inference-in-your-ide-with-cline/">
    Use frontier open-source models like Kimi K2 and Qwen3 Coder inside your IDE with Baseten and Cline.
  </Card>

  <Card title="HumanLayer" icon="person" iconType="light" href="https://www.humanlayer.dev">
    Build agents with human-in-the-loop powered by Baseten LLMs and HumanLayer.
  </Card>

  <Card title="LlamaIndex" icon="horse" iconType="light" href="https://docs.llamaindex.ai/en/latest/api_reference/llms/baseten/">
    Use Baseten models within your RAG applications with LlamaIndex.
  </Card>

  <Card title="LangChain" icon="bird" iconType="light" href="https://docs.langchain.com/oss/python/integrations/providers/baseten">
    Use your Baseten models with LangChain V1.0 to build workflows and agents.
  </Card>

  <Card title="LiteLLM" icon="grapes" iconType="light" href="https://docs.litellm.ai/docs/providers/baseten">
    Use your Baseten models in LiteLLM projects.
  </Card>

  <Card title="LiveKit" icon="microphone-lines" iconType="light" href="https://docs.livekit.io/agents/integrations/tts/baseten/">
    Build real-time voice agents with TTS models hosted on Baseten.
  </Card>

  <Card title="Vercel" icon="computer" iconType="light" href="https://ai-sdk.dev/providers/ai-sdk-providers/baseten">
    Power your Next.js web apps using Baseten models through AI SDK v5.
  </Card>
</CardGroup>

<Card title="Build your own" icon="hammer" iconType="light" href="mailto:support@baseten.co">
  Want to integrate Baseten with your platform or project? Reach out to
  [support@baseten.co](mailto:support@baseten.co) and we'll help with building
  and marketing the integration.
</Card>


# Model I/O in binary
Source: https://docs.baseten.co/inference/output-format/binary

Decode and save binary model output

Baseten and Truss natively support model I/O in binary and use msgpack encoding for efficiency.

## Deploy a basic Truss for binary I/O

If you need a deployed model to try the invocation examples below, follow these steps to create and deploy a super basic Truss that accepts and returns binary data. The Truss performs no operations and is purely illustrative.

<Accordion title="Steps for deploying an example Truss">
  <Steps>
    <Step title="Create a Truss">
      To create a Truss, run:

      ```sh  theme={"system"}
      truss init binary_test
      ```

      This creates a Truss in a new directory `binary_test`. By default, newly created Trusses implement an identity function that returns the exact input they are given.
    </Step>

    <Step title="Add logging">
      Optionally, modify `binary_test/model/model.py` to log that the data received is of type `bytes`:

      ```python binary_test/model/model.py theme={"system"}
      def predict(self, model_input):
          # Run model inference here
          print(f"Input type: {type(model_input['byte_data'])}")
          return model_input
      ```
    </Step>

    <Step title="Deploy the Truss">
      Deploy the Truss to Baseten with:

      ```sh  theme={"system"}
      truss push
      ```
    </Step>
  </Steps>
</Accordion>

## Send raw bytes as model input

To send binary data as model input:

1. Set the `content-type` HTTP header to `application/octet-stream`
2. Use `msgpack` to encode the data or file
3. Make a POST request to the model

This code sample assumes you have a file `Gettysburg.mp3` in the current working directory. You can download the [11-second file from our CDN](https://cdn.baseten.co/docs/production/Gettysburg.mp3) or replace it with your own file.

```python call_model.py theme={"system"}
import os
import requests
import msgpack


model_id = "MODEL_ID" # Replace with your model ID
deployment = "development" # `development`, `production`, or a deployment ID
baseten_api_key = os.environ["BASETEN_API_KEY"]
# Specify the URL to which you want to send the POST request
url = f"https://model-{model_id}.api.baseten.co/{deployment}/predict"
headers={
    "Authorization": f"Api-Key {baseten_api_key}",
    "content-type": "application/octet-stream",
}

with open('Gettysburg.mp3', 'rb') as file:
    response = requests.post(
        url,
        headers=headers,
        data=msgpack.packb({'byte_data': file.read()})
    )

print(response.status_code)
print(response.headers)
```

<Note>
  To support certain types like numpy and datetime values, you may need to
  extend client-side `msgpack` encoding with the same [encoder and decoder used
  by
  Truss](https://github.com/basetenlabs/truss/blob/main/truss/templates/shared/serialization.py).
</Note>

## Parse raw bytes from model output

To use the output of a non-streaming model response, decode the response content.

```python call_model.py theme={"system"}
# Continues `call_model.py` from above

binary_output = msgpack.unpackb(response.content)

# Change extension if not working with mp3 data
with open('output.mp3', 'wb') as file:
    file.write(binary_output["byte_data"])
```

## Streaming binary outputs

You can also stream output as binary. This is useful for sending large files or reading binary output as it is generated.

In the `model.py`, you must create a streaming output.

```python model/model.py theme={"system"}
# Replace the predict function in your Truss
def predict(self, model_input):
    import os

    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "tmpfile.txt")
    with open(file_path, mode="wb") as file:
            file.write(bytes(model_input["text"], encoding="utf-8"))

    def iterfile():
        # Get the directory of the current file
        current_dir = os.path.dirname(__file__)
        # Construct the full path to the .wav file
        file_path = os.path.join(current_dir, "tmpfile.txt")
        with open(file_path, mode="rb") as file_like:
            yield from file_like

    return iterfile()
```

Then, in your client, you can use streaming output directly without decoding.

```python stream_model.py theme={"system"}
import os
import requests
import json

model_id = "MODEL_ID" # Replace with your model ID
deployment = "development" # `development`, `production`, or a deployment ID
baseten_api_key = os.environ["BASETEN_API_KEY"]
# Specify the URL to which you want to send the POST request
url = f"https://model-{model_id}.api.baseten.co/{deployment}/predict"
headers={
    "Authorization": f"Api-Key {baseten_api_key}",
}

s = requests.Session()
with s.post(
    # Endpoint for production deployment, see API reference for more
    f"https://model-{model_id}.api.baseten.co/{deployment}/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    data=json.dumps({"text": "Lorem Ipsum"}),
    # Include stream=True as an argument so the requests libray knows to stream
    stream=True,
) as response:
    for token in response.iter_content(1):
        print(token) # Prints bytes
```


# Model I/O with files
Source: https://docs.baseten.co/inference/output-format/files

Call models by passing a file or URL

Baseten supports a wide variety of file-based I/O approaches. These examples show our recommendations for working with files during model inference, whether local or remote, public or private, in the Truss or in your invocation code.

## Files as input

### Example: Send a file with JSON-serializable content

The Truss CLI has a `-f` flag to pass file input. If you're using the API endpoint via Python, get file contents with the standard `f.read()` function.

<CodeGroup>
  ```sh Truss CLI theme={"system"}
  truss predict -f input.json
  ```

  ```python Python script theme={"system"}
  import urllib3
  import json

  model_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  # Read input as JSON
  with open("input.json", "r") as f:
      data = json.loads(f.read())

  resp = urllib3.request(
      "POST",
      # Endpoint for production deployment, see API reference for more
      f"https://model-{model_id}.api.baseten.co/production/predict",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json=data
  )

  print(resp.json())
  ```
</CodeGroup>

### Example: Send a file with non-serializable content

The `-f` flag for `truss predict` only applies to JSON-serializable content. For other files, like the audio files required by [MusicGen Melody](https://www.baseten.co/library/musicgen-melody), the file content needs to be base64 encoded before it is sent.

```python  theme={"system"}
import urllib3

model_id = ""
# Read secrets from environment variables
baseten_api_key = os.environ["BASETEN_API_KEY"]

# Open a local file
with open("mymelody.wav", "rb") as f: # mono wav file, 48khz sample rate
    # Convert file contents into JSON-serializable format
    encoded_data = base64.b64encode(f.read())
    encoded_str = encoded_data.decode("utf-8")
# Define the data payload
data = {"prompts": ["happy rock", "energetic EDM", "sad jazz"], "melody": encoded_str, "duration": 8}
# Make the POST request
response = requests.post(url, headers=headers, data=data)
resp = urllib3.request(
    "POST",
    # Endpoint for production deployment, see API reference for more
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)
data = resp.json()["data"]
# Save output to files
for idx, clip in enumerate(data):
    with open(f"clip_{idx}.wav", "wb") as f:
        f.write(base64.b64decode(clip))
```

### Example: Send a URL to a public file

Rather than encoding and serializing a file to send in the HTTP request, you can instead write a Truss that takes a URL as input and loads the content in the `preprocess()` function.

Here's an example from [Whisper in the model library](https://www.baseten.co/library/whisper-v3).

```python  theme={"system"}
from tempfile import NamedTemporaryFile
import requests

# Get file content without blocking GPU
def preprocess(self, request):
    resp = requests.get(request["url"])
    return {"content": resp.content}

# Use file content in model inference
def predict(self, model_input):
    with NamedTemporaryFile() as fp:
        fp.write(model_input["content"])
        result = whisper.transcribe(
            self._model,
            fp.name,
            temperature=0,
            best_of=5,
            beam_size=5,
        )
        segments = [
            {"start": r["start"], "end": r["end"], "text": r["text"]}
            for r in result["segments"]
        ]
    return {
        "language": whisper.tokenizer.LANGUAGES[result["language"]],
        "segments": segments,
        "text": result["text"],
    }
```

## Files as output

### Example: Save model output to local file

When saving model output to a local file, there's nothing Baseten-specific about the code. Just use the standard `>` operator in bash or `file.write()` function in Python to save the model output.

<CodeGroup>
  ```sh Truss CLI theme={"system"}
  truss predict -d '"Model input!"' > output.json
  ```

  ```python Python script theme={"system"}
  import urllib3
  import json

  model_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  # Call model
  resp = urllib3.request(
      "POST",
      # Endpoint for production deployment, see API reference for more
      f"https://model-{model_id}.api.baseten.co/production/predict",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json=json.dumps("Model input!")
  )
  # Write results to file
  with open("output.json", "w") as f:
      f.write(resp.json())
  ```
</CodeGroup>

Output for some models, like image and audio generation models, may need to be decoded before you save it. See our [image generation example](/examples/image-generation) for how to parse base64 output.


# Streaming
Source: https://docs.baseten.co/inference/streaming

How to call a model that has a streaming-capable endpoint.

Any model could be packaged with support for streaming output, but it only makes sense to do so for models where:

* Generating a complete output takes a relatively long time.
* The first tokens of output are useful without the context of the rest of the output.
* Reducing the time to first token improves the user experience.

LLMs in chat applications are the perfect use case for streaming model output.

## Example: Streaming with Mistral

[Mistral 7B Instruct](https://www.baseten.co/library/mistral-7b-instruct) from Baseten's model library is a recent LLM with streaming support. Invocation should be the same for any other model library LLM as well as any Truss that follows the same standard.

[Deploy Mistral 7B Instruct](https://www.baseten.co/library/mistral-7b-instruct) or a similar LLM to run the following examples.

### Truss CLI

The Truss CLI has built-in support for streaming model output.

```sh  theme={"system"}
truss predict -d '{"prompt": "What is the Mistral wind?", "stream": true}'
```

### API endpoint

When using a streaming endpoint with cURL, use the `--no-buffer` flag to stream output as it is received.

As with all cURL invocations, you'll need a model ID and API key.

```sh  theme={"system"}
curl -X POST https://app.baseten.co/models/MODEL_ID/predict \
  -H 'Authorization: Api-Key YOUR_API_KEY' \
  -d '{"prompt": "What is the Mistral wind?", "stream": true}' \
  --no-buffer
```

### Python application

Let's take things a step further and look at how to integrate streaming output with a Python application.

```python  theme={"system"}
import requests
import json
import os

# Model ID for production deployment
model_id = ""
# Read secrets from environment variables
baseten_api_key = os.environ["BASETEN_API_KEY"]

# Open session to enable streaming
s = requests.Session()
with s.post(
    # Endpoint for production deployment, see API reference for more
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    # Include "stream": True in the data dict so the model knows to stream
    data=json.dumps({
      "prompt": "What even is AGI?",
      "stream": True,
      "max_new_tokens": 4096
    }),
    # Include stream=True as an argument so the requests libray knows to stream
    stream=True,
) as resp:
    # Print the generated tokens as they get streamed
    for content in resp.iter_content():
        print(content.decode("utf-8"), end="", flush=True)
```


# Structured output (JSON mode)
Source: https://docs.baseten.co/inference/structured-output

Enforce an output schema on LLM inference

<Note>
  Structured outputs requires an LLM deployed using the [TensorRT-LLM Engine Builder](/development/model/performance/engine-builder-overview).

  If you want to try this structured output example code for yourself, deploy [this implementation of Llama 3.1 8B](/examples/tensorrt-llm).
</Note>

To generate structured outputs:

1. Define an object schema with [Pydantic](https://docs.pydantic.dev/latest/).
2. Pass the schema to the LLM with the `response_format` argument.
3. Receive output that is guaranteed to match the provided schema, including types and validations like `max_length`.

Using structured output, you should observe approximately equivalent tokens per second output speed to an ordinary call to the model after an initial delay for schema processing. If you're interested in the mechanisms behind structured output, check out this [engineering deep dive on our blog](https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms).

## Schema generation with Pydantic

[Pydantic](https://docs.pydantic.dev/latest/) is an industry standard Python library for data validation. With Pydantic, we'll build precise schemas for LLM output to match.

For example, here's a schema for a basic `Person` object.

```python  theme={"system"}
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class Person(BaseModel):
    first_name: str = Field(..., description="The person's first name", max_length=50)
    last_name: str = Field(..., description="The person's last name", max_length=50)
    age: int = Field(..., description="The person's age, must be a non-negative integer")
    email: str = Field(..., description="The person's email address")
```

Structured output supports multiple data types, required and optional fields, and additional validations like `max_length`.

## Add response format to LLM call

<Warning>
  The first time that you pass a given schema for the model, it can take a
  minute for the schema to be processed and cached. Subsequent calls with the
  same schema will run at normal speeds.
</Warning>

Once your object is defined, you can add it as a parameter to your LLM call with the `response_format` field:

```python  theme={"system"}
import json
import requests


payload = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        { "role": "user", "content": "Make up a new person!"},
    ],
    "max_tokens": 512,
    "response_format": {  # Add this parameter to use structured outputs
        "type": "json_schema",
        "json_schema": {"schema": Person.model_json_schema()},
    },
}

MODEL_ID = ""
BASETEN_API_KEY = ""

resp = requests.post(
    f"https://model-{MODEL_ID}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
    json=payload,
)

json.loads(resp.text)
```

The response may have an end of sequence token, which will need to be removed before the JSON can be parsed.

## Parsing LLM output

From the LLM, we expect output in the following format:

```json  theme={"system"}
{
  "first_name": "Astrid",
  "last_name": "Nyxoria",
  "age": 28,
  "email": "astrid.nyxoria@starlightmail.com"
}
```

This example output is valid, which can be double-checked with:

```python  theme={"system"}
Person.parse_raw(resp.text)
```


# Workspace access control
Source: https://docs.baseten.co/observability/access

Workspaces use role-based access control (RBAC) with two roles:

| Permission     | Admin | Creator |
| :------------- | ----- | ------- |
| Manage members | ✅     | ❌       |
| Manage billing | ✅     | ❌       |
| Deploy models  | ✅     | ✅       |
| Call models    | ✅     | ✅       |

<Note>
  **Note:** Startup plan workspaces are limited to five users. [Contact us](mailto:support@baseten.co) if you need to increase this limit.
</Note>


# Best practices for API keys
Source: https://docs.baseten.co/observability/api-keys

Securely access your Baseten models

API keys enable secure access to Baseten models for:

* **Model deployment** via Truss CLI
* **Inference API calls** (`truss predict`, `/wake` requests)
* **Model management** via the [management API](/reference/management-api/overview)
* **Metrics export** via the `/metrics` endpoint

You can create and revoke API keys from your [Baseten account](https://app.baseten.co/settings/api_keys).

## API key scope: Personal vs Workspace

There are two types of API keys on Baseten:

**Personal API Keys:**

* Tied to a user account.
* Inherit full workspace permissions.
* Actions are linked to the specific user.

**Workspace API Keys:**

* Shared across a workspace.
* Can have full access or be restricted to specific models.

<Note>Use personal keys for testing and workspace keys for automation and production.</Note>

## Using API keys with Truss

Add your API key to `~/.trussrc` for authentication:

```sh ~/.trussrc theme={"system"}
[baseten]
remote_provider = baseten
api_key = abcdefgh.1234567890ABCDEFGHIJKL1234567890
remote_url = https://app.baseten.co
```

If rotating keys, update the file with the new key.

### Using API keys with endpoints

Include the API key in request headers:

```sh  theme={"system"}
curl -X POST https://app.baseten.co/models/MODEL_ID/predict \
-H 'Authorization: Api-Key abcdefgh.1234567890ABCDEFGHIJKL1234567890' \
-d 'MODEL_INPUT'
```

Or in Python:

```python  theme={"system"}
headers = {"Authorization": "Api-Key abcdefgh.1234567890ABCDEFGHIJKL1234567890"}
```

## Tips for managing API keys

Best practices for API key use apply to your Baseten API keys:

* Always store API keys securely.
* Never commit API keys to your codebase.
* Never share or leak API keys in notebooks or screenshots.
* Name your API keys to keep them organized.

The [API key list on your Baseten account](https://app.baseten.co/settings/api_keys) shows when each key was first created and last used. Rotate API keys regularly and remove any unused API keys to reduce the risk of accidental leaks.


# Export to Datadog
Source: https://docs.baseten.co/observability/export-metrics/datadog

Export metrics from Baseten to Datadog

<Info> Exporting metrics is in beta mode. </Info>

The Baseten metrics endpoint can be integrated with [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) by configuring a Prometheus receiver that scrapes the endpoint. This allows Baseten metrics to be pushed to a variety of popular exporters—see the [OpenTelemetry registry](https://opentelemetry.io/ecosystem/registry/?component=exporter) for a full list.

**Using OpenTelemetry Collector to push to Datadog**

```yaml config.yaml theme={"system"}
receivers:  
  # Configure a Prometheus receiver to scrape the Baseten metrics endpoint.
  prometheus:
    config:
      scrape_configs:
        - job_name: 'baseten'
          scrape_interval: 60s
          metrics_path: '/metrics'
          scheme: https
          authorization:
            type: "Api-Key"
            credentials: "{BASETEN_API_KEY}"
          static_configs:
            - targets: ['app.baseten.co']
processors:
  batch:
exporters:
  # Configure a Datadog exporter.
  datadog:
    api:
      key: "{DATADOG_API_KEY}"
service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch]
      exporters: [datadog]
```


# Export to Grafana Cloud
Source: https://docs.baseten.co/observability/export-metrics/grafana

Export metrics from Baseten to Grafana Cloud

The Baseten + Grafana Cloud integration enables you to get real-time inference metrics within your existing Grafana setup.

## Video tutorial

See below for step-by-step details from the video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jS-JgwbTVH8?si=UZdHWFgV6hc85ptH" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen" allowfullscreen />

## Set up the integration

For a visual guide, please follow along with the video above.

Open your Grafana Cloud account:

1. Navigate to "Home > Connections > Add new connection".
2. In the search bar, type `Metrics Endpoint` and select it.
3. Give your scrape job a name like `baseten_metrics_scrape`.
4. Set the scrape job URL to `https://app.baseten.co/metrics`.
5. Leave the scrape interval set to `Every minute`.
6. Select `Bearer` for authentication credentials.
7. In your Baseten account, generate a metrics-only workspace API key.
8. In Grafana, enter the Bearer Token as `Api-Key abcd.1234567890` where the latter value is replaced by your API key.
9. Use the "Test Connection" button to ensure everything is entered correctly.
10. Click "Save Scrape Job."
11. Click "Install."
12. In your integrations list, select your new export and go through the "Enable" flow shown on video.

Now, you can navigate to your Dashboards tab, where you will see your data! Please note that it can take a couple of minutes for data to arrive and only new data will be scraped, not historical metrics.

## Build a Grafana dashboard

Importing the data is a great first step, but you'll need a dashboard to properly visualize the incoming information.

We've prepared a basic dashboard to get you started, which you can import by:

1. Downloading `baseten_grafana_dashboard.json` from [this GitHub Gist](https://gist.github.com/philipkiely-baseten/9952e7592775ce1644944fb644ba2a9c).
2. Selecting "New > Import" from the dropdown in the top-right corner of the Dashboard page.
3. Dropping in the provided JSON file.

For visual reference in navigating the dashboard, please see the video above.


# Export to New Relic
Source: https://docs.baseten.co/observability/export-metrics/new-relic

Export metrics from Baseten to New Relic

<Info> Exporting metrics is in beta mode. </Info>

Export Baseten metrics to New Relic by integrating with [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/). This involves configuring a Prometheus receiver that scrapes Baseten's metrics endpoint and configuring a New Relic exporter to send the metrics to your observability backend.

**Using OpenTelemetry Collector to push to New Relic**

```yaml config.yaml theme={"system"}
receivers:  
  # Configure a Prometheus receiver to scrape the Baseten metrics endpoint.
  prometheus:
    config:
      scrape_configs:
        - job_name: 'baseten'
          scrape_interval: 60s
          metrics_path: '/metrics'
          scheme: https
          authorization:
            type: "Api-Key"
            credentials: "{BASETEN_API_KEY}"
          static_configs:
            - targets: ['app.baseten.co']
processors:
  batch:
exporters:
  # Configure a New Relic exporter. Visit New Relic documentation to get your regional otlp endpoint.
  otlphttp/newrelic:
    endpoint: https://otlp.nr-data.net
    headers:
      api-key: "{NEW_RELIC_KEY}"
service:
  pipelines:
    metrics:
      receivers: [prometheus]
      processors: [batch]
      exporters: [otlphttp/newrelic]
```


# Overview
Source: https://docs.baseten.co/observability/export-metrics/overview

Export metrics from Baseten to your observability stack

Baseten provides a metrics endpoint in Prometheus format, allowing integration with observability tools like Prometheus, OpenTelemetry Collector, Datadog Agent, and Vector.

## Setting Up Metrics Scraping

<Steps>
  <Step title="Scrape endpoint: https://app.baseten.co/metrics" />

  <Step title="Authentication">
    Use the Authorization header with a [Baseten API key](https://app.baseten.co/settings/api_keys):

    ```json  theme={"system"}
    {"Authorization": "Api-Key YOUR_API_KEY"}
    ```
  </Step>

  <Step title="Scrape interval ">
    Recommended 1-minute interval (metrics update every 30 seconds).
  </Step>
</Steps>

## Supported Integrations

Baseten metrics can be collected via [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) and exported to:

* [Prometheus](/observability/export-metrics/prometheus)
* [Datadog](/observability/export-metrics/datadog)
* [Grafana](/observability/export-metrics/grafana)
* [New Relic](/observability/export-metrics/new-relic)

For available metrics, see the [supported metrics reference](/observability/export-metrics/supported-metrics).

## Rate Limits

* **6 requests per minute per organization**
* Exceeding this limit results in **HTTP 429 (Too Many Requests)** responses.
* To stay within limits, use a **1-minute scrape interval**.


# Export to Prometheus
Source: https://docs.baseten.co/observability/export-metrics/prometheus

Export metrics from Baseten to Prometheus

<Info> Exporting metrics is in beta mode. </Info>

To integrate with Prometheus, specify the Baseten metrics endpoint in a scrape config. For example:

```yaml prometheus.yml theme={"system"}
global:
  scrape_interval: 60s
scrape_configs:
  - job_name: 'baseten'
    metrics_path: '/metrics'
    authorization:
      type: "Api-Key"
      credentials: "{BASETEN_API_KEY}"
    static_configs:
      - targets: ['app.baseten.co']
    scheme: https
```

See the Prometheus docs for more details on [getting started](https://prometheus.io/docs/prometheus/latest/getting_started/) and [configuration options](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).


# Metrics support matrix
Source: https://docs.baseten.co/observability/export-metrics/supported-metrics

Which metrics can be exported

<Info> Exporting metrics is in beta mode. </Info>

## `baseten_inference_requests_total`

Cumulative number of requests to the model.

Type: `counter`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="status_code" type="label" required>
  The status code of the response.
</ParamField>

<ParamField query="is_async" type="label" required>
  Whether the request was an [async inference request](/inference/async).
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_end_to_end_response_time_seconds`

End-to-end response time in seconds.

Type: `histogram`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="status_code" type="label" required>
  The status code of the response.
</ParamField>

<ParamField query="is_async" type="label" required>
  Whether the request was an [async inference request](/inference/async).
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_container_cpu_usage_seconds_total`

Cumulative CPU time consumed by the container in core-seconds.

Type: `counter`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="replica" type="label" required>
  The ID of the replica.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_replicas_active`

Number of replicas ready to serve model requests.

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_replicas_starting`

Number of replicas starting up--i.e. either waiting for resources to be available or loading the model.

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is
  not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_container_cpu_memory_working_set_bytes`

Cumulative CPU time consumed by the container in seconds.

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="replica" type="label" required>
  The ID of the replica.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_gpu_memory_used`

GPU memory used in MiB.

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="replica" type="label" required>
  The ID of the replica.
</ParamField>

<ParamField query="gpu" type="label" required>
  The ID of the GPU.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the [promote to production process](/deployment/deployments#environments-and-promotion). Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>

## `baseten_gpu_utilization`

GPU utilization as a percentage (between 0 and 100).

Type: `gauge`

Labels:

<ParamField query="model_id" type="label" required>
  The ID of the model.
</ParamField>

<ParamField query="model_name" type="label" required>
  The name of the model.
</ParamField>

<ParamField query="deployment_id" type="label" required>
  The ID of the deployment.
</ParamField>

<ParamField query="replica" type="label" required>
  The ID of the replica.
</ParamField>

<ParamField query="gpu" type="label" required>
  The ID of the GPU.
</ParamField>

<ParamField query="environment" type="label">
  The environment that the deployment corresponds to. Empty if the deployment is not associated with an environment.
</ParamField>

<ParamField query="rollout_phase" type="label">
  The phase of the deployment in the promote to production process. Empty if the deployment is not associated with an environment.

  Possible values:

  * `"promoting"`
  * `"stable"`
</ParamField>


# Status and health
Source: https://docs.baseten.co/observability/health

Every model deployment in your Baseten workspace has a status to represent its activity and health.

## Model statuses

**Healthy states:**

* **Active**: The deployment is active and available. It can be called with `truss predict` or from its API endpoints.
* **Scaled to zero**: The deployment is active but is not consuming resources. It will automatically start up when called, then scale back to zero after traffic ceases.
* **Starting up**: The deployment is starting up from a scaled to zero state after receiving a request.
* **Inactive**: The deployment is unavailable and is not consuming resources. It may be manually reactivated.

**Error states:**

* **Unhealthy**: The deployment is active but is in an unhealthy state due to errors while running, such as an external service it relies on going down or a problem in your Truss that prevents it from responding to requests.
* **Build failed**: The deployment is not active due to a Docker build failure.
* **Deployment failed**: The deployment is not active due to a model deployment failure.

## Fixing unhealthy deployments

If you have an unhealthy or failed deployment, check the model logs to see if there's any indication of what the problem is. You can try deactivating and reactivating your deployment to see if the issue goes away. In the case of an external service outage, you may need to wait for the service to come back up before your deployment works again. For issues inside your Truss, you'll need to diagnose your code to see what is making it unresponsive.


# Metrics
Source: https://docs.baseten.co/observability/metrics

Understand the load and performance of your model

The Metrics tab in the model dashboard provides deployment-specific insights into model load and performance. Use the dropdowns to filter by environment or deployment and time range.

<img noZoom src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=a81bbd59a02719c6814e62fdbfa89ec3" data-og-width="964" width="964" data-og-height="552" height="552" data-path="images/observability.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=15a3fb2106b5f51cd50b261131541f01 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1aa2af207e9f007781838fbd8ca63f50 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=90b0499c358c033b78985f2e08386e2e 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e6dfb73381b1ac4f70a7299f473c2fe7 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=537db025cbccafe7f54dbe0d99c736fe 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/observability.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=daf4644abc87786401d3959d0f05d7d7 2500w" />

## Inference volume

Tracks the request rate over time, segmented by HTTP status codes:

* `2xx`: 🟢 Successful requests
* `4xx`: 🟡 Client errors
* `5xx`: 🔴 Server errors (includes model prediction exceptions)

<Note>
  Note that for non-HTTP models and Chains (WebSockets and gRPC), the status codes will
  reflect the status codes for those protocols.
</Note>

***

## Response time

Measured at different percentiles (p50, p90, p95, p99):

* **End-to-end response time:** Includes cold starts, queuing, and inference (excludes client-side latency). Reflects real-world performance.
* **Inference time:** Covers only model execution, including pre/post-processing. Useful for optimizing single-replica performance.
* **Time to first byte:** Measures the time-to-first-byte time distribution, including any queueing and routing time. A proxy for TTFT.

***

## Request and response size

Measured at different percentiles (p50, p90, p95, p99):

* **Request size:** Tracks the request size distribution. A proxy for input tokens.
* **Response size:** Tracks the response size distribution. A proxy for generated tokens.

***

## Replicas

Tracks the number of **active** and **starting** replicas:

* **Starting:** Waiting for resources or loading the model.
* **Active:** Ready to serve requests.
* For development deployments, a replica is considered active while running the live reload server.

***

## CPU usage and memory

Displays resource utilization across replicas. Metrics are averaged and may not capture short spikes.

### Considerations:

* **High CPU/memory usage**: May degrade performance—consider upgrading to a larger instance type.
* **Low CPU/memory usage**: Possible overprovisioning—switch to a smaller instance to reduce costs.

***

## GPU usage and memory

Shows GPU utilization across replicas.

* **GPU usage**: Percentage of time a kernel function occupies the GPU.
* **GPU memory**: Total memory used.

### Considerations:

* **High GPU load**: Can slow inference—check response time metrics.
* **High memory usage**: May cause out-of-memory failures.
* **Low utilization**: May indicate overprovisioning—consider a smaller GPU.

***

## Async Queue Metrics

* **Time in Async Queue**: Time spent in the async queue before execution (p50, p90, p95, p99).
* **Async Queue Size**: Number of queued async requests.

### Considerations:

* Large queue size indicates requests are queued faster than they are processed.
* To improve async throughput, increase the max replicas or adjust autoscaling concurrency.


# Best practices for secrets
Source: https://docs.baseten.co/observability/secrets

Securely store and access passwords, tokens, keys, and more

Store sensitive credentials like API keys and passwords using the [secrets dashboard](https://app.baseten.co/settings/secrets).

* Secrets are stored as **key-value pairs** (name → token).
* **Naming rules**: Non-alphanumeric characters are treated the same (e.g., `hf_access_token` and `hf-access-token` are identical). Creating a new secret with a similar name overwrites the existing one.
* Changes to secrets **immediately** affect all models using them.

Any model deployed to a workspace will have access to any secrets specified on the workspace.

## Using secrets in Truss

<Steps>
  <Step title="Add the secret name to config.yaml, setting the value to null:">
    ```yaml config.yaml theme={"system"}
    ...
    secrets:
      hf_access_token: null
    ...
    ```

    <Warning>
      Never set the actual value of the secret in `config.yaml` or any other file that gets committed to your codebase.
    </Warning>
  </Step>

  <Step title="Access secrets in model.py:">
    ```py model/model.py theme={"system"}
    def __init__(self, **kwargs):
        self._secrets = kwargs["secrets"]
    ```
  </Step>

  <Step title="Use secrets in load or predict:">
    ```py model/model.py theme={"system"}
    def load(self):
        self._model = pipeline(
            "fill-mask",
            model="baseten/docs-example-gated-model",
            use_auth_token=self._secrets["hf_access_token"]
        )
    ```
  </Step>
</Steps>


# Secure model inference
Source: https://docs.baseten.co/observability/security

Keeping your models safe and private

Baseten maintains [SOC 2 Type II certification](https://www.baseten.co/blog/soc-2-type-2) and [HIPAA compliance](https://www.baseten.co/blog/baseten-announces-hipaa-compliance), with robust security measures beyond compliance.

## Data privacy

Baseten does not store model inputs, outputs, or weights by default.

* **Model inputs/outputs**: Inputs for [async inference](/inference/async) are temporarily stored until processed. Outputs are never stored.
* **Model weights**: Loaded dynamically from sources like Hugging Face, GCS, or S3, moving directly to GPU memory.
  * Users can enable caching via Truss. Cached weights can be permanently deleted on request.
* **Postgres data tables**: Existing users may store data in Baseten’s hosted Postgres tables, which can be deleted anytime.

Baseten’s network accelerator optimizes model downloads. [Contact support](mailto:support@baseten.co) to disable it.

## Workload security

Inference workloads are isolated to protect users and Baseten’s infrastructure.

* **Container security**:
  * No GPUs are shared across users.
  * Security tooling: Falco (Sysdig), Gatekeeper (Pod Security Policies).
  * Minimal privileges for workloads and nodes to limit incident impact.
* **Network security**:
  * Each customer has a dedicated Kubernetes namespace.
  * Isolation enforced via [Calico](https://docs.tigera.io/calico/latest/about).
  * Nodes run in a private subnet with firewall protections.
* **Pentesting**:
  * Extended pentesting by [RunSybil](https://www.runsybil.com/) (ex-OpenAI and CrowdStrike experts).
  * Malicious model deployments tested in a dedicated prod-like environment.

## Self-hosted model inference

Baseten offers single-tenant environments and self-hosted deployments. The cloud version is recommended for ease of setup, cost efficiency, and elastic GPU access.

For self-hosting, [contact support](mailto:support@baseten.co).


# Tracing
Source: https://docs.baseten.co/observability/tracing

Investigate the prediction flow in detail

Baseten’s Truss server includes built-in [OpenTelemetry](https://opentelemetry.io/) (OTEL) instrumentation, with support for custom tracing.

Tracing helps diagnose performance bottlenecks but introduces minor overhead, so it is **disabled by default**.

## Exporting builtin trace data to Honeycomb

1. **Create a Honeycomb API** key and add it to[ Baseten secrets](https://app.baseten.co/settings/secrets).
2. **Update** `config.yaml` for the target model:

```yaml config.yaml theme={"system"}
environment_variables:
  HONEYCOMB_DATASET: your_dataset_name
runtime:
  enable_tracing_data: true
secrets:
  HONEYCOMB_API_KEY: '***'
```

3. **Send requests with tracing**

* Provide traceparent headers for distributed tracing.
* If omitted, Baseten generates random trace IDs.

## Adding custom OTEL instrumentation

To define custom spans and events, integrate OTEL directly:

```python model.py theme={"system"}
import time
from typing import Any, Generator

import opentelemetry.exporter.otlp.proto.http.trace_exporter as oltp_exporter
import opentelemetry.sdk.resources as resources
import opentelemetry.sdk.trace as sdk_trace
import opentelemetry.sdk.trace.export as trace_export
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider

trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({resources.SERVICE_NAME: "UserModel"}))
)
tracer = trace.get_tracer(__name__)
trace_provider = trace.get_tracer_provider()


class Model:
    def __init__(self, **kwargs) -> None:
        honeycomb_api_key = kwargs["secrets"]["HONEYCOMB_API_KEY"]
        honeycomb_exporter = oltp_exporter.OTLPSpanExporter(
            endpoint="https://api.honeycomb.io/v1/traces",
            headers={
                "x-honeycomb-team"   : honeycomb_api_key,
                "x-honeycomb-dataset": "marius_testing_user",
            },
        )
        honeycomb_processor = sdk_trace.export.BatchSpanProcessor(honeycomb_exporter)
        trace_provider.add_span_processor(honeycomb_processor)

    @tracer.start_as_current_span("load_model")
    def load(self):
        ...

    def preprocess(self, model_input):
        with tracer.start_as_current_span("preprocess"):
            ...
            return model_input

    @tracer.start_as_current_span("predict")
    def predict(self, model_input: Any) -> Generator[str, None, None]:
        with tracer.start_as_current_span("start-predict") as span:
            def inner():
                time.sleep(0.01)
                for i in range(5):
                    span.add_event("yield")
                    yield str(i)

            return inner()
```

Baseten’s built-in tracing **does not interfere** with user-defined OTEL implementations.


# Billing and usage
Source: https://docs.baseten.co/observability/usage

Manage payments and track overall Baseten usage

The [billing and usage dashboard](https://app.baseten.co/settings/billing) provides a breakdown of model usage and costs, updated hourly. Usage is tracked per deployment, and any available credits are automatically applied to your bill.

## Billing

### Credits

* New workspaces receive free credits for testing and deployment.
* If credits run out and no payment method is set, models will be deactivated until a payment method is added.

### Payment method

* Payment details can be added or updated on the [billing page](https://app.baseten.co/settings/billing).
* Payment information is securely stored with our payment processor, not Baseten.

On the [billing page](https://app.baseten.co/settings/billing), you can set and update your payment method. Your payment information, including credit card numbers and bank information, is always stored securely with our payments processor and not by Baseten directly.

### Invoice history

* View past invoices and payments in the billing dashboard.
* For questions, [contact support](mailto:support@baseten.co).

***

## Usage and billing FAQs

For full details, see our [pricing page](https://www.baseten.co/pricing/), but here are answers to some common questions:

### How exactly is usage calculated?

* Usage is billed per minute while a model is deploying, scaling, or serving requests.
* Costs are based on the [instance type](/deployment/resources#choosing-the-right-instance-type) used.

### How often are payments due?

* Initially, charges occur when usage **exceeds \$50** or at the **end of the month**, whichever comes first.
* After a history of successful payments, billing occurs **monthly**.

### Do you offer volume discounts?

* Volume discounts are available on the **Pro plan**. [Contact support](mailto:support@baseten.co) for details.

### Do you offer education and non-profit discounts?

* Yes, discounts are available for educational and nonprofit ML projects. [Contact support](mailto:support@baseten.co) to apply.


# Documentation
Source: https://docs.baseten.co/overview

Baseten is a platform for deploying and serving AI models performantly, scalably, and cost-efficiently.

<div class="homepage-bg" />

<div class="homepage-content flex flex-col box-border w-full relative grow mx-auto 2xl:max-w-2xl xl:w-[calc(100%-19rem)] max-w-2xl lg:mt-12">
  <h1 class="inline-block mb-4 text-2xl sm:text-3xl text-gray-900 tracking-tight dark:text-gray-200 font-semibold text-center">
    Build with Baseten
  </h1>

  <div class="mb-8 text-lg prose prose-gray dark:prose-invert text-center px-8">
    Baseten is a platform for deploying and serving AI models performantly,
    scalably, and cost-efficiently.
  </div>

  <CardGroup cols={2}>
    <Card title="Quick start" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-quick-start.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=0d260319305f9d33dcd9709c24fb2856" href="/quickstart" data-og-width="956" width="956" data-og-height="458" height="458" data-path="images/homepage-quick-start.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-quick-start.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f50847061bb46c24995c2b2324dcd317 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-quick-start.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=9b5c1c16a1c0bc8629c399ec9c4b06ff 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-quick-start.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=264a9551ca3c213d60382360b60f79db 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-quick-start.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c750084d5cdd920bb63aa759432e156d 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-quick-start.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3634e8b3c9a1b5b5965da76f8b7bc621 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-quick-start.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=47cc9d8cb99ddbc5209200974f29803c 2500w">
      Choose from common AI/ML usecases and modalities to get started on Baseten quickly.
    </Card>

    <Card title="How Baseten works" href="/concepts/howbasetenworks" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-how-baseten-works.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=140d3dccd789bd16e2b29f0f02533c11" data-og-width="956" width="956" data-og-height="458" height="458" data-path="images/homepage-how-baseten-works.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-how-baseten-works.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1943018606dc849ff843dba0a706f96d 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-how-baseten-works.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=55180fb766000c4a93444e80fde92828 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-how-baseten-works.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=35d1f18bc94b7ff2615b1d0e657ee60f 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-how-baseten-works.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=af7a160bb34e1adc25ad4e2fb52bf78f 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-how-baseten-works.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=edf3d42a2ebe2e507283af54bf0733d5 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/homepage-how-baseten-works.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8078061dba89c6e7d823e39f4e98e068 2500w">
      Baseten makes it easy to deploy, serve, and scale AI models so you can focus on building, not infrastructure.
    </Card>
  </CardGroup>

  <div class="mb-8 mt-8  prose prose-gray dark:prose-invert ">
    <h2 class="inline-block mb-4 text-2xl sm:text-2xl text-gray-900 tracking-tight dark:text-gray-200 font-semibold text-center w-full">
      Baseten is an inference and training platform that lets you:
    </h2>

    #### Deploy dedicated models with full control

    * [Package any model for production](/development/model/overview): Define dependencies, hardware, and custom code without needing to learn Docker. Build with your preferred frameworks (e.g. **PyTorch**, **transformers**, **diffusers**), [inference engines](development/model/performance/concepts) (e.g. **TensorRT-LLM**, **SGLang**, **vLLM**), and serving tools (e.g. **Triton**) as well as [any package](/development/model/configuration) installable via `pip` or `apt`.

    * [Build complex AI systems](/development/chain/overview): Orchestrate multi-step workflows with [Chains](/development/chain/overview), combining models, business logic, and external APIs.

    * [Deploy with confidence](/deployment/concepts): [Autoscale](/deployment/autoscaling) models, manage [environments](/deployment/environments), and roll out updates with zero-downtime deployments.

    * [Run high-performance inference](/inference/concepts): Serve [synchronous](/inference/calling-your-model), [asynchronous](/inference/async), and [streaming](/inference/streaming) predictions with low-latency execution controls.

    * [Monitor and optimize in production](/observability/metrics): Monitor performance, debug issues, and [export metrics](/observability/export-metrics/overview) with built-in observability tooling.

    #### Start fast with model APIs

    * [Try model APIs](/development/model-apis/overview): Model APIs provide a fast path to production with reliable, high-performance inference. Use OpenAI-compatible endpoints to integrate models like Llama, DeepSeek, and Qwen, with built-in support for structured outputs and tool calling.

    #### Pre-train and fine-tune models

    * [Run training jobs on scalable infrastructure](/training/overview): Launch containerized training jobs with configurable environments, compute (CPU/GPU), and resource scaling. Supports any training framework via a framework-agnostic API.

    * [Manage artifacts and streamline workflows](/training/management): Track experiments, organize training runs, and handle large artifacts like checkpoints and logs. Seamlessly transition from training to deployment within the Baseten ecosystem.
  </div>

  <h1 class="inline-block mb-4 text-2xl sm:text-2xl text-gray-900 tracking-tight dark:text-gray-200 font-semibold">
    Resources
  </h1>

  <CardGroup cols={1}>
    <Card title="Examples" href="/examples/overview">
      From deploying AI models to optimizing inference and scaling ML models.
    </Card>

    <Card title="Model library" href="/examples/models/overview">
      Prebuilt, ready to deploy in one click models like DeepSeek, Llama, and
      Qwen.
    </Card>

    <Card title="Explore API reference" href="/reference/overview#api-reference">
      API reference for calling deployed models, Chains or managing models and
      your workspace.
    </Card>
  </CardGroup>
</div>


# Quick start
Source: https://docs.baseten.co/quickstart



<Steps titleSize="h3">
  <Step title="What modality are you working with?">
    Choose from common modalities like LLMs, transcription, and image generation to get started quickly.

    <CardGroup cols={3}>
      <Card title="LLMs" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-chat.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=9e6ec9242ff323addbe7f8ab810e9f92" href="/quickstart/large-language-models" data-og-width="956" width="956" data-og-height="700" height="700" data-path="images/quick-start-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-chat.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=2f0ac4d1005a5c00ccd71d653608b115 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-chat.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8146013c52f4a1f51da785b02fadf7d6 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-chat.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=a3bef04d68ef9bcc2a78c3c379f26595 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-chat.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=500eccc135316c9acc3eb9f54f6a60a2 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-chat.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=181ed7322a8807e256e6e618ff71b3a5 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-chat.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=20af635a21ad4905e5344af2812bd0f1 2500w">
        Build and deploy large language models
      </Card>

      <Card title="Transcription" img="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/quick-start-transcription.png?fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=bc62896847fd112218b9024252e54514" href="/quickstart/transcription" data-og-width="956" width="956" data-og-height="700" height="700" data-path="images/quick-start-transcription.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/quick-start-transcription.png?w=280&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=e25f6438c8905ef1618db355d9a85ace 280w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/quick-start-transcription.png?w=560&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=06e991d9121e8d081bb3468bddac43bb 560w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/quick-start-transcription.png?w=840&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=c3fa359449541049e314577d761f7f7c 840w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/quick-start-transcription.png?w=1100&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=9bc8633c958bf11bd4f193ba7c92c938 1100w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/quick-start-transcription.png?w=1650&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=7bd53f6bbad23d2e1321c95b5cb74aca 1650w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/quick-start-transcription.png?w=2500&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=e6eba7c1a8b5b6648fa6c3360c6727f4 2500w">
        Transcribe audio and video
      </Card>

      <Card title="Image generation" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-image-gen.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=ed7eb39a55a2c2fa3e99e66de74f247f" href="/quickstart/image-generation" data-og-width="956" width="956" data-og-height="700" height="700" data-path="images/quick-start-image-gen.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-image-gen.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=820b3e6ea189259b59c204ab06c8e6c7 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-image-gen.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5d5e52ff83cf55b01963e86c189ade0d 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-image-gen.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=761bc5a39d202e89c03ecdb987a285ee 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-image-gen.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8102b269426cb242a2f5aa98256a7b4a 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-image-gen.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=2be9b8b78ed8073b03bfe64b7526ed75 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-image-gen.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=6047e9c5ab15286e42a67b0f0fbc7f3d 2500w">
        Rapidly generate images
      </Card>

      <Card title="Text to speech" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-text-to-speech.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=4a23cb748e01520527912d9dac1d8f24" href="/quickstart/text-to-speech" data-og-width="956" width="956" data-og-height="700" height="700" data-path="images/quick-start-text-to-speech.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-text-to-speech.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=8e62c3935c0246bc3d72b321cb58cdb6 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-text-to-speech.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=adc40e12b4fd2d779e3e474db70caba2 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-text-to-speech.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=cba0c443ea6707799f43064e17d84419 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-text-to-speech.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=69b00fe8ca0b71a0be1ff15dbc2523ab 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-text-to-speech.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=9ce923a49a7d4ae7e91d0e8706edf33d 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-text-to-speech.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=4d4afb876a79e626d3fef80e80364662 2500w">
        Build humanlike experiences
      </Card>

      <Card title="Compound AI" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-compound-ai.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=35d94f79ebcd5a864f528a475e3e5892" href="/quickstart/compound-ai" data-og-width="956" width="956" data-og-height="700" height="700" data-path="images/quick-start-compound-ai.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-compound-ai.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=d000a88a7d8f6fbf70c34292fa538639 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-compound-ai.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3c0dac476ae1619d241510a64619a1b3 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-compound-ai.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=6a3cab628b2c474b75c2b89891bea1be 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-compound-ai.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=4396cf8eaab9cac66dc5e7682865f283 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-compound-ai.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=806e8c4fffa5726a89e64bac50e32fe4 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-compound-ai.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1c4f4517d07b30aa6ac10a0b6d5ed4ce 2500w">
        Build real-time AI-native applications
      </Card>

      <Card title="Embeddings" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-embeddings.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c301c14c9e64ce66a7b8a4463204ee6d" href="/quickstart/embeddings" data-og-width="956" width="956" data-og-height="700" height="700" data-path="images/quick-start-embeddings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-embeddings.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=2b130318e315108095b3bcc69b3fe0d0 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-embeddings.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=d128ff9feb4617c708c7e307829c138c 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-embeddings.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e65a33bf999c5a562965da1e4ed4e73d 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-embeddings.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=87ff24deebcc76dd08b49adae3138ff7 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-embeddings.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=858016ede7fdba4fcdc76389e81c5510 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-embeddings.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=fc004b9d74cd7c16a7be1e39b5b0d794 2500w">
        Process millions of data points
      </Card>

      <Card title="Custom models" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-custom-models.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5b311851b5ef3c64457a5427a018490e" href="/quickstart/custom-models" data-og-width="956" width="956" data-og-height="700" height="700" data-path="images/quick-start-custom-models.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-custom-models.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e90f3d039b9bb98b54b68d5aa647e121 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-custom-models.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=f47980b0fc8b91e47d1d8b960e132e84 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-custom-models.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=af5e40a6052d67e79aab5649537c5faa 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-custom-models.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=6ed11fdf4929d98bf0ccb2ea56de2981 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-custom-models.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3080035003d95f38c5042f9f5824a83a 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/quick-start-custom-models.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=60d4eb0e4bdb201d50aa26372089a35c 2500w">
        Deploy any model
      </Card>
    </CardGroup>
  </Step>

  <Step title="Select a model or guide to get started...">
    Choose a use case or modality above first...
  </Step>
</Steps>


# Chains CLI reference
Source: https://docs.baseten.co/reference/cli/chains/chains-cli

Deploy, manage, and develop Chains using the Truss CLI.

# Deploy a Chain

## `push`

```sh  theme={"system"}
truss chains push [OPTIONS] SOURCE [ENTRYPOINT]
```

Deploys a chain to a remote environment.

* `SOURCE`: Path to a python file that contains the entrypoint chainlet.
* `ENTRYPOINT` (optional): Class name of the entrypoint chainlet. If omitted, the chainlet tagged with `@chains.mark_entrypoint` is used.

**Options:**

* `--name` (TEXT): Custom name for the chain (defaults to entrypoint name).
* `--publish / --no-publish`: Create chainlets as a published deployment.
* `--promote / --no-promote`: Promote newly deployed chainlets into production.
* `--environment` (TEXT): Deploy chainlets into a particular environment.
* `--wait / --no-wait`: Wait until all chainlets are ready (or deployment
  failed).
* `--watch / --no-watch`: Watches the chains source code and applies live
  patches. Using this option will wait for the chain to be deployed
  (i.e.`--wait` flag is applied), before starting to watch for changes.
  This option requires the deployment to be a development deployment.
* `--experimental-chainlet-names`: (TEXT): Runs `watch`, but only applies
  patches to specified chainlets. The option is a comma-separated list of
  chainlet (display) names. This option can give faster dev loops, but also
  lead to inconsistent deployments. Use with caution and refer to
  [docs](/development/chain/watch).
* `--dryrun`: Produces only generated files, but doesn't deploy anything.
* `--remote` (TEXT): Name of the remote in .trussrc to push to.
* `--log` `[humanfriendly|I|INFO|D|DEBUG]`: Customizes logging.
* `--help`: Show this message and exit.

***

# Live Reload Development

## `watch`

```sh  theme={"system"}
truss chains watch [OPTIONS] SOURCE [ENTRYPOINT]
```

Watches for source code changes and applies live updates to a development deployment.

* `SOURCE`: Path to a Python file containing the entrypoint chainlet.
* `ENTRYPOINT` (optional): Class name of the entrypoint chainlet. If omitted, the chainlet tagged with `@chains.mark_entrypoint` is used.

**Options:**

* `--name` (TEXT): Name of the chain to be deployed, if not given, the
  entrypoint name is used.
* `--remote`: (TEXT): Name of the remote in .trussrc to
  push to.
* `--experimental-chainlet-names`: (TEXT): Runs `watch`, but only applies
  patches to specified chainlets. The option is a comma-separated list of
  chainlet (display) names. This option can give faster dev loops, but also
  lead to inconsistent deployments. Use with caution and refer to
  [docs](/development/chain/watch).
* `--log [humanfriendly|W|WARNING|I|INFO|D|DEBUG]`: Customizes logging.
* `--help`: Show this message and exit.

***

# Initialize a Chain Project

## `init`

```sh  theme={"system"}
truss chains init [OPTIONS] [DIRECTORY]
```

Initializes a chains project directory.

* `DIRECTORY` (optional): Path to a **new or empty directory** for the chain. Defaults to the **current directory** if omitted.

Options:

* `--log LEVEL` → Set log verbosity `[humanfriendly | INFO | DEBUG]`.
* `--help` → Show command details.


# Training CLI reference
Source: https://docs.baseten.co/reference/cli/training/training-cli

Deploy, manage, and monitor training jobs using the Truss CLI.

# Initialize Training Jobs

## `init`

```sh  theme={"system"}
truss train init [OPTIONS]
```

Initializes files needed to launch a training job. If no options passed, initializes an empty training project.

**Options:**

* `--examples`: A single example or comma separated list of verified [examples](https://github.com/basetenlabs/ml-cookbook/tree/main/examples).
* `--target-directory`: Location to initialize the example/s or empty training project.

***

# Deploy Training Jobs

## `push`

```sh  theme={"system"}
truss train push [OPTIONS] CONFIG
```

Deploys and runs a training job.

* `CONFIG`: Path to a training configuration file.

**Options:**

* `--tail`: Tail status and logs after pushing the training job.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc to push to.

***

# Monitor Training Jobs

## `logs`

```sh  theme={"system"}
truss train logs [OPTIONS]
```

Fetch and display logs for a training job.

**Options:**

* `--job-id` (TEXT): Job ID to fetch logs from.
* `--tail`: Continuously stream new logs.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

## `metrics`

```sh  theme={"system"}
truss train metrics [OPTIONS]
```

Get metrics for a training job.

**Options:**

* `--job-id` (TEXT): Job ID to fetch metrics from.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

## `view`

```sh  theme={"system"}
truss train view [OPTIONS]
```

List and view training jobs.

**Options:**

* `--project` (TEXT): View training jobs for a specific project (ID or name).
* `--job-id` (TEXT): View details of a specific training job.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

***

# Manage Training Jobs

## `stop`

```sh  theme={"system"}
truss train stop [OPTIONS]
```

Stop a running training job.

**Options:**

* `--project` (TEXT): Specify the project (ID or name) to stop a training job from.
* `--job-id` (TEXT): ID of the job to stop.
* `--all`: Stop all running jobs.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

# Manage Training Cache

The training cache is scoped to a specific training project. The CLI allows you to see a summary of the contents in the cache to
help you manage your storage.

## `cache summarize`

```sh  theme={"system"}
truss train cache summarize <project_name or project_id> [OPTIONS]
```

View the contents of the training cache in a table. Optionally sort by different column names (e.g. modified, size, etc.)

**Options:**

* `--sort` (TEXT): column to sort by
* `--order` (TEXT): Ascending (asc) or descending (desc) order for sorting
* `--remote` (TEXT): Name of the remote in .trussrc.

# Manage Checkpoints

## `deploy_checkpoints`

```sh  theme={"system"}
truss train deploy_checkpoints [OPTIONS]
```

Deploy model checkpoints from a training job.

## `get_checkpoint_urls`

```sh  theme={"system"}
truss train get_checkpoint_urls [OPTIONS]
```

Get a list of URL's to checkpoint artifacts for a training job

**Options:**

* `--job-id` (TEXT): Job ID containing the checkpoints.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

**Options:**

* `--project` (TEXT): Project (ID or name) name containing the checkpoints.
* `--job-id` (TEXT): Job ID containing the checkpoints.
* `--config` (TEXT): Path to a Python file defining a DeployCheckpointsConfig.
* `--dry-run`: Generate a truss config without deploying.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

## `recreate`

```sh  theme={"system"}
truss train recreate [OPTIONS]
```

Recreate an existing training job from an existing job ID. If no job ID is provided, it will default to the last created active training job and ask for confirmation first.

**Options:**

* `--job-id` (TEXT): Existing Job ID of Training Job to recreate.
* `--tail`: Tail status and logs after recreation.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

## `download`

```sh  theme={"system"}
truss train download [OPTIONS]
```

Download training job artifacts.

**Options:**

* `--job-id` (TEXT): Job ID to download artifacts from. (Required)
* `--target-directory` (PATH): Directory where the file should be downloaded. Defaults to current directory.
* `--no-unzip`: Instructs truss to not unzip the compressed file upon download.
* `--help`: Show this message and exit.
* `--remote` (TEXT): Name of the remote in .trussrc.

# Ignoring files and folders

To ignore specific files or folders, place a `.truss_ignore` file in the root directory of your project. Define the files or folders you want `truss` to ignore.

These can be absolute paths or paths relative to the location of the `.truss_ignore`

```plaintext .truss_ignore theme={"system"}
# Python cache files
__pycache__/
*.pyc
*.pyo
*.pyd

# Type checking
.mypy_cache/
# Testing
.pytest_cache/

# Some large files
data/
```


# truss cleanup
Source: https://docs.baseten.co/reference/cli/truss/cleanup

Clean up truss data.

```
truss cleanup [OPTIONS]
```

Truss creates temporary directories for various operations such as for building Docker images. This command clears that data to free up disk space.

### Options

<ParamField body="--help">
  Show help message and exit.
</ParamField>


# truss container
Source: https://docs.baseten.co/reference/cli/truss/container

Subcommands for truss container.

```
truss container [OPTIONS] COMMAND [ARGS]...
```

### Options

<ParamField body="--help">
  Show help message and exit.
</ParamField>

## truss container kill

Kills containers related to Truss.

```
truss container kill [OPTIONS] [TARGET_DIRECTORY]
```

### Options

<ParamField body="--help">
  Show help message and exit.
</ParamField>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="str">
  A Truss directory. If none, use current directory.
</ParamField>

## truss container kill-all

Kills all Truss containers that are not manually persisted.

```
truss container kill-all [OPTIONS]
```

### Options

<ParamField body="--help">
  Show help message and exit.
</ParamField>

## truss container logs

Get logs in a container is running for a Truss.

```
truss container logs [OPTIONS] [TARGET_DIRECTORY]
```

### Options

<ParamField body="--help">
  Show help message and exit.
</ParamField>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="str">
  A Truss directory. If none, use current directory.
</ParamField>


# truss image
Source: https://docs.baseten.co/reference/cli/truss/image

Subcommands for truss image.

```
truss image [OPTIONS] COMMAND [ARGS]...
```

### Options

<ParamField body="--help">
  Show help message and exit.
</ParamField>

## truss image build

Builds the docker image for a Truss.

```
truss image build [OPTIONS] [TARGET_DIRECTORY] [BUILD_DIR]
```

### Options

<ParamField body="--tag" type="TEXT">
  Docker image tag.
</ParamField>

<ParamField body="--help">
  Show help message and exit.
</ParamField>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="Optional">
  A Truss directory. If none, use current directory.
</ParamField>

<ParamField body="BUILD_DIR" type="Optional">
  Image context. If none, a temp directory is created.
</ParamField>

## truss image build-context

Create a docker build context for a Truss.

```
truss image build-context [OPTIONS] BUILD_DIR [TARGET_DIRECTORY]
```

### Options

<ParamField body="--help">
  Show help message and exit.
</ParamField>

### Arguments

<ParamField body="BUILD_DIR" type="Optional">
  Folder where image context is built for Truss.
</ParamField>

<ParamField body="TARGET_DIRECTORY" type="Optional">
  A Truss directory. If none, use current directory.
</ParamField>

## truss image run

Runs the docker image for a Truss.

```
truss image run [OPTIONS] [TARGET_DIRECTORY] [BUILD_DIR]
```

### Options

<ParamField body="--tag" type="TEXT">
  Docker build image tag.
</ParamField>

<ParamField body="--port" type="INTEGER">
  Local port used to run image.
</ParamField>

<ParamField body="--attach">
  Flag for attaching the process.
</ParamField>

<ParamField body="--help">
  Show help message and exit.
</ParamField>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="Optional">
  A Truss directory. If none, use current directory.
</ParamField>

<ParamField body="BUILD_DIR" type="Optional">
  Image context. If none, a temp directory is created.
</ParamField>


# truss init
Source: https://docs.baseten.co/reference/cli/truss/init

Create a new Truss.

```
truss init [OPTIONS] TARGET_DIRECTORY
```

## Options

<ParamField body="-b, --backend" type="TrussServer|TGI|VLLM">
  What type of server to create. Default: `TrussServer`.
</ParamField>

<ParamField body="-n, --name" type="STRING">
  The value assigned to `model_name` in `config.yaml`.
</ParamField>

<ParamField body="--help">
  Show help message and exit.
</ParamField>

## Arguments

<ParamField body="TARGET_DIRECTORY" type="str">
  A Truss is created in this directory.
</ParamField>

## Example

```
truss init my_truss_directory
```

```
truss init --name "My Truss" my_truss_directory
```


# truss login
Source: https://docs.baseten.co/reference/cli/truss/login

Authenticate with Baseten.

Authenticate with Baseten.

```
truss login [OPTIONS]
```

Authenticates with Baseten, storing the API key in the local configuration file.

If used with no options, runs in interactive mode. Otherwise, the API key can be passed as an option.

### Options

<ParamField body="--api-key">
  Baseten API Key. If this is passed, the command runs in non-interactive mode.
</ParamField>


# Overview
Source: https://docs.baseten.co/reference/cli/truss/overview

Details on Truss CLI and configuration options

```Usage  theme={"system"}
truss [OPTIONS] COMMAND [ARGS]...
```

### Options

<ParamField body="--version">Show the version and exit.</ParamField>

<ParamField body="--help">Show help message and exit.</ParamField>

### Main usage

<CardGroup cols={1}>
  <Card title="truss login" href="/reference/cli/truss/login">
    Authenticate with Baseten.
  </Card>

  <Card title="truss init" href="/reference/cli/truss/init">
    Create a new Truss.
  </Card>

  <Card title="truss push" href="/reference/cli/truss/push">
    Pushes a Truss to a TrussRemote.
  </Card>

  <Card title="truss watch" href="/reference/cli/truss/watch">
    Seamless remote development with Truss.
  </Card>

  <Card title="truss predict" href="/reference/cli/truss/predict">
    Invokes the packaged model.
  </Card>
</CardGroup>

### Advanced usage

<CardGroup cols={1}>
  <Card title="truss run-python" href="/reference/cli/truss/run-python">
    Runs a Python script in the same environment as your Truss.
  </Card>

  <Card title="truss image" href="/reference/cli/truss/image">
    Subcommands for `truss image`.
  </Card>

  <Card title="truss container" href="/reference/cli/truss/container">
    Subcommands for `truss container`.
  </Card>

  <Card title="truss cleanup" href="/reference/cli/truss/cleanup">
    Clean up Truss data.
  </Card>
</CardGroup>


# truss predict
Source: https://docs.baseten.co/reference/cli/truss/predict

Invokes the packaged model.

```
truss predict [OPTIONS]
```

## Options

<ParamField body="--remote" type="TEXT">
  Name of the remote in .trussrc to patch changes to.
</ParamField>

<ParamField body="-d, --data" type="TEXT">
  String formatted as json that represents request.
</ParamField>

<ParamField body="-f, --file" type="PATH">
  Path to json file containing the request.
</ParamField>

<ParamField body="--model_version" type="TEXT">
  ID of model version to invoke.
</ParamField>

<ParamField body="--model" type="TEXT">
  ID of model to invoke.
</ParamField>

<ParamField body="--help">
  Show help message and exit.
</ParamField>

## Arguments

<ParamField body="TARGET_DIRECTORY" type="Optional">
  A Truss directory. If none, use current directory.
</ParamField>

## Examples

```
truss predict -d '{"prompt": "What is the meaning of life?"}'
```

```
truss predict --published -f my-prompt.json
```


# truss push
Source: https://docs.baseten.co/reference/cli/truss/push

Pushes a truss to a TrussRemote.

```Usage  theme={"system"}
truss push [OPTIONS] [TARGET_DIRECTORY]
```

## Options

<ParamField body="--remote" type="TEXT">
  Name of the remote in .trussrc to patch changes to.
</ParamField>

<ParamField body="--publish" type="BOOL">
  Push the truss as a published deployment. If no production deployment exists, promote the truss to production after deploy completes.
</ParamField>

<ParamField body="--promote" type="BOOL">
  Push the truss as a published deployment. Even if a production deployment exists, promote the truss to production after deploy completes.
</ParamField>

<ParamField body="--environment" type="TEXT">
  Push the truss as a published deployment. Promote the truss into the environment after deploy completes.
</ParamField>

<ParamField body="--preserve-previous-production-deployment" type="BOOL">
  Preserve the previous production deployment's autoscaling setting. When not specified, the previous production deployment will be updated to allow it to scale to zero. Can only be use in combination with `--promote` option.
</ParamField>

<ParamField body="--model-name" type="TEXT">
  Name of the model
</ParamField>

<ParamField body="--deployment-name" type="TEXT">
  Name of the deployment created by the push. Can only be used in combination with `--publish` or `--environment`. Deployment name must only contain alphanumeric, '.', '-' or '\_' characters.
</ParamField>

<ParamField body="--wait" type="BOOL">
  Whether to wait for deployment to complete before returning. If the deploy or build fails, will return with a non-zero exit code.
</ParamField>

<ParamField body="--timeout-seconds" type="INTEGER">
  Maximum time to wait for deployment to complete in seconds. Without specifying, the command will not complete until the deployment is complete.
</ParamField>

<ParamField body="--help">
  Show help message and exit.
</ParamField>

## Arguments

<ParamField body="TARGET_DIRECTORY" type="Optional">
  A Truss directory. If none, use current directory.
</ParamField>

## Examples

```
truss push
```

```
truss push --publish /path/to/my-truss
```

```
truss push --remote baseten --publish
```

```
truss push --remote baseten --publish --deployment-name my-truss_1.0
```


# truss run-python
Source: https://docs.baseten.co/reference/cli/truss/run-python

Subcommands for truss run-python.

```
truss run-python [OPTIONS] SCRIPT [TARGET_DIRECTORY]
```

Runs selected script in the same environment as your Truss. It builds a Docker
image matching your Truss environment, mounts the script you supply, and then
runs the script.

### Options

<ParamField body="--help">
  Show help message and exit.
</ParamField>

### Arguments

<ParamField body="SCRIPT" type="Required">
  Path to Python script to run.
</ParamField>

<ParamField body="TARGET_DIRECTORY" type="Optional">
  A Truss directory. If none, use current directory.
</ParamField>


# truss watch
Source: https://docs.baseten.co/reference/cli/truss/watch

Seamless remote development with truss.

```
truss watch [OPTIONS] [TARGET_DIRECTORY]
```

### Options

<ParamField body="--remote" type="TEXT">
  Name of the remote in .trussrc to patch changes to.
</ParamField>

<ParamField body="--logs" type="BOOL">
  Automatically open remote logs tab.
</ParamField>

<ParamField body="--help">
  Show help message and exit.
</ParamField>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="Optional">
  A Truss directory. If none, use current directory.
</ParamField>

### Examples

```
truss watch
```

```
truss watch /path/to/my-truss
```

```
truss watch --remote baseten
```


# Overview
Source: https://docs.baseten.co/reference/inference-api/overview

The inference API is used to call deployed models and chains.

Each deployment has a dedicated subdomain on `api.baseten.co` for optimized routing.

**For models**, the endpoints follow this format:

```
https://model-{model_id}.api.baseten.co/{deployment_type_or_id}/{endpoint}
```

**For chains**, the endpoints follow this format:

```
https://chain-{chain_id}.api.baseten.co/{deployment_type_or_id}/{endpoint}
```

**Where:**

* `model_id` – The model's alphanumeric ID (found in your model dashboard).
* `chain_id` – The chain's alphanumeric ID (found in your chain dashboard).
* `deployment_type_or_id` – Either `development`, `production`, or a specific deployment’s alphanumeric ID.
* `endpoint` – The API action, such as `predict`.

For long-running tasks, the inference API supports [asynchronous inference](/inference/async) with priority queuing.

## Predict endpoints

<Tabs>
  <Tab title="Models">
    | Method      | Endpoint                                                                                                           | Description                                                                                                 |
    | :---------- | :----------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
    | `POST`      | [`/environments/{env_name}/predict`](/reference/inference-api/predict-endpoints/environments-predict)              | Call an **environment**                                                                                     |
    | `POST`      | [`/development/predict`](/reference/inference-api/predict-endpoints/development-predict)                           | Call the **development deployment**                                                                         |
    | `POST`      | [`/deployment/{deployment_id}/predict`](/reference/inference-api/predict-endpoints/deployment-predict)             | Call any **deployment**                                                                                     |
    | `POST`      | [`/environments/{env_name}/async_predict`](/reference/inference-api/predict-endpoints/environments-async-predict)  | For [Async inference](/inference/async), call the deployment associated with the specified **environment**. |
    | `POST`      | [`/development/async_predict`](/reference/inference-api/predict-endpoints/development-async-predict)               | For [Async inference](/inference/async), call the **development deployment**.                               |
    | `POST`      | [`/deployment/{deployment_id}/async_predict`](/reference/inference-api/predict-endpoints/deployment-async-predict) | For [Async inference](/inference/async), call any published **deployment** of your model.                   |
    | `WEBSOCKET` | [`/environments/{env_name}/websocket`](/reference/inference-api/predict-endpoints/environments-websocket)          | For WebSockets, connect to an **environment**.                                                              |
    | `WEBSOCKET` | [`/development/websocket`](/reference/inference-api/predict-endpoints/development-websocket.mdx)                   | For WebSockets, connect to the **development deployment**.                                                  |
    | `WEBSOCKET` | [`/deployment/{deployment_id}/websocket`](/reference/inference-api/predict-endpoints/deployment-websocket.mdx)     | For WebSockets, connect to a **deployment**.                                                                |
  </Tab>

  <Tab title="Chains">
    | Method      | Endpoint                                                                                                                 | Description                                                                                                       |
    | :---------- | :----------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
    | `POST`      | [`/environments/{env_name}/run_remote`](/reference/inference-api/predict-endpoints/environments-run-remote)              | Call a Chain **environment**                                                                                      |
    | `POST`      | [`/development/run_remote`](/reference/inference-api/predict-endpoints/development-run-remote)                           | Call a Chain **development deployment**                                                                           |
    | `POST`      | [`/deployment/{deployment_id}/run_remote`](/reference/inference-api/predict-endpoints/deployment-run-remote)             | Call a Chain **deployment**                                                                                       |
    | `POST`      | [`/environments/{env_name}/async_run_remote`](/reference/inference-api/predict-endpoints/environments-async-run-remote)  | For [Async inference](/inference/async), call the Chain deployment associated with the specified **environment**. |
    | `POST`      | [`/development/async_run_remote`](/reference/inference-api/predict-endpoints/development-async-run-remote)               | For [Async inference](/inference/async), call a Chain **development deployment**.                                 |
    | `POST`      | [`/deployment/{deployment_id}/async_run_remote`](/reference/inference-api/predict-endpoints/deployment-async-run-remote) | For [Async inference](/inference/async), call any published Chain **deployment**.                                 |
    | `WEBSOCKET` | [`/environments/{env_name}/websocket`](/reference/inference-api/predict-endpoints/environments-websocket)                | For WebSockets, connect to an **environment**.                                                                    |
    | `WEBSOCKET` | [`/development/websocket`](/reference/inference-api/predict-endpoints/development-websocket.mdx)                         | For WebSockets, connect to the **development deployment**.                                                        |
    | `WEBSOCKET` | [`/deployment/{deployment_id}/websocket`](/reference/inference-api/predict-endpoints/deployment-websocket.mdx)           | For WebSockets, connect to a **deployment**.                                                                      |
  </Tab>
</Tabs>

## Async status endpoints

| Method | Endpoint                                                                                                                        | Description                                                                               |
| :----- | :------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------- |
| `GET`  | [`/async_request/{request_id}`](/reference/inference-api/status-endpoints/get-async-request-status)                             | Get the **status** of an **async request**.                                               |
| `DEL`  | [`/async_request/{request_id}`](/reference/inference-api/predict-endpoints/cancel-async-request)                                | **Cancel** an async request.                                                              |
| `GET`  | [`/environments/{env_name}/async_queue_status`](/reference/inference-api/status-endpoints/environments-get-async-queue-status)  | Get the **async queue status** for a model associated with the **specified environment**. |
| `GET`  | [`/development/async_queue_status`](/reference/inference-api/status-endpoints/development-get-async-queue-status)               | Get the **status** of a **development deployment’s** async queue.                         |
| `GET`  | [`/deployment/{deployment_id}/async_queue_status`](/reference/inference-api/status-endpoints/deployment-get-async-queue-status) | Get the **status** of a **deployment’s** async queue.                                     |

## Wake endpoints

| Method | Endpoint                                                                            | Description                                        |
| :----- | :---------------------------------------------------------------------------------- | :------------------------------------------------- |
| `POST` | [`/production/wake`](/reference/inference-api/wake/production-wake)                 | Wake the **production environment** of your model. |
| `POST` | [`/development/wake`](/reference/inference-api/wake/development-wake)               | Wake the **development deployment** of your model. |
| `POST` | [`/deployment/{deployment_id}/wake`](/reference/inference-api/wake/deployment-wake) | Wake any **deployment** of your model.             |


# Async cancel request
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/cancel-async-request

DELETE https://model-{model_id}.api.baseten.co/async_request/{request_id}
Use this endpoint to cancel a queued async request.

Only `QUEUED` requests may be canceled.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField path="model_id" type="string" required>
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField path="chain_id" type="string" required>
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

<ParamField path="request_id" type="string" required>
  The ID of the async request.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<ResponseField name="request_id" type="string" required>
  The ID of the async request.
</ResponseField>

<ResponseField name="canceled" type="boolean" required>
  Whether the request was canceled.
</ResponseField>

<ResponseField name="message" type="string" required>
  Additional details about whether the request was canceled.
</ResponseField>

### Rate limits

Calls to the cancel async request status endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

<RequestExample>
  ```py Python (Model) theme={"system"}
  import requests
  import os

  model_id = ""
  request_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.delete(
  f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
  headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Python (Chain) theme={"system"}
  import requests
  import os

  chain_id = ""
  request_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.delete(
  f"https://chain-{chain_id}.api.baseten.co/async_request/{request_id}",
  headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Async deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-async-predict

POST https://model-{model_id}.api.baseten.co/deployment/{deployment-id}/async_predict
Use this endpoint to call any [published deployment](/deploy/lifecycle) of your model.

### Parameters

<ParamField path="model_id" type="string" required>
  The ID of the model you want to call.
</ParamField>

<ParamField path="deployment_id" type="string" required>
  The ID of the specific deployment you want to call.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

There is a 256 KiB size limit to `/async_predict` request payloads.

<ParamField body="model_input" type="json" required>
  JSON-serializable model input.
</ParamField>

<ParamField body="webhook_endpoint" type="string" default="null">
  <Note> Baseten **does not** store model outputs. If `webhook_endpoint` is empty, your model must save prediction outputs so they can be accessed later. </Note>

  URL of the webhook endpoint. We require that webhook endpoints use HTTPS. Both HTTP/2 and HTTP/1.1 protocols are supported.
</ParamField>

<ParamField body="priority" type="integer" default={0}>
  Priority of the request. A lower value corresponds to a higher priority (e.g. requests with priority 0 are scheduled before requests of priority 1).

  `priority` is between 0 and 2, inclusive.
</ParamField>

<ParamField body="max_time_in_queue_seconds" type="integer" default={600}>
  Maximum time a request will spend in the queue before expiring.

  `max_time_in_queue_seconds` must be between 10 seconds and 72 hours, inclusive.
</ParamField>

<ParamField body="inference_retry_config" type="json">
  Exponential backoff parameters used to retry the model predict request.

  <Expandable>
    <ParamField body="max_attempts" type="integer" default={3}>
      Number of predict request attempts.

      `max_attempts` must be between 1 and 10, inclusive.
    </ParamField>

    <ParamField body="initial_delay_ms" type="integer" default={1000}>
      Minimum time between retries in milliseconds.

      `initial_delay_ms` must be between 0 and 10,000 milliseconds, inclusive.
    </ParamField>

    <ParamField body="max_delay_ms" type="integer" default={5000}>
      Maximum time between retries in milliseconds.

      `max_delay_ms` must be between 0 and 60,000 milliseconds, inclusive.
    </ParamField>
  </Expandable>
</ParamField>

### Response

<ResponseField name="request_id" type="string" required>
  The ID of the async request.
</ResponseField>

### Rate limits

Two types of rate limits apply when making async requests:

* Calls to the `/async_predict` endpoint are limited to **200 requests per second**.

* Each organization is limited to **5,000 `QUEUED` or `IN_PROGRESS` async requests**, summed across all deployments.

If either limit is exceeded, subsequent `/async_predict` requests will receive a 429 status code.

To avoid hitting these rate limits, we advise:

* Implementing a backpressure mechanism, such as calling `/async_predict` with exponential backoff in response to 429 errors.
* Monitoring the [async queue size metric](/observability/metrics#async-queue-metrics). If your model is accumulating a backlog of requests, consider increasing the number of requests your model can process at once by increasing the number of max replicas or the concurrency target in your autoscaling settings.

<RequestExample>
  ```py Python theme={"system"}
  import requests
  import os

  model_id = ""
  deployment_id = ""
  webhook_endpoint = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.post(
  f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={
  "model_input": {"prompt": "hello world!"},
  "webhook_endpoint": webhook_endpoint # Optional fields for priority, max_time_in_queue_seconds, etc
  },
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl --request POST \
    --url https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict \
    --header "Authorization: Api-Key $BASETEN_API_KEY" \
    --data '{
    "model_input": {"prompt": "hello world!"},
    "webhook_endpoint": "https://my_webhook.com/webhook",
    "priority": 1,
    "max_time_in_queue_seconds": 100,
    "inference_retry_config": {
      "max_attempts": 3,
      "initial_delay_ms": 1000,
      "max_delay_ms": 5000
    }
  }'
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({
        model_input: { prompt: "hello world!" },
        webhook_endpoint: "https://my_webhook.com/webhook",
        priority: 1,
        max_time_in_queue_seconds: 100,
        inference_retry_config: {
          max_attempts: 3,
          initial_delay_ms: 1000,
          max_delay_ms: 5000,
        },
      }),
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Async chains deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-async-run-remote

POST https://chain-{chain_id}.api.baseten.co/deployment/{deployment-id}/async_run_remote

Use this endpoint to call any [deployment](/deployment/deployments) of your
chain asynchronously.

```sh  theme={"system"}
https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/async_run_remote
```

### Parameters

<ParamField path="chain_id" type="string" required>
  The ID of the chain you want to call.
</ParamField>

<ParamField path="deployment_id" type="string" required>
  The ID of the specific deployment you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Chain input" type="json" required>
  JSON-serializable chain input. The input schema corresponds to the signature
  of the entrypoint's `run_remote` method. I.e. The top-level keys are the
  argument names. The values are the corresponding JSON representation of the
  types.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  chain_id = ""
  deployment_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://chain
  -{chain_id}.api.baseten.co/deployment/{deployment_id}/async_run_remote",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable chain input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/async_run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/async_run_remote",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-predict

POST https://model-{model_id}.api.baseten.co/deployment/{deployment-id}/predict

Use this endpoint to call any [published deployment](/deployment/deployments) of your model.

```sh  theme={"system"}
https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/predict
```

### Parameters

<ParamField path="model_id" type="string" required>
  The ID of the model you want to call.
</ParamField>

<ParamField path="deployment_id" type="string" required>
  The ID of the specific deployment you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Model input" type="json" required>
  JSON-serializable model input.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  model_id = ""
  deployment_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable model input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/predict \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable model input
  ```

  ```sh Truss theme={"system"}
  truss predict --model-version DEPLOYMENT_ID -d '{}' # JSON-serializable model input
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable model input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // JSON-serializable output varies by model theme={"system"}
  {}
  ```
</ResponseExample>


# Chains deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-run-remote

POST https://chain-{chain_id}.api.baseten.co/deployment/{deployment-id}/run_remote

Use this endpoint to call any [deployment](/deployment/deployments) of your
chain.

```sh  theme={"system"}
https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/run_remote
```

### Parameters

<ParamField path="chain_id" type="string" required>
  The ID of the chain you want to call.
</ParamField>

<ParamField path="deployment_id" type="string" required>
  The ID of the specific deployment you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Chain input" type="json" required>
  JSON-serializable chain input. The input schema corresponds to the signature
  of the entrypoint's `run_remote` method. I.e. The top-level keys are the
  argument names. The values are the corresponding JSON representation of the
  types.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  chain_id = ""
  deployment_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://chain
  -{chain_id}.api.baseten.co/deployment/{deployment_id}/run_remote",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable chain input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/run_remote",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // JSON-serializable output varies by chain theme={"system"}
  {}
  ```
</ResponseExample>


# Websocket deployment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-websocket

WEBSOCKET wss://{entity}-{entity_id}.api.baseten.co/deployment/{deployment_id}/websocket

Use this endpoint to connect via WebSockets to a specific deployment.

Note that `entity` here could be either `model` or `chain`, depending on whether you using Baseten models or Chains.

```sh  theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/deployment/{deployment_id}/websocket"
```

See [WebSockets](/development/model/websockets) for more details.

### Parameters

<ParamField path="entity" type="string" required>
  The type of entity you want to connect to. Either `model` or `chain`.
</ParamField>

<ParamField path="entity_id" type="string" required>
  The ID of the model or chain you want to connect to.
</ParamField>

<ParamField path="deployment_id" type="string" required>
  The ID of the deployment you want to connect to.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Api-Key YOUR_API_KEY' \
      wss://{entity}-{model_id}.api.baseten.co/deployment/{deployment_id}/websocket
  ```
</RequestExample>


# Async development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-async-predict

POST https://model-{model_id}.api.baseten.co/development/async_predict
Use this endpoint to call the [development deployment](/deploy/lifecycle) of your model asynchronously.

### Parameters

<ParamField path="model_id" type="string" required>
  The ID of the model you want to call.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

There is a 256 KiB size limit to `/async_predict` request payloads.

<ParamField body="model_input" type="json" required>
  JSON-serializable model input.
</ParamField>

<ParamField body="webhook_endpoint" type="string" default="null">
  <Note> Baseten **does not** store model outputs. If `webhook_endpoint` is empty, your model must save prediction outputs so they can be accessed later. </Note>

  URL of the webhook endpoint. We require that webhook endpoints use HTTPS. Both HTTP/2 and HTTP/1.1 protocols are supported.
</ParamField>

<ParamField body="priority" type="integer" default={0}>
  Priority of the request. A lower value corresponds to a higher priority (e.g. requests with priority 0 are scheduled before requests of priority 1).

  `priority` is between 0 and 2, inclusive.
</ParamField>

<ParamField body="max_time_in_queue_seconds" type="integer" default={600}>
  Maximum time a request will spend in the queue before expiring.

  `max_time_in_queue_seconds` must be between 10 seconds and 72 hours, inclusive.
</ParamField>

<ParamField body="inference_retry_config" type="json">
  Exponential backoff parameters used to retry the model predict request.

  <Expandable>
    <ParamField body="max_attempts" type="integer" default={3}>
      Number of predict request attempts.

      `max_attempts` must be between 1 and 10, inclusive.
    </ParamField>

    <ParamField body="initial_delay_ms" type="integer" default={1000}>
      Minimum time between retries in milliseconds.

      `initial_delay_ms` must be between 0 and 10,000 milliseconds, inclusive.
    </ParamField>

    <ParamField body="max_delay_ms" type="integer" default={5000}>
      Maximum time between retries in milliseconds.

      `max_delay_ms` must be between 0 and 60,000 milliseconds, inclusive.
    </ParamField>
  </Expandable>
</ParamField>

### Response

<ResponseField name="request_id" type="string" required>
  The ID of the async request.
</ResponseField>

### Rate limits

Two types of rate limits apply when making async requests:

* Calls to the `/async_predict` endpoint are limited to **200 requests per second**.

* Each organization is limited to **5,000 `QUEUED` or `IN_PROGRESS` async requests**, summed across all deployments.

If either limit is exceeded, subsequent `/async_predict` requests will receive a 429 status code.

To avoid hitting these rate limits, we advise:

* Implementing a backpressure mechanism, such as calling `/async_predict` with exponential backoff in response to 429 errors.
* Monitoring the [async queue size metric](/observability/metrics#async-queue-metrics). If your model is accumulating a backlog of requests, consider increasing the number of requests your model can process at once by increasing the number of max replicas or the concurrency target in your autoscaling settings.

<RequestExample>
  ```py Python theme={"system"}
  import requests
  import os

  model_id = ""
  webhook_endpoint = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.post(
  f"https://model-{model_id}.api.baseten.co/development/async_predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={
  "model_input": {"prompt": "hello world!"},
  "webhook_endpoint": webhook_endpoint # Optional fields for priority, max_time_in_queue_seconds, etc
  },
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl --request POST \
    --url https://model-{model_id}.api.baseten.co/development/async_predict \
    --header "Authorization: Api-Key $BASETEN_API_KEY" \
    --data '{
    "model_input": {"prompt": "hello world!"},
    "webhook_endpoint": "https://my_webhook.com/webhook",
    "priority": 1,
    "max_time_in_queue_seconds": 100,
    "inference_retry_config": {
      "max_attempts": 3,
      "initial_delay_ms": 1000,
      "max_delay_ms": 5000
    }
  }'
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/development/async_predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({
        model_input: { prompt: "hello world!" },
        webhook_endpoint: "https://my_webhook.com/webhook",
        priority: 1,
        max_time_in_queue_seconds: 100,
        inference_retry_config: {
          max_attempts: 3,
          initial_delay_ms: 1000,
          max_delay_ms: 5000,
        },
      }),
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Async chains development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-async-run-remote

POST https://chain-{chain_id}.api.baseten.co/development/async_run_remote

Use this endpoint to call the [development deployment](/development/chain/deploy#development) of
your chain asynchronously.

```sh  theme={"system"}
https://chain-{chain_id}.api.baseten.co/development/async_run_remote
```

### Parameters

<ParamField path="chain_id" type="string" required>
  The ID of the chain you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Chain input" type="json" required>
  JSON-serializable chain input. The input schema corresponds to the
  signature of the entrypoint's `run_remote` method. I.e. The top-level keys
  are the argument names. The values are the corresponding JSON representation of
  the types.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  chain_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://chain-{chain_id}.api.baseten.co/development/async_run_remote",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable chain input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/development/async_run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```js Node.js theme={"system"}
  const fetch = require('node-fetch');

  const resp = await fetch(
    'https://chain-{chain_id}.api.baseten.co/development/async_run_remote',
    {
      method: 'POST',
      headers: { Authorization: 'Api-Key YOUR_API_KEY' },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-predict

POST https://model-{model_id}.api.baseten.co/development/predict

Use this endpoint to call the [development deployment](/deployment/deployments) of your model.

```sh  theme={"system"}
https://model-{model_id}.api.baseten.co/development/predict
```

### Parameters

<ParamField path="model_id" type="string" required>
  The ID of the model you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Model input" type="json" required>
  JSON-serializable model input.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  model_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/development/predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable model input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/development/predict \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable model input
  ```

  ```sh Truss theme={"system"}
  truss predict --model-version DEPLOYMENT_ID -d '{}' # JSON-serializable model input
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/development/predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable model input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // JSON-serializable output varies by model theme={"system"}
  {}
  ```
</ResponseExample>


# Chains development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-run-remote

POST https://chain-{chain_id}.api.baseten.co/development/run_remote

Use this endpoint to call the [development deployment](/development/chain/deploy#development) of
your chain.

```sh  theme={"system"}
https://chain-{chain_id}.api.baseten.co/development/run_remote
```

### Parameters

<ParamField path="chain_id" type="string" required>
  The ID of the chain you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Chain input" type="json" required>
  JSON-serializable chain input. The input schema corresponds to the
  signature of the entrypoint's `run_remote` method. I.e. The top-level keys
  are the argument names. The values are the corresponding JSON representation of
  the types.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  chain_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://chain-{chain_id}.api.baseten.co/development/run_remote",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable chain input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/development/run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```js Node.js theme={"system"}
  const fetch = require('node-fetch');

  const resp = await fetch(
    'https://chain-{chain_id}.api.baseten.co/development/run_remote',
    {
      method: 'POST',
      headers: { Authorization: 'Api-Key YOUR_API_KEY' },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response theme={"system"}
  // JSON-serializable output varies by chain
  {}
  ```
</ResponseExample>


# Websocket development
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/development-websocket

WEBSOCKET wss://{entity}-{entity_id}.api.baseten.co/development/websocket

Use this endpoint to connect via WebSockets to the development deployment of a model or chain.

```sh  theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/development/websocket"
```

See [WebSockets](/development/model/websockets) for more details.

### Parameters

<ParamField path="entity" type="string" required>
  The type of entity you want to connect to. Either `model` or `chain`.
</ParamField>

<ParamField path="entity_id" type="string" required>
  The ID of the model or chain you want to connect to.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Api-Key YOUR_API_KEY' \
      wss://{entity}-{entity_id}.api.baseten.co/development/websocket
  ```
</RequestExample>


# Async environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-async-predict

POST https://model-{model_id}.api.baseten.co/environments/{env_name}/async_predict
Use this endpoint to call the model associated with the specified environment asynchronously.

### Parameters

<ParamField path="model_id" type="string" required>
  The ID of the model you want to call.
</ParamField>

<ParamField path="env_name" type="string" required>
  The name of the model's environment you want to call.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

There is a 256 KiB size limit to `/async_predict` request payloads.

<ParamField body="model_input" type="json" required>
  JSON-serializable model input.
</ParamField>

<ParamField body="webhook_endpoint" type="string" default="null">
  <Note> Baseten **does not** store model outputs. If `webhook_endpoint` is empty, your model must save prediction outputs so they can be accessed later. </Note>

  URL of the webhook endpoint. We require that webhook endpoints use HTTPS. Both HTTP/2 and HTTP/1.1 protocols are supported.
</ParamField>

<ParamField body="priority" type="integer" default={0}>
  Priority of the request. A lower value corresponds to a higher priority (e.g. requests with priority 0 are scheduled before requests of priority 1).

  `priority` is between 0 and 2, inclusive.
</ParamField>

<ParamField body="max_time_in_queue_seconds" type="integer" default={600}>
  Maximum time a request will spend in the queue before expiring.

  `max_time_in_queue_seconds` must be between 10 seconds and 72 hours, inclusive.
</ParamField>

<ParamField body="inference_retry_config" type="json">
  Exponential backoff parameters used to retry the model predict request.

  <Expandable>
    <ParamField body="max_attempts" type="integer" default={3}>
      Number of predict request attempts.

      `max_attempts` must be between 1 and 10, inclusive.
    </ParamField>

    <ParamField body="initial_delay_ms" type="integer" default={1000}>
      Minimum time between retries in milliseconds.

      `initial_delay_ms` must be between 0 and 10,000 milliseconds, inclusive.
    </ParamField>

    <ParamField body="max_delay_ms" type="integer" default={5000}>
      Maximum time between retries in milliseconds.

      `max_delay_ms` must be between 0 and 60,000 milliseconds, inclusive.
    </ParamField>
  </Expandable>
</ParamField>

### Response

<ResponseField name="request_id" type="string" required>
  The ID of the async request.
</ResponseField>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>

### Rate limits

Two types of rate limits apply when making async requests:

* Calls to the `/async_predict` endpoint are limited to **200 requests per second**.

* Each organization is limited to **5,000 `QUEUED` or `IN_PROGRESS` async requests**, summed across all deployments.

If either limit is exceeded, subsequent `/async_predict` requests will receive a 429 status code.

To avoid hitting these rate limits, we advise:

* Implementing a backpressure mechanism, such as calling `/async_predict` with exponential backoff in response to 429 errors.
* Monitoring the [async queue size metric](/observability/metrics#async-queue-metrics). If your model is accumulating a backlog of requests, consider increasing the number of requests your model can process at once by increasing the number of max replicas or the concurrency target in your autoscaling settings.


# Async chains environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-async-run-remote

POST https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote
Use this endpoint to call the deployment associated with the specified environment asynchronously.

```sh  theme={"system"}
https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote"
```

### Parameters

<ParamField path="chain_id" type="string" required>
  The ID of the chain you want to call.
</ParamField>

<ParamField path="env_name" type="string" required>
  The name of the chain's environment you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Chain input" type="json" required>
  JSON-serializable chain input. The input schema corresponds to the
  signature of the entrypoint's `run_remote` method. I.e. The top-level keys
  are the argument names. The values are the corresponding JSON representation of
  the types.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  chain_id = ""
  env_name = "staging"
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
      "POST",
      f"https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json={}, # JSON-serializable chain input
  )

  print(resp.json())
  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```js Node.js theme={"system"}
  const fetch = require('node-fetch');

  const resp = await fetch(
    'https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_run_remote',
    {
      method: 'POST',
      headers: { Authorization: 'Api-Key YOUR_API_KEY' },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>


# Environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-predict

POST https://model-{model_id}.api.baseten.co/environments/{env_name}/predict

Use this endpoint to call the deployment associated with the specified [environment](/deployment/environments).

```sh  theme={"system"}
https://model-{model_id}.api.baseten.co/environments/{env_name}/predict
```

### Parameters

<ParamField path="model_id" type="string" required>
  The ID of the model you want to call.
</ParamField>

<ParamField path="env_name" type="string" required>
  The name of the model's environment you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Model input" type="json" required>
  JSON-serializable model input.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  model_id = ""
  env_name = "staging"

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/environments/{env_name}/predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={}, # JSON-serializable model input
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/environments/{env_name}/predict \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable model input
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/environments/{env_name}/predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({}), // JSON-serializable model input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // JSON-serializable output varies by model theme={"system"}
  {}
  ```
</ResponseExample>


# Chains environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-run-remote

POST https://chain-{chain_id}.api.baseten.co/environments/{env_name}/run_remote
Use this endpoint to call the deployment associated with the specified environment.

```sh  theme={"system"}
https://chain-{chain}.api.baseten.co/environments/{env_name}/run_remote"
```

### Parameters

<ParamField path="chain_id" type="string" required>
  The ID of the chain you want to call.
</ParamField>

<ParamField path="env_name" type="string" required>
  The name of the chain's environment you want to call.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

<ParamField body="Chain input" type="json" required>
  JSON-serializable chain input. The input schema corresponds to the
  signature of the entrypoint's `run_remote` method. I.e. The top-level keys
  are the argument names. The values are the corresponding JSON representation of
  the types.
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  chain_id = ""
  env_name = "staging"
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
      "POST",
      f"https://chain-{chain_id}.api.baseten.co/environments/{env_name}/run_remote",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json={}, # JSON-serializable chain input
  )

  print(resp.json())
  ```

  ```sh cURL theme={"system"}
  curl -X POST https://chain-{chain_id}.api.baseten.co/environments/{env_name}/run_remote \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
    -d '{}' # JSON-serializable chain input
  ```

  ```js Node.js theme={"system"}
  const fetch = require('node-fetch');

  const resp = await fetch(
    'https://chain-{chain_id}.api.baseten.co/environments/{env_name}/run_remote',
    {
      method: 'POST',
      headers: { Authorization: 'Api-Key YOUR_API_KEY' },
      body: JSON.stringify({}), // JSON-serializable chain input
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response theme={"system"}
  // JSON-serializable output varies by chain
  {}
  ```
</ResponseExample>


# Websocket environment
Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/environments-websocket

WEBSOCKET wss://{entity}-{entity_id}.api.baseten.co/environments/{env_name}/websocket

Use this endpoint to connect via WebSockets to the deployment associated with the specified [environment](/deployment/environments).

Note that `entity` here could be either `model` or `chain`, depending on whether you using Baseten models or Chains.

```sh  theme={"system"}
wss://{entity}-{entity_id}.api.baseten.co/environments/{env_name}/websocket"
```

See [WebSockets](/development/model/websockets) for more details.

### Parameters

<ParamField path="entity" type="string" required>
  The type of entity you want to connect to. Either `model` or `chain`.
</ParamField>

<ParamField path="entity_id" type="string" required>
  The ID of the model or chain you want to connect to.
</ParamField>

<ParamField path="env_name" type="string" required>
  The name of the environment you want to connect to.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```sh websocat theme={"system"}
  websocat -H 'Authorization: Api-Key YOUR_API_KEY' \
      wss://{entity}-{model_id}.api.baseten.co/environments/{env_name}/websocket
  ```
</RequestExample>


# Async deployment
Source: https://docs.baseten.co/reference/inference-api/status-endpoints/deployment-get-async-queue-status

GET https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_queue_status
Use this endpoint to get the status of a published deployment's async queue.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField path="model_id" type="string" required>
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField path="chain_id" type="string" required>
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

<ParamField path="deployment_id" type="string" required>
  The ID of the deployment.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<ResponseField name="model_id" type="string" required>
  The ID of the model.
</ResponseField>

<ResponseField name="deployment_id" type="string" required>
  The ID of the deployment.
</ResponseField>

<ResponseField name="num_queued_requests" type="integer" required>
  The number of requests in the deployment's async queue with `QUEUED` status (i.e. awaiting processing by the model).
</ResponseField>

<ResponseField name="num_in_progress_requests" type="integer" required>
  The number of requests in the deployment's async queue with `IN_PROGRESS` status (i.e. currently being processed by the model).
</ResponseField>

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "model_id": "<string>",
    "deployment_id": "<string>",
    "num_queued_requests": 12,
    "num_in_progress_requests": 3
  }
  ```
</ResponseExample>

### Rate limits

Calls to the `/async_queue_status` endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To gracefully handle hitting this rate limit, we advise implementing a backpressure mechanism, such as calling `/async_queue_status` with exponential backoff in response to 429 errors.

<RequestExample>
  ```py Model theme={"system"}
  import requests
  import os

  model_id = ""
  deployment_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Chain theme={"system"}
  import requests
  import os

  chain_id = ""
  deployment_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Async development
Source: https://docs.baseten.co/reference/inference-api/status-endpoints/development-get-async-queue-status

GET https://model-{model_id}.api.baseten.co/development/async_queue_status
Use this endpoint to get the status of a development deployment's async queue.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField path="model_id" type="string" required>
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField path="chain_id" type="string" required>
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<ResponseField name="model_id" type="string" required>
  The ID of the model.
</ResponseField>

<ResponseField name="deployment_id" type="string" required>
  The ID of the deployment.
</ResponseField>

<ResponseField name="num_queued_requests" type="integer" required>
  The number of requests in the deployment's async queue with `QUEUED` status (i.e. awaiting processing by the model).
</ResponseField>

<ResponseField name="num_in_progress_requests" type="integer" required>
  The number of requests in the deployment's async queue with `IN_PROGRESS` status (i.e. currently being processed by the model).
</ResponseField>

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "model_id": "<string>",
    "deployment_id": "<string>",
    "num_queued_requests": 12,
    "num_in_progress_requests": 3
  }
  ```
</ResponseExample>

### Rate limits

Calls to the `/async_queue_status` endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To gracefully handle hitting this rate limit, we advise implementing a backpressure mechanism, such as calling `/async_queue_status` with exponential backoff in response to 429 errors.

<RequestExample>
  ```py Model theme={"system"}
  import requests
  import os

  model_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/development/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Chain theme={"system"}
  import requests
  import os

  chain_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/development/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Async environment
Source: https://docs.baseten.co/reference/inference-api/status-endpoints/environments-get-async-queue-status

GET https://model-{model_id}.api.baseten.co/environments/{env_name}/async_queue_status
Use this endpoint to get the async queue status for a model associated with the specified environment.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField path="model_id" type="string" required>
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField path="chain_id" type="string" required>
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

<ParamField path="env_name" type="string" required>
  The name of the environment.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<ResponseField name="model_id" type="string" required>
  The ID of the model.
</ResponseField>

<ResponseField name="deployment_id" type="string" required>
  The ID of the deployment.
</ResponseField>

<ResponseField name="num_queued_requests" type="integer" required>
  The number of requests in the deployment's async queue with `QUEUED` status (i.e. awaiting processing by the model).
</ResponseField>

<ResponseField name="num_in_progress_requests" type="integer" required>
  The number of requests in the deployment's async queue with `IN_PROGRESS` status (i.e. currently being processed by the model).
</ResponseField>

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "model_id": "<string>",
    "deployment_id": "<string>",
    "num_queued_requests": 12,
    "num_in_progress_requests": 3
  }
  ```
</ResponseExample>

### Rate limits

Calls to the `/async_queue_status` endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To gracefully handle hitting this rate limit, we advise implementing a backpressure mechanism, such as calling `/async_queue_status` with exponential backoff in response to 429 errors.

<RequestExample>
  ```py Model theme={"system"}
  import requests
  import os

  model_id = ""
  env_name = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/environments/{env_name}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Chain theme={"system"}
  import requests
  import os

  chain_id = ""
  env_name = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/environments/{env_name}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Async request
Source: https://docs.baseten.co/reference/inference-api/status-endpoints/get-async-request-status

GET https://model-{model_id}.api.baseten.co/async_request/{request_id}
Use this endpoint to get the status of an async request.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField path="model_id" type="string" required>
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField path="chain_id" type="string" required>
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

<ParamField path="request_id" type="string" required>
  The ID of the async request.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<Tabs>
  <Tab title="Model">
    <ResponseField name="request_id" type="string" required>
      The ID of the async request.
    </ResponseField>

    <ResponseField name="model_id" type="string" required>
      The ID of the model that executed the request.
    </ResponseField>

    <ResponseField name="deployment_id" type="string" required>
      The ID of the deployment that executed the request.
    </ResponseField>

    <ResponseField name="status" type="string" required>
      An enum representing the status of the request.

      Available options: `QUEUED`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `EXPIRED`, `CANCELED`, `WEBHOOK_FAILED`
    </ResponseField>

    <ResponseField name="webhook_status" type="string" required>
      An enum representing the status of sending the predict result to the provided webhook.

      Available options: `PENDING`, `SUCCEEDED`, `FAILED`, `CANCELED`, `NO_WEBHOOK_PROVIDED`
    </ResponseField>

    <ResponseField name="created_at" type="string" required>
      The time in UTC at which the async request was created.
    </ResponseField>

    <ResponseField name="status_at" type="string" required>
      The time in UTC at which the async request's status was updated.
    </ResponseField>

    <ResponseField name="errors" type="object[]" required default={[]}>
      Any errors that occurred in processing the async request. Empty if no errors occurred.

      <Expandable>
        <ResponseField name="code" type="string" required>
          An enum representing the type of error that occurred.

          Available options: `MODEL_PREDICT_ERROR`, `MODEL_PREDICT_TIMEOUT`, `MODEL_NOT_READY`, `MODEL_DOES_NOT_EXIST`, `MODEL_UNAVAILABLE`, `MODEL_INVALID_INPUT`, `ASYNC_REQUEST_NOT_SUPPORTED`, `INTERNAL_SERVER_ERROR`
        </ResponseField>

        <ResponseField name="message" type="string" required>
          A message containing details of the error that occurred.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>

  <Tab title="Chain">
    <ResponseField name="request_id" type="string" required>
      The ID of the async request.
    </ResponseField>

    <ResponseField name="chain_id" type="string" required>
      The ID of the chain that executed the request.
    </ResponseField>

    <ResponseField name="deployment_id" type="string" required>
      The ID of the deployment that executed the request.
    </ResponseField>

    <ResponseField name="status" type="string" required>
      An enum representing the status of the request.

      Available options: `QUEUED`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `EXPIRED`, `CANCELED`, `WEBHOOK_FAILED`
    </ResponseField>

    <ResponseField name="webhook_status" type="string" required>
      An enum representing the status of sending the predict result to the provided webhook.

      Available options: `PENDING`, `SUCCEEDED`, `FAILED`, `CANCELED`, `NO_WEBHOOK_PROVIDED`
    </ResponseField>

    <ResponseField name="created_at" type="string" required>
      The time in UTC at which the async request was created.
    </ResponseField>

    <ResponseField name="status_at" type="string" required>
      The time in UTC at which the async request's status was updated.
    </ResponseField>

    <ResponseField name="errors" type="object[]" required default={[]}>
      Any errors that occurred in processing the async request. Empty if no errors occurred.

      <Expandable>
        <ResponseField name="code" type="string" required>
          An enum representing the type of error that occurred.

          Available options: `MODEL_PREDICT_ERROR`, `MODEL_PREDICT_TIMEOUT`, `MODEL_NOT_READY`, `MODEL_DOES_NOT_EXIST`, `MODEL_UNAVAILABLE`, `MODEL_INVALID_INPUT`, `ASYNC_REQUEST_NOT_SUPPORTED`, `INTERNAL_SERVER_ERROR`
        </ResponseField>

        <ResponseField name="message" type="string" required>
          A message containing details of the error that occurred.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>
</Tabs>

<ResponseExample>
  ```json 200 (Model) theme={"system"}
  {
    "request_id": "<string>",
    "model_id": "<string>",
    "deployment_id": "<string>",
    "status": "<string>",
    "webhook_status": "<string>",
    "created_at": "<string>",
    "status_at": "<string>",
    "errors": [
      {
        "code": "<string>",
        "message": "<string>"
      }
    ]
  }
  ```

  ```json 200 (Chain) theme={"system"}
  {
    "request_id": "<string>",
    "chain_id": "<string>",
    "deployment_id": "<string>",
    "status": "<string>",
    "webhook_status": "<string>",
    "created_at": "<string>",
    "status_at": "<string>",
    "errors": [
      {
        "code": "<string>",
        "message": "<string>"
      }
    ]
  }
  ```
</ResponseExample>

### Rate limits

Calls to the get async request status endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To avoid hitting this rate limit, we recommend [configuring a webhook endpoint](/inference/async#configuring-the-webhook-endpoint) to receive async predict results instead of frequently polling this endpoint for async request statuses.

<RequestExample>
  ```py Python (Model) theme={"system"}
  import requests
  import os

  model_id = ""
  request_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Python (Chain) theme={"system"}
  import requests
  import os

  chain_id = ""
  request_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/async_request/{request_id}",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>


# Deployment
Source: https://docs.baseten.co/reference/inference-api/wake/deployment-wake

POST https://model-{model_id}.api.baseten.co/deployment/{deployment-id}/wake

Use this endpoint to wake any scaled-to-zero [deployment](/deployment/deployments) of your model.

```sh  theme={"system"}
https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/wake
```

### Parameters

<ParamField path="Model ID" type="string" required>
  The ID of the model you want to wake.
</ParamField>

<ParamField path="Deployment ID" type="string" required>
  The ID of the specific deployment you want to wake.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  model_id = ""
  deployment_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/wake",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/wake \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/wake",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // Returns a 202 response code theme={"system"}
  {}
  ```
</ResponseExample>


# Development
Source: https://docs.baseten.co/reference/inference-api/wake/development-wake

POST https://model-{model_id}.api.baseten.co/development/wake

Use this endpoint to wake the [development deployment](/deployment/deployments#development-deployment) of your model if it is scaled to zero.

```sh  theme={"system"}
https://model-{model_id}.api.baseten.co/development/wake
```

### Parameters

<ParamField path="Model ID" type="string" required>
  The ID of the model you want to wake.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  model_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/development/wake",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/development/wake \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/development/wake",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // Returns a 202 response code theme={"system"}
  {}
  ```
</ResponseExample>


# Production
Source: https://docs.baseten.co/reference/inference-api/wake/production-wake

POST https://model-{model_id}.api.baseten.co/production/wake

Use this endpoint to wake the [production environment](/deployment/deployments#environments-and-promotion) of your model if it is scaled to zero.

```sh  theme={"system"}
https://model-{model_id}.api.baseten.co/production/wake
```

### Parameters

<ParamField path="Model ID" type="string" required>
  The ID of the model you want to wake.
</ParamField>

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

<RequestExample>
  ```py Python theme={"system"}
  import urllib3
  import os

  model_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = urllib3.request(
  "POST",
  f"https://model-{model_id}.api.baseten.co/production/wake",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl -X POST https://model-{model_id}.api.baseten.co/production/wake \
    -H 'Authorization: Api-Key YOUR_API_KEY' \
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/production/wake",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json Example Response // Returns a 202 response code theme={"system"}
  {}
  ```
</ResponseExample>


# Create an API key
Source: https://docs.baseten.co/reference/management-api/api-keys/creates-an-api-key

post /v1/api_keys
Creates an API key with the provided name and type. The API key is returned in the response.



# Delete an API key
Source: https://docs.baseten.co/reference/management-api/api-keys/delete-an-api-key

delete /v1/api_keys/{api_key_prefix}
Deletes an API key by prefix and returns info about the API key.



# Get all API keys
Source: https://docs.baseten.co/reference/management-api/api-keys/lists-the-users-api-keys

get /v1/api_keys
Lists all API keys your account has access to.

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "name": "my-api-key", 
    "type": "PERSONAL"
  }
  ```
</ResponseExample>


# Delete chains
Source: https://docs.baseten.co/reference/management-api/chains/deletes-a-chain-by-id

delete /v1/chains/{chain_id}



# By ID
Source: https://docs.baseten.co/reference/management-api/chains/gets-a-chain-by-id

get /v1/chains/{chain_id}



# All chains
Source: https://docs.baseten.co/reference/management-api/chains/gets-all-chains

get /v1/chains



# Any deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/activate/activates-a-deployment

post /v1/models/{model_id}/deployments/{deployment_id}/activate
Activates an inactive deployment and returns the activation status.



# Activate environment deployment
Source: https://docs.baseten.co/reference/management-api/deployments/activate/activates-a-deployment-associated-with-an-environment

post /v1/models/{model_id}/environments/{env_name}/activate
Activates an inactive deployment associated with an environment and returns the activation status.



# Development deployment
Source: https://docs.baseten.co/reference/management-api/deployments/activate/activates-a-development-deployment

post /v1/models/{model_id}/deployments/development/activate
Activates an inactive development deployment and returns the activation status.



# Update chainlet environment's autoscaling settings
Source: https://docs.baseten.co/reference/management-api/deployments/autoscaling/update-a-chainlet-environments-autoscaling-settings

patch /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/autoscaling_settings
Updates a chainlet environment's autoscaling settings and returns the updated chainlet environment settings.



# Any model deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/autoscaling/updates-a-deployments-autoscaling-settings

patch /v1/models/{model_id}/deployments/{deployment_id}/autoscaling_settings
Updates a deployment's autoscaling settings and returns the update status.



# Development model deployment
Source: https://docs.baseten.co/reference/management-api/deployments/autoscaling/updates-a-development-deployments-autoscaling-settings

patch /v1/models/{model_id}/deployments/development/autoscaling_settings
Updates a development deployment's autoscaling settings and returns the update status.



# Any deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/deactivate/deactivates-a-deployment

post /v1/models/{model_id}/deployments/{deployment_id}/deactivate
Deactivates a deployment and returns the deactivation status.



# Deactivate environment deployment
Source: https://docs.baseten.co/reference/management-api/deployments/deactivate/deactivates-a-deployment-associated-with-an-environment

post /v1/models/{model_id}/environments/{env_name}/deactivate
Deactivates a deployment associated with an environment and returns the deactivation status.



# Development deployment
Source: https://docs.baseten.co/reference/management-api/deployments/deactivate/deactivates-a-development-deployment

post /v1/models/{model_id}/deployments/development/deactivate
Deactivates a development deployment and returns the deactivation status.



# Delete chain deployment
Source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-chain-deployment-by-id

delete /v1/chains/{chain_id}/deployments/{chain_deployment_id}



# Delete model deployments
Source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-models-deployment-by-id

delete /v1/models/{model_id}/deployments/{deployment_id}
Deletes a model's deployment by ID and returns the tombstone of the deployment.



# Any chain deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-chain-deployment-by-id

get /v1/chains/{chain_id}/deployments/{chain_deployment_id}



# Any model deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-models-deployment-by-id

get /v1/models/{model_id}/deployments/{deployment_id}
Gets a model's deployment by ID and returns the deployment.



# Development model deployment
Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-models-development-deployment

get /v1/models/{model_id}/deployments/development
Gets a model's development deployment and returns the deployment.



# Production model deployment
Source: https://docs.baseten.co/reference/management-api/deployments/gets-a-models-production-deployment

get /v1/models/{model_id}/deployments/production
Gets a model's production deployment and returns the deployment.



# Get all chain deployments
Source: https://docs.baseten.co/reference/management-api/deployments/gets-all-chain-deployments

get /v1/chains/{chain_id}/deployments



# Get all model deployments
Source: https://docs.baseten.co/reference/management-api/deployments/gets-all-deployments-of-a-model

get /v1/models/{model_id}/deployments



# Cancel model promotion
Source: https://docs.baseten.co/reference/management-api/deployments/promote/cancel-promotion

post /v1/models/{model_id}/environments/{env_name}/cancel_promotion
Cancels an ongoing promotion to an environment and returns the cancellation status.

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "status": "CANCELED",
    "message": "Promotion to production was successfully canceled."
  }
  ```

  ```json 400 theme={"system"}
  {
    "code": "VALIDATION_ERROR",
    "message": "Environment production has no in progress promotion."
  }
  ```
</ResponseExample>


# Promote to chain environment
Source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-chain-deployment-to-an-environment

post /v1/chains/{chain_id}/environments/{env_name}/promote
Promotes an existing chain deployment to an environment and returns the promoted chain deployment.



# Promote to model environment
Source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-deployment-to-an-environment

post /v1/models/{model_id}/environments/{env_name}/promote
Promotes an existing deployment to an environment and returns the promoted deployment.



# Any model deployment by ID
Source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-deployment-to-production

post /v1/models/{model_id}/deployments/{deployment_id}/promote
Promotes an existing deployment to production and returns the same deployment.



# Development model deployment
Source: https://docs.baseten.co/reference/management-api/deployments/promote/promotes-a-development-deployment-to-production

post /v1/models/{model_id}/deployments/development/promote
Creates a new production deployment from the development deployment, the currently building deployment is returned.



# Create Chain environment
Source: https://docs.baseten.co/reference/management-api/environments/create-a-chain-environment

post /v1/chains/{chain_id}/environments
Create a chain environment. Returns the resulting environment.



# Create environment
Source: https://docs.baseten.co/reference/management-api/environments/create-an-environment

post /v1/models/{model_id}/environments
Creates an environment for the specified model and returns the environment.



# Get Chain environment
Source: https://docs.baseten.co/reference/management-api/environments/get-a-chain-environments-details

get /v1/chains/{chain_id}/environments/{env_name}
Gets a chain environment's details and returns the chain environment.



# Get all Chain environments
Source: https://docs.baseten.co/reference/management-api/environments/get-all-chain-environments

get /v1/chains/{chain_id}/environments
Gets all chain environments for a given chain



# Get all environments
Source: https://docs.baseten.co/reference/management-api/environments/get-all-environments

get /v1/models/{model_id}/environments
Gets all environments for a given model



# Get environment
Source: https://docs.baseten.co/reference/management-api/environments/get-an-environments-details

get /v1/models/{model_id}/environments/{env_name}
Gets an environment's details and returns the environment.



# Update Chain environment
Source: https://docs.baseten.co/reference/management-api/environments/update-a-chain-environments-settings

patch /v1/chains/{chain_id}/environments/{env_name}
Update a chain environment's settings and returns the chain environment.



# Update chainlet environment's instance type
Source: https://docs.baseten.co/reference/management-api/environments/update-a-chainlet-environments-instance-type-settings

post /v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/instance_types/update
Updates a chainlet environment's instance type settings. The chainlet environment setting must exist. When updated, a new chain deployment is created and deployed. It is promoted to the chain environment according to promotion settings on the environment.



# Update model environment
Source: https://docs.baseten.co/reference/management-api/environments/update-an-environments-settings

patch /v1/models/{model_id}/environments/{env_name}
Updates an environment's settings and returns the updated environment.



# Delete models
Source: https://docs.baseten.co/reference/management-api/models/deletes-a-model-by-id

delete /v1/models/{model_id}



# By ID
Source: https://docs.baseten.co/reference/management-api/models/gets-a-model-by-id

get /v1/models/{model_id}



# All models
Source: https://docs.baseten.co/reference/management-api/models/gets-all-models

get /v1/models



# Overview
Source: https://docs.baseten.co/reference/management-api/overview

The management API is used to manage models and deployments. It supports monitoring, CI/CD, and automation at both the model and workspace levels.

# Model endpoints

| Method | Endpoint                                                                          | Description      |
| :----- | :-------------------------------------------------------------------------------- | :--------------- |
| `GET`  | [`/v1/models`](/reference/management-api/models/gets-all-models)                  | Get all models   |
| `GET`  | [`/v1/models/{model_id}`](/reference/management-api/models/gets-a-model-by-id)    | Get models by ID |
| `DEL`  | [`/v1/models/{model_id}`](/reference/management-api/models/deletes-a-model-by-id) | Delete models    |

# Chain endpoints

| Method | Endpoint                                                                          | Description          |
| :----- | :-------------------------------------------------------------------------------- | :------------------- |
| `GET`  | [`/v1/chains`](/reference/management-api/chains/gets-all-chains)                  | Get all Chains       |
| `GET`  | [`/v1/chains/{chain_id}`](/reference/management-api/chains/gets-a-chain-by-id)    | Get all Chains by ID |
| `DEL`  | [`/v1/chains/{chain_id}`](/reference/management-api/chains/deletes-a-chain-by-id) | Delete Chains        |

# Deployment endpoints

<Tabs>
  <Tab title="Models">
    ### Activate a model deployment

    | Method | Endpoint                                                                                                                                                         | Description                |
    | :----- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------- |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/activate`](/reference/management-api/deployments/activate/activates-a-deployment-associated-with-an-environment) | **Activate** a environment |
    | `POST` | [`/v1/models/{model_id}/deployments/development/activate`](/reference/management-api/deployments/activate/activates-a-development-deployment)                    | **Activate** development   |
    | `POST` | [`/v1/models/{model_id}/deployments/{deployment_id}/activate`](/reference/management-api/deployments/activate/activates-a-deployment)                            | **Activate** a deployment  |

    ### Deactivate a model deployment

    | Method | Endpoint                                                                                                                                                             | Description                  |
    | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/activate`](/reference/management-api/deployments/deactivate/deactivates-a-deployment-associated-with-an-environment) | **Deactivate** a environment |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/activate`](/reference/management-api/deployments/deactivate/deactivates-a-development-deployment)                    | **Deactivate** development   |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/activate`](/reference/management-api/deployments/deactivate/deactivates-a-deployment)                                | **Deactivate** a deployment  |

    ### Promote a model deployment

    | Method | Endpoint                                                                                                                                                 | Description                              |
    | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------- |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/promote`](/reference/management-api/deployments/promote/promotes-a-deployment-to-an-environment)         | **Promote** to model **environment**     |
    | `POST` | [`/v1/models/{model_id}/environments/{env_name}/cancel_promotion`](/reference/management-api/deployments/promote/cancel-promotion)                       | **Cancel** a promotion to an environment |
    | `POST` | [`/v1/models/{model_id}/deployments/development/promote`](/reference/management-api/deployments/promote/promotes-a-development-deployment-to-production) | **Promote** development deployment       |
    | `POST` | [`/v1/models/{model_id}/deployments/{deployment_id}/promote`](/reference/management-api/deployments/promote/promotes-a-deployment-to-production)         | **Promote** any deployment               |

    ### Autoscaling

    | Method  | Endpoint                                                                                                                                                       | Description                                     |
    | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
    | `PATCH` | [`.../deployments/development/autoscaling_settings`](/reference/management-api/deployments/autoscaling/updates-a-development-deployments-autoscaling-settings) | Updates **development's autoscaling** settings  |
    | `PATCH` | [`.../deployments/{deployment_id}/autoscaling_settings`](/reference/management-api/deployments/autoscaling/updates-a-deployments-autoscaling-settings)         | Updates a **deployment's autoscaling** settings |

    ### Manage deployment endpoints

    | Method | Endpoint                                                                                                                       | Description                  |
    | :----- | :----------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
    | `GET`  | [`/v1/models/{model_id}/deployments`](/reference/management-api/deployments/gets-all-deployments-of-a-model)                   | Get all model deployments    |
    | `GET`  | [`/v1/models/{model_id}/deployments/production`](/reference/management-api/deployments/gets-a-models-production-deployment)    | Production model deployment  |
    | `GET`  | [`/v1/models/{model_id}/deployments/development`](/reference/management-api/deployments/gets-a-models-development-deployment)  | Development model deployment |
    | `GET`  | [`/v1/models/{model_id}/deployments/{deployment_id}`](/reference/management-api/deployments/gets-a-models-deployment-by-id)    | Any model deployment by ID   |
    | `DEL`  | [`/v1/models/{model_id}/deployments/{deployment_id}`](/reference/management-api/deployments/deletes-a-models-deployment-by-id) | Delete model deployments     |
  </Tab>

  <Tab title="Chains">
    ### Promote a Chain deployment

    | Method | Endpoint                                                                                                                                               | Description                  |
    | :----- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
    | `POST` | [`/v1/chains/{chain_id}/environments/{env_name}/promote`](/reference/management-api/deployments/promote/promotes-a-chain-deployment-to-an-environment) | Promote to chain environment |

    ### Autoscaling

    | Method  | Endpoint                                                                                                                                              | Description                                            |
    | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------- |
    | `PATCH` | [`.../chainlet_settings/autoscaling_settings`](/reference/management-api/deployments/autoscaling/update-a-chainlet-environments-autoscaling-settings) | **Update chainlet** environment's autoscaling settings |

    ### Manage Chain deployments

    | Method | Endpoint                                                                                                                            | Description                  |
    | :----- | :---------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
    | `GET`  | [`/v1/chains/{chain_id}/deployments`](/reference/management-api/deployments/gets-all-chain-deployments)                             | Get all chain deployments    |
    | `GET`  | [`/v1/chains/{chain_id}/deployments/{chain_deployment_id}`](/reference/management-api/deployments/gets-a-chain-deployment-by-id)    | Any chain deployment by ID   |
    | `DEL`  | [`/v1/chains/{chain_id}/deployments/{chain_deployment_id}`](/reference/management-api/deployments/deletes-a-chain-deployment-by-id) | **Delete** chain deployments |
  </Tab>
</Tabs>

# Environment endpoints

<Tabs>
  <Tab title="Models">
    | Method  | Endpoint                                                                                                                  | Description                |
    | :------ | :------------------------------------------------------------------------------------------------------------------------ | :------------------------- |
    | `POST`  | [`/v1/models/{model_id}/environments`](/reference/management-api/environments/create-an-environment)                      | Create environment         |
    | `GET`   | [`/v1/models/{model_id}/environments`](/reference/management-api/environments/get-all-environments)                       | Get all environments       |
    | `GET`   | [`/v1/models/{model_id}/environments/{env_name}`](/reference/management-api/environments/get-an-environments-details)     | Get an environment details |
    | `PATCH` | [`/v1/models/{model_id}/environments/{env_name}`](/reference/management-api/environments/update-an-environments-settings) | Update model environment   |
  </Tab>

  <Tab title="Chains">
    | Method  | Endpoint                                                                                                                                                                                | Description                                 |
    | :------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------ |
    | `POST`  | [`/v1/chains/{chain_id}/environments`](/reference/management-api/environments/create-a-chain-environment)                                                                               | Create chain environment                    |
    | `GET`   | [`/v1/chains/{chain_id}/environments`](/reference/management-api/environments/get-all-chain-environments)                                                                               | Get all chain environments                  |
    | `GET`   | [`/v1/chains/{chain_id}/environments/{env_name}`](/reference/management-api/environments/get-a-chain-environments-details)                                                              | Get a chain environment                     |
    | `PATCH` | [`/v1/chains/{chain_id}/environments/{env_name}`](/reference/management-api/environments/update-a-chain-environments-settings)                                                          | Update chain environment                    |
    | `POST`  | [`/v1/chains/{chain_id}/environments/{env_name}/chainlet_settings/instance_types/update`](/reference/management-api/environments/update-a-chainlet-environments-instance-type-settings) | Update chainlet environment's instance type |
  </Tab>
</Tabs>

# Secret endpoints

| Method | Endpoint                                                            | Description                                               |
| :----- | :------------------------------------------------------------------ | :-------------------------------------------------------- |
| `GET`  | [`/v1/secrets`](/reference/management-api/secrets/gets-all-secrets) | Get all secrets                                           |
| `POST` | [`/v1/secrets`](/reference/management-api/secrets/upserts-a-secret) | Create a new secret or updates an existing secret secret. |

# API Key endpoints

| Method   | Endpoint                                                                      | Description                      |
| :------- | :---------------------------------------------------------------------------- | :------------------------------- |
| `GET`    | [`/v1/api_keys`](/reference/management-api/api-keys/lists-the-users-api-keys) | Get all API keys.                |
| `POST`   | [`/v1/api_keys`](/reference/management-api/api-keys/creates-an-api-key)       | Create a new API key.            |
| `DELETE` | [`/v1/api_keys`](/reference/management-api/api-keys/delete-an-api-key)        | Delete an API key by its prefix. |

# Training Job endpoints

| Method | Endpoint                                                                                                                                           | Description                       |
| :----- | :------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------- |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs`](/reference/training-api/list-training-jobs)                                                   | Get all training jobs             |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}`](/reference/training-api/get-training-job)                                   | Get training job by ID            |
| `POST` | [`/v1/training_jobs/search`](/reference/training-api/search-training-jobs)                                                                         | Search training jobs              |
| `POST` | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/stop`](/reference/training-api/stop-training-job)                             | Stop a training job               |
| `POST` | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/recreate`](/reference/training-api/recreate-training-job)                     | Recreate a training job           |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoints`](/reference/training-api/get-training-job-checkpoints)           | Get training job checkpoints      |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files`](/reference/training-api/get-training-job-checkpoint-files) | Get training job checkpoint files |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs`](/reference/training-api/get-training-job-logs)                         | Get training job logs             |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics`](/reference/training-api/get-training-job-metrics)                   | Get training job metrics          |
| `GET`  | [`/v1/training_projects/{training_project_id}/jobs/{training_job_id}/download`](/reference/training-api/download-training-job)                     | Download training job artifacts   |


# Get all secrets
Source: https://docs.baseten.co/reference/management-api/secrets/gets-all-secrets

get /v1/secrets



# Upsert a secret
Source: https://docs.baseten.co/reference/management-api/secrets/upserts-a-secret

post /v1/secrets
Creates a new secret or updates an existing secret if one with the provided name already exists. The name and creation date of the created or updated secret is returned.



# Reference documentation
Source: https://docs.baseten.co/reference/overview

For deploying, managing, and interacting with machine learning models on Baseten.

This reference section documents our API, CLI, and Python SDK—whether you're deploying models, managing inference chains, or calling endpoints in production.

# API Reference

Baseten provides two sets of API endpoints:

<CardGroup cols={2}>
  <Card title="Inference API" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference-api.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=db298df57b8b5162245c0288b629fdfe" href="/reference/inference-api/overview" data-og-width="956" width="956" data-og-height="458" height="458" data-path="images/inference-api.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference-api.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=9982f03f0affc8312745a1402b3447d8 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference-api.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=2fb9c1e0c4a4665921d18d549698f481 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference-api.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e371e48cce82d0a299c6a405404c7aa2 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference-api.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=7b833151112352f77ced33630d746667 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference-api.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=e6a0d200eb8c50b4b20ae1292d158a28 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/inference-api.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=4f37b7f16aa2f537df2cc38038ef8780 2500w">
    For calling deployed models and chains.
  </Card>

  <Card title="Management API" img="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/management-api.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=54a53f56d9b3798b3473734288242684" href="/reference/management-api/overview" data-og-width="956" width="956" data-og-height="458" height="458" data-path="images/management-api.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/management-api.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=acca67a3e8b37964c3c411edc05d5b95 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/management-api.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c1fd71607497ce40f17af54bd6c3eace 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/management-api.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1683d63e774c01bff1dac560c8bbf4f1 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/management-api.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=98e34a8389f74d2c1915e4447f648ef6 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/management-api.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=59fa9aacaa64df5f1d25a4d48360fc78 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/management-api.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=35509add742aeb071e5ff90ada2f130a 2500w">
    For managing models, workspaces, and training jobs.
  </Card>
</CardGroup>

# CLI Reference

The CLI provides a command-line interface for managing deployments, running local inference, and configuring Truss models.

* [Truss CLI reference](/reference/cli/truss/overview) – Commands for initializing, deploying, and managing models.
* [Chains CLI reference](/reference/cli/chains/chains-cli) – Commands for orchestrating multi-model workflows.
* [Training CLI reference](/reference/cli/training/training-cli) – Commands for managing training jobs.

***

# SDK Reference

The Python SDK provides an abstraction for deploying models, managing deployments, and interacting with models via code.

* [Truss SDK reference](/reference/sdk/truss) – Deploy and interact with Truss models using Python.
* [Chains SDK reference](/reference/sdk/chains) – Build and manage inference chains programmatically.
* [Training SDK reference](/reference/sdk/training) – Deploy and interact with trained models using Python.


# Chains SDK Reference
Source: https://docs.baseten.co/reference/sdk/chains

Python SDK Reference for Chains

# Chainlet classes

APIs for creating user-defined Chainlets.

### *class* `truss_chains.ChainletBase`

Base class for all chainlets.

Inheriting from this class adds validations to make sure subclasses adhere to the
chainlet pattern and facilitates remote chainlet deployment.

Refer to [the docs](/development/chain/getting-started) and this
[example chainlet](https://github.com/basetenlabs/truss/blob/main/truss-chains/truss_chains/reference_code/reference_chainlet.py)
for more guidance on how to create subclasses.

### *class* `truss_chains.ModelBase`

Base class for all standalone models.

Inheriting from this class adds validations to make sure subclasses adhere to the
truss model pattern.

### *class* `truss_chains.EngineBuilderLLMChainlet`

#### *method final async* run\_remote(llm\_input)

**Parameters:**

| Name        | Type                    | Description                |
| ----------- | ----------------------- | -------------------------- |
| `llm_input` | *EngineBuilderLLMInput* | OpenAI compatible request. |

* **Returns:**
  *AsyncIterator*\[str]

### *function* `truss_chains.depends`

Sets a “symbolic marker” to indicate to the framework that a chainlet is a
dependency of another chainlet. The return value of `depends` is intended to be
used as a default argument in a chainlet’s `__init__`-method.
When deploying a chain remotely, a corresponding stub to the remote is injected in
its place. In [`run_local`](#function-truss-chains-run-local) mode an instance
of a local chainlet is injected.

Refer to [the docs](/development/chain/getting-started) and this
[example chainlet](https://github.com/basetenlabs/truss/blob/main/truss-chains/truss_chains/reference_code/reference_chainlet.py)
for more guidance on how make one chainlet depend on another chainlet.

<Warning>
  Despite the type annotation, this does *not* immediately provide a
  chainlet instance. Only when deploying remotely or using `run_local` a
  chainlet instance is provided.
</Warning>

**Parameters:**

| Name                | Type                                                      | Default | Description                                                                                                                                                                                                                                                                                |
| ------------------- | --------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `chainlet_cls`      | *Type\[[ChainletBase](#class-truss-chains-chainletbase)]* |         | The chainlet class of the dependency.                                                                                                                                                                                                                                                      |
| `retries`           | *int*                                                     | `1`     | The number of times to retry the remote chainlet in case of failures (e.g. due to transient network issues). For streaming, retries are only made if the request fails before streaming any results back. Failures mid-stream not retried.                                                 |
| `timeout_sec`       | *float*                                                   | `600.0` | Timeout for the HTTP request to this chainlet.                                                                                                                                                                                                                                             |
| `use_binary`        | *bool*                                                    | `False` | Whether to send data in binary format. This can give a parsing speedup and message size reduction (\~25%) for numpy arrays. Use `NumpyArrayField` as a field type on pydantic models for integration and set this option to `True`. For simple text data, there is no significant benefit. |
| `concurrency_limit` | *int*                                                     | `300`   | The maximum number of concurrent requests to send to the remote chainlet. Excessive requests will be queued and a warning will be shown. Try to design your algorithm in a way that spreads requests evenly over time so that this the default value can be used.                          |

* **Returns:**
  A “symbolic marker” to be used as a default argument in a chainlet’s
  initializer.

### *function* `truss_chains.depends_context`

Sets a “symbolic marker” for injecting a context object at runtime.

Refer to [the docs](/development/chain/getting-started) and this
[example chainlet](https://github.com/basetenlabs/truss/blob/main/truss-chains/truss_chains/reference_code/reference_chainlet.py)
for more guidance on the `__init__`-signature of chainlets.

<Warning>
  Despite the type annotation, this does *not* immediately provide a
  context instance. Only when deploying remotely or using `run_local` a
  context instance is provided.
</Warning>

* **Returns:**
  A “symbolic marker” to be used as a default argument in a chainlet’s
  initializer.

### *class* `truss_chains.DeploymentContext`

Bases: `pydantic.BaseModel`

Bundles config values and resources needed to instantiate Chainlets.

The context can optionally be added as a trailing argument in a Chainlet’s
`__init__` method and then used to set up the chainlet (e.g. using a secret as
an access token for downloading model weights).

**Parameters:**

| Name                  | Type                                                                                       | Default | Description                                                                                                                                                                                              |
| --------------------- | ------------------------------------------------------------------------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `chainlet_to_service` | *Mapping\[str,[DeployedServiceDescriptor](#class-truss-chains-deployedservicedescriptor)]* |         | A mapping from chainlet names to service descriptors. This is used to create RPC sessions to dependency chainlets. It contains only the chainlet services that are dependencies of the current chainlet. |
| `secrets`             | *Mapping\[str,str]*                                                                        |         | A mapping from secret names to secret values. It contains only the secrets that are listed in `remote_config.assets.secret_keys` of the current chainlet.                                                |
| `data_dir`            | *Path\|None*                                                                               | `None`  | The directory where the chainlet can store and access data, e.g. for downloading model weights.                                                                                                          |
| `environment`         | *[Environment](#class-truss-chains-environment)\|None*                                     | `None`  | The environment that the chainlet is deployed in. None if the chainlet is not associated with an environment.                                                                                            |

#### *method* get\_baseten\_api\_key()

* **Returns:**
  str

#### *method* get\_service\_descriptor(chainlet\_name)

**Parameters:**

| Name            | Type  | Description               |
| --------------- | ----- | ------------------------- |
| `chainlet_name` | *str* | The name of the chainlet. |

* **Returns:**
  [*DeployedServiceDescriptor*](#class-truss-chains-deployedservicedescriptor)

### *class* `truss_chains.Environment`

Bases: `pydantic.BaseModel`

The environment the chainlet is deployed in.

* **Parameters:**
  **name** (*str*) – The name of the environment.

### *class* `truss_chains.ChainletOptions`

Bases: `pydantic.BaseModel`

**Parameters:**

| Name                     | Type                                                  | Default                                  | Description                                                                                                                                                                                                                                                   |
| ------------------------ | ----------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enable_b10_tracing`     | *bool*                                                | `False`                                  | enables baseten-internal trace data collection. This helps baseten engineers better analyze chain performance in case of issues. It is independent of a potentially user-configured tracing instrumentation. Turning this on, could add performance overhead. |
| `enable_debug_logs`      | *bool*                                                | `False`                                  | Sets log level to debug in deployed server.                                                                                                                                                                                                                   |
| `env_variables`          | *Mapping\[str,str]*                                   | `{}`                                     | static environment variables available to the deployed chainlet.                                                                                                                                                                                              |
| `health_checks`          | *HealthChecks*                                        | `truss.base.truss_config.HealthChecks()` | Configures health checks for the chainlet. See [guide](https://docs.baseten.co/truss/guides/custom-health-checks#chains).                                                                                                                                     |
| `metadata`               | *JsonValue\|None*                                     | `None`                                   | Arbitrary JSON object to describe chainlet.                                                                                                                                                                                                                   |
| `streaming_read_timeout` | *int*                                                 | `60`                                     | Amount of time (in seconds) between each streamed chunk before a timeout is triggered.                                                                                                                                                                        |
| `transport`              | *Union\[HTTPOptions\|WebsocketOptions\|GRPCOptions]'* | `None`                                   | Allows to customize certain transport protocols, e.g. websocket pings.                                                                                                                                                                                        |

### *class* `truss_chains.RPCOptions`

Bases: `pydantic.BaseModel`

Options to customize RPCs to dependency chainlets.

**Parameters:**

| Name                | Type    | Default | Description                                                                                                                                                                                                                                                                                |
| ------------------- | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `retries`           | *int*   | `1`     | The number of times to retry the remote chainlet in case of failures (e.g. due to transient network issues). For streaming, retries are only made if the request fails before streaming any results back. Failures mid-stream not retried.                                                 |
| `timeout_sec`       | *float* | `600.0` | Timeout for the HTTP request to this chainlet.                                                                                                                                                                                                                                             |
| `use_binary`        | *bool*  | `False` | Whether to send data in binary format. This can give a parsing speedup and message size reduction (\~25%) for numpy arrays. Use `NumpyArrayField` as a field type on pydantic models for integration and set this option to `True`. For simple text data, there is no significant benefit. |
| `concurrency_limit` | *int*   | `300`   | The maximum number of concurrent requests to send to the remote chainlet. Excessive requests will be queued and a warning will be shown. Try to design your algorithm in a way that spreads requests evenly over time so that this the default value can be used.                          |

### *function* `truss_chains.mark_entrypoint`

Decorator to mark a chainlet as the entrypoint of a chain.

This decorator can be applied to *one* chainlet in a source file and then the
CLI push command simplifies: only the file, not the class within, must be specified.

Optionally a display name for the Chain (not the Chainlet) can be set (effectively
giving a custom default value for the `name` arg of the CLI push command).

Example usage:

```python  theme={"system"}
import truss_chains as chains

@chains.mark_entrypoint
class MyChainlet(ChainletBase):
    ...

# OR with custom Chain name.
@chains.mark_entrypoint("My Chain Name")
class MyChainlet(ChainletBase):
    ...
```

# Remote Configuration

These data structures specify for each chainlet how it gets deployed remotely, e.g. dependencies and compute resources.

### *class* `truss_chains.RemoteConfig`

Bases: `pydantic.BaseModel`

Bundles config values needed to deploy a chainlet remotely.

This is specified as a class variable for each chainlet class, e.g.:

```python  theme={"system"}
import truss_chains as chains


class MyChainlet(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            pip_requirements=["torch==2.0.1", ...]
        ),
        compute=chains.Compute(cpu_count=2, gpu="A10G", ...),
        assets=chains.Assets(secret_keys=["hf_access_token"], ...),
    )
```

**Parameters:**

| Name           | Type                                                     | Default                          |
| -------------- | -------------------------------------------------------- | -------------------------------- |
| `docker_image` | *[DockerImage](#class-truss-chains-dockerimage)*         | `truss_chains.DockerImage()`     |
| `compute`      | *[Compute](#class-truss-chains-compute)*                 | `truss_chains.Compute()`         |
| `assets`       | *[Assets](#class-truss-chains-assets)*                   | `truss_chains.Assets()`          |
| `name`         | *str\|None*                                              | `None`                           |
| `options`      | *[ChainletOptions](#class-truss-chains-chainletoptions)* | `truss_chains.ChainletOptions()` |

### *class* `truss_chains.DockerImage`

Bases: `pydantic.BaseModel`

Configures the docker image in which a remoted chainlet is deployed.

<Note>
  Any paths are relative to the source file where `DockerImage` is
  defined and must be created with the helper function \[`make_abs_path_here`]
  (#function-truss-chains-make-abs-path-here).
  This allows you for example organize chainlets in different (potentially nested)
  modules and keep their requirement files right next their python source files.
</Note>

**Parameters:**

| Name                            | Type                                                                                               | Default                       | Description                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `base_image`                    | *[BasetenImage](#class-truss-chains-basetenimage)\|[CustomImage](#class-truss-chains-customimage)* | `truss_chains.BasetenImage()` | The base image used by the chainlet. Other dependencies and assets are included as additional layers on top of that image. You can choose a Baseten default image for a supported python version (e.g. `BasetenImage.PY311`), this will also include GPU drivers if needed, or provide a custom image (e.g. `CustomImage(image="python:3.11-slim")`).                                      |
| `pip_requirements_file`         | *AbsPath\|None*                                                                                    | `None`                        | Path to a file containing pip requirements. The file content is naively concatenated with `pip_requirements`.                                                                                                                                                                                                                                                                              |
| `pip_requirements`              | *list\[str]*                                                                                       | `[]`                          | A list of pip requirements to install.  The items are naively concatenated with the content of the `pip_requirements_file`.                                                                                                                                                                                                                                                                |
| `apt_requirements`              | *list\[str]*                                                                                       | `[]`                          | A list of apt requirements to install.                                                                                                                                                                                                                                                                                                                                                     |
| `data_dir`                      | *AbsPath\|None*                                                                                    | `None`                        | Data from this directory is copied into the docker image and accessible to the remote chainlet at runtime.                                                                                                                                                                                                                                                                                 |
| `external_package_dirs`         | *list\[AbsPath]\|None*                                                                             | `None`                        | A list of directories containing additional python packages outside the chain’s workspace dir, e.g. a shared library. This code is copied into the docker image and importable at runtime.                                                                                                                                                                                                 |
| `truss_server_version_override` | *str\|None*                                                                                        | `None`                        | By default, deployed Chainlets use the truss server implementation corresponding to the truss version of the user’s CLI. To use a specific version, e.g. pinning it for exact reproducibility, the version can be overridden here. Valid versions correspond to truss releases on PyPi: [https://pypi.org/project/truss/#history](https://pypi.org/project/truss/#history), e.g. “0.9.80”. |

### *class* `truss_chains.BasetenImage`

Bases: `Enum`

Default images, curated by baseten, for different python versions. If a Chainlet
uses GPUs, drivers will be included in the image.

| Enum Member | Value   |
| ----------- | ------- |
| `PY39`      | *py39*  |
| `PY310`     | *py310* |
| `PY311 `    | *py311* |

### *class* `truss_chains.CustomImage`

Bases: `pydantic.BaseModel`

Configures the usage of a custom image hosted on dockerhub.

**Parameters:**

| Name                     | Type                       | Default | Description                                                                                            |
| ------------------------ | -------------------------- | ------- | ------------------------------------------------------------------------------------------------------ |
| `image`                  | *str*                      |         | Reference to image on dockerhub.                                                                       |
| `python_executable_path` | *str\|None*                | `None`  | Absolute path to python executable (if default `python` is ambiguous).                                 |
| `docker_auth`            | *DockerAuthSettings\|None* | `None`  | See [corresponding truss config](/development/model/base-images#example%3A-docker-hub-authentication). |

### *class* `truss_chains.Compute`

Specifies which compute resources a chainlet has in the *remote* deployment.

<Note>
  Not all combinations can be exactly satisfied by available hardware, in some
  cases more powerful machine types are chosen to make sure requirements are met
  or over-provisioned. Refer to the
  [baseten instance reference](https://docs.baseten.co/deployment/resources).
</Note>

**Parameters:**

| Name                  | Type                          | Default | Description                                                                                                     |
| --------------------- | ----------------------------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| `cpu_count`           | *int*                         | `1`     | Minimum number of CPUs to allocate.                                                                             |
| `memory`              | *str*                         | `'2Gi'` | Minimum memory to allocate, e.g. “2Gi” (2 gibibytes).                                                           |
| `gpu`                 | *str\|Accelerator\|None*      | `None`  | GPU accelerator type, e.g. “A10G”, “A100”, refer to the [truss config](/deployment/resources) for more choices. |
| `gpu_count`           | *int*                         | `1`     | Number of GPUs to allocate.                                                                                     |
| `predict_concurrency` | *int\|Literal\['cpu\_count']* | `1`     | Number of concurrent requests a single replica of a deployed chainlet handles.                                  |

Concurrency concepts are explained in [this guide](/development/model/performance/concurrency#2-predict-concurrency).
It is important to understand the difference between predict\_concurrency and
the concurrency target (used for autoscaling, i.e. adding or removing replicas).
Furthermore, the `predict_concurrency` of a single instance is implemented in
two ways:

* Via python’s `asyncio`, if `run_remote` is an async def. This
  requires that `run_remote` yields to the event loop.
* With a threadpool if it’s a synchronous function. This requires
  that the threads don’t have significant CPU load (due to the GIL).

### *class* `truss_chains.Assets`

Specifies which assets a chainlet can access in the remote deployment.

For example, model weight caching can be used like this:

```python  theme={"system"}
import truss_chains as chains
from truss.base import truss_config

mistral_cache = truss_config.ModelRepo(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    allow_patterns=["*.json", "*.safetensors", ".model"]
)
chains.Assets(cached=[mistral_cache], ...)
```

**Parameters:**

| Name            | Type                          | Default | Description                                                                                                                                                     |
| --------------- | ----------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cached`        | *Iterable\[ModelRepo]*        | `()`    | One or more `truss_config.ModelRepo` objects.                                                                                                                   |
| `secret_keys`   | *Iterable\[str]*              | `()`    | Names of secrets stored on baseten, that the chainlet should have access to. You can manage secrets on baseten [here](https://app.baseten.co/settings/secrets). |
| `external_data` | *Iterable\[ExternalDataItem]* | `()`    | Data to be downloaded from public URLs and made available in the deployment (via `context.data_dir`).                                                           |

# Core

General framework and helper functions.

### *function* `truss_chains.push`

Deploys a chain remotely (with all dependent chainlets).

**Parameters:**

| Name                    | Type                             | Default     | Description                                                                                                                                                  |
| ----------------------- | -------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `entrypoint`            | *Type\[ChainletT]*               |             | The chainlet class that serves as the entrypoint to the chain.                                                                                               |
| `chain_name`            | *str*                            |             | The name of the chain.                                                                                                                                       |
| `publish`               | *bool*                           | `True`      | Whether to publish the chain as a published deployment (it is a draft deployment otherwise)                                                                  |
| `promote`               | *bool*                           | `True`      | Whether to promote the chain to be the production deployment (this implies publishing as well).                                                              |
| `only_generate_trusses` | *bool*                           | `False`     | Used for debugging purposes. If set to True, only the the underlying truss models for the chainlets are generated in `/tmp/.chains_generated`.               |
| `remote`                | *str*                            | `'baseten'` | name of a remote config in .trussrc. If not provided, it will be inquired.                                                                                   |
| `environment`           | *str\|None*                      | `None`      | The name of an environment to promote deployment into.                                                                                                       |
| `progress_bar`          | *Type\[progress.Progress]\|None* | `None`      | Optional rich.progress.Progress if output is desired.                                                                                                        |
| `include_git_info`      | *bool*                           | `False`     | Whether to attach git versioning info (sha, branch, tag) to deployments made from within a git repo. If set to True in .trussrc, it will always be attached. |

* **Returns:**
  [*ChainService*](#class-truss-chains-remote-chainservice): A chain service
  handle to the deployed chain.

### *class* `truss_chains.deployment.deployment_client.ChainService`

Handle for a deployed chain.

A `ChainService` is created and returned when using `push`. It
bundles the individual services for each chainlet in the chain, and provides
utilities to query their status, invoke the entrypoint etc.

#### *method* get\_info()

Queries the statuses of all chainlets in the chain.

* **Returns:**
  List of `DeployedChainlet`, `(name, is_entrypoint, status, logs_url)`
  for each chainlet.

#### *property* name *: str*

#### *method* run\_remote(json)

Invokes the entrypoint with JSON data.

**Parameters:**

| Name   | Type        | Description                  |
| ------ | ----------- | ---------------------------- |
| `json` | *JSON dict* | Input data to the entrypoint |

* **Returns:**
  The JSON response.

#### *property* run\_remote\_url *: str*

URL to invoke the entrypoint.

#### *property* status\_page\_url *: str*

Link to status page on Baseten.

### *function* `truss_chains.make_abs_path_here`

Helper to specify file paths relative to the *immediately calling* module.

E.g. in you have a project structure like this:

```default  theme={"system"}
root/
    chain.py
    common_requirements.text
    sub_package/
        chainlet.py
        chainlet_requirements.txt
```

You can now in `root/sub_package/chainlet.py` point to the requirements
file like this:

```python  theme={"system"}
shared = make_abs_path_here("../common_requirements.text")
specific = make_abs_path_here("chainlet_requirements.text")
```

<Warning>
  This helper uses the directory of the immediately calling module as an
  absolute reference point for resolving the file location. Therefore,
  you MUST NOT wrap the instantiation of `make_abs_path_here` into a
  function (e.g. applying decorators) or use dynamic code execution.

  Ok:

  ```python  theme={"system"}
  def foo(path: AbsPath):
      abs_path = path.abs_path


  foo(make_abs_path_here("./somewhere"))
  ```

  Not Ok:

  ```python  theme={"system"}
  def foo(path: str):
      dangerous_value = make_abs_path_here(path).abs_path


  foo("./somewhere")
  ```
</Warning>

**Parameters:**

| Name        | Type  | Description                |
| ----------- | ----- | -------------------------- |
| `file_path` | *str* | Absolute or relative path. |

* **Returns:**
  *AbsPath*

### *function* `truss_chains.run_local`

Context manager local debug execution of a chain.

The arguments only need to be provided if the chainlets explicitly access any the
corresponding fields of [`DeploymentContext`](#class-truss-chains-deploymentcontext).

**Parameters:**

| Name                  | Type                                                                                       | Default | Description                                                    |
| --------------------- | ------------------------------------------------------------------------------------------ | ------- | -------------------------------------------------------------- |
| `secrets`             | *Mapping\[str,str]\|None*                                                                  | `None`  | A dict of secrets keys and values to provide to the chainlets. |
| `data_dir`            | *Path\|str\|None*                                                                          | `None`  | Path to a directory with data files.                           |
| `chainlet_to_service` | *Mapping\[str,[DeployedServiceDescriptor](#class-truss-chains-deployedservicedescriptor)]* | `None`  | A dict of chainlet names to service descriptors.               |

Example usage (as trailing main section in a chain file):

```python  theme={"system"}
import os
import truss_chains as chains


class HelloWorld(chains.ChainletBase):
    ...


if __name__ == "__main__":
    with chains.run_local(
        secrets={"some_token": os.environ["SOME_TOKEN"]},
        chainlet_to_service={
            "SomeChainlet": chains.DeployedServiceDescriptor(
                name="SomeChainlet",
                display_name="SomeChainlet",
                predict_url="https://...",
                options=chains.RPCOptions(),
            )
        },
    ):
        hello_world_chain = HelloWorld()
        result = hello_world_chain.run_remote(max_value=5)

    print(result)
```

Refer to the [local debugging guide](/development/chain/localdev)
for more details.

### *class* `truss_chains.DeployedServiceDescriptor`

Bases: `pydantic.BaseModel`

Bundles values to establish an RPC session to a dependency chainlet,
specifically with `StubBase`.

**Parameters:**

| Name           | Type                                           | Default |
| -------------- | ---------------------------------------------- | ------- |
| `name`         | *str*                                          |         |
| `display_name` | *str*                                          |         |
| `options`      | *[RPCOptions](#class-truss-chains-rpcoptions)* |         |
| `predict_url`  | *str\|None*                                    | `None`  |
| `internal_url` | *InternalURL*                                  | `None`  |

### *class* `truss_chains.StubBase`

Bases: `BasetenSession`, `ABC`

Base class for stubs that invoke remote chainlets.

Extends `BasetenSession` with methods for data serialization, de-serialization
and invoking other endpoints.

It is used internally for RPCs to dependency chainlets, but it can also be used
in user-code for wrapping a deployed truss model into the Chains framework. It
flexibly supports JSON and pydantic inputs and output. Example usage:

```python  theme={"system"}
import pydantic
import truss_chains as chains


class WhisperOutput(pydantic.BaseModel):
    ...


class DeployedWhisper(chains.StubBase):
    # Input JSON, output JSON.
    async def run_remote(self, audio_b64: str) -> Any:
        return await self.predict_async(
            inputs={"audio": audio_b64})
        # resp == {"text": ..., "language": ...}

    # OR Input JSON, output pydantic model.
    async def run_remote(self, audio_b64: str) -> WhisperOutput:
        return await self.predict_async(
            inputs={"audio": audio_b64}, output_model=WhisperOutput)

    # OR Input and output are pydantic models.
    async def run_remote(self, data: WhisperInput) -> WhisperOutput:
        return await self.predict_async(data, output_model=WhisperOutput)


class MyChainlet(chains.ChainletBase):

    def __init__(self, ..., context=chains.depends_context()):
        ...
        self._whisper = DeployedWhisper.from_url(
            WHISPER_URL,
            context,
            options=chains.RPCOptions(retries=3),
        )

    async def run_remote(self, ...):
       await self._whisper.run_remote(...)
```

**Parameters:**

| Name                 | Type                                                                          | Description                               |
| -------------------- | ----------------------------------------------------------------------------- | ----------------------------------------- |
| `service_descriptor` | *[DeployedServiceDescriptor](#class-truss-chains-deployedservicedescriptor)]* | Contains the URL and other configuration. |
| `api_key`            | *str*                                                                         | A baseten API key to authorize requests.  |

#### *classmethod* from\_url(predict\_url, context\_or\_api\_key, options=None)

Factory method, convenient to be used in chainlet’s `__init__`-method.

**Parameters:**

| Name                 | Type                                                         | Description                                                                          |
| -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `predict_url`        | *str*                                                        | URL to predict endpoint of another chain / truss model.                              |
| `context_or_api_key` | *[DeploymentContext](#class-truss-chains-deploymentcontext)* | Deployment context object, obtained in the chainlet’s `__init__` or Baseten API key. |
| `options`            | *[RPCOptions](#class-truss-chains-rpcoptions)*               | RPC options, e.g. retries.                                                           |

#### Invocation Methods

* `async predict_async(inputs: PydanticModel, output_model: Type[PydanticModel]) → PydanticModel`
* `async predict_async(inputs: JSON, output_model: Type[PydanticModel]) →
   PydanticModel`
* `async predict_async(inputs: JSON) → JSON`
* `async predict_async_stream(inputs: PydanticModel | JSON) -> AsyncIterator[bytes]`

Deprecated synchronous methods:

* `predict_sync(inputs: PydanticModel, output_model: Type[PydanticModel]) → PydanticModel`
* `predict_sync(inputs: JSON, output_model: Type[PydanticModel]) → PydanticModel`
* `predict_sync(inputs: JSON) → JSON`

### *class* `truss_chains.RemoteErrorDetail`

Bases: `pydantic.BaseModel`

When a remote chainlet raises an exception, this pydantic model contains
information about the error and stack trace and is included in JSON form in the
error response.

**Parameters:**

| Name                    | Type                |
| ----------------------- | ------------------- |
| `exception_cls_name`    | *str*               |
| `exception_module_name` | *str\|None*         |
| `exception_message`     | *str*               |
| `user_stack_trace`      | *list\[StackFrame]* |

#### *method* format()

Format the error for printing, similar to how Python formats exceptions
with stack traces.

* **Returns:**
  str

### *class* `truss_chains.GenericRemoteException`

Bases: `Exception`

Raised when calling a remote chainlet results in an error and it is not possible
to re-raise the same exception that was raise remotely in the caller.


# Training
Source: https://docs.baseten.co/reference/sdk/training

Reference documentation for Baseten's Training SDK classes and configuration.

The Training SDK provides classes for configuring and managing machine learning model training jobs on Baseten. This reference documents the key classes used to define training configurations.

# Deploy a `TrainingJob`

To deploy a training job, use the following command:

```bash  theme={"system"}
truss train push <path_to_config_file>
```

The following classes are used to configure and deploy training jobs:

## TrainingJob

Defines a complete training job configuration.

```python  theme={"system"}
class TrainingJob:
    image: Image              # Container image configuration
    compute: Compute         # Compute resource configuration
    runtime: Runtime        # Runtime environment configuration
```

Example usage:

```python  theme={"system"}
training_job = TrainingJob(
    image=Image(base_image="pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime"),
    compute=Compute(cpu_count=4, memory="16Gi"),
    runtime=Runtime(
        start_commands=["python train.py"],
        checkpointing_config=CheckpointingConfig(enabled=True),
        cache_config=CacheConfig(enabled=True),
    )
)
```

## TrainingProject

Organizes training jobs and provides project-level configuration.

```python  theme={"system"}
class TrainingProject:
    name: str           # Project name
    job: TrainingJob   # Training job configuration
```

Example usage:

```python  theme={"system"}
project = TrainingProject(
    name="llm-fine-tuning",
    job=training_job
)
```

## Image

Specifies the container image for the training environment.

```python  theme={"system"}
class Image:
    base_image: str  # Docker image to use for training
    docker_auth: Optional[DockerAuth] # Authentication details for private docker images
```

Example usage:

```python  theme={"system"}
image = Image(base_image="pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime")
```

### DockerAuth

Configures authentication for private Docker registries. Ensure that any SecretReference
used has been set in your Baseten Workspace. See [secrets](/observability/secrets) for more details.

```python  theme={"system"}
class DockerAuth:
    auth_method: truss_config.DockerAuthType  # Authentication method type
    registry: str                              # Docker registry URL
    aws_iam_docker_auth: Optional[AWSIAMDockerAuth] = None
    gcp_service_account_json_docker_auth: Optional[GCPServiceAccountJSONDockerAuth] = None
```

#### AWSIAMDockerAuth

Authenticates with AWS ECR using IAM credentials.

```python  theme={"system"}
class AWSIAMDockerAuth:
    access_key_secret_ref: SecretReference      # AWS access key ID as a secret reference
    secret_access_key_secret_ref: SecretReference  # AWS secret access key as a secret reference
```

#### GCPServiceAccountJSONDockerAuth

Authenticates with Google Container Registry using service account JSON.

```python  theme={"system"}
class GCPServiceAccountJSONDockerAuth:
    service_account_json_secret_ref: SecretReference  # GCP service account JSON secret reference
```

#### Example

Example usage with GCP:

```python  theme={"system"}
# Configure image with GCP authentication
image = Image(
    base_image="gcr.io/my-project/my-repo/my-private-image:latest",
    docker_auth=DockerAuth(
        auth_method=truss_config.DockerAuthType.GCP_SERVICE_ACCOUNT_JSON,
        registry="gcr.io",
        gcp_service_account_json_docker_auth=GCPServiceAccountJSONDockerAuth(
            service_account_json_secret_ref=SecretReference(name="gcp_service_account_json")
        )
    )
)
```

## Compute

Specifies compute resources for training jobs.

```python  theme={"system"}
class Compute:
    node_count: int = 1      # Number of nodes for distributed training
    cpu_count: int = 1       # Number of CPU cores
    memory: str = "2Gi"      # Memory allocation
    accelerator: Optional[AcceleratorSpec] = None  # GPU configuration
```

Example usage:

```python  theme={"system"}
# Configure a training job with 2 GPUs and 4 CPUs
compute = Compute(
    accelerator=AcceleratorSpec(accelerator="H100", count=4)
)
```

## Runtime

Defines the runtime environment for training jobs.

```python  theme={"system"}
class Runtime:
    start_commands: List[str] = []  # Commands to run at job start
    environment_variables: Dict[str, Union[str, SecretReference]] = {}
    enable_cache: bool = False      # Enable caching
    checkpointing_config: CheckpointingConfig = CheckpointingConfig()
```

Example usage:

```python  theme={"system"}
runtime = Runtime(
    start_commands=["python train.py"],
    environment_variables={
        "BATCH_SIZE": "32",
        "WANDB_API_KEY": SecretReference(name="WANDB_KEY")
    },
    checkpointing_config=CheckpointingConfig(enabled=True)
)
```

### Training Cache

By default, the training cache provides two mount locations:

* [`$BT_PROJECT_CACHE_DIR`](#baseten-provided-environment-variables), which is shared and accessible by all jobs within a Project ID
* [`$BT_TEAM_CACHE_DIR`](#baseten-provided-environment-variables) which is shared by jobs that belong to the same Team.

Baseten will export these variables in your job's environment.

The cache storage is separate from ephemeral storage limits of your training job. Training Projects provide storage segragation within the cache. Training jobs within the same project share the same cache, while training jobs in different projects cannot access each other's data.

Example usage:

```python  theme={"system"}
runtime = Runtime(
    start_commands=["python train.py"],
    environment_variables={
        "BATCH_SIZE": "32",
        "WANDB_API_KEY": SecretReference(name="WANDB_KEY")
    },
    cache_config=CacheConfig(enabled=True)
)
```

### SecretReference

Used to securely reference secrets stored in your Baseten workspace.

```python  theme={"system"}
class SecretReference:
    name: str  # Name of the secret in your workspace
```

Example usage:

```python  theme={"system"}
# Reference a secret named "WANDB_API_KEY" 
secret_ref = SecretReference(name="WANDB_API_KEY")
```

### CheckpointingConfig

Configures model checkpointing behavior during training. Baseten will export the [`$BT_CHECKPOINT_DIR`](#baseten-provided-environment-variables) within
the Training Job's environment. The checkpointing storage is independent of the ephemeral stroage of the pod

```python  theme={"system"}
class CheckpointingConfig:
    enabled: bool = False              # Enable/disable checkpointing
    checkpoint_path: Optional[str] = None  # Custom checkpoint directory path
    volume_size_gib: Optional[int] = None # Custom size of your checkpointing directory
```

Example usage:

```python  theme={"system"}
# Enable checkpointing with default path
checkpointing = CheckpointingConfig(enabled=True)
```

### Baseten Provided Environment Variables

Baseten automatically provides several environment variables in your training job's environment to help integrate your code with the Baseten platform.

#### Environment Variables

| Environment Variable       | Description                                                              | Example                         |
| -------------------------- | ------------------------------------------------------------------------ | ------------------------------- |
| `BT_TRAINING_JOB_ID`       | ID of the Training Job                                                   | `"gvpql31"`                     |
| `BT_TRAINING_PROJECT_ID`   | ID of the Training Project                                               | `"aghi527"`                     |
| `BT_NUM_GPUS`              | Number of available GPUs per node                                        | `"4"`                           |
| `BT_PROJECT_CACHE_DIR`     | Directory shared across Training Jobs within a singular Training Project | `"/root/.cache/user_artifacts"` |
| `BT_TEAM_CACHE_DIR`        | Directory shared across Training Jobs within a singular Team             | `/root/.cache/team_artifacts`   |
| `BT_CHECKPOINT_DIR`        | Directory where checkpoints are automatically saved during training      | `"/mnt/ckpts"`                  |
| `BT_LOAD_CHECKPOINT_DIR`   | Directory of where loaded checkpoints will be                            | `"/tmp/loaded_checkpoints"`     |
| `BT_TRAINING_JOB_NAME`     | Name your the Training Job                                               | `"gpt-oss-20b-lora"`            |
| `BT_TRAINING_PROJECT_NAME` | Name your the Training Project                                           | `"gpt-oss-finetunes"`           |

#### Multinode Environment Variables

The following environment variables are particularly useful for multinode training jobs:

| Environment Variable | Description                                 | Example      |
| -------------------- | ------------------------------------------- | ------------ |
| `BT_GROUP_SIZE`      | Number of nodes in the multinode deployment | `"2"`        |
| `BT_LEADER_ADDR`     | Address of the leader node                  | `"10.0.0.1"` |
| `BT_NODE_RANK`       | Rank of the node                            | `"0"`        |

For multinode deployments, any traditionally used port number (e.g. `29500`) will work. There is no specific port number required by Baseten.

# Deploy Checkpoints as a Model

## Deploy checkpoints CLI wizard

The easiest way to deploy your checkpoints is by using the CLI wizard:

```bash  theme={"system"}
truss train deploy_checkpoints --job-id <job id>
```

Follow the setup wizard to choose your hardware and the checkpoint you'd like to deploy. Baseten will automatically recognize checkpoints for full finetunes and LoRAs for LLMs and Whisper models. Note that FSDP checkpoints aren't supported by `deploy_checkpoints` today and must be manually configured in the truss config.

Once you've completed the wizard, Baseten will generate a truss and deploy a published model according to the specs provided.

## Deploy checkpoints via static configuration

If you'd like to keep a static config of your checkpoint deploy, you can create a python config file defining the configuration you'd like to reference:

```bash  theme={"system"}
truss train deploy_checkpoints <path_to_config_file>
```

## DeployCheckpointsRuntime

Configures the runtime environment for deployed checkpoints.

```python  theme={"system"}
class DeployCheckpointsRuntime:
    environment_variables: Dict[str, Union[str, SecretReference]] = {}
```

## Checkpoint

Represents metadata for a saved model checkpoint.

```python  theme={"system"}
class Checkpoint:
    training_job_id: str   # ID of the training job
    id: str               # Checkpoint ID
    name: str            # Checkpoint name 
    lora_rank: Optional[int] = None  # LoRA rank if applicable. Auto-detected if not specified.
```

## CheckpointList

Manages a collection of checkpoints and their download configuration.

```python  theme={"system"}
class CheckpointList:
    download_folder: str = "training_checkpoints"  # Local download location upon deployment
    base_model_id: Optional[str] = None           # Base model identifier. Auto-dtected if not specified.
    checkpoints: List[Checkpoint] = []            # List of checkpoints
```

## DeployCheckpointsConfig

Specifies configuration for deploying trained model checkpoints.

```python  theme={"system"}
class DeployCheckpointsConfig:
    checkpoint_details: Optional[CheckpointList] = None  # Checkpoints to deploy
    model_name: Optional[str] = None                    # Name for the deployed model
    deployment_name: Optional[str] = None               # Name for the deployment
    runtime: Optional[DeployCheckpointsRuntime] = None  # Runtime configuration
    compute: Optional[Compute] = None                   # Compute resources
```

Example usage:

```python  theme={"system"}
deploy_config = DeployCheckpointsConfig(
    model_name="fine-tuned-llm",
    deployment_name="production-llm",
    checkpoint_details=CheckpointList(
        checkpoints=[
            Checkpoint(
                training_job_id="gvpql31",
                id="checkpoint_1",
                name="checkpoint_1"
            )
        ]
    ),
    compute=Compute(
        accelerator=AcceleratorSpec(accelerator="H100", count=1)
    )
)
```


# Truss SDK Reference
Source: https://docs.baseten.co/reference/sdk/truss

Python SDK for deploying and managing models with Truss.

# Authentication

## `truss.login(api_key: str) → None`

Authenticates with Baseten using an API key.

**Parameters:**

| Name      | Type  | Description      |
| --------- | ----- | ---------------- |
| `api_key` | *str* | Baseten API Key. |

***

# Deploying a Model

## `truss.push(target_directory: str, **kwargs) → ModelDeployment`

Deploys a **Truss** model to Baseten.

**Parameters:**

| Name                                      | Type             | Description                                                                                                              |
| ----------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `target_directory`                        | *str*            | Path to the Truss directory to push.                                                                                     |
| `remote`                                  | *Optional\[str]* | Name of the remote in `.trussrc` to push to.                                                                             |
| `model_name`                              | *Optional\[str]* | Override the model name in `config.yaml`.                                                                                |
| `publish`                                 | *bool*           | Deploy as **published**. If no production deployment exists, promote it to production.                                   |
| `promote`                                 | *bool*           | Deploy as **published** and promote to production, even if a production deployment exists.                               |
| `preserve_previous_production_deployment` | *bool*           | Preserve the previous production deployment’s **autoscaling settings** (only with `promote`).                            |
| `trusted`                                 | *bool*           | Grants **access to secrets** on the remote host.                                                                         |
| `deployment_name`                         | *Optional\[str]* | Custom deployment name (must contain only alphanumeric, `.`, `-`, or `_` characters). (Requires `publish` or `promote`.) |

**Returns:** [ModelDeployment](#class-truss-api-definitions-modeldeployment) – An object representing the deployed model.

***

# Model Deployment Object

## *class* `truss.api.definitions.ModelDeployment`

Represents a deployed model (returned by `truss.push()`).

**Attributes**

`model_id` → `str` – Unique ID of the deployed model.
`model_deployment_id` → `str` – Unique ID of the model deployment.

**Methods**

`wait_for_active()` → bool
Waits for the deployment to become **active**.

**Returns**: `True` when deployment is ready.
**Raises**: An error if deployment fails.


# Create training project
Source: https://docs.baseten.co/reference/training-api/create-training-project

post /v1/training_projects
Upserts a training project with the specified metadata.



# Download training job source code
Source: https://docs.baseten.co/reference/training-api/download-training-job

get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/download
Get the uploaded training job as a S3 Artifact



# Get training job
Source: https://docs.baseten.co/reference/training-api/get-training-job

get /v1/training_projects/{training_project_id}/jobs/{training_job_id}
Get the details of an existing training job.



# Get training job checkpoint files
Source: https://docs.baseten.co/reference/training-api/get-training-job-checkpoint-files

get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoint_files
Get presigned URLs for all checkpoint files for a training job.



# List training job checkpoints
Source: https://docs.baseten.co/reference/training-api/get-training-job-checkpoints

get /v1/training_projects/{training_project_id}/jobs/{training_job_id}/checkpoints
Get the checkpoints for a training job.



# Get training job logs
Source: https://docs.baseten.co/reference/training-api/get-training-job-logs

post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/logs
Get the logs for a training job with the provided filters.



# Get training job metrics
Source: https://docs.baseten.co/reference/training-api/get-training-job-metrics

post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/metrics
Get the metrics for a training job.



# List training projects
Source: https://docs.baseten.co/reference/training-api/get-training-projects

get /v1/training_projects
List all training projects for the organization.



# Overview
Source: https://docs.baseten.co/reference/training-api/overview

The Training API enables programmatic management of Baseten Training resources.

The Training API allows you to manage training projects, jobs, and related resources through a RESTful interface. This API is used to:

* Monitor training job metrics and logs
* Manage training jobs
* Manage checkpoints and artifacts

## Authentication

All Training API requests require authentication using an API key:

```bash  theme={"system"}
Authorization: Api-Key YOUR_API_KEY
```

## Base URL

All Training API endpoints are relative to:

```
https://api.baseten.co/v1
```

## Available Endpoints

### Training Projects

| Method | Endpoint                                                                | Description                   |
| ------ | ----------------------------------------------------------------------- | ----------------------------- |
| `GET`  | [`/training_projects`](/reference/training-api/get-training-projects)   | List all training projects    |
| `POST` | [`/training_projects`](/reference/training-api/create-training-project) | Create a new training project |

### Training Jobs

**Note: Creating Training Jobs via REST API is not supported at this time.**

The following endpoints have the relative base path: `/training_projects/{training_project_id}/jobs`

| Method | Endpoint                                                                                              | Description                       |
| ------ | ----------------------------------------------------------------------------------------------------- | --------------------------------- |
| `GET`  | [`.../`](/reference/training-api/list-training-jobs)                                                  | List all jobs in a project        |
| `GET`  | [`.../{training_job_id}`](/reference/training-api/get-training-job)                                   | Get a specific training job       |
| `POST` | [`.../{training_job_id}/stop`](/reference/training-api/stop-training-job)                             | Stop a training job               |
| `POST` | [`.../{training_job_id}/recreate`](/reference/training-api/recreate-training-job)                     | Recreate a training job           |
| `POST` | [`.../{training_job_id}/logs`](/reference/training-api/get-training-job-logs)                         | Get training job logs             |
| `POST` | [`.../{training_job_id}/metrics`](/reference/training-api/get-training-job-metrics)                   | Get training job metrics          |
| `GET`  | [`.../{training_job_id}/checkpoints`](/reference/training-api/get-training-job-checkpoints)           | List job checkpoints              |
| `GET`  | [`.../{training_job_id}/checkpoint_files`](/reference/training-api/get-training-job-checkpoint-files) | Get training job checkpoint files |
| `GET`  | [`.../{training_job_id}/download`](/reference/training-api/download-training-job)                     | Download training job artifacts   |

Search endpoint:

| Method | Endpoint                                                                | Description                     |
| ------ | ----------------------------------------------------------------------- | ------------------------------- |
| `POST` | [`/training_jobs/search`](/reference/training-api/search-training-jobs) | Search across all training jobs |


# Recreate training job
Source: https://docs.baseten.co/reference/training-api/recreate-training-job

post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/recreate
Create a new training job with the same configuration as an existing training job.



# Search training jobs
Source: https://docs.baseten.co/reference/training-api/search-training-jobs

post /v1/training_jobs/search
Search training jobs for the organization.



# Stop training job
Source: https://docs.baseten.co/reference/training-api/stop-training-job

post /v1/training_projects/{training_project_id}/jobs/{training_job_id}/stop
Stops a training job.



# Configure Truss
Source: https://docs.baseten.co/reference/truss-configuration

Set your model resources, dependencies, and more

Truss is configurable to its core. Every Truss must include a file config.yaml in its root directory, which is automatically generated when the Truss is created. However, configuration is optional. Every configurable value has a sensible default, and a completely empty config file is valid.

<Accordion title="YAML syntax help">
  YAML syntax can be a bit non-obvious when dealing with empty lists and dictionaries. You may notice the following in the default Truss config file:

  ```yaml  theme={"system"}
  requirements: []
  secrets: {}
  ```

  When you fill them in with values, lists and dictionaries should look like this:

  ```yaml  theme={"system"}
  requirements:
    - dep1
    - dep2
  secrets:
    key1: default_value1
    key2: default_value2
  ```
</Accordion>

## Example

Here's an example config file for a Truss that uses the [WizardLM](https://huggingface.co/WizardLM/WizardLM-7B-V1.0) model:

```yaml WizardLM config theme={"system"}
description: An instruction-following LLM Using Evol-Instruct.
environment_variables: {}
model_name: WizardLM
requirements:
  - accelerate==0.20.3
  - bitsandbytes==0.39.1
  - peft==0.3.0
  - protobuf==4.23.3
  - sentencepiece==0.1.99
  - torch==2.0.1
  - transformers==4.30.2
resources:
  cpu: "4"
  memory: 16Gi
  use_gpu: true
  accelerator: L4
secrets: {}
system_packages: []
```

## Full config reference

<Snippet file="config-params.mdx" />


# Baseten platform status
Source: https://docs.baseten.co/status/status

Current operational status of Baseten's services.

This page automatically refreshes with real-time data from our status monitoring system.

<div id="status-cards">
  <div className="status-banner">
    <div className="banner-icon">
      <Icon icon="circle-check" iconType="solid" />
    </div>

    <div className="banner-text">All systems are operational.</div>
  </div>

  <CardGroup cols={3}>
    <Card title="Model Inference" icon="circle-check" iconType="solid" href="https://status.baseten.co/">
      <div className="status-indicator">Normal</div>
    </Card>

    <Card title="Management API" icon="circle-check" iconType="solid" href="https://status.baseten.co/">
      <div className="status-indicator">Normal</div>
    </Card>

    <Card title="Web Application" icon="circle-check" iconType="solid" href="https://status.baseten.co/">
      <div className="status-indicator">Normal</div>
    </Card>
  </CardGroup>
</div>

<div style={{textAlign: "right", fontSize: "0.8rem", color: "#666", marginTop: "1rem", marginBottom: "2rem"}}>
  <span id="last-refreshed">Last updated: Loading...</span>
</div>


# Basics
Source: https://docs.baseten.co/training/concepts/basics

Learn how to get up and running on Baseten Training

This page covers the essential building blocks of Baseten Training. These are the core concepts you'll need to understand to effectively organize and execute your training workflows.

## How Baseten Training Works

Baseten Training jobs can be launched from any terminal. Training jobs are created from within a directory, and when created, that directory is packaged up and can be pushed up to Baseten.

This allows you to define your Baseten training config, scripts, code, and any other dependencies within the folder.

Within the folder, we require you to include a Baseten training config file, e.g. `config.py`. The `config.py` includes a list of `run_commands`, which can be anything from running a Python file (`python train.py`) to a bash script (e.g. `chmod +x run.sh && ./run.sh`).

<Tip>
  If you're looking to upload more than 1GB of files, we strongly suggest uploading your data to an object store and including a download command before running your training code. To avoid duplicate downloads, check out our documentation on the [cache](/training/concepts/cache).
</Tip>

## Setting Up Your Workspace

If you'd like to start from one of our existing recipies, you can check out one of the following examples:

**Simple CPU job with raw PyTorch:**

```bash  theme={"system"}
truss train init --examples mnist-pytorch
```

**More complex example that trains GPT-OSS-20b:**

```bash  theme={"system"}
truss train init --examples oss-gpt-20b-axolotl
```

Your `config.py` contains all infrastructure configuration for your job, which we will cover below.

Your `run.sh` is invoked by the command that runs when the job first begins. Here you can install any Python dependencies not already included in your Docker image, and begin the execution of your code either by calling a Python file with your training code or a launch command.

## Organizing Your Work with `TrainingProject`s

A `TrainingProject` is a lightweight organization tool to help you group different `TrainingJob`s together.

While there a few technical details to consider, your team can use `TrainingProject`s to facilitate collaboration and organization.

## Running a `TrainingJob`

Once you have a `TrainingProject`, the actual work of training a model happens within a **`TrainingJob`**. Each `TrainingJob` represents a single, complete execution of your training script with a specific configuration.

* **What it is:** A `TrainingJob` is the fundamental unit of execution. It bundles together:
  * Your training code.
  * A base `image`.
  * The `compute` resources needed to run the job.
  * The `runtime` configurations like startup commands and environment variables.
* **Why use it:** Each job is a self-contained, reproducible experiment. If you want to try training your model with a different learning rate, more GPUs, or a slightly modified script, you can create new `TrainingJob`s while knowing that previous ones have been persisted on Baseten.
* **Lifecycle:** A job goes through various stages, from being created (`TRAINING_JOB_CREATED`), to resources being set up (`TRAINING_JOB_DEPLOYING`), to actively running your script (`TRAINING_JOB_RUNNING`), and finally to a terminal state like `TRAINING_JOB_COMPLETED`. More details on the job lifecycle can be found on the [Lifecycle](/training/lifecycle) page.

## Compute Resources

The `Compute` configuration defines the computational resources your training job will use. This includes:

* **GPU specifications** - Choose from various GPU types based on your model's requirements
* **CPU and memory** - Configure the amount of CPU and RAM allocated to your job
* **Node count** - For single-node or multi-node training setups

## Base Images

Baseten provides pre-configured base images that include common ML frameworks and dependencies. These images are optimized for training workloads and include:

* Popular ML frameworks (PyTorch, VERL, Megatron, Axolotl, etc.)
* GPU drivers and CUDA support
* Common data science libraries

You can also use [custom or private images](/development/model/private-registries) if you have specific requirements.

## Securely Integrate with External Services with `SecretReference`

Successfully training a model often requires many tools and services. Baseten provides **`SecretReference`** for secure handling of secrets.

* **How to use it:** Store your secret (e.g., an API key for Weights & Biases) in your Baseten workspace with a specific name. In your job's configuration (e.g., environment variables), you refer to this secret by its name using `SecretReference`. The actual secret value is never exposed in your code.
* **How it works:** Baseten injects the secret value at runtime under the environment variable name that you specify.

```python  theme={"system"}
from truss_train import definitions

runtime = definitions.Runtime(
    # ... other runtime options
    environment_variables={
        "HF_TOKEN": definitions.SecretReference(name="hf_access_token"),
    },
)
```

## Running Inference on Trained Models

The journey from training to a usable model in Baseten typically follows this path:

1. A `TrainingJob` with checkpointing enabled, produces one or more model artifacts.
2. You run `truss train deploy_checkpoint` to deploy a model from your most recent training job. You can read more about this at [Serving Trained Models](/training/deployment).
3. Once deployed, your model will be available for inference via API. See more at [Calling Your Model](/inference/calling-your-model).

## Next Steps: Advanced Topics

Now that you understand the basics of Baseten Training, explore these advanced topics to optimize your training workflows:

* **[Cache](/training/concepts/cache)** - Speed up your training iterations by persisting data between jobs and avoiding expensive downloads
* **[Checkpointing](/training/concepts/checkpointing)** - Manage model checkpoints seamlessly and avoid disk errors during training
* **[Multinode Training](/training/concepts/multinode)** - Scale your training across multiple nodes with high-speed infiniband networking


# Cache
Source: https://docs.baseten.co/training/concepts/cache

Learn how to use the training cache to speed up your training iterations by persisting data between jobs.

The training cache enables you to persist data between training jobs. This can significantly improve iteration speed by skipping expensive downloads and data transformations.

## How to Use the Training Cache

Set the cache configuration in your `Runtime`:

```python  theme={"system"}
from truss_train import definitions

training_runtime = definitions.Runtime(
    # ... other configuration options
    cache_config=definitions.CacheConfig(enabled=True)
)
```

## Cache Directory

By default, the cache will be mounted in two locations

* `/root/.cache/user_artifacts`, which can be accessed via the [`$BT_PROJECT_CACHE_DIR`](/reference/sdk/training#baseten-provided-environment-variables) environment variable. This cache is shared by all jobs in a project.
* `/root/.cache/team_artifacts`, which can be accessed via the [`$BT_TEAM_CACHE_DIR`](/reference/sdk/training#baseten-provided-environment-variables) environment variable. This cache is shared by all jobs for a team.

## Hugging Face Cache Mount

You can mount your cache to the Hugging Face cache directory by setting `HF_HOME` to one of the provided mount points plus `/huggingface`. For example, you can set `HF_HOME=$BT_PROJECT_CACHE_DIR/huggingface` to use the project cache directory.

However, there are considerable technical pitfalls when trying to read from the cache with multiple processes, as Huggingface doesn't work well with distributed filesystems. To help enable this use case, ensure your dataset processors or process count is set to 1 to minimize the number of concurrent readers.

## Seeding Your Data and Models

For multi-gpu training, you should ensure that your data is seeded before running multi-process training jobs. You can do this by separating out a data loading script and a training script.
For a 400 GB HF Dataset, you can expect to save *nearly an hour* of compute time for each job - data download and preparation have been done already!

## Cache Management

You can inspect the contents of the cache through CLI with `truss train cache summarize <project_name or project_id>`. This visibility into what's in the cache can help you verify your code is working as expected, and additionally manage files and artifacts you no longer need.


# Checkpointing
Source: https://docs.baseten.co/training/concepts/checkpointing

Learn how to use Baseten's checkpointing feature to manage model checkpoints and avoid disk errors during training.

With checkpointing enabled, you can manage your model checkpoints seamlessly and avoid common training issues.

## Benefits of Checkpointing

* **Avoid catastrophic out of disk errors**: We mount additional storage at the checkpointing directory to help avoid out of disk errors during your training run.
* **Maximize GPU utilization**: When checkpointing is enabled, any data written to the checkpointing directory will be uploaded to the cloud by a separate process, allowing you to maximize GPU time spent training.
* **Seamless checkpoint management**: Checkpoints are automatically uploaded to cloud storage for easy access and management.

## Enabling Checkpointing

To enable checkpointing, add a `CheckpointingConfig` to the `Runtime` and set `enabled` to `True`:

```python  theme={"system"}
from truss_train import definitions

training_runtime = definitions.Runtime(
    # ... other configuration options
    checkpointing_config=definitions.CheckpointingConfig(enabled=True)
)
```

## Using the Checkpoint Directory

Baseten will automatically export the [`$BT_CHECKPOINT_DIR`](/reference/sdk/training#baseten-provided-environment-variables) environment variable in your job's environment.

<Danger>
  **Write your checkpoints to the `$BT_CHECKPOINT_DIR` directory so Baseten can automatically backup and preserve them.**
</Danger>

## Serving Checkpoints

Once your training is complete, you can serve your model checkpoints using Baseten's serving infrastructure. Learn more about [serving checkpoints](/training/deployment).


# Multinode Training
Source: https://docs.baseten.co/training/concepts/multinode

Learn how to configure and run multinode training jobs with Baseten Training.

Baseten Training supports multinode training via infiniband for distributed training across multiple nodes.

## Configuring Multinode Training

To deploy a multinode training job:

* Configure the `Compute` resource in your `TrainingJob` by setting the `node_count` to the number of nodes you'd like to use (e.g. 2).

```python  theme={"system"}
from truss_train import definitions

compute = definitions.Compute(
    node_count=2,  # Use 2 nodes for multinode training
    # ... other compute configuration options
)
```

## Environment Variables

Make sure you've properly integrated with the [Baseten provided environment variables](/reference/sdk/training#baseten-provided-environment-variables) for distributed training.

## Network Configuration

Baseten provides high-speed infiniband networking between nodes to ensure efficient communication during distributed training. This enables:

* Fast gradient synchronization
* Efficient parameter updates
* Low-latency communication between nodes

## Checkpointing in Multinode Training

Checkpointing behavior varies across training frameworks in multinode setups. One common pattern is to use the shared cache directory that all nodes can access:

```bash  theme={"system"}
# Use shared volume with job name for checkpointing
ckpt_dir="${BT_PROJECT_CACHE_DIR}/${BT_TRAINING_JOB_NAME}"
```

Then ensure you write to `ckpt_dir`. This ensures all nodes write to the same checkpoint location. For comprehensive framework-specific examples and patterns, see the [Training Cookbook](https://github.com/basetenlabs/ml-cookbook).
Keep in mind that these checkpoints will not be backed up by Baseten since they are not stored in \$BT\_CHECKPOINT\_DIR. Make sure to copy them there at some point to ensure they are preserved.

## Common Practices

When setting up multinode training:

1. **Data Loading**: Ensure your data loading is properly distributed across nodes
2. **Seeding**: Use consistent seeding across all nodes for reproducible results
3. **Monitoring**: Monitor training metrics across all nodes to ensure balanced training


# Serving Your Trained Model
Source: https://docs.baseten.co/training/deployment

How to deploy checkpoints from Baseten Training jobs as usable models.

Baseten Training seamlessly integrates with Baseten's model deployment capabilities. Once your `TrainingJob` has produced model checkpoints, you can deploy them as fully operational model endpoints.

**This feature works with HuggingFace compatible LLMs**, allowing you to easily deploy fine-tuned language models directly from your training checkpoints with a single command.

To leverage deploying checkpoints, first ensure you have a `TrainingJob` that's running with a `checkpointing_config` enabled.

```python  theme={"system"}
runtime = definitions.Runtime(
    start_commands=[
        "/bin/sh -c './run.sh'",
    ],
    checkpointing_config=definitions.CheckpointingConfig(
        enabled=True,
    ),
)
```

In your training code or configuration, ensure that your checkpoints are being written to the checkpointing directory, which can be referenced in via [`$BT_CHECKPOINT_DIR`](/reference/sdk/training#baseten-provided-environment-variables).
The contents of this directory are uploaded to Baseten's storage and made immediately available for deployment.
*(You can optionally specify a `checkpoint_path` in your `checkpointing_config` if you prefer to write to a specific directory).* The default location is "/tmp/training\_checkpoints".

To deploy your checkpoint(s) as a `Deployment`, you can:

### CLI Deployment

```bash  theme={"system"}
truss train deploy_checkpoints [OPTIONS]
```

**Options:**

* `--job-id` (TEXT): Job ID to deploy checkpoints from. If not specified, deploys from the most recent training job.

This will deploy the most recent checkpoint from your training job as an inference endpoint.

### UI Deployment

You can also deploy checkpoints directly from the Baseten UI by pressing the dropdown menu on your completed training job and selecting "Deploy" on your selected checkpoint.

### Advanced CLI Deployment

You can also:

* run `truss train deploy_checkpoints [--job-id <job_id>]` and follow the setup wizard.
* define an instance of a `DeployCheckpointsConfig` class (this is helpful for small changes that aren't provided by the wizard) and run `truss train deploy_checkpoints --config <path_to_config_file>`.

<Note>
  Currently, the `deploy_checkpoints` command only supports LoRA and Full Fine Tune for Single Node LLM Training jobs.
</Note>

When `deploy_checkpoints` is run, `truss` will construct a deployment `config.yml` and store it on disk in a temporary directory. If you'd like to preserve or modify the resulting deployment config, you can copy paste it
into a permanent directory and customize it as needed.

This file defines the source of truth for the deployment and can be deployed independently via `truss push`. See [deployments](../deployment/deployments) for more details.

After successful deployment, your model will be deployed on Baseten, where you can run inference requests and evaluate performance. See [Calling Your Model](/inference/calling-your-model) for more details.

To download the files you saved to the checkpointing directory or understand the file structure, you can run `truss train get_checkpoint_urls [--job-id=<job_id>]` to get a JSON file containing presigned URLs for each training job.

The JSON file contains the following structure:

```json  theme={"system"}
{
  "timestamp": "2025-06-23T13:44:16.485905+00:00",
  "job": {
    "id": "03yv1l3",
    "created_at": "2025-06-18T14:30:30.480Z",
    "current_status": "TRAINING_JOB_COMPLETED",
    "error_message": null,
    "instance_type": {
			"id": "H100:2x8x176x968",
			"name": "H100:2x8x176x968 - 2 Nodes of 8 H100 GPUs, 640 GiB VRAM, 176 vCPUs, 968 GiB RAM",
			"memory_limit_mib": 967512,
			"millicpu_limit": 176000,
			"gpu_count": 8,
			"gpu_type": "H100",
			"gpu_memory_limit_mib": 655360
		},
    "updated_at": "2025-06-18T14:30:30.510Z",
    "training_project_id": "lqz9o34",
    "training_project": {
      "id": "lqz9o34",
      "name": "checkpointing"
    }
  },
  "checkpoint_artifacts": [
    {
      "url": "https://bt-training-eqwnwwp-f815d6cd-19bf-4589-bfcb-da76cd8432c0.s3.amazonaws.com/training_projects/lqz9o34/jobs/03yv1l3/rank-0/checkpoint-24/tokenizer_config.json?AWSAccessKeyId=AKIARLZO4BEQO4Q2A5NH&Signature=0vdzJf0686wNE1d9bm4%2Bw9ik5lY%3D&Expires=1751291056",
      "relative_file_name": "checkpoint-24/tokenizer_config.json",
      "node_rank": 0
    }
    ...
  ]
}
```

**Important notes about the presigned URLs:**

* The presigned URLs expire after **7 days** from generation
* These URLs are primarily intended for **evaluation and testing purposes**, not for long-term inference deployments
* For production deployments, consider copying the checkpoint files to your Truss model directory and downloading them in the model's `load()` function

## Complex and Custom Use Cases

* Custom Model Architectures
* Weights Sharded Across Nodes (Contact Baseten for help implementating this)

Examine the structure of your files with `truss train get_checkpoint_urls --job-id=<your-training-job-id>`. If a file looks like this:

```json  theme={"system"}
{
  "url": "https://bt-training-eqwnwwp-f815d6cd-19bf-4589-bfcb-da76cd8432c0.s3.amazonaws.com/training_projects/lqz9o34/jobs/03yv1l3/rank-4/checkpoint-10/weights.safetensors?AWSAccessKeyId=AKIARLZO4BEQO4Q2A5NH&Signature=0vdzJf0686wNE1d9bm4%2Bw9ik5lY%3D&Expires=1751291056",
  "relative_file_name": "checkpoint-10/weights.safetensors",
  "node_rank": 4
}
```

In your Truss configuration, add a section like this: Wilcards `*` match to to an arbitrary number of chars while `?` matches to one.

```yaml  theme={"system"}
training_checkpoints:
  download_folder: /tmp/training_checkpoints
  artifact_references:
    - training_job_id: <your-training-job-id>
      paths:
        - rank-*/checkpoint-10/ # Pull in all the files for checkpoint-10 across all nodes
```

When your model pod starts up, you can read the file from the path `/tmp/training_checkpoints/rank-[node-rank]/[relative_file_name]`. For the example above, the file can be read from:

```
/tmp/training_checkpoints/<your-training-job-id>/rank-4/checkpoint-10/weights.safetensors
```


# Getting started
Source: https://docs.baseten.co/training/getting-started

Your first steps to creating and running training jobs on Baseten.

This guide will walk you through the initial setup and the process of submitting
your first `TrainingJob` using Baseten Training. In this demo, we'll create a finetuned revision
of OpenAI's `gpt-oss-20b`!

## Prerequisites

Before you begin, ensure you have the following:

1. **Baseten Account:** You'll need an active Baseten account. If you don't
   have one, please sign up on the [Baseten web app](https://app.baseten.co/).
2. **API Key:** Obtain an API key for your [Baseten account](https://app.baseten.co/settings/api_keys).
   This key is
   required to authenticate with the Baseten API and SDK.
3. **Truss SDK and CLI:** The `truss` package provides a python-native way for defining and running your training jobs.
   jobs. The CLI provides a convenient way to deploy and manage your training jobs. Install or update it:
   ```bash  theme={"system"}
   pip install -U truss 
   ```
4. **Dependencies**: In this demo, we'll use Huggingface to access and upload models. It's recommended that
   you create a [Huggingface access token](https://huggingface.co/docs/hub/en/security-tokens) and add it
   to your [Baseten Secrets](https://app.baseten.co/settings/secrets). Additionally, it can be
   helpful to visualize your training run. In this example, we use [Weights & Biases (wandb)](https://wandb.ai/site/). This is optional.

## Step 1: Define your training configuration

### Optional: Initialize configuration with [truss train init](https://docs.baseten.co/reference/cli/training/training-cli#training-cli-reference)

To download everything described in this step, run

```sh  theme={"system"}
truss train init --examples oss-gpt-20b-axolotl
cd oss-gpt-20b-axolotl
```

Now you can skip over to [Step 2](https://docs.baseten.co/training/getting-started#step-2%3A-submit-your-training-job) to launch your training job.

### Training configuration details

The primary way to define your training jobs is through a Python configuration
file, typically named `config.py`. This file uses the `truss` package to specify all
aspects of your `TrainingProject` and `TrainingJob`.

A simple example of a `config.py` file is shown below:

```python config.py theme={"system"}
# Import necessary classes from the Baseten Training SDK
from truss_train import definitions
from truss.base import truss_config

# 1. Define a base image for your training job. You can also use
# private images via AWS IAM or GCP Service Account authentication.
BASE_IMAGE = "pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime"

# 2. Define the Runtime Environment for the Training Job
# This includes start commands and environment variables.
# Secrets from the baseten workspace like API keys are referenced using 
# `SecretReference`.
training_runtime = definitions.Runtime(
    start_commands = [
        "chmod +x ./run.sh && ./run.sh",
    ],
    environment_variables={
        "HF_TOKEN": definitions.SecretReference(name="hf_access_token"), # The name of the HF Access Token secret in your B10 account
        # Uncomment to export your wandb api key.
        # "WANDB_API_KEY" : definitions.SecretReference(name="wandb_api_key"),
    },
    cache_config=definitions.CacheConfig(
        enabled=True,
    ),
    checkpointing_config=definitions.CheckpointingConfig(
        enabled=True,
    ),
)

# 3. Define the Compute Resources for the Training Job
training_compute = definitions.Compute(
    accelerator=truss_config.AcceleratorSpec(
        accelerator=truss_config.Accelerator.H100,  
        count=4,  
    ),
)

# 4. Define the Training Job
# This brings together the image, compute, and runtime configurations.
training_job = definitions.TrainingJob(
    image=definitions.Image(base_image=BASE_IMAGE),
    compute=training_compute,
    runtime=training_runtime
)


# This config will be pushed using the Truss CLI.
# The association of the job to the project happens at the time of push.
training_project = definitions.TrainingProject(
    name="LoRA Training Job - gpt-oss-20b",
    job=training_job
)
```

### Key considerations for your Baseten training configuration file

* **Local Artifacts:** If your training requires local scripts (like
  a `train.py` or a `run.sh`), helper files, or
  configuration files (e.g., accelerate config), place them in the same
  directory as your `config.py` or in subdirectories. When you push the training
  job, `truss` will package these artifacts and upload them. They will be copied
  into the container at the root of the base image's working directory.
* **Ignore Folders and Files**: You can exclude specific files from being pushed by creating a `.truss_ignore` file in root directory of your project.
  In this file, you can add entries in a style similar to `.gitignore`. Refer to the [CLI reference](/reference/cli/training/training-cli#ignoring-files-and-folders) for more details.
* **Secrets:** Ensure any secrets referenced via `SecretReference` (e.g.,
  `hf_access_token`, `wandb_api_key`) are defined in your Baseten
  [workspace settings](https://app.baseten.co/settings/secrets).
* **Private Images:** You can deploy your jobs with private images by specifying a `DockerAuth` in your `Image` configuration.
  See [our DockerAuth SDK](/reference/sdk/training#dockerauth) for more details.

For a complete guide on the `TrainingJob` type, check out our [SDK-reference](/reference/sdk/training).

### What can I run in the `start_commands`?

In short, anything! Baseten Training is a framework-agnostic training platform. Any training framework and training methodology
is supported. Typically, a `run.sh` script is used. An example might look like this:

```bash run.sh theme={"system"}
#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -eux

# Install dependencies
pip install "trl>=0.20.0" "peft>=0.17.0" "transformers>=4.55.0" 
# Uncomment to enable wandb
# pip install wandb

# Let's run! 
python3 train.py
```

To complete the example, we provide the `train.py` below.

```python  theme={"system"}
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Mxfp4Config
import torch

from trl import SFTConfig, SFTTrainer

## TODO: update your dataset here
dataset = load_dataset("HuggingFaceH4/Multilingual-Thinking", split="train")


tokenizer = AutoTokenizer.from_pretrained("openai/gpt-oss-20b")


quantization_config = Mxfp4Config(dequantize=True)
model_kwargs = dict(
    attn_implementation="eager",
    torch_dtype=torch.bfloat16,
    quantization_config=quantization_config,
    use_cache=False,
    device_map="auto",
)

model = AutoModelForCausalLM.from_pretrained("openai/gpt-oss-20b", **model_kwargs)

from peft import LoraConfig, get_peft_model

peft_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules="all-linear",
    target_parameters=[
        "7.mlp.experts.gate_up_proj",
        "7.mlp.experts.down_proj",
        "15.mlp.experts.gate_up_proj",
        "15.mlp.experts.down_proj",
        "23.mlp.experts.gate_up_proj",
        "23.mlp.experts.down_proj",
    ],
)
peft_model = get_peft_model(model, peft_config)
peft_model.print_trainable_parameters()

training_args = SFTConfig(
    learning_rate=2e-4,
    gradient_checkpointing=True,
    num_train_epochs=0.3,
    logging_steps=1,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    max_length=2048,
    warmup_ratio=0.03,
    lr_scheduler_type="cosine_with_min_lr",
    lr_scheduler_kwargs={"min_lr_rate": 0.1},
    output_dir="gpt-oss-20b-multilingual-reasoner",
    push_to_hub=False,
)

trainer = SFTTrainer(
    model=peft_model,
    args=training_args,
    train_dataset=dataset,
    processing_class=tokenizer,
)
trainer.train()

trainer.save_model(training_args.output_dir)
# Push the trained model in output_dir to a Hugging Face model repo
trainer.push_to_hub("baseten-admin/gpt-oss-20b-multilingual-reasoner")
```

### Training Different Models

This recipe and more can be found at [Baseten's ML Cookbook](https://github.com/basetenlabs/ml-cookbook). Clone the repo
to get the starter code for this demo, along with other training and finetuning examples!

### Additional features

We've kept the above config simple to help you get off the ground - but there's a lot more you can do Baseten Training:

* [Checkpointing](/training/concepts/checkpointing) - automatically save and deploy your model checkpoints.
* [Training Cache](/training/concepts/cache) - speed up training by caching data and models between jobs.
* [Multinode Training](/training/concepts/multinode) - train on multiple GPU nodes to make the most out of your compute.

## Step 2: Submit Your Training Job

Once your `config.py` and any local artifacts are ready, you submit the training
job using the `truss` [CLI](/reference/cli/training/training-cli):

```bash  theme={"system"}
truss train push config.py
```

This command does the following:

1. Parses your `config.py`.
2. Packages any local files in the directory (and subdirectories) alongside
   `config.py`.
3. Creates or updates the `TrainingProject` specified in your config.
4. Submits the defined `TrainingJob` under that project.

Upon successful submission, the CLI will print out a training job id with some helpful commands. You can also navigate to
the Baseten Web UI to view your logs and metrics: `https://app.baseten.co/training/`

## Next steps

* [Basics](/training/concepts/basics): Learn about the fundamental building blocks of Baseten Training
* [Cache](/training/concepts/cache): Speed up your training iterations with persistent caching
* [Checkpointing](/training/concepts/checkpointing): Manage model checkpoints seamlessly
* [Multinode Training](/training/concepts/multinode): Scale your training across multiple nodes
* [Management](/training/management): Learn how to check status,
  view logs and metrics, and stop jobs.


# Loading Checkpoints
Source: https://docs.baseten.co/training/loading

Resume training from existing checkpoints to continue where you left off

Checkpoint loading lets you resume training from previously saved model states. When enabled, Baseten automatically downloads your specified checkpoints to the training environment before your training code starts.

**Use cases:**

* Resume failed training jobs
* Incremental training and fine-tuning

## Accessing Downloaded Checkpoints

Checkpoints are available through the `BT_LOAD_CHECKPOINT_DIR` environment variable. For single-node training, they're located in `BT_LOAD_CHECKPOINT_DIR/rank-0/`.

<Note>
  Checkpoint restoration currently does not support loading weights that are sharded across multiple nodes.
</Note>

## Checkpoint Reference

Create references to checkpoints using the `BasetenCheckpoint` factory:

### From Latest

```python  theme={"system"}
# Load the latest checkpoint from a project 
BasetenCheckpoint.from_latest_checkpoint(project_name="my-training-project")  

# Load the latest checkpoint from a previous job  
BasetenCheckpoint.from_latest_checkpoint(job_id="gvpql31")
```

**Parameters:**

* `project_name`: Load the latest checkpoint from the most recent job in this project
* `job_id`: Load the latest checkpoint from this specific job
* Both parameters: Load the latest checkpoint from that specific job in that project

### From Named

```python  theme={"system"}
# Pin your starting point to a specific checkpoint
BasetenCheckpoint.from_named_checkpoint(checkpoint_name="checkpoint-20", job_id="gvpql31")
```

**Parameters:**

* `checkpoint_name`: The name of the specific checkpoint to load
* `job_id`: The job that contains the named checkpoint
* Both parameters: Load the named checkpoint from that specific job in that project

## Configuration Examples

Here are practical examples of how to configure checkpoint loading in your training jobs:

### From Latest

```python  theme={"system"}
# Latest checkpoint from project
load_config = LoadCheckpointConfig(
    enabled=True,
    checkpoints=[
        BasetenCheckpoint.from_latest_checkpoint(project_name="gpt-finetuning")
    ]
)

# Latest checkpoint from specific job
load_config = LoadCheckpointConfig(
    enabled=True,
    checkpoints=[
        BasetenCheckpoint.from_latest_checkpoint(job_id="gvpql31")
    ]
)
```

### From Named

```python  theme={"system"}
# Specific named checkpoint
load_config = LoadCheckpointConfig(
    enabled=True,
    checkpoints=[
        BasetenCheckpoint.from_named_checkpoint(
            checkpoint_name="checkpoint-20",
            job_id="gvpql31"
        )
    ]
)

# Named checkpoint with custom download location
load_config = LoadCheckpointConfig(
    enabled=True,
    download_folder="/tmp/my_checkpoints",
    checkpoints=[
        BasetenCheckpoint.from_named_checkpoint(
            checkpoint_name="checkpoint-20",
            job_id="rwnojdq"
        )
    ]
)
```

**Configuration parameters for :**

* `enabled`: Set to `True` to enable checkpoint loading
* `checkpoints`: List containing checkpoint references
* `download_folder`: Optional custom download location (defaults to `/tmp/loaded_checkpoints`)

## Complete TrainingJob Setup

```python  theme={"system"}
from truss_train import LoadCheckpointConfig, BasetenCheckpoint, CheckpointingConfig, TrainingJob, Image, Runtime, TrainingProject
from truss_train.definitions import CacheConfig

# Configure checkpoint loading
load_checkpoint_config = LoadCheckpointConfig(
    enabled=True,
    download_folder="/tmp/loaded_checkpoints",
    checkpoints=[
        BasetenCheckpoint.from_latest_checkpoint(job_id="previous_job_id")
    ]
)

# Configure checkpointing for saving new checkpoints
checkpointing_config = CheckpointingConfig(
    enabled=True,
    checkpoint_path="/tmp/training_checkpoints"
)

# Create TrainingJob
job = TrainingJob(
    image=Image(base_image="your-base-image"),
    runtime=Runtime(
        checkpointing_config=checkpointing_config,
        load_checkpoint_config=load_checkpoint_config,
        start_commands=["chmod +x ./run.sh && ./run.sh"],
        cache_config=CacheConfig(enabled=True)
    ),
)

project = TrainingProject(name="my-training-project", job=job)
```

## Using Checkpoints in Your Training Code

Access loaded checkpoints using the `BT_LOAD_CHECKPOINT_DIR` environment variable:

```python  theme={"system"}
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TrainingArguments, Trainer
from transformers.trainer_utils import get_last_checkpoint
import os

def train():
    checkpoint_dir = os.environ.get("BT_LOAD_CHECKPOINT_DIR")
    last_checkpoint = None

    if checkpoint_dir:
        last_checkpoint = get_last_checkpoint(checkpoint_dir)
        if last_checkpoint:
            print(f"✅ Resuming from checkpoint: {last_checkpoint}")
            model = AutoModelForSequenceClassification.from_pretrained(last_checkpoint)
            tokenizer = AutoTokenizer.from_pretrained(checkpoint_dir)
        else:
            print("⚠️ No checkpoint found, starting from scratch")
            model = AutoModelForSequenceClassification.from_pretrained("your-base-model")
            tokenizer = AutoTokenizer.from_pretrained("your-base-model")
    else:
        print("ℹ️ No checkpoint loading configured")
        model = AutoModelForSequenceClassification.from_pretrained("your-base-model")
        tokenizer = AutoTokenizer.from_pretrained("your-base-model")

    training_args = TrainingArguments(
        output_dir=os.environ.get("BT_CHECKPOINT_DIR", "/tmp/training_checkpoints"),
        save_strategy="steps",
        save_steps=1000,
        load_best_model_at_end=True,
    )

    trainer = Trainer(model=model, args=training_args)
    trainer.train(resume_from_checkpoint=last_checkpoint)
```


# Management
Source: https://docs.baseten.co/training/management

How to monitor, manage, and interact with your Baseten Training projects and jobs.

Once you have submitted training jobs, Baseten provides tools to manage your `TrainingProject`s and individual `TrainingJob`s. You can use the [CLI](/reference/cli/training/training-cli) or the [API](/reference/training-api/overview) to manage your jobs.

## `TrainingProject` management

* **Listing Projects:** To view all your training projects:
  ```bash  theme={"system"}
  truss train view
  ```
  This command will list all `TrainingProject`s you have access to, typically showing their names and IDs. Additionally, this command will show all active jobs.

* **Viewing Jobs within a Project:** To see all jobs associated with a specific project, use its `project` (obtained when creating the project or from `truss train view`):
  ```bash  theme={"system"}
  truss train view --project <project_id or project_name>
  ```

## `TrainingJob` management

After submitting a job with `truss train push config.py`, you receive a `project_id` and `job_id`.

* **Listing Jobs:** As shown above, you can list all jobs within a project using:
  ```bash  theme={"system"}
  truss train view --project <project_id or project_name>
  ```
  This will typically show job IDs, statuses, creation times, etc.

* **Checking Status and Retrieving Logs:** To view the logs for a specific job, you can tail them in real-time or fetch existing logs.
  * To view logs for the most recently submitted job in the current context (e.g., if you just pushed a job from your current terminal directory):
    ```bash  theme={"system"}
    truss train logs --tail
    ```
  * To view logs for a specific job using its `job-id`:
    ```bash  theme={"system"}
    truss train logs --job-id <your_job_id> [--tail]
    ```
    Add `--tail` to follow the logs live.

* **Understanding Job Statuses:**
  The `truss train view` and `truss train logs` commands will help you track which status a job is in. For more on the job lifecycle, see the [Lifecycle](/training/lifecycle) page.

* **Stopping a `TrainingJob`:** If you need to stop a running job, use the `stop` command with the job's project ID and job ID:
  ```bash  theme={"system"}
  truss train stop --job-id <your_job_id>
  truss train stop --all # Stops all active jobs; Will prompt the user for confirmation.
  ```
  This will transition the job to the `TRAINING_JOB_STOPPED` state.

* **Understanding Job Outputs & Checkpoints:**
  * The primary outputs of a successful `TrainingJob` are model **checkpoints** (if checkpointing is enabled and configured).
  * These checkpoints are stored by Baseten. Refer to the [Checkpointing section in Core Concepts](/training/concepts#checkpointing) for how `CheckpointingConfig` works.
  * When you are ready to [deploy a model](/training/deployment), you will specify which checkpoints to use. The `model_name` you assign during deployment (via `DeployCheckpointsConfig`) becomes the identifier for this trained model version derived from your specific job's checkpoints.
  * You can see the available checkpoints for a job via the [Training API](/reference/training-api/get-training-job-checkpoints).


# Overview
Source: https://docs.baseten.co/training/overview

An introduction on how to train and finetune models on Baseten.

Welcome to Baseten **Training**, a powerful product designed to streamline and manage the entire lifecycle of model training.

## Who it's for

Baseten Training is for MLEs, Engineers, and Developers who are looking for a fast, flexible, and scalable platform for training
and finetuning models – and getting these models into production.

## Use cases

Training on Baseten allows you to easily:

* **Optimize on cost and latency:** Train a smaller, faster, and cheaper model from a larger, more general, expensive one.
* **Develop specialized and agentic models:** Finetune a model with RL to do specific tasks, like [code completion](https://github.com/basetenlabs/ml-cookbook/tree/main/recipes/rl/ocaml_sepcialist) and tool calling.
* **Craft customized voice models:** Finetune a voice model like Orpheus to speak with specific [intonations and accents](https://github.com/basetenlabs/ml-cookbook/tree/main/examples/orpheus-transformers/training).
* **Get to prod:** Productionize trained models to scalable deployments with a click of a button.

## Why Baseten Training

### Streamline your path from training to prod

We want to make sure you're getting to impact as fast as possible. Our training platform prioritizes the end-to-end model development cycle with these key features:

* **Instantly up and running:** Check out our [getting started guide](/training/getting-started) for a step-by-step how-to and our [ml-cookbook](https://github.com/basetenlabs/ml-cookbook) for recipes and examples spanning Supervised Finetuning, Reinforcement Learning, and a variety of frameworks.
* **Flexibility:** Stay up to date with the most impactful training recipes and techniques across text, vision, and audio with our framework-agnostic training API.
* **Seamless Deploys:** Transition from training to inference and evals seamlessly within the Baseten ecosystem.

### Seamlessly scale your experimentation

We know training and finetuning are experimental in nature. Our platform provides the infrastructure you need to scale out and scale up:

* **Reproducibility:** Ensure consistent training runs by precisely defining your environment, code, and configurations.
* **Scalability:** Easily scale your training jobs from single-gpu, to multi-gpu, and even to multi-node distributed training. Handle large datasets, large sequence lengths, and complex models  - all without any commits.
* **Simplified Management:** Organize, monitor, and manage your training projects and jobs in a centralized platform.
* **Artifact Management:** Expedite handling of large artifacts like models, checkpoints, and datasets efficiently with Baseten storage.

## Get Started

Check out our [Getting Started](/training/getting-started) guide to get started with training on Baseten.

## Go deeper

Use the following resources to learn more about training on Baseten:

* [CLI Reference](/reference/cli/training/training-cli)
* [SDK Reference](/reference/sdk/training)
* [API Reference](/reference/training-api/overview)


# Deployments
Source: https://docs.baseten.co/troubleshooting/deployments

Troubleshoot common problems during model deployment

## Issue: `truss push` can't find `config.yaml`

```sh  theme={"system"}
[Errno 2] No such file or directory: '/Users/philipkiely/Code/demo_docs/config.yaml'
```

### Fix: set correct target directory

The directory `truss push` is looking at is not a Truss. Make sure you're giving `truss push` access to the correct directory by:

* Running `truss push` from the directory containing the Truss. You should see the file `config.yaml` when you run `ls` in your working directory.
* Or passing the target directory as an argument, such as `truss push /path/to/my-truss`.

## Issue: unexpected failure during model build

During the model build step, there can be unexpected failures from temporary circumstances. An example is a network error while downloading model weights from Hugging Face or installing a Python package from PyPi.

### Fix: restart deploy from Baseten UI

First, check your model logs to determine the exact cause of the error. If it's an error during model download, package installation, or similar, you can try restarting the deploy from the model dashboard in your workspace.


# Inference
Source: https://docs.baseten.co/troubleshooting/inference

Troubleshoot common problems during model inference

## Model I/O issues

### Error: JSONDecodeError

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

This error means you're attempting to pass a model input that is not JSON-serializable. For example, you might have left out the double quotes required for a valid string:

```sh  theme={"system"}
truss predict -d 'This is not a string' # Wrong
truss predict -d '"This is a string"'   # Correct
```

## Model version issues

### Error: No OracleVersion matches the given query

```
<Server response: {
    'errors': [{
        'message': 'No OracleVersion matches the given query.',
        'locations': [{'line': 3, 'column': 13}],
        'path': ['model_version']
    }],
    'data': {'model_version': None}
}>
```

Make sure that the model ID or deployment ID you're passing is correct and that the associated model has not been deleted.

Additionally, make sure you're using the correct endpoint:

* [Production environment endpoint](/reference/inference-api/predict-endpoints/environments-predict).
* [Development deployment endpoint](/reference/inference-api/predict-endpoints/development-predict).
* [Deployment endpoint](/reference/inference-api/predict-endpoints/deployment-predict).

## Authentication issues

### Error: Service provider not found

```
ValueError: Service provider example-service-provider not found in ~/.trussrc
```

This error means your `~/.trussrc` is incomplete or incorrect. It should be formatted as follows:

```
[baseten]
remote_provider = baseten
api_key = YOUR.API_KEY
remote_url = https://app.baseten.co
```

### Error: You have to log in to perform the request

```
<Server response: {
    'errors': [{
        'message': 'You have to log in to perform the request',
        'locations': [{'line': 3, 'column': 13}],
        'path': ['model_version'],
        'extensions': {'code': 'UNAUTHENTICATED_ACCESS'}
    }],
    'data': {'model_version': None}
}>
```

This error occurs on `truss predict` when the API key in `~/.trussrc` for a given host is missing or incorrect. To fix it, update your API key in the `~/.trussrc` file.

### Error: Please check the API key you provided

```
{
        "error": "please check the api-key you provided"
}
```

This error occurs when using `curl` or similar to call the model via its API endpoint when the API key passed in the request header is not valid. Make sure you're using a valid API key then try again.


