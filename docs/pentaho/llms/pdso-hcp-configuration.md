# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-configure-data-storage-optimizer/pdso-hcp-configuration.md

# Hitachi Content Platform configuration

Data Optimizer requires either Hitachi Content Platform or Virtual Storage Platform One Object.

For both Content Platform and VSP One Object, a single user defines who creates and owns all the Data Optimizer buckets. It is important for the security of the data in these buckets that the user credentials are not shared with any other application. For security, only an HDFS or Data Optimizer administrator should have access to credentials to create and define who owns the Data Optimizer buckets. The credentials are in the Data Optimizer configuration files on the HDFS DataNodes.

See the **Hitachi Content Platform** product documentation for more information.

{% hint style="info" %}
If you need to work with customer support to troubleshoot or resolve an issue, make sure that you share the Content Platform user credentials with them.
{% endhint %}

## Configure a tenant in Content Platform

To create a Content Platform tenant, you need the administrator role.

You must create a Hitachi Content Platform tenant for Data Optimizer. In most cases, Data Optimizer instances create their own buckets, so you need to properly configure namespace defaults to result in properly configured buckets.

Use the following steps to configure a tenant in Content Platform.

1. In the top-level menu of the Hitachi Content Platform System Management Console, click **Tenants**.

   The Tenants page opens.
2. On the Tenants page, click **Create Tenant**.

   The Create Tenant panel opens.
3. On the Create Tenant panel, create a tenant, making sure to:
   * Allocate enough quota for all anticipated Data Optimizer instances.
   * Enable versioning. See the **Hitachi Content Platform** product documentation for more information.
4. Use the following steps to enable the management API (MAPI), so that Data Optimizer instances can create buckets.
   1. Log into the System Management Console or Tenant Management Console using a user account with the security role.
   2. In the top-level menu of either console, select **Security** > **MAPI**.

      The Management API page opens.
   3. In the **Management API Setting** section on the Management API page, select **Enable the HCP management API**.
   4. Click **Update Settings**
5. Enable MAPI at the cluster level.
6. Use the following steps to configure namespace defaults for the tenant:
   1. From the Content Platform Tenant Management Console, select **Configuration** > **Namespace Defaults**.
   2. In the **Hard Quota** field, type a new number of gigabytes or terabytes of storage to allocate for an individual Data Optimizer instance namespace and select either GB or TB to indicate the measurement unit. The default is 50 GB. The maximum value you can specify is equal to the hard quota for the tenant.
   3. Set **Cloud Optimized** to **On**.
   4. Set **Versioning** to **On**.
   5. Enable version pruning older than 0 days.

## Create a tenant user account

Use this task in Hitachi Content Platform to create a tenant user account to be used exclusively by Data Optimizer, not by an actual user. This user owns and has exclusive data access permissions to Data Optimizer buckets.

**Note:** The tenant user must not have any administrative role in the tenant beyond administration of the buckets they own. No users should have access to the data in Data Optimizer buckets at any time for any reason except when required by customer support.

Use the following steps in the Content Platform Tenant Management Console to create a tenant user account. See the **Hitachi Content Platform** product documentation for more information.

1. Navigate to **Security** > **Users** > **Create User Account**.

   The Create User Account panel opens.
2. In the Create User Account panel, in the **Username** field, type a login account.

   Adhere to the following guidelines:

   1. Choose a name like `pdso-svc-usr`, to indicate that the user is not a person but a software service.
   2. Do not enable any administrative roles.
   3. Select **Allow namespace management**.

      You need to do this so Data Optimizer instances can create buckets.
3. Click **Create User Account**.

   The text “`Successfully created user account. Authorization token:`” is shown, followed by a text string with two values separated by a colon. The value on the left side of the text string is the base64-encoded username for the **ACCESS\_KEY** property, and the value on the right is the md5-encoded password to use for the **SECRET\_KEY** property.
4. Capture the base64-encoded username and md5-encoded password to add to the Data Optimizer configuration file.
5. Edit the `/etc/ldo`Data Optimizer configuration file and add the encoded username to the **ACCESS\_KEY** property and add the encoded password to the **SECRET\_KEY** property.
6. Save and close the configuration file.

## (Optional) Create a bucket for Data Optimizer

Use this task to manually create a bucket for the Data Optimizer instance.

{% hint style="info" %}
The best practice is to let Data Optimizer instances create their own buckets.
{% endhint %}

Perform the following steps in Hitachi Content Platform to create a bucket manually. See the **Hitachi Content Platform** documentation for more information.

1. In the Content Platform Tenant Management Console, click **Namespaces**.

   The Namespaces page opens.
2. On the Namespaces page, click **Create Namespace**.

   The Create Namespace panel opens.
3. Use the following steps to create a namespace:
   1. In the **Namespace Owner** field, specify the tenant user created in the [Create a tenant user account](https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-install-landing-page/pdso-install-in-hadoop-cluster/pdso-configure-data-storage-optimizer/pdso-hcp-configuration/hcp-tenant-user-configuration) procedure.
   2. Configure **Hard Quota** to provide adequate capacity for an individual Data Optimizer instance.
   3. Set **Cloud Optimized** to **On**.
   4. Set **Versioning** to **On**.
   5. Enable version pruning older than 0 days.
4. Use the following steps to enable an access control list (ACL):
   1. In the Tenant Management Console, click **Namespaces**.

      The Namespaces page opens.
   2. In the list of namespaces, click the name of the Data Optimizer namespace.
   3. Click the **Settings** tab.

      The Settings panel opens.
   4. On the left side of the Settings panel, click **ACLs**.

      The ACLs panel opens.
   5. In the ACLs panel, select **Enable ACLs**.

      A confirmation prompt displays.
   6. Click **Enable ACLs**.
5. Use the following steps to enable the Hitachi API for Amazon S3:
   1. In the Tenant Management Console, click **Namespaces**.

      The Namespaces page opens.
   2. In the list of namespaces, click the name of the Data Optimizer namespace.
   3. Click the **Protocols** tab.

      The Protocols panel opens.
   4. Select **Enable Hitachi API for Amazon S3**.

      **Note:** Enable HTTP only if you will not be using TLS.
   5. Click **Update Settings**.
6. Specify the namespace name in the **BUCKET** parameter of the Data Optimizer configuration file, `/etc/ldo`.
