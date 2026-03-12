# Source: https://docs.qodo.ai/qodo-documentation/on-prem/git-integration/setup-the-git-integration.md

# Setup the Git Integration

Follow this guide to setup, install, and begin using the Git Integration in On Prem environments.

{% hint style="info" %}
For steps to deploy the Qodo app, see our Git documentation.
{% endhint %}

## Prerequisites

Before deploying, ensure the following are in place:

* Access to a Kubernetes cluster that can reach `artif-reg-self-hosted.codium.ai`
* A node with at least `1 CPU` and `10Gi` memory
* Helm v3 installed
* `kubectl` CLI installed

#### Each provider (GitHub, Bitbucket, GitLab) requires:

1. A tailored `values.yaml`
2. Proper secrets configuration (`.secrets.toml`)
3. External or locally created Kubernetes secrets

***

## Github

1. **Create a `values.yaml` file:** This example is using GKE(GCP k8s), ALB as ingress and GCP managed certificate.

```yaml
image:
  repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/pr-agent
  tag: replicated_b85
  
configMaps:
  main:
    CONFIG.IDENTITY_PROVIDER: ""
    CONFIG.ANALYTICS_FOLDER: "/logs"

envFrom:
  configMapRefs:
    - name: main
      useShortName: true

deployments:
  enabled: true
  ports:
    - containerPort: 3000
      name: http
  resources:
    requests:
      cpu: '1'
      memory: '10Gi'
  command:
    - "python"
  args:
    - "-m"
    - "gunicorn"
    - "-k"
    - "uvicorn.workers.UvicornWorker"
    - "-c"
    - "pr_agent/servers/gunicorn_config.py"
    - "--forwarded-allow-ips"
    - "*"
    - "pr_agent.servers.github_app:app"
  probes:
    startup:
      httpGet:
        path: /self_test
        port: 3000
      failureThreshold: 3
      initialDelaySeconds: 20
      periodSeconds: 45
      successThreshold: 1
      timeoutSeconds: 45

  sidecars:
    analytics:
      image:
        repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/pr-agent-sidecar
        tag: replicated_b85
      command:
        - "python"
        - "main.py"
      args:
        - "--sink"
        - "mixpanel"
        - "--sink"
        - "stdout"
        - "--log_directory"
        - "/logs"
      ports: []
      envFrom:
        configMapRefs:
          - name: main
            useShortName: true
        secretRefs:
          - name: mixpanel
            useShortName: true

volumes:
  settings-volume:
    secret:
      secretName: settings
      useShortName: true
  logs-volume:
    emptyDir: {}

volumeMounts:
  settings-volume:
    mountPath: /app/pr_agent/settings_prod 
  logs-volume:
    mountPath: /logs

ingress:
  enabled: true
  host: example.company.com
  #annotations:
    # Custom annotations goes here
  hosts:
    - paths:
        - path: /
          pathType: Exact
        - path: /api/v1
          pathType: Prefix
        - path: /webhook
          pathType: Prefix
        - path: /installed
          pathType: Prefix
        - path: /uninstalled
          pathType: Prefix

service:
  enabled: true
  port: 3000
  type: NodePort
  ports:
    http:
      targetPort: "http" # named or numeric port in a pod

externalSecrets:
  enabled: true
  clusterSecretStore: true
  secretStoreName: "gcp-backend"
  secrets:
    - targetSecretName: settings
      remoteSecretName: qodo-merge-settings #create this on your secret backend
      data:
        - secretKey: .secrets.toml
```

2\. **Configure Qodo secrets:** You can define either an external or local secret.

To define a local secret, run:

```toml
kubectl create secret generic qodo-merge-settings --from-file=.secrets.toml -n $namespace
```

To define a `.secret.toml` file, check out the example below.

* There's a section in the file for each LLM engine.
* The Github section sets the app installment.
* Config section: this config depends on what LLMs are available. You can reach Qodo Support to ensure you're configuring this section correctly.

```toml
[anthropic]
key = ""

[aws]
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_REGION_NAME = ""

[openai]
key = ""
org = ""

[vertexai]
credentials = ""

[github]
deployment_type = ""
private_key = ""
webhook_secret = ""
app_id = ""

[config]
model_reasoning="claude-sonnet-4-20250514_thinking"
model="claude-3-7-sonnet-20250219"
model_turbo = "gpt-4.1-2025-04-14"
fallback_models=["gpt-4.1-2025-04-14"]
```

3. **Deploy:** Once the `values.yaml` file and the secrets are in place, you need to:

