# Source: https://docs.pentaho.com/pdc-admin/pdc-troubleshooting-cp-ag.md

# Troubleshooting Pentaho Data Catalog

The Pentaho Data Catalog log files contain information that can help you determine the root cause of error messages you might see. Refer to the following topics for information on how to resolve the issues causing the error messages.

***

## Low disk space message

If you see a `Low disk space` message from Pentaho Data Catalog while loading images into the Docker repository, you can resolve this issue by linking the Docker root directory to another directory.

**Important:** The other directory should have at least 100 GB of free space.

Use the following steps to resolve this issue:

1. Enter the following commands to link the `/var/lib/docker` directory to a directory with at least 100 GB of free space.

   **Note:** In this example, the directory with at least 100 GB of free space is *\<dir with min 100 GB free>*. You should replace *\<dir with min 100 GB free>* in the command with the full path to your directory with a minimum of 100 GB of free space.

   ```
   sudo systemctl stop docker
   sudo mv /var/lib/docker <dir with min 100 GB free>
   sudo ln -s <dir with min 100 GB free> /var/lib/docker
   sudo systemctl start docker
   ```
2. Repeat the action that produced the `Low disk space` message.

The action should succeed without producing a `Low disk space` message.

***

## Authentication failure after upgrading Remote Worker from 10.2.7 to 10.2.9

When upgrading the Remote Worker from version **10.2.7** to **10.2.9**, the Remote Worker container fails to start. The startup log displays an error indicating that authentication failed with the SASL mechanism SCRAM-SHA-512.

This issue occurs because the Kafka user credentials used by the Remote Worker become invalid during the upgrade.

After the upgrade, the Remote Worker container (pdc-ws-remote) fails to start and shows an authentication error similar to the following in the log:

