# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/monitoring-data-storage-optimizer.md

# Monitor Data Optimizer

Data Optimizer maintains operation and performance metrics that are useful for ongoing monitoring of the software. To instruct Data Optimizer to emit these metrics use the `ldoctl` command line utility as follows:

```
ldoctl metrics collect
```

The command causes Data Optimizer to emit a JSON string containing the metrics to the `systemd` journal log, or to the file specified in the `METRICS_FILE` parameter in the configuration file, if specified and permissions are properly set on the target folder.

`ldoctl metrics collect`

The command causes Data Optimizer to emit a JSON string containing the metrics to the `systemd` journal log, or to the file specified in the `METRICS_FILE` parameter in the configuration file, if specified and permissions are properly set on the target folder.

The format of the JSON string is as follows:

```
{
    "date": "2019 10 25 13:48:00 +0000",
    "metrics": [
        {
            "event": "*event\_name*",
            "max": *max\_value*,
            "mean": *mean\_value*,
            "min": *min\_value*,
            "stddev": *stddev*,
            "total": *event\_count*,
            "type": "timer"
        },
        {
            "event": "*event\_name*",
            "total": *event\_count*,
            "type": "counter"
        }
        
    ]
}

```

## Types of metrics events

There are two types of metrics events: `timer` and `counter`. Both `timer` and `counter` metrics events have an event name in the `event` field.

* **Timer events**

  Report the maximum (`max`), mean (`mean`), minimum (`min`), and standard deviation (`stddev`) of the amount of time it takes to complete certain measured internal operations. The `total` field for timer events is always a count of the number of times the event has occurred. Following is a list of the `timer` events:

  * `get_attr`: Filesystem request for file attributes, that is, `stat`
  * `readdir`: Directory listing, includes S3 listing if applicable
  * `md_cache_add_entry`: Adding an entry to the local metadata store
  * `md_cache_update_entry`: Updating an entry in the local metadata store
  * `md_cache_evict_entry`: Removing an entry in the local metadata store
  * `md_cache_get_entry`: Getting an entry from the local metadata store
  * `md_cache_copy_entry_new_path`: Copying an entry in the local metadata store
  * `md_cache_get_size`: Counting the entries in the local metadata store
  * `md_cache_readdir_root`: Listing the root directory from the local metadata store
  * `md_cache_readdir`: Listing a directory from the local metadata store
  * `*_prepare_stmt`: Preparing a DB operation for the local metadata store
  * `*_exec_stmt`: Executing a DB operation on the local metadata store
* **Counter Events**

  The `total` field can be a count of occurrences or some other count. Following is a list of the `counter` events:

  * `md_cache_size`: The number of entries in the local metadata store
  * `md_cache_size`: The number of entries in the local metadata store
  * `open_file_size`: The number of currently open file handles in the Data Optimizer volume
  * `s3_op_put`: The count of S3 PUT requests to the HCP
  * `s3_op_get`: The count of S3 GET requests to the HCP
  * `s3_op_list`: The count of bucket listing requests to the HCP
  * `s3_op_delete`: The count of S3 DELETE requests to the HCP
  * `s3_op_copy`: The count of S3 put-copy requests to the HCP
  * `s3_op_error`: The count of S3 error responses from the HCP
  * `warnings`: The count of logged warnings
  * `errors`: The count of logged errors

**Note:** All values reported in the metrics are cumulative and reset only when Data Optimizer restarts.
