# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-maintain-landing-page/troubleshoot-data-storage-optimizer-fs/data-storage-optimizer-logging/pdso-viewing-logs-on-ambari.md

# Viewing logs on Ambari

Depending on the version of Ambari you are using, the **Log Search** service, and other services it depends on, you might first need to installed and configure it. If the **Log Search** service was installed prior to installing Data Optimizer, restart the **Log Search** service to start indexing the logs in Data Optimizer. Without this service, Data Optimizer still logs, however, logs will not be integrated into Ambari and you should access natively.

To view logs through Ambari, use the **Log Search UI** link in the **Quick Links** drop-down menu in the **Log Search** service.

![](https://github.com/pentaho/documentation/blob/main/PDC/10.2/Data%20Optimizer/PDO%20Installing%20Data%20Optimizer%20Volumes/LDO%20Install/PDSO%20Install%20in%20Hadoop%20Cluster/PDSO%20Maintain%20\(Landing%20page\)/Troubleshoot%20Data%20Storage%20Optimizer%20FS/Data%20Storage%20Optimizer%20Logging/LDO%20logging=GUID-5CBFFDD6-D401-4D22-89C3-19A573A8B9C7=1=en=Low.png)

To isolate only Data Optimizer logs, in the **Troubleshooting**and **Service Logs** tabs, include the **ldo\_volume** as part of the component. This is the default component for Data Optimizer but can be changed in `Advanced ldo-logsearch-conf` configurations.
