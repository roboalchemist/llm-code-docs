# Source: https://docs.vllm.ai/en/stable/deployment/integrations/production-stack/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/integrations/production-stack.md "Edit this page")

# Production stack[¶](#production-stack "Permanent link")

Deploying vLLM on Kubernetes is a scalable and efficient way to serve machine learning models. This guide walks you through deploying vLLM using the [vLLM production stack](https://github.com/vllm-project/production-stack). Born out of a Berkeley-UChicago collaboration, [vLLM production stack](https://github.com/vllm-project/production-stack) is an officially released, production-optimized codebase under the [vLLM project](https://github.com/vllm-project), designed for LLM deployment with:

-   **Upstream vLLM compatibility** -- It wraps around upstream vLLM without modifying its code.
-   **Ease of use** -- Simplified deployment via Helm charts and observability through Grafana dashboards.
-   **High performance** -- Optimized for LLM workloads with features like multimodel support, model-aware and prefix-aware routing, fast vLLM bootstrapping, and KV cache offloading with [LMCache](https://github.com/LMCache/LMCache), among others.

If you are new to Kubernetes, don\'t worry: in the vLLM production stack [repo](https://github.com/vllm-project/production-stack), we provide a step-by-step [guide](https://github.com/vllm-project/production-stack/blob/main/tutorials/00-install-kubernetes-env.md) and a [short video](https://www.youtube.com/watch?v=EsTJbQtzj0g) to set up everything and get started in **4 minutes**!

## Pre-requisite[¶](#pre-requisite "Permanent link")

Ensure that you have a running Kubernetes environment with GPU (you can follow [this tutorial](https://github.com/vllm-project/production-stack/blob/main/tutorials/00-install-kubernetes-env.md) to install a Kubernetes environment on a bare-medal GPU machine).

## Deployment using vLLM production stack[¶](#deployment-using-vllm-production-stack "Permanent link")

The standard vLLM production stack is installed using a Helm chart. You can run this [bash script](https://github.com/vllm-project/production-stack/blob/main/utils/install-helm.sh) to install Helm on your GPU server.

To install the vLLM production stack, run the following commands on your desktop:

    sudo helm repo add vllm https://vllm-project.github.io/production-stack
    sudo helm install vllm vllm/vllm-stack -f tutorials/assets/values-01-minimal-example.yaml

This will instantiate a vLLM-production-stack-based deployment named `vllm` that runs a small LLM (Facebook opt-125M model).

### Validate Installation[¶](#validate-installation "Permanent link")

Monitor the deployment status using:

    sudo kubectl get pods

And you will see that pods for the `vllm` deployment will transit to `Running` state.

    NAME                                           READY   STATUS    RESTARTS   AGE
    vllm-deployment-router-859d8fb668-2x2b7        1/1     Running   0          2m38s
    vllm-opt125m-deployment-vllm-84dfc9bd7-vb9bs   1/1     Running   0          2m38s

Note

It may take some time for the containers to download the Docker images and LLM weights.

### Send a Query to the Stack[¶](#send-a-query-to-the-stack "Permanent link")

Forward the `vllm-router-service` port to the host machine:

    sudo kubectl port-forward svc/vllm-router-service 30080:80

And then you can send out a query to the OpenAI-compatible API to check the available models:

    curl -o- http://localhost:30080/v1/models

Output

    
      ]
    }

To send an actual chatting request, you can issue a curl request to the OpenAI `/completion` endpoint:

    curl -X POST http://localhost:30080/v1/completions \
      -H "Content-Type: application/json" \
      -d ''

Output

    
      ]
    }

### Uninstall[¶](#uninstall "Permanent link")

To remove the deployment, run:

    sudo helm uninstall vllm

------------------------------------------------------------------------

### (Advanced) Configuring vLLM production stack[¶](#advanced-configuring-vllm-production-stack "Permanent link")

The core vLLM production stack configuration is managed with YAML. Here is the example configuration used in the installation above:

Yaml

    servingEngineSpec:
      runtimeClassName: ""
      modelSpec:
      - name: "opt125m"
        repository: "vllm/vllm-openai"
        tag: "latest"
        modelURL: "facebook/opt-125m"

        replicaCount: 1

        requestCPU: 6
        requestMemory: "16Gi"
        requestGPU: 1

        pvcStorage: "10Gi"

In this YAML configuration:

-   **`modelSpec`** includes:
    -   `name`: A nickname that you prefer to call the model.
    -   `repository`: Docker repository of vLLM.
    -   `tag`: Docker image tag.
    -   `modelURL`: The LLM model that you want to use.
-   **`replicaCount`**: Number of replicas.
-   **`requestCPU` and `requestMemory`**: Specifies the CPU and memory resource requests for the pod.
-   **`requestGPU`**: Specifies the number of GPUs required.
-   **`pvcStorage`**: Allocates persistent storage for the model.

Note

If you intend to set up two pods, please refer to this [YAML file](https://github.com/vllm-project/production-stack/blob/main/tutorials/assets/values-01-2pods-minimal-example.yaml).

Tip

vLLM production stack offers many more features (*e.g.* CPU offloading and a wide range of routing algorithms). Please check out these [examples and tutorials](https://github.com/vllm-project/production-stack/tree/main/tutorials) and our [repo](https://github.com/vllm-project/production-stack) for more details!

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [December 14, 2025] ]