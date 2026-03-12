# Source: https://docs.pentaho.com/pdc-admin/ldc-advanced-configuration-ut_cp.md

# Advanced configuration

After [installing Data Catalog](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/), you may need to set up additional components, depending on your environment. Use the following topics as needed to finish setting up your environment.

## Configure system environment variables

Although not common, there might be instances where you need to change the default settings for Data Catalog system environment variables. These configuration modifications allow you to override default system behavior to align with the specific needs.

{% hint style="danger" %}
Modifying these settings can have system-wide implications, and incorrect changes might negatively impact the functionality of the other platforms. It is a best practice to collaborate with your Pentaho Data Catalog partner to ensure that any modifications align with the intended objectives.
{% endhint %}

1. In a terminal window, navigate to the `pdc-docker-deployment` folder and open the hidden environment variable configuration file (`.env`). This file is located in the `/opt` folder by default.
2. Verify the system environment variables set in the `/opt/pentaho/pdc-docker-deployment/vendor/.env.default` file:
   * For example, the number of worker instances that Data Catalog uses to run processes is set to 5:

     ```
     PDC_WS_DEFAULT_OPS_JOBPOOLMINSIZE=5
     PDC_WS_DEFAULT_OPS_JOBPOOLMAXSIZE=5
     ```

     **Note:** Make sure that `PDC_WS_DEFAULT_OPS_JOBPOOLMINSIZE` and `PDC_WS_DEFAULT_OPS_JOBPOOLMAXSIZE` have the same value for consistent worker instance management.
3. To override an environment variable set in the `vendor/.env.default` file, you can create a new `.env` file in the `opt/pentaho/pdc-docker-deployment/conf/` folder:

   `vi opt/pentaho/pdc-docker-deployment/conf/.env`
4. (Optional) The data in the Business Intelligence Database refreshes daily by default, as set in the `.env` file. To modify the data refresh frequency, update the variable in the .env file to one of the options listed in the following table:

<table><thead><tr><th width="216.22222900390625">Value</th><th>Description</th></tr></thead><tbody><tr><td><code>@yearly (or @annually)</code></td><td>Run once a year, midnight, Jan 1st</td></tr><tr><td><code>@monthly</code></td><td>Run once a month, midnight, first of the month</td></tr><tr><td><code>@weekly</code></td><td>Run once a week, midnight between Sat/Sun</td></tr><tr><td><code>@daily (or @midnight)</code></td><td>Run once a day, midnight</td></tr><tr><td><code>@hourly</code></td><td>Run once an hour, the beginning of the hour</td></tr><tr><td><code>@every &#x3C;number>m</code></td><td>Run at a custom interval, where <code>&#x3C;number></code> specifies the number of minutes. <br>For example, <code>@every 5m</code> runs the job every 5 minutes.</td></tr></tbody></table>

```
PDC_CRON_BI_VIEWS_INIT_SCHEDULE=@daily
```

5. After adding all required system variables, save the changes and restart the Data Catalog system services.

   ```
   ./pdc.sh stop
   ./pdc.sh up
   ```

***

## Configure chatbot in Data Catalog

The chatbot in Pentaho Data Catalog enables users to interact with cataloged metadata using natural language queries. The chatbot supports two response modes:

* **Standard (PDO-based) responses**, which retrieve structured metadata from the Business Intelligence Database (BIDB).
* **Conversational responses**, which use vector embeddings stored in Qdrant and a configured large language model (LLM) to provide contextual, semantic answers.

Before users can access chatbot capabilities, administrators must configure and validate several backend components. These configurations include enabling the chatbot service, configuring the large language model, populating indexing data stores, and defining role-based access for conversational search.

This section describes how to configure, enable, disable, and manage the chatbot feature in both Docker and Kubernetes (Amazon EKS) deployments.

### **Initial setup for chatbot** <a href="#initial-setup-for-chatbot" id="initial-setup-for-chatbot"></a>

Before users can interact with the chatbot in Data Catalog, administrators must complete several mandatory configuration steps. The chatbot depends on a large language model (LLM) configuration, metadata indexing, vector embedding generation, and role-based access control to function correctly.

Perform the following steps to complete the initial setup for the chatbot in Data Catalog:

**Prerequisites**

* Pentaho Data Catalog is installed and running.
* OpenSearch is deployed and accessible.
* The chatbot feature is supported in the selected deployment profile.
* You have administrative access to the deployment environment.
* You have valid LLM provider details, including API key, model name, and embedding model.

**Procedure**

