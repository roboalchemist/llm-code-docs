# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/supported-components.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/big-data-security/supported-components.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/supported-components.md

# Supported components

These components are currently only supported for secure impersonation.

| Component                                                                                                                                                   | Secure Impersonation Support? |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| Cloudera-Impala                                                                                                                                             | Yes                           |
| HBase                                                                                                                                                       | Yes                           |
| HDFS                                                                                                                                                        | Yes                           |
| Hadoop MapReduce                                                                                                                                            | Yes                           |
| Hive                                                                                                                                                        | Yes                           |
| Oozie                                                                                                                                                       | Yes                           |
| Pentaho MapReduce (PMR)**Note:** When running a Pentaho Map Reduce job, you can securely connect to Hive and HBase within the mapper, reducer, or combiner. | Yes                           |
| Carte on Yarn                                                                                                                                               | No                            |
| Impala                                                                                                                                                      | No                            |
| Sqoop                                                                                                                                                       | No                            |
| Spark SQL                                                                                                                                                   | No                            |

Secure impersonation directly from the following is not supported:

* PDI client
* Scheduled Jobs and Transformations
* Pentaho Report Designer
* Pentaho Metadata Editor
* Kitchen
* Pan
* Carte

When you run a transformation or job to run against the cluster from the PDI client, you cannot use secure impersonation. However, if you execute that job or transformation you created in the PDI client from the Pentaho Server, then you can use secure impersonation.
