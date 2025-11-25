# Source: https://docs.unstructured.io/ui/sources/sharepoint.md

# Source: https://docs.unstructured.io/open-source/ingestion/source-connectors/sharepoint.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/sharepoint.md

# SharePoint

<Note>
  If you're new to Unstructured, read this note first.

  Before you can create a source connector, you must first sign in to your Unstructured account:

  * If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
    After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).
    To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
  * If you already have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at
    [https://platform.unstructured.io](https://platform.unstructured.io). For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
    or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  After you sign in, the [Unstructured user interface](/ui/overview) (UI) appears, which you use to get your Unstructured API key, as follows:

  1. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).

  2. Click **Generate API Key**.<br />

  3. Follow the on-screen instructions to finish generating the key.<br />

  4. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

  After you create the source connector, add it along with a
  [destination connector](/api-reference/workflow/destinations/overview) to a [workflow](/api-reference/workflow/overview#workflows).
  Then run the worklow as a [job](/api-reference/workflow/overview#jobs). To learn how, try out the
  [hands-on Workflow Endpoint quickstart](/api-reference/workflow/overview#quickstart),
  go directly to the [quickstart notebook](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Unstructured_Platform_Workflow_Endpoint_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create source connectors with the Unstructured user interface (UI).
  [Learn how](/ui/sources/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a source connector! Keep reading to learn how.
</Note>

Ingest your files into Unstructured from SharePoint.

The requirements are as follows.

<Note>
  If you are setting up the SharePoint connector for the first time, you can skip past this note.

  Previous versions of the SharePoint connector relied on SharePoint app principals for authentication. Current versions of the
  SharePoint connector no longer support these SharePoint app principals. Microsoft deprecated support for Share Point app principals on November 27, 2023.
  SharePoint app principals will no longer work for SharePoint tenants that were created on or after November 1, 2024, and they will stop working
  for all SharePoint tenants as of April 2, 2026. [Learn more](https://learn.microsoft.com/sharepoint/dev/sp-add-ins/retirement-announcement-for-azure-acs).

  Current versions of the SharePoint connector now rely on Microsoft Entra ID app registrations for authentication.

  To migrate from SharePoint app princpals to Entra ID app regisrations, replace the following settings in your existing SharePoint connector,
  as listed in the requirements following this note:

  * Replace the deprecated SharePoint app principal's application client ID value with your replacement Entra ID app registration's **Application (client) ID** value.
  * Replace the deprecated SharePoint app principal's client secret value with your replacement Entra ID app registration's **Client secret** value.
  * Add your replacement Entra ID app registration's **Directory (tenant) ID** value, token authority URL value, and the correct set of Microsoft Graph access permissions for SharePoint Online.

  If you need migration help, get assistance from our [Slack community](https://short.unstructured.io/pzw05l7), or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).
</Note>

* A SharePoint Online plan, or a Microsoft 365 or Office 365 Business or enterprise plan that includes SharePoint Online.
  [Learn more](https://www.microsoft.com/en-us/microsoft-365/SharePoint/compare-SharePoint-plans).
  [Shop for business plans](https://www.microsoft.com/microsoft-365/business/compare-all-microsoft-365-business-products).
  [Shop for enterprise plans](https://www.microsoft.com/microsoft-365/enterprise/microsoft365-plans-and-pricing).

* A OneDrive for business plan, or a Microsoft 365 or Office 365 Business or enterprise plan that includes OneDrive.
  (Even if you only plan to use SharePoint Online, you still need a plan that includes OneDrive, because the SharePoint connector is built on OneDrive technology.)
  [Learn more](https://www.microsoft.com/microsoft-365/onedrive/compare-onedrive-plans).
  [Shop for business plans](https://www.microsoft.com/microsoft-365/business/compare-all-microsoft-365-business-products).
  [Shop for enterprise plans](https://www.microsoft.com/microsoft-365/enterprise/microsoft365-plans-and-pricing).
  OneDrive personal accounts, and Microsoft 365 Free, Basic, Personal, and Family plans are not supported.

* The SharePoint Online and OneDrive plans must share the same Microsoft Entra ID tenant.
  [Learn more](https://learn.microsoft.com/microsoft-365/enterprise/subscriptions-licenses-accounts-and-tenants-for-microsoft-cloud-offerings?view=o365-worldwide).

* The SharePoint Online site URL.

  * Site collection-level URLs typically have the format `https://<tenant>.sharepoint.com/sites/<site-collection-name>`.
  * Root site collection-level URLs typically have the format `https://<tenant>.sharepoint.com`.
  * To process all sites within a SharePoint tenant, use a site URL of `https://<tenant>-admin.sharepoint.com`.

  [Learn more](https://learn.microsoft.com/microsoft-365/community/query-string-url-tricks-sharepoint-m365).

* The display name of the SharePoint Online library to use. The default is `Documents`.

* The path to the SharePoint Online library to use. By default, the root of the target library is used.
  To start from a path other than the root, enter the path that you want to use, beginning from the root. For example, to use
  the **my-folder > my-subfolder** path in the target library, you would specify `my-folder/my-subfolder`.

  The following video shows how to get the site URL and a path within the site:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/E3fRwJU-KTc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* Two types of authentication are supported: client credentials and a username and password. Both authentication types require a
  Microsoft Entra ID app registration. You will need to provide
  the **Application (client) ID**, **Directory (tenant) ID**, and **Client secret** for the Entra ID app registration, and the
  app registration must have the correct set of Microsoft Graph access permissions. These permissions include:

  * `Sites.ReadWrite.All` (if both reading and writing are needed)
  * `User.Read.All`
    [Learn more](https://learn.microsoft.com/answers/questions/2116616/service-principal-access-to-sharepoint-online).

  1. [Create an Entra ID app registration](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app?pivots=portal).
  2. [Add Graph access permissions to an app registration](https://learn.microsoft.com/entra/identity-platform/howto-update-permissions?pivots=portal#add-permissions-to-an-application).
  3. [Grant consent for the added Graph permissions](https://learn.microsoft.com/entra/identity-platform/howto-update-permissions?pivots=portal#grant-consent-for-the-added-permissions-for-the-enterprise-application).

  The following video shows how to create an Entra ID app registration:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/aBAY-LKLPSo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  The following video shows how to add the correct set of Graph access permissions to the Entra ID app registration:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/X7fnRYyxy0Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* The token authority URL for your Microsoft Entra ID app registration. This is typically `https://login.microsoftonline.com`

* For username and password authentication, you must also provide the User Principal Name (UPN) and its password for the OneDrive account in the Microsoft Entra ID tenant. This UPN is typically the OneDrive account user's email address. To find a UPN:

  1. Depending on your plan, sign in to your Microsoft 365 admin center (typically [https://admin.microsoft.com](https://admin.microsoft.com)) using your administrator credentials,
     or sign in to your Office 365 portal (typically [https://portal.office.com](https://portal.office.com)) using your credentials.
  2. In the **Users** section, click **Active users**.
  3. Locate the user account in the list of active users.
  4. The UPN is displayed in the **Username** column.

  The following video shows how to get a UPN:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/H0yYfhfyCE0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

To create a SharePoint source connector, see the following examples.

<CodeGroup>
  ```python Python SDK theme={null}
  import os

  from unstructured_client import UnstructuredClient
  from unstructured_client.models.operations import CreateSourceRequest
  from unstructured_client.models.shared import CreateSourceConnector

  with UnstructuredClient(api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")) as client:
      response = client.sources.create_source(
          request=CreateSourceRequest(
              create_source_connector=CreateSourceConnector(
                  name="<name>",
                  type="sharepoint",
                  config={
                      "site": "<site>",
                      "library": "<library>",
                      "path": "<path>",
                      "recursive": <True|False>,
                      "client_id": "<client_id>",
                      "tenant": "<tenant>",
                      "authority_url": "<authority_url>",
                      "client_cred": "<client_cred>",
                      "user_pname": "<user_pname>", # For username and password authentication.
                      "password": "<password>" # For username and password authentication.
                  }
              )
          )
      )

      print(response.source_connector_information)
  ```

  ```bash curl theme={null}
  curl --request 'POST' --location \
  "$UNSTRUCTURED_API_URL/sources" \
  --header 'accept: application/json' \
  --header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
  --header 'content-type: application/json' \
  --data \
  '{
      "name": "<name>",
      "type": "sharepoint",
      "config": {
          "site": "<site>",
          "library": "<library>",
          "path": "<path>",
          "recursive": <true|false>,
          "client_id": "<client-id>",
          "tenant": "<tenant>",
          "authority_url": "<authority-url>",
          "client_cred": "<client-cred>",
          "user_pname": "<user-pname>", # For username and password authentication.
          "password": "<password>" # For username and password authentication.
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<site>` (*required*) - The base URL of the SharePoint site to connect to.
* `<library>` - The display name of the SharePoint library to use. The default is `Documents`.
* `<path>` - The path to use within the library. The default is the root of the target library. To use a different path, specify the correct path format as described previously in this article.
* For `recursive`, set to `true` to recursively process data from subfolders within the target path. The default is `false` if not otherwise specified.
* `<client-id>` (*required*) - The client ID provided by SharePoint for the app registration.
* `<tenant>` (*required*) - The **Directory (tenant) ID** for the Microsoft Entra ID app registration with the correct set of Microsoft Graph access permissions.
* `<authority-url>` - The authentication token provider URL for the Entra ID app registration. The default is [https://login.microsoftonline.com](https://login.microsoftonline.com).
* `<client-cred>` (*required*) - The **Client secret** for the Entra ID app registration.
* `<user-pname>` (*required* for username and password authentication) - For username and password authentication, the UPN for the OneDrive account in the Entra ID tenant.
* `<password>` (*required* for username and password authentication) - For username and password authentication, the password for the target UPN.
