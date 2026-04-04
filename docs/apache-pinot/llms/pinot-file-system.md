# Source: https://docs.pinot.apache.org/release-0.4.0/plugins/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-0.4.0/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-0.9.0/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-0.10.0/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/release-1.4.0/manage-data/data-import/pinot-file-system.md

# Source: https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system.md

# File Systems

FileSystem is an abstraction provided by Pinot to access data stored in distributed file systems (DFS).

Pinot uses distributed file systems for the following purposes:

* **Batch ingestion job**: To read the input data (CSV, Avro, Thrift, etc.) and to write generated segments to DFS.
* **Controller**: When a segment is uploaded to the controller, the controller saves it in the configured DFS.
* **Server**:- When a server(s) is notified of a new segment, the server copies the segment from remote DFS to their local node using the DFS abstraction.

## Supported file systems

Pinot lets you choose a distributed file system provider. The following file systems are supported by Pinot:

* [Amazon S3](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system/amazon-s3)
* [Google Cloud Storage](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system/import-from-gcp)
* [HDFS](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system/import-from-hdfs)
* [Azure Data Lake Storage](https://docs.pinot.apache.org/manage-data/data-import/pinot-file-system/import-from-adls-azure)

## Enabling a file system

To use a distributed file system, you need to enable plugins. To do that, specify the plugin directory and include the required plugins:

```
-Dplugins.dir=/opt/pinot/plugins -Dplugins.include=pinot-plugin-to-include-1,pinot-plugin-to-include-2
```

You can change the file system in the `controller` and `server` configuration. In the following configuration example, the URI is `s3://bucket/path/to/file` and `scheme` refers to the file system URI prefix `s3`.

```
#CONTROLLER

pinot.controller.storage.factory.class.[scheme]=className of the pinot file system
pinot.controller.segment.fetcher.protocols=file,http,[scheme]
pinot.controller.segment.fetcher.[scheme].class=org.apache.pinot.common.utils.fetcher.PinotFSSegmentFetcher
```

```
#SERVER

pinot.server.storage.factory.class.[scheme]=className of the Pinot file system
pinot.server.segment.fetcher.protocols=file,http,[scheme]
pinot.server.segment.fetcher.[scheme].class=org.apache.pinot.common.utils.fetcher.PinotFSSegmentFetcher
```

You can also change the file system during ingestion. In the ingestion job spec, specify the file system with the following configuration:

```
pinotFSSpecs
  - scheme: file
    className: org.apache.pinot.spi.filesystem.LocalPinotFS
```
