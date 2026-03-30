# Source: https://docs.anyscale.com/secrets/aws.md

# Source: https://docs.anyscale.com/iam/aws.md

# Source: https://docs.anyscale.com/configuration/compute/aws.md

# Compute configurations for AWS

[View Markdown](/configuration/compute/aws.md)

# Compute configurations for AWS

This page lists common cloud-specific compute configurations for Anyscale clouds deployed on AWS. You specify these options using the **Instance config** field in the Anyscale console at the node or cluster level.

important

When you configure any settings with the **Instance config** field for a worker group, this takes precedence and ignores all settings in the **Instance config** field at the cluster level.

For a general overview of compute configs, see [Compute configuration on Anyscale](/configuration/compute.md).

For configuration settings applicable to all Anyscale clouds, see [Advanced settings for compute configs on Anyscale](/configuration/compute/advanced.md).

For a complete reference on what might be configurable, see the [AWS docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_instances.html#) and contact Anyscale support.

Anyscale doesn't support setting the following fields:

```
ClientToken
DryRun
ImageId
InstanceType
Ipv6Addresses
LaunchTemplate
MaxCount
MinCount
PrivateIpAddress
SecurityGroups
UserData
```

## Manage capacity reservations[​](#capacity-reservations "Direct link to Manage capacity reservations")

Anyscale supports leveraging capacity reservations for worker nodes, which can be especially useful for instance types with limited capacity such as GPUs.

note

You can use machine pools to share capacity reservations across multiple workloads. See [Share compute resources with Anyscale machine pools](/machine-pools.md).

The following example demonstrates configuring a worker node to use virtual machines from an [AWS EC2 On-Demand Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html).

* Anyscale console
* CLI

Configure a capacity reservation in the Anyscale console by adding the following settings to the **Instance config** field for a worker node in your compute config:

```
{
  "CapacityReservationSpecification": {
    "CapacityReservationTarget": {
      "CapacityReservationId": "RESERVATION_ID"
    }
  }
}
```

Use the following syntax to configure a capacity reservation in a compute config YAML for the Anyscale CLI. See [Compute Config API Reference](/reference/compute-config-api.md).

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_ACCELERATED
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
    advanced_instance_config:
      CapacityReservationSpecification:
        CapacityReservationTarget:
          CapacityReservationId: RESERVATION_ID
```

To configure a capacity reservation for an [AWS Capacity Block for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html), you must add an additional configuration, as in the following example:

* Anyscale console
* CLI

Add the following settings to the **Instance config** field for a worker node in your compute config:

```
{
  "InstanceMarketOptions": {
    "MarketType": "capacity-block"
  },
  "CapacityReservationSpecification": {
    "CapacityReservationTarget": {
      "CapacityReservationId": "RESERVATION_ID"
    }
  }
}
```

Use the following syntax in a compute config YAML for the Anyscale CLI. See [Compute Config API Reference](/reference/compute-config-api.md).

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_ACCELERATED
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
    advanced_instance_config:
      InstanceMarketOptions:
        MarketType: capacity-block
      CapacityReservationSpecification:
        CapacityReservationTarget:
          CapacityReservationId: RESERVATION_ID
```

## Change the default disk size[​](#disk-size "Direct link to Change the default disk size")

The default disk size for all nodes in an Anyscale cluster is 150 GB. You can change the default disk size for the entire cluster or an individual worker node type.

To modify the default disk size from the console UI, use the **Advanced configuration** section for the Worker node or the **Advanced settings** section for the entire cluster. This example increases the default to 500 GB.

```
{
  "BlockDeviceMappings": [
    {
      "Ebs": {
        "VolumeSize": 500,
        "VolumeType": "gp3",
        "DeleteOnTermination": true
      },
      "DeviceName": "/dev/sda1"
    }
  ]
}
```

The following is an example YAML that modifies the disk for all nodes in the Anyscale cluster:

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_ACCELERATED
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
advanced_instance_config:
  BlockDeviceMappings:
    - Ebs:
      - VolumeSize: 500
        VolumeType: gp3
        DeleteOnTermination: true
      DeviceName: "/dev/sda1"
```

## NVMe configuration[​](#nvme "Direct link to NVMe configuration")

Anyscale supports Non-Volatile Memory Express (NVMe) interface to access SSD storage volumes, which provides additional temporary storage to the instances. This enables higher performance, lower latency, scalability, and support for versatile use cases across a variety of workloads. Anyscale exposes `/mnt/local_storage` as the mount path in the Ray container by default. For instance types that don't have NVMe, `/mnt/local_storage` just falls back to the root disk.

You can choose EC2 instance types that have NVMe. See [AWS instance store documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-volumes.html) for more details. Anyscale then automatically detects these devices, formats them, and mounts them when the Ray Container starts.

Anyscale configures EC2 instance types that have multiple NVMe devices with a software RAID ([RAID 0](https://linux.die.net/man/8/mdadm)), which maximizes disk performance.

<!-- -->

![EC2 NVMe Example](/assets/images/NVMe-ec2-d60e283bcbfb031271f6dfb5f1cc298b.png)

<!-- -->

## Subnets, security groups, and instance IAM role[​](#iam "Direct link to Subnets, security groups, and instance IAM role")

Specify the following configurations for the entire cluster (don't specify them for individual node groups unless you have to):

* Security groups and subnets:

  * Any security groups registered with the cloud.
  * Any subset of the security groups registered with the cloud.

* Instance IAM role:

  * Any IAM role for the cluster to run with. It must have an instance profile with the same name as the role.

To modify them from the console UI, use the **Advanced settings** section for the entire cluster.

```
{
  "IamInstanceProfile": {"Arn": "arn:aws:iam::<>:role/<>"},
  "SecurityGroupIds": ["security-group-id"],
  "SubnetId": "subnet-id",
}
```

This following sample YAML modifies the security groups, subnets, and instance IAM role for all nodes in the Anyscale cluster:

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_ACCELERATED
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
advanced_instance_config:
  IamInstanceProfile:
    Arn: "arn:aws:iam::<>:role/<>"
  SecurityGroupIds:
    - "security-group-id"
  SubnetId: "subnet-id"
```

## Configure Elastic Fabric Adapter (EFA) support[​](#efa "Direct link to Configure Elastic Fabric Adapter (EFA) support")

You can configure your Anyscale cluster to use Elastic Fabric Adapter (EFA) to accelerate network communication between nodes in your cluster.

### EFA requirements[​](#efa-requirements "Direct link to EFA requirements")

EFA support has the following requirements:

* You configure inbound and outbound communication between EFA and the security group used by Anyscale.

* You must set the environment variable `FI_PROVIDER=efa`.

* You must use an image that contains the following libraries:

  <!-- -->

  * EFA libraries
  * Libfabric libraries
  * NCCL
  * AWS OFI NCCL

* If using machine pools, you must configure EFA at the instance level. Cluster-level EFA configuration isn't supported for machine pools.

note

Anyscale slim base images don't include the necessary libraries by default.

### Cluster-level EFA configuration[​](#cluster-level-efa-configuration "Direct link to Cluster-level EFA configuration")

Anyscale recommends configuring EFA at the cluster level to simplify setup.

note

The console might prompt you to change your configuration if you enable EFA with the incorrect settings for zones.

Make sure you select a single zone and don't enable cross-zone scaling.

To configure EFA for your cluster, complete the following steps:

1. In your compute config, click **Advanced settings**.
2. Select a single zone in the **Allowed zones** field.
3. Click **Advanced features**.
4. To add EFA to your cluster and use the default values, add the `efa_config` property with an empty object, as in the following example:

```
{
    "efa_config": {}
}
```

You can optionally specify the following parameters for `efa_config` using JSON syntax:

| Parameter           | Description                                                                                                                                                                | Default                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `device_count`      | (Optional) The number of EFA interfaces to use per supported instance.<br /><br />If `0`, disables EFA.                                                                    | The maximum supported number of EFA interfaces for each supported node type. |
| `placement_group`   | (Optional) The name of the placement group for the EFA interfaces. For recommendations, see [AWS docs](https://docs.aws.amazon.com/parallelcluster/latest/ug/efa-v3.html). | None.                                                                        |
| `security_group_id` | (Optional) The security group used by EFA.                                                                                                                                 | The security group configured for the selected zone.                         |

### Instance-level EFA setup[​](#instance-level-efa-setup "Direct link to Instance-level EFA setup")

You can optionally configure EFA at the instance level. This provides you with more flexibility to customize your configuration but can be prone to errors.

note

Configuring EFA at the instance level for any worker group overrides cluster-level configuration to all nodes.

To configure EFA for your head node or worker nodes, complete the following steps:

1. In your compute config, click the name of the node.
2. Click **Advanced config**.
3. In the **Instance config** tab, add the `NetworkInterfaces` option using JSON syntax, as in the following example:

```
{
    "NetworkInterfaces": [
      {
          "Groups": [
              "sg-1234" # your security group id
          ],
          "SubnetId": "subnet-1234",
          "DeviceIndex": 0,
          "InterfaceType": "efa",
          "NetworkCardIndex": 0
      },
      {
          "Groups": [
              "sg-1234"
          ],
          "SubnetId": "subnet-1234",
          "DeviceIndex": 1,
          "InterfaceType": "efa",
          "NetworkCardIndex": 1
      },
      {
          "Groups": [
              "sg-1234"
          ],
          "SubnetId": "subnet-1234",
          "DeviceIndex": 1,
          "InterfaceType": "efa",
          "NetworkCardIndex": 2
      },
      {
          "Groups": [
              "sg-1234"
          ],
          "SubnetId": "subnet-1234",
          "DeviceIndex": 1,
          "InterfaceType": "efa",
          "NetworkCardIndex": 3
      }
    ],
    "Placement": { "GroupName": "my-placement-group" } # optional but recommended
}
```

note

You must specify the security group and subnet ID when configuring EFA at the instance level.

You must specify the correct `DeviceIndex` and `NetworkCardIndex` for each interface.
