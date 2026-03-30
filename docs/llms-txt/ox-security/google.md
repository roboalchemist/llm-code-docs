# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/registry/google.md

# Google Artifact Registry

Google Cloud Artifact Registry (GAR) is a unified registry service for managing and securing software artifacts.

GAR offers:

* **Centralized hosting** for multiple artifact types like Docker images, language-specific packages (Maven, npm, Python) and OS packages.
* **Granular access contro**l through Cloud IAM.
* **Direct integration with Google Cloud's deployment services**, such as Cloud Run and Google Kubernetes Engine (GKE).

By connecting GAR to OX Security, you have a constant connection to GAR and scanned results are displayed in the Artifact’s BOM.

<figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e91f2a84b4bbf6354361ea27d51822dad248b20d%2Fartifact%20bom.png?alt=media" alt=""><figcaption></figcaption></figure>

## Prerequisites

Ensure the following requirements are met:

* You have OX Security admin permissions to set up the connection.
* You have a Google Cloud account with permissions to create projects and API tokens.
* You have a project in Google Cloud.

## Connection overview

These steps summarize the connection process.

1. [Enable API services in Google Cloud.](#step-1-enable-api-services-in-google-cloud)
2. [Create a custom role in Google Cloud with specific permissions.](#step-2-create-a-custom-role-in-google-cloud-with-specific-permissions)
3. [Create a service account in Google Cloud.](#step-3-create-a-service-account-in-google-cloud)
4. [Create the service account API key in Google Cloud.](#step-4-create-the-service-account-api-key-in-google-cloud)
5. [Pass the credentials to OX Security](#step-5-pass-the-credentials-to-ox-security)

## Connection steps

To connect GAR to OX Security, follow these steps:

### Step 1: Enable API services in Google Cloud

1. From the dashboard, use the search bar to find **API & Services** and click **Enable API & Services**. This opens the **API Library** page.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6a025de47c23b6976a86454282c391bbec7acb47%2Fenable%20api%20services.png?alt=media" alt=""><figcaption></figcaption></figure></div>
2. From the **API Library** page, use the search bar to find **Cloud Resource Manager AP**I and click the **Cloud Resource Manager API** link.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-63ac5ea93bc768f0dbeba82867ddf991a52c532d%2Fcloud%20resource%20manager.png?alt=media" alt=""><figcaption></figcaption></figure>
3. Verify that the **API is enabled** (default). If not, click **Manage** to enable it.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-5ea4c37f7f73881150fa82c7c63d05ee879b26bf%2Fcloud%20resource%20manager%20enabled.png?alt=media" alt=""><figcaption></figcaption></figure>
4. Next, use the same search action to open the **Artifact Registry API** page and verify that it is also enabled.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9b464825f4c59504528ed106492c4869d307c7db%2Fartifact%20registry%20api%20enabled%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Step 2: Create a custom role in Google Cloud with specific permissions

1. From the Google Cloud dashboard menu, select **IAM & Admin > Roles**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-60e032992ae3f48b52317da64e57233e942d6939%2Fgoogle%20iam%20menu.png?alt=media" alt="" width="216"><figcaption></figcaption></figure></div>
2. From the **Roles** page, click **Create role**.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-3f548600fea1e05f824182bd8430f385cb07e93a%2Fcreate%20role.png?alt=media" alt=""><figcaption></figcaption></figure>
3. Enter a title and description.
   1. The ID is auto-generated.
   2. Leave the **Role launch stage** as is.

      <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6a3f572b665ff674805bc14d3246c21e3a7e0567%2Frole%20add%20permissions%20buttons.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
4. Click **Add permissions** to open a dialog box.\
   You’ll add two permissions **Artifact Registry Reader** and **resourcemanager.projects.get**.

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b4f0556efaef381a9148a3c1e36dc0f4405e1a3d%2Fpermissions%20add%20artifact%20registry.png?alt=media" alt="" width="545"><figcaption></figcaption></figure></div>
5. Locate the **Artifact Registry Reader**, activate the checkbox and click **OK**.
6. You’ll see that there are multiple pages of related permissions. To select all permissions on a specific page, activate the “master” checkbox in the header.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-454c0b0077ffe8238c593e2607e3eb98ba655f76%2Fpermissions%20add%20pemissions%20header.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
7. Use the navigation chevron at bottom to move to the next page and select all the permissions on that page.
8. Repeat until all the related permissions are selected, then click **Add**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-682bad32350ce85d72ad8dd1996e00938bd440de%2Fpermissions%20add%20permissions%20start.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
9. Next, locate the **permission resourcemanager.projects.get** and click **Add**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-63bf9dc1d9e733f459faa7903c9b1f2fc9493334%2Fresourcemanager%20get%20add.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
10. To complete and create the role, click **Create**.<br>

    <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-d9123384d305c2eb0fad7f673167e5fb79b965aa%2Fassigned%20permissions%20screen.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

***

### Step 3: Create a service account in Google Cloud

1. From **IAM & Admin / Roles**, select **Service Accounts** from the menu and click **Create service accoun**t.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-b3785ae3275b7c375754e6dcfe7161477652c65b%2Fcreate%20service%20account%20button%20(1).png?alt=media" alt=""><figcaption></figcaption></figure>
2. Enter a **Service account name** and **Service account description** (the **Service account ID** is auto-generated). Then click **Create and continue** to assign permissions to the service account.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-8eea39ea21f873f72bf2f38c933b7e8a9032c436%2Fcreate%20service%20account%20with%20details.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
3. To add the role you just created, open the **Select a role dropdown**, select **Custom**. Select the role (left screen), then click **Continue** (right screen).<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-17369d50769d14ac466af08d2e55ace42b4ada7f%2Fcreate%20service%20account%202%20screens.png?alt=media" alt=""><figcaption></figcaption></figure>
4. Leave the **Principals with access** as is. To complete the creation of the service account, click **Done**.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9f9ddbbaae1482d92cf2a9458d8a40d046ee3d1b%2Fcreate%20service%20account%20leave%20principals.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
5. To verify the service account, enter the service account name you just created in the filter.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-9f5491987d104f90f114817a6777405465b6126d%2Fservice%20account%20registry%20access%20filter.png?alt=media" alt=""><figcaption></figcaption></figure>

***

### Step 4: Create the service account API key in Google Cloud

1. Continue from the previous screen, select the service account you created and select the **Keys** tab.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-77a338494853159c87539ae486378962eb2378b7%2Fservice%20account%20keys.png?alt=media" alt=""><figcaption></figcaption></figure>
2. On the **Keys tab,** click **Add key** and select JSON as the Key type.<br>

   <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-32f67df164af20ce2ed3ffed283fe53d81f49fa1%2Fprivate%20key%20json.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
3. Read the warning about data security.

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-133577711fa0398f1778cf9a87a55ff0106ac4ba%2Fprivate%20key%20warning%20saved.png?alt=media" alt=""><figcaption></figcaption></figure>
4. To complete, click **Close**. The JSON key is now saved to your computer.

***

### Step 5: Pass the credentials to OX Security

1. Create a Base64 string including the Key and the Project name from the JSON key. There are several methods to do this. If you use [Node.js/Browser](http://node.js/Browser), here is a code example.<br>

   <figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-eca029991567b9b086e2b22d84d7ae3d557603a9%2Fbase64.png?alt=media" alt=""><figcaption></figcaption></figure>
2. Sign in to OX Security. From the **OX Connectors** page open the **GAR connector** and enter these details:
   1. **Project ID:** The ID of the project you want to scan.
   2. **API Token:** The Base64 string you created.<br>

      <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-53f5e4f7bd4d59dce5cda0be5be76e8a1b6c4b33%2Fgar%20connector%20ox%20screen.png?alt=media" alt=""><figcaption></figcaption></figure></div>
3. Click **Connect**. If the credentials are valid, a success message appears.

That’s it. OX Security is now connected to your Google Artifact Registry.

## Post-setup checks

Use either or both of these steps.

* From the OX Connectors page open the GAR connector and click **Verify Connectivity**.
* From the same screen, click **Settings**. This displays a list of all images.

## Logs and alerts

If your credentials are not accepted, an error message shows on the connection screen.

## Troubleshooting

If your credentials are valid but you can’t connect to GAR, reach out to Customer Support.

## Disconnection

To disconnect, open the GAR connector and select **DELETE**.

To reconnect, re-enter the Project ID and API token.

<br>