```
pdc-ws-remote-1  | {"timestamp":"2025-10-23T14:58:57.283873123Z","sequence":447,"loggerClassName":"org.jboss.logging.Logger","loggerName":"io.quarkus.runtime.Application","level":"ERROR","message":"Failed to start application","threadName":"main","threadId":1,"mdc":{},"ndc":"","hostName":"b6d234061919","processName":"/opt/java/openjdk/bin/java","processId":1,"exception":{"refId":1,"exceptionType":"java.lang.RuntimeException","message":"Failed to start quarkus","frames":[{"class":"io.quarkus.runner.ApplicationImpl","method":"doStart"},{"class":"io.quarkus.runtime.Application","method":"start","line":101},{"class":"io.quarkus.runtime.ApplicationLifecycleManager","method":"run","line":121},{"class":"io.quarkus.runtime.Quarkus","method":"run","line":77},{"class":"io.quarkus.runtime.Quarkus","method":"run","line":48},{"class":"io.quarkus.runtime.Quarkus","method":"run","line":137},{"class":"io.quarkus.runner.GeneratedMain","method":"main"}],"causedBy":{"exception":{"refId":2,"exceptionType":"jakarta.enterprise.inject.CreationException","message":"java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.SaslAuthenticationException: Authentication failed during authentication due to invalid credentials with SASL mechanism SCRAM-SHA-512","frames":[{"class":"com.pentaho.job.server.services.JobServiceMain_Bean","method":"create"},{"class":"com.pentaho.job.server.services.JobServiceMain_Bean","method":"create"},{"class":"io.quarkus.arc.impl.AbstractSharedContext","method":"createInstanceHandle","line":119},{"class":"io.quarkus.arc.impl.AbstractSharedContext$1","method":"get","line":38},{"class":"io.quarkus.arc.impl.AbstractSharedContext$1","method":"get","line":35},{"class":"io.quarkus.arc.generator.Default_jakarta_enterprise_context_ApplicationScoped_ContextInstances","method":"c9"},{"class":"io.quarkus.arc.generator.Default_jakarta_enterprise_context_ApplicationScoped_ContextInstances","method":"computeIfAbsent"},{"class":"io.quarkus.arc.impl.AbstractSharedContext","method":"get","line":35},{"class":"io.quarkus.arc.impl.ClientProxies","method":"getApplicationScopedDelegate","line":23},{"class":"com.pentaho.job.server.services.JobServiceMain_ClientProxy","method":"arc$delegate"},{"class":"com.pentaho.job.server.services.JobServiceMain_ClientProxy","method":"arc_contextualInstance"},{"class":"com.pentaho.job.server.services.JobServiceMain_Observer_Synthetic_Fe9tBUvfDGKBAGnSqsrAvtpRsn8","method":"notify"},{"class":"io.quarkus.arc.impl.EventImpl$Notifier","method":"notifyObservers","line":365},{"class":"io.quarkus.arc.impl.EventImpl$Notifier","method":"notify","line":347},{"class":"io.quarkus.arc.impl.EventImpl","method":"fire","line":81},{"class":"io.quarkus.arc.runtime.ArcRecorder","method":"fireLifecycleEvent","line":163},{"class":"io.quarkus.arc.runtime.ArcRecorder","method":"handleLifecycleEvents","line":114},{"class":"io.quarkus.runner.recorded.LifecycleEventsBuildStep$startupEvent1144526294","method":"deploy_0"},{"class":"io.quarkus.runner.recorded.LifecycleEventsBuildStep$startupEvent1144526294","method":"deploy"},{"class":"io.quarkus.runner.ApplicationImpl","method":"doStart"},{"class":"io.quarkus.runtime.Application","method":"start","line":101},{"class":"io.quarkus.runtime.ApplicationLifecycleManager","method":"run","line":121},{"class":"io.quarkus.runtime.Quarkus","method":"run","line":77},{"class":"io.quarkus.runtime.Quarkus","method":"run","line":48},{"class":"io.quarkus.runtime.Quarkus","method":"run","line":137},{"class":"io.quarkus.runner.GeneratedMain","method":"main"}],"causedBy":{"exception":{"refId":3,"exceptionType":"java.util.concurrent.ExecutionException","message":"org.apache.kafka.common.errors.SaslAuthenticationException: Authentication failed during authentication due to invalid credentials with SASL mechanism SCRAM-SHA-512","frames":[{"class":"java.util.concurrent.CompletableFuture","method":"reportGet"},{"class":"java.util.concurrent.CompletableFuture","method":"get"},{"class":"org.apache.kafka.common.internals.KafkaFutureImpl","method":"get","line":165},{"class":"com.pentaho.job.server.utils.Consumer","method":"createTopicIfNotExists","line":138},{"class":"com.pentaho.job.server.utils.Consumer","method":"startConsumer","line":43},{"class":"com.pentaho.job.server.services.JobServiceMain","method":"onStart","line":80},{"class":"com.pentaho.job.server.services.JobServiceMain_Bean","method":"doCreate"},{"class":"com.pentaho.job.server.services.JobServiceMain_Bean","method":"create"},{"class":"com.pentaho.job.server.services.JobServiceMain_Bean","method":"create"},{"class":"io.quarkus.arc.impl.AbstractSharedContext","method":"createInstanceHandle","line":119},{"class":"io.quarkus.arc.impl.AbstractSharedContext$1","method":"get","line":38},{"class":"io.quarkus.arc.impl.AbstractSharedContext$1","method":"get","line":35},{"class":"io.quarkus.arc.generator.Default_jakarta_enterprise_context_ApplicationScoped_ContextInstances","method":"c9"},{"class":"io.quarkus.arc.generator.Default_jakarta_enterprise_context_ApplicationScoped_ContextInstances","method":"computeIfAbsent"},{"class":"io.quarkus.arc.impl.AbstractSharedContext","method":"get","line":35},{"class":"io.quarkus.arc.impl.ClientProxies","method":"getApplicationScopedDelegate","line":23},{"class":"com.pentaho.job.server.services.JobServiceMain_ClientProxy","method":"arc$delegate"},{"class":"com.pentaho.job.server.services.JobServiceMain_ClientProxy","method":"arc_contextualInstance"},{"class":"com.pentaho.job.server.services.JobServiceMain_Observer_Synthetic_Fe9tBUvfDGKBAGnSqsrAvtpRsn8","method":"notify"},{"class":"io.quarkus.arc.impl.EventImpl$Notifier","method":"notifyObservers","line":365},{"class":"io.quarkus.arc.impl.EventImpl$Notifier","method":"notify","line":347},{"class":"io.quarkus.arc.impl.EventImpl","method":"fire","line":81},{"class":"io.quarkus.arc.runtime.ArcRecorder","method":"fireLifecycleEvent","line":163},{"class":"io.quarkus.arc.runtime.ArcRecorder","method":"handleLifecycleEvents","line":114},{"class":"io.quarkus.runner.recorded.LifecycleEventsBuildStep$startupEvent1144526294","method":"deploy_0"},{"class":"io.quarkus.runner.recorded.LifecycleEventsBuildStep$startupEvent1144526294","method":"deploy"},{"class":"io.quarkus.runner.ApplicationImpl","method":"doStart"},{"class":"io.quarkus.runtime.Application","method":"start","line":101},{"class":"io.quarkus.runtime.ApplicationLifecycleManager","method":"run","line":121},{"class":"io.quarkus.runtime.Quarkus","method":"run","line":77},{"class":"io.quarkus.runtime.Quarkus","method":"run","line":48},{"class":"io.quarkus.runtime.Quarkus","method":"run","line":137},{"class":"io.quarkus.runner.GeneratedMain","method":"main"}],"causedBy":{"exception":{"refId":4,"exceptionType":"org.apache.kafka.common.errors.SaslAuthenticationException","message":"Authentication failed during authentication due to invalid credentials with SASL mechanism SCRAM-SHA-512","frames":[]}}}}}}}}
pdc-ws-remote-1  | {"timestamp":"2025-10-23T14:58:57.293651565Z","sequence":448,"loggerClassName":"org.jboss.logging.Logger","loggerName":"com.pentaho.exec.utils.Monitor","level":"INFO","message":"monitor: pool exiting","threadName":"Thread-6","threadId":31,"mdc":{},"ndc":"","hostName":"b6d234061919","processName":"/opt/java/openjdk/bin/java","processId":1}
```

