# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-hcp-rest.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-hcp-rest.md

# Access to HCP REST

Hitachi Content Platform (HCP) is a distributed storage system that can be used through a VFS connection in the PDI client.

Within HCP, access control lists (ACLs) grant privileges to the user to perform a variety of file operations. [Namespaces](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/System_administration/Introduction_to_Hitachi_Content_Platform/01_About_Hitachi_Content_Platform/), owned and managed by tenants, are used for logical groupings, access and permissions, and object metadata such as versioning, retention and shred settings. For more information about HCP, see the [Introduction to Hitachi Content Platform](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/Tenants_and_Namespaces/Introduction_to_Hitachi_Content_Platform).

Perform the following steps to setup access to HCP:

**Note:** The following process assumes that you have HCP tenant permissions and that namespaces have been created. For more information, see [Tenant Management Console](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/Tenants_and_Namespaces/General_administrative_information/03_Tenant_Management_Console).

**Note:** To create a successful VFS connection to HCP, object versioning must be configured in HCP [Namespaces](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/Tenants_and_Namespaces/Managing_namespaces).

1. Log on to the HCP Tenant Management Console.
2. Click **Namespaces** and then select the **Name** you want to configure.

   ![HCP Tenant Management Console](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-04ccfa45ac66944d2da343e424e608e7cbf97db3%2FPDI_HCP-DM_Dialog.png?alt=media)
3. In the **Protocols** tab, click **HTTP(S)**, and verify **Enable HTTPS** and **Enable REST API** with **Authenticated access only** are selected.
4. In the **Settings** tab, select **ACLs**.
5. Select the **Enable ACLs** check box and, when prompted, click **Enable ACLs** to confirm.

This completes the setup of HCP for accessing files in the PDI client.
