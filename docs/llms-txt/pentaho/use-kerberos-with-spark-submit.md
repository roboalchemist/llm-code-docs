# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/use-kerberos-with-spark-submit.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/big-data-security/how-to-enable-kerberos-authentication/use-kerberos-with-spark-submit.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/use-kerberos-with-spark-submit.md

# Use Kerberos with Spark Submit

This article explains how to execute Spark Submit jobs on secure Cloudera CDP clusters using Kerberos authentication. Spark jobs can be submitted to the secure clusters by adding keytab and principal utility parameter values to the job. These values are what enable Kerberos authentication for Spark.

## Prerequisites

The following prerequisites must be completed before running the Spark jobs:

* A Spark client must be installed, Refer to the **Pentaho Data Integration** document for information on installing and configuring the Spark client to use with the Spark Submit job entry.
* The cluster must be secured with Kerberos, and the Kerberos server used by the cluster must be accessible to the Pentaho Server.
* The Pentaho computer must have Kerberos installed and configured as explained in [Set Up Kerberos for Pentaho](https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/set-up-kerberos-for-pentaho).

**Note:** A valid Kerberos ticket must already be in the ticket cache area on your client machine before you launch and submit the Spark Submit job.

## Spark Submit entry properties

<figure><img src="https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2FdaNtrjnMmsp3pxvNHdoK%2Fimage.png?alt=media&#x26;token=930c6cb5-80d0-48e9-b1f0-78ed9ffe9d10" alt=""><figcaption></figcaption></figure>

Configure your job setup with the parameters in the following table. For additional details, see Spark Submit in the **Pentaho Data Integration** document.

| Parameter                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Entry Name**           | Specify the name of the entry. You can customize this, or leave it as the default.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Spark Submit Utility** | Specify the name of the script that launches the Spark job, which is the batch/shell file name of the underlying spark-submit tool. For example, `Spark2-submit`.                                                                                                                                                                                                                                                                                                                                                                          |
| **Master URL**           | <p>Choose a master URL for the cluster from the drop-down: - <strong>yarn-cluster</strong>: Runs the driver program as a thread of the YARN application master (one of the node managers in the cluster). This option is similar to the way MapReduce works.</p><ul><li><strong>yarn-client</strong>: Runs the driver program on the YARN client. Tasks are still executing in the node managers of the YARN cluster.</li></ul>                                                                                                            |
| **Type**                 | <p>Select the file type of the Spark job you want to submit. Your job can be written in Java, Scala, or Python. The fields displayed in the <strong>Files</strong> tab will depend on what language option you select.</p><p>Python support on Windows requires Spark version 2.3.x or higher.</p>                                                                                                                                                                                                                                         |
| **Utility Parameters**   | <p>Specify the <strong>Name</strong> and <strong>Value</strong> of optional Spark configuration parameters associated with the <code>spark-defaults.conf</code> file. Add the following name and value pairs:</p><ul><li><strong>Name: <code>spark.yarn.keytab</code></strong></li></ul><p><strong>Value</strong>: File path to the <code>spark.yarn.keytab</code> file</p><ul><li><strong>Name: <code>spark.yarn.principal</code></strong></li></ul><p><strong>Value</strong>: Kerberos principal used to authenticate to the cluster</p> |
| **Enable Blocking**      | Select **Enable Blocking** to have the Spark Submit entry wait until the Spark job finishes running. If this option is not selected, the Spark Submit entry proceeds with its execution once the Spark job is submitted for execution. Blocking is enabled by default.                                                                                                                                                                                                                                                                     |

Authentication via password is not supported.
