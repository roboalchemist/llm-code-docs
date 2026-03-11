# Source: https://docs.anyscale.com/configuration/compute/gcp.md

# Compute configuration options for Google Cloud

[View Markdown](/configuration/compute/gcp.md)

# Compute configuration options for Google Cloud

This page lists common cloud-specific compute configurations for Anyscale clouds deployed on Google cloud. You specify these options using the **Instance config** field in the Anyscale console at the node or cluster level.

important

When you configure any settings with the **Instance config** field for a worker group, this takes precedence and ignores all settings in the **Instance config** field at the cluster level.

For a general overview of compute configs, see [Compute configuration on Anyscale](/configuration/compute.md).

For configuration settings applicable to all Anyscale clouds, see [Advanced settings for compute configs on Anyscale](/configuration/compute/advanced.md).

For a complete reference on what might be configurable, see the [Google Cloud docs](https://cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert#request-body) and contact Anyscale support.

Anyscale doesn't support setting the following fields:

```
count
minCount
namePattern
instanceProperties
  machineType
  metadata
    items
      user-data
  disks
    initializeParams
      sourceImage
```

## Manage capacity reservations[​](#capacity-reservations "Direct link to Manage capacity reservations")

Securing certain instance types from cloud providers can sometimes be challenging due to high demand or limited availability. With Anyscale, you can leverage your cloud provider capacity reservations, ensuring the availability of required node types for your workloads. To configure capacity reservations for a specific worker node type, modify the advanced configuration through the console UI or by editing the compute config YAML file.

To add a reservation with the console UI, navigate to a worker node and expand the **Advanced config** section. Under the **Instance config** tab, input the following JSON, substituting in your specific reservation name:

```
{
  "instanceProperties": {
    "reservationAffinity": {
      "consumeReservationType": "SPECIFIC_RESERVATION",
      "key": "compute.googleapis.com/reservation-name",
      "values": ["RESERVATION_NAME"]
    }
  }
}
```

The following is a sample YAML file that you can use with the Anyscale CLI or SDK:

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_ACCELERATED
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
    advanced_instance_config:
      instanceProperties:
        reservationAffinity:
          consumeReservationType: SPECIFIC_RESERVATION
          key: compute.googleapis.com/reservation-name
          values: [RESERVATION_NAME]
```

For additional details on utilizing open reservations in Google Cloud, see the [Google Cloud documentation](https://cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation).

## Change the default disk size[​](#disk-size "Direct link to Change the default disk size")

The default disk size for all nodes in an Anyscale cluster is 150 GB. You can change the default disk size for the entire cluster or an individual worker node type.

To modify the default disk size from the console UI, use the **Advanced configuration** section for the Worker node or the **Advanced settings** section for the entire cluster. This example increases the default to 500 GB.

```
{
  "instance_properties": {
    "disks": [
      {
        "boot": true,
        "auto_delete": true,
        "initialize_params": {
          "disk_size_gb": 500
        }
      }
    ]
  }
}
```

The following sample YAML modifies the disk for all nodes in the Anyscale cluster:

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_ACCELERATED
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
advanced_instance_config:
  instanceProperties:
    disks:
      - boot: true
        auto_delete: true
        initialize_params:
          - disk_size_gb: 500
```

## NVMe configuration[​](#nvme "Direct link to NVMe configuration")

Anyscale supports Non-Volatile Memory Express (NVMe) interface to access SSD storage volumes, which provides additional temporary storage to the instances. This enables higher performance, lower latency, scalability, and support for versatile use cases across a variety of workloads. Anyscale exposes `/mnt/local_storage` as the mount path in the Ray container by default. For instance types that don't have NVMe, `/mnt/local_storage` just falls back to the root disk.

You need to manually specify the number of NVMe devices to attach to the instance. See [Google Cloud local SSD documentation](https://cloud.google.com/compute/docs/disks/add-local-ssd) for more details. Note that each local SSD has 375 GB. Specify the number of NVMe devices to attach in the **Advanced settings > Instance config** section of the compute config. Here is an example:

![GCE NVMe Example](/assets/images/NVMe-gce-33d2e75e490a96d05c1e66322c187c63.png)

```
{
  "instance_properties": {
    "disks": [
      {
        "boot": true,
        "type": "PERSISTENT",
        "initializeParams": {
          "diskSizeGb": 150
        }
      },
      {
        "type": "SCRATCH",
        "interface": "NVME",
        "autoDelete": true,
        "initializeParams": {
          "diskType": "local-ssd"
        }
      },
      {
        "type": "SCRATCH",
        "interface": "NVME",
        "autoDelete": true,
        "initializeParams": {
          "diskType": "local-ssd"
        }
      }
    ]
  }
}
```

## Subnets and service accounts[​](#iam "Direct link to Subnets and service accounts")

Specify the following configurations for the entire cluster (don't specify them for individual node groups unless you have to):

* Subnets:
  <!-- -->
  * Any subnet registered with the cloud.
* Service accounts:
  <!-- -->
  * Any service account for the cluster to run with. It must have permissions specified for a Ray cluster service account in the cloud deployment documentation.

To modify them from the console UI, use the **Advanced settings** section for the entire cluster.

```
{
  "instance_properties": {
    "service_accounts": [
      {
        "email": "service-account-to-use",
        "scopes": [
          "https://www.googleapis.com/auth/cloud-platform"
        ]
      }
    ],
    "network_interfaces": [
      {
        "subnetwork": "subnetUrl",
        "access_configs": [
          {
            "type": "ONE_TO_ONE_NAT"
          }
        ]
      }
    ]
  }
}
```

The following sample YAML modifies the service account and subnets for all nodes in the Anyscale cluster:

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_ACCELERATED
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
advanced_instance_config:
  instance_properties:
    service_accounts:
      - email: service-account-to-use
        scopes:
          - "https://www.googleapis.com/auth/cloud-platform"
    network_interfaces:
      - subnetwork: subnetUrl
        access_configs:
          - type: ONE_TO_ONE_NAT
```