**Workaround**

You can fix this issue by resetting the Kafka SCRAM-SHA-512 password for the pdcuser on the PDC main server and restarting the Remote Worker.

Use the following steps to resolve this issue:

1. Log in to the Kafka container on the PDC main server:

   ```
   sudo ./pdc.sh shell kafka
   ```
2. Run the following command to reset the SCRAM-SHA-512 password for the Kafka user pdcuser:

   ```
   kafka-configs.sh --bootstrap-server kafka:9092 \
   --alter --add-config 'SCRAM-SHA-512=[password=GvTEOULMgqjOrlfE13]' \
   --entity-type users --entity-name pdcuser
   ```
3. Exit the Kafka container.
4. Restart the Remote Worker service:

   ```
   sudo ./pdc.sh restart
   ```

After resetting the Kafka password and restarting the Remote Worker, authentication succeeds and the Remote Worker starts successfully.

***

## **Chatbot vector indexing issues** <a href="#troubleshoot-chatbot-vector-indexing-issues" id="troubleshoot-chatbot-vector-indexing-issues"></a>

The chatbot indexing process is designed to prevent duplicate execution and overlapping runs. Only one indexing job can run at a time. During normal operation:

* If an indexing job is already running, a second job does not start.
* If multiple triggers occur close together (for example, a manual trigger and a scheduled cron run), only one indexing job runs.
* If the service is restarted while an indexing job is in progress, a new job does not start until the previous job state is cleaned up.

When an indexing job completes successfully, no manual cleanup is required. Subsequent runs execute according to the configured schedule and perform incremental indexing.

