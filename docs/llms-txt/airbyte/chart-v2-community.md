# Source: https://docs.airbyte.com/platform/deploying-airbyte/chart-v2-community.md

# Source: https://docs.airbyte.com/platform/2.0/deploying-airbyte/chart-v2-community.md

# Source: https://docs.airbyte.com/platform/1.8/deploying-airbyte/chart-v2-community.md

# Upgrade to Helm chart V2 (Self-Managed Community)

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Airbyte has upgraded its Helm chart to a new version called "V2." Using Helm chart V2 is currently optional. At some future date the V2 Helm chart will become the standard, so we advise that you upgrade your existing deployment to use the new chart before the transition. If you're a new Airbyte user, you can skip the upgrade altogether and start with the new chart.

Enterprise customers

Follow the [Self-Managed Enterprise guide](/platform/1.8/enterprise-setup/chart-v2-enterprise.md) instead.

## Why you should upgrade[​](#why-you-should-upgrade "Direct link to Why you should upgrade")

Upgrading to the new Helm chart now has the following benefits.

1. By upgrading in advance, you can schedule this upgrade for a convenient time. Avoid blocking yourself from upgrading Airbyte to a future version when the new chart is mandatory and you're busy.

2. The new Helm chart is more aligned with Helm's best practices for chart design.

3. The new Helm chart has broader and more detailed options to customize your deployment. In most cases, it's no longer necessary to specify environment variables in your `values.yaml` file because the chart offers a more detailed interface for customization. If you do need to use environment variables, you can use fewer of them.

## Which versions can upgrade to Helm chart V2[​](#which-versions-can-upgrade-to-helm-chart-v2 "Direct link to Which versions can upgrade to Helm chart V2")

The following versions of Airbyte can use Helm chart V2:

* Airbyte version 1.6.0 and later, if installed and managed with Helm

The following versions of Airbyte *can't* use Helm chart V2:

* Airbyte versions before 1.6.0

* Airbyte versions installed and managed with abctl

## How to upgrade[​](#how-to-upgrade "Direct link to How to upgrade")

In most cases, upgrading is straightforward. To upgrade to Helm chart V2, you complete the following steps.

1. Ensure you have configured Airbyte to use an external database and external bucket storage. If you haven't, backup Airbyte's internal Postgres database.

2. Prepare to deploy a fresh installation of Airbyte in a new namespace, but only if you're using an external database. If you're using Airbyte's internal Postgres database, you'll reuse your existing namespace.

3. Create a new `values.yaml` file.

4. Deploy a new version of Airbyte using your new `values.yaml` file and the new Helm chart version.

### Backup Airbyte's internal Postgres database[​](#backup-airbytes-internal-postgres-database "Direct link to Backup Airbyte's internal Postgres database")

* External database
* No external database

If you have configured an external database, skip this step. However, it is a good idea to backup your database on a regular cadence.

If you haven't configured an external database, you must backup Airbyte's internal Postgres database. If you fail to do this, and something goes wrong during your upgrade, you could lose all your connections and states.

1. Get your database pod name. It's probably `airbyte-db-0`, but you can check for it with the following command.

   ```
   kubectl get pods --all-namespaces | grep db
   ```

2. Get the name of your database. It's probably `db-airbyte`, but you can check for it with the following command.

   ```
   kubectl exec -n airbyte -it airbyte-db-0 -- psql -U airbyte postgres
   ```

3. Get your database credentials. They're probably in `airbyte-airbyte-secrets`, but you can check for them with the following command.

   ```
   kubectl get secrets -n <namespace>
   ```

   Now print them to the terminal.

   ```
   kubectl get secret airbyte-airbyte-secrets -n airbyte -o jsonpath='{.data}'
   ```

   You should see a result that's similar to this.

   ```
   {"DATABASE_PASSWORD":"<username>","DATABASE_USER":"<password>","MINIO_ACCESS_KEY_ID":"<key>","MINIO_SECRET_ACCESS_KEY":"<key>","WORKLOAD_API_BEARER_TOKEN":"<key>"}%   
   ```

   Note your `DATABASE_PASSWORD` and `DATABASE_USER`.

4. Run `pg_dump` inside the Postgres pod and copy the dump locally.

   ```
   kubectl exec -n <namespace> -it <database_pod> -- bash -c "pg_dump -U airbyte db-airbyte > /tmp/airbyte_backup.sql"
   ```

   Copy your backup out of the pod and to the destination of your choice. In this example, you copy it to your local machine.

   ```
   kubectl cp airbyte/airbyte-db-0:/tmp/airbyte_backup.sql ./airbyte_backup.sql
   ```

