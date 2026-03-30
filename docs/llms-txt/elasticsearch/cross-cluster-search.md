# Source: https://www.elastic.co/docs/explore-analyze/cross-cluster-search

﻿---
title: Cross-cluster search
description: Cross-cluster search lets you run a single search request against one or more remote clusters. For example, you can use a cross-cluster search to filter...
url: https://www.elastic.co/docs/explore-analyze/cross-cluster-search
products:
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Unavailable
  - Elastic Stack: Generally available
---

# Cross-cluster search
**Cross-cluster search** lets you run a single search request against one or more remote clusters. For example, you can use a cross-cluster search to filter and analyze log data stored on clusters in different data centers.

## Supported APIs

The following APIs support cross-cluster search:
- [Search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search)
- [Async search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-async-search-submit)
- [Multi search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-msearch)
- [Search template](https://www.elastic.co/docs/solutions/search/search-templates)
- [Multi search template](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-msearch-template)
- [Field capabilities](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-field-caps)
- [Painless execute API](https://www.elastic.co/docs/reference/scripting-languages/painless/painless-api-examples)
- [Resolve Index API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-resolve-index)
- [Vector tile search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-mvt)
- <applies-to>Elastic Stack: Generally available since 9.1, Elastic Stack: Preview in 9.0</applies-to> [ES|QL](https://www.elastic.co/docs/reference/query-languages/esql/esql-cross-clusters)
- <applies-to>Elastic Stack: Preview</applies-to> [EQL search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-eql-search)
- <applies-to>Elastic Stack: Preview</applies-to> [SQL search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-sql-query)


## Prerequisites

- Cross-cluster search requires remote clusters. To set up remote clusters, see [*Remote clusters*](https://www.elastic.co/docs/deploy-manage/remote-clusters).
  To ensure your remote cluster configuration supports cross-cluster search, see [Supported cross-cluster search configurations](#ccs-supported-configurations).
- To use cross-cluster search with ES|QL, both the local and remote clusters must have the appropriate [subscription level](https://www.elastic.co/subscriptions).
- The local coordinating node must have the [`remote_cluster_client`](/docs/deploy-manage/distributed-architecture/clusters-nodes-shards/node-roles#remote-node) node role.
- If you use [sniff mode](/docs/deploy-manage/remote-clusters/remote-clusters-self-managed#sniff-mode), the local coordinating node must be able to connect to seed and gateway nodes on the remote cluster.
  We recommend using gateway nodes capable of serving as coordinating nodes. The seed nodes can be a subset of these gateway nodes.
- If you use [proxy mode](/docs/deploy-manage/remote-clusters/remote-clusters-self-managed#proxy-mode), the local coordinating node must be able to connect to the configured `proxy_address`. The proxy at this address must be able to route connections to gateway and coordinating nodes on the remote cluster.
- Cross-cluster search requires different security privileges on the local cluster and remote cluster. See [Configure privileges for cross-cluster search](/docs/deploy-manage/remote-clusters/remote-clusters-cert#remote-clusters-privileges-ccs) and [*Remote clusters*](https://www.elastic.co/docs/deploy-manage/remote-clusters).


## Cross-cluster search examples


### Remote cluster setup

The following [cluster update settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-put-settings) API request adds three remote clusters: `cluster_one`, `cluster_two`, and `cluster_three`.
```json

{
  "persistent": {
    "cluster": {
      "remote": {
        "cluster_one": {
          "seeds": [
            "35.238.149.1:9443"
          ],
          "skip_unavailable": true
        },
        "cluster_two": {
          "seeds": [
            "35.238.149.2:9443"
          ],
          "skip_unavailable": false
        },
        "cluster_three": {  <1>
          "seeds": [
            "35.238.149.3:9443"
          ]
        }
      }
    }
  }
}
```


### Search a single remote cluster

In the search request, you specify data streams and indices on a remote cluster as `<remote_cluster_name>:<target>`.
The following [search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search) API request searches the `my-index-000001` index on a single remote cluster, `cluster_one`.
```json

{
  "size": 1,
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```

The API returns the following response. Note that when you search one or more remote clusters, a `_clusters` section is included to provide information about the search on each cluster.
```json
{
  "took": 150,
  "timed_out": false,
  "_shards": {
    "total": 12,
    "successful": 12,
    "failed": 0,
    "skipped": 0
  },
  "_clusters": {
    "total": 1,  
    "successful": 1,
    "skipped": 0,
    "running": 0,
    "partial": 0,
    "failed": 0,
    "details": {
      "cluster_one": {  
        "status": "successful",
        "indices": "my-index-000001", 
        "took": 148,  
        "timed_out": false,
        "_shards": {  
          "total": 12,
          "successful": 12,
          "skipped": 0,
          "failed": 0
        }
      }
    }
  },
  "hits": {
    "total" : {
        "value": 1,
        "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "cluster_one:my-index-000001", 
        "_id": "0",
        "_score": 1,
        "_source": {
          "user": {
            "id": "kimchy"
          },
          "message": "GET /search HTTP/1.1 200 1070000",
          "http": {
            "response":
              {
                "status_code": 200
              }
          }
        }
      }
    ]
  }
}
```


### Search multiple remote clusters

The following [search](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search) API request searches the `my-index-000001` index on three clusters:
- The local ("querying") cluster, with 10 shards
- Two remote clusters, `cluster_one`, with 12 shards and `cluster_two` with 6 shards.

```json

{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```

The API returns the following response:
```json
{
  "took": 150,
  "timed_out": false,
  "num_reduce_phases": 4,
  "_shards": {
    "total": 28,
    "successful": 28,
    "failed": 0,
    "skipped": 0
  },
  "_clusters": {
    "total": 3,
    "successful": 3,
    "skipped": 0,
    "running": 0,
    "partial": 0,
    "failed": 0,
    "details": {
      "(local)": {            
        "status": "successful",
        "indices": "my-index-000001",
        "took": 21,
        "timed_out": false,
        "_shards": {
          "total": 10,
          "successful": 10,
          "skipped": 0,
          "failed": 0
        }
      },
      "cluster_one": {
        "status": "successful",
        "indices": "my-index-000001",
        "took": 48,
        "timed_out": false,
        "_shards": {
          "total": 12,
          "successful": 12,
          "skipped": 0,
          "failed": 0
        }
      },
      "cluster_two": {
        "status": "successful",
        "indices": "my-index-000001",
        "took": 141,
        "timed_out": false,
        "_shards": {
          "total" : 6,
          "successful" : 6,
          "skipped": 0,
          "failed": 0
        }
      }
    }
  },
  "hits": {
    "total" : {
        "value": 3,
        "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "my-index-000001", 
        "_id": "0",
        "_score": 2,
        "_source": {
          "user": {
            "id": "kimchy"
          },
          "message": "GET /search HTTP/1.1 200 1070000",
          "http": {
            "response":
              {
                "status_code": 200
              }
          }
        }
      },
      {
        "_index": "cluster_one:my-index-000001", 
        "_id": "0",
        "_score": 1,
        "_source": {
          "user": {
            "id": "kimchy"
          },
          "message": "GET /search HTTP/1.1 200 1070000",
          "http": {
            "response":
              {
                "status_code": 200
              }
          }
        }
      },
      {
        "_index": "cluster_two:my-index-000001", 
        "_id": "0",
        "_score": 1,
        "_source": {
          "user": {
            "id": "kimchy"
          },
          "message": "GET /search HTTP/1.1 200 1070000",
          "http": {
            "response":
              {
                "status_code": 200
              }
          }
        }
      }
    ]
  }
}
```


## Using async search for cross-cluster search with ccs_minimize_roundtrips=true

Remote clusters can be queried asynchronously using the [async search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-async-search-submit) API. A cross-cluster search accepts a [`ccs_minimize_roundtrips`](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search#operation-search-ccs_minimize_roundtrips) parameter. For asynchronous searches it defaults to `false`. (Note: for synchronous searches it defaults to `true`.) See [Considerations for choosing whether to minimize roundtrips in a cross-cluster search](#ccs-min-roundtrips) to learn more about this option.
The following request does an asynchronous search of the `my-index-000001` index using `ccs_minimize_roundtrips=true` against three clusters (same ones as the previous example).
```json

{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```

The API returns the following response:
```json
{
  "id": "FklQYndoTDJ2VEFlMEVBTzFJMGhJVFEaLVlKYndBWWZSMUdicUc4WVlEaFl4ZzoxNTU=", 
  "is_partial": true,
  "is_running": true,
  "start_time_in_millis": 1685563581380,
  "expiration_time_in_millis": 1685995581380,
  "response": {
    "took": 1020,
    "timed_out": false,
    "num_reduce_phases": 0,
    "_shards": {
      "total": 10,     
      "successful": 0,
      "failed": 0,
      "skipped": 0
    },
    "_clusters": {    
      "total" : 3,
      "successful" : 0,
      "skipped": 0,
      "running": 3,
      "partial": 0,
      "failed": 0,
      "details": {
        "(local)": {
          "status": "running",
          "indices": "my-index-000001",
          "timed_out": false
        },
        "cluster_one": {
          "status": "running",
          "indices": "my-index-000001",
          "timed_out": false
        },
        "cluster_one": {
          "status": "running",
          "indices": "my-index-000001",
          "timed_out": false
        }
      }
    },
    "hits": {
      "total" : {
          "value": 0,
          "relation": "eq"
      },
      "max_score": null,
      "hits": []
    }
  }
}
```

If you query the [get async search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-async-search-submit) endpoint while the query is still running, you will see an update in the `_clusters` and `_shards` section of the response as each cluster finishes its search.
If you set `ccs_minimize_roundtrips=false`, then you will also see partial aggregation results from shards (from any cluster) that have finished, but no results are shown in "hits" section until the search has completed.
If you set `ccs_minimize_roundtrips=true`, then you will also see partial results in the "hits" and "aggregations" section of the response from all clusters that have completed so far. (Note: you can also see partial aggregation results from the local cluster even before it finishes.) The example below shows the `ccs_minimize_roundtrips=true` case.
```json
```

Response:
```json
{
  "id": "FklQYndoTDJ2VEFlMEVBTzFJMGhJVFEaLVlKYndBWWZSMUdicUc4WVlEaFl4ZzoxNTU=",
  "is_partial": true,
  "is_running": true,
  "start_time_in_millis": 1685564911108,
  "expiration_time_in_millis": 1685996911108,
  "response": {
    "took": 11164,
    "timed_out": false,
    "terminated_early": false,
    "_shards": {
      "total": 22,
      "successful": 22,  
      "skipped": 0,
      "failed": 0
    },
    "_clusters": {
      "total": 3,
      "successful": 2,  
      "skipped": 0,
      "running": 1,
      "partial": 0,
      "failed": 0,
      "details": {
        "(local)": {
          "status": "successful",
          "indices": "my-index-000001",
          "took": 2034,
          "timed_out": false,
          "_shards": {
            "total": 10,
            "successful": 10,
            "skipped": 0,
            "failed": 0
          }
        },
        "cluster_one": {
          "status": "successful",
          "indices": "my-index-000001",
          "took": 9039,
          "timed_out": false,
          "_shards": {
            "total": 12,
            "successful": 12,
            "skipped": 0,
            "failed": 0
          }
        },
        "cluster_two": {
          "status": "running",
          "indices": "my-index-000001",
          "timed_out": false
        }
      }
    },
    "hits": {
      "total": {
        "value": 542,  
        "relation": "eq"
      },
      "max_score": 1.7232,
      "hits": [...list of hits here...]
    }
  }
}
```

After searches on all the clusters have completed, querying the [get async search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-async-search-submit) endpoint will show the final status of the `_clusters` and `_shards` section as well as the hits and any aggregation results.
```json
```

Response:
```json
{
  "id": "FklQYndoTDJ2VEFlMEVBTzFJMGhJVFEaLVlKYndBWWZSMUdicUc4WVlEaFl4ZzoxNTU=",
  "is_partial": false,
  "is_running": false,
  "start_time_in_millis": 1685564911108,
  "expiration_time_in_millis": 1685996911108,
  "completion_time_in_millis": 1685564938727,  
  "response": {
    "took": 27619,
    "timed_out": false,
    "num_reduce_phases": 4,
    "_shards": {
      "total": 28,
      "successful": 28,  
      "skipped": 0,
      "failed": 0
    },
    "_clusters": {
      "total": 3,
      "successful": 3,   
      "skipped": 0,
      "running": 0,
      "partial": 0,
      "failed": 0,
      "details": {
        "(local)": {
          "status": "successful",
          "indices": "my-index-000001",
          "took": 2034,
          "timed_out": false,
          "_shards": {
            "total": 10,
            "successful": 10,
            "skipped": 0,
            "failed": 0
          }
        },
        "cluster_one": {
          "status": "successful",
          "indices": "my-index-000001",
          "took": 9039,
          "timed_out": false,
          "_shards": {
            "total": 12,
            "successful": 12,
            "skipped": 0,
            "failed": 0
          }
        },
        "cluster_two": {
          "status": "successful",
          "indices": "my-index-000001",
          "took": 27550,
          "timed_out": false,
          "_shards": {
            "total": 6,
            "successful": 6,
            "skipped": 0,
            "failed": 0
          }
        }
      }
    },
    "hits": {
      "total": {
        "value": 1067,
        "relation": "eq"
      },
      "max_score": 1.8293576,
      "hits": [...list of hits here...]
    }
  }
}
```


## Cross-cluster search failures

Failures during a cross-cluster search can result in one of two conditions:
1. partial results (2xx HTTP status code)
2. a failed search (4xx or 5xx HTTP status code)

Failure details will be present in the search response in both cases.
A search will be failed if a cluster marked with `skip_unavailable`=`false` is unavailable, disconnects during the search, or has search failures on all shards. In all other cases, failures will result in partial results.
Search failures on individual shards will be present in both the `_shards` section and the `_clusters` section of the response.
A failed search will have an additional top-level `errors` entry in the response.
Here is an example of a search with partial results due to a failure on one shard of one cluster. The search would be similar to ones shown previously. The `_async_search/status` endpoint is used here to show the completion status and not show the hits.
```json
```

Response:
```json
{
  "id": "FmpwbThueVB4UkRDeUxqb1l4akIza3cbWEJyeVBPQldTV3FGZGdIeUVabXBldzoyMDIw",
  "is_partial": true,  
  "is_running": false,
  "start_time_in_millis": 1692106901478,
  "expiration_time_in_millis": 1692538901478,
  "completion_time_in_millis": 1692106903547,
  "response": {
    "took": 2069,
    "timed_out": false,
    "num_reduce_phases": 4,
    "_shards": {
      "total": 28,
      "successful": 27,
      "skipped": 0,
      "failed": 1,
      "failures": [   
        {
          "shard": 1,
          "index": "cluster_two:my-index-000001",
          "node": "LMpUnAu0QEeCUMfg_56sAg",
          "reason": {
            "type": "query_shard_exception",
            "reason": "failed to create query: [my-index-000001][1] exception message here",
            "index_uuid": "4F2VWx8RQSeIhUE-nksvCQ",
            "index": "cluster_two:my-index-000001",
            "caused_by": {
              "type": "runtime_exception",
              "reason": "runtime_exception: [my-index-000001][1] exception message here"
            }
          }
        }
      ]
    },
    "_clusters": {
      "total": 3,
      "successful": 2,
      "skipped": 0,
      "running": 0,
      "partial": 1,   
      "failed": 0,
      "details": {
        "(local)": {
          "status": "successful",
          "indices": "my-index-000001",
          "took": 1753,
          "timed_out": false,
          "_shards": {
            "total": 10,
            "successful": 10,
            "skipped": 0,
            "failed": 0
          }
        },
        "cluster_one": {
          "status": "successful",
          "indices": "my-index-000001",
          "took": 2054,
          "timed_out": false,
          "_shards": {
            "total": 12,
            "successful": 12,
            "skipped": 0,
            "failed": 0
          }
        },
        "cluster_two": {
          "status": "partial",   
          "indices": "my-index-000001",
          "took": 2039,
          "timed_out": false,
          "_shards": {
            "total": 6,
            "successful": 5,
            "skipped": 0,
            "failed": 1   
          },
          "failures": [  
            {
              "shard": 1,
              "index": "cluster_two:my-index-000001",
              "node": "LMpUnAu0QEeCUMfg_56sAg",
              "reason": {
                "type": "query_shard_exception",
                "reason": "failed to create query: [my-index-000001][1] exception message here",
                "index_uuid": "4F2VWx8RQSeIhUE-nksvCQ",
                "index": "cluster_two:my-index-000001",
                "caused_by": {
                  "type": "runtime_exception",
                  "reason": "runtime_exception: [my-index-000001][1] exception message here"
                }
              }
            }
          ]
        }
      }
    },
    "hits": {
    }
  }
}
```

Here is an example where both `cluster_one` and `cluster_two` lost connectivity during a cross-cluster search. Since `cluster_one` is marked as `skip_unavailable`=`true`, its status is `skipped` and since `cluster_two` is marked as `skip_unavailable`=`false`, its status is `failed`. Since there was a `failed` cluster, a top level `error` is also present and this returns an HTTP status of 500 (not shown).
If you want the search to still return results even when a cluster is unavailable, set `skip_unavailable`=`true` for all the remote clusters.
```json
```

Response:
```json
{
  "id": "FjktRGJ1Y2w1U0phLTRhZnVyeUZ2MVEbWEJyeVBPQldTV3FGZGdIeUVabXBldzo5NzA4",
  "is_partial": true,
  "is_running": false,
  "start_time_in_millis": 1692112102650,
  "expiration_time_in_millis": 1692544102650,
  "completion_time_in_millis": 1692112106177,
  "response": {
    "took": 3527,
    "timed_out": false,
    "terminated_early": false,
    "_shards": {
      "total": 10,   
      "successful": 10,
      "skipped": 0,
      "failed": 0
    },
    "_clusters": {
      "total": 3,
      "successful": 1,
      "skipped": 1,
      "running": 0,
      "partial": 0,
      "failed": 1,
      "details": {
        "(local)": {
          "status": "successful",
          "indices": "my-index-000001",
          "took": 1473,
          "timed_out": false,
          "_shards": {
            "total": 10,
            "successful": 10,
            "skipped": 0,
            "failed": 0
          }
        },
        "cluster_one": {
          "status": "skipped",   
          "indices": "my-index-000001",
          "timed_out": false,
          "failures": [
            {
              "shard": -1,
              "index": null,
              "reason": {
                "type": "node_disconnected_exception",   
                "reason": "[myhostname1][35.238.149.1:9443][indices:data/read/search] disconnected"
              }
            }
          ]
        },
        "cluster_two": {
          "status": "failed",   
          "indices": "my-index-000001",
          "timed_out": false,
          "failures": [
            {
              "shard": -1,
              "index": null,
              "reason": {
                "type": "node_disconnected_exception",
                "reason": "[myhostname2][35.238.149.2:9443][indices:data/read/search] disconnected"
              }
            }
          ]
        }
      }
    },
    "hits": {
    },
  }
  "error": {  
    "type": "status_exception",
    "reason": "error while executing search",
    "caused_by": {
      "type": "node_disconnected_exception",
      "reason": "[myhostname2][35.238.149.2:9443][indices:data/read/search] disconnected"
    }
  }
}
```


## Excluding clusters or indices from a cross-cluster search

If you use a wildcard to include a large list of clusters and/or indices, you can explicitly exclude one or more clusters or indices with a `-` minus sign in front of the cluster or index.
To exclude an entire cluster, you would put the minus sign in front of the cluster alias, such as: `-mycluster:*`. When excluding a cluster, you must use `*` in the index position or an error will be returned.
To exclude a specific remote index, you would put the minus sign in front of the index, such as `mycluster:-myindex`.
**Exclude a remote cluster**
Here’s how you would exclude `cluster_three` from a cross-cluster search that uses a wildcard to specify a list of clusters:
```json

{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```

**Exclude a remote index**
Suppose you want to search all indices matching `my-index-*` but you want to exclude `my-index-000001` on `cluster_three`. Here’s how you could do that:
```json

{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```


## Using async search for cross-cluster search with ccs_minimize_roundtrips=false

The `_shards` and `_clusters` section of the response behave differently when `ccs_minimize_roundtrips` is `false`.
Key differences are:
1. The `_shards` section total count will be accurate immediately as the total number of shards is gathered from all clusters before the search starts.
2. The `_shards` section will be incrementally updated as searches on individual shards complete, whereas when minimizing roundtrips, the shards section will be updated as searches on shards complete on the local cluster and then as each remote cluster reports back its full search results.
3. The `_cluster` section starts off listing all of its shard counts, since they are also obtained before the query phase begins.

Example using the same setup as in the previous section (`ccs_minimize_roundtrips=true`):
```json

{
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  },
  "_source": ["user.id", "message", "http.response.status_code"]
}
```

The API returns the following response if the query takes longer than the `wait_for_completion_timeout` duration (see [Async search](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-async-search-submit)).
```json
{
  "id": "FklQYndoTDJ2VEFlMEVBTzFJMGhJVFEaLVlKYndBWWZSMUdicUc4WVlEaFl4ZzoxNTU=",
  "is_partial": true,
  "is_running": true,
  "start_time_in_millis": 1685563581380,
  "expiration_time_in_millis": 1685995581380,
  "response": {
    "took": 1020,
    "timed_out": false,
    "_shards": {
      "total": 28,     
      "successful": 0,
      "failed": 0,
      "skipped": 0
    },
    "_clusters": {
      "total" : 3,
      "successful": 0,
      "skipped": 0,
      "running": 3,    
      "partial": 0,
      "failed": 0,
      "details": {    
        "(local)": {
          "status": "running",
          "indices": "my-index-000001",
          "timed_out": false,
          "_shards": {
            "total": 10,
            "successful": 0,
            "skipped": 0,
            "failed": 0
          }
        },
        "cluster_one": {
          "status": "running",
          "indices": "my-index-000001",
          "timed_out": false,
          "_shards": {
            "total": 12,
            "successful": 0,
            "skipped": 0,
            "failed": 0
          }
        },
        "cluster_two": {
          "status": "running",
          "indices": "my-index-000001",
          "timed_out": false,
          "_shards": {
            "total": 6,
            "successful": 0,
            "skipped": 0,
            "failed": 0
          }
        }
      }
    },
    "hits": {
      "total" : {
          "value": 0,
          "relation": "eq"
      },
      "max_score": null,
      "hits": []
    }
  }
}
```


## Optional remote clusters

By default, a cross-cluster search fails if a remote cluster in the request is unavailable or returns an error where the search on all shards failed. Use the `skip_unavailable` cluster setting to mark a specific remote cluster as either optional or required for cross-cluster search.
<important>
  In Elasticsearch 8.15, the default value for `skip_unavailable` was changed from `false` to `true`. Before Elasticsearch 8.15, if you want a cluster to be treated as optional for a cross-cluster search, then you need to set that configuration. From Elasticsearch 8.15 forward, you need to set the configuration in order to make a cluster required for the cross-cluster search.
</important>

If `skip_unavailable` is `true`, a cross-cluster search:
- Skips the remote cluster if its nodes are unavailable during the search. The response’s `_clusters.skipped` value contains a count of any skipped clusters and the `_clusters.details` section of the response will show a `skipped` status.
- Ignores errors returned by the remote cluster, such as errors related to unavailable shards or indices. This can include errors related to search parameters such as [`allow_no_indices`](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/api-conventions#api-multi-index) and [`ignore_unavailable`](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/api-conventions#api-multi-index).
- Ignores the [`allow_partial_search_results`](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search#operation-search-allow_partial_search_results) parameter and the related `search.default_allow_partial_results` cluster setting when searching the remote cluster. This means searches on the remote cluster may return partial results.

You can modify the `skip_unavailable` setting by editing the `cluster.remote.<cluster_alias>` settings in the [`elasticsearch.yml`](https://www.elastic.co/docs/deploy-manage/stack-settings) config file. For example:
```yml
cluster:
    remote:
        cluster_one:
            seeds: 35.238.149.1:9443
            skip_unavailable: false
        cluster_two:
            seeds: 35.238.149.2:9443
            skip_unavailable: true
```

Or you can set the `cluster.remote` settings via the [cluster update settings](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-cluster-put-settings) API as shown [here](#ccs-remote-cluster-setup).
When a remote cluster configured with `skip_unavailable: true` (such as `cluster_two` above) is disconnected or unavailable during a cross-cluster search, Elasticsearch won’t include matching documents from that cluster in the final results and the search will be considered successful (HTTP status 200 OK).
If at least one shard from a cluster provides search results, those results will be used and the search will return partial data. This is true regardless of the `skip_unavailable` setting of the remote cluster. (If doing cross-cluster search using async search, the `is_partial` field will be set to `true` to indicate partial results.)

## How cross-cluster search handles network delays

Because cross-cluster search involves sending requests to remote clusters, any network delays can impact search speed. To avoid slow searches, cross-cluster search offers two options for handling network delays:
<definitions>
  <definition term="Minimize network roundtrips">
    By default, Elasticsearch reduces the number of network roundtrips between remote clusters. This reduces the impact of network delays on search speed. However, Elasticsearch can’t reduce network roundtrips for large search requests, such as those including a [scroll](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/paginate-search-results#scroll-search-results) or [inner hits](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/retrieve-inner-hits).
    See [Considerations for choosing whether to minimize roundtrips in a cross-cluster search](#ccs-min-roundtrips) to learn how this option works.
  </definition>
  <definition term="Don’t minimize network roundtrips">
    For search requests that include a scroll or inner hits, Elasticsearch sends multiple outgoing and ingoing requests to each remote cluster. You can also choose this option by setting the [`ccs_minimize_roundtrips`](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search) parameter to `false`. While typically slower, this approach may work well for networks with low latency.
    See [Don’t minimize network roundtrips](#ccs-unmin-roundtrips) to learn how this option works.
  </definition>
</definitions>

<note>
  The [vector tile search API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-search-mvt) always minimizes network roundtrips and doesn’t include the `ccs_minimize_roundtrips` parameter.
</note>

<note>
  The [Approximate kNN search](/docs/solutions/search/vector/knn#approximate-knn) doesn’t support minimizing network roundtrips, and sets the parameter `ccs_minimize_roundtrips` to `false`.
</note>


### Considerations for choosing whether to minimize roundtrips in a cross-cluster search

Advantages of minimizing roundtrips:
1. For cross-cluster searches that query a large number of shards, the minimize roundtrips option typically provides much better performance. This is especially true if the clusters being searched have high network latency (e.g., distant geographic regions).
2. When doing an async cross-cluster search, the `GET _async_search/<search_id>` endpoint will provide both top hits and aggregations from all clusters that have reported back results even while the search is still running on other clusters. In other words, it provides "incremental" partial results as the search progresses. Note that if the local cluster is included in the search, it has special handling in that it can show partial aggregations (but not partial top hits) while the search on the local cluster is still running.

Not minimizing roundtrips when using async-search allows you to get back incremental results of any aggregations in your query as individual shards complete (rather than whole clusters) while the search is still running, but top hits are not shown until the search has completed on all clusters.
By default, synchronous searches minimize roundtrips, while asynchronous searches do not. You can override the default by using the `ccs_minimize_roundtrips` parameter, setting it to either `true` or `false`, as shown in several examples earlier in this document.

### Minimize network roundtrips

Here’s how cross-cluster search works when you minimize network roundtrips.
1. You send a cross-cluster search request to your local cluster. A coordinating node in that cluster receives and parses the request.
   ![ccs min roundtrip client request](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-min-roundtrip-client-request.svg)
2. The coordinating node sends a single search request to each cluster, including the local cluster. Each cluster performs the search request independently, applying its own cluster-level settings to the request.
   ![ccs min roundtrip cluster search](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-min-roundtrip-cluster-search.svg)
3. Each remote cluster sends its search results back to the coordinating node.
   ![ccs min roundtrip cluster results](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-min-roundtrip-cluster-results.svg)
4. After collecting results from each cluster, the coordinating node returns the final results in the cross-cluster search response.
   ![ccs min roundtrip client response](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-min-roundtrip-client-response.svg)


### Don’t minimize network roundtrips

Here’s how cross-cluster search works when you don’t minimize network roundtrips.
1. You send a cross-cluster search request to your local cluster. A coordinating node in that cluster receives and parses the request.
   ![ccs min roundtrip client request](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-min-roundtrip-client-request.svg)
2. The coordinating node sends a "search shards" transport layer request to each remote cluster to have them to perform a "can match" search to determine which shards on each cluster should be searched.
   ![ccs min roundtrip cluster search](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-min-roundtrip-cluster-search.svg)
3. Each remote cluster sends its response back to the coordinating node. This response contains information about the indices and shards the cross-cluster search request will be executed on.
   ![ccs min roundtrip cluster results](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-min-roundtrip-cluster-results.svg)
4. The coordinating node sends a search request to each shard, including those in its own cluster. Each shard performs the search request independently.
   <warning>
   When network roundtrips aren’t minimized, the search is executed as if all data were in the coordinating node’s cluster. We recommend updating cluster-level settings or search request parameters that limit searches, such as `action.search.shard_count.limit`, `pre_filter_shard_size`, and `max_concurrent_shard_requests`, to account for this. If these limits are too low, the search may be rejected.
   </warning>
   ![ccs dont min roundtrip shard search](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-dont-min-roundtrip-shard-search.svg)
5. Each shard sends its search results back to the coordinating node.
   ![ccs dont min roundtrip shard results](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-dont-min-roundtrip-shard-results.svg)
6. After collecting results from each cluster, the coordinating node returns the final results in the cross-cluster search response.
   ![ccs min roundtrip client response](https://www.elastic.co/docs/solutions/images/elasticsearch-reference-ccs-min-roundtrip-client-response.svg)


## Supported cross-cluster search configurations

Elastic supports searches from a local cluster to a remote cluster running:
- The previous minor version.
- The same version.
- A newer minor version in the same major version.

Elastic also supports searches from a local cluster running the last minor version of a major version to a remote cluster running any minor version in the following major version. For example, a local 8.19 cluster can search any remote 9.x cluster. However, a search from a local 9.0 cluster to a remote 8.17 or 7.17 cluster is not supported.
<note>
  Version 8.19 is the final minor release in the 8.x series. Unlike past releases, 8.18 was launched simultaneously with 9.0, allowing cross-version compatibility between them. Hence, as shown in the compatibility table, 8.18 can only search 9.0 clusters in the 9.x series, while 8.19 supports searching 9.0 clusters and later.
</note>



|                       |                        |     |     |     |     |     |     |     |     |     |     |      |      |      |      |      |      |      |      |      |      |     |     |     |     |
|-----------------------|------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|------|------|------|------|------|------|------|-----|-----|-----|-----|
|                       | Remote cluster version |     |     |     |     |     |     |     |     |     |     |      |      |      |      |      |      |      |      |      |      |     |     |     |     |
| Local cluster version | 7.17                   | 8.0 | 8.1 | 8.2 | 8.3 | 8.4 | 8.5 | 8.6 | 8.7 | 8.8 | 8.9 | 8.10 | 8.11 | 8.12 | 8.13 | 8.14 | 8.15 | 8.16 | 8.17 | 8.18 | 8.19 | 9.0 | 9.1 | 9.2 | 9.3 |
| 7.17                  | ✅                      | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.0                   | ✅                      | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.1                   | ❌                      | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.2                   | ❌                      | ❌   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.3                   | ❌                      | ❌   | ❌   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.4                   | ❌                      | ❌   | ❌   | ❌   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.5                   | ❌                      | ❌   | ❌   | ❌   | ❌   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.6                   | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ✅   | ✅   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.7                   | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ✅   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.8                   | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ✅   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.9                   | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ✅   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.10                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ✅   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.11                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.12                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.13                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.14                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.15                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ❌    | ✅    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.16                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ❌    | ❌    | ✅    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.17                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ✅    | ✅    | ✅    | ✅    | ❌   | ❌   | ❌   | ❌   |
| 8.18                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ✅    | ✅    | ✅    | ✅   | ❌   | ❌   | ❌   |
| 8.19                  | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ✅    | ✅    | ✅   | ✅   | ✅   | ✅   |
| 9.0                   | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ✅    | ❌    | ✅   | ✅   | ✅   | ✅   |
| 9.1                   | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ✅   | ✅   | ✅   | ✅   |
| 9.2                   | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌   | ✅   | ✅   | ✅   |
| 9.3                   | ❌                      | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌   | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌    | ❌   | ❌   | ✅   | ✅   |

<important>
  For the [EQL search API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-eql-search), the local and remote clusters must use the same Elasticsearch version if they have versions prior to 7.17.7 (included) or prior to 8.5.1 (included).
</important>

Only features that exist across all searched clusters are supported. Using a feature with a remote cluster where the feature is not supported will result in undefined behavior.
A cross-cluster search using an unsupported configuration may still work. However, such searches aren’t tested by Elastic, and their behavior isn’t guaranteed.

### Ensure cross-cluster search support

The simplest way to ensure your clusters support cross-cluster search is to keep each cluster on the same version of Elasticsearch. If you need to maintain clusters with different versions, you can:
- Maintain a dedicated cluster for cross-cluster search. Keep this cluster on the earliest version needed to search the other clusters. For example, if you have 8.19 and 9.x clusters, you can maintain a dedicated 8.19 cluster to use as the local cluster for cross-cluster search.
- Keep each cluster no more than one minor version apart. This lets you use any cluster as the local cluster when running a cross-cluster search.


### Cross-cluster search during an upgrade

You can still search a remote cluster while performing a rolling upgrade on the local cluster. However, the local coordinating node’s "upgrade from" and "upgrade to" version must be compatible with the remote cluster’s gateway node.
<warning>
  Running multiple versions of Elasticsearch in the same cluster beyond the duration of an upgrade is not supported.
</warning>

For more information about upgrades, see [Upgrading Elasticsearch](https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster).