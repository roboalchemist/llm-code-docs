# Source: https://docs.unstructured.io/ui/sources/onedrive.md

# Source: https://docs.unstructured.io/ui/destinations/onedrive.md

# Source: https://docs.unstructured.io/open-source/ingestion/destination-connectors/onedrive.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/onedrive.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/onedrive.md

# Source: https://docs.unstructured.io/api-reference/workflow/sources/onedrive.md

# Source: https://docs.unstructured.io/api-reference/workflow/destinations/onedrive.md

# OneDrive

<Note>
  If you're new to Unstructured, read this note first.

  Before you can create a destination connector, you must first sign in to your Unstructured account:

  * If you do not already have an Unstructured account, [sign up for free](https://unstructured.io/?modal=try-for-free).
    After you sign up, you are automatically signed in to your new Unstructured **Let's Go** account, at [https://platform.unstructured.io](https://platform.unstructured.io).
    To sign up for a **Business** account instead, [contact Unstructured Sales](https://unstructured.io/?modal=contact-sales), or [learn more](/api-reference/overview#pricing).
  * If you already have an Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business SaaS** account and are not already signed in, sign in to your account at
    [https://platform.unstructured.io](https://platform.unstructured.io). For other types of **Business** accounts, see your Unstructured account administrator for sign-in instructions,
    or email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  After you sign in, the [Unstructured user interface](/ui/overview) (UI) appears, which you use to get your Unstructured API key.

  1. After you sign in to your Unstructured **Let's Go**, **Pay-As-You-Go**, or **Business** account, click **API Keys** on the sidebar.<br />

     For a **Business** account, before you click **API Keys**, make sure you have selected the organizational workspace you want to create an API key
     for. Each API key works with one and only one organizational workspace. [Learn more](/ui/account/workspaces#create-an-api-key-for-a-workspace).

  2. Click **Generate API Key**.<br />

  3. Follow the on-screen instructions to finish generating the key.<br />

  4. Click the **Copy** icon next to your new key to add the key to your system's clipboard. If you lose this key, simply return and click the **Copy** icon again.<br />

  After you create the destination connector, add it along with a
  [source connector](/api-reference/workflow/sources/overview) to a [workflow](/api-reference/workflow/overview#workflows).
  Then run the worklow as a [job](/api-reference/workflow/overview#jobs). To learn how, try out the
  [hands-on Workflow Endpoint quickstart](/api-reference/workflow/overview#quickstart),
  go directly to the [quickstart notebook](https://colab.research.google.com/github/Unstructured-IO/notebooks/blob/main/notebooks/Unstructured_Platform_Workflow_Endpoint_Quickstart.ipynb),
  or watch the two 4-minute video tutorials for the [Unstructured Python SDK](/api-reference/workflow/overview#unstructured-python-sdk).

  You can also create destination connectors with the Unstructured user interface (UI).
  [Learn how](/ui/destinations/overview).

  If you need help, email Unstructured Support at [support@unstructured.io](mailto:support@unstructured.io).

  You are now ready to start creating a destination connector! Keep reading to learn how.
</Note>

Send processed data from Unstructured to OneDrive.

The requirements are as follows.

* A OneDrive for business plan, or a Microsoft 365 or Office 365 Business or enterprise plan that includes OneDrive.
  [Learn more](https://www.microsoft.com/microsoft-365/onedrive/compare-onedrive-plans).
  [Shop for business plans](https://www.microsoft.com/microsoft-365/business/compare-all-microsoft-365-business-products).
  [Shop for enterprise plans](https://www.microsoft.com/microsoft-365/enterprise/microsoft365-plans-and-pricing).
  OneDrive personal accounts, and Microsoft 365 Free, Basic, Personal, and Family plans are not supported.

* A SharePoint Online plan, or a Microsoft 365 or Office 365 Business or enterprise plan that includes SharePoint Online.
  (Even if you only plan to use OneDrive, you still need a plan that includes SharePoint Online, because OneDrive is built on SharePoint technology.)
  [Learn more](https://www.microsoft.com/en-us/microsoft-365/SharePoint/compare-SharePoint-plans).
  [Shop for business plans](https://www.microsoft.com/microsoft-365/business/compare-all-microsoft-365-business-products).
  [Shop for enterprise plans](https://www.microsoft.com/microsoft-365/enterprise/microsoft365-plans-and-pricing).

* The OneDrive and SharePoint Online plans must share the same Microsoft Entra ID tenant.
  [Learn more](https://learn.microsoft.com/microsoft-365/enterprise/subscriptions-licenses-accounts-and-tenants-for-microsoft-cloud-offerings?view=o365-worldwide).

* The path to the target OneDrive folder, starting from the OneDrive account's root folder, for example `my-folder/my-subfolder`.

  The following video shows how to get a path:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/SfUA1IwtI5U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* Two types of authentication are supported: client credentials, and a username and password. Both authentication types require a Microsoft Entra ID app registration.

  <Note>
    The OneDrive connector does not support any other authentication methods, such as multifactor (MFA) or passwordless authentication.
  </Note>

  You will need to provide the **Application (client) ID**, **Directory (tenant) ID**, and **Client secret** for the Entra ID app registration that has access to the target OneDrive account, and
  the app registration must have the correct set of Microsoft Graph access permissions. These permissions include:

  * `Files.ReadWrite.All` (if both reading and writing are needed)

  * `Sites.ReadWrite.All` (if both reading and writing are needed)

  * `User.Read.All`

  * `Directory.Read.All`

  1. [Create an Entra ID app registration](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app?pivots=portal).
  2. [Add Graph access permissions to an app registration](https://learn.microsoft.com/entra/identity-platform/howto-update-permissions?pivots=portal#add-permissions-to-an-application).
  3. [Grant consent for the added Graph permissions](https://learn.microsoft.com/entra/identity-platform/howto-update-permissions?pivots=portal#grant-consent-for-the-added-permissions-for-the-enterprise-application).

  The following video shows how to create an Entra ID app registration:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/aBAY-LKLPSo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

  The following video shows how to add the correct set of Graph access permissions to the Entra ID app registration:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/jBJsrSkpClo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* Both authentication types also require the User Principal Name (UPN) for the OneDrive account. This is typically the OneDrive account user's email address. To find a UPN:

  1. Depending on your plan, sign in to your Microsoft 365 admin center (typically [https://admin.microsoft.com](https://admin.microsoft.com)) using your administrator credentials,
     or sign in to your Office 365 portal (typically [https://portal.office.com](https://portal.office.com)) using your credentials.
  2. In the **Users** section, click **Active users**.
  3. Locate the user account in the list of active users.
  4. The UPN is displayed in the **Username** column.

  The following video shows how to get a UPN:

  <iframe width="560" height="315" src="https://www.youtube.com/embed/H0yYfhfyCE0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

* For username and password authentication, you will also need the password for the target UPN.

To create a OneDrive destination connector, see the following examples.

<CodeGroup>
  ```python Python SDK theme={null}
  import os

  from unstructured_client import UnstructuredClient
  from unstructured_client.models.operations import CreateDestinationRequest
  from unstructured_client.models.shared import CreateDestinationConnector

  with UnstructuredClient(api_key_auth=os.getenv("UNSTRUCTURED_API_KEY")) as client:
      response = client.destinations.create_destination(
          request=CreateDestinationRequest(
              create_destination_connector=CreateDestinationConnector(
                  name="<name>",
                  type="onedrive",
                  config={
                      "client_id": "<client-id>",
                      "user_pname": "<user-pname>",
                      "password": "<password>",  # For username and password authentication
                      "tenant": "<tenant>",
                      "authority_url": "<authority-url>",
                      "client_cred": "<client-cred>",
                      "remote_url": "<remote-url>"
                  }
              )
          )
      )

      print(response.destination_connector_information)
  ```

  ```bash curl theme={null}
  curl --request 'POST' --location \
  "$UNSTRUCTURED_API_URL/destinations" \
  --header 'accept: application/json' \
  --header "unstructured-api-key: $UNSTRUCTURED_API_KEY" \
  --header 'content-type: application/json' \
  --data \
  '{
      "name": "<name>",
      "type": "onedrive",
      "config": {
          "client_id": "<client-id>", 
          "user_pname": "<user-pname>",
          "password": "<password>", # For username and password authentication.
          "tenant": "<tenant>", 
          "authority_url": "<authority-url>",
          "client_cred": "<client-cred>",
          "remote_url": "<remote-url>" 
      }
  }'
  ```
</CodeGroup>

Replace the preceding placeholders as follows:

* `<name>` (*required*) - A unique name for this connector.
* `<client-id>` (*required*) - The application (client) ID of the Microsoft Entra ID app registration that has access to the OneDrive account.
* `<user-pname>` (*required*) - The User Principal Name (UPN) for the OneDrive user account in Entra ID. This is typically the user's email address.
* `<password>` (*required* for username and password authentication): The password for the target UPN.
* `<tenant>` (*required*) - The directory (tenant) ID of the Entra ID app registration.
* `<authority-url>` (*required*) - The authentication token provider URL for the Entra ID app registration. The default is [https://login.microsoftonline.com](https://login.microsoftonline.com).
* `<client-cred>` (*required*) - The client secret for the Entra ID app registration.
* `<path>` (source connector only) - The path to the target folder in the OneDrive account, starting with the account's root folder, for example `my-folder/my-subfolder`.
* For `recursive` (source connector only), set to `true` to recursively access files from subfolders within the specified OneDrive `<path>`. The default is `false` if not otherwise specified.
* `<remote-url>` (destination connector only) - `onedrive://`, followed by the path to the target folder in the OneDrive account, starting with the account's root folder, for example `onedrive://my-folder/my-subfolder`.
