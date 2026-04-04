# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/data-storage-optimizer-logging/pdso-marking-logs.md

# Marking logs

Inserting entries into the logs can help mark the beginning or end of a test or series of tests. The `ldoctl` command line utility gives a command to easily insert entries into the log. Use the following command to insert a custom message into the log:

```
ldoctl logs mark "Message to put in the log."
```
