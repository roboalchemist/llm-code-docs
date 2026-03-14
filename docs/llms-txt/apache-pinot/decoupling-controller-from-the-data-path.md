# Source: https://docs.pinot.apache.org/release-0.9.0/operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/release-0.10.0/operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/release-0.11.0/operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/release-0.12.0/operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/release-0.12.1/operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Source: https://docs.pinot.apache.org/operators/operating-pinot/decoupling-controller-from-the-data-path.md

# Decoupling Controller from the Data Path

## Ingestion bottleneck on the Pinot Controller

For real-time tables, when a Pinot server finishes consuming a segment, the segment goes through a completion protocol sequence. By default, the segment is uploaded to the lead Pinot controller which in turn persists the segment to deep store (for example, NFS, S3 or HDFS). As a result, because all real-time segments flow through the controller, it may become a bottleneck and slow down the overall ingestion rate. To overcome this limitation, we've added a new stream-level configuration to bypass the controller and upload the completed segment to deep store directly.

### Upload completed segment to deep store directly

To upload the completed segment to the deep store directly, add the following stream-level configuration.

```
realtime.segment.serverUploadToDeepStore = true
```

When this configuration is enabled, Pinot servers attempt to upload the completed segment to the segment store directly, bypassing the controller. When finished, Pinot updates the controller with the corresponding segment metadata.

{% hint style="info" %}
`pinot.server.instance.segment.store.uri` is optional by default. However, this config is required so that the server knows where the deep store is. Before enabling `realtime.segment.serverUploadToDeepStore` on the table, verify the `pinot.server.instance.segment.store.uri=<controller.data.dir>` is configured on the servers.
{% endhint %}

## Overview of peer download policy

Peer download policy allows failure recovery in case uploading the completed segment to the deep store fails. If the segment store is unavailable, the corresponding segments can still be downloaded directly from the Pinot servers.

## Enable peer download for segments

This scheme only works for real-time tables using the Low Level Consumer (LLC) mode. To enable peer download for segments, update the controller, server, and table configurations as follows:

### Server Config

Add the following things to the server configuration:

```
pinot.server.instance.segment.store.uri=<URI of segment store>
pinot.server.instance.enable.split.commit=true
pinot.server.storage.factory.class.(scheme)=<the corresponding Pinot FS impl>
```

Here. the URI of segment store should point to the ***full*** path in the corresponding data directory, with both the filesystem scheme and path (eg: `file://dir` or `hdfs://path` or `s3://path`).

Replace *pinot.server.storage.factory.class.(scheme)* with the corresponding scheme (for example, *hdfs, s3* or *gcs*) of the segment store URI configured above. Then, add the PinotFS subclass for the scheme as the config value.

### Table config

Add the following to the real-time [segments config](https://docs.pinot.apache.org/configuration-reference/table#segmentsconfig):

```
    "segmentsConfig": {
      ...
      "peerSegmentDownloadScheme": "http"
    }
```

In this case, the `peerSegmentDownloadScheme` can be either `http` or `https`.

### Config for failure case handling

Enabling peer download may incur LLC segments failed to be uploaded to segment store in some failure cases, e.g. segment store is unavailable during segment completion. Add the following controller config to enable the upload retry by a controller periodic job asynchronously.

```
controller.realtime.segment.deepStoreUploadRetryEnabled=true
```
