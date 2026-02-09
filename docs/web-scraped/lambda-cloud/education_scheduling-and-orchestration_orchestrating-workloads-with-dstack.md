# Orchestrating AI workloads with dstack -

Source: https://docs.lambda.ai/education/scheduling-and-orchestration/orchestrating-workloads-with-dstack/

---

[api](../../../tags/#tag:api) [llm](../../../tags/#tag:llm)

# Orchestrating AI workloads with dstack

## Introduction

[dstack](https://dstack.ai/) is an open-source alternative to Kubernetes and Slurm, built for orchestrating containerized AI and ML workloads. It simplifies the development, training, and deployment of AI models.

With dstack, you use YAML configuration files to define how your applications run. These files specify which [Lambda On-Demand Cloud](https://lambda.ai/service/gpu-cloud) resources to use and how to start your workloads. You can run one-off jobs, set up full-featured remote development environments that open in VS Code, or deploy persistent services that expose APIs for your models.

In this tutorial, you'll learn how to:

- Run a [Task](https://dstack.ai/docs/concepts/tasks/) that evaluates an LLM's ability to solve multiplication problems.
- Set up a remote [development environment](https://dstack.ai/docs/concepts/dev-environments/) for use with VS Code.
- Launch a [Service](https://dstack.ai/docs/concepts/services/) that serves an LLM via an OpenAI-compatible API endpoint.
- Create an [SSH Fleet](https://dstack.ai/docs/concepts/fleets/#ssh) on a [Lambda 1-Click Cluster](https://lambda.ai/service/gpu-cloud/1-click-clusters).

## Prerequisites

All of the instructions in this tutorial should be followed on your local machine, not on an on-demand instance.

Before you begin, make sure the following tools are installed:

- `python3`
- `python3-pip`
- `git`
- `curl`
- `jq`

On Ubuntu, you can install these packages by running:

```bash
sudo apt update && sudo apt install -y python3 python3-pip git curl jq
```
