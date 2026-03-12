# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/big-data-security/pentaho-and-cdp-security-big-date-security.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/pentaho-and-cdp-security-big-date-security.md

# Pentaho and CDP security

**Note:** If you are also using Knox as a gateway security tool, see [Use Knox to access CDP](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/use-knox-to-access-hortonworks) for details.

The following systems are supported for Kerberos and Knox when using Pentaho with a secured CDP cluster:

| System                                                                                                                                                         | Kerberos      | Knox          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------- |
| HDFS                                                                                                                                                           | Supported     | Supported     |
| Avro                                                                                                                                                           | Supported     | Supported     |
| OFC                                                                                                                                                            | Supported     | Not supported |
| Parquet                                                                                                                                                        | Supported     | Not supported |
| YARN                                                                                                                                                           | Supported     | Not supported |
| YARN-based Pentaho MapReduce (PMR)                                                                                                                             | Supported\*   | Not supported |
| Sqoop                                                                                                                                                          | Supported     | Not supported |
| Hive                                                                                                                                                           | Supported     | Supported     |
| YARN-based HBase                                                                                                                                               | Supported     | Supported     |
| YARN-based Hadoop job executor                                                                                                                                 | Supported     | Not supported |
| Oozie                                                                                                                                                          | Not supported | Supported     |
| Impala                                                                                                                                                         | Supported     | Supported     |
| Spark submit                                                                                                                                                   | Supported     | Not supported |
| \* You must have enough permission to write to the `/opt` directory in the HDFS root directory to run Pentaho MapReduce in the CDP Public cloud with Kerberos. |               |               |

**Note:** Per CDP support, all cluster nodes must be deployed on CentOS, which cannot be customized.