* Login to [artifacts-self-hosted.qodo.ai](http://artifacts-self-hosted.qodo.ai):

```bash
helm registry login artifacts-self-hosted.qodo.ai --username $provided_user --password $provided_password
```

* Pull the latest helm chart:

```bash
helm pull oci://artifacts-self-hosted.qodo.ai/codium-stack/stable/module
```

* Deploy Qodo:

```bash
helm upgrade --install qodo-merge ./module-0.4.4.tgz -f ./values.yaml  -n qodo-merge --create-namespace
```

***

## Bitbucket

1. **Create a `values.yaml` file:** This example is using GKE(GCP k8s), ALB as ingress and GCP managed certificate.
   * The Ingress section must be updated with proper domain and certificate.
   * When using other cloud providers or native K8s, make sure to update Ingress values and External secrets or mount volumes.

```yaml
image:
  repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/pr-agent
  tag: replicated_b85

configMaps:
  main:
    CONFIG.IDENTITY_PROVIDER: ""
    CONFIG.ANALYTICS_FOLDER: "/logs"

envFrom:
  configMapRefs:
    - name: main
      useShortName: true

deployments:
  enabled: true
  ports:
    - containerPort: 3000
      name: http
  resources:
    requests:
      cpu: '1'
      memory: '10Gi'
  command:
    - "python"
  args:
    - "-m"
    - "gunicorn"
    - "-k"
    - "uvicorn.workers.UvicornWorker"
    - "-c"
    - "pr_agent/servers/gunicorn_config.py"
    - "--forwarded-allow-ips"
    - "*"
    - "pr_agent.servers.bitbucket_server_webhook:app"
  probes:
    startup:
      httpGet:
        path: /self_test
        port: 3000
      failureThreshold: 3
      initialDelaySeconds: 20
      periodSeconds: 45
      successThreshold: 1
      timeoutSeconds: 45

  sidecars:
    analytics:
      image:
        repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/pr-agent-sidecar
        tag: replicated_b85
      command:
        - "python"
        - "main.py"
      args:
        - "--sink"
        - "mixpanel"
        - "--sink"
        - "stdout"
        - "--log_directory"
        - "/logs"
      ports: []
      envFrom:
        configMapRefs:
          - name: main
            useShortName: true
        secretRefs:
          - name: mixpanel
            useShortName: true

volumes:
  settings-volume:
    secret:
      secretName: settings
      useShortName: true
  logs-volume:
    emptyDir: {}

volumeMounts:
  settings-volume:
    mountPath: /app/pr_agent/settings_prod 
  logs-volume:
    mountPath: /logs

ingress:
  enabled: true
  host: example.company.com
  #annotations:
     # Custom annotations goes here
  hosts:
    - paths:
        - path: /
          pathType: Exact
        - path: /api/v1
          pathType: Prefix
        - path: /webhook
          pathType: Prefix
        - path: /installed
          pathType: Prefix
        - path: /uninstalled
          pathType: Prefix

service:
  enabled: true
  port: 3000
  type: NodePort
  ports:
    http:
      targetPort: "http"
      
externalSecrets:
  enabled: true
  clusterSecretStore: true
  secretStoreName: "gcp-backend"
  secrets:
    - targetSecretName: settings
      remoteSecretName: qodo-merge-settings #create this on your secret backend
      data:
        - secretKey: .secrets.toml

```

2\. **Configure Qodo secrets:** You can define either an external or local secret.

To define a local secret, run:

```toml
kubectl create secret generic qodo-merge-settings --from-file=.secrets.toml -n $namespace
```

To define a `.secret.toml` file, check out the example below.

* There's a section in the file for each LLM engine.
* The Bitbucket section sets webhook secret, bearer token and Bitbucket URL.
* Config section: this config depends on what LLMs are available. You can reach Qodo Support to ensure you're configuring this section correctly.

```toml
[anthropic]
key = ""

[aws]
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_REGION_NAME = ""

[openai]
key = ""
org = ""

[vertexai]
credentials = ""

[bitbucket_server]
webhook_secret = ""
bearer_token = ""
url = ""

#this Filesystem it's only necessary for Bitbucket Datacenter
[file_system]
directory = "/pr-agent-secrets"
hash_file_names = true
encryption_key = "ia84cjHNYeCW9cyBr_8_XWZ9EMJr67lKsupG55RpXTM=" #this could be any random generate string

[config]
model_reasoning="claude-sonnet-4-20250514_thinking"
model="claude-3-7-sonnet-20250219"
model_turbo = "gpt-4.1-2025-04-14"
fallback_models=["gpt-4.1-2025-04-14"]
```

3. **Deploy:** Once the `values.yaml` file and the secrets are in place, you need to:

* Login to [artifacts-self-hosted.qodo.ai](http://artifacts-self-hosted.qodo.ai):

```bash
helm registry login artifacts-self-hosted.qodo.ai --username $provided_user --password $provided_password
```

* Pull the latest helm chart:

```bash
helm pull oci://artifacts-self-hosted.qodo.ai/codium-stack/stable/module
```

* Deploy Qodo:

```bash
helm upgrade --install qodo-merge ./module-0.4.4.tgz -f ./values.yaml  -n qodo-merge --create-namespace
```

## Gitlab

1. **Create a `values.yaml` file:** This example is using GKE(GCP k8s), ALB as ingress and GCP managed certificate.
   * The Ingress section must be updated with proper domain and certificate.
   * When using other cloud providers or native K8s, make sure to update Ingress values and External secrets or mount volumes.

```yaml
image:
  repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/pr-agent
  tag: replicated_b85

configMaps:
  main:
    CONFIG.IDENTITY_PROVIDER: ""
    CONFIG.ANALYTICS_FOLDER: "/logs"
    CONFIG.SECRET_PROVIDER: "configuration"

envFrom:
  configMapRefs:
    - name: main
      useShortName: true

deployments:
  enabled: true
  ports:
    - containerPort: 3000
      name: http
  resources:
    requests:
      cpu: '1'
      memory: '10Gi'
  command:
    - "python"
  args:
    - "-m"
    - "gunicorn"
    - "-k"
    - "uvicorn.workers.UvicornWorker"
    - "-c"
    - "pr_agent/servers/gunicorn_config.py"
    - "--forwarded-allow-ips"
    - "*"
    - "pr_agent.servers.gitlab_webhook:app"
  probes:
    startup:
      httpGet:
        path: /self_test
        port: 3000
      failureThreshold: 3
      initialDelaySeconds: 20
      periodSeconds: 45
      successThreshold: 1
      timeoutSeconds: 45

  sidecars:
    analytics:
      image:
        repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/pr-agent-sidecar
        tag: replicated_b85
      command:
        - "python"
        - "main.py"
      args:
        - "--sink"
        - "mixpanel"
        - "--sink"
        - "stdout"
        - "--log_directory"
        - "/logs"
      ports: []
      envFrom:
        configMapRefs:
          - name: main
            useShortName: true
        secretRefs:
          - name: mixpanel
            useShortName: true

volumes:
  settings-volume:
    secret:
      secretName: settings
      useShortName: true
  logs-volume:
    emptyDir: {}

volumeMounts:
  settings-volume:
    mountPath: /app/pr_agent/settings_prod 
  logs-volume:
    mountPath: /logs

ingress:
  enabled: true
  host: example.company.com
  annotations:
    kubernetes.io/ingress.class: "gce"
    kubernetes.io/ingress.allow-http: "true"
    networking.gke.io/v1beta1.FrontendConfig: qodo-merge-frontend-tls-config
    networking.gke.io/managed-certificates: '{{ .Release.Name | trunc 63 | trimSuffix "-" }}'
  hosts:
    - paths:
        - path: /
          pathType: Exact
        - path: /api/v1
          pathType: Prefix
        - path: /webhook
          pathType: Prefix
        - path: /installed
          pathType: Prefix
        - path: /uninstalled
          pathType: Prefix

service:
  enabled: true
  port: 3000
  type: NodePort
  ports:
    http:
      targetPort: "http" # named or numeric port in a pod

externalSecrets:
  enabled: true
  clusterSecretStore: true
  secretStoreName: "gcp-backend"
  secrets:
    - targetSecretName: settings
      remoteSecretName: qodo-merge-settings # create this on your secret backend
      data:
        - secretKey: .secrets.toml
```

2. **Configure Qodo secrets:** You can define either an external or local secret.

To define a local secret, run:

```toml
kubectl create secret generic qodo-merge-settings --from-file=.secrets.toml -n $namespace
```

To define a `.secret.toml` file, check out the example below.

* There's a section in the file for each LLM engine.
* The GitLab section sets the GitLab secret.
* Config section: this config depends on what LLMs are available. You can reach Qodo Support to ensure you're configuring this section correctly.

```toml
[anthropic]
key = ""

[aws]
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_REGION_NAME = ""

[openai]
key = ""
org = ""

[vertexai]
credentials = ""

[secret_store.gitlab]
key = ""
value = ""

[config]
model_reasoning="claude-sonnet-4-20250514_thinking"
model="claude-3-7-sonnet-20250219"
model_turbo = "gpt-4.1-2025-04-14"
fallback_models=["gpt-4.1-2025-04-14"]
```

3. **Deploy:** Once the `values.yaml` file and the secrets are in place, you need to:

* Login to [artifacts-self-hosted.qodo.ai](http://artifacts-self-hosted.qodo.ai):

```bash
helm registry login artifacts-self-hosted.qodo.ai --username $provided_user --password $provided_password
```

* Pull the latest helm chart:

```bash
helm pull oci://artifacts-self-hosted.qodo.ai/codium-stack/stable/module
```

* Deploy Qodo:

```bash
helm upgrade --install qodo-merge ./module-0.4.4.tgz -f ./values.yaml  -n qodo-merge --create-namespace
```
