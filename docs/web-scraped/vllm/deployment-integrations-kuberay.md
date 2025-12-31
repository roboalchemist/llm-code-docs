# Source: https://docs.vllm.ai/en/stable/deployment/integrations/kuberay/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/deployment/integrations/kuberay.md "Edit this page")

# KubeRay[¶](#kuberay "Permanent link")

[KubeRay](https://github.com/ray-project/kuberay) provides a Kubernetes-native way to run vLLM workloads on Ray clusters. A Ray cluster can be declared in YAML, and the operator then handles pod scheduling, networking configuration, restarts, and blue-green deployments --- all while preserving the familiar Kubernetes experience.

## Why KubeRay instead of manual scripts?[¶](#why-kuberay-instead-of-manual-scripts "Permanent link")

  Feature              Manual scripts                                  KubeRay
  -------------------- ----------------------------------------------- ------------------------------------------------------------------------------------
  Cluster bootstrap    Manually SSH into every node and run a script   One command to create or update the whole cluster: `kubectl apply -f cluster.yaml`
  Autoscaling          Manual                                          Automatically patches CRDs for adjusting cluster size
  Upgrades             Tear down & re-create manually                  Blue/green deployment updates supported
  Declarative config   Bash flags & environment variables              Git-ops-friendly YAML CRDs (RayCluster/RayService)

Using KubeRay reduces the operational burden and simplifies integration of Ray + vLLM with existing Kubernetes workflows (CI/CD, secrets, storage classes, etc.).

## Learn more[¶](#learn-more "Permanent link")

-   [\"Serve a Large Language Model using Ray Serve LLM on Kubernetes\"](https://docs.ray.io/en/master/cluster/kubernetes/examples/rayserve-llm-example.html) - An end-to-end example of how to serve a model using vLLM, KubeRay, and Ray Serve.
-   [KubeRay documentation](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [July 15, 2025] ]