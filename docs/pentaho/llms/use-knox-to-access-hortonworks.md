# Source: https://docs.pentaho.com/pdia-admin/administer/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/use-knox-to-access-hortonworks.md

# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/secure-the-pentaho-system/big-data-security/how-to-enable-kerberos-authentication/use-knox-to-access-hortonworks.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/secure-the-pentaho-system/big-data-security/kerberos-authentication-versus-secure-impersonation/how-to-enable-kerberos-authentication/use-knox-to-access-hortonworks.md

# Use Knox to access CDP

Apache Knox is a gateway security tool that provides perimeter security for the Cloudera Data Platform (CDP). Knox provides secure access to the CDP components on a cluster. Connecting to a cluster using Knox provides you with a single point of access to connect to CDP services, eliminating the need to map to each service separately. If your system administrator has implemented Apache Ranger on the cluster, Pentaho will respect the policies your system administrator has set up.

As an example of a Knox deployment, the PDI client connects to Knox using a user ID and password that is registered in LDAP. Knox then authenticates to the Kerberos Key Distribution Center (KDC) with the PDI client user ID and password. Lastly, Knox authorizes with Ranger and submits the request to the cluster.

![Knox environment](https://3256662623-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FTSPdUdWBWVGi0uurnXBG%2Fuploads%2Fgit-blob-f78b1ce698fc757001db71612ed11eb7d19e5cfa%2FKnox_Environment.png?alt=media)

## Setup requirements for Knox with Pentaho

As a system or cluster administrator, you must obtain the following information and provide it to your Pentaho users:

* **Credentials**

  The cluster name, gateway URL, username, and password.
* **SSL certificate**

  The SSL certificate must be installed. The Knox URL is a secure URL. You need an SSL certificate to successfully perform operations using a Knox gateway. See [Configure SSL (HTTPS) in the Pentaho User Console and Server](https://docs.pentaho.com/pdia-admin/10.2-admin/user-security/advanced-security-providers/ssl-security#configure-ssl-https-in-the-pentaho-user-console-and-pentaho-server) for information on SSL.
* **LDAP directory server**

  Authentication with Knox is provided by an LDAP directory server. You must be able to authenticate to an LDAP server. For more information, review the articles [Switch to LDAP](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/Administer/Secure%20the%20Pentaho%20system/Secure%20the%20Pentaho%20System/User%20security/Advanced%20security%20providers/LDAP%20security/Switch%20to%20LDAP=GUID-60A43274-459A-4593-ACC1-D887E2C4BA49=5=en=.md) and [LDAP Properties](https://docs.pentaho.com/pdia-admin/10.2-admin/user-security/advanced-security-providers/ldap-security#ldap-properties).

## Hive configuration with Knox

You can configure your Hive database with Knox.

1. Open the connection to your Hive database, or review **Define data connections** in the **Install Pentaho Data Integration and Analytics** document for instructions on setting up a connection.
2. In the **Database Connection** dialog box, select **Options** in the page panel on the left to display the **Parameters** panel.
3. Enter the following parameters and values in the **Options** section and click **OK**.

   | Parameter           | Definition                 | Value                                                                                                                                 |
   | ------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
   | **httpPath**        | Path to database           | `datahub_cluster_name/cdp-proxy-api/hive`, where the `datahub_cluster_name` and `cdp-proxy-api` variables depend on your environment. |
   | **knox** (Optional) | Option to use Knox         | *true*                                                                                                                                |
   | **transportMode**   | Connection protocol to use | *http*                                                                                                                                |
   | **ssl**             | Option to use SSL          | *true*                                                                                                                                |
4. Enter `443` for the **Port Number** in the **General** tab.

You are now ready to use this connection for any Hive steps.
