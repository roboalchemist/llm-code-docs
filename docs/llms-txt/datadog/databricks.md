# Source: https://docs.datadoghq.com/data_observability/quality_monitoring/data_warehouses/databricks.md

# Source: https://docs.datadoghq.com/data_observability/jobs_monitoring/databricks.md

---
title: 'Enable Data Observability: Jobs Monitoring for Databricks'
description: >-
  Enable Data Observability: Jobs Monitoring for Databricks workspaces with
  OAuth or Personal Access Token authentication and Datadog Agent installation.
breadcrumbs: >-
  Docs > Data Observability Overview > Data Observability: Jobs Monitoring >
  Enable Data Observability: Jobs Monitoring for Databricks
---

# Enable Data Observability: Jobs Monitoring for Databricks

[Data Observability: Jobs Monitoring](https://docs.datadoghq.com/data_jobs) gives visibility into the performance and reliability of your Databricks jobs and workflows running on clusters or serverless compute.

## Setup{% #setup %}

{% alert level="info" %}
[Databricks Networking Restrictions](https://docs.databricks.com/en/security/network/front-end/index.html) can block some Datadog functions. Add the following Datadog IP ranges to your allow-list: webhook IPs, API IPs.
{% /alert %}

Follow these steps to enable Data Observability: Jobs Monitoring for Databricks.

1. Configure the Datadog-Databricks integration for a Databricks workspace.
1. Install the Datadog Agent on your Databricks cluster(s) in the workspace.

### Configure the Datadog-Databricks integration{% #configure-the-datadog-databricks-integration %}

{% tab title="Use a Service Principal for OAuth" %}

{% alert level="danger" %}
New workspaces must authenticate using OAuth. Workspaces integrated with a Personal Access Token continue to function and can switch to OAuth at any time. After a workspace starts using OAuth, it cannot revert to a Personal Access Token.
{% /alert %}

1. In your Databricks account, click on **User Management** in the left menu. Then, under the **Service principals** tab, click **Add service principal**.

1. Under the **Credentials & secrets** tab, click **Generate secret**. Set **Lifetime (days)** to the maximum value allowed (730), then click **Generate**. Take note of your client ID and client secret. Also take note of your account ID, which can be found by clicking on your profile in the upper-right corner.

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/databricks/client-id-secret.4386b391182410f9592d6fc2a427c049.png?auto=format"
      alt="In Databricks, a modal showing the client ID and secret associated with a new OAuth secret is displayed." /%}

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/databricks/account-id.c45907baaf6016db52c9498c64023ae7.png?auto=format"
      alt="In Databricks, a drop-down menu showing the user's account ID is displayed." /%}

1. Click **Workspaces** in the left menu, then select the name of your workspace.

1. Go to the **Permissions** tab and click **Add permissions**.

1. Search for the service principal you created and assign it the **Admin** permission.

1. In Datadog, open the Databricks integration tile.

1. On the **Configure** tab, click **Add Databricks Workspace**.

1. Enter a workspace name, your Databricks workspace URL, account ID, and the client ID and secret you generated.

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/databricks/configure-workspace-form-m2m.bec7fde2d9849f57a2de658e4c837e91.png?auto=format"
      alt="In the Datadog-Databricks integration tile, a Databricks workspace is displayed. This workspace has a name, URL, account ID, client ID, and client secret." /%}

