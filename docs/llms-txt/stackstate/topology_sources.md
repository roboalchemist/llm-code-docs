# Source: https://archivedocs.stackstate.com/5.1/configure/topology/topology_sources.md

# Topology sources

## Overview

Topology sources are used to get data from the Kafka bus, which receives the data from the StackState topology API. They can be configured from the StackState UI page **Settings** > **Topology Synchronization** > **Sts sources**. Each configured topology data source is listed here, together with its connection status and settings. You can also edit, delete and export topology data sources from this list.

## Add a new topology data source

To add a new topology data source, click **ADD STS DATA SOURCE** from the screen **Settings** > **Topology Synchronization** > **Sts sources** and enter the required configuration.

![ADD STS DATA SOURCE screen](https://2702698828-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Ft9xRpVRApnyVQrX3f8HH%2Fuploads%2Fgit-blob-c46c37271af0650e90fd260cbe6f92e8ca1f291c%2Fv51_add_sts_data_source.png?alt=media)

The screen has the following fields:

| Field                              | Description                                                                                                                                                                                                                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**                           | The name of the data source.                                                                                                                                                                                                                                                       |
| **Description**                    | Optional. A description of the data source.                                                                                                                                                                                                                                        |
| **Use StackState's default Kafka** | Select to use either the default Kafka bus on the StackState server or a separate Kafka instance.                                                                                                                                                                                  |
| **Kafka host(s)**                  | Required if StackState's default Kafka isn't used.                                                                                                                                                                                                                                 |
| **Instance type**                  | The integration type. Select from the dropdown list. This list is populated with the `type` passed in the `instance` field in the [source JSON data](https://archivedocs.stackstate.com/5.1/configure/send-topology-data#topology-json-format).                                    |
| **Topic**                          | The Kafka topic to retrieve data from. Select from the dropdown list. This list is populated based on the `type` and `url` passed in the `instance` field in the [source topology JSON](https://archivedocs.stackstate.com/5.1/configure/send-topology-data#topology-json-format). |
| **Maximum batch size**             | The maximum number of components from a JSON file that are processed in a single batch. Used for rate limiting.                                                                                                                                                                    |
| **Expire elements**                | When enabled, topology elements will be set to `expired` if they don't appear in this data source for a configured amount of time. Expired elements will be automatically removed.                                                                                                 |
| **Expire after (minutes)**         | When **Expire elements** is enabled, this is the timeout period after which elements should be expired.                                                                                                                                                                            |
| **Identifier**                     | Optional. A valid URN.                                                                                                                                                                                                                                                             |

{% hint style="info" %}
**Snapshot mode**

When topology data is sent in snapshot mode, it isn't necessary to expire elements. Each snapshot represents a complete landscape instance and elements missing from the snapshot will be automatically deleted.

See the [Topology JSON format description](https://archivedocs.stackstate.com/5.1/configure/send-topology-data#topology-json-format) for details.
{% endhint %}

## See also

* [Topoology synchronization](https://archivedocs.stackstate.com/5.1/configure/topology/send-topology-data)
* [Topology JSON format](https://archivedocs.stackstate.com/5.1/configure/send-topology-data#topology-json-format)
