# Source: https://docs.qodo.ai/qodo-documentation/on-prem/qodo-on-premise/infrastructure-requirements.md

# Infrastructure Requirements

#### **Kubernetes Cluster:**

* Kubernetes version 1.24 or higher
* Supported distributions: Any K8s-compatible platform (`GKE`, `EKS`, `AKS`, `OpenShift`, `Rancher`, vanilla `k8s`)
* Network connectivity to `artifacts-self-hosted.qodo.ai` and `artif-reg-self-hosted.codium.ai`

#### **Tools Required:**

* `helm`
* `kubectl` - configured with cluster admin access&#x20;

#### **Resources:**

<table><thead><tr><th>Component</th><th>CPU request</th><th valign="middle">Memory request</th></tr></thead><tbody><tr><td>Qodo Git</td><td>1</td><td valign="middle">10Gi</td></tr><tr><td>Qodo IDE</td><td>4</td><td valign="middle">12Gi</td></tr><tr><td>Indexer</td><td>500m</td><td valign="middle">2Gi</td></tr><tr><td>Metadata Service</td><td>500m</td><td valign="middle">2Gi</td></tr><tr><td>Context Engine</td><td>500m</td><td valign="middle">2Gi</td></tr></tbody></table>

#### **Network Requirements:**

* Kubernetes cluster must be able to reach Qodo's container registries
* Access to external AI model APIs (`OpenAI`, `Anthropic`, `Vertex AI`, `AWS Bedrock`) or self-hosted LLMs
* Connectivity to your Git provider (`GitHub`, `GitLab`, `Bitbucket`)
