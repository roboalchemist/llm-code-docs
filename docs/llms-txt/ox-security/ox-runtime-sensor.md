# Source: https://docs.ox.security/secure-runtime/ox-runtime-sensor.md

# OX Runtime Sensor

> **Note:** This capability is currently in Early Access (EA) and is not generally available. To request access, please contact OX technical support.

Runtime Sensor is an OX capability for Kubernetes environments that collects runtime signals from your applications and turns them into actionable insights in OX.

The current version of Runtime Sensor focuses on JavaScript, so it is applicable to your system if your repositories include JavaScript.

Runtime Sensor helps you decide what to fix first. It detects which third-party libraries are actually loaded in memory at runtime. When a known vulnerability affects a library in your codebase, knowing whether that library is loaded now gives you a stronger indication of urgency during triage.

Insights appear in OX in the Active Issues page as severity factors. You see whether a dependency is loaded in runtime or not loaded, with evidence you can review. This context lets you prioritize fixes that reduce real, current risk in your running services.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-267a1ea37e63bb3938349471919fadbcbebb85e8%2FRuntime_active%20_issues%20(2).png?alt=media" alt=""><figcaption></figcaption></figure>

In the [SBOM page](https://docs.ox.security/inventory-with-ox-bom/sbom) you can view the runtime status of each asset.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-592038b7ffc54785d709802ed752727cb4e72c5d%2FRuntime_SBOM1.png?alt=media" alt=""><figcaption></figcaption></figure>

The OX Runtime Sensor runs as a Kubernetes DaemonSet. It loads eBPF programs to observe runtime activity on each node, including library loading and process behavior in your workloads. The sensor authenticates to OX with an API key over outbound TLS. It does not write data to the node and does not require persistent storage. CPU, memory, and disk usage are minimal.

## Prerequisites

* **Technology:** K8s (EKS/AKS/GKE)
* **K8s version:** Kubernetes v1.20 and later
* **Linux distributions:** Debian, Alpine
* **Linux kernel:** v5.10 and later with BTF enabled

## Step 1: Create a new API key

1. From the left pane of **OX dashboard**, select **Settings > API Key Settings**.
2. In the **API Key Settings** window, select **CREATE API KEY**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7e81b28f5c0ff11132bf749b7a737e69b3905b09%2FRuntime%20API%20key.png?alt=media" alt="" width="358"><figcaption></figcaption></figure>

1. In the **Create API Key** box, set the following and select **CREATE**:

* **API Key Name:** Add a meaningful name that is easy to identify. It is good practice to include the key's intended purpose in the name.
* **API Key Type:** Select **K8 Inspector/Runtime Sensor Integration**.
* **Expiration Date:** Until when you can use this key.

1. Copy the key that appears and save the key it in a safe location. This is the only time when you can see and copy the actual key.
2. Select **CLOSE**. The new key appears in the **API Key Settings** page.

## Step 2: Ensure cluster access

Make sure that the cluster has access to: `api.cloud.ox.security` .

## Step 3: Create `ox-runtime` namespace

```
kubectl create namespace ox-runtime
```

## Step 4: Push API keys to Kubernetes Secrets

1. To create a Kubernetes secret named `ox-runtime-sensor-secret` with your API key, run:

```
kubectl -n ox-runtime create secret generic ox-runtime-sensor-secret --from-literal=api-key=<your-api-key-value>
```

1. Replace `<your-api-key-value>` with the [API key](#creating-a-new-api-key) you previously generated.

## Step 5: Install OX Runtime Sensor with Helm

```
helm repo add ox-runtime-sensor-repo https://charts.cloud.ox.security
helm repo update
helm install ox-runtime-sensor ox-runtime-sensor-repo/ox-runtime-sensor --namespace ox-runtime
```

## Step 6: Connect to OX Runtime Sensor

> **Note:** Before connecting, a DevOps team member must ensure that the CronJob is running in your environment.

1. In the OX platform, go to the **Connectors** page.
2. Select **Add Connector** and search for **OX Runtime Sensor**.
3. In the **Configure your OX Runtime Sensor credentials** dialog, select **CONNECT**.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-639cd751b81fdc06e5bd05864256351d7ffb42a9%2FRuntime%20connect.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

[To use eBPF programs, OX complies with the GPL.](https://docs.ox.security/secure-runtime/ox-runtime-sensor/gpl-licensed-components-and-source-availability)
