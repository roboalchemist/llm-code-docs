# Source: https://docs.datadoghq.com/containers/bits_ai_kubernetes_remediation.md

---
title: Bits AI Kubernetes Remediation
description: >-
  Discover and automatically remediate Kubernetes errors with Bits AI Kubernetes
  Remediation
breadcrumbs: Docs > Containers > Bits AI Kubernetes Remediation
---

# Bits AI Kubernetes Remediation

Bits AI Kubernetes Remediation analyzes and fixes Kubernetes errors in your infrastructure.

The following Kubernetes errors are supported:

- `CrashLoopBackOff`
- `ErrImagePull`
- `ImagePullBackOff`
- `OOMKilled`
- `CreateContainerError`
- `CreateContainerConfigError`

## Usage{% #usage %}

You can launch Bits AI Kubernetes Remediation from multiple locations within Datadog:

- **From a Kubernetes monitor**: In the *Troubleshooting* section, select a workload under *Problematic Workloads*.
- **From [Kubernetes Explorer](https://app.datadoghq.com/orchestration/explorer/pod)**: Hover over a pod status with an error to see more information about the alert and the affected workload(s), and click *Start Remediation*.
- **From the [Kubernetes Remediation](https://app.datadoghq.com/orchestration/remediation) tab**: Select a workload from the list.

Any one of these actions opens a Remediation side panel that displays:

- An AI-powered explanation for root cause, based on collected telemetry and known patterns
- Recommended next steps, which you may be able to perform directly from Datadog
- Related information on an adjustable timeframe: recent deployments, error logs, Kubernetes events, etc., including relevant metrics based on specific issue type

{% image
   source="https://datadog-docs.imgix.net/images/containers/remediation/side_panel2.96321e60f3644b81816ae4a774ebba36.png?auto=format"
   alt="Remediation side panel opened for a workload with a CrashLoopBackOff error. Displays a What Happened section with a Bits AI-powered explanation of the error's root cause. Below, a Recommended Next Steps section where the user can inspect the workload manifest. Step-by-step instructions for a suggested fix are also displayed." /%}

### Remediate from Datadog{% #remediate-from-datadog %}

{% callout %}
##### Join the Preview!

Automated fixes from Bits AI Kubernetes Remediation is in Preview. To sign up, click **Request Access** and complete the form.

[Request Access](https://www.datadoghq.com/product-preview/kubernetes-remediation/)
{% /callout %}

If your repositories are [connected to Datadog](https://docs.datadoghq.com/integrations/guide/source-code-integration/?tab=githubsaasonprem#connect-your-git-repositories-to-datadog), and an error can be fixed by changing code in one of these connected repositories, then you can use Bits AI to perform the remediation action directly from Datadog. For other problem scenarios, Bits AI provides a detailed list of remediation steps to follow.

{% collapsible-section open=null #example-pr %}
#### Example: Increasing memory limit for a deployment

{% video
   url="https://datadog-docs.imgix.net/images/containers/remediation/bitsai_action2.mp4" /%}

When a pod is terminated because the memory usage exceeded its limit, you may be able to fix the error by increasing your container's memory limit.

1. Click **Edit Memory Limit**.
1. Adjust your limit so that it is higher than what your container normally uses.
1. Click **Fix with Bits AI**.
1. On the next page, select the repository where your deployment is defined, and review the proposed changes. Click **Fix with Bits** to create a pull request.
1. You are redirected to a Bits [Code Session](https://app.datadoghq.com/code?tab=my-sessions), where you can verify that the Bits AI Dev Agent identified the specific configuration file where your memory limits are defined. Click **Create Pull Request** to initiate the creation of the pull request.
1. Click **View Pull Request** to view the pull request in GitHub.

{% /collapsible-section %}

## Further reading{% #further-reading %}

- [Accelerate Kubernetes issue resolution with AI-powered guided remediation](https://www.datadoghq.com/blog/kubernetes-active-remediation-ai/)
