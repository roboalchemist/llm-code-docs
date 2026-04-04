# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/cache-with-pvc.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Cache with PVC

> Enable plugin caching with Persistent Volume Claims to speed up Terraform and OpenTofu deployments

This page explains how to enable plugin caching for OpenTofu (also applies to Terraform and Terragrunt) when using a Self-Hosted Kubernetes Agent with Persistent Volume Claims (PVC). This feature is available for SHAG (Self-Hosted Agent on Kubernetes) customers only.

## Overview

To improve performance in infrastructure-as-code environments, env zero supports an optional plugin cache. This cache stores previously downloaded provider plugins on a persistent volume, allowing reuse across runs within the same environment. The plugin cache can reduce run times and avoid redundant downloads when enabled.

This caching mechanism is opt-in and requires specific environment variables. It is supported only for environments running with a self-hosted Kubernetes agent that uses PVC.

## Prerequisites

Before enabling plugin caching, ensure that:

* You are using Self-Hosted Kuberneties Agent (SHAG) v3.0.1097 or above
* Your agent is already configured to use Persistent Volume Claims (PVC)
* You are running OpenTofu, Terraform, or Terragrunt

## Enabling Plugin Cache

There are two supported ways to use plugin caching with PVC:

### Option 1  - Agent’s Existing PVC (Recommended)

If your agent is already configured with a PVC (e.g., for state, working directory, etc.), you can simply enable caching by setting:

```
ENV0_USE_TF_PLUGIN_CACHE=true
```

**Where to set this?**

* As an Organization or Project Environment Variable in env0

When this variable is set, env zero will use a persistent volume to cache provider plugins used by OpenTofu, Terraform, or Terragrunt. These plugins will then be reused in subsequent runs within the same environment

### **Option 2 – Using a Dedicated PVC for Terraform Plugin Cache (Advanced)**

If you have multiple PVCs, and you want to explicitly choose which PVC is used for Terraform plugin cache, then do not set `ENV0_USE_TF_PLUGIN_CACHE=true`

Instead, set the following in your Helm values under `agentAdditionalEnvVars` (or `podAdditionalEnvVars`):

```yaml  theme={null}
agentAdditionalEnvVars:
  - name: TF_PLUGIN_CACHE_DIR
    value: "/path/to/your/pvc/cache"
  - name: TF_PLUGIN_CACHE_MAY_BREAK_DEPENDENCY_LOCK_FILE
    value: "true"
```

### Wiping the Cache

If you need to wipe the plugin cache before a run (for example, to force re-downloading of providers or resolve potential cache issues), set the following additional environment variable:

`ENV0_WIPE_TF_PLUGIN_CACHE=true`

<Info>
  📘 Note: This variable only takes effect if `ENV0_USE_TF_PLUGIN_CACHE` is also set.
</Info>

When both variables are set, the plugin cache will be cleared before the run begins.

<Warning>
  Requirements

* Self-Hosted Kubernetes Agent (SHAG) v3.0.1097 or above
* Use of Persistent Volume Claims (PVC) for storage
* Applies to environments using OpenTofu, Terraform, or Terragrunt
</Warning>

Built with [Mintlify](https://mintlify.com).
