# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/edit-configuration-files-for-users-cdp/edit-core-site-xml-file-cdp.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-pentaho-server-to-connect-to-a-hadoop-cluster/additional-configurations-for-specific-distributions-connecting-to-a-cluster/advanced-settings-for-connecting-to-cloudera-data-platform/edit-configuration-files-for-users-cdp/edit-core-site-xml-file-cdp.md

# Edit Core site XML file

If you are using a secured instance of CDP, follow these instructions to update the `core-site.xml` file.

1. Navigate to the `*&lt;username&gt;*/.pentaho/metastore/pentaho/NamedCluster/Configs/*&lt;user-defined connection name&gt;*` directory and open the `core-site.xml` file.
2. Add the following values:

   | Parameter                                        | Value                                                                               |
   | ------------------------------------------------ | ----------------------------------------------------------------------------------- |
   | **hadoop.proxyuser.oozie.hosts**                 | Set to any Oozie hosts on your instance of CDP.                                     |
   | **hadoop.proxyuser.oozie.groups**                | Set to any Oozie groups on your instance of CDP.                                    |
   | **hadoop.proxyuser.\<security\_service>.hosts**  | Set to any other proxy user hosts on your instance of CDP.                          |
   | **hadoop.proxyuser.\<security\_service>.groups** | Set to any other proxy user groups on your instance of CDP.                         |
   | **fs.s3a.access.key**                            | Set to your S3 access key if you are accessing S3 elements on your instance of CDP. |
   | **fs.s3a.secret.key**                            | Set to your S3 secret key if you are accessing S3 elements on your instance of CDP. |

   If you are connecting to CDP Public Cloud and want to use storage external to the CDP environment, use the following steps to make the necessary changes to the `core-site.xml` file.
3. (Optional, AWS only) If you are connecting to CDP Public Cloud on AWS and you are using an S3 bucket that is external to your CDP environment, do the following:
   * Replace the value of the `fs.s3a.delegation.token.binding` property with the following setting:

     ```
     <value>org.apache.hadoop.fs.s3a.auth.delegation.SessionTokenBinding</value></property>
     ```
   * Add this property:

     ```
     <property><name>fs.s3a.aws.credentials.provider</name><value>com.amazonaws.auth.InstanceProfileCredentialsProvider</value></property>
     ```

     Make sure that the file is placed in the `.aws` folder in the home directory of the gateway node with the proper credentials.
4. (Optional, Azure only) If you are connecting to CDP Public Cloud on Azure and you are using a storage account that is external to your CDP environment, do the following:

   Remove these properties:

   * `fs.azure.enable.delegation.token`
   * `fs.azure.delegation.token.provider.type`
   * `fs.azure.account.auth.type`
   * `fs.azure.account.oauth.provider.type`\
     Add these properties:
   * `fs.azure.account.auth.type.<your storage account name>.dfs.core.windows.net` with the value **SharedKey**.
   * `fs.azure.account.key.<your storage account name>.dfs.core.windows.net` with the value \<your\_storage\_account\_key>.
5. (Optional, GCP only) If you are connecting to CDP Public Cloud on GCP and you are using a bucket that is external to your CDP environment, create a custom role with the following permissions:

   ```
   storage.bucket.get, storage.objects.create, storage.objects.delete, storage.objects.get, storage.objects.getIamPolicy, storage.objects.list, storage.objects.setIamPolicy, storage.objects.update
   ```

   Assign this custom role to the data lake and log service accounts for the bucket that you want to use with Pentaho MapReduce (PMR).
6. Save and close the file.

See **Pentaho MapReduce** in the **Pentaho Data Integration** document to more information about the Pentaho MapReduce job entity.
