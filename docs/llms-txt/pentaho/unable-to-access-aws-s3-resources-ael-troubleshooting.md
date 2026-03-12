# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/unable-to-access-aws-s3-resources-ael-troubleshooting.md

# Unable to access AWS S3 resources

You might receive an error message when trying to access AWS S3 resources. The URIs starting with `s3://`, `s3n://`, or `s3a://`, such as "`s3://mybucket/myobject.parquet`" for example, require specific cluster configurations.

To resolve the issue for an EMR cluster, see [Hadoop libraries are missing](https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/hadoop-libraries-are-missing) for instructions.

To resolve the issue for a Cloudera or Hortonworks cluster, see the following vendor-specific cluster documentation for details:

* [Cloudera documentation](https://docs.cloudera.com/documentation/enterprise/latest/topics/sg_aws_credentials.html)
* [Hortonworks documentation](https://docs.cloudera.com/HDPDocuments/HDP3/HDP-3.1.0/bk_cloud-data-access/content/about.html)
