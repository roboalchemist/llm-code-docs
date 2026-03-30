# Source: https://docs.anyscale.com/resources/environment-variables.md

# Environment variables

[View Markdown](/resources/environment-variables.md)

# Environment variables

The following environment variables are available in the Ray container for all Anyscale clusters and can be used in initialization scripts to configure various aspects of the container and cluster operations:

* `ANYSCALE_ARTIFACT_STORAGE` - Path for storing runtime artifacts; for example, `s3://$ANYSCALE_CLOUD_STORAGE_BUCKET/$ANYSCALE_ORGANIZATION_ID/$ANYSCALE_CLOUD_ID/artifact_storage/`.
* `ANYSCALE_CLI_TOKEN` - Token for authenticating the current context to Anyscale.
* `ANYSCALE_CLOUD_ID` - Cloud ID.
* `ANYSCALE_CLOUD_STORAGE_BUCKET` - Name of the storage bucket for this cluster's cloud.
* `ANYSCALE_CLOUD_STORAGE_BUCKET_REGION` - Region of the storage bucket for this cluster's cloud.
* `ANYSCALE_CLUSTER_ID` - Cluster ID.
* `ANYSCALE_DEBUG` - Set to enable debug-level logging for Anyscale utilities.
* `ANYSCALE_INSTANCE_ID` - Instance ID.
* `ANYSCALE_NODE_GROUP_ID` - Name of the node group; for example, `worker-node-group-0`.
* `ANYSCALE_NODE_IP` - Instance private IP.
* `ANYSCALE_ORGANIZATION_ID` - Anyscale organization ID.
* `ANYSCALE_PROJECT_ID` - Anyscale project ID.
* `ANYSCALE_PROJECT` - Anyscale project name.
* `ANYSCALE_RAY_METRICS_ENDPOINT` - Local Prometheus address for Ray metrics exposure.
* `ANYSCALE_USERNAME` - Username of the cluster creator.
* `ANYSCALE_USER_EMAIL` - Email of the cluster creator.
* `ANYSCALE_WORKING_DIR` - Working directory of the cluster or workspace.
* `ANYSCALE_WORKLOAD_NAME` - The Anyscale job, service, or workspace name.

## Additional Anyscale jobs environment variables[​](#jobs-vars "Direct link to Additional Anyscale jobs environment variables")

The following environment variables are available in the Ray container for Anyscale jobs clusters.

* `ANYSCALE_JOB_ID` - Job ID.
* `ANYSCALE_JOB_NAME` - Job name.
* `ANYSCALE_JOB_QUEUE_ID` - The ID of the job queue if this job is part of a job queue.

## Additional Anyscale service environment variables[​](#service-vars "Direct link to Additional Anyscale service environment variables")

The following environment variables are available in the Ray container for Anyscale service clusters.

* `ANYSCALE_SERVICE_ID` - Service ID.
* `ANYSCALE_SERVICE_NAME` - Service name.
* `ANYSCALE_SERVICE_VERSION_ID` - ID of the current service version.