However, if an indexing job is interrupted or the service is restarted before the job completes, the stored job state may prevent new indexing jobs from starting. In such cases, scheduled jobs may not run, manual triggers may have no effect, and no new embeddings are generated.

***

### **Symptoms** <a href="#symptoms" id="symptoms"></a>

If the indexing process does not resume after an interruption, you may observe one or more of the following:

* The scheduled cron job does not start at the expected time.
* A manual indexing trigger does not initiate a new job.
* No new embeddings are generated in the vector database.
* Backend logs do not show indexing activity.
* Recently added or modified metadata does not appear in chatbot results.

These symptoms typically indicate that a previous indexing job did not complete successfully and that the stored job state is preventing new indexing jobs from starting.

***

### **Cleanup an incomplete indexing job** <a href="#cleanup-an-incomplete-indexing-job" id="cleanup-an-incomplete-indexing-job"></a>

Cleanup is required only when an indexing job was interrupted and the system cannot start a new job because the previous job state remains active. Perform the cleanup procedure only if all of the following conditions are true:

* An indexing job was running.
* The service or pod was restarted before the job completed.
* The scheduled cron job does not start.
* Manual indexing triggers do not initiate a new job.
* No indexing activity appears in the backend logs.

In this situation, the incomplete job state stored in Redis prevents new indexing jobs from starting.

Perform the following steps to remove the incomplete indexing state.

**Procedure**

1. Open a terminal session on the server where Pentaho Data Catalog is deployed.
2. Shell into the Redis container.

   ```
   sudo ./pdc.sh shell redis-master
   ```
3. Inside the container, list environment variables to locate the Redis password.

   ```
   env
   ```

   Identify the value of the Redis password (for example, REDIS\_PASSWORD).
4. Connect to Redis using the redis-cli.

   ```
   redis-cli -a <password>
   ```

   Replace \<password> with the value obtained from the previous step.
5. List keys to verify the presence of the indexing state.

   ```
   keys *
   ```

   Look for the key:

   ```
   metadata_indexer_job
   ```
6. Delete the incomplete indexing state key.

   ```
   del metadata_indexer_job
   ```

   After deleting this key, the system treats the previous indexing job as cleaned up.
7. Exit the Redis shell.

**Result**