It's important you safeguard this SQL database. Although problems after upgrades are rare, if they do happen, your backup is critical to restoring Airbyte.

### Prepare a new namespace for Airbyte[​](#prepare-a-new-namespace-for-airbyte "Direct link to Prepare a new namespace for Airbyte")

* External database
* No external database

When moving to Helm chart V2, deploy Airbyte with a new namespace and use a fresh values and secrets file. It is possible to do a straight upgrade, but different Airbyte users have different and sometimes complex configurations that could produce unique and unexpected situations during the upgrade. By doing a fresh install, you create a separate environment that's easier to troubleshoot if something in your values or secrets files acts unexpectedly.

```
kubectl create namespace airbyte-v2
```

If you're not using an external database, skip this step. At deployment time, you will reinstall Airbyte in your existing namespace.

### Add V2 chart repo[​](#add-v2-chart-repo "Direct link to Add V2 chart repo")

Helm chart V2 uses a different repo URL than V1 did. In your command line tool, add this repo and index it.

```
# Helm chart V1
# helm repo add airbyte https://airbytehq.github.io/helm-charts

# Helm chart V2
helm repo add airbyte-v2 https://airbytehq.github.io/charts
helm repo update
```

You can browse all charts uploaded to your repository.

```
helm search repo airbyte-v2
```

### Update your values.yaml file[​](#update-your-valuesyaml-file "Direct link to Update your values.yaml file")

In most cases, the adjustments to `values.yaml` are small and involve changing keys and moving sections. This section walks you through the main updates you need to make. If you already know what to do, see [Values.yaml reference](/platform/1.8/deploying-airbyte/values.md) for the full V1 and V2 interfaces.

Airbyte recommends approaching this project in this way:

1. Note the customizations in your V1 `values.yaml` file to ensure you don't forget anything.

2. Start with a basic V2 `values.yaml` to verify that it works. Map your V1 settings to V2, transferring one set of configurations at a time.

3. Don't test in production.

Follow the steps below to start generating `values.yaml`.

Create a `values.yaml` file and a `global` configuration

Create a new `values.yaml` file on your machine. In that file, create your basic global configuration.

values.yaml

```
global:
  edition: community

  airbyteUrl: "" # The URL where Airbyte will be reached; This should match your Ingress host
```

Add your database (if applicable)

If you're not using an external database, skip this step.

If you are using an external database, disable Airbyte's default Postgres database and add your own. The main difference in Helm chart V2 is the `global.database.database` key has changed to `global.database.name`.

values.yaml

```
global: 
  database:
    # -- Secret name where database credentials are stored
    secretName: "" # e.g. "airbyte-config-secrets"
    # -- The database host
    host: ""
    # -- The database port
    port:
    # -- The database name - this key used to be "database" in Helm chart 1.0
    name: ""

    # Use EITHER user or userSecretKey, but not both
    # -- The database user
    user: ""
    # -- The key within `secretName` where the user is stored
    userSecretKey: "" # e.g. "database-user"

    # Use EITHER password or passwordSecretKey, but not both
    # -- The database password
    password: ""
    # -- The key within `secretName` where the password is stored
    passwordSecretKey: "" # e.g."database-password"

postgresql:
  enabled: false
```

Add external log storage (if applicable)

If you're using external log storage, implement it. If you aren't, skip this step.

```
global:
  storage:
    secretName: ""
    type: minio # default storage is minio. Set to s3, gcs, or azure, according to what you use.

    bucket:
      log: airbyte-bucket
      state: airbyte-bucket
      workloadOutput: airbyte-bucket
      activityPayload: airbyte-bucket

    # Set ONE OF the following storage types, according to your specification above

    # S3
    s3:
      region: "" ## e.g. us-east-1
      authenticationType: credentials ## Use "credentials" or "instanceProfile"
      accessKeyId: ""
      secretAccessKey: ""

    # GCS
    gcs:
      projectId: <project-id>
      credentialsJson:  <base64-encoded>
      credentialsJsonPath: /secrets/gcs-log-creds/gcp.json

    # Azure
    azure:
      # one of the following: connectionString, connectionStringSecretKey
      connectionString: <azure storage connection string>
      connectionStringSecretKey: <secret coordinate containing an existing connection-string secret>
```

Add external connector secret management (if applicable)

If you're using external secret management, implement it. If you aren't, skip this step.

