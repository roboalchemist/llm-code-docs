# Source: https://docs.qodo.ai/qodo-documentation/on-prem/ide-plugin/install-qodo-agentic-mode.md

# Install Qodo Agentic Mode

This document provides step-by-step instructions for On Prem customers to install and configure Agentic Mode in their backend infrastructure.&#x20;

[Learn more about Agentic Mode](https://docs.qodo.ai/qodo-documentation/qodo-gen/qodo-gen-chat/agentic-mode).

#### Administrator-Only Configuration

The installation and configuration process in this manual should be performed by s**ystem administrators only**.

### Requirements

Before proceeding with the installation, ensure the following prerequisites are met:

#### Database

Postgres v17+ must be deployed. Managed cloud solutions like **AWS RDS** or **GCP CloudSQL** are recommended.

The database should follow a few minimum specifications:

* 2 vCPU
* 16 GB of memory
* 50 GB of disk space
* Accessible from the EC2 instance running the Qodo stack

**If you’re using a public cloud**, managed solutions like GCP CloudSQL and AWS RDS are recommended.

#### Qodo stack version

Ensure Qodo Stack version is at least 0.1.300.

#### **Helm installation**

Ensure Helm is installed for managing Kubernetes deployments.

**Embedded Cluster (Optional)**: If Kubernetes is not available, installation can be performed using Replicated (web UI-based deployment).

### Configuration Details for Helm users

#### Environment Variables

* The primary configuration file is `/copilot_proxy/settings_prod/.secrets.toml`.
* The file is a Kubernetes secret that must be appended to.

#### Required Installations

* In addition to setting values, users must enable cronjobs and jobs in the Helm chart.
* The following command ensures all necessary jobs are scheduled:

```
kubectl apply -f cronjobs.yaml
```

## Installation steps for Helm users

#### 1. Database Setup

Deploy a Postgres v17+ database and configure it with the required credentials.

**Example Configuration:**

```
[agenticdb]
username=<your-username>
password=<your-password>
host=<your-db-host>
port=5432
db_name="agentic"
```

* If using a public cloud, managed solutions like AWS RDS, GCP CloudSQL or Azure SQL are recommended.

#### 2. Update Helm Values

Modify the Helm values file to include the necessary configurations for Agentic Mode:

```
jobs:
  db-migration:
    annotations:
      "helm.sh/hook": pre-install,pre-upgrade
      "helm.sh/hook-delete-policy": before-hook-creation,hook-succeeded
    command:
      - python
      - -m
      - alembic
      - upgrade
      - head
  db-partition-create-init:
    backoffLimit: 10
    activeDeadlineSeconds: 3600
    annotations:
      helm.sh/hook: post-install,post-upgrade
      helm.sh/hook-weight: "-4"
      helm.sh/hook-delete-policy: hook-succeeded
    command:
      - python
      - /copilot_proxy/db/partitoning/partition_script.py
cronJobs:
  db-partition-delete:
    backoffLimit: 10
    activeDeadlineSeconds: 3600
    concurrencyPolicy: Forbid
    schedule: "0 1 * * *"
    command:
      - /bin/sh
      - -c
      - "PYTHONPATH=/copilot_proxy:/ragger/indexing:/ python /copilot_proxy/db/partitoning/cleanup_script.py"
  db-partition-create:
    concurrencyPolicy: Forbid
    schedule: "0 1 * * *"
    command:
      - python
      - /copilot_proxy/db/partitoning/partition_script.py
```

#### 3. Run Helm Upgrade

Apply the updated Helm values by running:

```jsx
helm upgrade qodo-gen oci://artifacts-self-hosted.qodo.ai/codium-stack/stable/module -f ./values.yaml
```

This will run database migrations and create the necessary partitions.

#### 4. Update Secrets

Modify the Kubernetes secret file `/copilot_proxy/settings_prod/.secrets.toml` to include:

```toml
[agenticdb] # Agentic DB details
username=$USERNAME
password=$PWD
host=$HOST
port="5432"
db_name="agentic"

[app] # Feature flags
agentic_support = true    # Enable Agentic mode
lean_agent_enabled = true # Enable lean agent for smoother, more flexible development workflows.
custom_mcp_enabled = true # Enable Agentic Tools (MCPs)
apply_flow_on = true
test_flow_on = true

/copilot_proxy/settings/settings.toml (default settings in the image)
[app]
apply_flow_on = false
test_flow_on = false
agentic_support = false
custom_mcp_enabled = false
langgraph_checkpointer="postgres"
```

Ensure the pods pick up the new version of the secret.

You can also pass over these secrets as environemt variables:

```bash
APP.AGENTIC_SUPPORT=true
APP.LEAN_AGENT_ENABLED=true
```

#### Configuration Sections Explained

* **\[app]**: Defines feature flags.
* **\[agenticdb]**: Contains Agentic DB details.

#### 5. Verify Agentic Mode

Restart your IDE and verify that Agentic Mode is enabled.

## Installation steps for Embedded Cluster users

For customers without Kubernetes, use Replicated to install Agentic Mode on a virtual machine.

#### Steps

1. **Enable the Agentic Mode license flag:** Notify the Qodo team to enable the license flag.
2. **Sync license:** Once confirmed, sync the license in the Admin web UI.
3. In the Admin web UI, navigate to the **Config** tab.

<figure><img src="https://639223961-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJPQ5Hacyry184nXtoJN4%2Fuploads%2FntwQ6Z4kPys4FbEbPxD1%2Fconfigtab.png?alt=media&#x26;token=4b06736b-2997-4e24-bbba-2b9fb4148a0f" alt="" width="563"><figcaption></figcaption></figure>

4. **Enable Agentic Mode within Qodo Gen:** In the **Qodo Gen Settings** section, enable Agentic Mode.
5. **Update secret:** Append to the end of Qodo Gen secret `toml` file:

```
[agenticdb]
username=<your-username>
password=<your-password>
host=<your-db-host>
port=5432
db_name="agentic"

```

6. **Ensure the configuration was updated**: ensure the popup `The config for Qodo stack has been updated.` appears, then click **Go to updated version**.
7. **Deploy the updated configuration**: in the **Version history** tab you’ve been forwarded to, find the **Config change** entry in the top of the versions list. Click **Deploy**.

<figure><img src="https://639223961-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJPQ5Hacyry184nXtoJN4%2Fuploads%2FkFlo7WypUhD2xvo4bpfs%2Fdeployupdatedconfig.png?alt=media&#x26;token=944cf56d-6955-4d13-ba8a-fcb91dfc54de" alt="" width="563"><figcaption></figcaption></figure>

8. **Wait for a pod to start**: Changing the secret causes the container restart. Wait until it fully starts up.
9. **Restart and start using Agentic Mode:** Restart your IDE. You should be able to use Agentic Mode in your IDE.

For further details, refer to the [official documentation](https://docs.qodo.ai/qodo-documentation/qodo-gen/qodo-gen-chat/agentic-mode).
