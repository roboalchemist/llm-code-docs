# Source: https://docs.qodo.ai/qodo-documentation/on-prem/qodo-on-premise/installation-process-overview.md

# Installation Process Overview

#### Phase 1: Preparation

**1. Obtain Replicated Credentials**

* Contact Qodo to receive your Replicated registry credentials
* Verify access to both registries:
  * `artifacts-self-hosted.qodo.ai`
  * `artif-reg-self-hosted.codium.ai`

**2. Prepare Infrastructure**

* Deploy and configure Kubernetes cluster
* Set up `kubectl` access with admin permissions
* Install `helm` cli.
* (For Context Engine) Deploy `PostgreSQL v17+` with required databases and `pgvector`&#x20;

**3. Configure External Dependencies**

For all products:

* Set up AI model access (API keys for `OpenAI`, `Anthropic`, `Vertex AI`, or `AWS Bedrock`)
* Configure Git provider webhooks and authentication.

For **Context Engine** specifically:

* Create PostgreSQL databases for indexer and metadata service
* Configure network access from K8s cluster to database
* Set up vector database (pgvector)

**4. Gather Configuration Values**

* AI model API keys
* Git provider credentials and webhook secrets
* Database connection strings
* Domain names and TLS certificates
* Organization/team structure

#### Phase 2: Deployment

**General Helm Deployment Pattern:**

All Qodo products follow a similar deployment workflow:

```bash
# 1. Login to Replicated registry
helm registry login artifacts-self-hosted.qodo.ai \
  --username $provided_user \
  --password $provided_password

# 2. Pull the Helm chart
helm pull oci://artifacts-self-hosted.qodo.ai/codium-stack/stable/module

# 3. Create values.yaml file (product-specific)

# 4. Create secrets configuration (TOML format)

# 5. Deploy with Helm
helm upgrade --install <product-name> ./module-<version>.tgz \
  -f ./values.yaml \
  -n <namespace> \
  --create-namespace
```

**Product-Specific Deployment Steps:**

**Qodo IDE:**

* Create `.secrets.toml` file with AI model keys
* (Optional) Enable Agentic Mode with additional database configuration
* (Optional) Enable CronJobs and Jobs for Agentic Mode database partitioning

**Qodo GIT:**

* Create `.secrets.toml` with Git provider configuration
* Configure webhooks in your Git provider
* Deploy with analytics sidecar

**Context Engine (Multi-Service Deployment):** Deploy each service separately with its own values file:

1. Metadata Service
2. Indexer Service (with reindex CronJob)
3. Context Retriever Service
4. Configure shared secrets for all services

#### Phase 3: Configuration

**1. Secrets Management**

All products use TOML files for secret configuration, mounted as Kubernetes secrets:

Example structure:

```toml
[openai]
key = "sk-..."
org = "org-..."

[anthropic]
key = "sk-ant-..."

[github]  # or gitlab, bitbucket
private_key = """
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----
"""
webhook_secret = "..."
app_id = "..."

[config]
model = "claude-3-7-sonnet-20250219"
model_reasoning = "claude-sonnet-4-20250514_thinking"
model_turbo = "gpt-4.1-2025-04-14"
fallback_models = ["gpt-4.1-2025-04-14"]
```

**2. Ingress Configuration**

Example ingress configuration (`EKS` with `ALB`):

```yaml
ingress:
  enabled: true
  host: "qodo.yourcompany.com"
  annotations:
    kubernetes.io/ingress.class: "alb"  # or nginx
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
  hosts:
    - paths:
        - path: /api
          pathType: Prefix
  tls:
    - secretName: qodo-tls-cert
      hosts:
        - qodo.yourcompany.com
```

**3. Git Provider Integration**

For GitHub:

* Create GitHub App with appropriate permissions
* Generate private key
* Install app on organization/repositories
* Configure webhook URL to point to your ingress

For GitLab/Bitbucket:

* Configure webhook secrets
* Set up bearer tokens or OAuth
* Configure API base URL for self-hosted instances

#### Phase 4: Validation

**1. Verify Pod Status**

```bash
kubectl get pods -n <namespace>
kubectl logs <pod-name> -n <namespace>
```

**2. Check Service Endpoints**

```bash
kubectl get svc -n <namespace>
kubectl get ingress -n <namespace>
```

**3. Test Connectivity**

* For Qodo GIT: Trigger a test webhook from Git provider
* For Qodo Context: Add test repository to index
* For Qodo IDE: Connect IDE and test chat/generation

***
