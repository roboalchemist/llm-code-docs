# Source: https://docs.axonius.com/docs/aam-installation-and-configuration.md

# AAM Installation and Configuration

Axonius uses the Agentless AAM method (called Central Credential Provider (CCP)) to integrate with CyberArk.
In the below section, the term “Application” refers, in this case, to Axonius.

<Callout icon="📘" theme="info">
  NOTE

  License for Central Credential Provider (CCP) is a prerequisite for CyberArk integration
</Callout>

### Central Credentials Provider Installation

* For installation and configuration, please refer to the CyberArk’s “Central Credential Provider Implementation guide”.
* No specific steps are required to configure Central Credential Provider (CCP) with Axonius.

### Defining the Application ID (APPID) and Authentication Details

To define the Application, here are the instructions to define it manually via CyberArk’s PVWA (Password Vault Web Access) Interface:

1. While logged in as a user allowed to manage applications (this requires Manage Users authorization), click Add Application in the Applications tab;  the **Add Application** page appears.
   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(120\).png)

2. Specify the following information:

   * In the Name edit box, specify the unique name (ID) of the application. The recommended Application ID for this integration is:  **APPID** = Axonius
   * In the Description, specify a short description of the application that will help you identify it.
   * In the Business owner section, specify contact information about the application’s Business owner.
   * In the lowest section, specify the Location of the application in the Vault hierarchy. If a Location is not selected, the application will be added in the same Location as the user who is creating this application.

3. Click **Add**; the application is added and is displayed in the Application Details
   page.

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(121\).png)

   * **Allowing extended authentication restrictions**.  This enables you to specify an unlimited number of machines and Windows domain OS users for a single application.

4. Specify the application’s **Authentication** details. This information enables the Credential Provider to check certain application characteristics before retrieving the application password.

5. In the Authentication tab, click **Add**; a drop-down list of authentication characteristics is displayed.

   * Protect the Application ID with a client certificate serial number. Specify the Certificate Serial number:
     ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(122\).png)

### Provisiong Accounts and Setting Permissions for Application Access

For the application to perform its functionality or tasks, the application must have access to particular existing accounts, or new accounts to be provisioned in CyberArk Vault (Step 1). Once the accounts are managed by CyberArk, make sure to setup the access to both the application and CyberArk Application Password Providers serving the Application (Step 2).

1. In the Password Safe, provision the privileged accounts that will be required by the application. You can ¬do this in either of the following ways:

   * **Manually** – Add accounts manually one at a time, and specify all the account details.

   * **Automatically** – Add multiple accounts automatically using the Password Upload feature.

   For this step, the **Add accounts** authorization in the Password Safe is required.
   For more information about adding and managing privileged accounts, refer to [https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Adding-Accounts.htm?Highlight=adding%20accounts](https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Adding-Accounts.htm?Highlight=adding%20accounts)

2. Add the Credential Provider and application users as members of the Password Safes where the application passwords are stored. This can either be done manually in the Safes tab, or by specifying the Safe names in the CSV file for adding multiple applications.

   1. Add the Provider user as a Safe Member with the following authorizations:
      * List accounts
      * Retrieve accounts
      * View Safe Members
        **Note**: When installing multiple Providers for this integration, it is recommended to create a group for them, and to then add the group to the Safe with the above authorization.

        ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(126\).png)

   2. Add the application (the APPID) as a Safe Member with the following authorizations:
      * Retrieve accounts

        ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(125\).png)

   3. If your environment is configured for dual control:
      * In PIM-PSM environments (v7.2 and lower), if the Safe is configured to require confirmation from authorized users before passwords can be retrieved, give the Provider user and the application the following permission:
        * Access Safe without Confirmation
      * In Privileged Account Security solutions (v8.0 and higher), when working with dual control, the Provider user can always access without confirmation, thus, it is not necessary to set this permission.

   4. If the Safe is configured for object level access, make sure that both the Provider user and the application have access to the password(s) to retrieve.

   For more information about configuring Safe Members, refer to the **CyberArks' Privileged Access Security Implementation Guide.**