1. To gain visibility into your Databricks costs in Data Observability: Jobs Monitoring or [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management/), provide the ID of a [Databricks SQL Warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/) that Datadog can use to query your [system tables](https://docs.databricks.com/aws/en/admin/system-tables/).

   - The service principal must have access to the SQL Warehouse. In the Warehouse configuration page, go to **Permissions** (top right) and grant it `CAN USE` permission.
   - Grant the service principal read access to the Unity Catalog [system tables](https://docs.databricks.com/aws/en/admin/system-tables/) by running the following commands:

   ```sql
   GRANT USE CATALOG ON CATALOG system TO <service_principal>;
   GRANT SELECT ON CATALOG system TO <service_principal>;
   GRANT USE SCHEMA ON CATALOG system TO <service_principal>;
   ```

The user granting these must have `MANAGE` privilege on `CATALOG system`.

   - The SQL Warehouse must be Pro or Serverless. Classic Warehouses are **NOT** supported. A 2XS warehouse is recommended, with Auto Stop set to 5-10 minutes to reduce cost.

1. In the **Select products to set up integration** section, ensure that Data Observability: Jobs Monitoring is **Enabled**.

1. In the **Datadog Agent Setup** section, choose either

   - Managed by Datadog (recommended): Datadog installs and manages the Agent with a global init script in the workspace.
   - Manually: Follow the instructions below to install and manage the init script for installing the Agent globally or on specific Databricks clusters.

{% /tab %}

{% tab title="Use a Personal Access Token (Legacy)" %}

{% alert level="danger" %}
This option is only available for workspaces created before July 7, 2025. New workspaces must authenticate using OAuth.
{% /alert %}

1. In your Databricks workspace, click on your profile in the top right corner and go to **Settings**. Select **Developer** in the left side bar. Next to **Access tokens**, click **Manage**.

1. Click **Generate new token**, enter "Datadog Integration" in the **Comment** field, set the **Lifetime (days)** value to the maximum allowed (730 days), and create a reminder to update the token before it expires. Then click **Generate**. Take note of your token.

**Important:**

   - For the Datadog managed init script install (recommended), ensure the token's Principal is a **Workspace Admin**.
   - For manual init script installation, ensure the token's Principal has [CAN VIEW access](https://docs.databricks.com/en/security/auth-authz/access-control/index.html#job-acls) for the Databricks jobs and clusters you want to monitor.

As an alternative, follow the [official Databricks documentation](https://docs.databricks.com/en/admin/users-groups/service-principals.html#manage-personal-access-tokens-for-a-service-principal) to generate an access token for a [service principal](https://docs.databricks.com/en/admin/users-groups/service-principals.html#what-is-a-service-principal). The service principal must have the [**Workspace access** entitlement](https://docs.databricks.com/aws/en/security/auth/entitlements#entitlements-overview) enabled and the **Workspace Admin** or [CAN VIEW access](https://docs.databricks.com/en/security/auth-authz/access-control/index.html#job-acls) permissions as described above.

1. In Datadog, open the Databricks integration tile.

1. On the **Configure** tab, click **Add Databricks Workspace**.

1. Enter a workspace name, your Databricks workspace URL, and the Databricks token you generated.

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/databricks/configure-workspace-form.4a5539259a81167b92e06f066d8447d4.png?auto=format"
      alt="In the Datadog-Databricks integration tile, a Databricks workspace is displayed. This workspace has a name, URL, and API token." /%}

1. To gain visibility into your Databricks costs in Data Observability: Jobs Monitoring or [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management), provide the ID of a [Databricks SQL Warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/) that Datadog can use to query your [system tables](https://docs.databricks.com/aws/en/admin/system-tables/).

   - The token's principal must have access to the SQL Warehouse. Give it `CAN USE` permission from **Permissions** at the top right of the Warehouse configuration page.
   - Grant the service principal read access to the Unity Catalog [system tables](https://docs.databricks.com/aws/en/admin/system-tables/) by running the following commands::

   ```sql
   GRANT USE CATALOG ON CATALOG system TO <token_principal>;
   GRANT SELECT ON CATALOG system TO <token_principal>;
   GRANT USE SCHEMA ON CATALOG system TO <token_principal>;
   ```

The user granting these must have `MANAGE` privilege on `CATALOG system`.

   - The SQL Warehouse must be Pro or Serverless. Classic Warehouses are **NOT** supported. A 2XS size warehouse is recommended, with Auto Stop configured for 5-10 minutes to minimize cost.

1. In the **Select products to set up integration** section, make sure the Data Observability: Jobs Monitoring product is **Enabled**.

1. In the **Datadog Agent Setup** section, choose either

   - Managed by Datadog (recommended): Datadog installs and manages the Agent with a global init script in the workspace.
   - Manually: Follow the instructions below to install and manage the init script for installing the Agent globally or on specific Databricks clusters.

{% /tab %}

### Install the Datadog Agent{% #install-the-datadog-agent %}

The Datadog Agent must be installed on Databricks clusters to monitor Databricks jobs that run on all-purpose or job clusters. This step is not required to monitor jobs on [serverless compute](https://docs.databricks.com/en/security/secrets/index.html).

{% tab title="Datadog managed global init script (Recommended)" %}
Datadog can install and manage a global init script in the Databricks workspace. The Datadog Agent is installed on all clusters in the workspace, when they start.

{% alert level="danger" %}

- This setup does not work on Databricks clusters in **Standard** access mode, because global init scripts cannot be installed on those clusters. If you are using clusters with the **Standard** access mode, Datadog recommends to Manually configure a cluster policy across multiple clusters or Manually install on a specific cluster.
- This install option, in which Datadog installs and manages your Datadog global init script, requires a Databricks Access Token with **Workspace Admin** permissions. A token with CAN VIEW access does not allow Datadog to manage the global init script of your Databricks account.

{% /alert %}

#### When integrating a workspace with Datadog{% #when-integrating-a-workspace-with-datadog %}

1. In the **Select products to set up integration** section, make sure the Data Observability: Jobs Monitoring product is **Enabled**.

1. In the **Datadog Agent Setup** section, select the **Managed by Datadog** toggle button.

1. Click **Select API Key** to either select an existing Datadog API key or create a new Datadog API key.

1. (Optional) Disable **Enable Log Collection** if you do not want to collect driver and worker logs for correlating with jobs.

1. Click **Save Databricks Workspace**.

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/databricks/configure-data-jobs-monitoring-new-2.e50d0c8a0a8d503ab3b23f2fdcf0a02a.png?auto=format"
      alt="In the Datadog-Databricks integration tile, Datadog Agent Setup when adding a Databricks workspace. Datadog can install and manage a global init script." /%}

#### When adding the init script to a Databricks workspace already integrated with Datadog{% #when-adding-the-init-script-to-a-databricks-workspace-already-integrated-with-datadog %}

1. On the **Configure** tab, click the workspace in the list of workspaces

1. Click the **Configured Products** tab

1. Make sure the Data Observability: Jobs Monitoring product is **Enabled**.

1. In the **Datadog Agent Setup** section, select the **Managed by Datadog** toggle button.

1. Click **Select API Key** to either select an existing Datadog API key or create a new Datadog API key.

1. (Optional) Disable **Enable Log Collection** if you do not want to collect driver and worker logs for correlating with jobs.

1. Click **Save Databricks Workspace** at the bottom of the browser window.

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/databricks/configure-data-jobs-monitoring-existing.020021f82b26a3b84068c1b9a9dfe3f2.png?auto=format"
      alt="In the Datadog-Databricks integration tile, Datadog Agent Setup for a Databricks workspace already added to the integration. Datadog can install and manage a global init script." /%}

Optionally, you can add tags to your Databricks cluster and Spark performance metrics by configuring the following environment variable in the Advanced Configuration section of your cluster in the Databricks UI or as [Spark env vars](https://docs.databricks.com/api/workspace/clusters/edit#spark_env_vars) with the Databricks API:

| Variable                        | Description                                                                                                                                                                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DD_TAGS                         | Add tags to Databricks cluster and Spark performance metrics. Comma or space separated key:value pairs. Follow [Datadog tag conventions](https://docs.datadoghq.com/getting_started/tagging/). Example: `env:staging,team:data_engineering` |
| DD_ENV                          | Set the `env` environment tag on metrics, traces, and logs from this cluster.                                                                                                                                                               |
| DD_LOGS_CONFIG_PROCESSING_RULES | Filter the logs collected with processing rules. See [Advanced Log Collection](https://docs.datadoghq.com/agent/logs/advanced_log_collection/?tab=environmentvariable#global-processing-rules) for more details.                            |

{% /tab %}

{% tab title="Manually configure a cluster policy" %}
This approach is recommended for clusters in **Standard** access mode.

**Create the init script**

1. In Databricks, create an init script file in a [Unity Catalog volume](https://docs.databricks.com/en/connect/unity-catalog/volumes.html) with the following content. Be sure to make note of the volume path (for example, `/Volumes/catalog_name/schema_name/volume_name/datadog-init-script.sh`).

   ```shell
   #!/bin/bash
   
   # Download and run the latest init script
   curl -L https://install.datadoghq.com/scripts/install-databricks.sh > djm-install-script
   bash djm-install-script || true
   ```

The script above downloads and runs the latest init script for Data Observability: Jobs Monitoring in Databricks. If you want to pin your script to a specific version, you can replace the filename in the URL with `install-databricks-0.14.0.sh` to use version `0.14.0`, for example. The source code used to generate this script, and the changes between script versions, can be found on the [Datadog Agent repository](https://github.com/DataDog/datadog-agent/blob/main/pkg/fleet/installer/setup/djm/databricks.go).

1. **Add the init script to the allowlist**: For clusters in **Standard** access mode, you must add the init script path to the Unity Catalog allowlist. Follow the instructions in the [Databricks documentation](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/allowlist#how-to-add-items-to-the-allowlist) to add your init script path to the allowlist.

**Configure the compute policy**

1. In **Compute**, navigate to the **Policies** tab. If you already have a cluster policy applied to your clusters, navigate to that existing policy to edit it. This is the simpler approach as the policy automatically applies to all clusters using it. Otherwise, click **Create Policy** to create a new policy.

1. To add the init script to the cluster policy, in the **Definition** section, click **Add Definition**. In the modal that opens, fill in the fields:

   1. In the **Field** dropdown, select **init\_scripts**.
   1. In the **Source** dropdown, select **Volume**.
   1. Under **Destination**, enter the volume path to your init script.
   1. Click **Add**.

1. Configure the environment variables. You must add each of the following environment variables to the cluster policy you created:

| Key                  | Description                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| DD_API_KEY           | Your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).                                                                                              |
| DD_SITE              | Your [Datadog site](https://docs.datadoghq.com/getting_started/site/).                                                                                                         |
| DATABRICKS_WORKSPACE | Name of your Databricks Workspace. It should match the name provided in the Datadog-Databricks integration step. Enclose the name in double quotes if it contains whitespaces. |

   1. For each of the above variables, in the **Definition** section, click **Add Definition**. In the modal that opens, fill in the fields:
      1. In the **Field** dropdown, select **spark\_env\_vars**.
      1. In the **Key** field, enter the environment variable key.
      1. In the **Value** field, enter the environment variable value.
      1. Under the **Type** drop-down, select `Fixed`.
      1. Check the **Hidden** checkbox to reduce exposure of sensitive values.
   1. Optionally, set other init script parameters and Datadog environment variables, such as `DD_ENV` and `DD_SERVICE`. You can configure the script using the following parameters:
| Variable                        | Description                                                                                                                                                                                                                                        | Default |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| DRIVER_LOGS_ENABLED             | Collect spark driver logs in Datadog.                                                                                                                                                                                                              | false   |
| WORKER_LOGS_ENABLED             | Collect spark workers logs in Datadog.                                                                                                                                                                                                             | false   |
| DD_TAGS                         | Add tags to Databricks cluster and Spark performance metrics, using comma- or space-separated key:value pairs. Follow [Datadog tag conventions](https://docs.datadoghq.com/getting_started/tagging/). Example: `env:staging,team:data_engineering` |
| DD_ENV                          | Set the `env` environment tag on metrics, traces, and logs from this cluster.                                                                                                                                                                      |
| DD_LOGS_CONFIG_PROCESSING_RULES | Filter the logs collected with processing rules. See [Advanced Log Collection](https://docs.datadoghq.com/agent/logs/advanced_log_collection/?tab=environmentvariable#global-processing-rules) for more details.                                   |

1. Click **Create** if creating a new policy or **Save** if updating an existing policy. If you update an existing policy, all clusters using that policy automatically apply the changes on their next restart. If you create a new policy, follow the steps below to apply it to your clusters.

**Apply the cluster policy to clusters**

1. In **Compute**, select the cluster you want to update or click **Create Compute** for a new cluster.
1. In the **Policy** dropdown at the top, select the policy you created.
1. Click **Confirm** to save the changes. The cluster needs to be restarted for the policy to take effect.

{% /tab %}

{% tab title="Manually install a global init script" %}

{% alert level="danger" %}
This setup does not work on Databricks clusters in **Standard** access mode, because global init scripts cannot be installed on those clusters. If you are using clusters with the **Standard** access mode, Datadog recommends to Manually configure a cluster policy or Manually install on a specific cluster.
{% /alert %}

1. In Databricks, click your display name (email address) in the upper right corner of the page.

1. Select **Settings** and click the **Compute** tab.

1. In the **All purpose clusters** section, next to **Global init scripts**, click **Manage**.

1. Click **Add**. Name your script. Then, in the **Script** field, copy and paste the following script, remembering to replace the placeholders with your parameter values.

   ```shell
   #!/bin/bash
   
   # Required parameters
   export DD_API_KEY=<YOUR API KEY>
   export DD_SITE=<YOUR DATADOG SITE>
   export DATABRICKS_WORKSPACE="<YOUR WORKSPACE NAME>"
   
   # Download and run the latest init script
   curl -L https://install.datadoghq.com/scripts/install-databricks.sh > djm-install-script
   bash djm-install-script || true
   ```

The script above sets the required parameters, and downloads and runs the latest init script for Data Observability: Jobs Monitoring in Databricks. If you want to pin your script to a specific version, you can replace the filename in the URL with `install-databricks-0.14.0.sh` to use version `0.14.0`, for example. The source code used to generate this script, and the changes between script versions, can be found on the [Datadog Agent repository](https://github.com/DataDog/datadog-agent/blob/main/pkg/fleet/installer/setup/djm/databricks.go).

1. To enable the script for all new and restarted clusters, toggle **Enabled**.

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/databricks/toggle.5eb3edcf35da5e86187d080c35d0b100.png?auto=format"
      alt="Databricks UI, admin settings, global init scripts. A script called 'install-datadog-agent' is in a list with an enabled toggle." /%}

1. Click **Add**.

#### Set the required init script parameters{% #set-the-required-init-script-parameters %}

Provide the values for the init script parameters at the beginning of the global init script.

```bash
export DD_API_KEY=<YOUR API KEY>
export DD_SITE=<YOUR DATADOG SITE>
export DATABRICKS_WORKSPACE="<YOUR WORKSPACE NAME>"
```

Optionally, you can also set other init script parameters and Datadog environment variables here, such as `DD_ENV` and `DD_SERVICE`. The script can be configured using the following parameters:

| Variable                        | Description                                                                                                                                                                                                                                 | Default |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| DD_API_KEY                      | Your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).                                                                                                                                                           |
| DD_SITE                         | Your [Datadog site](https://docs.datadoghq.com/getting_started/site/).                                                                                                                                                                      |
| DATABRICKS_WORKSPACE            | Name of your Databricks Workspace. It should match the name provided in the Datadog-Databricks integration step. Enclose the name in double quotes if it contains whitespace.                                                               |
| DRIVER_LOGS_ENABLED             | Collect spark driver logs in Datadog.                                                                                                                                                                                                       | false   |
| WORKER_LOGS_ENABLED             | Collect spark workers logs in Datadog.                                                                                                                                                                                                      | false   |
| DD_TAGS                         | Add tags to Databricks cluster and Spark performance metrics. Comma or space separated key:value pairs. Follow [Datadog tag conventions](https://docs.datadoghq.com/getting_started/tagging/). Example: `env:staging,team:data_engineering` |
| DD_ENV                          | Set the `env` environment tag on metrics, traces, and logs from this cluster.                                                                                                                                                               |
| DD_LOGS_CONFIG_PROCESSING_RULES | Filter the logs collected with processing rules. See [Advanced Log Collection](https://docs.datadoghq.com/agent/logs/advanced_log_collection/?tab=environmentvariable#global-processing-rules) for more details.                            |

{% /tab %}

{% tab title="Manually install on a specific cluster" %}

1. In Databricks, create an init script file in a [Unity Catalog volume](https://docs.databricks.com/en/connect/unity-catalog/volumes.html) with the following content. Be sure to make note of the volume path (for example, `/Volumes/catalog_name/schema_name/volume_name/datadog-init-script.sh`).

   ```shell
   #!/bin/bash
   
   # Download and run the latest init script
   curl -L https://install.datadoghq.com/scripts/install-databricks.sh > djm-install-script
   bash djm-install-script || true
   ```

The script above downloads and runs the latest init script for Data Observability: Jobs Monitoring in Databricks. If you want to pin your script to a specific version, you can replace the filename in the URL (for example, `install-databricks-0.14.0.sh` to use version `0.14.0`). You can find the source code used to generate this script, and the changes between script versions, on the [Datadog Agent repository](https://github.com/DataDog/datadog-agent/blob/main/pkg/fleet/installer/setup/djm/databricks.go).

1. **Add the init script to the allowlist** (required for **Standard** access mode clusters): If your cluster uses **Standard** access mode, you must add the init script path to the Unity Catalog allowlist. Follow the instructions in the [Databricks documentation](https://docs.databricks.com/en/data-governance/unity-catalog/manage-privileges/allowlist#how-to-add-items-to-the-allowlist) to add your init script path to the allowlist.

1. On the cluster configuration page, click the **Advanced options** toggle.

1. At the bottom of the page, go to the **Init Scripts** tab.

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/databricks/init_scripts.6d7363a6b42e56498486e96d6d205376.png?auto=format"
      alt="Databricks UI, cluster configuration advanced options,  Init Scripts tab. A 'Destination' drop-down and an 'Init script path' file selector." /%}

   - Under the **Destination** drop-down, select `Volume`.
   - Under **Init script path**, enter the volume path to your init script.
   - Click **Add**.

#### Set the required init script parameters{% #set-the-required-init-script-parameters %}

1. In Databricks, on the cluster configuration page, click the **Advanced options** toggle.

1. At the bottom of the page, go to the **Spark** tab.

   {% image
      source="https://datadog-docs.imgix.net/images/data_jobs/databricks/configure-databricks-cluster-init-script-quoted.1b795a8010bd230e937cdbad9f7ff73d.png?auto=format"
      alt="Databricks UI, cluster configuration advanced options, Spark tab. A textbox titled 'Environment variables' contains values for DD_API_KEY and DD_SITE." /%}

In the **Environment variables** textbox, provide the values for the init script parameters.

   ```text
   DD_API_KEY=<YOUR API KEY>
   DD_SITE=<YOUR DATADOG SITE>
   DATABRICKS_WORKSPACE="<YOUR WORKSPACE NAME>"
   ```

Optionally, you can also set other init script parameters and Datadog environment variables here, such as `DD_ENV` and `DD_SERVICE`. The script can be configured using the following parameters:

| Variable                        | Description                                                                                                                                                                                                                                 | Default |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| DD_API_KEY                      | Your [Datadog API key](https://app.datadoghq.com/organization-settings/api-keys).                                                                                                                                                           |
| DD_SITE                         | Your [Datadog site](https://docs.datadoghq.com/getting_started/site/).                                                                                                                                                                      |
| DATABRICKS_WORKSPACE            | Name of your Databricks Workspace. It should match the name provided in the Datadog-Databricks integration step. Enclose the name in double quotes if it contains whitespace.                                                               |
| DRIVER_LOGS_ENABLED             | Collect spark driver logs in Datadog.                                                                                                                                                                                                       | false   |
| WORKER_LOGS_ENABLED             | Collect spark workers logs in Datadog.                                                                                                                                                                                                      | false   |
| DD_TAGS                         | Add tags to Databricks cluster and Spark performance metrics. Comma or space separated key:value pairs. Follow [Datadog tag conventions](https://docs.datadoghq.com/getting_started/tagging/). Example: `env:staging,team:data_engineering` |
| DD_ENV                          | Set the `env` environment tag on metrics, traces, and logs from this cluster.                                                                                                                                                               |
| DD_LOGS_CONFIG_PROCESSING_RULES | Filter the logs collected with processing rules. See [Advanced Log Collection](https://docs.datadoghq.com/agent/logs/advanced_log_collection/?tab=environmentvariable#global-processing-rules) for more details.                            |
Click **Confirm**.
{% /tab %}

### Restart already-running clusters{% #restart-already-running-clusters %}

The init script installs the Agent when clusters start.

Already-running all-purpose clusters or long-lived job clusters must be manually restarted for the init script to install the Datadog Agent.

For scheduled jobs that run on job clusters, the init script installs the Datadog Agent automatically on the next run.

## Validation{% #validation %}

In Datadog, view the [Data Observability: Jobs Monitoring](https://app.datadoghq.com/data-jobs/) page to see a list of all your Databricks jobs.

If some jobs are not visible, navigate to the [Configuration](https://app.datadoghq.com/data-jobs/configuration) page to understand why. This page lists all your Databricks jobs not yet configured with the Agent on their clusters, along with guidance for completing setup.

## Troubleshooting{% #troubleshooting %}

If you don't see any data in DJM after installing the product, follow these steps.

1. **API Key Validation:** If the init script was manually installed, but cluster data still isn't showing up in the DJM product, use the [Validate API key endpoint](https://docs.datadoghq.com/api/latest/authentication/?code-lang=curl#validate-api-key) to ensure that the Datadog API key specified in the script is valid.
1. **Agent Validation:** The init script installs the Datadog Agent. To make sure it is properly installed, connect to the cluster with SSH and run the Agent status command:

```shell
sudo datadog-agent status
```

## Advanced Configuration{% #advanced-configuration %}

### Filter log collection on clusters{% #filter-log-collection-on-clusters %}

#### Exclude all log collection from an individual cluster{% #exclude-all-log-collection-from-an-individual-cluster %}

Configure the following environment variable in the Advanced Configuration section of your cluster in the Databricks UI or as a [Spark environment variable](https://docs.databricks.com/api/workspace/clusters/edit#spark_env_vars) in the Databricks API.

```bash
DD_LOGS_CONFIG_PROCESSING_RULES=[{\"type\": \"exclude_at_match\",\"name\": \"drop_all_logs\",\"pattern\": \".*\"}]
```

### Permissions{% #permissions %}

Grant **Workspace Admin** privileges to the user or service principal that connects to your Databricks workspace. This allows Datadog to manage init script installations and updates automatically, reducing the risk of misconfiguration.

If you need more granular control, grant these minimal permissions to the following [workspace level objects](https://docs.databricks.com/aws/en/security/auth/access-control#access-control-lists-overview) to still be able to monitor all jobs, clusters, and queries within a workspace:

| Object                         | Permission                                                                                                      |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Job                            | [CAN VIEW](https://docs.databricks.com/aws/en/security/auth/access-control#job-acls)                            |
| Compute                        | [CAN ATTACH TO](https://docs.databricks.com/aws/en/security/auth/access-control#compute-acls)                   |
| Lakeflow Declarative Pipelines | [CAN VIEW](https://docs.databricks.com/aws/en/security/auth/access-control#lakeflow-declarative-pipelines-acls) |
| Query                          | [CAN VIEW](https://docs.databricks.com/aws/en/security/auth/access-control#query-acls)                          |
| SQL warehouse                  | [CAN MONITOR](https://docs.databricks.com/aws/en/security/auth/access-control#sql-warehouse-acls)               |

Additionally, for Datadog to access your Databricks cost data in Data Observability: Jobs Monitoring or [Cloud Cost Management](https://docs.datadoghq.com/cloud_cost_management), the user or service principal used to query [system tables](https://docs.databricks.com/aws/en/admin/system-tables/) must have the following permissions:

- `CAN USE` permission on the SQL Warehouse.
- Read access to the [system tables](https://docs.databricks.com/aws/en/admin/system-tables/) within Unity Catalog. This can be granted with:

```sql
GRANT USE CATALOG ON CATALOG system TO <service_principal>;
GRANT SELECT ON CATALOG system TO <service_principal>;
GRANT USE SCHEMA ON CATALOG system TO <service_principal>;
```

The user granting these must have `MANAGE` privilege on `CATALOG system`.

### Tag spans at runtime{% #tag-spans-at-runtime %}

You can set tags on Spark spans at runtime. These tags are applied *only* to spans that start after the tag is added.

```scala
// Add tag for all next Spark computations
sparkContext.setLocalProperty("spark.datadog.tags.key", "value")
spark.read.parquet(...)
```

To remove a runtime tag:

```scala
// Remove tag for all next Spark computations
sparkContext.setLocalProperty("spark.datadog.tags.key", null)
```

### Aggregate cluster metrics from one-time job runs{% #aggregate-cluster-metrics-from-one-time-job-runs %}

This configuration is applicable if you want cluster resource utilization data about your jobs and create a new job and cluster for each run via the [one-time run API endpoint](https://docs.databricks.com/api/workspace/jobs/submit) (common when using orchestration tools outside of Databricks such as Airflow or Azure Data Factory).

If you are submitting Databricks Jobs through the [one-time run API endpoint](https://docs.databricks.com/api/workspace/jobs/submit), each job run has a unique job ID. This can make it difficult to group and analyze cluster metrics for jobs that use ephemeral clusters. To aggregate cluster utilization from the same job and assess performance across multiple runs, you must set the `DD_JOB_NAME` variable inside the `spark_env_vars` of every `new_cluster` to the same value as your request payload's `run_name`.

Here's an example of a one-time job run request body:

```json
{
   "run_name": "Example Job",
   "idempotency_token": "8f018174-4792-40d5-bcbc-3e6a527352c8",
   "tasks": [
      {
         "task_key": "Example Task",
         "description": "Description of task",
         "depends_on": [],
         "notebook_task": {
            "notebook_path": "/Path/to/example/task/notebook",
            "source": "WORKSPACE"
         },
         "new_cluster": {
            "num_workers": 1,
            "spark_version": "13.3.x-scala2.12",
            "node_type_id": "i3.xlarge",
            "spark_env_vars": {
               "DD_JOB_NAME": "Example Job"
            }
         }
      }
   ]
}
```

### Set up Data Observability: Jobs Monitoring with Databricks Networking Restrictions{% #set-up-data-observability-jobs-monitoring-with-databricks-networking-restrictions %}

With [Databricks Networking Restrictions](https://docs.databricks.com/en/security/network/front-end/index.html), Datadog may not have access to your Databricks APIs, which is required to collect traces for Databricks job executions along with tags and other metadata.

If you are controlling Databricks API access with [IP access lists](https://docs.databricks.com/en/security/network/front-end/ip-access-list.html), allow-listing Datadog's specific webhook IP addresses allows Datadog to connect to the Databricks APIs in your workspaces/account. See Databricks's documentation for configuring IP access lists for [individual workspaces](https://docs.databricks.com/en/security/network/front-end/ip-access-list-workspace) and the [account console](https://docs.databricks.com/aws/en/security/network/front-end/ip-access-list-account) to give Datadog API access. Updating the IP access lists **at both the workspace and account level is required** for the Databricks integration. **Note:** Datadog only uses Databricks account-level APIs to automatically refresh your service principal's client secret.

**Note**: Monitoring workspaces that use [Databricks Private Link](https://www.databricks.com/trust/security-features/secure-your-data-with-private-networking) connectivity is not supported.

## Further Reading{% #further-reading %}

- [Data Observability: Jobs Monitoring](https://docs.datadoghq.com/data_jobs)
- [Detect issues and optimize spend with Databricks serverless job monitoring](https://www.datadoghq.com/blog/databricks-serverless-jobs-datadog/)
