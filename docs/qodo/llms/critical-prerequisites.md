# Source: https://docs.qodo.ai/qodo-documentation/on-prem/qodo-on-premise/critical-prerequisites.md

# Critical Prerequisites

#### Container Registry Access (Replicated)

**IMPORTANT**: All Qodo on-premises deployments require credentials to access container images through Replicated:

* **Image Registry**: `artifacts-self-hosted.qodo.ai` and `artif-reg-self-hosted.codium.ai`
* **Authentication Required**: You must have credentials provided by Qodo
* **Login Command**:

{% code overflow="wrap" expandable="true" %}

```bash
  helm registry login artifacts-self-hosted.qodo.ai --username $provided_user --password $provided_password
```

{% endcode %}

**Before starting any installation, ensure you have received your Replicated credentials from Qodo.**