```
global:
  secretsManager:
    enabled: false
    type: "" # one of: VAULT, GOOGLE_SECRET_MANAGER, AWS_SECRET_MANAGER, AZURE_KEY_VAULT, TESTING_CONFIG_DB_TABLE
    secretName: "airbyte-config-secrets"

    # Set ONE OF the following groups of configurations, based on your configuration in global.secretsManager.type.

    awsSecretManager:
      region: <aws-region>
      authenticationType: credentials ## Use "credentials" or "instanceProfile"
      tags: ## Optional - You may add tags to new secrets created by Airbyte.
      - key: ## e.g. team
          value: ## e.g. deployments
        - key: business-unit
          value: engineering
      kms: ## Optional - ARN for KMS Decryption.

    # OR

    googleSecretManager:
      projectId: <project-id>
      credentialsSecretKey: gcp.json

    # OR

    azureKeyVault:
      tenantId: ""
      vaultUrl: ""
      clientId: ""
      clientIdSecretKey: ""
      clientSecret: ""
      clientSecretSecretKey: ""
      tags: ""

    # OR

    vault:
      address: ""
      prefix: ""
      authToken: ""
      authTokenSecretKey: ""
```

Update syntax for other customizatons

If you have further customizations in your V1 values.yaml file, move those over to your new values.yaml file, and update key names where appropriate.

* Change hyphenated V1 keys keys to camel case in V2. For example, when copying over `workload-launcher`, change it to `workloadLauncher`.

* Some keys have different names. For example, `orchestrator` is `containerOrchestrator` in V2.

Here is the full list of changes.

| Helm chart V1                                                        | Helm chart V2                                                                      |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Not available (manual ingress only)                                  | `ingress` - See [Ingress](/platform/1.8/deploying-airbyte/integrations/ingress.md) |
| `global.database.database`                                           | `global.database.name`                                                             |
| `workload-launcher`                                                  | `workloadLauncher`                                                                 |
| `airbyte-bootloader`                                                 | `airbyteBootloader`                                                                |
| `orchestrator`                                                       | `containerOrchestrator`                                                            |
| `workload-launcher.extraEnvs[JOB_KUBE_NODE_SELECTORS]`               | `global.jobs.kube.nodeSelector`                                                    |
| `workload-launcher.extraEnvs[CHECK_JOB_KUBE_NODE_SELECTORS]`         | `global.jobs.kube.scheduling.check.nodeSelectors`                                  |
| `workload-launcher.extraEnvs[DISCOVER_JOB_KUBE_NODE_SELECTORS]`      | `global.jobs.kube.scheduling.discover.nodeSelectors`                               |
| `worker.extraEnvs[MAX_SYNC_WORKERS]`                                 | `worker.maxSyncWorkers`                                                            |
| `worker.extraEnvs[MAX_CHECK_WORKERS]`                                | `worker.maxCheckWorkers`                                                           |
| `server.extraEnvs[HTTP_IDLE_TIMEOUT]`                                | `server.httpIdleTimeout`                                                           |
| `global.env_vars[TRACKING_STRATEGY]`                                 | `global.tracking.strategy`                                                         |
| `server.env_vars[AUDIT_LOGGING_ENABLED]`                             | `server.auditLoggingEnabled`                                                       |
| `global.env_vars[STORAGE_BUCKET_AUDIT_LOGGING]`                      | `global.storage.bucket.auditLogging`                                               |
| `global.env_vars[JOB_MAIN_CONTAINER_CPU_REQUEST]`                    | `global.workloads.resources.mainContainer.cpu.request`                             |
| `orchestrator.nodeSelector`                                          | `global.jobs.kube.nodeSelector`                                                    |
| Individual bucket env vars (`S3_LOG_BUCKET`, `GCS_LOG_BUCKET`, etc.) | `global.storage.bucket.log`                                                        |
| `STORAGE_BUCKET_STATE`                                               | `global.storage.bucket.state`                                                      |
| `STORAGE_BUCKET_WORKLOAD_OUTPUT`                                     | `global.storage.bucket.workloadOutput`                                             |
| `STORAGE_BUCKET_ACTIVITY_PAYLOAD`                                    | `global.storage.bucket.activityPayload`                                            |

Convert `extraEnv` variables

In previous versions of your values.yaml file, you might have specified a number of environment variables through `extraEnv`. Many (but not all) of these variables have a dedicated interface in Helm chart V2. For example, look at the following configuration, which tells `workload-launcher` to run pods in the `jobs` node group.

values.yaml using Helm chart V1

