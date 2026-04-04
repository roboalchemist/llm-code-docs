# Source: https://docs.aws.amazon.com/iot-twinmaker/latest/guide/llms.txt

# AWS IoT TwinMaker User Guide

> AWS IoT TwinMaker is an AWS IoT service that enables you to build operational digital twins of physical systems.

- [What is AWS IoT TwinMaker?](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/what-is-twinmaker.html)
- [AWS IoT TwinMaker app kit integration](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-app-kit.html)
- [Switch AWS IoT TwinMaker pricing modes](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-pricing-mode.html)
- [Connect Alarms to Grafana dashboards](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-alarm-config.html)
- [Matterport integration](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-matterport-integration.html)
- [Streaming video to AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/video-integration.html)
- [Using the AWS IoT TwinMaker Flink library](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-flink-library.html)
- [Endpoints and quotas](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/endpionts-and-quotas.html)
- [Document history](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/doc-history.html)

## [Getting started with AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-gs.html)

- [Create and manage a service role for AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-gs-service-role.html): AWS IoT TwinMaker requires that you use a service role to allow it to access resources in other services on your behalf.
- [Create a workspace](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-gs-workspace.html): Create and configure your first AWS IoT TwinMaker workspace.
- [Create your first entity](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-gs-entity.html): To create your first entity, use the following steps.
- [Setting up an AWS account](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/set-up-aws-account.html): Create an AWS account to get started with AWS IoT TwinMaker.


## [Using and creating component types](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-component-types.html)

- [Example component types](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/twinmaker-component-types-examples.html): This topic contains examples that show how to implement key concepts of component types.


## [Bulk operations](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-import-export.html)

- [Performing bulk import and export operations](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-import-export-api.html): Learn about how to use the AWS IoT TwinMaker metadataTransferJob.
- [AWS IoT TwinMaker metadata transfer job schema](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-import-export-schema.html): Learn about the AWS IoT TwinMaker metadata transfer job schema.


## [Data connectors](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/data-connector-interface.html)

- [Data connectors](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/data-connector-interfaces.html): Learn about the AWS IoT TwinMaker data connectors.
- [Athena tabular data connector](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/athena-tabular-data-connector.html): Learn how to use the Athena tabular data connector.

### [AWS IoT TwinMaker time-series data connector](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/time-series-data-connectors.html)

Learn how to create AWS IoT TwinMaker Time-Series Data Connectors.

- [AWS IoT TwinMaker cookie factory data connector](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/time-series-data-connectors-example.html): The complete code of the cookie factory Lambda function is available on GitHub.


## [Creating AWS IoT TwinMaker scenes](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes.html)

- [Before creating scenes](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-before-starting.html): Use best practices to optimize your resources and scenes for AWS IoT TwinMaker.
- [Uploading resources in AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-using-resource-library.html): Learn more about the AWS IoT TwinMaker resource library.
- [Create your scenes](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-creation.html): Learn more about creating AWS IoT TwinMaker scenes.
- [Add fixed cameras](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-camera.html): Learn how to add fixed cameras in AWS IoT TwinMaker scenes.
- [Enhanced editing](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-ee.html): Learn how to use the enhanced editing features in AWS IoT TwinMaker scenes.

### [Edit your scenes](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-editing.html)

Learn how to add objects and configure widgets for your scenes in AWS IoT TwinMaker.

- [Add models](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-editing-add-models.html): Learn how to add models to your scenes in AWS IoT TwinMaker.
- [Add widgets](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-editing-add-color-widget.html): Learn how to add augmented UI widgets to your scenes in AWS IoT TwinMaker.
- [Adding tags](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/scenes-editing-add-tags.html): Learn how to add tags to your scenes in AWS IoT TwinMaker.
- [Optimize your 3D model](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/3d-tiles-model-format.html): Learn how to use 3D tiles in your AWS IoT TwinMaker scenes.
- [Dynamic scenes](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/dynamic-scenes.html): Learn more about creating AWS IoT TwinMaker dynamic scenes.


## [Knowledge graph](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-knowledge-graph.html)

