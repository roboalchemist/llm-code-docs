# Source: https://www.elastic.co/docs/manage-data/use-case-use-elasticsearch-to-manage-time-series-data

﻿---
title: Use case: Use Elasticsearch to manage time series data
description: Elasticsearch offers features to help you store, manage, and search time series data, such as logs and metrics. Once in Elasticsearch, you can analyze...
url: https://www.elastic.co/docs/manage-data/use-case-use-elasticsearch-to-manage-time-series-data
products:
  - Elasticsearch
---

# Use case: Use Elasticsearch to manage time series data
Elasticsearch offers features to help you store, manage, and search time series data, such as logs and metrics. Once in Elasticsearch, you can analyze and visualize your data using Kibana and other Elastic Stack features.

## Set up data tiers

Elasticsearch's [ILM](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management) feature uses [data tiers](https://www.elastic.co/docs/manage-data/lifecycle/data-tiers) to automatically move older data to nodes with less expensive hardware as it ages. This helps improve performance and reduce storage costs.
The hot and content tiers are required. The warm, cold, and frozen tiers are optional.
Use high-performance nodes in the hot and warm tiers for faster indexing and faster searches on your most recent data. Use slower, less expensive nodes in the cold and frozen tiers to reduce costs.
The content tier is not typically used for time series data. However, it’s required to create system indices and other indices that aren’t part of a data stream.
The steps for setting up data tiers vary based on your deployment type:
<applies-switch>
  <applies-item title="ess:" applies-to="Elastic Cloud Hosted: Generally available">
    1. Log in to the [Elastic Cloud Console](https://cloud.elastic.co/registration?page=docs&placement=docs-body).
    2. Add or select your deployment from the Elastic Cloud home page or the **Hosted deployments** page.
    3. From your deployment menu, select **Edit deployment**.
    4. To enable a data tier, click **Add capacity**.
    **Enable autoscaling**[Autoscaling](https://www.elastic.co/docs/deploy-manage/autoscaling) automatically adjusts your deployment’s capacity to meet your storage needs. To enable autoscaling, select **Autoscale this deployment** on the **Edit deployment** page. Autoscaling is only available for Elastic Cloud Hosted.
  </applies-item>

  <applies-item title="self:" applies-to="Self-managed Elastic deployments: Generally available">
    To assign a node to a data tier, add the respective [node role](https://www.elastic.co/docs/reference/elasticsearch/configuration-reference/node-settings#node-roles) to the node’s [`elasticsearch.yml`](https://www.elastic.co/docs/deploy-manage/stack-settings) file. Changing an existing node’s roles requires a [rolling restart](/docs/deploy-manage/maintenance/start-stop-services/full-cluster-restart-rolling-restart-procedures#restart-cluster-rolling).
    ```yaml
    # Content tier
    node.roles: [ data_content ]

    # Hot tier
    node.roles: [ data_hot ]

    # Warm tier
    node.roles: [ data_warm ]

    # Cold tier
    node.roles: [ data_cold ]

    # Frozen tier
    node.roles: [ data_frozen ]
    ```
    We recommend you use dedicated nodes in the frozen tier. If needed, you can assign other nodes to more than one tier.
    ```yaml
    node.roles: [ data_content, data_hot, data_warm ]
    ```
    Assign your nodes any other roles needed for your cluster. For example, a small cluster can have nodes with multiple roles.
    ```yaml
    node.roles: [ master, ingest, ml, data_hot, transform ]
    ```
  </applies-item>
</applies-switch>


## Register a snapshot repository

The cold and frozen tiers can use [searchable snapshots](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/searchable-snapshots) to reduce local storage costs.
To use searchable snapshots, you must register a supported snapshot repository. The steps for registering this repository vary based on your deployment type and storage provider:
<applies-switch>
  <applies-item title="ess:" applies-to="Elastic Cloud Hosted: Generally available">
    When you create a cluster, Elastic Cloud Hosted automatically registers a default [`found-snapshots`](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore) repository. This repository supports searchable snapshots.The `found-snapshots` repository is specific to your cluster. To use another cluster’s default repository, refer to the Cloud [Snapshot and restore](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore) documentation.You can also use any of the following custom repository types with searchable snapshots:
    - [Google Cloud Storage (GCS)](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/ec-gcs-snapshotting)
    - [Azure Blob Storage](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/ec-azure-snapshotting)
    - [Amazon Web Services (AWS)](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/ec-aws-custom-repository)
  </applies-item>

  <applies-item title="self:" applies-to="Self-managed Elastic deployments: Generally available">
    Use any of the following repository types with searchable snapshots:
    - [AWS S3](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/s3-repository)
    - [Google Cloud Storage](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/google-cloud-storage-repository)
    - [Azure Blob Storage](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/azure-repository)
    - [Hadoop Distributed File Store (HDFS)](https://www.elastic.co/docs/reference/elasticsearch/plugins/repository-hdfs)
    - [Shared filesystems](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/shared-file-system-repository) such as Network File System (NFS)
    - [Read-only HTTP and HTTPS repositories](https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/read-only-url-repository)
    You can also use alternative implementations of these repository types, for instance [MinIO](/docs/deploy-manage/tools/snapshot-and-restore/s3-repository#repository-s3-client), as long as they are fully compatible. Use the [Repository analysis](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-snapshot-repository-analyze) API to analyze your repository’s suitability for use with searchable snapshots.
  </applies-item>
</applies-switch>


## Create or edit an index lifecycle policy

A [data stream](https://www.elastic.co/docs/manage-data/data-store/data-streams) stores your data across multiple backing indices. ILM uses an [index lifecycle policy](https://www.elastic.co/docs/manage-data/lifecycle/index-lifecycle-management/index-lifecycle) to automatically move these indices through your data tiers.
If you use Fleet or Elastic Agent, edit one of Elasticsearch's built-in lifecycle policies. If you use a custom application, create your own policy. In either case, ensure your policy:
- Includes a phase for each data tier you’ve configured.
- Calculates the threshold, or `min_age`, for phase transition from rollover.
- Uses searchable snapshots in the cold and frozen phases, if wanted.
- Includes a delete phase, if needed.

<tab-set>
  <tab-item title="Fleet or Elastic Agent">
    Fleet and Elastic Agent use the following built-in lifecycle policies:
    - `logs`
    - `metrics`
    - `synthetics`
    You can customize these policies based on your performance, resilience, and retention requirements.To edit a policy in Kibana:
    1. Go to the **Index Lifecycle Policies** management page using the navigation menu or the [global search field](https://www.elastic.co/docs/explore-analyze/find-and-organize/find-apps-and-objects).
    2. Click the policy you’d like to edit.
    You can also use the [update lifecycle policy API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-put-lifecycle).
    ```json

    {
      "policy": {
        "phases": {
          "hot": {
            "actions": {
              "rollover": {
                "max_primary_shard_size": "50gb"
              }
            }
          },
          "warm": {
            "min_age": "30d",
            "actions": {
              "shrink": {
                "number_of_shards": 1
              },
              "forcemerge": {
                "max_num_segments": 1
              }
            }
          },
          "cold": {
            "min_age": "60d",
            "actions": {
              "searchable_snapshot": {
                "snapshot_repository": "found-snapshots"
              }
            }
          },
          "frozen": {
            "min_age": "90d",
            "actions": {
              "searchable_snapshot": {
                "snapshot_repository": "found-snapshots"
              }
            }
          },
          "delete": {
            "min_age": "735d",
            "actions": {
              "delete": {}
            }
          }
        }
      }
    }
    ```
  </tab-item>

  <tab-item title="Custom application">
    To create a policy in Kibana:
    1. Go to the **Index Lifecycle Policies** management page using the navigation menu or the [global search field](https://www.elastic.co/docs/explore-analyze/find-and-organize/find-apps-and-objects).
    2. Click **Create policy**.
    You can also use the [update lifecycle policy API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-ilm-put-lifecycle).
    ```json

    {
      "policy": {
        "phases": {
          "hot": {
            "actions": {
              "rollover": {
                "max_primary_shard_size": "50gb"
              }
            }
          },
          "warm": {
            "min_age": "30d",
            "actions": {
              "shrink": {
                "number_of_shards": 1
              },
              "forcemerge": {
                "max_num_segments": 1
              }
            }
          },
          "cold": {
            "min_age": "60d",
            "actions": {
              "searchable_snapshot": {
                "snapshot_repository": "found-snapshots"
              }
            }
          },
          "frozen": {
            "min_age": "90d",
            "actions": {
              "searchable_snapshot": {
                "snapshot_repository": "found-snapshots"
              }
            }
          },
          "delete": {
            "min_age": "735d",
            "actions": {
              "delete": {}
            }
          }
        }
      }
    }
    ```
  </tab-item>
</tab-set>


## Create component templates

<tip>
  If you use Fleet or Elastic Agent, skip to [Search and visualize your data](#search-visualize-your-data). Fleet and Elastic Agent use built-in templates to create data streams for you.
</tip>

If you use a custom application, you need to set up your own data stream. A data stream requires a matching index template. Usually, you compose this index template using one or more component templates. You typically use separate component templates for mappings and index settings. This lets you reuse the component templates in multiple index templates.
When creating your component templates, include:
- A [`date`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/date) or [`date_nanos`](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/date_nanos) mapping for the `@timestamp` field. If you don’t specify a mapping, Elasticsearch maps `@timestamp` as a `date` field with default options.
- Your lifecycle policy in the `index.lifecycle.name` index setting.

<tip>
  Use the [Elastic Common Schema (ECS)](https://www.elastic.co/docs/reference/ecs) when mapping your fields. ECS fields integrate with several Elastic Stack features by default.If you’re unsure how to map your fields, use [runtime fields](https://www.elastic.co/docs/manage-data/data-store/mapping/define-runtime-fields-in-search-request) to extract fields from [unstructured content](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/keyword#mapping-unstructured-content) at search time. For example, you can index a log message to a `wildcard` field and later extract IP addresses and other data from this field during a search.
</tip>

To create a component template in Kibana:
1. Go to the **Index Management** page using the navigation menu or the [global search field](https://www.elastic.co/docs/explore-analyze/find-and-organize/find-apps-and-objects).
2. In the **Index Templates** tab, click **Create component template**.

You can also use the [create component template API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-put-component-template).
```json
# Creates a component template for mappings

{
  "template": {
    "mappings": {
      "properties": {
        "@timestamp": {
          "type": "date",
          "format": "date_optional_time||epoch_millis"
        },
        "message": {
          "type": "wildcard"
        }
      }
    }
  },
  "_meta": {
    "description": "Mappings for @timestamp and message fields",
    "my-custom-meta-field": "More arbitrary metadata"
  }
}

# Creates a component template for index settings

{
  "template": {
    "settings": {
      "index.lifecycle.name": "my-lifecycle-policy"
    }
  },
  "_meta": {
    "description": "Settings for ILM",
    "my-custom-meta-field": "More arbitrary metadata"
  }
}
```


## Create an index template

Use your component templates to create an index template. Specify:
- One or more index patterns that match the data stream’s name. We recommend using our [data stream naming scheme](/docs/reference/fleet/data-streams#data-streams-naming-scheme).
- That the template is data stream enabled.
- Any component templates that contain your mappings and index settings.
- A priority higher than `200` to avoid collisions with built-in templates. Refer to [Avoid index pattern collisions](/docs/manage-data/data-store/templates#avoid-index-pattern-collisions).

To create an index template in Kibana:
1. Go to the **Index Management** page using the navigation menu or the [global search field](https://www.elastic.co/docs/explore-analyze/find-and-organize/find-apps-and-objects).
2. In the **Index Templates** tab, click **Create template**.

You can also use the [create index template API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-put-index-template). Include the `data_stream` object to enable data streams.
```json

{
  "index_patterns": ["my-data-stream*"],
  "data_stream": { },
  "composed_of": [ "my-mappings", "my-settings" ],
  "priority": 500,
  "_meta": {
    "description": "Template for my time series data",
    "my-custom-meta-field": "More arbitrary metadata"
  }
}
```


## Add data to a data stream

[Indexing requests](/docs/manage-data/data-store/data-streams/use-data-stream#add-documents-to-a-data-stream) add documents to a data stream. These requests must use an `op_type` of `create`. Documents must include a `@timestamp` field.
To automatically create your data stream, submit an indexing request that targets the stream’s name. This name must match one of your index template’s index patterns.
```json

{ "create":{ } }
{ "@timestamp": "2099-05-06T16:21:15.000Z", "message": "192.0.2.42 - - [06/May/2099:16:21:15 +0000] \"GET /images/bg.jpg HTTP/1.0\" 200 24736" }
{ "create":{ } }
{ "@timestamp": "2099-05-06T16:25:42.000Z", "message": "192.0.2.255 - - [06/May/2099:16:25:42 +0000] \"GET /favicon.ico HTTP/1.0\" 200 3638" }


{
  "@timestamp": "2099-05-06T16:21:15.000Z",
  "message": "192.0.2.42 - - [06/May/2099:16:21:15 +0000] \"GET /images/bg.jpg HTTP/1.0\" 200 24736"
}
```


## Search and visualize your data

To explore and search your data in Kibana, open the main menu and select **Discover**. Refer to Kibana's [Discover documentation](https://www.elastic.co/docs/explore-analyze/discover).
Use Kibana's **Dashboard** feature to visualize your data in a chart, table, map, and more. Refer to Kibana's [Dashboard documentation](https://www.elastic.co/docs/explore-analyze/dashboards).
You can also search and aggregate your data using the [search API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search). Use [runtime fields](https://www.elastic.co/docs/manage-data/data-store/mapping/define-runtime-fields-in-search-request) and [grok patterns](https://www.elastic.co/docs/explore-analyze/scripting/grok) to dynamically extract data from log messages and other unstructured content at search time.
```json

{
  "runtime_mappings": {
    "source.ip": {
      "type": "ip",
      "script": """
        String sourceip=grok('%{IPORHOST:sourceip} .*').extract(doc[ "message" ].value)?.sourceip;
        if (sourceip != null) emit(sourceip);
      """
    }
  },
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gte": "now-1d/d",
              "lt": "now/d"
            }
          }
        },
        {
          "range": {
            "source.ip": {
              "gte": "192.0.2.0",
              "lte": "192.0.2.255"
            }
          }
        }
      ]
    }
  },
  "fields": [
    "*"
  ],
  "_source": false,
  "sort": [
    {
      "@timestamp": "desc"
    },
    {
      "source.ip": "desc"
    }
  ]
}
```

Elasticsearch searches are synchronous by default. Searches across frozen data, long time ranges, or large datasets can take longer. Use the [async search API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-async-search-submit) to run searches in the background. For more search options, refer to [*The search API*](https://www.elastic.co/docs/solutions/search/querying-for-search).
```json

{
  "runtime_mappings": {
    "source.ip": {
      "type": "ip",
      "script": """
        String sourceip=grok('%{IPORHOST:sourceip} .*').extract(doc[ "message" ].value)?.sourceip;
        if (sourceip != null) emit(sourceip);
      """
    }
  },
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "@timestamp": {
              "gte": "now-2y/d",
              "lt": "now/d"
            }
          }
        },
        {
          "range": {
            "source.ip": {
              "gte": "192.0.2.0",
              "lte": "192.0.2.255"
            }
          }
        }
      ]
    }
  },
  "fields": [
    "*"
  ],
  "_source": false,
  "sort": [
    {
      "@timestamp": "desc"
    },
    {
      "source.ip": "desc"
    }
  ]
}
```