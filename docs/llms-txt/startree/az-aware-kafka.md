# Source: https://docs.startree.ai/corecapabilities/ingestdata/adv-concepts/realtime/az-aware-kafka.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Guide for setting up AZ aware Kafka ingestion

# AZ Aware Kafka ingestion in Pinot

## **Cross AZ data transfer cost**

In a StarTree Pinot cluster, Pinot servers utilize low-level Kafka consumers to retrieve data from Kafka brokers. When a Pinot consumer operates in a different Availability Zone than the Kafka broker hosting the required partition, each fetch request generates cross-AZ network traffic.

Cross-AZ traffic for Kafka consumers creates several challenges:

* Increased costs: Cross-AZ data transfer incurs additional charges
* Higher latency: Network requests across zones introduce additional delay
* Reduced reliability: Cross-zone communication increases potential failure points

Implementing AZ-aware consumption in StarTree pinot provides:

* Improved application performance through reduced latency
* Significant cost savings on data transfer fees
* Enhanced system reliability and fault tolerance

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/ingestdata/images/az_aware_2.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=cb44ebcd88680e3c97e444d48640b91b" alt="Az Aware 2 Pn" title="Az Aware 2 Pn" style={{ width:"81%" }} width="1436" height="1376" data-path="corecapabilities/ingestdata/images/az_aware_2.png" />

## **Solution Architecture**

The optimization strategy centers on implementing AZ-aware Kafka consumers using the Kafka RackAwareReplicaSelector. This approach ensures that Pinot servers preferentially consume from Kafka brokers within the same Availability Zone.

<img src="https://mintcdn.com/startree/qZwmUU4Se8wDV-BE/corecapabilities/ingestdata/images/az_aware_1.png?fit=max&auto=format&n=qZwmUU4Se8wDV-BE&q=85&s=8c1a82fc7350457d84ac35b8a0111620" alt="Az Aware 1 Pn" title="Az Aware 1 Pn" style={{ width:"78%" }} width="1436" height="1376" data-path="corecapabilities/ingestdata/images/az_aware_1.png" />

Here are the key steps in achieving this

* Step 1: Implement AZ-Aware Instance Assignment (Recommended but optional)

  Configure the instance assignment strategy to consider Availability Zone placement when distributing workloads across the cluster.
* Step 2: Configure AZ-Aware Table Settings

## **Implementation details**

### **Make instance assignment AZ-aware**

<Note>
  Note: This step is recommended but not necessary. Even if the Pinot servers are not perfectly provisioned in the same zones as Kafka cluster, we can still get partial benefits (best effort).
</Note>

First thing to do is setup pool-based instance assignment, wherein we tag servers in the same AZ with the same name (eg CLOUD\_AZ\_POOL\_REALTIME). For example, set servers in aps1-az1 with value 0, aps1-az2 with value 1, etc.

```
{
  "listFields": {
    "TAG_LIST": {
      "CLOUD_AZ_POOL_REALTIME"
    }
  },
  "mapFields": {
    "pool": {
      "CLOUD_AZ_POOL_REALTIME": 0
  },
}
```

For pool-based instance assignment, you need to configure CONSUMING with tag CLOUD\_AZ\_POOL\_REALTIME and poolBased in instanceAssignmentConfigMap:\
Example config:

```
"instanceAssignmentConfigMap": {
  "CONSUMING": {
    "tagPoolConfig": {
      "tag": "CLOUD_AZ_POOL_REALTIME",
      "poolBased": true
    },
    "replicaGroupPartitionConfig": {
      "replicaGroupBased": true,
      "numInstances": 0,
      "numReplicaGroups": 2,
      "numInstancesPerReplicaGroup": 0,
      "numPartitions": 0,
      "numInstancesPerPartition": 1
    },
    "partitionSelector": "INSTANCE_REPLICA_GROUP_PARTITION_SELECTOR"
  }
}
```

### **Make table configuration AZ-aware**

When we create realtime table, configure client.rack

```
"client.rack": "${CLOUD_AZ}"
```

This environment variable *CLOUD\_AZ* is automatically set on the servers and includes the coprresponding cloud zone information.

## **Summary**

This guide addresses the critical issue of cross-Availability Zone network traffic in StarTree Pinot clusters. This can be enabled by configuring pool based instance assignment and setting *client.rack* property of kafka consumer to the right value. Results demonstrate substantial optimization with same-AZ traffic increasing from 50% to 96-98% across all tested zones, resulting in significant cost savings and improved system performance.

Built with [Mintlify](https://mintlify.com).
