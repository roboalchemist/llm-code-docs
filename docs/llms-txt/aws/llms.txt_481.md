# Source: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/llms.txt

# AWS IoT SiteWise User Guide

> Describes key concepts of AWS IoT SiteWise and provides instructions for using the features of AWS IoT SiteWise.

- [Get started](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/getting-started.html)
- [Use the quick start demo](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/getting-started-demo.html)
- [Endpoints and quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/endpoints-and-quotas.html)
- [Document history](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/document-history.html)

## [What is AWS IoT SiteWise?](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html)

- [Working with AWS SDKs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.
- [Concepts](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/concept-overview.html): Learn about the core concepts of AWS IoT SiteWise.


## [Tutorials](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tutorials.html)

- [Calculate OEE](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/calculate-oee.html): Calculate the industrial operation overall equipment effectiveness, or OEE, using AWS IoT SiteWise.
- [Ingest data](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-data-from-iot-things.html): A tutorials to learn how to ingest data from AWS IoT things by using the AWS IoT SiteWise rule action.
- [Integrate data with SiteWise Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/integrate_sitewise_edge_mqtt.html): A tutorial to learn how to intergrate data by using the AWS IoT SiteWise and MQTT-enabled, V3 gateway
- [Visualize and share data in Grafana](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/visualize-with-grafana.html): This tutorial teaches you how to visualize data in Grafana using the AWS IoT SiteWise plugin.
- [Visualize and share data in SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-wind-farm.html): Learn how to visualize and share your industrial data using the wind farm demo in this AWS IoT SiteWise Monitor tutorial.
- [Publish to Amazon DynamoDB](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/publish-to-amazon-dynamodb.html): Learn how to interact with other AWS services by publishing your asset property value updates from AWS IoT SiteWise to a DynamoDB table in this tutorial.


## [Ingest data to AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/industrial-data-ingestion.html)

### [Manage data streams](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-data-streams.html)

Explore data stream management in AWS IoT SiteWise.

- [Configure permissions and settings](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-data-streams-configuration.html): Configure your IoT SiteWise permissions and settings to accept data streams.
- [Associate a data stream to an asset property](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-data-streams-method.html): Manage data streams in AWS IoT SiteWise.
- [Disassociate a data stream from an asset property](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/disassociate-data-streams-method.html): Manage data streams in AWS IoT SiteWise.
- [Delete a data stream](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-data-streams-method.html): Manage data streams in AWS IoT SiteWise.
- [Update an asset property alias](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-data-streams-method.html): Update an asset property alias in AWS IoT SiteWise.
- [Common scenarios](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-ingestion-scenarios.html): Scenarios for data ingestion three examples.

### [Ingest data with AWS IoT SiteWise APIs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html)

Use the AWS IoT SiteWise API to ingest your asset data.

- [BatchPutAssetPropertyValue API](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api-batch-putasset.html): Use the BatchPutAssetPropertyValue API to ingest your asset data.

### [CreateBulkImportJob API](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-bulkImport.html)

Use the CreateBulkImportJob API to import data from Amazon S3.

- [Create a bulk import job](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/CreateBulkImportJob.html): Transfer data from Amazon S3 to AWS IoT SiteWise using the CreateBulkImportJob API.
- [Describe a bulk import job](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/DescribeBulkImportJob.html): Retrieve information about a bulk import job in AWS IoT SiteWise.
- [List bulk import jobs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ListBulkImportJobs.html): Retrieve a list of summaries of AWS IoT SiteWise bulk import jobs.

### [Use AWS IoT Core rules](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/iot-rules.html)

Ingest asset data to AWS IoT SiteWise using AWS IoT Core rules with MQTT.

- [Grant required access](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/grant-rule-access.html): Provide a rule action with access to your asset properties in AWS IoT SiteWise.
- [Configure the rule action](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-rule-action.html): Configure the AWS IoT SiteWise rule action to ingest data from MQTT messages.
- [Reduce costs with Basic Ingest](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/basic-ingest-rules.html): Use Basic Ingest to send data to a rule without incurring messaging costs.
- [Use AWS IoT Events actions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/iot-events.html): Learn how to ingest asset data when an event occurs in AWS IoT Events.
- [Use AWS IoT Greengrass stream manager](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/greengrass-stream-manager.html): Use AWS IoT Greengrass stream manager to ingest asset data through custom edge sources.


## [Use SiteWise Edge gateways](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html)

### [Self-host a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gw-self-host-gg2.html)

Learn how self-hosting an AWS IoT SiteWise gateway works with AWS IoT Greengrass V2 so that you can collect, process and visualize your data.

- [Requirements](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-gateway-ggv2.html): Learn more about the requirements for SiteWise Edge gateways.
- [Create a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-gateway-ggv2.html): Use the AWS IoT SiteWise console to create a SiteWise Edge gateway.
- [Install gateway software](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/install-gateway-software-on-local-device.html): Install the SiteWise Edge gateway software to set up your local device with Linux or on Microsoft Windows server.

### [MQTT-enabled, V3 gateways](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/mqtt-enabled-v3-gateway.html)

A description of how the MQTT protocol works within the AWS IoT SiteWise architecture.

### [Connect external applications](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-external-applications-emqx.html)

Learn how to connect external applications to AWS IoT SiteWise using the EMQX broker.

- [Message payload format](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-broker-payload-format.html): Learn about the payload format requirements for messages sent to the AWS IoT Greengrass EMQX broker on AWS IoT SiteWise Edge.
- [](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-emqx-broker.html): Configure the EMQX broker.
- [Connect an application](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-app-to-broker.html): Learn how to connect an application to AWS IoT SiteWise using the EMQX broker.

### [Set up authorization rules](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/authorization-rules-emqx-broker.html)

EMQX supports adding authorization rules based on identifiers such as username, IP address or client ID.

- [Configure authorization using Linux](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-auth-rules-database-emqx-broker-linux.html): When you configure authorization rules, there are two configuration choices that depend on your deployment setup.
- [Configure authorization using Microsoft Windows](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-auth-rules-database-emqx-broker-windows.html): This section covers configuring authorization rules using the built-in database for Windows deployments.
- [Update the deployment](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-emqx-broker-authorization.html)
- [Add authorization rules for users](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-rules-emqx-broker.html): You can add or update authorization rules using the EMQX Dashboard or the AWS IoT SiteWise EMQX CLI tool.

### [Process and visualize data at the Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/open-source-edge-integrations.html)

Learn how to integrate open source tools with SiteWise Edge for local data processing, storage, and visualization.

### [Manual setup using Windows](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/windows-manual-setup.html)

Use this guide to manually create a time series bucket for wind speed data that connects with GrafanaÂ® and Node-REDÂ®.

- [Set up local storage with InfluxDB](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/windows-influxdb-setup.html): With InfluxDBÂ®, you can store time series data from your devices locally.

### [Configure Node-RED flows](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/windows-nodered-config.html)

Configure Node-RED flows to publish device data to AWS IoT SiteWise and store data locally.

- [Configure the data publish flow](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/windows-nodered-data-publish-flow.html): The data publish flow uses three nodes to create a pipeline that sends your industrial data to the cloud.
- [Configure the data retention flow](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/windows-nodered-data-retention-flow.html): The data retention flow is can be used to maintain operational visibility at the edge.
- [Set up Grafana for SiteWise Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/windows-grafana.html): GrafanaÂ® lets you create local real-time monitoring dashboards for your industrial data.
- [Docker setup using Linux](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/linux-docker-setup.html): Deploy SiteWise Edge, InfluxDB, Node-RED, and Grafana using Docker.
- [Process data for open source integrations](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/open-source-data-processing-open-source.html): The data can be processed (such as transformation or aggregation), at different stages using various tools, each serving different monitoring requirements.

### [Classic streams, V2 gateways](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/classic-streams-v2-gateway.html)

Understand the features and limitations of Classic streams, V2 gateways for AWS IoT SiteWise Edge.

### [Use packs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-packs.html)

Enable packs on your SiteWise Edge gateway for AWS IoT SiteWise.

- [Data processing pack availability change](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/iotsitewise-dpp-availability-change.html)
- [Configure the publisher](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-publisher-component.html): Learn how to configure the AWS IoT SiteWise publisher component.
- [AWS IoT Greengrass stream manager](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/destinations-gg-stream-manager.html): Use AWS IoT Greengrass stream manager to send data to various AWS Cloud destinations.
- [Configure edge capabilities](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-data-collection-and-processing.html): Information on collecting data at the edge and optional processing capabilities through AWS IoT SiteWise.
- [Configure edge data processing](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-processing.html): Add edge processing capability to your AWS IoT SiteWise models and assets.

### [Add data sources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-data-sources.html)

Learn how to configure a self-hosted gateway on AWS IoT SiteWise Edge.

### [OPC UA data sources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources-opcua.html)

Learn how to configure data sources so your SiteWise Edge gateway can ingest data from industrial equipment to AWS IoT SiteWise.

- [Set up an OPC UA source](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-opcua-source.html): Add and define an OPC UA source to your SiteWise Edge gateway.
- [Set up OPC UA servers to trust the gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/enable-source-trust.html): Enable your industrial data sources to trust your SiteWise Edge gateway.
- [Filter data ingestion ranges](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opcua-data-acquisition.html): Learn how to filter ingested data using OPC UA deadbanding and scan mode.
- [Use OPC UA node filters](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opc-ua-node-filters.html): Learn how to use OPC UA node filter wildcards for your SiteWise Edge gateway sources.
- [Converting unsupported data types](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/string-conversion.html): How to convert unsupported data types for source data to prevent data loss in AWS IoT SiteWise Edge
- [Configure data source authentication](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-source-authentication-ggv2.html): Describes how to configure authentication secrets so that your SiteWise Edge gateway can connect to your local servers.

### [Partner data sources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/partner-data-sources.html)

Add a partner data source to an SiteWise Edge gateway.

- [Set up Docker on a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/cpa-install-docker.html): Set up Docker on your SiteWise Edge gateway for use with partner data sources.
- [Add a partner data source](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/cpa-add-source.html): Add partner data sources to SiteWise Edge gateways.
- [Partner data source options](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-partner-data-source.html): Information about specific SiteWise Edge gateway partner data sources
- [Components for SiteWise Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sw-edge-components.html): Explore the key AWS IoT Greengrass components that enable SiteWise Edge functionality at the edge.
- [Filter assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/filter-assets-ggv2.html): Use edge filtering to manage the assets on your SiteWise Edge gateway.

### [Proxy support and trust stores](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-apis-manage-trust-stores-proxy.html)

Learn how to configure proxy HTTPS for SiteWise Edge gateways by managing trust stores.

- [Configure proxy settings during installation](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-trust-stores-proxy_config.html): Step-by-step instructions for installing an AWS IoT SiteWise gateway with proxy settings.
- [Manually configure trust stores for HTTPS proxy support](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-trust-stores-proxy_trust-store-locations-and-configuration.html): Learn how to configure trust store locations for different SiteWise Edge components to enable proxy support.

### [Use APIs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-apis.html)

Utilize the AWS IoT SiteWise Edge API.

- [All available APIs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-apis-available.html): List of all APIs available for use with SiteWise Edge edge devices.
- [Edge-only APIs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-local-apis.html): The list of APIs that are available for use on AWS IoT SiteWise edge devices only.
- [Enable CORS](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/enable-cors-edge-apis.html): Enable CORS for AWS IoT SiteWise Edge APIs.
- [Configure session timeouts](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-apis-session-timeout.html): Learn how to configure a session timeout for SiteWise Edge APIs so that you can enhance security by automatically terminating inactive sessions.
- [Tutorial: Get a list of asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-apis-tutorial.html): Learn how to set up and use APIs on SiteWise Edge gateways.

### [Host a gateway on Siemens Industrial Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sitewise-edge-on-siemens.html)

Learn how to run AWS IoT SiteWise on Siemens Industrial Edge devices.

- [Requirements](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/siemens-app-gateway-requirements.html): The requirements for the AWS IoT SiteWise Edge application on Siemens Industrial Edge.
- [Create a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sa-create-config.html): How to create a SiteWise Edge gateway using Siemens Industrial Edge.
- [Create a Siemens Databus user](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sa-databus-user.html): Create a Siemens Databus user for the AWS IoT SiteWise Edge application in Siemens Industrial Edge
- [Access the application](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sa-get-app.html): How to get access to the AWS IoT SiteWise Edge application
- [Install the application](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sa-install-app.html): How to install the AWS IoT SiteWise Edge application on Siemens Industrial Edge
- [Update an installed application configuration](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sa-update-config.html): When and how to update installed configuration for the AWS IoT SiteWise Edge application on Siemens Industrial Edge.
- [Data generated by the use of this service](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sa-data-legal.html): Data generated by the use of this service

### [Destinations and path filters](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gw-destinations.html)

Learn about SiteWise Edge destinations to efficiently export data from sources and data processing pipelines.

- [Add a real-time destination](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/destinations-real-time.html): Configure a real-time destination to stream IoT data directly from devices and gateways into AWS IoT SiteWise storage.
- [Add a buffered destination using Amazon S3](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/destinations-buffered.html): Configure a buffered destination to temporarily store IoT data in an Amazon S3 bucket before importing it into AWS IoT SiteWise.
- [Add path filters](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/destinations-add-path-filters.html): Add path filters to a destination.
- [Manage destinations](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/destinations-manage.html): Perform various operations to manage your destinations in SiteWise Edge.
- [Manage gateways](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-gateways-ggv2.html): Manage your SiteWise Edge gateway through the console or local SiteWise Edge gateway application.
- [Back up and restore gateways](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/backup-restore-gateways-ggv2.html): Learn how to back up and restore SiteWise Edge gateways.
- [Legacy gateways (AWS IoT Greengrass Version 1)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv1.html): Learn about setting up a AWS IoT Greengrass Version 1 SiteWise Edge gateway.


## [Model industrial assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/industrial-asset-models.html)

### [Asset and model states](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-and-model-states.html)

Learn about the states that assets and models can have and when these states occur in AWS IoT SiteWise.

- [Check the status of an asset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/check-asset-status.html): You can use the AWS IoT SiteWise console or API to check the status of an asset.
- [Check the status of an asset or component model](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/check-model-status.html): You can use the AWS IoT SiteWise console or API to check the status of an asset model or component model.
- [Asset model versions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html): Learn how to retrieve the active version of an asset model or component model AWS IoT SiteWise.
- [Custom composite models (components)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html): Learn about how to stay organized with custom composite models, or components, in AWS IoT SiteWise.

### [Asset model interfaces](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-interfaces.html)

Learn about using interfaces to set standards across different asset models in AWS IoT SiteWise.

- [Understand the interface-asset model relationship](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interface-asset-model-relationship.html): Interfaces and asset models work together in a complementary relationship:
- [Create an interface](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interface-create.html): You can create interfaces using either the AWS IoT SiteWise console or the AWS CLI.
- [Apply an interface to an asset model](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interfaces-link-asset-model.html): When applying an interface to an asset model, you map asset model properties and hierarchies to their interface counterparts.
- [Manage interfaces](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interfaces-manage.html): Learn how to manage interfaces and asset model relationships.
- [Additional interface examples](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interface-additional-examples.html): Here are additional examples of how interfaces can be used in different industrial scenarios:
- [Set up object IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html): Work with object IDs in AWS IoT SiteWise.

### [Create models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-asset-and-component-models.html)

Create asset models, component models, and interfaces to standardize the shape and hierarchy of your industrial data in AWS IoT SiteWise.

### [Create asset models in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-asset-models.html)

Create asset models to standardize the shape and hierarchy of your industrial data in AWS IoT SiteWise.

- [Define asset model hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-asset-hierarchies.html): Define relationships between your asset models in AWS IoT SiteWise so that you can aggregate data to compute metrics that represent your operation.
- [Create component models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-component-models.html): Create component models to represent subcomponents in AWS IoT SiteWise.

### [Define data properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html)

Learn how asset properties define data for your assets in AWS IoT SiteWise.

- [Define static data](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/attributes.html): Attribute asset properties define data that rarely changes in AWS IoT SiteWise.
- [Define data streams from equipment (measurement)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/measurements.html): Measurement asset properties define the data streams that your equipment sends to AWS IoT SiteWise.
- [Transform data (transforms)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/transforms.html): Transform asset properties map data from one form to another in AWS IoT SiteWise.
- [Aggregate data (metrics)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/metrics.html): Learn how metric asset properties define how to aggregate data from properties and other assets in AWS IoT SiteWise.

### [Use formula expressions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/formula-expressions.html)

Learn about the variables and functions that you can use in formula expressions in AWS IoT SiteWise.

- [Use variables](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-variables.html): Learn about AWS IoT SiteWise variables, including how to reference properties in variable values.
- [Use literals](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-literals.html): Learn more about AWS IoT SiteWise literals in formula expressions.
- [Use operators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-operators.html): Learn about AWS IoT SiteWise operators in formula expressions.
- [Use constants](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-constants.html): Learn about using AWS IoT SiteWise constants in formula expressions.

### [Use functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-functions.html)

Learn about AWS IoT SiteWise functions in formula expressions.

- [Use common functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-common-functions.html): Discover common functions used in AWS IoT SiteWise expressions.
- [Use comparison functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-comparison-functions.html): Learn about AWS IoT SiteWise comparison functions.
- [Use conditional functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-conditional-functions.html): Learn about AWS IoT SiteWise conditional functions.
- [Use string functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-string-functions.html): Learn more about AWS IoT SiteWise string functions.
- [Use aggregation functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-aggregation-functions.html): Learn about AWS IoT SiteWise aggregation functions.
- [Use temporal functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-temporal-functions.html): Learn more about AWS IoT SiteWise temporal functions.
- [Use date and time functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-date-and-time-functions.html): Learn about AWS IoT SiteWise date and time functions.
- [Formula expression tutorials](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/expression-tutorials.html): Learn about using strings in formulas and more in the AWS IoT SiteWise formula expression tutorials.
- [Create custom composite models (components)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html): Learn about using custom composite models in AWS IoT SiteWise to group properties together, or to reference component models.

### [Create assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html)

Learn about creating assets using your asset models in AWS IoT SiteWise.

- [Configure a new asset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-asset-next-steps.html): Explore next steps after creating an asset in AWS IoT SiteWise.
- [Search assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-search.html): Search for assets on AWS IoT SiteWise console.
- [Update attribute values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-attribute-values.html): Learn how to update an asset attribute value in AWS IoT SiteWise.
- [Associate and disassociate assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-associated-assets.html): Learn how to associate and disassociate child assets to an asset in AWS IoT SiteWise.

### [Update assets and models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html)

Learn how to update assets, asset models, component models, and interfaces in AWS IoT SiteWise.

- [Update assets in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets.html): Update assets in AWS IoT SiteWise.
- [Update asset models, component models, and interfaces](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-asset-models.html): Learn how to update asset models, component models, and interfaces in AWS IoT SiteWise.
- [Update custom composite models (components)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-custom-composite-models.html): Learn how to update custom custom composite models, or components in the console, in AWS IoT SiteWise.
- [Optimistic locking for asset model writes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html): Learn how to do a optimistic locking for asset model writes.

### [Delete assets and models in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html)

Learn how to delete assets, asset models, component models, and interfaces in AWS IoT SiteWise in the console or with the AWS CLI.

- [Delete assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets.html): Learn how to delete assets using the console or API.
- [Delete models and interfaces](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-asset-models.html): Learn how to delete asset models, component models, and interfaces using the console or command line interface.

### [Bulk operations with assets and models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/bulk-operations-assets-and-models.html)

Learn how to perform bulk operations on AWS IoT SiteWise assets and asset models.

- [Bulk operation prerequisites](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/bulk-operations-prereqs.html): Learn about bulk operation prerequisites, including IAM permissions for exchanging resources between AWS services and your local machine.
- [Run a bulk import job](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/running-bulk-operations-import.html): Learn how to run a bulk import operation that moves metadata into an AWS IoT SiteWise workspace.
- [Run a bulk export job](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/running-bulk-operations-export.html): Learn the procedure for running a bulk export operation.

### [Jobs progress tracking and error handling](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/jobs-progress-error-handling.html)

Learn about jobs progress tracking and error handling.

- [Jobs progress tracking](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/review-job-progress.html): Review job progress in AWS IoT SiteWise.
- [Inspect errors](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/inspect-errors.html): Track and inspect errors details for AWS IoT SiteWise using the console or AWS CLI.
- [Import metadata examples](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/bulk-operations-import-metadata-example.html): Create metadata files to import asset models and assets with a single bulk import operation.
- [Export metadata examples](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/bulk-operations-export-filter-examples.html): Learn about using export filters to determine which resources to export.
- [Metadata transfer job schema](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/bulk-operations-schema.html): Learn about the AWS IoT SiteWise metadata transfer job schema.


## [Monitor data with alarms](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/industrial-alarms.html)

### [Define alarms on asset models](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-alarms.html)

Define alarms on asset models to standardize which industrial data to monitor in AWS IoT SiteWise.

- [Requirements for alarm notifications](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/iot-events-alarm-notification-requirements.html): Learn about the requirements to set up alarm notifications in AWS IoT SiteWise.
- [Define AWS IoT Events alarms](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-iot-events-alarms.html): Define AWS IoT SiteWise alarms that use AWS IoT Events to detect alarm state in the AWS Cloud.
- [Define external alarms](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-external-alarms.html): Define AWS IoT SiteWise alarms that ingest state from external sources.

### [Configure alarms on assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-alarms.html)

Configure the thresholds and notification settings for each alarm in AWS IoT SiteWise.

- [Configure notification settings](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-alarm-notification-settings.html): Configure notification settings using the console or the command line interface.
- [Respond to alarms](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/respond-to-alarms.html): Enable, disable, acknowledge, and snooze your AWS IoT Events alarms in AWS IoT SiteWise.

### [Ingest an external alarm state](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-external-alarm-state.html)

Ingest the state of alarms that you evaluate outside of AWS IoT SiteWise.

- [Map external alarm state streams](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-alarm-data-streams.html): Map your alarm state data streams to the alarm state property to ingest external alarm state to AWS IoT SiteWise.
- [Ingest alarm state data](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-alarm-state-data.html): Ingest the state of external alarms to alarm properties in AWS IoT SiteWise.


## [AWS IoT SiteWise Assistant](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-get-started.html)

- [Configure the AWS IoT SiteWise Assistant](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-console-login.html): The AWS IoT SiteWise Assistant and its use in AWS IoT SiteWise console and login
- [Create a dataset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-console-create-dataset.html): Create a dataset for use with the AWS IoT SiteWise Assistant.
- [Edit a dataset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-console-edit-dataset.html): Edit a dataset for use with the AWS IoT SiteWise Assistant.
- [Delete a dataset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-console-delete-dataset.html): Delete a dataset for use with the AWS IoT SiteWise Assistant.
- [AWS IoT SiteWise Assistant questions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-questions-in-assistant.html): AWS IoT SiteWise Assistant questions to ask.


## [Monitor data with AWS IoT SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-data.html)

### [Get started with AWS IoT SiteWise Monitor (Classic)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-getting-started.html)

Create a portal and add users in AWS IoT SiteWise Monitor.

- [Create a portal](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-create-portal.html): Learn how to create a portal in AWS IoT SiteWise Monitor.
- [Configure your portal](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-configure-portal.html): Configure your AWS IoT SiteWise Monitor portal details and contact information.
- [Invite administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-invite-administrators.html): Invite administrators to manage your portal in AWS IoT SiteWise Monitor.
- [Add portal users](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-add-portal-users.html): Add users to your portal in AWS IoT SiteWise Monitor.
- [Create dashboards (CLI)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html): Create an AWS IoT SiteWise Monitor dashboard using the AWS Command Line Interface.
- [Turn on alarms for your portals](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-enable-alarms.html): Enable alarms in AWS IoT Events for AWS IoT SiteWise.
- [Enable your portal at the edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-enable-edge.html): Enable the SiteWise Monitor portal at the edge.

### [Administer your portals](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html)

Manage your AWS IoT SiteWise Monitor portals by adding users or updating administrators.

- [Change a portal's attributes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/portal-change-details.html): Learn how to change a portal name, description, support email, branding, and permissions in AWS IoT SiteWise Monitor.
- [Add or remove portal administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/portal-change-admins.html): Learn how to add or remove portal administrators in AWS IoT SiteWise Monitor.
- [Send email invitations to portal administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/send-email-invitations-to-portal.html): Send email invitations to portal administrators in AWS IoT SiteWise Monitor.
- [Add or remove portal users](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/portal-change-users.html): Learn how to add or remove portal users in AWS IoT SiteWise Monitor.
- [Delete a portal](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/portal-delete-portal.html): Learn how to delete a portal from AWS IoT SiteWise Monitor.

### [Get started with AWS IoT SiteWise Monitor (AI-aware)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-getting-started-ai.html)

Create a portal and add users in AWS IoT SiteWise Monitor.

- [Create a portal](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-create-ai-portal.html): Learn how to create an AI portal in AWS IoT SiteWise Monitor.
- [Configure your portal](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-configure-ai-portal.html): Configure your AWS IoT SiteWise Monitor portal details and contact information.

### [Administer your portals](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals-ai.html)

Manage your AWS IoT SiteWise Monitor portals by adding or updating administrators.

- [Edit portal attributes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/portal-change-details-ai.html): Learn how to change a portal name, description, support email, branding, and permissions in AWS IoT SiteWise Monitor.
- [Add or remove portal administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/portal-change-admins-ai.html): Learn how to add or remove portal administrators in AWS IoT SiteWise Monitor.
- [Send email invitations to portal administrators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/send-email-invitations-to-portal-ai.html): Send email invitations to portal administrators
- [Delete a portal](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/portal-delete-portal-ai.html): Learn how to delete a portal from AWS IoT SiteWise Monitor.
- [Create dashboards with AWS CLI](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html): Create a dashboard in AWS CLI
- [Portal login](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/portal-login.html): Create a off console dashboard login to use.
- [Create a project](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-project.html): Create an off console dashboard project.
- [Update a project](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edit-project.html): Edit an off console dashboard project.
- [Delete a project](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-project.html): Delete an off console dashboard project.
- [Create a dashboard](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboard.html): Create a dashboard in a project.
- [Update a dashboard](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-dashboard.html): Update a dashboard in a project.
- [Delete a dashboard](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-dashboard.html): Delete a dashboard in a project.

### [Configure dashboard](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-dashboard.html)

Configure IoT dashboard with the resource explorer

### [Resource explorer](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/resource-exp.html)

Configure your dashboard with the resource explorer

- [Modeled](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/resource-exp-modeled.html): Configure your dashboard with the resource explorer- modeled assets
- [Unmodeled](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/resource-exp-unmodeled.html): Configure your dashboard with the resource explorer- unmodeled assets
- [Dynamic assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/resource-exp-dynamic.html): Configure your dashboard with the resource explorer- dynamic assets
- [Widgets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/dashboard-widgets.html): Configure your dashboard by adding widgets
- [Configure widgets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/dashboard-widgets-conf.html): Configure your widgets in the dashboard
- [Use widgets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/dashboard-widgets-manip.html): Using your widgets in the dashboard

### [Alarms in widgets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/alarm-widgets.html)

Alarm in widgets in the dashboard

- [Alarms in different widgets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/alarm-in-different-widgets.html): Alarm in different widgets in the dashboard

### [AWS IoT SiteWise Assistant use in widgets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-widgets.html)

AWS IoT SiteWise Assistant in widgets

- [Use case - Alarm summaries](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-widgets-alarm.html): Use case - Alarm summaries
- [Use case - Situational summaries](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-widgets-situation.html): Use case - Situational summaries
- [Use case - Deep dive summaries](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-widgets-deepdive.html): Use case - Deep dive summaries
- [Sample questions to ask AWS IoT SiteWise Assistant](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-questions.html): Questions to ask the Assistant


## [Query data from AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html)

- [Query current asset values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/current-values.html): Learn how to query current asset property values in AWS IoT SiteWise.
- [Query historical asset property values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/historical-values.html): Learn how to query historical asset property values in AWS IoT SiteWise.
- [Query asset property aggregates](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/aggregates.html): Learn how to query asset property aggregates in AWS IoT SiteWise.

### [AWS IoT SiteWise query language](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql.html)

Learn how to use the query language in AWS IoT SiteWise.

### [Query language reference](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-reference.html)

Explore the AWS IoT SiteWise query language.

- [Query reference views](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-reference-views.html): Learn how to understand the views in AWS IoT SiteWise, such as process metadata and telemetry data.
- [Supported data types](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/supported-data-types.html): Learn about the data types that AWS IoT SiteWise query language supports.
- [Supported clauses](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/supported-clauses.html): Learn about the clauses that AWS IoT SiteWise query language supports.
- [Logical operators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-supported-logical.html): Learn about the logical operators that AWS IoT SiteWise supports.
- [Comparison operators](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-supported-comparision.html): Learn about the comparison operators that AWS IoT SiteWise supports.

### [SQL functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions.html)

Examples of SQL functions - Scalar and string

### [Scalar functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-scalar.html)

Examples of SQL functions - Scalar

- [Null data functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-null.html): Examples of null data functions
- [String functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-string.html): Examples of SQL functions - String
- [Math functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-math.html): Examples of SQL functions - Math
- [Date time functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-date.html): Examples of SQL functions - Date time functions
- [Type conversion functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-type-conv.html): Examples of SQL functions - Type conversion functions
- [Aggregate functions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-functions-aggregated.html): Examples of SQL functions - Aggregate
- [Example queries](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sql-examples.html): Get code examples of queries for metadata filtering and value filtering.
- [Query optimization](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-optimize.html): Learn how to optimize your query

### [ODBC](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-ODBC.html)

Learn how to explore your industrial data using the AWS IoT SiteWise ODBC driver

- [Connection string syntax](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-ODBC-connecting.html): The syntax for specifying connection-string options for the ODBC driver is as follows:
- [Connection string examples](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-ODBC-connecting-examples.html)
- [Troubleshooting](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-ODBC-connecting-troubleshooting.html)


## [Interact with other services](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html)

- [Understand asset properties in MQTT topics](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/mqtt-topics.html): Learn about the unique MQTT topic paths that AWS IoT SiteWise assigns each asset property.
- [Work with notifications](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/property-notifications.html): Learn how to work with asset property notifications in AWS IoT SiteWise.
- [Query notifications](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-notification-messages.html): Learn how to query asset property notification messages sent from AWS IoT SiteWise to AWS IoT Core.
- [Export data to Amazon S3](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/export-to-s3.html): Learn how to export incoming data from AWS IoT SiteWise to an Amazon S3 bucket in your account.
- [Integrate Grafana](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/grafana-integration.html): Visualize and monitor your AWS IoT SiteWise data in Grafana.
- [Integrate with AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/integrate-tm.html): Integrate AWS IoT SiteWise with AWS IoT TwinMaker.
- [Detect equipment anomalies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/anomaly-detection.html): Learn how to detect anomalies in your AWS IoT SiteWise industrial data for predictive maintenance with Amazon Lookout for Equipment.


## [Native anomaly detection](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sitewise-anomaly-detection.html)

- [Native anomaly detection features](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/sitewise-anomaly-detection-features.html): Discover the powerful capabilities of the AWS IoT SiteWise platform, enabling you to leverage predictive maintenance, seamless integration, and advanced anomaly detection with ease.
- [Prerequisites](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/anomaly-prerequisites.html): Learn how to detect native anomalies in sitewise - prerequisites
- [Enable anomaly detection on sensors of an asset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/anom-detection-sensors-asset.html): Learn how to Enable anomaly detection on sensors of an asset
- [Enable anomaly detection on sensors across assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/anom-detection-sensors-across-asset.html): Learn how to Enable anomaly detection on sensors across assets
- [Advanced training configurations](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/adv-training-configs.html): Learn how to enable Advanced training configurations
- [Advanced inference configurations](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/advanced-inference-configurations.html): Learn how to configure model inference schedules for AWS IoT SiteWise anomaly detection, including high-frequency, low-frequency, and flexible scheduling modes.
- [Review inference results](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/reviewing-inference-results.html): Learn how to retrieve and understand inference results from AWS IoT SiteWise anomaly detection models, including response fields and diagnostic information.
- [Trigger custom actions on anomalous behavior (AWS Management Console)](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/trigger-custom-actions-anomalous-behavior.html): Learn how to configure custom actions that respond to anomalous behavior using AWS IoT SiteWise MQTT notifications and AWS IoT Core rules.
- [Best practices](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ano-best-practices.html): Follow these best practices for training data duration, sampling configuration, and labeling to optimize your AWS IoT SiteWise anomaly detection models.


## [Manage data storage](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-data-storage.html)

- [Configure storage settings](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-storage.html): Configure storage settings forAWS IoT SiteWise data.
- [Troubleshoot storage settings](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/troubleshoot-storage-configuration.html): Troubleshoot and resolve issues with the AWS IoT SiteWise storage configuration.
- [File paths and schemas of data saved in the cold tier](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/file-path-and-schema.html): Explore file paths and schemas for AWS IoT SiteWise cold tier data.


## [Code examples](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/service_code_examples_basics.html)

The following code examples show how to use the basics of AWS IoT SiteWise with AWS SDKs.

- [Hello AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_Hello_section.html): Hello AWS IoT SiteWise
- [Learn the basics](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_Scenario_section.html): Learn the basics of AWS IoT SiteWise with an AWS SDK

### [Actions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/service_code_examples_actions.html)

The following code examples show how to use AWS IoT SiteWise with AWS SDKs.

- [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_BatchPutAssetPropertyValue_section.html): Use BatchPutAssetPropertyValue with an AWS SDK or CLI
- [CreateAsset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_CreateAsset_section.html): Use CreateAsset with an AWS SDK or CLI
- [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_CreateAssetModel_section.html): Use CreateAssetModel with an AWS SDK or CLI
- [CreateGateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_CreateGateway_section.html): Use CreateGateway with an AWS SDK or CLI
- [DeleteAsset](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_DeleteAsset_section.html): Use DeleteAsset with an AWS SDK or CLI
- [DeleteAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_DeleteAssetModel_section.html): Use DeleteAssetModel with an AWS SDK or CLI
- [DeleteGateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_DeleteGateway_section.html): Use DeleteGateway with an AWS SDK or CLI
- [DescribeAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_DescribeAssetModel_section.html): Use DescribeAssetModel with an AWS SDK or CLI
- [DescribeGateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_DescribeGateway_section.html): Use DescribeGateway with an AWS SDK or CLI
- [GetAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_GetAssetPropertyValue_section.html): Use GetAssetPropertyValue with an AWS SDK or CLI
- [ListAssetModelProperties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_ListAssetModelProperties_section.html): Use ListAssetModelProperties with an AWS SDK
- [ListAssetModels](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/example_iotsitewise_ListAssetModels_section.html): Use ListAssetModels with an AWS SDK or CLI


## [Security](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-protection.html)

Learn how the AWS shared responsibility model applies to data protection in AWS IoT SiteWise.

- [Internetwork traffic privacy](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/internetwork-traffic-privacy.html): Learn how the AWS shared responsibility model applies to internetwork traffic privacy in AWS IoT SiteWise.
- [AWS IoT SiteWise Assistant Business Service improvement](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-bsp.html): AWS IoT SiteWise Assistant Business Service improvement in writing to show that we dont store information

### [Data encryption](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-encryption.html)

Learn how the AWS shared responsibility model applies to data encryption in AWS IoT SiteWise.

- [Encryption at rest](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/encryption-at-rest.html): Learn how the AWS shared responsibility model applies to encryption at rest in AWS IoT SiteWise.

### [Encryption in transit](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/encryption-in-transit.html)

Learn how the AWS shared responsibility model applies to encryption in transit in AWS IoT SiteWise.

- [Data in transit over the internet](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/internet-encryption-in-transit.html): Learn about data encryption in transit for AWS IoT SiteWise.
- [Data in transit over the local network](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/local-encryption-in-transit.html): Learn about AWS IoT SiteWise data in transit over the local network.
- [Data in transit between components](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-encryption-in-transit.html): Learn about AWS IoT SiteWise data in transit between local components on SiteWise Edge gateways.
- [Key management](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html): Learn how the AWS shared responsibility model applies to key management in AWS IoT SiteWise.

### [Identity and access management](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security-iam.html)

Authenticate requests and manage access your AWS IoT SiteWise resources.

- [Audience](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_audience.html): Learn about the audience for AWS IoT SiteWise security.
- [Authenticate with identities](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_authentication.html): Authenticate with identities in AWS IoT SiteWise.

### [How AWS IoT SiteWise works with IAM](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html)

Use IAM policies and roles to manage access to your AWS IoT SiteWise resources.

- [AWS IoT SiteWise IAM roles](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam-roles.html): Learn about IAM roles in AWS IoT SiteWise security.
- [Authorization based on tags](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam-tags.html): Learn about authorization based on AWS IoT SiteWise tags.
- [Identity-based policies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam-id-based-policies.html): Learn about AWS IoT SiteWise identity-based policies.
- [Identity-based policy examples](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_id-based-policy-examples.html): Use example IAM policy documents to manage access to your resources in AWS IoT SiteWise.
- [Manage access using policies in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_access-manage.html): Learn how to manage access to AWS IoT SiteWise using policies.
- [Managed policies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS IoT SiteWise and also recent changes to those policies.

### [Service-linked roles](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/using-service-linked-roles.html)

Use service-linked roles to give AWS IoT SiteWise access to resources in your AWS account.

- [Service-linked role permissions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/service-linked-role-permissions.html): Learn how to use service-linked role permissions in AWS IoT SiteWise
- [Create a service-linked role](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-service-linked-role.html): Learn how to create a service-linked role for AWS IoT SiteWise.
- [Update a service-linked role](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edit-service-linked-role.html): Learn how to update a service-linked role for AWS IoT SiteWise.
- [Delete a service-linked role](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-service-linked-role.html): Learn how to delete a service-linked role in AWS IoT SiteWise
- [Use service roles for SiteWise Monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html): Use service roles to give federated AWS IoT SiteWise Monitor portal users access to AWS IoT SiteWise resources in your AWS account.
- [Set up permissions for alarms](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/alarms-iam-permissions.html): You must give AWS IoT SiteWise and AWS IoT Events permission to share alarm data between the two services.
- [Cross-service confused deputy prevention in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/cross-service-confused-deputy-prevention.html): Protect your data from confused deputy issues across services.
- [Troubleshoot identity and access](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_troubleshoot.html): Identify and fix common IAM issues when you manage access to AWS IoT SiteWise.
- [Compliance validation](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS IoT SiteWise features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/infrastructure-security.html): Learn how AWS IoT SiteWise isolates service traffic.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/vulnerability-analysis-and-management.html): The AWS shared responsibility model and vulnerability analysis and management in AWS IoT SiteWise.

### [VPC endpoints](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/vpc-interface-endpoints.html)

Use an interface VPC endpoint to create a private connection between your virtual private cloud, or VPC, and AWS IoT SiteWise.

- [Supported API operations](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/vpc-endpoint-considerations.html): Learn about supported API operations for VPC endpoints in AWS IoT SiteWise
- [Create an interface VPC endpoint](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/vpc-endpoint-create.html): Learn how to create AWS IoT SiteWise VPC endpoints.
- [Access AWS IoT SiteWise through an interface VPC endpoint](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/vpc-endpoint-access.html): Learn how to access AWS IoT SiteWise through an interface VPC endpoint.
- [Create a VPC endpoint policy](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/vpc-endpoint-policy.html): Learn how to create an AWS IoT SiteWise VPC endpoint policy.
- [Security best practices](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security-best-practices.html): Follow security best practices in AWS IoT SiteWise.


## [Log and monitor](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/logging-and-monitoring.html)

- [Monitor service logs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-cloudwatch-logs.html): Learn about monitoring AWS IoT SiteWise with Amazon CloudWatch Logs.

### [Monitor SiteWise Edge gateway logs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-gateway-logs.html)

Learn about monitoring SiteWise Edge gateways with logs stored in Amazon CloudWatch Logs or the local file system.

- [Use Amazon CloudWatch Logs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-cloudwatch-logs.html): Learn how to configure your SiteWise Edge gateway to send logs to CloudWatch Logs.
- [Use service logs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-local-logs.html): Access and analyze SiteWise Edge service log files.
- [Monitor with Amazon CloudWatch metrics](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-cloudwatch-metrics.html): Learn about monitoring AWS IoT SiteWise with Amazon CloudWatch Metrics.
- [Log API calls with AWS CloudTrail](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/logging-using-cloudtrail.html): Log AWS IoT SiteWise API calls with AWS CloudTrail.


## [Tag your resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html)

- [Use tags in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-basics.html): Use tags to categorize your AWS IoT SiteWise resources.
- [Use tags with IAM policies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tags-iam.html): Use resource tags in your IAM policies with AWS IoT SiteWise.


## [Troubleshooting](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/troubleshooting.html)

- [Troubleshooting a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/troubleshooting-gateway.html): Troubleshoot common issues with your SiteWise Edge gateway.
- [Troubleshoot a portal](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/troubleshooting-portal.html): Troubleshoot common issues with your AWS IoT SiteWise portals.
- [Troubleshoot an AWS IoT SiteWise rule action](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/troubleshoot-rule.html): Troubleshoot your AWS IoT rule and AWS IoT SiteWise rule action.
- [Troubleshoot bulk import and export](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/troubleshooting-bulk.html): Troubleshoot common issues for bulk import and export.
