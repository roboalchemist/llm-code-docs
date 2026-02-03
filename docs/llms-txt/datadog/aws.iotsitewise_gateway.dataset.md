# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotsitewise_gateway.dataset.md

---
title: IoT SiteWise Gateway
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT SiteWise Gateway
---

# IoT SiteWise Gateway

IoT SiteWise Gateway in AWS is a software appliance that runs on local hardware or edge devices to securely connect industrial equipment data to the AWS Cloud. It collects, processes, and transfers data from on-premises sources such as OPC-UA servers, historians, and other industrial systems into AWS IoT SiteWise for monitoring and analysis.

```
aws.iotsitewise_gateway
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ---------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| creation_date                | core | timestamp  | The date the gateway was created, in Unix epoch time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| gateway_capability_summaries | core | json       | A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use DescribeGatewayCapabilityConfiguration.                                                                                                                                                                                                                                                                        |
| gateway_id                   | core | string     | The ID of the gateway device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| gateway_name                 | core | string     | The name of the gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| gateway_platform             | core | json       | The gateway's platform configuration. You can only specify one platform type in a gateway. (Legacy only) For Greengrass V1 gateways, specify the greengrass parameter with a valid Greengrass group ARN. For Greengrass V2 gateways, specify the greengrassV2 parameter with a valid core device thing name. If creating a V3 gateway (gatewayVersion=3), you must also specify the coreDeviceOperatingSystem. For Siemens Industrial Edge gateways, specify the siemensIE parameter with a valid IoT Core thing name. |
| gateway_version              | core | string     | The version of the gateway. A value of 3 indicates an MQTT-enabled, V3 gateway, while 2 indicates a Classic streams, V2 gateway.                                                                                                                                                                                                                                                                                                                                                                                       |
| last_update_date             | core | timestamp  | The date the gateway was last updated, in Unix epoch time.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| tags                         | core | hstore_csv |
