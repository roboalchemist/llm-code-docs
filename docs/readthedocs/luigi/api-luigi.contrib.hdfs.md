# luigi.contrib.hdfs

Provides access to HDFS using the `HdfsTarget`, a subclass of `Target`.
You can configure what client by setting the “client” config under the “hdfs” section in the configuration, or using the `--hdfs-client` command line option.
“hadoopcli” is the slowest, but should work out of the box.

Since the hdfs functionality is quite big in luigi, it’s split into smaller
files under `luigi/contrib/hdfs/*.py`. But for the sake of convenience and
API stability, everything is reexported under `luigi.contrib.hdfs`.

Modules

`abstract_client`

Module containing abstract class about hdfs clients.

`clients`

The implementations of the hdfs clients.

`config`

You can configure what client by setting the "client" config under the "hdfs" section in the configuration, or using the `--hdfs-client` command line option.

`error`

The implementations of the hdfs clients.

`format`

`hadoopcli_clients`

The implementations of the hdfs clients.

`target`

Provides access to HDFS using the `HdfsTarget`, a subclass of `Target`.

`webhdfs_client`

A luigi file system client that wraps around the hdfs-library (a webhdfs client)