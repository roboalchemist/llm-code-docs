# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/data-storage-optimizer-logging/pdso-aws-s3-sdk-logging.md

# AWS S3 SDK logging

In some cases, particularly when troubleshooting issues between the Data Optimizer instance and the Hitachi Content Platform,you may want to see the detailed AWS SDK logs. These logs include many client-side details as to the content of the requests being sent to the HCP and the detailed content of the responses received. To enable this logging the `LOG_SDK` configuration parameter must be properly set, and the `LOG_LEVEL` parameter set to DEBUG. This logging is enabled only at start time and cannot be enabled by reloading the configuration file. When enabled, details about the communication between the Data Optimizer instance and the HCP are logged to a file called `ldo_aws_sdk_*datestamp*.log` in the specified folder, where *datestamp* represents the day and hour logging began.

As a best practice, it is recommended to keep SDK logging disabled unless actively troubleshooting. The logs can get quite large, and Data Optimizer does not manage or rotate these logs. It is up to the user to delete these files when done with troubleshooting exercises.