- [Using knowledge graph](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-knowledge-graph-use.html): Learn how to use the AWS IoT TwinMaker knowledge graph and the prerequisites required for use.
- [Generate a scene graph](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-knowledge-graph-scene.html): Learn how to use AWS IoT TwinMaker knowledge graph with AWS IoT TwinMaker scenes.
- [Knowledge graph Grafana panel](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-knowledge-Grafana-panel.html): Learn about the AWS IoT TwinMaker query editor
- [Knowledge graph additional resources](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-knowledge-graph-resources.html): Learn about the AWS IoT TwinMaker knowledge graph syntax and data model.


## [Asset synchronization with AWS IoT SiteWise](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-asset-sync.html)

### [Using asset sync with AWS IoT SiteWise](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-asset-sync-use.html)

Learn how to use asset sync in the AWS IoT TwinMaker console.

- [Using a custom workspace](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-custom-ws.html): Learn how to use asset sync with a custom workspace.
- [Using the IoTSiteWiseDefaultWorkspace](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-default-ws.html): Learn how to use asset sync with the IoTSiteWiseDefaultWorkspace.
- [Differences between custom and default workspaces](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-default-ws-diffs.html)
- [Resources synced from AWS IoT SiteWise](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-asset-sync-map.html): Learn about the mapping between AWS IoT SiteWise and AWS IoT TwinMaker resources.
- [Analyze sync status and errors](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-asset-sync-ts.html): This topic provides guidance on how to analyze sync errors and statuses.
- [Delete a sync job](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-asset-sync-delete.html): Learn how to delete a sync job.
- [Asset sync limits](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-asset-sync-limits.html): Learn how to delete a sync job.


## [Setting up Grafana dashboards](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/grafana-integration.html)

- [CORS configuration](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/cors-configuration-grafana.html): Learn how configure CORS for Grafana.

### [Setting up your Grafana environment](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/grafana-environment.html)

Learn how to set up your Grafana environment.

- [Amazon Managed Grafana](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/amazon-managed-grafana.html): Learn about using Amazon Managed Grafana with AWS IoT TwinMaker.
- [Self-managed Grafana](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/self-managed-grafana.html): Learn about using self-managed Grafana with AWS IoT TwinMaker.
- [Creating a dashboard role](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/dashboard-IAM-role.html): Learn about setting up IAM roles for AWS IoT TwinMaker.
- [Creating an AWS IoT TwinMaker Video Player policy](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-video-policy.html): Learn about creating an AWS IoT TwinMaker video player policy.


## [Logging and monitoring](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/logging-and-monitoring.html)

- [Monitoring with Amazon CloudWatch metrics](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/monitor-cloudwatch-metrics.html): Learn about monitoring AWS IoT TwinMaker with Amazon CloudWatch Metrics.
- [Logging API calls with AWS CloudTrail](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/logging-using-cloudtrail.html): Log AWS IoT TwinMaker API calls with AWS CloudTrail.


## [Security](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/security.html)

- [Data protection](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/data-protection.html): Learn how the AWS shared responsibility model applies to data protection in AWS IoT TwinMaker.

### [Identity and Access Management](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/security-iam.html)

How to authenticate requests and manage access your AWS IoT TwinMaker resources.

- [How AWS IoT TwinMaker works with IAM](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS IoT TwinMaker, learn what IAM features are available to use with AWS IoT TwinMaker.
- [Identity-based policy examples](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/security_iam_id-based-policy-examples.html): By default, users and roles don't have permission to create or modify AWS IoT TwinMaker resources.
- [Troubleshooting](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS IoT TwinMaker and IAM.
- [Using service-linked roles](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/using-service-linked-roles.html): How to use service-linked roles to give AWS IoT TwinMaker access to resources in your AWS account.
- [AWS managed policies](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS IoT TwinMaker and recent changes to those policies.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/vpc-interface-endpoints.html): You can use an interface virtual private cloud (VPC) endpoint to create a private connection between your VPC and AWS IoT TwinMaker, without requiring access over the internet or through a network address translation (NAT) device, a VPN connection, or an Direct Connect connection.
- [Compliance Validation](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/SERVICENAME-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS IoT TwinMaker features for data resiliency.
- [Infrastructure Security](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/infrastructure-security.html): Learn how AWS IoT TwinMaker isolates service traffic.
