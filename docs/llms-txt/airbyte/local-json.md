# Source: https://docs.airbyte.com/integrations/destinations/local-json.md

![](https://connectors.airbyte.com/files/metadata/airbyte/destination-local-json/latest/icon.svg)

# Local JSON

Copy Page

* Availability

  Core Standard Plus Pro Enterprise Flex Self-Managed Enterprise PyAirbyte

* Support Level

  [Marketplace](/integrations/connector-support-levels.md)

* Connector Version

  [0.2.13](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-local-json)

  <!-- -->

  [ ](https://github.com/airbytehq/airbyte/blob/master/airbyte-integrations/connectors/destination-local-json)(last updated 9 months ago)

* Sync Success Rate

* Usage Rate

* Definition ID

  `a625d593-bba5-4a1c-a53d-2d246268a816`

danger

This destination is meant to be used on a local workstation and won't work on Kubernetes

## Overview[​](#overview "Direct link to Overview")

This destination writes data to a directory on the *local* filesystem on the host running Airbyte. By default, data is written to `/tmp/airbyte_local`. To change this location, modify the `LOCAL_ROOT` environment variable for Airbyte.

### Sync Overview[​](#sync-overview "Direct link to Sync Overview")

#### Output schema[​](#output-schema "Direct link to Output schema")

Each stream will be output into its own file. Each file will a collections of `json` objects containing 3 fields:

* `_airbyte_ab_id`: a uuid assigned by Airbyte to each event that is processed.
* `_airbyte_emitted_at`: a timestamp representing when the event was pulled from the data source.
* `_airbyte_data`: a json blob representing with the extracted data.

#### Performance considerations[​](#performance-considerations "Direct link to Performance considerations")

This integration will be constrained by the speed at which your filesystem accepts writes.

## Supported sync modes[​](#supported-sync-modes "Direct link to Supported sync modes")

| Sync mode                                                                                                                                     | Supported? |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [Full Refresh - Overwrite](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite)                   | Yes        |
| [Full Refresh - Append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-append)                         | Yes        |
| [Full Refresh - Overwrite + Deduped](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/full-refresh-overwrite-deduped) | No         |
| [Incremental Sync - Append](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append)                      | Yes        |
| [Incremental Sync - Append + Deduped](https://docs.airbyte.com/platform/using-airbyte/core-concepts/sync-modes/incremental-append-deduped)    | No         |

## Getting Started[​](#getting-started "Direct link to Getting Started")

The `destination_path` will always start with `/local` whether it is specified by the user or not. Any directory nesting within local will be mapped onto the local mount.

By default, the `LOCAL_ROOT` env variable in the `.env` file is set `/tmp/airbyte_local`.

The local mount is mounted by Docker onto `LOCAL_ROOT`. This means the `/local` is substituted by `/tmp/airbyte_local` by default.

caution

Please make sure that Docker Desktop has access to `/tmp` (and `/private` on a MacOS, as /tmp has a symlink that points to /private. It will not work otherwise). You allow it with "File sharing" in `Settings -> Resources -> File sharing -> add the one or two above folder` and hit the "Apply & restart" button.

### Example:[​](#example "Direct link to Example:")

* If `destination_path` is set to `/local/cars/models`
* the local mount is using the `/tmp/airbyte_local` default
* then all data will be written to `/tmp/airbyte_local/cars/models` directory.

## Access Replicated Data Files[​](#access-replicated-data-files "Direct link to Access Replicated Data Files")

If your Airbyte instance is running on the same computer that you are navigating with, you can open your browser and enter <file:///tmp/airbyte_local> to look at the replicated data locally. If the first approach fails or if your Airbyte instance is running on a remote server, follow the following steps to access the replicated files:

1. Access the scheduler container using `docker exec -it airbyte-server bash`
2. Navigate to the default local mount using `cd /tmp/airbyte_local`
3. Navigate to the replicated file directory you specified when you created the destination, using `cd /{destination_path}`
4. List files containing the replicated data using `ls`
5. Execute `cat {filename}` to display the data in a particular file

You can also copy the output file to your host machine, the following command will copy the file to the current working directory you are using:

```
docker cp airbyte-server:/tmp/airbyte_local/{destination_path}/{filename}.jsonl .
```

Note: If you are running Airbyte on Windows with Docker backed by WSL2, you have to use similar step as above or refer to this [link](/integrations/locating-files-local-destination.md) for an alternative approach.

## Namespace support[​](#namespace-support "Direct link to Namespace support")

This destination does not support [namespaces](https://docs.airbyte.com/platform/using-airbyte/core-concepts/namespaces).

## Reference[​](#reference "Direct link to Reference")

### Config fields reference

Field

Type

Property name

›

Destination Path

required

string

destination\_path

## Changelog[​](#changelog "Direct link to Changelog")

Expand to review

| Version | Date       | Pull Request                                             | Subject                                                           |
| ------- | ---------- | -------------------------------------------------------- | ----------------------------------------------------------------- |
| 0.2.13  | 2025-03-24 | [56355](https://github.com/airbytehq/airbyte/pull/56355) | Upgrade to airbyte/java-connector-base:2.0.1 to be M4 compatible. |
| 0.2.12  | 2024-12-18 | [49908](https://github.com/airbytehq/airbyte/pull/49908) | Use a base image: airbyte/java-connector-base:1.0.0               |
| 0.2.11  | 2022-02-14 | [14641](https://github.com/airbytehq/airbyte/pull/14641) | Include lifecycle management                                      |
