# Source: https://docs.qodo.ai/qodo-documentation/on-prem/context-engine/setup-context-engine.md

# Setup Context Engine

Follow this guide to setup, install, and begin using the Context Engine in On Prem environments.

{% hint style="success" %}

## Context Engine documentation

[See the full Context Engine documentation](https://docs.qodo.ai/qodo-documentation/qodo-AWARE) for more details on the Context Engine.
{% endhint %}

## Prerequisites

### Infrastructure Requirements

The machine running the Context Engine components should have at least:

* **vCPU:** 8
* 16 **GB RAM**

**PostgreSQL Instance (Recommended Size):**

* **vCPU**: 4
* **Memory**: 32 GB
* **Disk**: 100 GB

> You may opt for smaller instances if working with a relatively small codebase.

**PostgreSQL Version**: 17

**Required Configuration:**

* `pg_vector` extension installed

  *Note: This is pre-installed in managed cloud deployments.*
* TCP port `5432` must be accessible from the Kubernetes cluster where the Context Engine will be deployed
* Two separate databases:
  * `rag-indexer`
  * `metadata`
* Two PostgreSQL users with full access to their respective databases

#### Supported Git Providers:

* GitHub (Cloud or Enterprise)
* GitLab
* Bitbucket Data Center

***

### Models Supported

These models are used by the Context Engine and must be available for the Context Engine to be used:

* `gpt-5`
* `claude-4.1-opus`

{% hint style="warning" %}
Contact Qodo support if **none of these AI models are supported by your system**.
{% endhint %}

{% hint style="warning" %}
Contact Qodo support If you're using a **custom LLM gateway**.
{% endhint %}

***

## 1. Context Engine Installation

The Context Engine consists of a few components. Install them **in the following order**:

1. `metadata-service`
2. `rag-indexer`
3. `context-retriever`
4. `context-retriever-mcp` (only if you'd like to connect your codebase understanding capabilities to tools that are not Qodo Gen or Qodo Merge).

We recommend deploying all components in the **same Kubernetes namespace**.

Each component requires its own `values.yaml` file with configuration like the following.

#### 1. metadata-service

**Example `metadata-values.yaml`:**

```yaml
image:
  repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/qodo-engine-metadata
  tag: 1.33.1
  
deployments:
  enabled: true
  resources:
    requests:
      cpu: "500m"
      memory: "2Gi"
  ports:
    - containerPort: 8000
      name: http
  probes:
    liveness:
      httpGet:
        path: /api/v1/health
        port: http
      initialDelaySeconds: 15
      failureThreshold: 5
      periodSeconds: 30
      successThreshold: 1

service:
  enabled: true
  type: NodePort
  port: 8000
  ports:
    http:
      targetPort: http

# add externalSecrets block here if needed

volumes:
  qodo-aware-secrets:
    secret:
      secretName: qodo-aware-secrets

volumeMounts:
  qodo-aware-secrets:
    mountPath: /workspace/app/config_prod
```

**Install with Helm:**

```
helm upgrade --install metadata-service oci://artifacts-self-hosted.qodo.ai/codium-stack/stable/module -f ./metadata-values.yaml
```

#### 2. rag-indexer

```yaml
image:
  repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/qodo-engine-indexer
  tag: 1.33.1
  
deployments:
  enabled: true
  resources:
    requests:
      cpu: "500m"
      memory: "2Gi"
  ports:
    - containerPort: 3000
      name: http
  probes:
    liveness:
      httpGet:
        path: /api/v1/indexer/health
        port: http
      initialDelaySeconds: 15
      failureThreshold: 5
      periodSeconds: 30
      successThreshold: 1

service:
  enabled: true
  type: NodePort
  port: 3000
  ports:
    http:
      targetPort: http

# add externalSecrets block here if needed

volumes:
  qodo-aware-secrets:
    secret:
      secretName: qodo-aware-secrets

volumeMounts:
  qodo-aware-secrets:
    mountPath: /workspace/qodo_engine/shared_settings/secrets

cronJobs:
  reindex:
    schedule: "0 3 * * *"
    concurrencyPolicy: "Allow"
    suspend: false
    image:
      repository: curlimages/curl
      tag: 8.11.1
      pullPolicy: IfNotPresent
    command:
      - "/bin/sh"
      - "-c"
      - "curl -X POST -H 'Content-Type: application/json' -d '{}' http://indexer:3000/api/v1/indexer/reindex"

configMaps:
  main:
    REINDEX_CRONJOB_SCHEDULE: "0 3 * * *"
    ENVIRONMENT_TYPE: "ON_PREM"
```

**Install with Helm:**

```
helm upgrade --install indexer oci://artifacts-self-hosted.qodo.ai/codium-stack/stable/module -f ./indexer-values.yaml
```

#### 3. context-retriever

```yaml
image:
  repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/qodo-engine-context-retriever
  tag: 1.33.1
  
deployments:
  enabled: true
  resources:
    requests:
      cpu: "500m"
      memory: "2Gi"
  ports:
    - containerPort: 8001
      name: http
  probes:
    liveness:
      httpGet:
        path: /v1/context/health
        port: http
      initialDelaySeconds: 15
      failureThreshold: 5
      periodSeconds: 30
      successThreshold: 1

service:
  enabled: true
  type: NodePort
  port: 8001
  ports:
    http:
      targetPort: http

volumes:
  qodo-aware-secrets:
    secret:
      secretName: qodo-aware-secrets

# add externalSecrets block here if needed

volumeMounts:
  qodo-aware-secrets:
    mountPath: /app/qodo_engine/shared_settings/secrets

envFrom:
  configMapRefs:
    - name: main

configMaps:
  main:
    SERVICE_CONFIG__AUTH_BACKEND_PROVIDER: "noauth"
    ENVIRONMENT_TYPE: "ON_PREM"
    test: "TEsts"
```

**Install with Helm:**

```
helm upgrade --install context-retriever oci://artifacts-self-hosted.qodo.ai/codium-stack/stable/module -f ./context-retriever-values.yaml
```

4. Trigger initial indexing (if you prefer to not wait until the cronjob is triggered): `kubectl create job indexer-reindex-manual --from=cronjob/indexer-reindex`
5. Verify `indexer` pod (that is part of the deployment, not the job) logs, to confirm indexing has completed (can take anywhere from minutes to up to a day, depends on how many repositories are configured and how big they are).

#### 4. context-retriever-mcp

{% hint style="warning" %}
**Note:** Set `context-retriever-mcp` only if you'd like to connect your codebase understanding capabilities to tools that are not Qodo Gen or Qodo Merge.
{% endhint %}

```yaml
image:
  repository: artif-reg-self-hosted.codium.ai/proxy/codium-stack/us-central1-docker.pkg.dev/codium-production/codium-repo-self-hosted/qodo-engine-context-retriever
  tag: 1.5.0
  
deployments:
  enabled: true
  resources:
    requests:
      cpu: "500m"
      memory: "2Gi"
  ports:
    - containerPort: 8001
      name: http
  probes:
    liveness:
      httpGet:
        path: /health
        port: http
      initialDelaySeconds: 15
      failureThreshold: 5
      periodSeconds: 30
      successThreshold: 1

ingress:
  enabled: true
  host: "" # add client host here
  annotations:
    # add relevant annotations here
  hosts:
    - paths:
        - path: /mcp
          pathType: Prefix

replicaCount: 1

service:
  enabled: true
  type: NodePort
  port: 8001
  ports:
    http:
      targetPort: http

volumes:
  qodo-aware-secrets:
    secret:
      secretName: qodo-aware-secrets

# add externalSecrets block here if needed

volumeMounts:
  qodo-aware-secrets:
    mountPath: /app/qodo_engine/shared_settings/secrets

envFrom:
  configMapRefs:
    - name: main

configMaps:
  main:
    SERVICE_CONFIG__EXPOSE_MCP_SERVER: "true"
    ENVIRONMENT_TYPE: "ON_PREM"
    SERVICE_CONFIG__AUTH_BACKEND_PROVIDER: "local"

```

***

## 2. Finish Setup on your version control

Finish setting up Qodo Aware on your version control:

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="image">Cover image</th></tr></thead><tbody><tr><td><h3>GitHub</h3></td><td><a href="setup-context-engine/github">github</a></td><td><a href="https://639223961-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJPQ5Hacyry184nXtoJN4%2Fuploads%2F7sgXJOyuxOozCb0tUtDN%2FGitHub.png?alt=media&#x26;token=370d90e2-02b5-4060-b88c-cdfc3b1a8fee">GitHub.png</a></td></tr><tr><td><h3>GitLab</h3></td><td><a href="setup-context-engine/gitlab">gitlab</a></td><td><a href="https://639223961-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJPQ5Hacyry184nXtoJN4%2Fuploads%2F2jMn1dgMUoPyJGWp6tCd%2FGitLab.png?alt=media&#x26;token=4134c8f1-4f94-4561-9448-cac40fc0780a">GitLab.png</a></td></tr><tr><td><h3>Bitbucket Data Center</h3></td><td><a href="setup-context-engine/bitbucket-data-center">bitbucket-data-center</a></td><td><a href="https://639223961-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJPQ5Hacyry184nXtoJN4%2Fuploads%2Ftk3AXy5wv67uyv7FEUk1%2FBitbucket.png?alt=media&#x26;token=4e3e9246-826b-444c-95ed-9f52fe0bd34e">Bitbucket.png</a></td></tr></tbody></table>

### 2.1 Custom CA

If you are using On prem git provider with HTTPS connection from qodo-engine you will need to configure the custom CA like this:

<pre class="language-yaml" data-full-width="false"><code class="lang-yaml"><strong>configMaps:
</strong><strong>  main:
</strong>    CONFIG__CERTIFICATE_BUNDLE: "/etc/ssl/custom/ca.pem"

volumeMounts:
  custom-ca:
    mountPath: /etc/ssl/custom/ca.pem
    subPath: ca.pem

volumes:
  custom-ca:
    secret:
      secretName: customer-ca-secret
</code></pre>

***

## Enabling Context Engine functionality in the Git Integration

#### Git Integration

1. Update qodo-merge secret, append the following

```toml
[rag_arguments]
enable_rag=true

[context_retrieval_service]
url = "<service name>.<namespace>" # set this to context-retriever service address
```

2. Restart pods to pick up the new secret.
