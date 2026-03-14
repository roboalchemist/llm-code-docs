# Source: https://docs.together.ai/docs/dedicated-container-inference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Deploy custom containers on Together's managed GPU infrastructure with automatic scaling, job queues, and built-in observability.

Dedicated Containers let you run your own Dockerized inference workloads on Together's managed GPU infrastructure. You bring the container — Together handles compute provisioning, autoscaling, networking, and observability.

You build and push a Docker image using the [Jig CLI](/docs/deployments-jig). Inside your container, the [Sprocket SDK](/docs/deployments-sprocket) connects your inference code to Together's managed [job queue](/docs/deployments-queue). Once deployed, your workers can receive requests.

* Wrap and deploy your model in 20 minutes
* Boost conversion and margins with fair priority queueing
* Bottomless capacity just before you need it

<Frame>
  <img src="https://mintcdn.com/togetherai-52386018/guu83tcrNiDPEySM/images/dedicatedcontainers.svg?fit=max&auto=format&n=guu83tcrNiDPEySM&q=85&s=1697805b576af1b144ac6f280e829ecc" alt="Dedicated Containers Architecture" width="2357" height="1168" data-path="images/dedicatedcontainers.svg" />
</Frame>

***

## Quickstart

<Card title="Deploy Your First Container" icon="rocket" href="/docs/containers-quickstart">
  Deploy your first container from the command line
</Card>

## Concepts

<Card title="Platform Overview" icon="sitemap" href="/docs/together-deployments">
  Architecture, deployment lifecycle, autoscaling, and troubleshooting
</Card>

<CardGroup cols={3}>
  <Card title="Jig CLI" icon="hammer" href="/docs/deployments-jig">
    Build, deploy, secrets, and volumes
  </Card>

  <Card title="Sprocket SDK" icon="code" href="/docs/deployments-sprocket">
    Inference workers with setup() and predict()
  </Card>

  <Card title="Queue API" icon="layer-group" href="/docs/deployments-queue">
    Async jobs with priority and progress
  </Card>
</CardGroup>

## Guides

<CardGroup cols={2}>
  <Card title="Image Generation" icon="image" href="/docs/dedicated_containers_image">
    Single-GPU Flux2 model
  </Card>

  <Card title="Video Generation" icon="video" href="/docs/dedicated_containers_video">
    Multi-GPU Wan 2.1 with torchrun
  </Card>
</CardGroup>

## Reference

<CardGroup cols={3}>
  <Card title="Jig CLI" icon="terminal" href="/reference/dci-reference-jig">
    CLI commands and pyproject.toml configuration
  </Card>

  <Card title="Sprocket SDK" icon="code" href="/reference/dci-reference-sprocket">
    Base classes, file handling, and error reference
  </Card>

  <Card title="REST API" icon="book" href="/reference/deployments-list">
    Deployments, secrets, storage, and queue
  </Card>
</CardGroup>

***

<Card title="Get Access" icon="envelope" href="mailto:support@together.ai">
  Contact your account representative or [support@together.ai](mailto:support@together.ai) to enable Dedicated Containers for your organization.
</Card>


Built with [Mintlify](https://mintlify.com).