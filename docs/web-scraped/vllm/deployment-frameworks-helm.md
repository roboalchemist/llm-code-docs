# Source: https://docs.vllm.ai/en/stable/deployment/frameworks/helm/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/frameworks/helm.md "Edit this page")

# Helm[¶](#helm "Permanent link")

A Helm chart to deploy vLLM for Kubernetes

Helm is a package manager for Kubernetes. It helps automate the deployment of vLLM applications on Kubernetes. With Helm, you can deploy the same framework architecture with different configurations to multiple namespaces by overriding variable values.

This guide will walk you through the process of deploying vLLM with Helm, including the necessary prerequisites, steps for Helm installation and documentation on architecture and values file.

## Prerequisites[¶](#prerequisites "Permanent link")

Before you begin, ensure that you have the following:

-   A running Kubernetes cluster
-   NVIDIA Kubernetes Device Plugin (`k8s-device-plugin`): This can be found at <https://github.com/NVIDIA/k8s-device-plugin>
-   Available GPU resources in your cluster
-   (Optional) An S3 bucket or other storage with the model weights, if using automatic model download

## Installing the chart[¶](#installing-the-chart "Permanent link")

To install the chart with the release name `test-vllm`:

    helm upgrade --install --create-namespace \
      --namespace=ns-vllm test-vllm . \
      -f values.yaml \
      --set secrets.s3endpoint=$ACCESS_POINT \
      --set secrets.s3bucketname=$BUCKET \
      --set secrets.s3accesskeyid=$ACCESS_KEY \
      --set secrets.s3accesskey=$SECRET_KEY

## Uninstalling the chart[¶](#uninstalling-the-chart "Permanent link")

To uninstall the `test-vllm` deployment:

    helm uninstall test-vllm --namespace=ns-vllm

The command removes all the Kubernetes components associated with the chart **including persistent volumes** and deletes the release.

## Architecture[¶](#architecture "Permanent link")

[![helm deployment architecture](../../../assets/deployment/architecture_helm_deployment.png)](../../../assets/deployment/architecture_helm_deployment.png)

## Values[¶](#values "Permanent link")

