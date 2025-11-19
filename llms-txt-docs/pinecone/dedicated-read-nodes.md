# Source: https://docs.pinecone.io/guides/index-data/dedicated-read-nodes.md

# Dedicated read nodes

> Reserve dedicated storage and compute resources for predictable query performance.

<Note>
  This feature is in [early access](/release-notes/feature-availability) and not yet available to all users. To request access, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>

Dedicated read nodes is a new feature that lets you reserve dedicated storage and compute resources for an index, ensuring predictable performance and cost efficiency for queries. It is ideal for workloads with **millions to billions of records** and **moderate to high query rates**.

## Key concepts

When you create an index with dedicated read nodes, Pinecone allocates dedicated storage and compute resources based on your choice of node type, number of shards, and number of replicas.

* **Dedicated storage** ensures that index data is always cached in memory and on disk for warm, low-latency queries. In contrast, for on-demand indexes, [caching is best-effort](/guides/get-started/database-architecture#query-executors); new and infrequently-accessed data may need to be fetched from object storage, resulting in cold, higher-latency queries.

* **Dedicated compute** ensures that an index always has the capacity to handle high query rates. In contrast, on-demand indexes share compute resources and are subject to [rate limits](/reference/api/database-limits#rate-limits) and throttling.

<Note>
  Dedicated read nodes affects only read performance. Write performance is the same as for on-demand indexes.
</Note>

### Node types

There are two node types: `b1` and `t1`. Both are suitable for large-scale and demanding workloads, but `t1` nodes provide increased processing power and memory. Additionally, `t1` nodes cache more data in memory, enabling lower query latency.

### Shards

Shards determine the storage capacity of an index.

Each shard provides 250 GB of storage, making it straightforward to calculate the number of shards necessary for your index size, including room for growth. For example:

| Index size | Shards | Capacity |
| :--------- | :----- | :------- |
| 100 GB     | 1      | 250 GB   |
| 500 GB     | 3      | 750 GB   |
| 1 TB       | 5      | 1.25 TB  |
| 1.6 TB     | 7      | 1.75 TB  |

When [index fullness](#index-fullness) reaches 80%, consider [adding shards](#add-or-remove-shards), especially if you expect continued growth. Adding shards accomplishes the following things:

* Relieves storage (disk) fullness. Data is spread across shards, so adding shards reduces the amount of data on each one.
* Relieves memory fullness. With less data stored on each shard, there's also less data to cache in memory.

<Warning>
  You are responsible for allocating enough shards for your index size. If your index exceeds its storage capacity, write operations (upsert, update, delete) are rejected.
</Warning>

### Replicas

Replicas multiply the compute resources and data of an index, allowing higher query throughput and availability.

* **Query throughput**: Each replica duplicates the compute resources available to the index, allowing increased parallel processing and higher queries per second.

  * In general, throughput scales linearly with the number of replicas, but performance varies based on the shape of the workload and the complexity of [metadata filters](/guides/search/filter-by-metadata).

  * To determine the right number of replicas, test your query patterns or [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).

* **High availability**: Replicas ensure your index remains available even if an availability zone experiences an outage.

  * When you add a replica, Pinecone places it in a different zone within the same region, up to a maximum of three zones. If you add more than three replicas, additional replicas are placed in zones that already have a replica. This multizone approach allows your index to continue serving queries even if one zone becomes unavailable.

  * To achieve high availability, allocate at least n+1 replicas, where n is the minimum number of replicas required to meet your throughput needs. This ensures that, even if a zone (and its replica) fails, your index still has enough capacity to handle your workload without interruption.

<Tip>
  As your query throughput and availability requirements change, you can [increase or decrease replicas](#add-or-remove-replicas). Adding or removing replicas can be done through the API and does not require downtime, but it can take up to 30 minutes.
</Tip>

### Index fullness

Dedicated read nodes store a search index in memory and record data on disk.

There are three measures of [index fullness](#check-index-fullness):

* `memory_fullness`: How much of the index's memory capacity is currently in use (0 to 1).
* `storage_fullness`: How much of the index's storage capacity is currently in use (0 to 1).
* `indexFullness`: The greater of `memory_fullness` and `storage_fullness`.

In most cases, `storage_fullness` is the limiting factor. However, memory can fill up first in the following scenarios:

* `b1` nodes, a large namespace (hundreds of millions of records), low-dimension vectors (128 or 256 dimensions), and minimal metadata.
* `t1` nodes, high-dimension vectors (1024 or 1536 dimensions), and lots of metadata.

When [index fullness](#index-fullness) reaches 80%, consider [adding shards](#add-or-remove-shards), especially if you expect continued growth. Adding shards accomplishes the following things:

* Relieves storage (disk) fullness. Data is spread across shards, so adding shards reduces the amount of data on each one.
* Relieves memory fullness. With less data stored on each shard, there's also less data to cache in memory.

<Warning>
  You're responsible for allocating enough shards to accommodate your index size. If your index exceeds its storage capacity, write operations (upsert, update, delete) are rejected.
</Warning>

## Using dedicated read nodes

<Note>
  This feature is in [early access](/release-notes/feature-availability) and is not yet available to all users. To request access, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).
</Note>

The following sections describe how to create and manage an index deployed on dedicated read nodes, using version `2025-10` of the Pinecone API.

### Calculate the size of your index

To decide how many [shards](#shards) to allocate for your index, calculate the total index size and then add some room for growth. Each shard provides 250 GB of storage.

To calculate the total size of an index, find the aggregate size of all its records. The size of an individual record is the sum of the following components:

* ID size (in bytes)

* Dense vector size (4 bytes \* dense dimensions)

* Sparse vector size (9 bytes \* number of non-zero sparse value)

  <Tip>
    To estimate the sparse vector component of your index size, multiply 9 bytes by the average number of non-zero values per vector.
  </Tip>

* Total metadata size (total size of all metadata fields, in bytes)

Allocate enough shards to accommodate the total size of your index, plus some room for growth. For more details, see [shards](#shards).

### Create an index

To create a dedicated index, call [create an index](https://docs.pinecone.io/reference/api/2025-10/control-plane/create_index).

In the `spec.serverless.read_capacity` object:

* Set `mode` to `Dedicated`.
* Set `dedicated.node_type` to either `b1` or `t1`, depending on the [node type](#node-types) you want to use.
* Set `dedicated.scaling` to `Manual` (currently, `Manual` is the only option, and it must be included in the request).
* Set `dedicated.manual.shards` to the number of [shards](#shards) required to accommodate at least the current size of your index, with a minimum of 1 shard. Each shard provides 250 GB of storage.
* Set `dedicated.manual.replicas` to the number of [replicas](#replicas) for the index, with a minimum of 0 replicas (an index with 0 replicas is [paused](#pause-a-dedicated-index)).

<Note>
  To determine the number of shards required by your index, see [calculate the size of your index](#calculate-the-size-of-your-index).
</Note>

Example request:

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" \
    -d '{
  		"name": "example-dedicated-index",
  		"dimension": 1536,
  		"metric": "cosine",
  		"deletion_protection": "enabled",
  		"tags": {
  			"tag0": "value0"
  		},
  		"vector_type": "dense",
  		"spec": {
  			"serverless": {
  				"cloud": "aws",
  				"region": "us-east-1",
  				"read_capacity": {
  					"mode": "Dedicated",
  					"dedicated": {
  						"node_type": "b1",
  						"scaling": "Manual",
  						"manual": {
  							"shards": 2,
  							"replicas": 1
  						}
  					}
  				}
  			}
  		}
  	}'
  ```
</CodeGroup>

Example response:

<CodeGroup>
  ```json curl theme={null}
  {
  	"name": "example-dedicated-index",
  	"vector_type": "dense",
  	"metric": "cosine",
  	"dimension": 1536,
  	"status": {
  		"ready": false,
  		"state": "Initializing"
  	},
  	"host": "example-dedicated-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
  	"spec": {
  		"serverless": {
  			"region": "us-east-1",
  			"cloud": "aws",
  			"read_capacity": {
  				"mode": "Dedicated",
  				"dedicated": {
  					"node_type": "b1",
  					"scaling": "Manual",
  					"manual": {
  						"shards": 2,
  						"replicas": 1
  					}
  				},
  				"status": {
  					"state": "Migrating",
  					"current_shards": null,
  					"current_replicas": null
  				}
  			}
  		}
  	},
  	"deletion_protection": "enabled",
  	"tags": {
  		"tag0": "value0"
  	}
  }
  ```
</CodeGroup>

### Add a hosted embedding model (optional)

If you'd like Pinecone to host the model that generates embeddings for your data, so that you use Pinecone's API to insert and search by text (rather than vectors generated by an external model), configure your index to use a [hosted embedding model](/guides/index-data/create-an-index#embedding-models). To do this, call [configure an index](/reference/api/2025-10/control-plane/configure_index), and specify the `embed` object in the request body.

Example request:

<Note>
  Remember:

  * Replace `chunk_test` with the name of the field in your data that contains the text to be embedded.
  * Be sure to use a model whose dimension requirements match the dimensions of your index.
</Note>

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_NAME="YOUR_INDEX_NAME"

  curl -s -X PATCH "https://api.pinecone.io/indexes/$INDEX_NAME" \
      -H "Content-Type: application/json" \
      -H "Api-Key: $PINECONE_API_KEY" \
      -H "X-Pinecone-API-Version: 2025-10" \
      -d '{
              "embed": {
                  "field_map": { "text": "chunk_test" },
                  "model": "llama-text-embed-v2",
                  "read_parameters": { "input_type": "query", "truncate": "NONE" },
                  "write_parameters": { "input_type": "passage" }
              }
          }' 
  ```
</CodeGroup>

Example response:

<CodeGroup>
  ```json curl theme={null}
  {
    "name": "example-dedicated-index-1024",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1024,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-dedicated-index-1024-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 1
            }
          },
          "status": {
            "state": "Migrating",
            "current_shards": null,
            "current_replicas": null
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag0": "value0"
    },
    "embed": {
      "model": "llama-text-embed-v2",
      "field_map": {
        "text": "dataField"
      },
      "dimension": 1024,
      "metric": "cosine",
      "write_parameters": {
        "dimension": 1024,
        "input_type": "passage",
        "truncate": "END"
      },
      "read_parameters": {
        "dimension": 1024,
        "input_type": "query",
        "truncate": "NONE"
      },
      "vector_type": "dense"
    }
  }
  ```
</CodeGroup>

<Note>
  It's also possible to specify a hosted embedding model when creating a dedicated read nodes index. To do this, call [create an index with integrated embedding](/reference/api/2025-10/control-plane/create_for_model). In the request body, use the `read_capacity` object to configure node type, shards, and replicas.
</Note>

### Check index fullness

To check [index fullness](#index-fullness), call [get index stats](/reference/api/2025-10/data-plane/describeindexstats).

Example request:

<CodeGroup>
  ```bash curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/describe_index_stats" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10"
  ```
</CodeGroup>

Example response:

<CodeGroup>
  ```json curl theme={null}
  {
    "namespaces": {
      "example-namespace": {
        "vectorCount": 10282
      }
    },
    "indexFullness": 0.2,
    "memory_fullness": 0.1,
    "storage_fullness": 0.2,
    "totalVectorCount": 7516163,
    "dimension": 1536,
    "metric": "cosine",
    "vectorType": "dense"
  }
  ```
</CodeGroup>

In the response, `indexFullness` describes how full the index is, on a scale of 0 to 1. It's set to the greater of `memory_fullness` and `storage_fullness`.

### Add or remove shards

To add or remove [shards](#shards), [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket). This cannot be done with the API.

### Add or remove replicas

<Note>
  You can add or remove replicas no more than once per hour, starting one hour after index creation. Each change can take up to 30 minutes to complete.
</Note>

Adding or removing [replicas](#replicas) can be done through the API and does not require downtime, but it can take up to 30 minutes. To do this, call [configure an index](/reference/api/2025-10/control-plane/configure_index). In the request body, set `spec.serverless.read_capacity.dedicated.manual.replicas` to the desired number of replicas.

Example request:

<CodeGroup>
  ```bash curl  theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl -X PATCH "https://api.pinecone.io/indexes/example-dedicated-index" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" \
    -d '{
          "spec": {
            "serverless": {
              "read_capacity": {
                "dedicated": {
                  "manual": {
                    "replicas": 2
                  }
                }
              }
            }
          }
        }'
  ```
</CodeGroup>

Example response:

<CodeGroup>
  ```json curl highlight={22,28} theme={null}
  {
    "name": "example-dedicated-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-dedicated-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 2 <-- desired state
            }
          },
          "status": {
            "state": "Scaling",
            "current_shards": 1,
            "current_replicas": 1 <-- current state
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag0": "value0"
    }
  }
  ```
</CodeGroup>

### Pause a dedicated index

To pause an index, [set the number of replicas](#add-or-remove-replicas) to 0. This change should take less than a minute to complete, after which the index blocks all writes and reads.

<Note>
  While an index is [paused](#pause-a-dedicated-index), you cannot write to it or read from it.
</Note>

### Change node types

To change the [type of node](#node-types) used for a dedicated index, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket). This cannot be done with the API.

### Migrate from on-demand to dedicated

<Note>
  You can change the <Tooltip tip="Dedicated or OnDemand">mode</Tooltip> of your index no more than once every 24 hours. The change can take up to 30 mins to complete.
</Note>

To change an on-demand index to dedicated, do the following:

1. Determine the [current size of your index](#calculate-the-size-of-your-index).

2. Call [configure an index](/reference/api/2025-10/control-plane/configure_index).

   In the request body, in the `spec.serverless.read_capacity` object, set the following fields:

   * Set `mode` to `Dedicated`.
   * Set `node_type` to the [node type](#node-types) you want to use (`b1` or `t1`).
   * Set `shards` to the number of [shards](#shards) required for your index. Each shard provides 250 GB of storage.
   * Set `replicas` to the number of [replicas](#replicas) required for your query throughput needs.

   For example, this example migrates an index named `index-to-migrate` to a dedicated index with `b1` nodes, 1 shard, and 1 replica:

   <CodeGroup>
     ```bash curl theme={null}
     curl -X PATCH "https://api.pinecone.io/indexes/index-to-migrate" \
       -H "Accept: application/json" \
       -H "Content-Type: application/json" \
       -H "Api-Key: $PINECONE_API_KEY" \
       -H "X-Pinecone-API-Version: 2025-10" \
       -d '{
             "spec": {
               "serverless": {
                 "read_capacity": {
                   "mode": "Dedicated",
                   "dedicated": {
                     "node_type": "b1",
                     "scaling": "Manual",
                     "manual": {
                       "shards": 1,
                       "replicas": 1
                     }
                   }
                 }
               }
             }
           }'
     ```
   </CodeGroup>

   Response:

   <CodeGroup>
     ```bash curl theme={null}
     {
       "name": "index-to-migrate",
       "vector_type": "dense",
       "metric": "cosine",
       "dimension": 1536,
       "status": {
         "ready": true,
         "state": "Ready"
       },
       "host": "index-to-migrate-bhnyigt.svc.aped-4627-b74a.pinecone.io",
       "spec": {
         "serverless": {
           "region": "us-east-1",
           "cloud": "aws",
           "read_capacity": {
             "mode": "Dedicated",
             "dedicated": {
               "node_type": "b1",
               "scaling": "Manual",
               "manual": {
                 "shards": 1,
                 "replicas": 1
               }
             },
             "status": {
               "state": "Migrating",
               "current_shards": null,
               "current_replicas": null
             }
           }
         }
       },
       "deletion_protection": "disabled",
       "tags": null
     }
     ```
   </CodeGroup>

3. [Monitor the status of the migration](#check-the-status-of-a-change).

   When the migration is complete, the value of [`spec.serverless.read_capacity.status.state`](/reference/api/2025-10/control-plane/describe_index#response-spec-serverless-read-capacity-status-state) is `Ready`.

   An `Error` state means that you didn't allocate enough shards for the size of your index. Migrate to dedicated again, using a sufficient number of shards.

### Migrate from dedicated to on-demand

To change a dedicated index to on-demand, contact [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket). This can't be done with the API.

### Check the status of a change

After changing a dedicated index, check the status of the change by calling [describe an index](/reference/api/2025-10/control-plane/describe_index):

Example request:

<CodeGroup>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl "https://api.pinecone.io/indexes/example-dedicated-index" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-API-Version: 2025-10" 
  ```
</CodeGroup>

Example response, for an index that is scaling from 1 to 2 replicas:

<CodeGroup>
  ```json curl theme={null}
  {
    "name": "example-dedicated-index",
    "vector_type": "dense",
    "metric": "cosine",
    "dimension": 1536,
    "status": {
      "ready": true,
      "state": "Ready"
    },
    "host": "example-dedicated-index-bhnyigt.svc.aped-4627-b74a.pinecone.io",
    "spec": {
      "serverless": {
        "region": "us-east-1",
        "cloud": "aws",
        "read_capacity": {
          "mode": "Dedicated",
          "dedicated": {
            "node_type": "b1",
            "scaling": "Manual",
            "manual": {
              "shards": 1,
              "replicas": 2
            }
          },
          "status": {
            "state": "Scaling",
            "current_shards": 1,
            "current_replicas": 1
          }
        }
      }
    },
    "deletion_protection": "enabled",
    "tags": {
      "tag0": "value0"
    }
  }
  ```
</CodeGroup>

The status of a change is communicated by the `spec.serverless.read_capacity.status.state` field. Possible values include:

* `Ready`: The dedicated index is ready to serve queries.
* `Scaling`: A change to the node type, number of shards, or number of replicas is in progress.
* `Migrating`: A change to the <Tooltip tip="Dedicated or OnDemand">mode</Tooltip> is in progress.
* `Error`: You did not allocate enough shards for the size of your index. Migrate to dedicated again, using a sufficient number of shards.

## Limits

### Read limits

On dedicated indexes, read operations (query, list, fetch) have no [rate limits](/reference/api/database-limits#rate-limits). However, if your query rate exceeds the compute capacity of your index, you may observe decreased query throughput. In such cases, consider [adding replicas](#add-or-remove-replicas) to increase the compute resources of the index.

### Write limits

* On dedicated indexes, write operations (upsert, update, delete) have the same [rate limits](/reference/api/database-limits#rate-limits) as on-demand indexes.
* Writes that would cause your index to exceed its storage capacity are rejected. In such cases, consider [adding shards](#add-or-remove-shards) to increase available storage. To determine how close to the limit you are,  [check index fullness](#check-index-fullness).

### Operational limits

| Metric                                                                                  | Limit          |
| :-------------------------------------------------------------------------------------- | :------------- |
| Min shards per index                                                                    | 1              |
| Max namespaces per index                                                                | 1              |
| [Node type](#node-types) or <Tooltip tip="Dedicated or OnDemand">mode</Tooltip> changes | 1 per 24 hours |
| Max shard or replica changes                                                            | 1 per hour     |

### Other limits

* To increase or decrease shards, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).
* To change node types, [contact support](https://app.pinecone.io/organizations/-/settings/support/ticket).
* Dedicated indexes do not support backups or bulk imports.
* `memory_fullness` is an approximation and doesn't yet account for metadata.

## Cost

The cost of an index that uses dedicated read nodes is calculated by this formula:

`(Dedicated read nodes costs)` + `(storage costs)` + `(write costs)`

* `(Dedicated read nodes costs)` are calculated as:

  ```
  (Node type monthly rate) * (number of shards) * (number of replicas)
  ```

  <Note>
    Node type rates vary based on [pricing plan](https://www.pinecone.io/pricing/) and cloud region. For exact rates, [contact Pinecone](https://www.pinecone.io/contact/).
  </Note>

* `(Storage costs)` are the [same as for on-demand indexes](/guides/manage-cost/understanding-cost#storage).

* `(Write costs)` are the [same as for on-demand indexes](/guides/manage-cost/understanding-cost#write-units).

Additionally, if you use a [hosted model](/guides/index-data/create-an-index#embedding-models) for search or reranking, there are additional costs for the model usage. See [inference pricing](https://www.pinecone.io/pricing/?plans=inference\&scrollTo=product-pricing-modal-section) for details.

### Example cost calculations

<AccordionGroup>
  <Accordion title="b1 nodes, 2 shards, 2 replicas - Standard plan">
    If the Standard plan rate for `b1` nodes is \$548.96/month, the cost of dedicated read nodes would be as follows:

    ```
    548.96 * 2 * 2 = $2,195.84/month, plus storage and write costs
    ```
  </Accordion>

  <Accordion title="t1 nodes, 2 shards, 2 replicas - Standard plan">
    If the Standard plan rate for `t1` nodes is \$1,758.53/month, the cost of dedicated read nodes would be as follows:

    ```
    1758.53 * 2 * 2 = $7,034.12/month, plus storage and write costs
    ```
  </Accordion>
</AccordionGroup>
