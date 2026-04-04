# Source: https://docs.verda.com/containers/overview.md

# Overview

With our Containers service, you can create your own inference endpoints to serve your models while paying only for the compute that is in active use.

We support loading containers from any registry and are [quite flexible](https://github.com/DataCrunch-io/container-examples) about how the container is built.

You can deploy your first container by following the guide: [deploy-with-vllm-quick](https://docs.verda.com/containers/tutorials/deploy-with-vllm-quick "mention")

## Serverless Containers pricing

Price is calculated in 10-minute intervals for the currently running replicas of your container. The number of currently running replicas will depend on your [scaling](https://docs.verda.com/containers/scaling "mention") settings.

[See here for pricing](https://datacrunch.io/serverless-containers).

### Features

* Scale to hundreds of GPUs when needed with our battle-tested inference cluster
* Scale to zero when idle, so you only pay while your container is running
* Support for any container registry, using either registry-specific authentication methods or a vanilla Docker `config.json`-style auth
* Both manual and request queue-based autoscaling, with adjustable scaling sensitivity
* Logging and metrics in the console
* [RESTful API](https://api.datacrunch.io/v1/docs#tag/serverless-containers) for managing your deployments
* [Python SDK](https://datacrunch-python.readthedocs.io/en/latest/examples/containers/)
* Support for [async / polling requests](https://docs.verda.com/containers/synchronous-and-asynchronous-inference)
* Shared storage between the Containers and Cloud GPU instances
* Batch jobs - recommended for long inference durations > 3min

### Coming soon

* Container Registry
