# Source: https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/llms.txt

# Timestream for InfluxDB API Reference

> Management APIs for Timestream InfluxDB.

- [Welcome](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_Operations.html)

- [CreateDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbCluster.html): Creates a new Timestream for InfluxDB cluster.
- [CreateDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbInstance.html): Creates a new Timestream for InfluxDB DB instance.
- [CreateDbParameterGroup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_CreateDbParameterGroup.html): Creates a new Timestream for InfluxDB DB parameter group to associate with DB instances.
- [DeleteDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DeleteDbCluster.html): Deletes a Timestream for InfluxDB cluster.
- [DeleteDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DeleteDbInstance.html): Deletes a Timestream for InfluxDB DB instance.
- [GetDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_GetDbCluster.html): Retrieves information about a Timestream for InfluxDB cluster.
- [GetDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_GetDbInstance.html): Returns a Timestream for InfluxDB DB instance.
- [GetDbParameterGroup](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_GetDbParameterGroup.html): Returns a Timestream for InfluxDB DB parameter group.
- [ListDbClusters](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbClusters.html): Returns a list of Timestream for InfluxDB DB clusters.
- [ListDbInstances](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbInstances.html): Returns a list of Timestream for InfluxDB DB instances.
- [ListDbInstancesForCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbInstancesForCluster.html): Returns a list of Timestream for InfluxDB clusters.
- [ListDbParameterGroups](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListDbParameterGroups.html): Returns a list of Timestream for InfluxDB DB parameter groups.
- [ListTagsForResource](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_ListTagsForResource.html): A list of tags applied to the resource.
- [RebootDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_RebootDbCluster.html): Reboots a Timestream for InfluxDB cluster.
- [RebootDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_RebootDbInstance.html): Reboots a Timestream for InfluxDB instance.
- [TagResource](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_TagResource.html): Tags are composed of a Key/Value pairs.
- [UntagResource](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_UntagResource.html): Removes the tag from the specified resource.
- [UpdateDbCluster](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_UpdateDbCluster.html): Updates a Timestream for InfluxDB cluster.
- [UpdateDbInstance](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_UpdateDbInstance.html): Updates a Timestream for InfluxDB DB instance.


## [Data Types](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_Types.html)

- [DbClusterSummary](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbClusterSummary.html): Describes a summary of a Timestream for InfluxDB cluster.
- [DbInstanceForClusterSummary](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbInstanceForClusterSummary.html): Contains a summary of a DB instance belonging to a DB cluster.
- [DbInstanceSummary](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbInstanceSummary.html): Contains a summary of a DB instance.
- [DbParameterGroupSummary](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_DbParameterGroupSummary.html): Contains a summary of a DB parameter group.
- [Duration](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_Duration.html): Duration for InfluxDB parameters in Timestream for InfluxDB.
- [InfluxDBv2Parameters](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_InfluxDBv2Parameters.html): All the customer-modifiable InfluxDB v2 parameters in Timestream for InfluxDB.
- [InfluxDBv3CoreParameters](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_InfluxDBv3CoreParameters.html): All the customer-modifiable InfluxDB v3 Core parameters in Timestream for InfluxDB.
- [InfluxDBv3EnterpriseParameters](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_InfluxDBv3EnterpriseParameters.html): All the customer-modifiable InfluxDB v3 Enterprise parameters in Timestream for InfluxDB.
- [LogDeliveryConfiguration](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_LogDeliveryConfiguration.html): Configuration for sending InfluxDB engine logs to send to specified S3 bucket.
- [Parameters](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_Parameters.html): The parameters that comprise the parameter group.
- [PercentOrAbsoluteLong](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_PercentOrAbsoluteLong.html): Percent or Absolute Long for InfluxDB parameters
- [S3Configuration](https://docs.aws.amazon.com/ts-influxdb/latest/ts-influxdb-api/API_S3Configuration.html): Configuration for S3 bucket log delivery.
