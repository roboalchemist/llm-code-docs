# Source: https://docs.pinot.apache.org/release-0.4.0/developers/tutorials/pinot-connectors/batch/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-0.9.0/developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-0.10.0/developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-0.11.0/developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-0.12.0/developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-0.12.1/developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Source: https://docs.pinot.apache.org/developers/plugin-architecture/write-custom-plugins/write-your-batch.md

# Batch Segment Fetcher Plugin

You can also implement your own segment fetchers for other file systems and load into Pinot system with an external jar.

All you need to do is to implement a class that extends the interface of [SegmentFetcher](https://github.com/apache/pinot/blob/master/pinot-common/src/main/java/org/apache/pinot/common/segment/fetcher/SegmentFetcher.java) and provide config to Pinot Controller and Server as follows:

```
pinot.controller.segment.fetcher.`<protocol>`.class =`<class path to your implementation>
```

or

```
pinot.server.segment.fetcher.`<protocol>`.class =`<class path to your implementation>
```

You can also provide other configs to your fetcher under config-root `pinot.server.segment.fetcher.<protocol>`
