# Source: https://docs.baseten.co/concepts/howbasetenworks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# How Baseten works

> Baseten is a platform for building, serving, and scaling AI models in production.

It supports multiple entry points depending on your workflow—whether you're deploying a dedicated model, calling an open-source LLM via our Model API, or training from scratch.

**At the core is the Baseten Inference Stack:** performant model engines on top of Inference optimized infrastructure. Instead of managing infrastructure, scaling policies, and performance optimization, you can focus on building and iterating on your AI-powered applications.

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

This full-stack infrastructure, from packaging to observability, is powered by the **Baseten Inference Stack**: performant model engines, cross-cloud availability, and seamless developer workflows.

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
