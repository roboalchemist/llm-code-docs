# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/troubleshooting-overview-cp.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp.md

# Troubleshoot the Pentaho system

As a best practice, your initial approach for troubleshooting components within Pentaho should be to use logging to monitor operations within transformations, jobs, database connections, and the server. You can monitor transformations, jobs, and database connections through [logging in PDI](https://docs.pentaho.com/pdia-admin/10.2-admin/optimize-the-pentaho-system/monitoring-system-performance/pdi-logging). For the Pentaho Server, the log file is `pentaho.log`, which is in the `pentaho-server/logs` folder. The contents of this file can help you track down why the server failed to start or work properly.

**Note:** If you used a manual install with your own Tomcat web application server, `pentaho.log` resides under `pentaho-server/tomcat/logs`.

Besides analyzing logs, a number of Pentaho customers and partners have posted problems and solutions they have encountered in the past. The following common categories contain descriptions of these problems and how to resolve them:

* [**General issues**](https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/general-issues)

  Common general software issues associated with the Pentaho
* [**Security issues**](https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/security-issues)

  Log file output, signs of configuration errors, and possible issues during LDAP configuration
* [**Pentaho Server issues**](https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-server-issues)

  Common issues associated with the Pentaho Server
* [**Pentaho Repository issues**](https://docs.pentaho.com/pdia-admin/10.2-admin/troubleshooting-overview-cp/pentaho-repository-issues)

  Common issues associated with the Pentaho Repository