1. Enable the chatbot frontend and backend services in your deployment.

   * For Docker deployments, configure the chatbot services in the Docker profile and restart the application.
   * For Kubernetes deployments, enable `chatbot-frontend` and `chatbot-backend` in the active profile YAML file and apply the Helm upgrade.

   For detailed steps, see [#enable-chatbot-in-data-catalog](#enable-chatbot-in-data-catalog "mention").
2. Configure the required LLM and embedding settings:

   * API key
   * LLM model
   * Embedding model
   * Base URL (if applicable)
   * Target vector dimensions
   * Vector indexing schedule

   Ensure that the embedding model and target vector dimensions match.\
   **Important:**\
   You cannot change the embedding model after the initial setup without rebuilding the vector index.\
   For detailed steps, see [#configure-a-large-language-model-llm-for-the-chatbot-in-data-catalog](#configure-a-large-language-model-llm-for-the-chatbot-in-data-catalog "mention").
3. Configure conversational roles to define which user roles are allowed to receive conversational chatbot responses. For detailed steps, see [#configure-data-catalog-user-roles-for-conversational-search-chatbot](#configure-data-catalog-user-roles-for-conversational-search-chatbot "mention").<br>

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Users without the configured roles receive standard (PDO-based) chatbot responses.</p></div>
4. For the chatbot to return responses, the required data stores must be populated. Verify data population and indexing:

   1. For standard (PDO) queries, the Business Intelligence Database (BIDB) must contain indexed metadata.
   2. For conversational queries, the Qdrant vector database must contain generated embeddings.

   Both BIDB and Qdrant indexing processes run as scheduled jobs. By default, these jobs run once per day at midnight. The schedule is configurable. If you encounter any issues, see [#troubleshoot-chatbot-vector-indexing-issues](https://docs.pentaho.com/pdc-admin/pdc-troubleshooting-cp-ag#troubleshoot-chatbot-vector-indexing-issues "mention").
5. Once the configuration is completed, sign in to Data Catalog and verify that:
   * The chatbot icon is visible in the user interface.
   * The chatbot accepts and processes queries.
   * Users with configured conversational roles receive contextual responses.
   * Users without conversational roles receive standard responses.
   * Review backend logs if responses are missing or incomplete.

**Result**

The chatbot is fully configured and operational.

* Standard (PDO) queries return results from BIDB.
* Conversational queries return semantic responses from Qdrant embeddings.
* Indexing runs on schedule and updates incrementally.

The chatbot is now ready for production use.

**What next**

* If responses are incomplete or missing, review the  [#troubleshoot-chatbot-vector-indexing-issues](https://docs.pentaho.com/pdc-admin/pdc-troubleshooting-cp-ag#troubleshoot-chatbot-vector-indexing-issues "mention").
* Monitor indexing logs during initial production deployment.
* Periodically verify indexing schedules and role assignments.

### Enable chatbot in Data Catalog <a href="#enable-chatbot-in-data-catalog" id="enable-chatbot-in-data-catalog"></a>

In Pentaho Data Catalog, the chatbot enables users to interact with cataloged data via natural language, retrieve insights, explore business glossary terms, and access related dashboards directly within the Data Catalog interface. This procedure explains how to enable the chatbot feature in Data Catalog. After you enable the chatbot, the chatbot icon appears in the user interface, and users can start conversational data discovery.

**Prerequisites**

* Data Catalog is deployed using **Docker Compose** or **Kubernetes**.
* You have administrative access to the deployment environment, such as Docker or Amazon EKS.
* Ensure that any one large language model (LLM) is configured for chatbot in Data Catalog. For more information, see [#configure-a-large-language-model-llm-for-the-chatbot-in-data-catalog](#configure-a-large-language-model-llm-for-the-chatbot-in-data-catalog "mention").

{% tabs %}
{% tab title="Docker deployment" %}

#### Docker deployment <a href="#docker-deployment.1" id="docker-deployment.1"></a>

Perform the following steps to enable the chatbot in the Docker deployment:

**Procedure**

1. Open a terminal session on the server where Data Catalog is deployed using Docker Compose.
2. Change to the Data Catalog Docker deployment directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment
   ```
3. Stop all running Data Catalog services.

   ```
   ./pdc.sh stop
   ```
4. Open the Docker Compose configuration file.

   ```
   vi vendor/docker-compose.chatbot.yml
   ```
5. Change the `profiles` value from the disabled profile name (for example, `core1`) back to `core` for the chatbot backend and frontend services.

   ```
   services:
     chatbot-backend:
       profiles: ["core"]
     
     chatbot-frontend:
       profiles: ["core"]
     
   ```

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>The <code>profiles</code> value should match with the profile name defined for <code>COMPOSE_PROFILES</code> parameter in <code>vendor/env.default</code> (for example, <code>core</code>).</p></div>
6. Save the file and exit the editor.
7. Start the Data Catalog services.

   ```
   ./pdc.sh up
   ```
8. Open the Data Catalog UI and confirm that the chatbot icon is visible.
   {% endtab %}

{% tab title="Amazon EKS deployment" %}

#### **Amazon EKS deployment** <a href="#amazon-eks-deployment.1" id="amazon-eks-deployment.1"></a>

Perform the following steps to enable the chatbot in the Amazon EKS deployment:

**Procedure**

1. Open a terminal session on the system used to manage the Data Catalog Amazon EKS deployment.
2. Change to the directory that contains the Kubernetes profile configuration files.

   ```
   cd <pdc-helm-deployment-directory>/k8s/profiles
   ```
3. Open the profile YAML file used by the active deployment (for example, `pdc-full.yaml`, `pdc-classic.yaml`, or `pdc-pdm.yaml`).

   ```
   vi <profile-name>.yaml
   ```
4. Set `enabled: true` for both the chatbot frontend and backend services or delete them from the profile YAML file.

   ```
   cat:
     chatbot-frontend:
       enabled: true
     chatbot-backend:
       enabled: true
   ```
5. Save the profile YAML file and exit the editor.
6. Redeploy Data Catalog using Helmfile.

   ```
   helmfile sync -n <namespace>
   ```
7. Monitor the deployment status.

   ```
   kubectl get pods -n <namespace> -w
   ```
8. Open the Data Catalog UI and confirm that the chatbot icon is visible.
   {% endtab %}
   {% endtabs %}

**Result**

The chatbot frontend and backend services are enabled, and the chatbot icon appears in the Data Catalog interface. Users can now use the chatbot to explore catalog data using natural language.

**What next**

You can disable the chatbot if no longer required by reversing the configuration changes. For more information, see [#disable-chatbot-in-data-catalog](#disable-chatbot-in-data-catalog "mention").

### **Disable chatbot in Data Catalog** <a href="#disable-chatbot-in-data-catalog" id="disable-chatbot-in-data-catalog"></a>

In Pentaho Data Catalog, the chatbot enables users to interact with cataloged data via natural language, retrieve insights, explore business glossary terms, and access related dashboards directly within the Data Catalog interface. Sometimes, you might disable the chatbot when the feature is not required. This procedure explains how to disable the chatbot in Data Catalog.

Disabling the chatbot stops the chatbot frontend and backend services and removes the chatbot icon from the user interface.

**Prerequisites**

* Data Catalog is deployed using **Docker Compose** or **Kubernetes**.
* You have administrative access to the deployment environment.
* You can open a terminal session on the deployment server or management system.

{% tabs %}
{% tab title="Docker deployment" %}

#### **Docker deployment** <a href="#docker-deployment" id="docker-deployment"></a>

Perform the following steps to disable the chatbot in the Docker deployment:

**Procedure**

1. Open a terminal session on the server where Data Catalog is deployed using Docker Compose.
2. Change to the Data Catalog Docker deployment directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment
   ```
3. Stop all running Data Catalog services.

   ```
   ./pdc.sh stop
   ```
4. Open the Docker Compose configuration file.

   ```
   vi vendor/docker-compose.chatbot.yml
   ```
5. Change the `profiles` value from `core` to an unused value (for example, `core1`) for the chatbot backend and frontend services.

   ```
   services:
     chatbot-backend:
       # ...
       profiles: ["core1"]
       # ...
     chatbot-frontend:
       # ...
       profiles: ["core1"]
   ```

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>The <code>profiles</code> value used to disable the chatbot must not match any active profile defined for <code>COMPOSE_PROFILES</code> parameter in <code>vendor/env.default</code> (for example, <code>core</code>). If an admin later updates the profile's value, a name that is listed in <code>vendor/env.default</code> , the chatbot frontend and backend services start automatically.</p></div>
6. Save the file and exit the editor.
7. Start the Data Catalog services.

   ```
   ./pdc.sh up
   ```
8. Open the Data Catalog application and confirm that the chatbot icon is no longer visible.
   {% endtab %}

{% tab title="Amazon EKS deployment" %}

#### **Amazon EKS deployment** <a href="#amazon-eks-deployment" id="amazon-eks-deployment"></a>

Perform the following steps to disable the chatbot in the Amazon EKS deployment:

**Procedure**

1. Open a terminal session on the system that manages the Data Catalog Amazon EKS deployment.
2. Change to the directory that contains the Kubernetes profile configuration files.

   ```
   cd <pdc-helm-deployment-directory>/k8s/profiles
   ```
3. Open the profile YAML file used by the active deployment (for example, `pdc-full.yaml`, `pdc-classic.yaml`, or `pdc-pdm.yaml`).

   ```
   vi <profile-name>.yaml
   ```
4. Set `enabled: false` for both the chatbot frontend and backend services in the active profile YAML file.

   ```
   cat:
     chatbot-frontend:
       enabled: false
     chatbot-backend:
       enabled: false
   ```
5. Save the configuration file.
6. Redeploy Data Catalog using Helmfile.

   ```
   helmfile sync -n <namespace>
   ```
7. Monitor the deployment status.

   ```
   kubectl get pods -n <namespace> -w
   ```
8. Open the Data Catalog UI and confirm that the chatbot icon is no longer visible.
   {% endtab %}
   {% endtabs %}

**Result**

The chatbot frontend and backend services are disabled, and the chatbot icon is removed from the Data Catalog interface. Users can no longer access or use the chatbot feature. Additionally, you can verify that no chatbot services are running by checking containers or pods.

**What next**

You can re-enable the chatbot if required by reversing the configuration changes. For more information, see [#enable-chatbot-in-data-catalog](#enable-chatbot-in-data-catalog "mention").

### Configure a large language model (LLM) for the chatbot in Data Catalog

In Data Catalog, the chatbot requires a configured large language model (LLM) to generate responses, create vector embeddings, and support conversational search for authorized users. This procedure explains how, as an admin, you can configure a LLM for the chatbot feature in Data Catalog. After you configure the LLM, the chatbot backend can process user queries, generate embeddings, and return contextual responses based on catalog metadata and permissions.

**Prerequisites**

* The chatbot feature is enabled in Pentaho Data Catalog.
* You have valid LLM provider details, including API key, model name, and embedding model.

{% tabs %}
{% tab title="Docker deployment" %}

#### **Docker deployment**

Perform the following steps to configure a LLM for the chatbot feature in Data Catalog Docker deployment:

**Procedure**

1. Open a terminal session on the server where Data Catalog is deployed using Docker Compose.
2. Change to the Pentaho Data Catalog Docker deployment directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment
   ```
3. Stop all running Data Catalog services.

   ```
   ./pdc.sh stop
   ```
4. Open the environment configuration file.

   ```
   vi conf/.env
   ```
5. Configure the chatbot LLM and embedding settings.

   ```
   PDC_CHATBOT_API_KEY="<your-llm-api-key>"
   PDC_CHATBOT_EMBEDDING_MODEL="text-embedding-3-large"
   PDC_CHATBOT_LLM="gpt-4o"
   PDC_CHATBOT_LLM_BASE_URL="https://api.example-llm.com/v1"
   PDC_CHATBOT_TARGET_VECTOR_DIMENSIONS="3072"
   PDC_CHATBOT_TARGET_VECTOR_BATCH_SIZE="500"
   PDC_CHATBOT_TARGET_VECTOR_MAX_CONCURRENT_BATCHES="1"
   PDC_CHATBOT_SCHEDULE_VECTOR_INDEX_UPDATE="@daily"
   ```

   <table><thead><tr><th width="272">Environment variable</th><th>Description</th></tr></thead><tbody><tr><td><code>PDC_CHATBOT_API_KEY</code></td><td>API key used to authenticate with the configured LLM provider. The chatbot backend does not start if this value is missing or invalid.</td></tr><tr><td><code>PDC_CHATBOT_LLM</code></td><td>Name of the LLM used to generate chatbot responses.</td></tr><tr><td><code>PDC_CHATBOT_LLM_BASE_URL</code></td><td>Base URL of the LLM provider endpoint. Use this value for self-hosted or non-default LLM providers.</td></tr><tr><td><code>PDC_CHATBOT_EMBEDDING_MODEL</code></td><td>Embedding model used to generate vector representations for conversational search.<br>You cannot change this value after the initial setup.</td></tr><tr><td><code>PDC_CHATBOT_TARGET_VECTOR_DIMENSIONS</code></td><td>Number of dimensions produced by the embedding model. This value must match the dimensions supported by the embedding model.</td></tr><tr><td><code>PDC_CHATBOT_TARGET_VECTOR_BATCH_SIZE</code></td><td>Number of records processed in a single batch during vector indexing. Higher values improve throughput but increase memory usage.</td></tr><tr><td><code>PDC_CHATBOT_TARGET_VECTOR_MAX_CONCURRENT_BATCHES</code></td><td>Maximum number of vector indexing batches processed in parallel. Increasing this value increases the load on the system.</td></tr><tr><td><code>PDC_CHATBOT_CONVERSATIONAL_ROLES</code></td><td>User roles allowed to receive conversational (vector-based) chatbot responses. You can add additional roles separated by a comma.</td></tr><tr><td><code>PDC_CHATBOT_SCHEDULE_VECTOR_INDEX_UPDATE</code></td><td>Schedule that controls how often the chatbot refreshes the vector index (for example, @daily).</td></tr></tbody></table>

   <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>You cannot change the embedding model after the initial setup. If you need to use a different embedding model, you must redeploy the chatbot with a fresh vector index.</p></div>
6. Save the file and exit the editor.
7. Restart Pentaho Data Catalog services.

   ```
   ./pdc.sh stop
   ./pdc.sh up
   ```
8. Sign in to Data Catalog and verify that the chatbot returns responses.
   {% endtab %}

{% tab title="Amazon EKS deployment" %}

#### **Amazon EKS deployment**

1. Open a terminal session on the system used to manage the Pentaho Data Catalog Amazon EKS deployment.
2. Change to the directory that contains the chatbot backend Helm values.

   ```
   vi pentaho/pdc-helm-charts/conf/default/custom-values.yaml
   ```
3. Open the chatbot backend values file.

   ```
   vi custom-values.yaml
   ```
4. Configure the chatbot LLM and embedding settings.

   ```
   chatbot-backend:
     chatbot:
       modelconfig:
         apiKey: "<your-llm-api-key>"
         model: "gpt-4o"
         embeddingModel: "text-embedding-3-large"
         baseUrl: "https://api.example-llm.com/v1"
         targetVectorDimensions: 3072
         targetVectorBatchSize: 500
         targetVectorMaxConcurrentBatches: 1
         conversationalRoles: "Data Steward"
         schedule: "0 0 * * *"
   ```

   <table><thead><tr><th width="311">YAML parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>apiKey</code></td><td>API key used to authenticate with the configured LLM provider. The chatbot backend does not start if this value is missing or invalid.</td></tr><tr><td><code>model</code></td><td>Name of the LLM used to generate chatbot responses.</td></tr><tr><td><code>baseUrl</code></td><td>Base URL of the LLM provider endpoint. Required for self-hosted or custom LLM providers.</td></tr><tr><td><code>embeddingModel</code></td><td>Embedding model used to generate vector representations for conversational search.<br>You cannot change this value after the initial setup.</td></tr><tr><td><code>targetVectorDimensions</code></td><td>Number of dimensions produced by the embedding model. This value must match the dimensions supported by the embedding model.</td></tr><tr><td><code>targetVectorBatchSize</code></td><td>Number of records processed in a single batch during vector indexing.</td></tr><tr><td><code>targetVectorMaxConcurrentBatches</code></td><td>Maximum number of vector indexing batches processed in parallel.</td></tr><tr><td><code>conversationalRoles</code></td><td>User roles allowed to receive conversational (vector-based) chatbot responses. You can add additional roles separated by a comma.</td></tr><tr><td><code>schedule</code></td><td>Cron expression that controls how often the chatbot refreshes the vector index (for example, 0 0 * * *).</td></tr></tbody></table>
5. Save the configuration file.
6. Redeploy Data Catalog using Helmfile.

   ```
   helmfile sync -n <namespace>
   ```

   This command applies the updated Helm values and triggers a rolling update for the Job Server deployment.
7. Monitor the deployment status.

   ```
   kubectl get pods -n <namespace> -w
   ```
8. Sign in to Data Catalog and verify that the chatbot returns responses.
   {% endtab %}
   {% endtabs %}

**Result**

The chatbot is configured with a large language model and embedding settings. Users can use the chatbot to receive contextual responses in the chatbot.

**What next**

You can configure additional roles for conversational search to control which users receive vector-based responses. For more information, see [#configure-data-catalog-user-roles-for-conversational-search-chatbot](#configure-data-catalog-user-roles-for-conversational-search-chatbot "mention").

***

### **Configure Data Catalog user roles for conversational search chatbot**

In Pentaho Data Catalog, conversational search uses vector-based retrieval and large language models to return contextual responses, while other users continue to receive standard reporting (BIDB-based) responses.

In Data Catalog, by configuring roles for conversational search, you can control access to advanced chatbot capabilities based on user responsibilities, such as allowing users with roles, such as Data Stewards and Business Stewards, to receive deeper, semantic responses. This procedure explains how to configure which user roles can use conversational search in the Data Catalog chatbot.

**Prerequisites**

* Data Catalog is deployed using Docker Compose or Amazon EKS.
* The chatbot feature is enabled.
* You have administrative access to the deployment environment.

{% tabs %}
{% tab title="Docker deployment" %}

#### **Docker deployment**

Perform the following steps to configure Data Catalog user roles for the conversational search chatbot in the Docker deployment:

**Procedure**

1. Open a terminal session on the server where Data Catalog is deployed using Docker Compose.
2. Change to the Data Catalog Docker deployment directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment
   ```
3. Stop all running Data Catalog services.

   ```
   ./pdc.sh stop
   ```
4. Open the environment configuration file.

   ```
   vi conf/.env
   ```
5. Set the conversational search roles separated by a comma.

   ```
   PDC_CHATBOT_CONVERSATIONAL_ROLES="Data Stewrad, Business Steward"
   ```

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>By default, conversational search is enabled only for the Data Steward role. To know more about user roles in Data Catalog, see <a data-mention href="https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-user-roles-and-permissions">User roles and permissions in Data Catalog</a>. </p></div>
6. Save the file and exit the editor.
7. Start the Data Catalog services.

   ```
   ./pdc.sh up
   ```

{% endtab %}

{% tab title="Amazon EKS deployment" %}

#### **Amazon EKS deployment**

Perform the following steps to configure Data Catalog user roles for the conversational search chatbot in the Amazon EKS deployment:

**Procedure**

1. Open a terminal session on the system used to manage the Data Catalog Amazon EKS deployment.
2. Open the Kubernetes configuration file custom-values.yaml.

   ```
   vi pentaho/pdc-helm-charts/conf/default/custom-values.yaml
   ```
3. Configure the conversational search roles separated by a comma.

   ```
   cat:
     chatbot-backend:
       chatbot:
         conversationalSearch:
           conversationalRoles: "Data Steward, Business Steward"
   ```

> **Note:** By default, conversational search is enabled only for the Data Steward role. To know more about user roles in Data Catalog, see [User roles and permissions in Data Catalog](https://docs.pentaho.com/pdc-use/pdc-user-roles-and-permissions).

4. Save the configuration file.
5. Redeploy Data Catalog using Helmfile.

   ```
   helmfile sync -n <namespace>
   ```
6. Monitor the deployment status.

   ```
   kubectl get pods -n <namespace> -w
   ```
7. Sign in to Data Catalog with a user account assigned to one of the configured roles and verify that conversational responses are returned.
   {% endtab %}
   {% endtabs %}

**Result**

Conversational search is enabled only for the configured user roles. Users with these roles receive vector-based, context-aware chatbot responses, while other users continue to receive standard chatbot responses.

***

## Enable or disable business rules in Data Catalog

In Data Catalog, business rules are disabled by default. Administrators can enable or disable business rules by setting a deployment flag, then restarting the affected services in [Docker](https://hv-eng.atlassian.net/wiki/spaces/PDC/pages/edit-v2/33051246593#Docker-deployments) or redeploying them in [Amazon EKS](https://hv-eng.atlassian.net/wiki/spaces/PDC/pages/edit-v2/33051246593#Kubernetes-deployments) deployments.

Perform the following steps to enable or disable business rules in the Data Catalog:

{% tabs %}
{% tab title="Docker deployments" %}

### Docker deployments

**Procedure**

1. Sign in to the server where Data Catalog is installed and open a terminal.
2. Go to the deployment folder.

   ```
   cd /opt/pentaho/pdc-docker-deployment
   ```
3. Open the environment configuration file.

   ```
   vi /opt/pentaho/pdc-docker-deployment/conf/.env
   ```

   Data Catalog supports overriding variables from vendor/.env.default by placing them in conf/.env.
4. Enable business rules by adding the following line:

   ```
   PDC_BUSINESS_RULE_ENABLED=true
   ```

   To disable business rules, set the value to false:

   ```
   PDC_BUSINESS_RULE_ENABLED=false
   ```
5. Save the file and restart Data Catalog services.

   ```
   ./pdc.sh up
   ```

{% endtab %}

{% tab title="Amazon EKS deployments" %}

### Amazon EKS deployments

**Procedure**

1. Open a terminal on the system used to manage the Amazon EKS cluster.
2. Navigate to the folder that contains the custom values file.

   ```
   cd pentaho/pdc-helm-charts/conf/default
   ```
3. Open your custom-values.yaml file (or the values file you use for your deployment).

   ```
   vi custom-values.yaml
   ```
4. Add the `cat.fe-workers.fe` section and set the `businessRuleEnabled` flag to `"true"`.

   ```
   cat:
     fe-workers:
       fe:
         businessRuleEnabled: "true"
   ```

   To disable business rules, set the value to `"false"`.
5. Save the configuration file.
6. Redeploy Data Catalog using Helmfile.

   ```
   helmfile sync -n <namespace>
   ```
7. Monitor the deployment status.

   ```
   kubectl get pods -n <namespace> -w
   ```
8. Open the Data Catalog UI and confirm that the business rules are enabled (or disabled).
   {% endtab %}
   {% endtabs %}

**Result**

Business rules are enabled (or disabled) after services restart or the updated configuration is rolled out.

## Disable the Physical Assets feature from Data Catalog deployment <a href="#heading-title-text" id="heading-title-text"></a>

By default, the Physical Assets feature is included in the Data Catalog deployment to support OT assets metadata through Pentaho Edge. However, if your deployment does not require this feature, you can disable it by removing its reference from the Compose file. This helps reduce the size of the deployment and saves compute resources. This guide depicts how to disable the Physical Assets feature in Data Catalog.

{% hint style="info" %}
This procedure only disables the container associated with Physical Assets. It does not remove any binaries or metadata files. The service can be re-enabled at any time by restoring the profile reference.
{% endhint %}

Before you begin, make sure the following conditions are met:

* Data Catalog is already installed using the Docker deployment method. To know more about installation, see [Install Pentaho Data Catalog](https://docs.pentaho.com/pdc-10.2-install).
* You have access to the deployment directory (pdc-docker-deployment) and permission to edit the `.env.default` or `.env` file.

Perform the following steps to disable the Physical Assets feature:

1. Navigate to the following directory:

   ```
   cd /pentaho/pdc-docker-deployment/vendor
   ```
2. Open the .env.default file in a text editor:

   ```
   vi .env.default
   ```
3. Locate the COMPOSE\_PROFILES line. It may look like this:

   ```
   COMPOSE_PROFILES=core,mongodb,collab,pdso,mdm,physical-assets
   ```
4. Remove physical-assets from the list:

   ```
   COMPOSE_PROFILES=core,mongodb,collab,pdso,mdm
   ```
5. Save the file and return to the deployment root folder:

   ```
   cd /pentaho/pdc-docker-deployment
   ```
6. Restart the deployment using the following command:

   ```
   ./pdc.sh up
   ```

{% hint style="success" %}
You have successfully disabled the Physical Assets service, and it will no longer be started when deploying or restarting Data Catalog. This reduces the number of running containers and optimizes resource usage for environments where OT asset lineage is not required.
{% endhint %}

***

## **Running Data Catalog workloads using node affinity, taints, and tolerations**

Data Catalog is a distributed application that runs several containerized components, including the application, database, and worker pods. Worker pods perform data scanning, profiling, and metadata ingestion from enterprise data sources. These operations often involve direct access to sensitive or large-scale datasets.

In large or security-sensitive deployments, administrators often need precise control over where workloads run within a Kubernetes (EKS) cluster. This control helps ensure that critical services and data processing tasks run in secure, compliant, and performance-optimized environments. It becomes especially important when certain components of Data Catalog handle data that is confidential, high-volume, or requires specialized compute resources such as GPUs or high-performance storage.

By using **Kubernetes node affinity**, **taints**, and **tolerations**, you can configure Data Catalog so that:

* Worker pods run only on specific nodes. For example, nodes in a restricted security group or a separate availability zone.
* Non-worker workloads, such as the user interface or metadata services, are prevented from running on those nodes.
* The system continues to meet data segregation and compliance requirements without affecting performance or scalability.

Running PDC workloads using node affinity, taints, and tolerations provides a secure, compliant, and efficient way to manage distributed deployments across different availability zones or network segments.

Perform the following steps to configure node affinity, taints, and tolerations for Data Catalog workloads.

**Before you begin**

* Ensure that your Data Catalog deployment is running on Amazon Elastic Kubernetes Service (EKS).
* Verify that you have kubectl and AWS CLI installed and configured with permissions to update node groups and apply taints.
* Identify the node group where you want to run PDC worker workloads.
* Obtain access to the `custom-values.yaml` file used for your PDC Helm deployment.
* Confirm that your deployment uses Helmfile for orchestration.

**Procedure**

1. Open a terminal on the machine that manages your Kubernetes cluster.
2. Apply a taint to the node group you want to reserve for worker workloads.

   ```
   aws eks update-nodegroup-config \
     --cluster-name <your-cluster-name> \
     --nodegroup-name <your-nodegroup-name> \
     --taints key=dedicated,value=ws,effect=NO_SCHEDULE
   ```

   Replace the placeholders with your cluster and node group names.

   * `key=dedicated specifies the taint key`.
   * `value=ws` indicates that the node is dedicated for worker services.
   * `effect=NO_SCHEDULE` prevents other pods from being scheduled on these nodes unless they have a matching toleration.

   **Tip**: Use descriptive taint keys and values that reflect the node group’s purpose, such as key=data-processing or value=worker.
3. Edit the custom-values.yaml file for your Helm deployment.

   For **PDC 10.2.8 and later**, locate the job-server section and add:

   ```
   job-server:
     tolerations:
       - key: "dedicated"
         operator: Equal
         value: "ws"
         effect: "NoSchedule"
     affinity:
       nodeAffinity:
         requiredDuringSchedulingIgnoredDuringExecution:
           nodeSelectorTerms:
             - matchExpressions:
               - key: eks.amazonaws.com/nodegroup
                 operator: In
                 values:
                   - <your-nodegroup-name>
   ```

   Replace `<your-nodegroup-name>` with the name of the dedicated node group.
4. Save the file and deploy the configuration.

   ```
   helmfile sync -n pentaho
   ```

   The `-n pentaho` flag ensures that the deployment targets the correct namespace.

**Result**

You have successfully configure node affinity, taints, and tolerations for Data Catalog workloads. After deployment:

* Data Catalog worker pods are scheduled only on the nodes defined by the node affinity rules.
* Other pods are prevented from being scheduled on those nodes unless they include a matching toleration.
* Your Data Catalog deployment now supports workload segregation across different availability zones or network segments in AWS.

This configuration helps validate compliance and segregation requirements for deployments where worker nodes must belong to distinct security groups or availability zones.

**Next steps**

* To verify the configuration, run:

  ```
  kubectl get pods -o wide -n pentaho
  ```

  Confirm that worker pods are assigned to nodes in the expected node group.
* Monitor node usage using Amazon EKS Console or the kubectl describe node command.

**Additional information**

For more information, see the official AWS documentation:\
[Place Kubernetes pods on Amazon EKS by using node affinity, taints, and tolerations](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/place-kubernetes-pods-on-amazon-eks-by-using-node-affinity-taints-and-tolerations.html)

***

## Install user-provided SSL certificates

To provide a greater level of security to your data, you can use signed Secure Sockets Layer (SSL) certificates from your Certificate Authority (CA) with Data Catalog.

Data Catalog automatically installs self-signed certs in the *\<install-directory>*`/conf/https` directory as `server.key` (PEM-encoded private key) and `server.crt` (PEM-encoded self-signed certificate). You can replace these files with certificates signed by your CA.

Use this procedure to install signed SSL certificates for Data Catalog:

1. On your Data Catalog server, navigate to the Data Catalog installation directory `<install-directory>/conf/https`, where *\<install-directory>* is the directory where Data Catalog is installed.
   * `server.key` is a PEM-formatted file that contains the private key of a specific certificate.
   * `server.crt` is a PEM-formatted file containing the certificate.
2. Replace the *\<install-directory>*`/conf/https/server.key` file with the PEM-encoded private key used to sign the SSL certificate or generate a new private key in PEM-encoded format.
3. Replace the *\<install-directory>*`/conf/https/server.crt` file with the PEM-encoded signed certificate associated with the private key in Step 1.

   If a new private key is generated, then you need to download a new PEM-encoded signed SSL certificate from your CA.
4. Append the *\<install-directory>*`/conf/extra-certs/bundle.pem` file with the following three certificates in this order:
   1. Top level PEM-encoded signed SSL certificate (basically the content of the *\<install-directory>*`/conf/https/server.crt` file).
   2. Intermediate PEM-encoded certificate, if any, from your CA.
   3. Root PEM-encoded certificate, if any, from your CA.
5. Navigate to the Data Catalog `<install-directory>`.
6. Use the following command to restart Data Catalog:

   `./pdc.sh restart`

{% hint style="success" %}
The SSL certificates are installed.
{% endhint %}

***

## Check and remove outdated certificates

If Data Catalog services fail to start or show SSL-related errors, the issue might be caused by expired or outdated certificates in the `bundle.pem` file. You can identify and remove outdated certificates by checking their validity dates.

**Before you begin**

* Ensure you have access to the server where Data Catalog is installed.
* Verify that you have permission to view and edit files in the `conf/extra-certs` directory.

**Procedure**

1. Go to the directory where the `bundle.pem` file is stored:

   ```
   cd /<PDCInstallDir>/conf/extra-certs/
   ```
2. Run the following command to check the validity dates of all certificates in the `bundle.pem` file:

   ```
   awk 'BEGIN{block=""}
   /-----BEGIN CERTIFICATE-----/ {block=$0 RS; inblock=1; next}
   inblock {block=block $0 RS}
   /-----END CERTIFICATE-----/ {
      block=block $0 RS
      print "================"
      print block | "openssl x509 -noout -dates"
      close("openssl x509 -noout -dates")
      block=""
      inblock=0
   }' bundle.pem
   ```
3. Review the command output. You see sections similar to the following:

   ```
   notBefore=Sep  1 09:01:05 2025 GMT
   notAfter=Sep  1 09:01:05 2026 GMT

   notBefore=Jun 10 06:00:00 2023 GMT
   notAfter=Jun 10 06:00:00 2024 GMT
   ```
4. Interpret the fields in the output:

   Field Description **notBefore** Date from which the certificate becomes valid. **notAfter** Date after which the certificate expires.
5. Compare the current date with the **notAfter** value:\
   If the current date is later than **notAfter**, the certificate has expired. For example:

   ```
   notAfter=Jun 10 06:00:00 2024 GMT   ❌ Expired (past date)
   notAfter=Sep  1 09:01:05 2026 GMT   ✅ Active (future date)
   ```
6. Edit the bundle.pem file to remove the expired certificates.
   * Use any text editor such as vi or nano.
   * Remove the complete certificate block starting from\
     `-----BEGIN CERTIFICATE-----`\
     to\
     `-----END CERTIFICATE-----`.
7. Save the file and restart the Data Catalog services.

**Result**

The `bundle.pem` file now contains only active certificates, preventing SSL validation issues during Data Catalog startup or connectivity.

***

## Add email domains to the safe list in Data Catalog after deployment

During the initial deployment of Data Catalog, it is typically configured to allow only a predefined set of email domains for user authentication. However, you might grant access to users with email addresses from new domains. Instead of redeploying Data Catalog, which can cause downtime and operational delays, you can dynamically update the list of allowed email domains using the Identity & Access Management (IAM) APIs.

{% hint style="info" %}
Adding email domains and SMTP details during the initial Data Catalog deployment is always a best practice. For more information, see the [Install Pentaho Data Catalog](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/ "mention").
{% endhint %}

Perform the following steps to add email domains to the safe list using IAM APIs after deployment:

**Prerequisites**

* You must have administrative access to use the IAM APIs.
* Identify your Data Catalog DNS (for example, `catalog.example.com`).
* Obtain admin credentials to generate a Bearer token.

**Procedure**

1. Open the CMD prompt and run the following cURL command to generate an authentication token to interact with the IAM APIs:

   ```
   curl -k --location 'http://<your-server-url>/keycloak/realms/master/protocol/openid-connect/token' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'username=<admin-username>' \
   --data-urlencode 'password=<admin-password>' \
   --data-urlencode 'client_id=admin-cli' \
   --data-urlencode 'grant_type=password'
   ```

   * Replace `<your-server-url>` with your Data Catalog server URL.
   * Replace `<admin-username>` and `<admin-password>` with the actual Keycloak master realm admin user credentials.\
     The response includes the token value.

   ```
   {"access_token":"<TOKEN_VALUE>"}
   ```
2. Before updating, you can view the currently configured email domains using the following GET command.

   ```
   curl -k -X 'GET' \
     'https://<your-server-url>/css-admin-api/api/internal/css-auth-proxy/v1/provider/<your-server-url>' \
     -H 'accept: application/json' \
     -H 'Authorization: Bearer <ACCESS_TOKEN>'
   ```

   The response displays the current domain configuration:

   ```
   {
     "id": "catalog.example.com",
     "emailDomains": ["hv.com", "hitachivantara.com"]
   }
   ```
3. Run the following IAM API cURL request to update email domains:

   ```
   curl -k -X 'PUT' \
     'https://<your-server-url>/css-admin-api/api/internal/css-auth-proxy/v1/provider' \
     -H 'Authorization: Bearer <ACCESS_TOKEN>' \
     -H 'Content-Type: application/json' \
     -d '{
     "id": "<provider-id>",
     "emailDomains": [
       "hv.com",
       "hitachivantara.com",
       "gmail.com"
     ]
   }'
   ```

   * Replace `<your-server-url>` with your Data Catalog server URL.
   * Replace `<ACCESS_TOKEN>` with the token obtained in the previous step.
   * Replace `<provider-id>` with your Data Catalog server’s domain or IP address used during installation.
   * Modify the "`emailDomains`" list as needed.

   **Note**: Do not remove hv.com and hitachivantara.com from the email domain list.&#x20;
4. Run the GET command again (see Step 2) to verify that the email domains are added.

   ```
   curl -k -X 'GET' \
     'https://<your-server-url>/css-admin-api/api/internal/css-auth-proxy/v1/provider/<your-server-url>' \
     -H 'accept: application/json' \
     -H 'Authorization: Bearer <ACCESS_TOKEN>'
   ```

   The response displays the current domain configuration:

   ```
   {
     "id": "catalog.example.com",
     "emailDomains": ["hv.com", "hitachivantara.com", "gmail.com"]
   }
   ```

{% hint style="success" %}
New email domains have been added to the Data Catalog safe list, and users with those domains can now sign in successfully.
{% endhint %}

***

## Set up an email server to send Data Catalog notifications

To set up Data Catalog to send email notifications to users, you can configure any Simple Mail Transfer Protocol (SMTP) server that meets your needs.

Examples of notifications are when a user is tagged with '@' in a comment or set up in a data pipe template to be notified when a job completes.

{% hint style="info" %}
The steps to set up an SMTP server that are in the [Installing Data Catalog](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/) topic in [Install Pentaho Data Catalog](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/) only set up the forgot password functionality.
{% endhint %}

To integrate an SMTP server with Data Catalog, use the following steps:

1. Gather the following information for the SMTP server you want to use:
   * Host name of SMTP server (IP address or domain name)
   * Port number for SMTP server
   * Username on SMTP server in *\<mail userID>*`@<domain>.com` format
   * Password for username
   * Sender mail ID in *\<mail userID>*`@<domain>.com` format
   * Whether to use Transport Layer Security (TLS) or Secure Sockets Layer (SSL) security.
   * TLS or SSL port number\
     For example, you can use Gmail’s SMTP server to send emails from your application. Here are the SMTP server configuration settings for Gmail:
   * **SMTP Server Address**

     `smtp.gmail.com`
   * **Secure Connection**

     TLS/SSL based on your mail client/website SMTP plugin
   * **SMTP Username**

     your Gmail account (`xxxx@gmail.com`)
   * **SMTP Password**

     your Gmail password
   * **Gmail SMTP port**

     465 (SSL) or 587 (TLS)
2. Log into Data Catalog using root user credentials to configure Data Catalog to use the SMTP server, as in the following example:

   `https://*&lt;full domain name for PDC server&gt;*/`
3. Navigate to the `configuresystem/smtp` directory on the Data Catalog server, as in the following example:

   `https://*&lt;full domain name for PDC server&gt;*/configuresystem/smtp`

   The Configure Your System page opens.
4. Specify the SMTP server information as detailed in the following table:

<table><thead><tr><th width="132.888916015625">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Host</strong></td><td>IP address or domain name of SMTP server</td></tr><tr><td><strong>Port</strong></td><td>Port number for SMTP server</td></tr><tr><td><strong>Username</strong></td><td>User name in <code>*&#x26;lt;mail userID&#x26;gt;*@*&#x26;lt;domain&#x26;gt;*.com</code> format</td></tr><tr><td><strong>Password</strong></td><td>Password for user name specified above</td></tr><tr><td><strong>Sender Mail</strong></td><td>Sender mail ID in <code>*&#x26;lt;mail userID&#x26;gt;*@*&#x26;lt;domain&#x26;gt;*.com</code> format</td></tr><tr><td><strong>Encryption</strong></td><td><ul><li><strong>TLS</strong>: Default value (leave the <strong>Use SSL</strong> checkbox blank)</li><li><strong>SSL</strong>: Select the <strong>Use SSL</strong> checkbox</li></ul></td></tr></tbody></table>

5\. Click **Test Connection** to test the integration.\
A success confirmation message is displayed next to the **Test Connection** button.

6\. Click **Save Changes**.

{% hint style="success" %}
The SMTP server is configured.
{% endhint %}

***

## Update SMTP details in Data Catalog after deployment

Adding Simple Mail Transfer Protocol (SMTP) details in Data Catalog enables email notifications and alerts within the application, such as:

* Alerts about Data Catalog changes, approvals, and errors like data ingestion, metadata extraction, or synchronization failures.
* Password reset links when users forget their credentials.
* Notification alerts when tagged in the comments tab.

SMTP details are typically configured during the initial deployment of Data Catalog. However, if you want to update SMTP details post-deployment, you can use the Identity & Access Management (IAM) APIs without redeploying Data Catalog, which might cause downtime and operational delays.

{% hint style="info" %}
Adding email domains and SMTP details during the initial Data Catalog deployment is always the best practice. For more information, see the **Installing Data Catalog** topic in Get started with Pentaho Data Catalog document.
{% endhint %}

Perform the following steps to update SMTP details in Data Catalog using IAM APIs after deployment:

Ensure you have sufficient access to use the IAM APIs.

1. To generate an authentication token to interact with the IAM APIs, open the CMD prompt, and run the following cURL command:

   ```
   curl -k --location 'http://<your-server-url>/keycloak/realms/master/protocol/openid-connect/token' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'username=<admin-username>' \
   --data-urlencode 'password=<admin-password>' \
   --data-urlencode 'client_id=admin-cli' \
   --data-urlencode 'grant_type=password'

   ```

   * Replace `<your-server-url>` with your Data Catalog server URL.
   * Replace `<admin-username>` and `<admin-password>` credentials with the actual admin credentials.\
     The response includes the token value.

   ```
   {"access_token":"<TOKEN_VALUE>"}
   ```
2. To update SMTP details, run the following IAM API cURL request:

   ```
   curl -X PUT \
     'https://<PDC_HOST>/css-admin-api/api/v1/tenants/<TENANT_NAME>' \
     -H 'Accept: */*' \
     -H 'Authorization: Bearer <TOKEN_VALUE>' \
     -H 'Content-Type: application/json' \
     -d '{
       "realm": "<TENANT_NAME>",
       "smtpServer": {
         "password": "<SMTP_PASSWORD>",
         "replyToDisplayName": "<REPLY_TO_DISPLAY_NAME>",
         "starttls": "<true|false>",
         "auth": "<true|false>",
         "port": "<SMTP_PORT>",
         "host": "<SMTP_HOST>",
         "replyTo": "<REPLY_TO_EMAIL>",
         "from": "<FROM_EMAIL>",
         "fromDisplayName": "<FROM_DISPLAY_NAME>",
         "envelopeFrom": "<ENVELOPE_FROM>",
         "ssl": "<true|false>",
         "user": "<SMTP_USERNAME>"
       }
     }'

   ```

   <table><thead><tr><th width="221.11114501953125">Parameter</th><th>Description</th></tr></thead><tbody><tr><td><code>&#x3C;PDC_HOST></code></td><td>The host name or IP address of your Data Catalog instance.</td></tr><tr><td><code>&#x3C;TENANT_NAME></code></td><td>The tenant name, typically "pdc".</td></tr><tr><td><code>&#x3C;TOKEN_VALUE></code></td><td>A valid authentication token (must be obtained through IAM authentication).</td></tr><tr><td><code>&#x3C;SMTP_PASSWORD></code></td><td>The password for the SMTP server authentication.</td></tr><tr><td><code>&#x3C;REPLY_TO_DISPLAY_NAME></code></td><td>The display name for the reply-to email address.</td></tr><tr><td><code>&#x3C;SMTP_PORT></code></td><td>The port number used by the SMTP server.</td></tr><tr><td><code>&#x3C;SMTP_HOST></code></td><td>The SMTP server host address).</td></tr><tr><td><code>&#x3C;REPLY_TO_EMAIL></code></td><td>The reply-to email address.</td></tr><tr><td><code>&#x3C;FROM_EMAIL></code></td><td>The email address used to send notifications.</td></tr><tr><td><code>&#x3C;FROM_DISPLAY_NAME></code></td><td>The display name associated with the sender’s email.</td></tr><tr><td><code>&#x3C;ENVELOPE_FROM></code></td><td>The envelope sender address (optional).</td></tr><tr><td><code>&#x3C;SMTP_USERNAME></code></td><td>The username for SMTP authentication.</td></tr></tbody></table>

{% hint style="success" %}
You have successfully updated SMTP details in Data Catalog.
{% endhint %}

***

## Configure proxy server settings for the Licensing-API service

In Pentaho Data Catalog, the Licensing-API service is responsible for managing and validating software licenses, ensuring that only authorized users and services can access Data Catalog features. When Data Catalog is deployed in an enterprise environment that restricts direct internet access, services like the Licensing-API require a proxy server to reach external licensing servers and authenticate endpoints.

Post deployment of Data Catalog, perform the following steps to configure the proxy server for the Licensing-API service:

{% hint style="info" %}
When configuring the proxy server for the Licensing-API service, use the domain name instead of the IP address. SSL certificates are typically issued for domain names, ensuring secure communication.
{% endhint %}

Ensure that you have:

* Access to the `conf/.env` and `vendor/docker-compose.licensing.yml` files.
* Administrative privileges to modify configuration files and restart services.
* The required proxy server details (domain, port, username, and password).
* The SSL certificate file (`proxy-cert.pem`) if required for secure proxy connections.

**Procedure**

1. To configure proxy environment variables, go to Data Catalog root folder and then open the `conf/.env` file.
2. In the `conf/.env` file, update the following proxy variables with respective values:

   | Variable                          | Description                                   | Example Value     |
   | --------------------------------- | --------------------------------------------- | ----------------- |
   | `LICENSING_SERVER_PROXY_ENABLED`  | Enables or disables proxy configuration.      | `true` or `false` |
   | `LICENSING_SERVER_PROXY_DOMAIN`   | The domain or IP address of the proxy server. | `10.177.176.126`  |
   | `LICENSING_SERVER_PROXY_PORT`     | The port number used for proxy communication. | `443`             |
   | `LICENSING_SERVER_PROXY_USER`     | The username for proxy authentication.        | `admin`           |
   | `LICENSING_SERVER_PROXY_PASSWORD` | The password for proxy authentication.        | `password`        |

   ```
   LICENSING_SERVER_PROXY_ENABLED=true
   LICENSING_SERVER_PROXY_DOMAIN=10.177.176.126
   LICENSING_SERVER_PROXY_PORT=443
   LICENSING_SERVER_PROXY_USER=user
   LICENSING_SERVER_PROXY_PASSWORD=password

   ```

   **Note:** It is a best practice to avoid hard coding sensitive credentials like `PROXY_USER and PROXY_PASSWORD`. Use secret management tools or environment variables to secure them.
3. To update proxy server configuration in Docker Compose, open the `vendor/docker-compose.licensing.yml` file and update the licensing-api service configuration as follows:

   ```
   services:
     licensing-api:
       image: ${GLOBAL_IMAGE_PREFIX}/${LICENSING_API_IMAGE}
       restart: always
       environment:
         LICENSING_SERVER_URL: ${LICENSING_SERVER_URL}
         PROXY_ENABLED: ${LICENSING_SERVER_PROXY_ENABLED}
         # Use domain because SSL requires a domain, not an IP, for configuration
         PROXY_HOST: ${LICENSING_SERVER_PROXY_DOMAIN}
         PROXY_PORT: ${LICENSING_SERVER_PROXY_PORT}
         PROXY_USER: ${LICENSING_SERVER_PROXY_USER}
         PROXY_PASSWORD: ${LICENSING_SERVER_PROXY_PASSWORD}
         # Used for configuring SSL certificate for proxy
         JAVA_EXTRA_CERTS: "cert.pem"
       platform: linux/amd64
       profiles:
         - core
       volumes:
         - ${PDC_CLIENT_PATH}/proxy-cert.pem:/app/cert.pem

   ```

   **Note:**

   * The `PROXY_ENABLED`, `PROXY_HOST`, `PROXY_PORT`, `PROXY_USER`, and `PROXY_PASSWORD` environment variables are mapped inside the Docker container.
   * The `JAVA_EXTRA_CERTS` is set to `"cert.pem"` to configure SSL certificates for proxy authentication.
   * A volume mount is added to ensure that the SSL certificate file `proxy-cert.pem` is accessible within the container.
4. (Optional) If the proxy server requires SSL authentication, place the SSL certificate file (`proxy-cert.pem`) in the specified directory:

   ```
   cp /path/to/proxy-cert.pem ${PDC_CLIENT_PATH}/proxy-cert.pem
   ```

   **Note:** Ensure that the file permissions allow access by the Licensing-API service.
5. After updating the configuration, restart the Data Catalog services to apply the changes:

   ```
   ./pdc.sh restart
   ```

{% hint style="success" %}
You have successfully configured the proxy server settings for Licensing APIs in Data Catalog.
{% endhint %}

***

## Configure job server auto-scaling in Amazon EKS

The Job Server in Pentaho Data Catalog can automatically scale its pods in an Amazon Elastic Kubernetes Service (EKS) cluster based on CPU and memory utilization. This auto-scaling applies to all jobs that are executed through the Job Server, including data profiling, data identification, and metadata ingestion tasks. By enabling auto-scaling, Data Catalog maintains consistent performance for job executions while optimizing compute resource usage.

Scaling operations are managed through the Kubernetes Horizontal Pod Autoscaler (HPA) for pod-level scaling and the EKS Cluster Autoscaler for node-level scaling.

Perform the following steps to configure job server auto-scaling in Amazon EKS:

**Before you begin**

Ensure the following prerequisites are met before enabling Job Server auto-scaling:

* Data Catalog is deployed in an Amazon EKS cluster.
* The Cluster Autoscaler is enabled for the EKS node groups.
* You have administrative privileges to modify and redeploy the Helm configuration.
* Identify the namespace where Data Catalog is installed.
* Verify that your workload profiling results (for example, file profiling or JDBC profiling) are available.\
  These results help you define the appropriate CPU and memory utilization thresholds for scaling.

**Procedure**

1. Open the Job Server Helm values file.

   ```
   vi pentaho/pdc-helm-charts/charts/pdc/charts/job-server/values.yaml
   ```
2. Enable auto-scaling and define utilization parameters.

   Add or update the following configuration under the deployments section:

   ```
   cat:
     job-server:
      serviceAccount:
        annotations:
          eks.amazonaws.com/role-arn: <IAM_ROLE-FOR-IRSA>
      deployments:
        p1:
          autoscaling:
            # set to true to enable HPA for this deployment
            enabled: true
            # set based on your min node count in auto scaling node group
            minReplicas: 1
            # set based on your max node count in auto scaling node group
            maxReplicas: 3
            targetCPUUtilizationPercentage: 50
            targetMemoryUtilizationPercentage: 50
          # tweak this based on your workload and node configuration.
          jobPoolMaxSize: 10
          # tuned for m5.4xlarge aws instance type
          resources:
            limits:
              cpu: "32000m"
              memory: "48Gi"
            requests:
              cpu: "12000m"
              memory: "36Gi"
   ```

   **Note:**

   * Adjust the CPU and memory utilization percentages according to the workload behavior.
   * For high-throughput profiling or ingestion, a lower threshold (for example, 50–60%) helps scale out faster.
   * The minReplicas and maxReplicas values define the lower and upper bounds for the Job Server pods.
3. Save the configuration file.
4. Redeploy Data Catalog using Helmfile.

   ```
   helmfile sync -n <namespace>
   ```

   This command applies the updated Helm values and triggers a rolling update for the Job Server deployment.
5. Verify that the Horizontal Pod Autoscaler (HPA) is active.

   ```
   kubectl get hpa -n <namespace>
   ```

   The output lists the Job Server HPA with its configured CPU and memory thresholds.
6. Monitor scaling activity.

   ```
   kubectl get pods -n <namespace> -w
   ```

   As workload intensity increases, additional Job Server pods are created automatically.\
   When utilization decreases, the pods scale in to conserve resources.

**Result**

Data Catalog dynamically scales the Job Server pods based on CPU and memory utilization thresholds. The scaling behavior ensures optimal resource consumption while maintaining consistent performance for heavy profiling or ingestion workloads.

**Example Reference Configuration**

<table><thead><tr><th>Parameter</th><th width="104">Value</th><th>Description</th></tr></thead><tbody><tr><td>minReplicas</td><td>1</td><td>Minimum number of Job Server pods</td></tr><tr><td>maxReplicas</td><td>100</td><td>Maximum number of Job Server pods</td></tr><tr><td>targetCPUUtilizationPercentage</td><td>80</td><td>Scale-out threshold for CPU usage</td></tr><tr><td>targetMemoryUtilizationPercentage</td><td>80</td><td>Scale-out threshold for memory usage</td></tr></tbody></table>

**Next steps**

Adjust jobPoolMaxSize in the configuration to control the number of concurrent jobs per pod. It defines the number of simultaneous jobs that each Job Server pod can execute. For example, if jobPoolMaxSize=10 and there are 4 Job Server pods, up to 40 jobs can run in parallel across the cluster.

***

## Configure Smart Type to SQL feature in Data Catalog <a href="#configure-smart-type-to-sql-feature-in-data-catalog" id="configure-smart-type-to-sql-feature-in-data-catalog"></a>

In Data Catalog, you can use the Smart Type to SQL feature, which converts natural-language text into executable SQL queries within Data Pipes. This feature uses a large-language-model (LLM) service to interpret user input and automatically generate valid SQL statements for the selected database tables.

Perform the following steps to configure the Smart Type to SQL feature in Data Catalog:

**Before you begin**

* Ensure your Data Catalog deployment includes the **ml-gateway-service**.
* Confirm that the `aiml` profile is enabled. The feature is unavailable without it.
* Obtain valid credentials or API keys for your LLM provider.

**Procedure**

**For Docker Compose deployment**

1. Go to the `conf/.env` file in your Data Catalog installation directory.
2. Add the following environment variables:

   `ML_LLM_MODEL="" ML_LLM_API_KEY="" ML_LLM_INFERENCE_BASE_URL=""`
3. Save the file and restart the containers for the configuration to take effect.

**For Kubernetes deployment**

1. Open the `values.yaml` file of the `ml-gateway-service`.
2. Update the following configuration parameters:

   `llmModel: llmApiKey: llmInferenceBaseUrl:`
3. Save the file and redeploy the `ml-gateway-service`.

**Result**

You have successfully configured Smart Type to SQL feature. When the `aiml` profile is active, users can enter plain-language prompts in the SQL Editor to generate valid SQL queries automatically.

***

## Configure database password encoding for special characters <a href="#configure-database-password-encoding-for-special-characters" id="configure-database-password-encoding-for-special-characters"></a>

By default, the `pg-migration` service in Pentaho Data Catalog automatically encodes special characters (such as `@`, `:`, `/`, and `?`) in PostgreSQL database passwords to ensure they are safely included in the database connection URL, preventing connection failures caused by unescaped reserved characters. If your environment requires passing passwords without URI encoding, you can disable this behavior by setting the `PDC_PG_MIGRATIONS_DB_PASSWORD_REQUIRED_ENCODING` environment variable to `false`.

{% hint style="warning" %}
Disabling URI encoding is not recommended, as it may cause connection failures if passwords contain special characters.
{% endhint %}

Perform the following steps to disable URI encoding for passwords used by the `pg-migration` service:

**Before you begin**

Ensure that you have permission to edit the PDC environment configuration file (`.env` or `.env.default`).

**Procedure**

1. Open the environment configuration file:
   * For **Docker Compose** deployment:

     ```
     cd /opt/pentaho/pdc-docker-deployment/vendor
     vi .env.default
     ```
   * For **Kubernetes** deployment, update the value in the `values.yaml` file of the `pg-migrations` helm chart.
2. Locate or add the following environment variable and set it to false:

   ```
   PDC_PG_MIGRATIONS_DB_PASSWORD_REQUIRED_ENCODING=false
   ```
3. Save the file and start the PDC services to apply the change:
   * Docker Compose:

     ```
     docker-compose down
     docker-compose up -d
     ```
   * Kubernetes (Helm):\
     Deploy the pg-migrations release with the updated values.yaml takes effect:

     ```
     helm upgrade <pg-migrations-release-name> <chart-path-or-repo> -f values.yaml
     ```

     Replace `<pg-migrations-release-name>` and `<chart-path-or-repo>` with your actual values.

**Result**

Data Catalog disables URI encoding for PostgreSQL database passwords used by the `pg-migration` service. The password is passed to the database connection URL as-is.

**Next steps**

If you need to modify additional system-level configuration variables, see [#configure-system-environment-variables](#configure-system-environment-variables "mention").

***

## Configure table and column sorting order in Data Canvas

By default, Pentaho Data Catalog displays tables and columns in their ordinal order within the **Data Canvas**, that is, in the same sequence as they appear in the source database. This ordering helps users analyze the data structure as designed in the original schema. However, sometimes, you might prefer to view tables and columns in alphabetical order, which simplifies browsing and locating objects across large schemas. You can modify this behavior by updating the system environment variable `PDC_FE_DATA_CANVAS_COLUMN_SORTING_ORDER` in the deployment configuration file.

Perform the following steps to configure table and column sorting order:

**Prerequisites**

Ensure that you have access to the Data Catalog deployment directory on the server.

**Procedure**

1. Log in to the server where Pentaho Data Catalog is installed.
2. Go to the Data Catalog Docker deployment configuration directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment/conf
   ```
3. Open the `.env` (environment configuration) file.

   ```
   vi .env
   ```

   If the `.env` file does not exist, create it and save the file before proceeding.
4. Add or update the following environment variable.

   ```
   PDC_FE_DATA_CANVAS_COLUMN_SORTING_ORDER=name,asc
   ```
5. Save the file and exit the editor.
6. Restart the Data Catalog containers for the changes to take effect.

   ```
   cd /opt/pentaho/pdc-docker-deployment/
   ./pdc.sh up
   ```

{% hint style="info" %}
This configuration affects only the display order in the Data Canvas and does not modify metadata, lineage, or profiling results.
{% endhint %}

**Result**

Tables and columns in the Data Canvas are now displayed in alphabetical order.

**Next steps**

* If you prefer to revert to the default ordinal order, set the variable in the `.env.default` file.

  ```
  PDC_FE_DATA_CANVAS_COLUMN_SORTING_ORDER=ordinalPosition,asc
  ```
* For details on editing environment variables, see [#configure-system-environment-variables](#configure-system-environment-variables "mention").

***

## **Configure the OCR feature in Data Catalog**

The Optical Character Recognition (OCR) feature in Data Catalog enables the system to extract and classify text from scanned documents and image files. OCR enhances Document Processing in Data Discovery by automatically identifying sensitive or business-critical text, such as passport numbers, personal names, or identifiers. This text is matched against predefined or user-defined **data patterns** and then tagged or associated with **business glossary terms** for consistent governance.

By default, Pentaho Data Catalog uses **Tesseract** as the OCR engine. For improved accuracy with low-resolution or complex images, you can enable the **EasyOCR** model.

Perform the following steps to configure OCR in Data Catalog:

**Before you begin**

* Verify that you have administrative access to the Pentaho Data Catalog deployment.
* Ensure that the environment (Docker or EKS) is running a supported version of PDC (10.2.9 or later).
* Identify the deployment type (Docker-based or EKS-based).
* Back up your configuration files before making any changes.

**Procedure**

Perform teh following steps to configure OCR feature in Data Catalog:

**For Docker-based deployments**

1. Navigate to the conf/ directory of your Pentaho Data Catalog deployment.
2. Open the .env file for editing.
3. Add the following environment variable:

   ```
   PDC_WS_DEFAULT_USE_EASYOCR=true
   ```
4. Save the file and restart the services using the following command:

   ```
   ./pdc.sh restart
   ```

   After the restart, Pentaho Data Catalog uses the EasyOCR model to process scanned documents and images.

**For EKS-based deployments**

1. Open a terminal window configured with kubectl access to your cluster.
2. Edit the Job Server deployment by running:

   ```
   kubectl edit deploy cat-job-server-priority-0 -n <namespace>
   ```
3. In the **env** section, add the following variable:

   <pre><code><strong>- name: USE_EASYOCR
   </strong>  value: "true"
   </code></pre>
4. Save and exit the editor. The deployment automatically restarts with the new configuration.

**Result**

Data Catalog now uses the EasyOCR engine for document text recognition. When users perform Data Discovery and then Document Processing, the system extracts text from scanned files and identifies information that matches OCR patterns.

***

## Configure Large Language Models in Data Catalog <a href="#configure-large-language-models-in-data-catalog" id="configure-large-language-models-in-data-catalog"></a>

In Data Catalog, machine learning–driven document intelligence enables automated understanding and enrichment of unstructured content. Data Catalog applies pre-trained and configurable language models to analyze document content and deliver capabilities such as document classification, address detection, and document summarization.

By default, Data Catalog uses built-in models optimized for enterprise content, and you can also configure a custom or third-party language model to control how document content is processed, analyzed, and enriched across these ML-powered features. Refer to the following procedures to configure an LLM for [Docker](https://hv-eng.atlassian.net/wiki/spaces/PDC/pages/32536920066/TECHPUBS-4459+Document+Classification#Docker-deployment) and [Amazon EKS](https://hv-eng.atlassian.net/wiki/spaces/PDC/pages/32536920066/TECHPUBS-4459+Document+Classification#Amazon-EKS-deployment) deployments.

#### Docker deployment

Perform the following steps to configure a custom or third-party language model in the Data Catalog Docker deployment:

**Before you begin**

Obtain the following information from your language model provider:

* Model name or identifier
* Inference endpoint base URL
* API key

**Procedure**

1. Log in to the server where Pentaho Data Catalog is installed.
2. Go to the Data Catalog Docker deployment configuration directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment/conf
   ```
3. Open the .env (environment configuration) file.

   ```
   vi .env
   ```

   If the .env file does not exist, create it and save the file before proceeding.
4. Add or update the following environment variables based on your deployment requirements:
   * `ML_USE_LLM_FOR_CONTENT_PROCESSING`: Enables language model–based content processing for document classification. Set this value to true.
   * `ML_LLM_MODEL`: Specifies the name or identifier of the language model to use.
   * `ML_LLM_API_KEY`: Specifies the API key used to authenticate with the language model service.
   * `ML_LLM_INFERENCE_BASE_URL`: Specifies the base URL for the language model inference endpoint.
   * `ML_CLASSIFICATION_THRESHOLD`: Minimum confidence score required to accept a model-generated classification.
   * `ML_TERM_MATCHING_THRESHOLD`: Minimum semantic similarity score required to assign a user-defined term to a document.\
     Example:

     ```
     ML_USE_LLM_FOR_CONTENT_PROCESSING=true
     ML_LLM_MODEL="<model-name>"
     ML_LLM_API_KEY="<api-key>"
     ML_LLM_INFERENCE_BASE_URL="<inference-endpoint-url>"
     ML_CLASSIFICATION_THRESHOLD=0.5
     ML_TERM_MATCHING_THRESHOLD=0.7
     ```
5. After adding all required variables, save the changes and restart the Data Catalog services to apply the configuration.

   ```
   ./pdc.sh stop
   ./pdc.sh up
   ```

**Result**

You have configured the specified language model for [AI-assisted document processing features](https://hv-eng.atlassian.net/wiki/spaces/PDC/pages/32536920066/TECHPUBS-4459+Document+Classification#AI-assisted-document-processing) in the Docker deployment. Additionally, you can fine-tune the prompts used by AI-assisted document processing features to better align with your organization’s requirements. The default prompts are defined in the following file:

```
pdc-docker-deployment/compose/vendor/prompts/default-prompts.yaml
```

#### Amazon EKS deployment

Perform the following steps to configure a custom or third-party language model for AI-assisted document processing features in a Data Catalog Amazon EKS deployment:

**Before you begin**

* Ensure you have access to the Kubernetes cluster and namespace where Data Catalog is deployed.
* Ensure kubectl and helm are installed on the machine you use to administer the cluster.
* Obtain the following details from your language model provider:
  * Model name or ID
  * Inference endpoint base URL
  * API key

{% hint style="info" %}
**Security recommendation:** Store the API key in a Kubernetes Secret and reference it from the Helm values. Do not store API keys in Git.
{% endhint %}

**Procedure**

1. Open a terminal on the machine you use to administer the Amazon EKS cluster.
2. Navigate to the directory containing the Helm chart values for the **ml-gateway-services** component.

   ```
   cd /pdc-docker-deployment/k8s/charts/pdc/charts/ml-gateway-services
   ```
3. Open the values.yaml (environment configuration) file.

   ```
   vi values.yaml
   ```
4. Add or update the following environment variables based on your deployment requirements:
   * `useLLMForContentProcessing`: Enables language model–based content processing for document classification. Set this value to true.
   * `llmModel`: Specifies the name or identifier of the language model to use.
   * `llmApiKey`: Specifies the API key used to authenticate with the language model service.
   * `llmInferenceBaseUrl`: Specifies the base URL for the language model inference endpoint.
   * `mlClassificationThreshold`: Minimum confidence score required to accept a model-generated classification.
   * `mlTermMatchingThreshold`: Minimum semantic similarity score required to assign a user-defined term to a document.\
     Example:

     ```
     useLLMForContentProcessing: true
     llmModel: "<model-name>"
     llmApiKey: "<api-key>"
     llmInferenceBaseUrl: "<inference-endpoint-url>"
     mlClassificationThreshold: "0.5" 
     mlTermMatchingThreshold: "0.7"
     ```
5. Apply the configuration to the cluster by upgrading the Helm release that deploys Data Catalog.

   ```
   helm upgrade <release-name> <chart-path> -n <namespace> -f values.yaml
   ```
6. Verify that the updated pods have rolled out successfully.

   ```
   kubectl rollout status deployment/<deployment-name> -n <namespace>
   ```
7. Verify that the services are running and pods are in a Ready state.

   ```
   kubectl get pods -n <namespace>
   ```

**Result**

You have configured the specified language model for [AI-assisted document processing features](https://hv-eng.atlassian.net/wiki/spaces/PDC/pages/32536920066/TECHPUBS-4459+Document+Classification#AI-assisted-document-processing) in your Amazon EKS deployment. Additionally, you can fine-tune the prompts used by AI-assisted document processing features to better align with your organization’s requirements. The default prompts are defined in the following file:

```cmd
k8s/charts/pdc/charts/ml-gateway-service/values.yaml
```

***

## Connect to Business Intelligence Database (BIDB)

The Data Catalog includes the Business Intelligence Database (BIDB) server, which stores and manages reporting metadata. Depending on your PDC version, BIDB is implemented using either PostgreSQL (PDC 10.2.5 and later) or MongoDB (PDC 10.2.1). You can use the respective connection methods and connect to the BIDB server to access reporting data and build dashboards. See the [Reporting and data visualization](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-data-catalog-user-features-cp#business-intelligence-database) section in the [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/) guide for details about BIDB and the components available in BIDB.

### PDC 10.2.5 and later (PostgreSQL)

Beginning with PDC 10.2.5, BIDB has been migrated from MongoDB to PostgreSQL, providing a relational database structure that improves query performance and enhances compatibility with broader tool sets.

Perform the following steps to connect to BIDB (PostgreSQL) in PDC 10.2.5 and later:

1. Locate the BIDB credentials in the PDC server:
   1. Navigate to the `/vendor/.env.default` file.
   2. Identify the variables beginning with `POSTGRES_BIDB_USER_*`.
   3. To list the values, run:\ <kbd>`cat .env.default | grep 'POSTGRES_BIDB'`</kbd>
2. Install the required PostgreSQL driver:
   * For JDBC, download the PostgreSQL JDBC driver from the official PostgreSQL site.
   * For ODBC, install the PostgreSQL ODBC driver (psqlODBC) on your system.
3. Configure your connection:
   * JDBC connection string format:\
     `jdbc:postgresql://pdc.pentaho.com:5432/bidb`
   * ODBC DSN settings:
     * Server: `<HOSTNAME>`
     * Port: `5432`
     * Database: `bidb`
     * Username: `bidb_ro`
     * Password: `${POSTGRES_BIDB_USER_PASSWORD}`
4. Save the configuration in your reporting or analytics tool.
5. Test the connection to confirm access.

**Important**:&#x20;

* It is best practice not to hardcode credentials in your application. Instead, reference the environment variables (`POSTGRES_BIDB_USER_*`) to ensure secure and flexible credential management.
* Ensure that the `.env.default` file is stored securely and is not shared publicly.

{% hint style="success" %}
You have successfully connected to the BIDB PostgreSQL database in PDC 10.2.5 or later. You can now run queries, build reports, and use reporting tools through JDBC or ODBC connections.
{% endhint %}

***

### PDC versions prior to 10.2.5 (MongoDB)

In PDC versions prior to 10.2.5, the Business Intelligence Database (BIDB) is implemented using MongoDB. To connect to the BIDB server, you can use either the Java Database Connectivity (JDBC) connector or the Open Database Connectivity (ODBC) connector, depending on your application or reporting tool requirements.

#### Configure the Java Database Connectivity (JDBC) connector

Perform the following steps to configure the JDBC connector for connecting to BIDB:

1. Download the MySQL JDBC Connector JAR file from the [MySQL website](https://dev.mysql.com/downloads/connector/j/) after selecting the appropriate version for the operating system.
2. Download the [JDBC Authentication Plugin](https://www.mongodb.com/docs/bi-connector/current/reference/auth-plugin-jdbc/#jdbc-authentication-plugin).
3. Download the DBeaver application from the [DBeaver website](https://dbeaver.io/download/) and install it on the system. See [DBeaver installation](https://dbeaver.com/docs/dbeaver/Installation/) for more details.
4. To add the MySQL JDBC Driver and MySQL authentication plugin to DBeaver, open DBeaver and go to **Database** > **Driver Manager**.
5. Click **New** to add a new driver.
6. Select **MySQL** from the list and enter a name for the driver.
7. Click **Browse** to locate and select the downloaded JDBC driver (JAR file) and the MySQL authentication plugin, then click **OK** or **Finish** to add the driver.
8. After adding the MySQL driver, to create a **New Connection**, go to the **DBeaver** home page, click **New Database Connection**, and select **MySQL** as the database type.
9. Enter the MySQL server connection details, such as host, port, username, password, and so on.
10. Specify the jars in the local client configuration as shown in the following section.

    ```
    jdbc:mysql://20.8.222.21:3307?useSSL=false&authenticationPlugins=org.mongodb.mongosql.auth.plugin.MongoSqlAuthenticationPlugin
    ```

    ![](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-94bb0a856d19c32442fd019702f107ae22ba4f17%2FPDC_local_client_config.jpg?alt=media)
11. Click **Test Connection** to verify the connection is working.
12. Click **Finish** to save the connection configuration.

{% hint style="success" %}
You are now connected to BIDB using the JDBC connector. Use any third-party BI tool to connect to BIDB to analyze data and create dashboards.
{% endhint %}

***

#### Configure the Open Database Connectivity (ODBC) connector

The MongoDB ODBC connector allows you to connect tools that support ODBC to MongoDB and query the data using SQL. Perform the following steps to configure the JDBC connector for connecting to BIDB.

1. Download and install the MongoDB ODBC connector.

   See [MongoDB BI Connector ODBC Driver](https://www.mongodb.com/docs/bi-connector/current/reference/odbc-driver/#mongodb-bi-connector-odbc-driver) for more information.
2. Download and install an ODBC driver manager on your system.

   For example, on the Windows operating system, you can use the default Windows ODBC Data Source Administrator.
3. Open the **ODBC Data Source Administrator** on your machine and go to the **System DSN** tab.
4. Click **Add** to add a new data source and select the **MongoDB Driver**.
5. To configure the DSN (Data Source Name) settings:
   1. Set the server field to the address of your MongoDB server.
   2. Enter the port number if it differs from the default (`27017`).
   3. Enter the required details for authentication, username, and password.
   4. As a part of the connection details, enter the plugin directory details.
   5. Set the **SSL Mode** to **Disabled** in the SSL configuration.
6. Click **Test** to verify that connection is working.
7. Click **OK** to save the connection configuration.

{% hint style="success" %}
You are now connected to BIDB using the MongoDB ODBC connector. Use any third-party BI tool to connect to BIDB to analyze data and create dashboards.
{% endhint %}

***

## Configure a machine learning (ML) server connection in Data Catalog

You can connect a machine learning (ML) server to Data Catalog and import ML model server components into the **ML Models** hierarchy. Supported server types include:

* Pre-Production Model Servers such as MLflow, which capture experiments, runs, versions, and artifacts.
* Production Model Servers such as NVIDIA Triton, which provide model deployment, inference statistics, and operational metrics.

Once configured, the ML server appears under the **Synchronize** card in the **Management** section of Data Catalog, allowing you to import model components into the ML Models hierarchy. For more information about ML Models, see the [ML Models](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-machine-learning-ml-models-ug) section in [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/).

### Configure an MLflow server connection

Perform the following steps to configure a pre-production MLflow server connection in Data Catalog.

Before you begin:

* Make sure you have access to the MLflow server you want to connect to.
* If the MLflow server requires authentication, make sure you have the necessary credentials, either a valid username and password or an access token.

**Procedure**

1. Verify whether the file `external-data-source-config.yml` exists in the path `${PDC_CLIENT_PATH}/external-datasource/`. If not available, create it.
2. Open the `external-data-source-config.yml` file and add ML server configuration:

   ```yaml
   servers:
     - id: {SERVER_ID}
       name: {SERVER_NAME}
       type: {SERVER_TYPE}
       url: {SERVER_URL}
       config:
         username: {username}
         password: {password}
         access_token: {access_token}
   ```

<table><thead><tr><th width="129">Parameter</th><th>Description</th><th>Example</th></tr></thead><tbody><tr><td><code>id</code></td><td>Unique identifier (UUID) for the ML server.</td><td><code>916d3b20-7fd6-49d2-b911-cc051f56e837</code></td></tr><tr><td><code>name</code></td><td>Display name for the server. This name appears in the UI.</td><td><code>MLflowServer</code></td></tr><tr><td><code>type</code></td><td>Type of server (enum value). For ML server, use ‘<code>MlFlow</code>’.</td><td> </td></tr><tr><td><code>URL</code></td><td>The base URL of the ML server.</td><td><code>http://mlflow.mycompany.com</code></td></tr><tr><td><code>config</code></td><td><p>Configuration keys specific to ML server you are configuring. Include either, only if authentication is enabled:- Username and password</p><ul><li>Access token</li></ul></td><td> </td></tr></tbody></table>

3\. After configuring the ML server in the YAML file, restart the PDC services to apply the changes.

{% hint style="success" %}
You have successfully configured the MLflow server in Data Catalog as an external data source. It appears under the **Synchronize** card in the **Management** section of Data Catalog.
{% endhint %}

You can now import ML model server components into the ML Models hierarchy of Data Catalog. For more information, see [Import ML model server components into ML Models hierarchy](https://docs.pentaho.com/pdc-admin/pdc-manage-ml-models#import-ml-model-server-components-into-data-catalog).

***

### Configure a Triton server connection

Perform the following steps to configure a production Triton inference server connection in Data Catalog:

Before you begin:

* Ensure the Triton inference server is running and accessible.
* If running Triton in Docker, confirm that the ports are exposed (HTTP, gRPC, Metrics). For example:

```yaml
version: "3.9"
services:
  triton:
    image: nvcr.io/nvidia/tritonserver:24.11-py3
    volumes:
      - ./models:/models
    command: ["tritonserver", "--model-repository=/models", "--backend-config=execution_mode=cpu", "--strict-model-config=false"]
    ports:
      - "8000:8000"   # HTTP
      - "8001:8001"   # gRPC
      - "8002:8002"   # Metrics
```

**Procedure**

1. Verify whether the file `external-data-source-config.yml` exists in the path `${PDC_CLIENT_PATH}/external-datasource/`. If not available, create it.
2. Open the `external-data-source-config.yml` file and add ML server configuration:

   ```yaml
   servers:
     - id: {SERVER_ID}
       name: {SERVER_NAME}
       type: Triton
       url: {TRITON_SERVER_URL}
       config:
         metadata_port: {metadata-port}
         metrics_port: {metrics-port}
   ```

<table><thead><tr><th width="210">Parameter</th><th width="322">Description</th><th>Example</th></tr></thead><tbody><tr><td><code>id</code></td><td>Unique identifier (UUID) for the Triton server.</td><td><code>44e2fa51-e3af-4094-8dd3-c62320952de5</code></td></tr><tr><td><code>name</code></td><td>Display name for the server. This name appears in the UI.</td><td><code>Triton-Prod-server</code></td></tr><tr><td><code>type</code></td><td>Type of server (enum value). For Triton server, use ‘<code>Triton</code>’.</td><td> <code>Triton</code></td></tr><tr><td><code>URL</code></td><td>The base URL where the Triton server is deployed.</td><td><code>http://192.168.0.10</code></td></tr><tr><td><code>config.metadata_port</code></td><td>HTTP port configured when deploying the Triton server.
<br>The default port is 8000.
</td><td> <code>8000</code></td></tr><tr><td><code>config.metrics_port</code></td><td>Metrics port configured by the user when deploying the Triton server.
<br>The default is 8002.</td><td><code>8002</code></td></tr></tbody></table>

3\. Save the YAML file and restart the PDC services to apply the changes.

{% hint style="success" %}
You have successfully configured the Triton server in Data Catalog as an external data source. It appears under the **Synchronize** card in the **Management** section of Data Catalog.
{% endhint %}

You can now import ML model server components into the ML Models hierarchy of Data Catalog. For more information, see [Import ML model server components into ML Models hierarchy](https://docs.pentaho.com/pdc-admin/pdc-manage-ml-models#import-ml-model-server-components-into-data-catalog).

***

## Configure a Tableau server connection in Data Catalog

You can configure a connection between a Tableau server and Data Catalog to import Tableau metadata such as dashboards, workbooks, projects, and data sources into the Business Intelligence (BI) section of Data Catalog. To learn more, see the [Business Intelligence](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-business-intelligence) section in the [Use Pentaho Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/) guide. This guide depicts a step-by-step procedure to configure the Tableau server connection in Data Catalog.

Before you begin:

* Make sure you have access to the Tableau Cloud or Tableau Server instance you want to connect to. The URL format looks like:

  ```
  https://<region>.online.tableau.com/#/site/<site-id>/home
  ```
* Identify the Site ID for the Tableau site. For Tableau Cloud, you can find this in the URL after `/site/`.
* Generate a valid Personal Access Token (PAT) in Tableau, including PAT name and PAT secret.

Perform the following steps to configure a connection between the Tableau server and Data Catalog:

1. Verify whether the file `external-data-source-config.yml` exists in the path `$ {PDC_CLIENT_PATH}/external-datasource/`. If not available, create it.
2. Open the `external-data-source-config.yml` file and add Tableau server configuration:

   ```
   servers:
     - id: dev-8f012f9ca7
       name: Test_Server
       type: Tableau
       url: https://prod-apnortheast-a.online.tableau.com/api/3.22/auth/signin
       config:
         pat_name: 'test'
         pat_secret: 'kITbTaYmTPSdZ7ADeP11VA==:hwt9jkehQqGuq72Lh9V4wiFlfZcIpny8'

   ```

   <table><thead><tr><th width="123.33331298828125">Parameter</th><th>Description</th><th>Example</th></tr></thead><tbody><tr><td><code>id</code></td><td>The site ID (unique identifier) of the Tableau site to connect to, as seen in the Tableau Cloud URL.</td><td><code>dev-8f012f9ca7</code></td></tr><tr><td><code>name</code></td><td>Display name for the server. This name appears in the UI.</td><td><code>TableauServer</code></td></tr><tr><td><code>type</code></td><td>Type of server (enum value). For Tableau server, use ‘<code>Tableau</code>’.</td><td><code>Tableau</code></td></tr><tr><td><code>URL</code></td><td>The Tableau REST API authentication endpoint. Use the <code>signin</code> endpoint for the Tableau site.</td><td><code>https://prod-apnortheast-a.online.tableau.com/api/3.22/auth/signin</code></td></tr><tr><td><code>config</code></td><td>Configuration keys specific to the Tableau server you are configuring.</td><td></td></tr><tr><td>- <code>pat_name</code></td><td>The name of the Tableau Personal Access Token (PAT) used for authentication.</td><td></td></tr><tr><td>- <code>pat_secret</code></td><td>The secret key associated with the PAT. Ensure this is stored securely and never exposed.</td><td></td></tr></tbody></table>
3. After configuring the Tableau server in the YAML file, restart the following PDC services to apply the changes:

   * Frontend service (fe)
   * Worker service (ws-default)

   ```
   # Restart the frontend and worker services
   ./pdc.sh restart fe
   ./pdc.sh restart ws-default

   ```

{% hint style="info" %}
You have successfully configured the Tableau server in Data Catalog as an external data source. It appears under the **Synchronize** card in the **Management** section of Data Catalog.
{% endhint %}

You can now [import Tableau server components](https://docs.pentaho.com/pdc-admin/pdc-manage-business-intelligence-components#import-and-sync-tableau-server-components-into-data-catalog) into the [Business Intelligence](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-business-intelligence) hierarchy of Data Catalog.

***

## Configure a Power BI service connection in Data Catalog

You can connect the Microsoft Power BI service to Data Catalog and import Power BI metadata into the [Business Intelligence](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-business-intelligence) section. This integration lets you discover, explore, and manage Power BI reports, datasets, and workspaces directly from Data Catalog. This guide provides step-by-step instructions to configure a Power BI server connection in Data Catalog using either username and password–based authentication or Service Principal (SPN) authentication.

Before you begin:

* Ensure that you have a valid Microsoft account with an active Power BI service license. Contact your Microsoft administrator if you need access.
* Register an Azure Active Directory (Azure AD) application in the [Azure portal](https://portal.azure.com). For more information, see [Microsoft guide to register an app](https://learn.microsoft.com/azure/active-directory/develop/quickstart-register-app).
* Generate a client secret in the Azure AD application and store it securely. For more information, see [Microsoft guide to add client secrets](https://learn.microsoft.com/azure/active-directory/develop/howto-add-app-roles-in-azure-ad-apps).
* Assign the following API permissions to the Azure AD app:

  <table><thead><tr><th width="219.1666259765625">Permission</th><th>Description</th></tr></thead><tbody><tr><td><code>App.Read.All</code></td><td>View all Power BI apps</td></tr><tr><td><code>Capacity.Read.All</code></td><td>View all capacities</td></tr><tr><td><code>Dashboard.Read.All</code></td><td>Read dashboards</td></tr><tr><td><code>Dataflow.Read.All</code></td><td>Read dataflows</td></tr><tr><td><code>Dataset.Read.All</code></td><td>View all datasets</td></tr><tr><td><code>Report.Read.All</code></td><td>Read reports</td></tr><tr><td><code>Tenant.Read.All</code></td><td>View all content in tenant</td></tr><tr><td><code>Workspace.Read.All</code></td><td>View all workspaces</td></tr></tbody></table>

  See [Power BI automation permissions](https://learn.microsoft.com/power-bi/developer/automation/automation-permissions) for more information.
* Ensure that a service account is available with access to all Power BI workspaces that you need to integrate with Data Catalog.
* Confirm outbound HTTPS access to `https://api.powerbi.com` on port `443` from the Data Catalog server.
* Collect the following details before continuing:

  <table><thead><tr><th width="214.16668701171875">Field</th><th>Description</th></tr></thead><tbody><tr><td>Client ID</td><td>From Azure AD App registration</td></tr><tr><td>Client Secret</td><td>Securely generated during Azure AD registration</td></tr><tr><td>Tenant ID</td><td>Azure AD Directory unique identifier</td></tr><tr><td>OAuth2 Token URL</td><td>https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token</td></tr><tr><td>API Host URL</td><td>https://api.powerbi.com</td></tr><tr><td>Username</td><td>Credentials for the Power BI server.</td></tr><tr><td>Password</td><td>Credentials for the Power BI server.</td></tr></tbody></table>

{% hint style="info" %}

* Admin consent must be granted for all permissions during Azure AD app setup.
* A Power BI Pro or Premium Per User (PPU) license is required to use the Power BI REST APIs for integration with Data Catalog.
* Data Catalog uses the Resource Owner Password Credentials (ROPC) grant type for authentication.
  {% endhint %}

Perform the following steps to configure a connection between the Power BI server and Data Catalog:

1. Connect to the Data Catalog server using SSH.
   1. From your local machine, open a terminal (for Linux or macOS) or an SSH client, such as PuTTY (for Windows).
   2. Enter the SSH command to connect to the server where Pentaho Data Catalog is installed.

      ```
      ssh <pdc-admin>@<pdc-server-ip>
      ```

      Replace `<username>` with your server login account and `<server-ip>` with the server’s IP address or hostname.&#x20;
   3. When prompted, enter the password for the specified account. \
      After a successful login, you will have access to the Data Catalog server’s command line.

2. Navigate to the configuration folder and verify whether the file `external-data-source-config.yml` exists in the path `$ {PDC_CLIENT_PATH}/external-datasource/`. If not available, create it.

   <pre><code><strong>/opt/pentaho/pdc-docker-deployment/conf/external-data-source
   </strong></code></pre>

3. Open the `external-data-source-config.yml` file and add the Power BI server configuration:\
   Choose one of the following authentication options based on your environment.
   1. **Username and password–based authentication (ROPC)**\
      Use this option when connecting with a Power BI service account that uses username and password authentication.

      <pre class="language-yaml"><code class="lang-yaml">servers:
        - id: &#x3C;your-server-id>
      <strong>    name: PowerBIServer
      </strong>    type: PowerBI
          url: https://login.microsoftonline.com/organizations/oauth2/v2.0/token
          config:
            client_id: &#x3C;your-client-id>
            username: &#x3C;your-username>
            password: &#x3C;your-password>
            client_secret: &#x3C;your-client-secret>
            host_url: https://api.powerbi.com

      </code></pre>
   2. **Service Principal (SPN)–based authentication**\
      Use this option when connecting with an Azure AD service principal. Service Principal (SPN) authentication is recommended for production environments because it avoids storing user credentials and aligns with Azure security best practices. This option does not require a username or password.

      ```yaml
      servers:
        - id: <your-server-id>
          name: PowerBIServer
          type: PowerBI
          url: https://login.microsoftonline.com/organizations/oauth2/v2.0/token
          config:
            client_id: <your-client-id>
            client_secret: <your-client-secret>
            tenant_id: <your-tenant-id>
            host_url: https://api.powerbi.com

      ```

      <table><thead><tr><th width="123.33331298828125">Parameter</th><th>Description</th><th>Example</th></tr></thead><tbody><tr><td><code>id</code></td><td>The unique identifier for the Power BI server connection. You define this value in the YAML.</td><td><code>dev-powerbi01</code></td></tr><tr><td><code>name</code></td><td>Display name for the server. This name appears in the Data Catalog UI.</td><td><code>PowerBIServer</code></td></tr><tr><td><code>type</code></td><td>Type of server (enum value). For Power BI server, use ‘<code>PowerBI</code>’.</td><td><code>PowerBI</code></td></tr><tr><td><code>URL</code></td><td>The Microsoft identity platform OAuth 2.0 token endpoint. Used for authentication requests.</td><td><code>https://prod-apnortheast-a.online.tableau.com/api/3.22/auth/signin</code></td></tr><tr><td><code>config</code></td><td>Configuration keys specific to the Power BI server you are configuring.</td><td></td></tr><tr><td>- <code>client_id</code></td><td>The application (client) ID generated during Azure AD app registration.</td><td><code>12345678-abcd-1234-abcd-1234567890ab</code></td></tr><tr><td>- <code>username</code></td><td>The Microsoft account username with access to the Power BI service. </td><td><code>admin@contoso.com</code></td></tr><tr><td>-<code>password</code></td><td>The password associated with the Microsoft account username. Ensure this is stored securely.</td><td></td></tr><tr><td>-<code>client_secret</code></td><td>The client secret generated for the Azure AD app. Ensure this is stored securely and never exposed.</td><td><code>abcdEFGH12345!@#xyz</code></td></tr><tr><td>-<code>tenant_id</code></td><td>The Azure Active Directory tenant ID used for Service Principal authentication.</td><td><code>contoso.onmicrosoft.com</code></td></tr><tr><td>-<code>host_url</code></td><td>The base API endpoint for Power BI service.</td><td><code>https://api.powerbi.com</code></td></tr></tbody></table>

4. After configuring the Power BI server in the YAML file, restart the following PDC services to apply the changes:

   ```
   ./pdc.sh up

   ```

{% hint style="success" %}
You have successfully configured the Power BI server in Data Catalog as an external data source. It appears under the **Synchronize** card in the **Management** section of Data Catalog.
{% endhint %}

You can now [import Power BI server component<mark style="color:$primary;">s</mark>](https://docs.pentaho.com/pdc-admin/pdc-manage-business-intelligence-components#import-and-sync-bi-server-tableau-or-power-bi-components-into-data-catalog) into the **Business Intelligence** hierarchy of Data Catalog.

***

## Configure the Physical Assets service in Data Catalog

In Pentaho Data Catalog, you can import operational technology (OT) components, including device services, locations, devices, and values, and view them in the Physical Assets section of Data Catalog in a hierarchical structure. With the Physical Assets feature, you can understand how data flows from physical sources into analytical systems, enabling better traceability and context. Additionally, users can enrich asset nodes with business terms, policies, lineage, and metadata to strengthen data governance and compliance. For more information, see [Physical Assets](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-physical-assets "mention") in the [Use Pentaho Data Catalog](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ "mention") guide.

To use the Physical Assets feature in Data Catalog, you must first configure the Physical Assets service. This involves completing the following procedures:

* [Enable the Physical Assets service in Data Catalog](#enable-the-physical-assets-service-in-data-catalog)
* [Configure Pentaho Edge for the Physical Assets service](#configure-pentaho-edge-for-the-physical-assets-service)

**Note:** The configuration steps assume Data Catalog is already installed. For installation instructions, see[Install Data Catalog](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/install-pentaho-data-catalog/install-data-catalog "mention") in the [Install Pentaho Data Catalog](https://app.gitbook.com/s/Njj4joO63OgOTabje2xP/ "mention") guide.

### Enable the Physical Assets service in Data Catalog

Perform the following steps to enable the Physical Assets service in the existing Data Catalog deployment.

1. Log in to the server where Data Catalog is installed.
2. Go to the Data Catalog Docker deployment configuration directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment/conf
   ```
3. Open the `.env` (environment configuration) file.

   ```
   vi .env
   ```

   If the `.env` file does not exist, create it and save the file before proceeding.
4. Add or update the following lines.

   ```
   COMPOSE_PROFILES=core,mongodb,collab,pdso,mdm,physical-assets
   ASSET_HIERARCHY_URL=/physical-assets-service
   ```
5. Add the Pentaho Edge connection details:

   ```
   PENTAHO_EDGE_URL=http://<PE-IP>:4000
   PENTAHO_EDGE_USERNAME_PASSWORD=admin:admin
   PENTAHO_EDGE_BACKEND_URL=https://<PE-IP>:8443
   ```

   Replace `<PE-IP>` with the IP where Pentaho Edge is installed.
6. Restart Data Catalog to apply changes:

   ```
   cd /pdc-docker-deployment
   ./pdc.sh up
   ```

You have successfully enabled the Physical Assets service in the Data Catalog deployment. The service is now active and ready to connect with Pentaho Edge to receive physical assets metadata.

***

### Configure Pentaho Edge for the Physical Assets service

Perform the following steps to configure Pentaho Edge to connect it to Data Catalog.

1. Clone the [Pentaho Edge installer repository](https://github.com/pentaho/edge-installer/tree/release-10.3.0) and navigate to the installer folder:

   ```
   git clone <repo-url>
   cd installer

   ```
2. Edit the `docker-compose-pentaho-edge.yml` file:

   ```
   ENABLE_ASSET_HIERARCHY_FEATURE=true
   ```
3. Save and close the `docker-compose-pentaho-edge.yml` file.
4. Open the `.env` file:

   ```
   vi .env
   ```
5. Update the following properties:

   ```
   PDC_ASSET_HIE_SERVICE_BASE_URL=https://<PDC-IP>/physical-assets-service/api/v1/assets
   AUTH_URL=https://<PDC-IP>/keycloak
   PDC_INSECURE_SKIP_VERIFY=true
   ENABLE_ASSET_HIERARCHY_FEATURE=true

   ```

   **Note:**

   * Replace the `<PDC-IP>` address of the URL with the IP where `pdc-docker-deployment` is installed.
   * Use the FQDN instead of the IP address if needed.

     ```
     PDC_ASSET_HIE_SERVICE_BASE_URL=https://<FQDN>/physical-assets-service/api/v1/assets
     AUTH_URL=https://<FQDN>
     PDC_INSECURE_SKIP_VERIFY=true
     ENABLE_ASSET_HIERARCHY_FEATURE=true

     ```
6. Add authentication properties:

   ```
   AUTH_USERNAME=
   AUTH_PASSWORD=
   AUTH_CLIENT_ID=
   AUTH_REALM=

   ```
7. Run the Edge installer script:

   ```
   ./install.sh
   ```
8. When prompted, provide a user ID and password.

You have successfully configured Pentaho Edge to support the Physical Assets hierarchy and configured the connection to Data Catalog. You can now view OT assets in the Physical Assets in Data Catalog.

***

## Configure PDI to send lineage to Data Catalog

You can configure Pentaho Data Integration (PDI) to write lineage information from key lineage events into the Data Catalog metadata store. When configured, PDI writes lineage metadata for supported lineage events to the Data Catalog metadata store. Data Catalog continuously runs an API that reads the lineage information from PDI. Both PDI and Data Catalog support the OpenLineage\
framework for data lineage collection and analysis.

See [Data lineage](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/pdc-lineage/pdc-data-lineage-cp) in [Use Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/RAKLVv06oBKpy9VLbw7P/) guide for information on the specific lineage events that are supported.

{% hint style="info" %}
You must perform these steps on PDI.
{% endhint %}

Before you begin this task, turn off PDI and the Pentaho Server.

Perform the following steps to set up PDI to send lineage metadata to Data Catalog.

1. On the [Support Portal](https://support.pentaho.com/hc/en-us) home page, sign in using the Pentaho support username and password provided in your Pentaho Welcome Packet.\
   If you don't have credentials, contact your PDI administrator.
2. On the **Pentaho** card, click **Download**.
3. Navigate to the Marketplace location with plugin downloads.
4. Download the **PDI OpenLineage** plugin.
5. Extract the downloaded package.
6. Run the installer for PDI:
   1. Run `install.sh` if on Linux, or `install.bat` if on Windows.
   2. Install in the `<data-integration>` folder.
7. Run the installer for Pentaho Server:
   1. Run `install.sh` if on Linux, or `install.bat` if on Windows.
   2. Install in the `<pentaho-server>` folder.

      ```
      ./install.sh -t /full/path/to/data-integration
      ```

      **Note:** To view lineage information in Data Catalog, ensure that the data connections and tables used in your PDI transformations are already mapped in the **Data Canvas**. If there are no connections, connections will be created by metadata push using APIs only for Lineage purposes.
8. Create a `config.yml` file, adding the correct users and passwords for your environment, and the URL for Data Catalog.

   There is an example in the `readme.txt` file:

   <pre class="language-yaml" data-title="Example of a configuration file"><code class="lang-yaml">version: 0.0.1
   consumers:
    console:
    file:
     - path: /path/to/file
    http:
     - name: Marquez
      url: http://localhost:5001
     - name: PDC
      url: https://pdc.example.com
      endpoint: /lineage/api/events
      authenticationParameters:
       endpoint: /keycloak/realms/pdc/protocol/openid-connect/token
       username: user
       password: pass
       client_id: pdc-client-in-keycloak
       scope: openid
   </code></pre>

   ```
   ```
9. Edit the `~/.kettle/kettle.properties` file and add the following properties:

   ```
   KETTLE_OPEN_LINEAGE_CONFIG_FILE=</full/path/to/your/openlineage/config.yml>  
   KETTLE_OPEN_LINEAGE_ACTIVE=true
   ```
10. Restart PDI and the Pentaho Server.

{% hint style="success" %}
You have successfully configured the PDI OpenLineage plugin. PDI now sends lineage metadata to Data Catalog.
{% endhint %}

## Integrate Active Directory with Pentaho Data Catalog

You can integrate Microsoft Active Directory (AD) with Pentaho Data Catalog (PDC) to enable users of AD to have single sign-on access to PDC. Part of this integration includes configuring the Keycloak identity and access management tool to use AD as an identity provider.

The configuration includes the following topics:

* [Verify the LDAP server configuration](#verify-the-ldap-server-configuration)
* [Configure the LDAP provider](#configure-the-ldap-provider)
* [(Optional) Connect to AD using the LDAP server's SSL certificate](#connect-to-a-d-using-the-ldap-servers-ssl-certificate-optional)
* [Configure LDAP mappers in Keycloak](#configure-ldap-mappers-in-keycloak)
* [Configure PDC permissions for an AD user](#configure-pdc-permissions-for-an-a-d-user)

{% hint style="info" %}
After importing AD users to PDC, you need to perform the following operations from Active Directory, because they can no longer be done from the Data Catalog User Management page:

* Edit a user
* Add a new user
* Delete a user
  {% endhint %}

### Verify the LDAP server configuration

To integrate Active Directory with Pentaho Data Catalog, you need to integrate Lightweight Directory Access Protocol (LDAP) with Keycloak. You first need to check that your LDAP server is configured correctly.

For detailed information on how to configure LDAP in your environment, consult your LDAP server documentation.

You should have the following components in an example configuration:

* **Base DN**: Base Distinguished Name, such as: `dc=example,dc=com`, where `dc` is the domain component. The Base DN is the root entry where you want to start your LDAP searches.
* **User DN**: User Distinguished Name, such as: `ou=users,dc=example,dc=com`, where `ou` is the organizational unit and dc is the domain component.
* **Groups DN**: Groups Distinguished Name, such as: `ou=groups,dc=example,dc=com`, where `ou` is the organizational unit and `dc` is the domain component.

#### Next steps

* [Configure the LDAP provider](#configure-the-ldap-provider)
* [Connect to AD using the LDAP server's SSL certificate (Optional)](#connect-to-a-d-using-the-ldap-servers-ssl-certificate-optional)
* [Configure LDAP mappers in Keycloak](#configure-ldap-mappers-in-keycloak)
* [Configure PDC permissions for an AD user](#configure-pdc-permissions-for-an-a-d-user)

### Configure the LDAP provider

To integrate Active Directory (AD) with Pentaho Data Catalog (PDC), you need to configure the LDAP provider for PDC in the Keycloak interface.

Use the following steps to configure the LDAP provider:

1. Navigate to your Keycloak admin console (such as `https://<FQDN>/keycloak/`) and log in with admin credentials.
2. Select the PDC realm.

   If you haven't already configured an LDAP provider, click **Add provider** and select **ldap**. If you have an existing LDAP provider, click on it to edit.
3. Enter the following information for the LDAP provider:

   <table><thead><tr><th width="184.4444580078125">Field</th><th>Value</th></tr></thead><tbody><tr><td>Vendor</td><td>Active Directory</td></tr><tr><td>Connection URL</td><td><code>ldap://*&#x26;lt;LDAP\_SERVER&#x26;gt;*:*&#x26;lt;PORT&#x26;gt;*</code> such as: <code>ldap://localhost:389</code></td></tr></tbody></table>
4. Click **Test connection**.

   You should get a success message.
5. Enter the following information on the remainder of the page:

   <table><thead><tr><th width="184.4444580078125">Field</th><th>Value</th></tr></thead><tbody><tr><td>Bind type</td><td>Select <strong>simple</strong></td></tr><tr><td>Bind DN</td><td>DN for your LDAP admin user, such as: <code>cn=administrator,dc=example,dc=com</code></td></tr><tr><td>Bind credentials</td><td>Password for the LDAP admin user</td></tr></tbody></table>
6. Click **Test authentication**.

   You should get a success message.

The LDAP provider is configured for use with AD.

* [Connect to AD using the LDAP server's SSL certificate (Optional)](#connect-to-a-d-using-the-ldap-servers-ssl-certificate-optional)
* [Configure LDAP mappers in Keycloak](#configure-ldap-mappers-in-keycloak)
* [Configure PDC permissions for an AD user](#configure-pdc-permissions-for-an-a-d-user)

### Connect to AD using the LDAP server's SSL certificate (Optional)

When you use an LDAP server with Pentaho Data Catalog (PDC), you can use the LDAP server's SSL certificate to securely connect to Active Directory (AD). This is an optional step in integrating AD with PDC.

For more information on integrating AD with PDC, see [Integrate Active Directory with Pentaho Data Catalog](#integrate-active-directory-with-pentaho-data-catalog). Refer to [Keycloak documentation](https://www.keycloak.org/docs/latest/server_admin/index.html) if necessary.

Perform the following steps to use the LDAP server's SSL certificate to connect to AD.

1. To retrieve the certificate from your LDAP server, enter the following command:

   `openssl s_client -connect ldap.example.com:636 -showcerts`
2. Copy the entire certificate chain (from `-----BEGIN CERTIFICATE----- to -----END CERTIFICATE-----`) and save it to a file, such as `ldap-cert.pem`.
3. Update the `*&lt;PDC\_INSTALL\_LOCATION&gt;*/conf/extra-certs/bundle.pem` file with the LDAP server’s SSL certificate, where `*&lt;PDC\_INSTALL\_LOCATION&gt;*` is the directory where PDC is installed.
4. Restart PDC services by entering the following command:

   `sh pdc.sh restart`
5. Log in to the Keycloak admin console (`https://*&lt;FQDN&gt;*/keycloak/`).
6. Navigate to the PDC realm.
7. Click **User Federation**.
8. Click the LDAP provider to edit it.
9. Enter the following LDAP settings:

<table><thead><tr><th width="191.7777099609375">Field</th><th>Value</th></tr></thead><tbody><tr><td>UI display name</td><td>Name to display, such as LDAPS</td></tr><tr><td>Vendor</td><td>Select <strong>Active Directory</strong></td></tr><tr><td>Connection URL</td><td><code>ldaps://*&#x26;lt;LDAP\_SERVER&#x26;gt;*:*&#x26;lt;PORT&#x26;gt;*</code>such as: <code>ldaps://ldap.example.com:636</code></td></tr></tbody></table>

10\. Click **Test connection**.\
You should see a success message.

11\. Enter the remaining LDAP connection and authentication settings:

<table><thead><tr><th width="164">Field</th><th>Value</th></tr></thead><tbody><tr><td>Bind type</td><td>Select <strong>simple</strong></td></tr><tr><td>Bind DN</td><td>DN to bind to the LDAP server, such as: <code>cn=admin,dc=example,dc=com</code>.</td></tr><tr><td>Bind credentials</td><td>password for the Bind DN</td></tr></tbody></table>

12\. Click **Test authentication**.\
You should see a success message.

13\. Enter values for the required LDAP searching and updating settings:

<table><thead><tr><th width="220.6666259765625">Field</th><th>Value</th></tr></thead><tbody><tr><td>Edit mode</td><td>It is a best practice to set this to <code>Readonly</code></td></tr><tr><td>Users DN</td><td>Specify the DN where the user entries are located, such as: <code>ou=users,dc=example,dc=com</code></td></tr><tr><td>Username LDAP attribute</td><td><code>cn</code></td></tr><tr><td>RDN LDAP attribute</td><td><code>cn</code></td></tr><tr><td>UUID LDAP attribute</td><td><code>objectGUID</code></td></tr><tr><td>User object classes</td><td><code>person, organizationalPerson, user</code></td></tr></tbody></table>

14\. Click **Save** to save the configuration.

AD is set up to use the SSL certificate of the LDAP server for a secure connection.

Optionally, you can configure the following settings:

* Set how often Keycloak should sync with LDAP.
* Set periodic full sync and periodic changed users sync.

### Configure LDAP mappers in Keycloak

To integrate Active Directory (AD) with Pentaho Data Catalog (PDC), you need to configure LDAP mappers so that PDC has the necessary information (such as usernames, email addresses, or group memberships) to connect to an LDAP directory.

* [Verify the LDAP server configuration](#verify-the-ldap-server-configuration)
* [Configure the LDAP provider](#configure-the-ldap-provider)
* [Connect to AD using the LDAP server's SSL certificate (Optional)](#connect-to-a-d-using-the-ldap-servers-ssl-certificate-optional)
* Make sure you know the correct attribute name used in your LDAP directory for usernames.

The Keycloak LDAP mapper translates attributes stored in an LDAP directory into the corresponding attributes needed by PDC.

Use the following steps in Keycloak to configure the LDAP mappers for Data Catalog. See [Keycloak documentation](https://www.keycloak.org/documentation.html) for more information.

1. In your Keycloak admin console (such as `https://<FQDN>/keycloak/`), log in with admin credentials.
2. Select the PDC realm and go to the User Federation settings.
3. Click the LDAP provider and go to the Mappers tab.
4. Map the LDAP attribute for the username.
5. Map other user attributes as needed (such as email, first name, last name).
6. To add additional mappers to assign default roles for the users being imported from AD, enter the following settings under **User federation** > **Settings** > **Mapper details**.

   For the Business User role:

   <table><thead><tr><th width="145.5555419921875">Field</th><th>Value</th></tr></thead><tbody><tr><td><strong>Name</strong></td><td>Business_User_Role_Mapper_To_LDAP_USERS</td></tr><tr><td><strong>Mapper type</strong></td><td>hardcoded-ldap-role-mapper</td></tr><tr><td><strong>Role</strong></td><td>Business_User (select from menu and click <strong>Assign</strong>)</td></tr></tbody></table>
7. Click **Save**.
8. Repeat step 6 for the Data User role, using the following values:

   <table><thead><tr><th width="134.44439697265625">Field</th><th>Value</th></tr></thead><tbody><tr><td>Name</td><td>Data_User_Role_Mapper_To_LDAP_USERS</td></tr><tr><td>Mapper type</td><td>hardcoded-ldap-role-mapper</td></tr><tr><td>Role</td><td>Data_User (select from menu and click <strong>Assign</strong>)</td></tr></tbody></table>
9. Click **Save**.
10. Save the configuration.
11. From the Action menu, click **Sync all users** to import users from LDAP.

    A success message displays.

    When users are synced from AD, the default PDC realm assigns the Business User and Data User roles to all the users.

    **Note:** PDC applies limits for licensing when users receive one or more of the following roles:

    * Business Steward
    * Data Steward
    * Data Developer
    * Admin
12. Go to **Users** and verify that the users were imported correctly into Keycloak.

{% hint style="success" %}
The LDAP mappers are configured.
{% endhint %}

### Configure PDC permissions for an AD user

The last step in integrating Active Directory (AD) with Pentaho Data Catalog (PDC) is to set up permissions in PDC for the AD users.

* [Verify the LDAP server configuration](#verify-the-ldap-server-configuration)
* [Configure the LDAP provider](#configure-the-ldap-provider)
* [Connect to AD using the LDAP server's SSL certificate (Optional)](#connect-to-a-d-using-the-ldap-servers-ssl-certificate-optional)
* [Configure LDAP mappers in Keycloak](#configure-ldap-mappers-in-keycloak)

Use the following steps to create and verify an AD user.

1. Log into Data Catalog as the admin user.
2. Click **Management**, and on the **Users & Communities** card, click **Users**.
3. Check that the imported users display correctly and make any needed adjustments.
4. Select an AD user and assign a community or role to the user.
5. Click **Save**, and log out.
6. Log in as the AD user to verify the login is working properly.

{% hint style="success" %}
Active Directory is now integrated with PDC.
{% endhint %}

## Integrate Okta with Pentaho Data Catalog

You can integrate Okta authentication with Pentaho Data Catalog for the added security provided by multi-factor authentication. To integrate Okta with Pentaho Data Catalog, you need to configure Okta in parallel with the Keycloak identity and access management tool.

The steps in the integration process are:

* [Add an OpenID Connect provider in Keycloak](#add-an-oidc-provider-in-keycloak)
* [Add an OpenID Connect application in Okta](#add-an-oidc-application-in-okta)
* [Set up security in Okta](#set-up-security-in-okta)
* [Configure an identity provider in Keycloak](#configure-an-identity-provider-in-keycloak)
* [Sign in to PDC using Okta](#sign-in-to-pentaho-data-catalog-using-okta)

### Add an OIDC provider in Keycloak

To integrate Okta with Pentaho Data Catalog, you need to set up an identity provider in Keycloak. Keycloak uses the OpenID Connect (OIDC) protocol to connect to identity providers.

If necessary, see the [Keycloak documentation](https://www.keycloak.org/docs/latest/server_admin/index.html#_identity_broker_oidc) to complete this task.

Perform the following steps in the Keycloak interface:

1. Log in to Keycloak and select the **PDC** realm.

   If a PDC realm does not already exist, consult your PDC administrator or see [Creating a realm](https://www.keycloak.org/docs/latest/server_admin/index.html#proc-creating-a-realm_server_administration_guide) in the Keycloak documentation to create one.
2. Click **Identity Providers** and select **OpenID Connect v1.0**.

   If necessary, see [OpenID Connect v1.0 identity providers](https://www.keycloak.org/docs/latest/server_admin/index.html#_identity_broker_oidc) in the Keycloak documentation.
3. Use the following steps to add an OIDC ID provider:
   1. Enter an alias in the **Alias** field.

      This populates the **Redirect URI** field, in a format like the following:

      ```
      http://localhost:8180/realms/master/broker/<alias>/endpoint
      ```
   2. Copy the Redirect URI to be used in the next task, [Add an OpenID Connect application in Okta](#add-an-oidc-application-in-okta).

{% hint style="success" %}
You have added an OpenID Connect provider in Keycloak.
{% endhint %}

Perform the following tasks:

* [Add an OpenID Connect application in Okta](#add-an-oidc-application-in-okta)
* [Set up security in Okta](#set-up-security-in-okta)
* [Configure an identity provider in Keycloak](#configure-an-identity-provider-in-keycloak)
* [Sign in to Pentaho Data Catalog using Okta](#sign-in-to-pentaho-data-catalog-using-okta)

### Add an OIDC application in Okta

The next step in integrating Okta with Pentaho Data Catalog is to add an OpenID Connect (OIDC) application in Okta.

Before beginning this task, make sure to perform this task:

* [Add an OpenID Connect provider in Keycloak](#add-an-oidc-provider-in-keycloak)

In this task, you need the Keycloak Identity Provider Redirect URI you copied in the [Add an OpenID Connect provider in Keycloak](#add-an-oidc-provider-in-keycloak) task. If necessary, see [Launch the wizard](https://help.okta.com/oie/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm) in the [Okta documentation](https://help.okta.com/oie/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm).

Perform the following steps in the Okta Admin console:

1. From the left menu, click **Applications** and then **Applications**.
2. Click **Create App Integration**.
3. Select or enter the following values:

   <table><thead><tr><th width="201.11114501953125">Field</th><th>Value</th></tr></thead><tbody><tr><td>Sign-in method</td><td><strong>OIDC – OpenID Connect</strong></td></tr><tr><td>Application type</td><td><strong>Web Application</strong></td></tr><tr><td>App integration name</td><td><strong>CatalogPlus_10.2.1</strong></td></tr><tr><td>Grant type</td><td><strong>Authorization Code</strong></td></tr><tr><td>Sign-in redirect URIs</td><td>Keycloak Identity Provider Redirect URI copied in the <a href="#add-an-oidc-provider-in-keycloak">Add OpenID Connect provider in Keycloak</a> task</td></tr></tbody></table>

   `https://<application_url>/keycloak/realms/<realm_name>/broker/<alias_name>/endpoint/logout_response`
4. For **Sign-out redirect URIs**, configure your logout URI in this format:

   For example:

   ```
   https://<ip address>/keycloak/realms/pdc/broker/okta/endpoint/logout_response
   ```
5. Continue entering values in Okta screens:

   <table><thead><tr><th width="232.22222900390625">Field</th><th>Value</th></tr></thead><tbody><tr><td>Controlled access</td><td>Select the default value, <strong>Allow everyone in your organization to access</strong></td></tr><tr><td>Enable immediate access</td><td>Clear the checkbox</td></tr></tbody></table>
6. In the **General** tab, make a note of the **Client Id** and **Client Secret** to use in the [Configure an identity provider in Keycloak](#configure-an-identity-provider-in-keycloak) task.
7. Click **Save**.
8. On the left menu, click **Applications**.
9. From the down arrow, select **Assign to Groups**.
10. Assign a group to your application.

{% hint style="success" %}
You have set up an OpenID Connect application in Okta.
{% endhint %}

Perform the following tasks:

* [Set up security in Okta](#set-up-security-in-okta)
* [Configure an identity provider in Keycloak](#configure-an-identity-provider-in-keycloak)
* [Sign in to Pentaho Data Catalog using Okta](#sign-in-to-pentaho-data-catalog-using-okta)

### Set up security in Okta

When integrating Okta with Pentaho Data Catalog, you need to set up security in Okta for the connection to PDC.

Before beginning this task, make sure to perform these tasks:

* [Add an OpenID Connect provider in Keycloak](#add-an-oidc-provider-in-keycloak)
* [Add an OpenID Connect application in Okta](#add-an-oidc-application-in-okta)

Perform the following steps in the Okta admin console:

1. On the left menu, click **Security**, then **API**, then **Default**.
2. On the **Access Policies** tab, click **Add New Access Policy**.
3. Add details for the policy and click **Create Policy**.
4. Click **Add Rule**.
5. Add details for the rule and click **Create Rule**.

{% hint style="success" %}
You have set up security for the Okta connection to PDC.
{% endhint %}

Perform the following tasks:

* [Configure an identity provider in Keycloak](#configure-ldap-mappers-in-keycloak)
* [Sign in to Pentaho Data Catalog using Okta](#sign-in-to-pentaho-data-catalog-using-okta)

### Configure an identity provider in Keycloak

To integrate Okta with Pentaho Data Catalog, you need to configure an identity provider in Keycloak. If necessary, see the Keycloak documentation.

Before beginning this task, make sure to perform these tasks:

* [Add an OpenID Connect provider in Keycloak](#add-an-oidc-provider-in-keycloak)
* [Add an OpenID Connect application in Okta](#add-an-oidc-application-in-okta)
* [Set up security in Okta](#set-up-security-in-okta)

In this task, you need the Client Id and Client Secret you noted during the [Add an OpenID Connect application in Okta](#add-an-oidc-application-in-okta) task.

Perform the following steps in the Keycloak admin console:

1. From the left menu, click **Identity providers**.
2. Click **OpenID Connect v1.0**.
3. Make sure the **Use discovery endpoint** switch is on.
4. In the **Discovery endpoint** field, enter the discovery endpoint URL in the following format:

   `https://hostname/auth/realms/master/.well-known/openid-configuration`

   The Authorization URL, Token URL, Logout URL, and User Info URL and other fields populate automatically.
5. Enter the Client Id and Client Secret noted during the [Add an OpenID Connect application in Okta](#add-an-oidc-application-in-okta) task.
6. On the **Settings** tab, select the following settings:
   * First login flow override: **First login flow override**
   * Sync mode: **Force**
7. Expand the Advanced settings and set the Scopes setting to **openid email profile** (separated by a single space).
8. Click **Save**.

{% hint style="success" %}
You have configured the identity provider in Keycloak.
{% endhint %}

Perform the following task:

* [Sign in to Pentaho Data Catalog using Okta](#sign-in-to-pentaho-data-catalog-using-okta)

### Sign in to Pentaho Data Catalog using Okta

After Pentaho Data Catalog is integrated with Okta, you have the option to log in to PDC with Okta.

Before beginning this task, make sure to perform these tasks:

* [Add an OpenID Connect provider in Keycloak](#add-an-oidc-provider-in-keycloak)
* [Add an OpenID Connect application in Okta](#add-an-oidc-application-in-okta)
* [Set up security in Okta](#set-up-security-in-okta)
* [Configure an identity provider in Keycloak](#configure-an-identity-provider-in-keycloak)

To log in to PDC using Okta, perform the following steps:

1. On the PDC login screen, click the button corresponding to the Okta alias.

   **Note:** The alias matches whatever is set for Okta OpenID Connect in Keycloak.

   In the following example, the button is labeled **CATALOG+OKTA**:

   ![Updated PDC login screen after Okta integration](https://34323290-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FcUaDtyTop3vo8cjqgjGk%2Fuploads%2Fgit-blob-b87ce9a85f69cc1e710028f2552a9f54ae78ce47%2FUpdated%20PDC%20login%20screen.png?alt=media)
2. On the Okta login screen that appears, enter the credentials for the Okta user assigned to PDC.

   Okta prompts you to enter a code.
3. To finish logging in, enter the code that Okta provides.

You have completed the integration of Okta with PDC.

## Integrate an identity provider with Data Catalog using Keycloak (SAML 2.0) <a href="#integrate-an-identity-provider-with-data-catalog-using-keycloak-saml-2.0" id="integrate-an-identity-provider-with-data-catalog-using-keycloak-saml-2.0"></a>

You can integrate an external identity provider (IdP), such as PingFederate or Ping Identity, with Data Catalog by configuring **Keycloak as a SAML 2.0 identity broker**. After you complete this integration, users authenticate with your IdP and then access Data Catalog using single sign-on (SSO). Users can also continue to sign in using local username and password if local users remain enabled.

**Prerequisites**

Make sure that you have:

* Administrative access to the target Keycloak instance.
* Valid credentials to invoke Keycloak Admin REST APIs.
* Administrative access to the IdP (for example, PingFederate).
* IdP SAML metadata (Entity ID, SSO endpoint, SLO endpoint if used, and signing certificate).
* Network connectivity between Keycloak and IdP endpoints.

{% stepper %}
{% step %}

### Collect SAML metadata from your identity provider

Before you configure Keycloak, collect the SAML metadata values required to create the SAML identity provider (IdP) instance.

**Prerequisites**

Make sure you have administrative access to your IdP console.

**Procedure**

1. Export or download the SAML metadata for the SAML application/connection that represents Keycloak as the service provider.
   * **PingFederate**: On **SP Connections**, select the service provider connection, and then select **Export Metadata**.
   * **Ping Identity**: Open the SAML application, and then select **Download Metadata** on the **Overview** tab.
2. From the metadata, record these values:
   * **IdP Entity ID** (`idpEntityId`)\
     This is the IdP `entityID` value in the metadata.
   * **Single sign-on service URL** (`singleSignOnServiceUrl`)\
     This is `SingleSignOnService Location`.
   * **Single logout service URL** (`singleLogoutServiceUrl`) (if used)\
     This is `SingleLogoutService Location`.
   * **Signing certificate (X.509)** (`signingCertificate`)\
     This is the `X509Certificate` value.

**Result**

You have the IdP metadata values needed to configure a SAML identity provider in Keycloak.
{% endstep %}

{% step %}

### Authenticate to Keycloak and retrieve realm certificates

To configure Keycloak for IdP integration, you must first authenticate to Keycloak and obtain an **admin access token**. You then use that token to call Keycloak APIs, such as retrieving the **realm certificates** that are used for signing and validation.

**Prerequisites**

Make sure you have:

* Keycloak base URL: `https://<host>/keycloak`
* Keycloak admin credentials:
  * `<admin-username>`
  * `<admin-password>`
* PDC realm name: `<pdc-realm>`

{% hint style="info" %}
**Important**: Treat the admin credentials and tokens as sensitive information. Do not store them in logs or share them in screenshots.
{% endhint %}

**Procedure**

1. To generate an admin access token, send a token request to Keycloak.

   **Endpoint**

   ```
   POST https://<host>/keycloak/realms/master/protocol/openid-connect/token
   ```

   **Headers**

   ```
   Content-Type: application/x-www-form-urlencoded
   ```

   **Body (x-www-form-urlencoded)**

   * `username=<admin-username>`
   * `password=<admin-password>`
   * `client_id=admin-cli`
   * `grant_type=password`

   **Example (PowerShell)**

   ```
   $tokenResponse = Invoke-RestMethod -Method Post `
     -Uri "https://<host>/keycloak/realms/master/protocol/openid-connect/token" `
     -ContentType "application/x-www-form-urlencoded" `
     -Body @{
       username   = "<admin-username>"
       password   = "<admin-password>"
       client_id  = "admin-cli"
       grant_type = "password"
     } -SkipCertificateCheck

   $accessToken = $tokenResponse.access_token
   $accessToken

   ```
2. Record the `access_token` value from the response.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>The token expires based on the expires_in value in the response. If the token expires, generate a new token and retry the API call.</p><p>You have an admin access token to use as Authorization: Bearer &#x3C;access-token> in Keycloak Admin API requests.</p></div>
3. To retrieve realm certificates, call the realm certificates endpoint.

   **Endpoint**

   ```
   GET https://<host>/keycloak/realms/<pdc-realm>/protocol/openid-connect/certs
   ```

   **Authentication**

   ```
   Authorization: Bearer <access-token>
   ```

   **Example (PowerShell)**

   ```
   $certs = Invoke-RestMethod -Method Get `
     -Uri "https://<host>/keycloak/realms/<pdc-realm>/protocol/openid-connect/certs" `
     -Headers @{ Authorization = "Bearer $accessToken" } `
     -SkipCertificateCheck

   $certs.keys

   ```
4. From the response, identify the signing certificate:
   1. Find the key entry with `"use": "sig"`.
   2. The certificate chain is in `x5c[]`.

      <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>If your IdP administrator requests the certificate, provide the first value in x5c[]. This is the base64-encoded X.509 certificate.</p></div>

**Result**

You retrieved the realm certificates for `<pdc-realm>`. You can now use them for verification or IdP-side configuration (if required by your organization).
{% endstep %}

{% step %}

### Create a SAML identity provider in Keycloak for Data Catalog

Create a SAML identity provider (IdP) instance in Keycloak, so Keycloak can broker authentication from your external IdP (for example, PingFederate) into the PDC realm.

**Prerequisites**

Make sure you have:

* Keycloak base URL: `https://<host>/keycloak`
* PDC realm name: `<pdc-realm>`
* SAML provider alias: `<saml-alias>` (for example, `PingFed` or `CorporateSSO`)
* A valid Keycloak admin access token: `<admin-token>`
* The following values from your IdP SAML metadata:
  * `<idp-entity-id>` (IdP Entity ID)
  * `<idp-sso-url>` (SingleSignOnService Location)
  * `<idp-slo-url>` (SingleLogoutService Location), if used
  * `<idp-signing-cert>` (X509Certificate)

{% hint style="info" %}
**Important**: In this procedure, set `"syncMode": "FORCE"`. This ensures Keycloak refreshes user details and role mappings on every login.
{% endhint %}

**Procedure**

1. Create a file named `create-saml-idp.json` and paste the following content into the file and replace placeholders with your values.

   ```
   {
     "alias": "<saml-alias>",
     "displayName": "<saml-alias>",
     "config": {
       "allowCreate": "true",
       "guiOrder": "",
       "entityId": "https://<host>/keycloak/realms/<pdc-realm>",
       "idpEntityId": "<idp-entity-id>",
       "singleSignOnServiceUrl": "<idp-sso-url>",
       "singleLogoutServiceUrl": "<idp-slo-url>",
       "backchannelSupported": "true",
       "sendIdTokenOnLogout": "true",
       "sendClientIdOnLogout": "true",
       "nameIDPolicyFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
       "principalType": "SUBJECT",
       "postBindingResponse": "true",
       "postBindingAuthnRequest": "true",
       "postBindingLogout": "true",
       "wantAuthnRequestsSigned": "true",
       "wantAssertionsSigned": "false",
       "wantAssertionsEncrypted": "false",
       "forceAuthn": "false",
       "validateSignature": "false",
       "signSpMetadata": "false",
       "loginHint": "false",
       "allowedClockSkew": 0,
       "attributeConsumingServiceIndex": 0,
       "attributeConsumingServiceName": "",
       "signingCertificate": "<idp-signing-cert>",
       "enabledFromMetadata": "true",
       "syncMode": "FORCE",
       "addExtensionsElementWithKeyInfo": "false",
       "signatureAlgorithm": "RSA_SHA256",
       "xmlSigKeyInfoKeyNameTransformer": "KEY_ID",
       "firstBrokerLoginFlowAlias": "pdc-login-flow",
       "postBrokerLoginFlowAlias": "pdc-post-login-flow"
     },
     "providerId": "saml",
     "firstBrokerLoginFlowAlias": "pdc-login-flow",
     "postBrokerLoginFlowAlias": "pdc-post-login-flow"
   }

   ```

   \
   Use this reference when replacing placeholders:

   * `idpEntityId` → IdP Entity ID\
     Source: SAML metadata root `entityID` attribute.
   * `singleSignOnServiceUrl` → IdP SSO endpoint\
     Source: `SingleSignOnService Location`.
   * `singleLogoutServiceUrl` → IdP SLO endpoint\
     Source: `SingleLogoutService Location` (if your IdP supports SLO and you use it).
   * `signingCertificate` → IdP signing certificate\
     Source: `X509Certificate` value in SAML metadata.

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><ul><li>Keep the <code>firstBrokerLoginFlowAlias</code> and <code>postBrokerLoginFlowAlias</code> values as shown unless your Keycloak administrator has configured different broker flows for Data Catalog.</li><li>When <code>backchannelSupported</code> is enabled, Keycloak uses a server-to-server logout flow: <strong>Keycloak pod → PingFederate</strong>. If this request times out, it typically indicates a network connectivity issue between the Keycloak pod and PingFederate (for example, firewall rules, DNS resolution, routing, or a blocked port).</li></ul></div>

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Tip</strong>: If you copy the <code>X509Certificate</code> value from XML, remove line breaks and extra spaces so the certificate is stored as a single continuous base64 string.</p></div>
2. Send a request to the Keycloak Admin API.

   **Endpoint**

   ```
   POST https://<host>/keycloak/admin/realms/<pdc-realm>/identity-provider/instances
   ```

   \
   **Authentication**

   ```
   Authorization: Bearer <admin-token>
   ```

   \
   **Headers**

   ```
   Content-Type: application/json
   ```

   \
   **Example**

   ```powershell
   $body = Get-Content -Raw -Path ".\create-saml-idp.json"

   Invoke-RestMethod -Method Post `
     -Uri "https://<host>/keycloak/admin/realms/<pdc-realm>/identity-provider/instances" `
     -Headers @{
       Authorization = "Bearer <admin-token>"
       "Content-Type" = "application/json"
     } `
     -Body $body `
     -SkipCertificateCheck

   ```

   \
   **Example**

   ```powershell
   curl -k -X POST "https://<host>/keycloak/admin/realms/<pdc-realm>/identity-provider/instances" \
     -H "Authorization: Bearer <admin-token>" \
     -H "Content-Type: application/json" \
     -d @create-saml-idp.json

   ```
3. Confirm the request succeeds.\
   A successful request typically returns **HTTP 201 (Created)** or **HTTP 204 (No Content),** depending on your Keycloak version and configuration.

**Result**

A SAML identity provider instance named `<saml-alias>` is created in the `<pdc-realm>` realm.
{% endstep %}

{% step %}

### Configure SAML mappers in Keycloak for Data Catalog

SAML mappers tell Keycloak how to translate identity provider (IdP) attributes (for example, Ping Identity claims) into:

* **Keycloak user attributes** (email, username, first name, last name)
* **Keycloak roles** that Data Catalog uses for authorization (Admin, Data Steward, and so on)

Configure the user attribute mappers first, and then configure the role mappers.

**Prerequisites**

Make sure you have:

* Keycloak base URL: `https://<host>/keycloak`
* PDC realm name: `<pdc-realm>`
* Keycloak SAML identity provider alias: `<saml-alias>`
* A valid Keycloak admin access token: `<admin-token>`
* The Ping Identity attribute names used for:
  * Email
  * Given name
  * Family name
  * Group membership (for example, `memberOf`)
* The Ping Identity group values that should map to Data Catalog roles (one group value per role)

{% hint style="info" %}
**Important**: Set `syncMode` to `FORCE` in every mapper. This ensures Keycloak refreshes user details and role assignments on every login and prevents stale role assignments.
{% endhint %}

**Mapper endpoint reference**

All mapper requests use the same endpoint.

**Endpoint**

```
POST https://<host>/keycloak/admin/realms/<pdc-realm>/identity-provider/instances/<saml-alias>/mappers
```

**Authentication**

```
Authorization: Bearer <admin-token>
```

**Headers**

```
Content-Type: application/json
```

**Procedure**

1. Create the following user attribute mappers so Keycloak can populate user profile fields for IdP users.\
   **Tip**: If you are using a stable email address as NameID at your IdP, configure the username mapper to use ${NAMEID} as shown in this procedure.

{% tabs %}
{% tab title="Email mapper" %}
Create a file named `mapper-email.json` :

```powershell
{
  "name": "email-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-email-attribute-name>",
    "attribute.friendly.name": "",
    "attribute.name.format": "ATTRIBUTE_FORMAT_BASIC",
    "user.attribute": "email"
  },
  "identityProviderMapper": "saml-user-attribute-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}

```

{% endtab %}

{% tab title="Username mapper" %}
Create a file named `mapper-username.json`:

```powershell
{
  "name": "username-mapper",
  "config": {
    "syncMode": "FORCE",
    "template": "${NAMEID}",
    "target": "LOCAL"
  },
  "identityProviderMapper": "saml-username-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}

```

{% endtab %}

{% tab title="First name mapper" %}
Create a file named `mapper-firstname.json`:

```powershell
{
  "name": "first-name-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-given-name-attribute>",
    "attribute.friendly.name": "",
    "attribute.name.format": "ATTRIBUTE_FORMAT_BASIC",
    "user.attribute": "firstName"
  },
  "identityProviderMapper": "saml-user-attribute-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}

```

{% endtab %}

{% tab title="Last name mapper" %}
Create a file named `mapper-lastname.json`:

```powershell
{
  "name": "last-name-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-family-name-attribute>",
    "attribute.friendly.name": "",
    "attribute.name.format": "ATTRIBUTE_FORMAT_BASIC",
    "user.attribute": "lastName"
  },
  "identityProviderMapper": "saml-user-attribute-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}

```

{% endtab %}
{% endtabs %}

2. Create each user attribute mapper in Keycloak. For each JSON file, send a POST request to create the mapper.\
   **Example**

   ```powershell
   $body = Get-Content -Raw -Path ".\mapper-email.json"

   Invoke-RestMethod -Method Post `
     -Uri "https://<host>/keycloak/admin/realms/<pdc-realm>/identity-provider/instances/<saml-alias>/mappers" `
     -Headers @{
       Authorization = "Bearer <admin-token>"
       "Content-Type" = "application/json"
     } `
     -Body $body `
     -SkipCertificateCheck

   ```

   \
   Repeat the request for:

   * `mapper-username.json`
   * `mapper-firstname.json`
   * `mapper-lastname.json`\
     Keycloak can create and update IdP users with populated email, username, first name, and last name values.
3. Before you create role mappers, confirm the Ping Identity values that represent membership for each Data Catalog role.\
   Record the values your IdP provides:

   * Group attribute name: `<ping-group-attribute-name>` (for example, `memberOf`)
   * Admin group value: `<ping-admin-group-value>`
   * Business Steward group value: `<ping-business-steward-group-value>`
   * Business User group value: `<ping-business-user-group-value>`
   * Data Developer group value: `<ping-data-developer-group-value>`
   * Data Steward group value: `<ping-data-steward-group-value>`
   * Data Storage Administrator group value: `<ping-data-storage-admin-group-value>`
   * Data User group value: `<ping-data-user-group-value>`&#x20;

   <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Important</strong>: Create <strong>one role mapper per Data Catalog role</strong>. If you do not create a mapper for a role, users will not receive that role through the IdP.</p></div>
4. Create role mappers (one mapper per Data Catalog role) to assign a Keycloak role when a Ping Identity attribute contains a specific group value.<br>

   **Role mapper rules**

   * Set `syncMode` to `FORCE` in every role mapper.
   * Update these values in every mapper:
     * `attribute.name` to the Ping Identity group attribute name (for example, `memberOf`)
     * `attribute.value` to the group value that represents the role
     * `identityProviderAlias` to the Keycloak SAML IdP alias (`<saml-alias>`)

{% tabs %}
{% tab title="Admin role mapper" %}
Create a file named `role-admin.json`:

```powershell
{
  "name": "admin-role-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-group-attribute-name>",
    "attribute.friendly.name": "",
    "attribute.value": "<ping-admin-group-value>",
    "role": "Admin"
  },
  "identityProviderMapper": "saml-role-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}
```

{% endtab %}

{% tab title="Business Steward role mapper" %}
Create a file named `role-business-steward.json`:

```powershell
{
  "name": "business-steward-role-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-group-attribute-name>",
    "attribute.friendly.name": "",
    "attribute.value": "<ping-business-steward-group-value>",
    "role": "Business_Steward"
  },
  "identityProviderMapper": "saml-role-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}
```

{% endtab %}

{% tab title="Business User role mapper" %}
Create a file named `role-business-user.json`:

```powershell
{
  "name": "business-user-role-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-group-attribute-name>",
    "attribute.friendly.name": "",
    "attribute.value": "<ping-business-user-group-value>",
    "role": "Business_User"
  },
  "identityProviderMapper": "saml-role-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}
```

{% endtab %}

{% tab title="Data Developer role mapper" %}
Create a file named `role-data-developer.json`:

```powershell
{
  "name": "data-developer-role-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-group-attribute-name>",
    "attribute.friendly.name": "",
    "attribute.value": "<ping-data-developer-group-value>",
    "role": "Data_Developer"
  },
  "identityProviderMapper": "saml-role-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}
```

{% endtab %}

{% tab title="Data Steward role mapper" %}
Create a file named `role-data-steward.json`:

```
{
  "name": "data-steward-role-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-group-attribute-name>",
    "attribute.friendly.name": "",
    "attribute.value": "<ping-data-steward-group-value>",
    "role": "Data_Steward"
  },
  "identityProviderMapper": "saml-role-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}
```

{% endtab %}

{% tab title="Data Steward role mapper" %}
Create a file named `role-data-steward.json`:

```powershell
{
  "name": "data-steward-role-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-group-attribute-name>",
    "attribute.friendly.name": "",
    "attribute.value": "<ping-data-steward-group-value>",
    "role": "Data_Steward"
  },
  "identityProviderMapper": "saml-role-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}
```

{% endtab %}

{% tab title="Data Storage Administrator role mapper" %}
Create a file named `role-data-storage-admin.json`:

```powershell
{
  "name": "data-storage-administrator-role-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-group-attribute-name>",
    "attribute.friendly.name": "",
    "attribute.value": "<ping-data-storage-admin-group-value>",
    "role": "Data_Storage_Administrator"
  },
  "identityProviderMapper": "saml-role-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}
```

{% endtab %}

{% tab title="Data User role mapper" %}
Create a file named `role-data-user.json`:

```powershell
{
  "name": "data-user-role-mapper",
  "config": {
    "syncMode": "FORCE",
    "attribute.name": "<ping-group-attribute-name>",
    "attribute.friendly.name": "",
    "attribute.value": "<ping-data-user-group-value>",
    "role": "Data_User"
  },
  "identityProviderMapper": "saml-role-idp-mapper",
  "identityProviderAlias": "<saml-alias>"
}
```

{% endtab %}
{% endtabs %}

5. To create each role mapper in Keycloak, send a POST request to create the mapper for each role mapper JSON file.

   **Example**

   ```powershell
   $body = Get-Content -Raw -Path ".\role-admin.json"

   Invoke-RestMethod -Method Post `
     -Uri "https://<host>/keycloak/admin/realms/<pdc-realm>/identity-provider/instances/<saml-alias>/mappers" `
     -Headers @{
       Authorization = "Bearer <admin-token>"
       "Content-Type" = "application/json"
     } `
     -Body $body `
     -SkipCertificateCheck
   ```
6. Repeat the request for each mapper file you created.\
   Keycloak assigns the correct Data Catalog roles based on Ping Identity group membership.

**Result**

Keycloak mappers are configured for:

* User attributes (email, username, first name, last name)
* Role assignments (one mapper per Data Catalog role)

Users signing in through the SAML IdP are provisioned with the expected identity details and permissions.
{% endstep %}
{% endstepper %}

## Configure Metadata Request Access in Data Catalog

You can configure Metadata Request Access in Data Catalog to manage user requests for metadata access. This feature uses the Access Request Service, a backend service that integrates with ticketing tools such as Jira or ServiceNow. The service creates, tracks, and updates access requests, and synchronizes their status between Data Catalog and the external system. This guide depicts how to configure Metadata Request Access in Data Catalog.

By default, only metadata access requests are managed in Data Catalog. Data access requests are routed to an integrated ticketing system.

Before you begin,

* Ensure you have:
  * Network connectivity between the service and Jira or ServiceNow.
  * Credentials for authenticating with your identity provider and your ticketing system.
* Confirm that the external system (Jira or ServiceNow) contains a custom field to store the access request status (for example, *Access Status* with values *Approved* and *Rejected*). For more information, see [Integrating ServiceNow with Data Catalog](https://docs.pentaho.com/pdc-admin/ldc-advanced-configuration-ut_cp#integrating-servicenow-with-data-catalog) and [Integrating Jira with Data Catalog](https://docs.pentaho.com/pdc-admin/ldc-advanced-configuration-ut_cp#integrating-servicenow-with-data-catalog).
* Gather the following details:
  * Service account credentials for Jira or ServiceNow.
  * Database connection parameters.
  * Authentication service endpoint, client ID, and credentials.

Perform the following steps to configure Metadata Request Access in Data Catalog:

1. Configure the service by setting the required environment variables\[PA1] .\
   Use either your deployment tool (for example, Docker Compose, Kubernetes, or Helm) or a configuration file.\
   \
   **Key environment variables**

   | Variable                                          | Description                                                      | Required | Example             |
   | ------------------------------------------------- | ---------------------------------------------------------------- | -------- | ------------------- |
   | TENANT\_NAME                                      | Tenant identifier                                                | Yes      | your-tenant         |
   | ACCESS\_REQUEST\_SERVICE\_DEFAULT\_ASSIGNEE\[SR5] | Default assignee email if no auto-assignment                     | Yes      | <admin@example.com> |
   | STATUS\_FETCHER\_INTERVAL                         | Poll interval for status updates; supports cron or @every syntax | Yes      | @every 5m           |
   | PAGINATION\_MAX\_RESULTS\_SIZE                    | Maximum results per API request                                  | No       | 1000                |
   | LOG\_LEVEL                                        | Logging verbosity (info, debug, warn, error)                     | No       | info                |

   \
   **CAUTION**: The value of `ACCESS_REQUEST_SERVICE_DEFAULT_ASSIGNEE` must match a user created in Data Catalog with the Admin role using User Management. \
   \
   **Authentication settings**

   | Variable         | Description                  | Required | Example                    |
   | ---------------- | ---------------------------- | -------- | -------------------------- |
   | AUTH\_URL        | Authentication endpoint URL  | Yes      | <https://auth.example.com> |
   | AUTH\_HOST       | Authentication host and port | Yes      | auth-host:5000             |
   | AUTH\_CLIENT\_ID | Client ID for authentication | Yes      | generic-client-id          |
   | AUTH\_USER\_NAME | Username for authentication  | Yes      | generic-user               |
   | AUTH\_PASSWORD   | Password for authentication  | Yes      | generic-password           |

   \
   **Database settings**

   | Variable      | Description                 | Required | Example             |
   | ------------- | --------------------------- | -------- | ------------------- |
   | DB\_URL       | Database host               | Yes      | generic-db-host     |
   | DB\_PORT      | Database port               | Yes      | 5432                |
   | DB\_NAME      | Database name               | Yes      | generic\_db         |
   | DB\_USER      | Database user               | Yes      | generic-db-user     |
   | DB\_PASSWORD  | Database password           | Yes      | generic-db-password |
   | DB\_SSL\_MODE | SSL mode (disable, require) | Yes      | disable             |

   \
   **Ticketing provider selection**

   | Variable       | Description                                  | Required | Example |
   | -------------- | -------------------------------------------- | -------- | ------- |
   | PROVIDER\_TOOL | Select ticketing system (Jira or ServiceNow) | Yes      | Jira    |

   \
   **If Jira is used**

   | Variable                              | Description                      | Required | Example                    |
   | ------------------------------------- | -------------------------------- | -------- | -------------------------- |
   | JIRA\_URLrestart                      | Jira server URL                  | Yes      | <https://jira.example.com> |
   | JIRA\_PROJECT\_NAME                   | Project key or name              | Yes      | GENERIC                    |
   | JIRA\_USER\_NAME                      | Jira service account username    | Yes      | <jira.user@example.com>    |
   | JIRA\_PASSWORD                        | Jira password or API token       | Yes      | generic-jira-password      |
   | JIRA\_ACCESS\_STATUS\_KEY             | Jira field key for access status | Yes      | Access Status              |
   | JIRA\_ACCESS\_STATUS\_APPROVED\_VALUE | Field value for approval         | Yes      | Approved                   |
   | JIRA\_ACCESS\_STATUS\_REJECTED\_VALUE | Field value for rejection        | Yes      | Rejected                   |

   \
   **If ServiceNow is used**

   | Variable                                    | Description                            | Required | Example                          |
   | ------------------------------------------- | -------------------------------------- | -------- | -------------------------------- |
   | SERVICENOW\_URL                             | ServiceNow instance URL                | Yes      | <https://servicenow.example.com> |
   | SERVICENOW\_USER\_NAME                      | ServiceNow service account username    | Yes      | <servicenow.user@example.com>    |
   | SERVICENOW\_PASSWORD                        | ServiceNow password                    | Yes      | generic-snow-password            |
   | SERVICENOW\_CLIENT\_ID                      | ServiceNow client ID                   | Yes      | snow-client-id                   |
   | SERVICENOW\_CLIENT\_SECRET                  | ServiceNow client secret               | Yes      | snow-client-secret               |
   | SERVICENOW\_ACCESS\_STATUS\_KEY             | ServiceNow field key for access status | Yes      | u\_access\_status                |
   | SERVICENOW\_ACCESS\_STATUS\_APPROVED\_VALUE | Field value for approval               | Yes      | Approved                         |
   | SERVICENOW\_ACCESS\_STATUS\_REJECTED\_VALUE | Field value for rejection              | Yes      | Rejected                         |
2. Save your configuration and restart the access-request-service container.
3. (optional) Once you restarted the access-request-service container, you can verify the configuration:
   1. Submit a metadata request in the PDC UI.
   2. Confirm that a corresponding ticket is created in Jira or ServiceNow.
   3. Update the ticket status to *Approved* or *Rejected*.
   4. Confirm that PDC reflects the updated status after the poll interval.

{% hint style="success" %}
You have configured Metadata Request Access in Data Catalog. Users can request metadata access, and the request is automatically created and tracked in the configured ticketing system. Approved or rejected statuses are synchronized back to PDC.
{% endhint %}

## Integrating Jira with Pentaho Data Catalog

You can integrate Jira as an external ticketing system with Data Catalog to manage data access requests. This guide describes how to configure Jira integration using a `config.yaml` file or environment variables, and how to create a custom field in Jira to use for the data access request statuses.

{% hint style="info" %}
You can set any administrative user as the default administrator to manage data access requests. However, there can be only one default administrator set, because the `ACCESS_REQUEST_SERVICE_DEFAULT_ASSIGNEE` environment variable only supports a single user. If necessary, the default administrator can edit a data access request to assign it to another administrative user.
{% endhint %}

To integrate Jira with Data Catalog, perform the following tasks:

1. Choose one of the following configuration methods:
   * [Integrate Jira with Data Catalog using a config.yaml file](#integrate-jira-with-data-catalog-using-a-config.yaml-file)
   * [Integrate Jira with Data Catalog using environment variables](#integrate-jira-with-data-catalog-using-environment-variables)
2. [Add a custom field to Jira](#add-a-custom-field-to-jira)

### Integrate Jira with Data Catalog using a config.yaml file

To integrate the Jira ticketing system with Pentaho Data Catalog, you can use a `config.yaml` file with settings for connection details, credentials, project information, and status mappings. If your system does not have a `config.yaml` file, you can also integrate Jira with Data Catalog using environment variables. For more information, see [Integrate Jira with Data Catalog using environment variables](#integrate-jira-with-data-catalog-using-environment-variables).

Perform the following steps to integrate Jira with Data Catalog using a `config.yaml` file:

1. Go to `/pentaho/pdc-docker-deployment/conf` folder and open `config.yaml` file. If not available, create it.

2. Add the following configuration to the `config.yaml` file.

   **Note:** Replace the placeholder values in angle brackets (< >) with your actual Jira credentials and project details.<br>

   ```
   tools:
     jira:
       url: <your_jira_url>
       username: <your_jira_username>
       password: <your_jira_password>
       project_name: <your_jira_project_name>
       access_status_key: <your_jira_access_status_key>
       status_mapping:
         approved_status: <your_jira_approved_status_value>
         rejected_status: <your_jira_rejected_status_value>
   database:
     postgres:
       host: '<POSTGRES_HOST>'
       port: 5432
       user: '<POSTGRES_USER>'
       password: '<POSTGRES_PASSWORD>'
       dbname: '<ACCESS_REQUEST_DB>'
       sslmode: 'disable'
   ```

3. Additionally, add the following `auth` section as per the PDC version in `config.yaml` file.
   * For **PDC 10.2.5** and **10.2.6**

     ```
     auth:
       url: 'https://<PDC_SERVER_HOST>/keycloak'
       auth_host: '<AUTH_SERVICE_HOST>:5000'
       username: '<ADMIN_USERNAME>'
       password: '<ADMIN_PASSWORD>'
       client_id: 'admin-cli'
     ```
   * For **10.2.7** and **10.2.8**

     ```
     auth:
       pdc_external_url: 'https://<PDC_SERVER_HOST>'
       keycloak_url: 'https://<PDC_SERVER_HOST>/keycloak'
       auth_host: '<AUTH_SERVICE_HOST>:5000'
       username: '<ADMIN_USERNAME>'
       password: '<ADMIN_PASSWORD>'
       client_id: 'admin-cli'
     ```
   * For **PDC 10.2.9**, along with auth section add mds section also.

     ```
     auth:
       pdc_external_url: 'https://<PDC_SERVER_HOST>'
       keycloak_url: 'https://<PDC_SERVER_HOST>/keycloak'
       auth_host: '<AUTH_SERVICE_HOST>:5000'
       username: '<ADMIN_USERNAME>'
       password: '<ADMIN_PASSWORD>'
       client_id: 'admin-cli'

     mds:
       url: 'http://<MDS_SERVICE_HOST>:<MDS_PORT>/api/assets'
     ```

4. Save the changes and close the `config.yaml` file.

5. Open `vendor/docker-compose-um.yml` file. Under the access request service container configuration, add the `Volumes` section parallel to the `environment` section, save the changes, and close the file.

   ```
   volumes:
         - <path-to-the-config.yaml>:/app/config.yaml:ro
   ```

6. Restart the access request service to apply changes:

   `./pdc.sh restart access-request-service`

{% hint style="success" %}
You have successfully configured Jira with Data Catalog using the `config.yaml` file.
{% endhint %}

You now need to add a custom field to Jira, to include the data access request statuses. For more information, see [Add a custom field to Jira](#add-a-custom-field-to-jira).

### Integrate Jira with Data Catalog using environment variables

To integrate the Jira ticketing system with Data Catalog, you can use environment variables to set connection details, credentials, project information, and status mappings. You can also [Integrate Jira with Data Catalog using a config.yaml file](#integrate-jira-with-data-catalog-using-a-config.yaml-file).

Perform the following steps to integrate Jira with Data Catalog using environment variables:

1. Log in to the server where Data Catalog is installed.
2. Go to the Data Catalog Docker deployment configuration directory.

   ```
   cd /opt/pentaho/pdc-docker-deployment/conf
   ```
3. Open the `.env` (environment configuration) file.

   ```
   vi .env
   ```

   If the `.env` file does not exist, create it and save the file before proceeding.
4. Add the following lines:

   **Note:** You can also add environment variables to the default location `/opt/pentaho/pdc-docker-deployment/conf/.env` file.

   ```
   ACCESS_REQUEST_SERVICE_PROVIDER_TOOL=Jira
   ACCESS_REQUEST_SERVICE_JIRA_URL=your_jira_url
   ACCESS_REQUEST_SERVICE_JIRA_USER_NAME=your_jira_username
   ACCESS_REQUEST_SERVICE_JIRA_PASSWORD=your_jira_password
   ACCESS_REQUEST_SERVICE_JIRA_PROJECT_NAME=your_jira_project_name
   ACCESS_REQUEST_SERVICE_JIRA_ACCESS_STATUS_KEY=your_jira_access_status_key
   ACCESS_REQUEST_SERVICE_JIRA_ACCESS_STATUS_APPROVED_VALUE=your_jira_approved_status_value
   ACCESS_REQUEST_SERVICE_JIRA_ACCESS_STATUS_REJECTED_VALUE=your_jira_rejected_status_value
   ACCESS_REQUEST_SERVICE_DEFAULT_ASSIGNEE=PDC_admin_user_email

   ```
5. Save the changes and close the file.
6. Restart the access request service to apply changes:

   ```
   ./pdc.sh restart access-request-service
   ```

{% hint style="success" %}
You have successfully configured Jira with Data Catalog using environment variables.
{% endhint %}

You now need to add a custom field to Jira to include the data access request statuses. For more information, see [Add a custom field to Jira](#add-a-custom-field-to-jira).

### Add a custom field to Jira

If you have configured Data Catalog to connect to Jira for managing data access requests, you need to add a custom field to Jira to map the Data Catalog data access request statuses to complete the Jira integration.

Perform the following steps to add a custom field to Jira:

1. Log in to Jira with administrative rights.
2. Go to the **Jira Admin** settings.

   If you cannot find the **Jira Admin** settings, use these steps:

   1. Open any issue.
   2. In the **Details** section, click the settings icon, then click **Manage Fields**. In the bottom right corner, you see the **Go to Custom Fields** option.
   3. Click **Go to Custom Fields**, and you are taken to the **Jira Admin** settings.
3. Click **Custom Fields** and then click **Create custom field**.
4. Select the **Select List** type and enter `Access Status` as the name.
5. Add the options: `Approved`, `Rejected`, and `Pending`, and click **Create**.
6. Open any issue. In the **Details** section, click the settings icon, then click **Manage Fields**.
7. Locate the newly created **Access Status** field in the list of fields on the right side.
8. Drag and drop the **Access Status** field into the **Context Fields** section.

Jira is now updated to use data access request statuses with Data Catalog.

## Integrating ServiceNow with Data Catalog

You can integrate ServiceNow as an external ticketing system with Data Catalog to manage data access requests. This guide describes how to configure ServiceNow integration using a config.yaml file or environment variables, and how to create a custom field in ServiceNow to track data access request statuses.

{% hint style="info" %}
You can set any administrative user as the default administrator to manage data access requests. However, there can be only one default administrator set, because the `ACCESS_REQUEST_SERVICE_DEFAULT_ASSIGNEE` environment variable only supports a single user. If necessary, the default administrator can edit a data access request to assign it to another administrative user.
{% endhint %}

To integrate ServiceNow with Data Catalog, you need to perform the following tasks:

1. Choose one of the following configuration methods:
   * [Integrate ServiceNow with Data Catalog using a config.yaml file](#integrate-servicenow-with-data-catalog-using-environment-variables)
   * [Integrate ServiceNow with Data Catalog using environment variables](#integrate-servicenow-with-data-catalog-using-a-config.yaml-file)
2. [Add a custom field to ServiceNow](#add-a-custom-field-to-servicenow)

### Integrate ServiceNow with Data Catalog using a config.yaml file

To integrate the ServiceNow ticketing system with Data Catalog, you can use a `config.yaml` file with settings for connection details, credentials, project information, and status mappings. If your system does not have a `config.yaml` file, you can also [Integrate ServiceNow with Data Catalog using environment variables](#integrate-servicenow-with-data-catalog-using-a-config.yaml-file).

To integrate ServiceNow with Data Catalog using a `config.yaml` file, use the following steps:

1. Go to `/pentaho/pdc-docker-deployment/conf` folder and open `config.yaml` file. If not available, create it.

2. Add the following configuration to the `config.yaml` file.

   **Note:** Replace the placeholder values in angle brackets (< >) with your actual ServiceNow credentials and project details.

   ```
   tools:
     servicenow:
       url: <your_servicenow_url>
       username: <your_servicenow_username>
       password: <your_servicenow_password>
       client_id: <your_servicenow_client_id>
       client_secret: <your_servicenow_client_secret>
       access_status_key: <your_servicenow_access_status_key>
       status_mapping:
         approved_status: <your_servicenow_approved_status_value>
         rejected_status: <your_servicenow_rejected_status_value>
   database:
     postgres:
       host: 'um-postgresql'
       port: 5432
       user: 'postgres'
       password: 'admin123#'
       dbname: 'pdc_access_request_db'
       sslmode: 'disable'
   ```

3. Additionally, add the following `auth` section as per the PDC version in `config.yaml` file.
   * For **PDC 10.2.5** and **10.2.6**

     ```
     auth:
       url: 'https://<PDC_SERVER_HOST>/keycloak'
       auth_host: '<AUTH_SERVICE_HOST>:5000'
       username: '<ADMIN_USERNAME>'
       password: '<ADMIN_PASSWORD>'
       client_id: 'admin-cli'
     ```
   * For **10.2.7** and **10.2.8**

     ```
     auth:
       pdc_external_url: 'https://<PDC_SERVER_HOST>'
       keycloak_url: 'https://<PDC_SERVER_HOST>/keycloak'
       auth_host: '<AUTH_SERVICE_HOST>:5000'
       username: '<ADMIN_USERNAME>'
       password: '<ADMIN_PASSWORD>'
       client_id: 'admin-cli'
     ```
   * For **PDC 10.2.9**, along with auth section add mds section also.

     ```
     auth:
       pdc_external_url: 'https://<PDC_SERVER_HOST>'
       keycloak_url: 'https://<PDC_SERVER_HOST>/keycloak'
       auth_host: '<AUTH_SERVICE_HOST>:5000'
       username: '<ADMIN_USERNAME>'
       password: '<ADMIN_PASSWORD>'
       client_id: 'admin-cli'

     mds:
       url: 'http://<MDS_SERVICE_HOST>:<MDS_PORT>/api/assets'
     ```

4. Save the changes and close the `config.yaml` file.

5. Open `vendor/docker-compose-um.yml` file. Under the access request service container configuration, add the `Volumes` section parallel to the `environment` section, save the changes, and close the file.

   ```
   volumes:
         - <path-to-the-config.yaml>:/app/config.yaml:ro
   ```

6. Restart the access request service to apply changes:

   `./pdc.sh restart access-request-service`

{% hint style="success" %}
You have successfully configured ServiceNow with Data Catalog using the `config.yaml` file.
{% endhint %}

You now need to add a custom field to ServiceNow, to include the data access request statuses. For more information, see [Add a custom field to ServiceNow](#add-a-custom-field-to-servicenow).

### Integrate ServiceNow with Data Catalog using environment variables

To integrate the ServiceNow ticketing system with Data Catalog, you can use environment variables to set connection details, credentials, project information, and status mappings. You can also integrate ServiceNow with Data Catalog using a `config.yaml` file.

Perform the following steps to integrate ServiceNow with Data Catalog using environment variables:

1. Edit the `/opt/pentaho/pdc-docker-deployment/vendor/.env.default` file and add the following lines:

   **Note:** Instead of the default location, your environment variables may be set in an `opt/pentaho/pdc-docker-deployment/conf/.env` file.

   ```
   ACCESS_REQUEST_SERVICE_PROVIDER_TOOL= ServiceNow
   ACCESS_REQUEST_SERVICE_SERVICENOW_URL=your_servicenow_url
   ACCESS_REQUEST_SERVICE_SERVICENOW_USER_NAME=your_servicenow_username
   ACCESS_REQUEST_SERVICE_SERVICENOW_PASSWORD=your_servicenow_password
   ACCESS_REQUEST_SERVICE_SERVICENOW_CLIENT_ID=your_servicenow_client_id
   ACCESS_REQUEST_SERVICE_SERVICENOW_CLIENT_SECRET=your_servicenow_client_secret
   ACCESS_REQUEST_SERVICE_SERVICENOW_ACCESS_STATUS_KEY=your_servicenow_access_status_key
   ACCESS_REQUEST_SERVICE_SERVICENOW_ACCESS_STATUS_APPROVED_VALUE=your_servicenow_approved_status_value
   ACCESS_REQUEST_SERVICE_SERVICENOW_ACCESS_STATUS_REJECTED_VALUE=your_servicenow_rejected_status_value
   ACCESS_REQUEST_SERVICE_DEFAULT_ASSIGNEE=PDC_admin_user_email

   ```
2. Save the changes and close the file.
3. Restart the access request service to apply changes:

   ```
   ./pdc.sh restart access-request-service
   ```

{% hint style="success" %}
You have successfully configured ServiceNow with Data Catalog using environment variables.
{% endhint %}

You now need to add a custom field to ServiceNow to include the data access request statuses. For more information, see [Add a custom field to ServiceNow](#add-a-custom-field-to-servicenow).

### Add a custom field to ServiceNow

If you have configured Data Catalog to connect to ServiceNow for managing data access requests, you need to add a custom field to ServiceNow to map the Data Catalog data access request statuses to complete the ServiceNow integration.

Perform the following steps to add a custom field to ServiceNow:

1. Log in to the ServiceNow instance with administrative rights.
2. Go to **System Definition** > **Tables** and locate the **Incident** table.
3. Open the **Incident** table, and at the bottom, in the **Columns** section, click **New** to add a new column (custom field).
4. Configure the following properties:

<table><thead><tr><th width="152.888916015625">Property</th><th>Description</th></tr></thead><tbody><tr><td>Column Label</td><td>Enter a descriptive name like <code>Access Request Status</code>.</td></tr><tr><td>Column Name</td><td>Automatically generated as <code>u_access_request_status</code> (prefixed with u_ to indicate it’s a custom field).</td></tr><tr><td>Type</td><td>Select the appropriate field type, which should be <strong>Choice</strong> for values like <strong>Pending</strong>, <strong>Granted</strong>, and <strong>Denied</strong>.</td></tr><tr><td>Choices</td><td><p>Once the field type is set to <strong>Choice</strong>, there is an option to add <strong>Choice List Values</strong>. Add the following values:- <strong>Pending</strong></p><ul><li><strong>Granted</strong></li><li><strong>Denied</strong><br>You can also set a default value if desired.</li></ul></td></tr></tbody></table>

5\. Verify the changes you have made and click **Submit**.

{% hint style="success" %}
ServiceNow is now updated to use data access request statuses with Data Catalog.
{% endhint %}

## Configure Power BI templates with Pentaho Data Catalog

This guide outlines steps to configure Pentaho Data Catalog by connecting Power BI reports to a PostgreSQL database for catalog metadata. It details the setup for integration, including:

* Pre-created database objects in PostgreSQL
* Configuration of Power BI Desktop and Service
* Scheduled refresh setup

Additionally, it explains synchronizing materialized view refresh jobs in PostgreSQL with Power BI dataset refresh schedules.

### Prerequisites

Before configuring Power BI with Data Catalog, ensure:

* PostgreSQL database is installed, configured, and accessible from the Power BI network.
* A SQL client tool, such as DBeaver Community Edition, is available to run database scripts.
* The user account has the necessary roles and privileges to create tables and materialized views in the PostgreSQL database.
* Power BI Desktop is installed for creating and testing reports.
* Power BI Service access is available for publishing reports and scheduling dataset refreshes.
* The on-premises data gateway is installed and running to enable secure connectivity between Power BI Service and the PostgreSQL database.
* Network permissions allow communication between the Power BI gateway host and the PostgreSQL server.

### Table and view mapping

The following views and tables are pre-created in PDC for the Power BI.

| **View Name**                              | **Dependent Tables**                                                                                                                                     |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mv\_master                                 | entities\_master\_view, datasource\_category\_mapping, currency\_exchange\_rates                                                                         |
| mv\_entity\_category\_summary\_view        | entities\_custom\_categorization, glossary\_summary\_view, terms\_view, entities\_master\_view, currency\_exchange\_rates, datasource\_category\_mapping |
| mv\_duplicate\_savings\_by\_original\_view | duplicate\_files\_view, entities\_master\_view, currency\_exchange\_rates, datasource\_category\_mapping                                                 |
| mv\_duplicate\_by\_term\_summary\_view     | entities\_custom\_categorization, glossary\_summary\_view, duplicate\_files\_view, terms\_view, entities\_master\_view, currency\_exchange\_rates        |
| mv\_duplicate\_entities\_summary\_view     | duplicate\_files\_view, entities\_master\_view, currency\_exchange\_rates                                                                                |
| mv\_duplicate\_entity\_detail\_view        | duplicate\_files\_view, entities\_master\_view, currency\_exchange\_rates                                                                                |
| mv\_policies\_summary                      | policies\_summary\_view, entities\_policies\_view, entities\_master\_view                                                                                |

### Configure the Power BI Desktop environment

Use Power BI Desktop to update the PostgreSQL data source and configure connection settings before publishing the report to Power BI Service.

Perform the following steps to configure Power BI Desktop:

1. Open Power BI Desktop application and open the Power BI report (,pbix).
2. On the ribbon, select **Transform Data** > **Data Source Settings**.
3. In the **Data Source Settings** window, select your PostgreSQL connection.
4. Click **Change Source**, update **Server name/host** and **Database** name, and click **OK**.
5. Click **Edit Permission**, uncheck **Encrypt connection** and enter valid PostgreSQL database credentials.
6. Click **OK** and then click **Close**.
7. On the **Home** tab, select **Apply Changes > Run All** to apply the new configuration.
8. (Optional) To modify parameters directly, select **Home > Edit Parameters**, update values, and then click **Apply Changes**.

Power BI Desktop connects to the PostgreSQL database with the updated host, database, and credential settings. The report is now ready to be published to Power BI Service.

### Configure the Power BI Service gateway

Use the Power BI Service to configure the on-premises data gateway and connect the Power BI dataset to the PostgreSQL database used by Data Catalog. Perform the following procedure to configure Power BI Service gateway:

Before you begin ensure you have an administrator access.

{% stepper %}
{% step %}
**Install and configure on-premises Data Gateway**

1. Download the **On-premises data gateway** installer from the [Microsoft Power BI portal](https://www.microsoft.com/en-us/power-platform/products/power-bi/).
2. Run the installer as an administrator.
3. Select **On-premises data gateway** (recommended) when prompted.
4. Choose **Standard mode**, and then click **Next**.
5. Sign in with your Power BI credentials.
6. Enter a **Gateway name** and **Recovery key** (password), and then click **Configure**.
7. After installation completes, verify that the gateway status shows **Online** in the Power BI Service.
   {% endstep %}

{% step %}
**Configure Dataset in the Power BI Service**

1. In Power BI Service, go to the workspace that contains your dataset.
2. Select the **More options (⋮)** menu next to the dataset, and then select **Settings**.
3. Under **Parameters**, update the **Host name** and **Database name** values.
4. Click **Apply**, and then select **Reload** to refresh the dataset parameters.
   {% endstep %}

{% step %}
Add gateway connection

1. Go to **Manage gateways** from the Power BI Service navigation pane.
2. Select your gateway, and then choose **Add to gateway**.
3. Enter a **Connection name** (preferably the same as the PostgreSQL host name).
4. Select **Basic authentication**.
5. Enter the PostgreSQL username and password.
6. Click **Apply** to create and map the connection to the dataset.
   {% endstep %}
   {% endstepper %}

The Power BI dataset is connected to the PostgreSQL database through the on-premises data gateway. The gateway is active and can be used for scheduled dataset refreshes in Power BI Service.

### Modifying parameters in Power BI Service

Use Power BI Service to update data source parameters for the PostgreSQL connection used by Data Catalog.

Perform the following procedure to change data source details:

1. In **Power BI Service**, go to the workspace that contains your dataset.
2. Select the **More options (⋮)** menu next to the dataset, and then select **Settings**.
3. Under **Parameters**, update the required values such as **Host name** or **Database name**.
4. Click **Apply**, and then select **Reload** to refresh the dataset.
5. If a gateway error occurs, re-create the gateway connection from **Manage gateways**.
6. If the gateway is valid, map the dataset again to ensure the updated parameters are applied.

The Power BI dataset is updated with the new PostgreSQL connection parameters and successfully mapped through the on-premises data gateway.

### Optional - Refresh scheduling and synchronisation

Generally, Cron jobs refresh materialized views in BIDB; however, you can also set a manual refresh schedule for a materialized view in PostgreSQL.

Perform the following steps to schedule a manual refresh:

#### PostgreSQL materialize view refresh scheduling

{% stepper %}
{% step %}
**Create a PostgreSQL refresh function**

Open your SQL client (for example, DBeaver) and run the following script to refresh all required materialized views:

<pre class="language-bash"><code class="lang-bash">CREATE OR REPLACE FUNCTION refresh_all_pentaho_views() RETURNS void AS $$
BEGIN
<strong>    REFRESH MATERIALIZED VIEW CONCURRENTLY public.mv_master;
</strong>    REFRESH MATERIALIZED VIEW CONCURRENTLY public.mv_entity_category_summary_view;
    REFRESH MATERIALIZED VIEW CONCURRENTLY public.mv_duplicate_savings_by_original_view;
    REFRESH MATERIALIZED VIEW CONCURRENTLY public.mv_duplicate_by_term_summary_view;
    REFRESH MATERIALIZED VIEW CONCURRENTLY public.mv_duplicate_entities_summary_view;
    REFRESH MATERIALIZED VIEW CONCURRENTLY public.mv_duplicate_entity_detail_view;
    REFRESH MATERIALIZED VIEW CONCURRENTLY public.mv_policies_summary;
END;
$$ LANGUAGE plpgsql;
</code></pre>

{% endstep %}

{% step %}
**Schedule automatic refresh jobs**

Use **pgAgent** or an operating system scheduler such as **cron** or **Windows Task Scheduler** to automate materialized view refreshes.

* Example cron job for Linux:

  ```bash
  # Refresh Pentaho Data Catalog views every day at 1:00 AM
  0 1 * * * psql -U db_user -d your_database -c "SELECT refresh_all_pentaho_views();"
  ```
* For Windows, use Task Scheduler:
  * Action: Launch psql.exe
  * Arguments: -U db\_user -d your\_database -c "SELECT refresh\_all\_pentaho\_views();"
    {% endstep %}
    {% endstepper %}

#### Power BI Dataset refresh configuration

Perform the following procedure to configure scheduled refresh in Power BI Service:

{% stepper %}
{% step %}
**Power BI Service (Scheduled Refresh)**

1. In **Power BI Service**, open your workspace and select the **Datasets** tab.
2. Select **Schedule refresh** for the dataset connected to PostgreSQL.
3. Turn on **Keep your data up to date**.
4. Configure the refresh schedule:
   1. **Power BI Pro:** up to 8 refreshes per day
   2. **Power BI Premium:** up to 48 refreshes per day
5. Set the time zone, frequency, and preferred refresh times.
6. Align the dataset refresh to run *after* the PostgreSQL refresh completes.
   {% endstep %}

{% step %}
**Gateway mapping validation**

1. Go to **Settings > Manage gateways > Connections**.
2. Verify that the on-premises data gateway status is **Online**.
3. Confirm that the dataset connection is mapped correctly and uses valid credentials.
   {% endstep %}

{% step %}
**Refresh notification and logs**

1. In **Power BI Service**, go to **Settings > Scheduled refresh > Failure notifications**.
2. Enable email alerts for refresh failures to receive proactive notifications.
   {% endstep %}
   {% endstepper %}

Power BI datasets refresh automatically after PostgreSQL materialized views are updated.

### Recommended refresh synchronization strategy

| Component                     | Frequency                | Trigger Time               | Dependency                              |
| ----------------------------- | ------------------------ | -------------------------- | --------------------------------------- |
| PostgreSQL Materialized Views | Every 24 hours (1:00 AM) | Cron job/pgAgent           | N/A                                     |
| Power BI Dataset              | Every 24 hours (2:00 AM) | Power BI scheduled refresh | Runs after PostgreSQL refresh completes |

This ensures that Power BI always retrieves updated, fully processed data from Data Catalog’s database views.