The incomplete indexing job state is removed from Redis. You can now [#start-a-new-indexing-job-after-cleanup](#start-a-new-indexing-job-after-cleanup "mention"), either manually or according to the configured schedule. After a successful indexing run, future jobs execute automatically and perform incremental updates.

***

### **Start a new indexing job after the cleanup** <a href="#start-a-new-indexing-job-after-cleanup" id="start-a-new-indexing-job-after-cleanup"></a>

After cleanup, you can either wait for the next scheduled cron run or manually trigger a new indexing job. You can manually trigger jobs in two ways:

{% tabs %}
{% tab title="Option 1" %}

#### **Option 1: Trigger using API from the chatbot backend container**

1. Open a terminal session on the server.
2. Shell into the chatbot backend container.

   ```
   sudo ./pdc.sh shell chatbot-backend
   ```
3. Trigger the indexing job.

   ```
   curl -X POST http://chatbot-backend:5000/api/chat/run_indexer
   ```

   This immediately starts a new indexing job, provided no other job is running.

   Endpoint used:

   ```
   http://chatbot-backend:5000/api/chat/run_indexer
   ```

{% endtab %}

{% tab title="Option 2" %}

#### **Option 2: Trigger indexing using cron** <a href="#option-2-trigger-indexing-using-cron" id="option-2-trigger-indexing-using-cron"></a>

Temporarily change the indexing schedule environment variable to `@now`. For more information, see [#configure-a-large-language-model-llm-for-the-chatbot-in-data-catalog](https://docs.pentaho.com/pdc-admin/ldc-advanced-configuration-ut_cp#configure-a-large-language-model-llm-for-the-chatbot-in-data-catalog "mention").

After applying the configuration change and restarting the service, the indexing job runs immediately per the platform’s cron scheduling. After the indexing job starts, restore the original cron schedule.
{% endtab %}
{% endtabs %}

***

## OpenSearch jobs may fail or stall when running high parallel loads

When Pentaho Data Catalog executes a large number of parallel jobs, such as concurrent scans, profiling jobs, or metadata loads, OpenSearch may reach its default limit for open scroll contexts. By default, the OpenSearch setting search.max\_open\_scroll\_context is set to **500**. Pentaho Data Catalog uses OpenSearch scroll queries to read large result sets, and each parallel job can open one or more scroll contexts. When the combined number of concurrent read operations exceeds this limit, jobs can fail, stall, or behave unpredictably, especially in performance or high-concurrency environments. This issue is more likely to occur when:

* Multiple workers execute jobs in parallel.
* Large datasets are processed concurrently.
* Performance or load testing environments are used.
* High read concurrency is configured in Data Catalog.

**Resolution**

To resolve this issue, you can increase the OpenSearch scroll context limit by updating the cluster configuration. Perform the following steps to update `search.max_open_scroll_context` value:

**Procedure**

1. Connect to the **opensearch-master** pod.

   Example:

   ```
   kubectl exec -it <opensearch-master-pod-name> -- /bin/bash
   ```
2. Run the following command to increase the scroll context limit:

   ```
   curl -XPUT "localhost:9200/_cluster/settings" \
     -H 'Content-Type: application/json' \
     -d '{
       "persistent": {
         "search.max_open_scroll_context": 2000
       }
     }'
   ```

**Result**

OpenSearch allows up to 2000 concurrent scroll contexts, enabling Pentaho Data Catalog to run a higher number of parallel jobs without hitting scroll context limits.

{% hint style="info" %}
The Pentaho Data Catalog team validated **2000** for performance environments. You can increase this value further if required, based on your infrastructure capacity.
{% endhint %}

***

## Unable to connect to OpenSearch using HTTPS (Security plugin not initialized)&#x20;

When accessing OpenSearch over HTTPS, the system may fail to connect because the OpenSearch Security plugin is enabled but not yet initialized. This occurs when the .opendistro\_security index does not exist, preventing OpenSearch from recognizing user credentials, roles, TLS settings, and other security configurations.&#x20;

You may see the following error in the logs:&#x20;

{% code overflow="wrap" %}

```
[2025-06-16T16:53:35,311][ERROR][o.o.s.c.ConfigurationLoaderSecurity7] [af38e3ceb454] Failure no such index [.opendistro_security] retrieving configuration for [ACTIONGROUPS, ALLOWLIST, AUDIT, CONFIG, INTERNALUSERS, NODESDN, ROLES, ROLESMAPPING, TENANTS, WHITELIST] (index=.opendistro_security) 
```

{% endcode %}

This issue typically appears during an upgrade (for example, from PDC 10.2.1 to 10.2.6), not in fresh installations of Data Catalog 10.2.5 or later, where the security index is initialized by default.&#x20;

{% hint style="warning" %}
For fresh installations, the initialization process should be performed only under the supervision of Pentaho Data Catalog Customer Support. &#x20;
{% endhint %}

**Workaround**

Perform the following steps to resolve the issue:&#x20;

1. Log in to the deployment server where Data Catalog is running.&#x20;
2. Stop all Pentaho Data Catalog containers:

   <pre><code><strong>--alter --add-config 'SCRAM-SHA-512=[password=GvTEOULMgqjOrlfE13]' \
   </strong>--entity-type users --entity-name pdcuser 
   </code></pre>

./pdc.sh stop&#x20;

3. Identify the OpenSearch container IDs.

   ```
   docker ps -a | grep pdc-opensearch 
   ```
4. Remove the OpenSearch containers.

   ```
   docker rm <container_id1> <container_id2> <container_id3> 
   ```
5. List all Docker volumes related to OpenSearch to confirm their presence:

   ```
   docker volume ls | grep pdc_opensearch
   ```

   Typical volumes include:&#x20;

   ```
   pdc_opensearch_data 
   pdc_opensearch_snapshots 
   ```

{% hint style="warning" %}
⚠️ Caution: Do not delete OpenSearch volumes unless explicitly instructed by Customer Support. Deleting these volumes will permanently remove all OpenSearch data, including indexes, and should only be done under the supervision of support.&#x20;
{% endhint %}

6. Delete the pdc\_opensearch\_data volume:&#x20;

   ```
   docker volume rm pdc_opensearch_data 
   ```
7. Delete the pdc\_opensearch\_snapshots volume:&#x20;

   ```
   docker volume rm pdc_opensearch_snapshots 
   ```
8. Restart Data Catalog services:&#x20;

   ```
   ./pdc.sh up 
   ```
9. Verify that all the services are up and running now.&#x20;

   ```
   ./pdc.sh ps
   ```

After removing the existing OpenSearch volumes and restart the system, the .opendistro\_security index is reinitialized. OpenSearch initializes the Security plugin, loads its configuration successfully, and connects over HTTPS without errors.&#x20;

***

## **Jobs remain in the&#x20;*****Accepted*****&#x20;state after deployment**

After deploying Pentaho Data Catalog, some jobs may remain in the **Accepted** state and do not move to **Running** or **Completed**. You may notice one or more of the following:

* A job appears as **Accepted** and does not progress.
* The job does not complete even after several minutes.
* Resubmitting the job shows the same behavior.
* Restarting Ops services temporarily resolves the issue.

Refreshing the browser or resubmitting the job does not resolve the issue.

**Workaround**

Restart only the **Ops services** to refresh the job scheduling components.\
Perform the following restart procedure that matches your deployment.

**Docker deployments**

1. Log in to the server where Data Catalog is installed.
2. Go to the Data Catalog installation directory (where pdc.sh is located).
3. Run the following command:

   ```
   ./pdc.sh restart ops
   ```

After the restart completes, re-run the operation that was previously stuck and verify that the job progresses normally.

**Kubernetes deployments**

1. Connect to the Kubernetes cluster where Data Catalog is deployed.
2. Restart the Ops deployment:

   ```
   kubectl rollout restart deployment cat-ops -n <namespace>
   ```
3. Monitor the rollout status:

   ```
   kubectl rollout status deployment cat-ops -n <namespace>
   ```

After the pods are ready, run the operation again and confirm that the job moves beyond the **Accepted** state.

## *Request Header Fields Too Large* error when importing metadata from Power BI

When importing metadata from Power BI, Data Catalog might display the following error:

```
Request Header Fields Too Large
```

This issue occurs when the metadata payload sent to the Power BI service exceeds the allowed header size limits. In environments with large dashboards, long report paths, or extensive metadata, this batch size may be too large and may trigger the request-header-size error.

**Workaround**

The batch size is controlled by the `POWERBI_BATCH_SIZE` environment variable in the `docker-compose.bi-metadata.yml` file.

```
POWERBI_BATCH_SIZE=50
```

By default, Data Catalog uses a batch size of **50** when fetching metadata from Power BI. Reduce the value of the `POWERBI_BATCH_SIZE` environment variable to lower the number of metadata items sent per request. A smaller batch size reduces header size and prevents the error from occurring.

Perform the following steps to reduce the value of the `POWERBI_BATCH_SIZE` environment variable:

**Procedure for Docker deployments**

1. Open the Data Catalog installation directory:

   ```
   /opt/pentaho/pdc-docker-deployment/
   ```
2. Open the docker-compose.bi-metadata.yml file from the same directory:

   ```
   ./vendor/docker-compose.bi-metadata.yml
   ```
3. Locate the following environment variable:

   ```
   POWERBI_BATCH_SIZE=50
   ```
4. Reduce the value. For example:

   ```
   POWERBI_BATCH_SIZE=20
   ```

   You can try **20**, **10**, or even **5**, depending on the environment size.
5. Save the file.
6. Restart the **bi-metadata** service:

   ```
   ./pdc.sh restart bi-metadata
   ```
7. Re-run the Power BI metadata import.

**Procedure for Kubernetes deployments**

If you deploy using Helm or Kubernetes manifests, update the environment variable in the bi-metadata deployment and restart the pods:

1. Go to the Helm chart directory for your PDC deployment:

   ```
   pdc-helm-charts/charts/pdc/
   ```
2. Open the values file for the **bi-metadata-api** service and set or update the batch size.\
   The environment variables for this service are defined in:

   ```
   charts/pdc/charts/bi-metadata-api/values.yaml
   ```

   Add or update the following entry:

   ```
   POWERBI_BATCH_SIZE: 20
   ```

   The chart will inject this value into the deployment templates, including:

   ```
   charts/pdc/charts/bi-metadata-api/templates/values.yaml
   ```
3. Save the changes.
4. After updating the values file, redeploy the Helm chart:

   ```
   helmfile sync -n <namespace>
   ```
5. Wait for the bi-metadata-api pods to restart.\
   You can check the rollout status using:

   ```
   kubectl get pods -n <namespace>
   ```
6. Re-run the Power BI metadata import.

**Result**

Data Catalog applies the updated batch size to Power BI metadata requests. The metadata import operation proceeds without triggering the *Request Header Fields Too Large* error. If the error persists, reduce the batch size further and redeploy the Helm chart.

**Recommended values**

The optimal batch size depends on the amount of metadata per workspace. Use the following guidance:

<table><thead><tr><th width="139">Batch size</th><th>When to use</th></tr></thead><tbody><tr><td><strong>50 (default)</strong></td><td>Small to medium Power BI environments</td></tr><tr><td><strong>20</strong></td><td>Large metadata collections, occasional failures</td></tr><tr><td><strong>10</strong></td><td>Frequent “Request Header Fields Too Large” errors</td></tr><tr><td><strong>5</strong></td><td>Very large or complex Power BI deployments</td></tr></tbody></table>

## Metadata rule execution fails for large generic conditions

When you configure a Metadata Rule with a very generic condition that matches a large number of files, the associated [Data Discovery](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-processing-data#data-discovery) or [Data Profiling](https://app.gitbook.com/s/RAKLVv06oBKpy9VLbw7P/ldc-explore-your-data-cp/pdc-processing-data#data-profiling) job may not start or complete successfully.

In this scenario:

* The rule execution status initially appears as **Submitted**.
* The status then changes to **Failed** in the rule execution history.
* No corresponding Data Discovery or Data Profile job completes for the matched files.

This issue typically occurs when the rule matches a very large number of assets and the job submission payload exceeds processing limits.

**Workaround**

In Data Catalog, the rules engine supports **batching** when submitting Data Discovery or Data Profile jobs. You can reduce the batch size to limit the number of asset IDs submitted in a single request.

By default, the batch size is set to 10,000 IDs per batch, and the batch size is controlled by the RULES\_START\_PROCESS\_PAYLOAD\_BATCH\_SIZE environment variable.

To mitigate this issue, reduce the batch size value.

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
4. Add or update the following environment variable:

   ```
   RULES_START_PROCESS_PAYLOAD_BATCH_SIZE=10000
   ```
5. Reduce the batch size to a lower value, for example:

   ```
   RULES_START_PROCESS_PAYLOAD_BATCH_SIZE=5000
   ```
6. Save the file.
7. Restart the Pentaho Data Catalog application to apply the change.

   ```
   ./pdc.sh up
   ```
8. Rerun the metadata rule.

**Result**

The rules engine submits Data Discovery or Data Profile jobs in smaller batches, reducing payload size and allowing the jobs to start and complete successfully for large rule matches.