```
workload-launcher:
  nodeSelector:
    type: static
  ## Pods spun up by the workload launcher will run in the 'jobs' node group.
  extraEnv:
    - name: JOB_KUBE_NODE_SELECTORS
      value: type=jobs
    - name: SPEC_JOB_KUBE_NODE_SELECTORS
      value: type=jobs
    - name: CHECK_JOB_KUBE_NODE_SELECTORS
      value: type=jobs
    - name: DISCOVER_JOB_KUBE_NODE_SELECTORS
      value: type=jobs
```

You can specify these values directly without using environment variables, achieving the same effect.

values.yaml using Helm chart V2

```
global:
  jobs:
    kube:
      nodeSelector:
        type: jobs
      scheduling:
        check:
          nodeSelectors:
            type: jobs
        discover:
          nodeSelectors:
            type: jobs
        spec:
          nodeSelectors:
            type: jobs

workloadLauncher:
  nodeSelector:
    type: static
```

Here is a complete list of environment variables with their Helm chart V2 equivalent. Some environment variables don't have direct V2 equivalents, so you can set these using the `extraEnv` configuration in the appropriate service section.

| Environment variable                                              | Helm chart V2 equivalent                                               |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Core**                                                          |                                                                        |
| AIRBYTE\_VERSION                                                  | global.version                                                         |
| AIRBYTE\_EDITION                                                  | global.edition                                                         |
| AIRBYTE\_CLUSTER\_TYPE                                            | global.cluster.type                                                    |
| AIRBYTE\_CLUSTER\_NAME                                            | global.cluster.name                                                    |
| AIRBYTE\_URL                                                      | global.airbyteUrl                                                      |
| AIRBYTE\_API\_HOST                                                | global.api.host                                                        |
| AIRBYTE\_API\_AUTH\_HEADER\_NAME                                  | global.api.authHeaderName                                              |
| AIRBYTE\_API\_AUTH\_HEADER\_VALUE                                 | global.api.authHeaderValue                                             |
| AIRBYTE\_SERVER\_HOST                                             | global.server.host                                                     |
| API\_AUTHORIZATION\_ENABLED                                       | global.auth.enabled                                                    |
| CONNECTOR\_BUILDER\_SERVER\_API\_HOST                             | global.connectorBuilderServer.apiHost                                  |
| DEPLOYMENT\_ENV                                                   | global.deploymentEnv                                                   |
| INTERNAL\_API\_HOST                                               | global.api.internalHost                                                |
| LOCAL                                                             | global.local                                                           |
| WEBAPP\_URL                                                       | global.webapp.url                                                      |
| SPEC\_CACHE\_BUCKET                                               | Use extraEnvs                                                          |
| **Secrets**                                                       |                                                                        |
| SECRET\_PERSISTENCE                                               | global.secretsManager.type                                             |
| SECRET\_STORE\_GCP\_PROJECT\_ID                                   | global.secretsManager.googleSecretManager.projectId                    |
| SECRET\_STORE\_GCP\_CREDENTIALS                                   | global.secretsManager.googleSecretManager.credentials                  |
| VAULT\_ADDRESS                                                    | global.secretsManager.vault.address                                    |
| VAULT\_PREFIX                                                     | global.secretsManager.vault.prefix                                     |
| VAULT\_AUTH\_TOKEN                                                | global.secretsManager.vault.token                                      |
| VAULT\_AUTH\_METHOD                                               | global.secretsManager.vault.authMethod                                 |
| AWS\_ACCESS\_KEY                                                  | global.aws.accessKeyId                                                 |
| AWS\_SECRET\_ACCESS\_KEY                                          | global.aws.secretAccessKey                                             |
| AWS\_KMS\_KEY\_ARN                                                | global.secretsManager.awsSecretManager.kmsKeyArn                       |
| AWS\_SECRET\_MANAGER\_SECRET\_TAGS                                | global.secretsManager.awsSecretManager.tags                            |
| AWS\_ASSUME\_ROLE\_ACCESS\_KEY\_ID                                | global.aws.assumeRole.accessKeyId                                      |
| **Database**                                                      |                                                                        |
| DATABASE\_USER                                                    | global.database.user                                                   |
| DATABASE\_PASSWORD                                                | global.database.password                                               |
| DATABASE\_URL                                                     | global.database.url                                                    |
| DATABASE\_HOST                                                    | global.database.host                                                   |
| DATABASE\_PORT                                                    | global.database.port                                                   |
| DATABASE\_DB                                                      | global.database.database                                               |
| JOBS\_DATABASE\_INITIALIZATION\_TIMEOUT\_MS                       | global.database.initializationTimeoutMs                                |
| CONFIG\_DATABASE\_USER                                            | global.database.user                                                   |
| CONFIG\_DATABASE\_PASSWORD                                        | global.database.password                                               |
| CONFIG\_DATABASE\_URL                                             | global.database.url                                                    |
| CONFIG\_DATABASE\_INITIALIZATION\_TIMEOUT\_MS                     | global.database.initializationTimeoutMs                                |
| RUN\_DATABASE\_MIGRATION\_ON\_STARTUP                             | global.migrations.runAtStartup                                         |
| USE\_CLOUD\_SQL\_PROXY                                            | global.cloudSqlProxy.enabled                                           |
| **Airbyte Services**                                              |                                                                        |
| TEMPORAL\_HOST                                                    | temporal.host                                                          |
| **Jobs**                                                          |                                                                        |
| SYNC\_JOB\_MAX\_ATTEMPTS                                          | Use extraEnvs                                                          |
| SYNC\_JOB\_RETRIES\_COMPLETE\_FAILURES\_MAX\_SUCCESSIVE           | Use extraEnvs                                                          |
| SYNC\_JOB\_RETRIES\_COMPLETE\_FAILURES\_MAX\_TOTAL                | Use extraEnvs                                                          |
| SYNC\_JOB\_RETRIES\_COMPLETE\_FAILURES\_BACKOFF\_MIN\_INTERVAL\_S | Use extraEnvs                                                          |
| SYNC\_JOB\_RETRIES\_COMPLETE\_FAILURES\_BACKOFF\_MAX\_INTERVAL\_S | Use extraEnvs                                                          |
| SYNC\_JOB\_RETRIES\_COMPLETE\_FAILURES\_BACKOFF\_BASE             | Use extraEnvs                                                          |
| SYNC\_JOB\_RETRIES\_PARTIAL\_FAILURES\_MAX\_SUCCESSIVE            | Use extraEnvs                                                          |
| SYNC\_JOB\_RETRIES\_PARTIAL\_FAILURES\_MAX\_TOTAL                 | Use extraEnvs                                                          |
| SYNC\_JOB\_MAX\_TIMEOUT\_DAYS                                     | Use extraEnvs                                                          |
| JOB\_MAIN\_CONTAINER\_CPU\_REQUEST                                | global.workloads.resources.mainContainer.cpu.request                   |
| JOB\_MAIN\_CONTAINER\_CPU\_LIMIT                                  | global.workloads.resources.mainContainer.cpu.limit                     |
| JOB\_MAIN\_CONTAINER\_MEMORY\_REQUEST                             | global.workloads.resources.mainContainer.memory.request                |
| JOB\_MAIN\_CONTAINER\_MEMORY\_LIMIT                               | global.workloads.resources.mainContainer.memory.limit                  |
| JOB\_KUBE\_TOLERATIONS                                            | global.jobs.kube.tolerations                                           |
| JOB\_KUBE\_NODE\_SELECTORS                                        | global.jobs.kube.nodeSelector                                          |
| JOB\_KUBE\_ANNOTATIONS                                            | global.jobs.kube.annotations                                           |
| JOB\_KUBE\_MAIN\_CONTAINER\_IMAGE\_PULL\_POLICY                   | global.jobs.kube.mainContainerImagePullPolicy                          |
| JOB\_KUBE\_MAIN\_CONTAINER\_IMAGE\_PULL\_SECRET                   | global.jobs.kube.mainContainerImagePullSecret                          |
| JOB\_KUBE\_SIDECAR\_CONTAINER\_IMAGE\_PULL\_POLICY                | global.jobs.kube.sidecarContainerImagePullPolicy                       |
| JOB\_KUBE\_SOCAT\_IMAGE                                           | global.jobs.kube.images.socat                                          |
| JOB\_KUBE\_BUSYBOX\_IMAGE                                         | global.jobs.kube.images.busybox                                        |
| JOB\_KUBE\_CURL\_IMAGE                                            | global.jobs.kube.images.curl                                           |
| JOB\_KUBE\_NAMESPACE                                              | global.jobs.kube.namespace                                             |
| JOB\_KUBE\_SERVICEACCOUNT                                         | global.jobs.kube.serviceAccount                                        |
| **Jobs-specific**                                                 |                                                                        |
| SPEC\_JOB\_KUBE\_NODE\_SELECTORS                                  | global.jobs.kube.scheduling.spec.nodeSelectors                         |
| CHECK\_JOB\_KUBE\_NODE\_SELECTORS                                 | global.jobs.kube.scheduling.check.nodeSelectors                        |
| DISCOVER\_JOB\_KUBE\_NODE\_SELECTORS                              | global.jobs.kube.scheduling.discover.nodeSelectors                     |
| SPEC\_JOB\_KUBE\_ANNOTATIONS                                      | global.jobs.kube.scheduling.spec.annotations                           |
| CHECK\_JOB\_KUBE\_ANNOTATIONS                                     | global.jobs.kube.scheduling.check.annotations                          |
| DISCOVER\_JOB\_KUBE\_ANNOTATIONS                                  | global.jobs.kube.scheduling.discover.annotations                       |
| **Connections**                                                   |                                                                        |
| MAX\_FIELDS\_PER\_CONNECTION                                      | Use extraEnvs                                                          |
| MAX\_DAYS\_OF\_ONLY\_FAILED\_JOBS\_BEFORE\_CONNECTION\_DISABLE    | Use extraEnvs                                                          |
| MAX\_FAILED\_JOBS\_IN\_A\_ROW\_BEFORE\_CONNECTION\_DISABLE        | Use extraEnvs                                                          |
| **Logging**                                                       |                                                                        |
| LOG\_LEVEL                                                        | global.logging.level                                                   |
| GCS\_LOG\_BUCKET                                                  | global.storage.gcs.bucket                                              |
| S3\_BUCKET                                                        | global.storage.s3.bucket                                               |
| S3\_REGION                                                        | global.storage.s3.region                                               |
| S3\_AWS\_KEY                                                      | global.storage.s3.accessKeyId                                          |
| S3\_AWS\_SECRET                                                   | global.storage.s3.secretAccessKey                                      |
| S3\_MINIO\_ENDPOINT                                               | global.storage.minio.endpoint                                          |
| S3\_PATH\_STYLE\_ACCESS                                           | global.storage.s3.pathStyleAccess                                      |
| **Monitoring**                                                    |                                                                        |
| PUBLISH\_METRICS                                                  | global.metrics.enabled                                                 |
| METRIC\_CLIENT                                                    | global.metrics.client                                                  |
| DD\_AGENT\_HOST                                                   | global.datadog.agentHost                                               |
| DD\_AGENT\_PORT                                                   | global.datadog.agentPort                                               |
| OTEL\_COLLECTOR\_ENDPOINT                                         | global.metrics.otel.exporter.endpoint                                  |
| MICROMETER\_METRICS\_ENABLED                                      | global.metrics.enabled                                                 |
| **Worker**                                                        |                                                                        |
| MAX\_CHECK\_WORKERS                                               | worker.maxCheckWorkers                                                 |
| MAX\_SYNC\_WORKERS                                                | worker.maxSyncWorkers                                                  |
| TEMPORAL\_WORKER\_PORTS                                           | worker.temporalWorkerPorts                                             |
| DISCOVER\_REFRESH\_WINDOW\_MINUTES                                | Use extraEnvs                                                          |
| **Launcher**                                                      |                                                                        |
| WORKLOAD\_LAUNCHER\_PARALLELISM                                   | workloadLauncher.parallelism                                           |
| **Data Retention**                                                |                                                                        |
| TEMPORAL\_HISTORY\_RETENTION\_IN\_DAYS                            | Use extraEnvs                                                          |
| **Server**                                                        |                                                                        |
| AUDIT\_LOGGING\_ENABLED                                           | server.auditLoggingEnabled                                             |
| STORAGE\_BUCKET\_AUDIT\_LOGGING                                   | server.auditLoggingBucket                                              |
| HTTP\_IDLE\_TIMEOUT                                               | server.httpIdleTimeout                                                 |
| READ\_TIMEOUT                                                     | Use extraEnvs                                                          |
| **Authentication**                                                |                                                                        |
| AB\_INSTANCE\_ADMIN\_PASSWORD                                     | global.auth.instanceAdmin.password                                     |
| AB\_AUTH\_SECRET\_CREATION\_ENABLED                               | global.auth.secretCreationEnabled                                      |
| AB\_KUBERNETES\_SECRET\_NAME                                      | global.auth.managedSecretName                                          |
| AB\_INSTANCE\_ADMIN\_CLIENT\_ID                                   | global.auth.instanceAdmin.clientId                                     |
| AB\_INSTANCE\_ADMIN\_CLIENT\_SECRET                               | global.auth.instanceAdmin.clientSecret                                 |
| AB\_JWT\_SIGNATURE\_SECRET                                        | global.auth.security.jwtSignatureSecret                                |
| AB\_COOKIE\_SECURE                                                | global.auth.security.cookieSecureSetting                               |
| INITIAL\_USER\_FIRST\_NAME                                        | global.auth.instanceAdmin.firstName                                    |
| INITIAL\_USER\_LAST\_NAME                                         | global.auth.instanceAdmin.lastName                                     |
| INITIAL\_USER\_EMAIL                                              | global.auth.instanceAdmin.email                                        |
| INITIAL\_USER\_PASSWORD                                           | global.auth.instanceAdmin.password                                     |
| **Tracking**                                                      |                                                                        |
| TRACKING\_ENABLED                                                 | global.tracking.enabled                                                |
| TRACKING\_STRATEGY                                                | global.tracking.strategy                                               |
| **Enterprise**                                                    |                                                                        |
| AIRBYTE\_LICENSE\_KEY                                             | global.enterprise.licenseKey                                           |
| **Feature Flags**                                                 |                                                                        |
| FEATURE\_FLAG\_CLIENT                                             | global.featureFlags.client                                             |
| LAUNCHDARKLY\_KEY                                                 | global.featureFlags.launchDarkly.sdkKey                                |
| **Java**                                                          |                                                                        |
| JAVA\_TOOL\_OPTIONS                                               | global.java.opts                                                       |
| **Temporal**                                                      |                                                                        |
| AUTO\_SETUP                                                       | temporal.autoSetup                                                     |
| TEMPORAL\_CLI\_ADDRESS                                            | global.temporal.cli.address                                            |
| TEMPORAL\_CLOUD\_ENABLED                                          | global.temporal.cloud.enabled                                          |
| TEMPORAL\_CLOUD\_HOST                                             | global.temporal.cloud.host                                             |
| TEMPORAL\_CLOUD\_NAMESPACE                                        | global.temporal.cloud.namespace                                        |
| TEMPORAL\_CLOUD\_CLIENT\_CERT                                     | global.temporal.cloud.clientCert                                       |
| TEMPORAL\_CLOUD\_CLIENT\_KEY                                      | global.temporal.cloud.clientKey                                        |
| **Container Orchestrator**                                        |                                                                        |
| CONTAINER\_ORCHESTRATOR\_SECRET\_NAME                             | global.workloads.containerOrchestrator.secretName                      |
| CONTAINER\_ORCHESTRATOR\_SECRET\_MOUNT\_PATH                      | global.workloads.containerOrchestrator.secretMountPath                 |
| CONTAINER\_ORCHESTRATOR\_DATA\_PLANE\_CREDS\_SECRET\_NAME         | global.workloads.containerOrchestrator.dataPlane.credentialsSecretName |
| CONTAINER\_ORCHESTRATOR\_IMAGE                                    | global.workloads.containerOrchestrator.image                           |
| **Workload Launcher**                                             |                                                                        |
| WORKLOAD\_LAUNCHER\_PARALLELISM                                   | workloadLauncher.parallelism                                           |
| CONNECTOR\_PROFILER\_IMAGE                                        | workloadLauncher.connectorProfiler.image                               |
| WORKLOAD\_INIT\_IMAGE                                             | workloadLauncher.workloadInit.image                                    |
| **Connector Registry**                                            |                                                                        |
| CONNECTOR\_REGISTRY\_SEED\_PROVIDER                               | global.connectorRegistry.seedProvider                                  |
| CONNECTOR\_REGISTRY\_BASE\_URL                                    | global.connectorRegistry.baseUrl                                       |
| **AI Assist**                                                     |                                                                        |
| AI\_ASSIST\_URL\_BASE                                             | connectorBuilderServer.aiAssistUrlBase                                 |
| AI\_ASSIST\_API\_KEY                                              | connectorBuilderServer.aiAssistApiKey                                  |
| **Connector Rollout**                                             |                                                                        |
| CONNECTOR\_ROLLOUT\_EXPIRATION\_SECONDS                           | global.connectorRollout.expirationSeconds                              |
| CONNECTOR\_ROLLOUT\_PARALLELISM                                   | global.connectorRollout.parallelism                                    |
| CONNECTOR\_ROLLOUT\_GITHUB\_AIRBYTE\_PAT                          | connectorRolloutWorker.githubToken                                     |
| **Customer.io**                                                   |                                                                        |
| CUSTOMERIO\_API\_KEY                                              | global.customerio.apiKey                                               |
| **Shopify**                                                       |                                                                        |
| SHOPIFY\_CLIENT\_ID                                               | global.shopify.clientId                                                |
| SHOPIFY\_CLIENT\_SECRET                                           | global.shopify.clientSecret                                            |
| **Keycloak**                                                      |                                                                        |
| KEYCLOAK\_ADMIN\_USER                                             | keycloak.auth.adminUsername                                            |
| KEYCLOAK\_ADMIN\_PASSWORD                                         | keycloak.auth.adminPassword                                            |
| KEYCLOAK\_ADMIN\_REALM                                            | keycloak.auth.adminRealm                                               |
| KEYCLOAK\_INTERNAL\_REALM\_ISSUER                                 | keycloak.realmIssuer                                                   |
| **MinIO**                                                         |                                                                        |
| MINIO\_ROOT\_USER                                                 | minio.rootUser                                                         |
| MINIO\_ROOT\_PASSWORD                                             | minio.rootPassword                                                     |
| **Micronaut**                                                     |                                                                        |
| MICRONAUT\_ENVIRONMENTS                                           | global.micronaut.environments                                          |
| **Topology**                                                      |                                                                        |
| NODE\_SELECTOR\_LABEL                                             | global.topology.nodeSelectorLabel                                      |
| QUICK\_JOBS\_NODE\_SELECTOR\_LABEL                                | global.topology.quickJobsNodeSelectorLabel                             |
| **Workloads**                                                     |                                                                        |
| CONNECTOR\_SPECIFIC\_RESOURCE\_DEFAULTS\_ENABLED                  | global.workloads.resources.useConnectorResourceDefaults                |
| DATA\_CHECK\_TASK\_QUEUES                                         | global.workloads.queues.check                                          |