The following table describes configurable parameters of the chart in `values.yaml`:

  Key                                          Type     Default                                                                                                                                                                                     Description
  -------------------------------------------- -------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------
  autoscaling                                  object                                                                                                Autoscaling configuration
  autoscaling.enabled                          bool     false                                                                                                                                                                                       Enable autoscaling
  autoscaling.maxReplicas                      int      100                                                                                                                                                                                         Maximum replicas
  autoscaling.minReplicas                      int      1                                                                                                                                                                                           Minimum replicas
  autoscaling.targetCPUUtilizationPercentage   int      80                                                                                                                                                                                          Target CPU utilization for autoscaling
  configs                                      object                                                                                                                                                                                             Configmap
  containerPort                                int      8000                                                                                                                                                                                        Container port
  customObjects                                list     \[\]                                                                                                                                                                                        Custom Objects configuration
  deploymentStrategy                           object                                                                                                                                                                                             Deployment strategy configuration
  externalConfigs                              list     \[\]                                                                                                                                                                                        External configuration
  extraContainers                              list     \[\]                                                                                                                                                                                        Additional containers configuration
  extraInit                                    object   ,\"initContainers\":\[\],\"pvcStorage\":\"1Gi\"}                                                                                                       Additional configuration for init containers
  extraInit.modelDownload                      object                                                                                                                                                                             Model download functionality configuration
  extraInit.modelDownload.enabled              bool     true                                                                                                                                                                                        Enable automatic model download job and wait container
  extraInit.modelDownload.image                object                                                                                                          Image for model download operations
  extraInit.modelDownload.waitContainer        object                                                                                                                                                                                             Wait container configuration (command, args, env)
  extraInit.modelDownload.downloadJob          object                                                                                                                                                                                             Download job configuration (command, args, env)
  extraInit.initContainers                     list     \[\]                                                                                                                                                                                        Custom init containers (appended after model download if enabled)
  extraInit.pvcStorage                         string   \"1Gi\"                                                                                                                                                                                     Storage size for the PVC
  extraInit.s3modelpath                        string   \"relative_s3_model_path/opt-125m\"                                                                                                                                                         (Optional) Path of the model on S3
  extraInit.awsEc2MetadataDisabled             bool     true                                                                                                                                                                                        (Optional) Disable AWS EC2 metadata service
  extraPorts                                   list     \[\]                                                                                                                                                                                        Additional ports configuration
  gpuModels                                    list     \[\"TYPE_GPU_USED\"\]                                                                                                                                                                       Type of gpu used
  image                                        object      Image configuration
  image.command                                list     \[\"vllm\",\"serve\",\"/data/\",\"\--served-model-name\",\"opt-125m\",\"\--host\",\"0.0.0.0\",\"\--port\",\"8000\"\]                                                                        Container launch command
  image.repository                             string   \"vllm/vllm-openai\"                                                                                                                                                                        Image repository
  image.tag                                    string   \"latest\"                                                                                                                                                                                  Image tag
  livenessProbe                                object   ,\"initialDelaySeconds\":15,\"periodSeconds\":10}                                                                   Liveness probe configuration
  livenessProbe.failureThreshold               int      3                                                                                                                                                                                           Number of times after which if a probe fails in a row, Kubernetes considers that the overall check has failed: the container is not alive
  livenessProbe.httpGet                        object                                                                                                                                                           Configuration of the kubelet http request on the server
  livenessProbe.httpGet.path                   string   \"/health\"                                                                                                                                                                                 Path to access on the HTTP server
  livenessProbe.httpGet.port                   int      8000                                                                                                                                                                                        Name or number of the port to access on the container, on which the server is listening
  livenessProbe.initialDelaySeconds            int      15                                                                                                                                                                                          Number of seconds after the container has started before liveness probe is initiated
  livenessProbe.periodSeconds                  int      10                                                                                                                                                                                          How often (in seconds) to perform the liveness probe
  maxUnavailablePodDisruptionBudget            string   \"\"                                                                                                                                                                                        Disruption Budget Configuration
  readinessProbe                               object   ,\"initialDelaySeconds\":5,\"periodSeconds\":5}                                                                     Readiness probe configuration
  readinessProbe.failureThreshold              int      3                                                                                                                                                                                           Number of times after which if a probe fails in a row, Kubernetes considers that the overall check has failed: the container is not ready
  readinessProbe.httpGet                       object                                                                                                                                                           Configuration of the kubelet http request on the server
  readinessProbe.httpGet.path                  string   \"/health\"                                                                                                                                                                                 Path to access on the HTTP server
  readinessProbe.httpGet.port                  int      8000                                                                                                                                                                                        Name or number of the port to access on the container, on which the server is listening
  readinessProbe.initialDelaySeconds           int      5                                                                                                                                                                                           Number of seconds after the container has started before readiness probe is initiated
  readinessProbe.periodSeconds                 int      5                                                                                                                                                                                           How often (in seconds) to perform the readiness probe
  replicaCount                                 int      1                                                                                                                                                                                           Number of replicas
  resources                                    object   ,\"requests\":}                                                         Resource configuration
  resources.limits.\"nvidia.com/gpu\"          int      1                                                                                                                                                                                           Number of GPUs used
  resources.limits.cpu                         int      4                                                                                                                                                                                           Number of CPUs
  resources.limits.memory                      string   \"16Gi\"                                                                                                                                                                                    CPU memory configuration
  resources.requests.\"nvidia.com/gpu\"        int      1                                                                                                                                                                                           Number of GPUs used
  resources.requests.cpu                       int      4                                                                                                                                                                                           Number of CPUs
  resources.requests.memory                    string   \"16Gi\"                                                                                                                                                                                    CPU memory configuration
  secrets                                      object                                                                                                                                                                                             Secrets configuration
  serviceName                                  string   \"\"                                                                                                                                                                                        Service name
  servicePort                                  int      80                                                                                                                                                                                          Service port
  labels.environment                           string   test                                                                                                                                                                                        Environment name

## Configuration Examples[¶](#configuration-examples "Permanent link")

### Using S3 Model Download (Default)[¶](#using-s3-model-download-default "Permanent link")

    extraInit:
      modelDownload:
        enabled: true
      pvcStorage: "10Gi"
      s3modelpath: "models/llama-7b"

### Using Custom Init Containers Only[¶](#using-custom-init-containers-only "Permanent link")

For use cases like llm-d where you need custom sidecars without model download:

    extraInit:
      modelDownload:
        enabled: false
      initContainers:
        - name: llm-d-routing-proxy
          image: ghcr.io/llm-d/llm-d-routing-sidecar:v0.2.0
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8080
              name: proxy
          securityContext:
            runAsUser: 1000
          restartPolicy: Always
      pvcStorage: "10Gi"

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 6, 2025] ]