### Deploy Airbyte[​](#deploy-airbyte "Direct link to Deploy Airbyte")

* External database
* No external database

Deploy Airbyte. Here is an example of how to deploy version 1.7.0 of Airbyte using the latest Helm chart V2 values. Normally the Helm chart version is identical to the Airbyte version. Since using this chart version is optional, the Helm chart and Airbyte have different, but compatible, versions.

```
helm install airbyte airbyte-v2/airbyte \
  --namespace airbyte-v2 \       # Target Kubernetes namespace
  --values ./values.yaml \       # Custom configuration values
  --version 2.0.3 \              # Helm chart version to use
  --set global.image.tag=1.7.0   # Airbyte version to use
```

danger

Do not proceed if you have not backed up Airbyte's internal Postgres database.

1. Uninstall Airbyte. **Do not delete the Airbyte namespace**. This example assumes you installed Airbyte in the `airbyte` namespace.

   ```
   helm uninstall airbyte -n airbyte
   ```

2. Reinstall Airbyte into the same namespace as before. Here is an example of how to deploy version 1.7.0 of Airbyte using the latest Helm chart V2 values. Normally the Helm chart version is identical to the Airbyte version. Since using this chart version is optional, the Helm chart and Airbyte have different, but compatible, versions.

   ```
   helm install airbyte airbyte-v2/airbyte \
   --namespace airbyte \          # Target Kubernetes namespace
   --values ./values.yaml \       # Custom configuration values
   --version 2.0.3 \              # Helm chart version to use
   --set global.image.tag=1.7.0   # Airbyte version to use
   ```

Airbyte continues in this namespace as before, now running on Helm Chart V2.

#### Restore your database[​](#restore-your-database "Direct link to Restore your database")

You do not need to restore your database except in exceptional circumstances. Only restore your database if there is an issue with your deployment that isn't related to your configurations. The restoration process is essentially the reverse of the backup process you went through above.

These examples assume your namespace is still `airbyte` and your database pod name is still `airbyte-db-0`.

1. Copy the SQL backup file into your pod's /tmp directory.

   ```
   kubectl cp ./airbyte_backup.sql airbyte/airbyte-db-0:/tmp/airbyte_backup.sql
   ```

2. Since your original database probably already contains data, drop and recreate the schema. This erases all data in the database.

   ```
   kubectl exec -n airbyte -it airbyte-db-0 -- bash -c "psql -U airbyte -d db-airbyte -c 'DROP SCHEMA public CASCADE; CREATE SCHEMA public;'"
   ```

3. Restore the database.

   ```
   kubectl exec -n airbyte -it airbyte-db-0 -- bash -c "psql -U airbyte -d db-airbyte < /tmp/airbyte_backup.sql"
   ```
