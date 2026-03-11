# Source: https://docs.axonius.com/docs/docusign.md

# DocuSign

DocuSign helps organizations connect and automate how they prepare, sign, act on, and manage agreements.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Roles
* Groups
* Licenses
* Application Settings
* SaaS data

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the DocuSign server. This is usually `http://account.docusign.com`.
2. **User ID** - The DocuSign User ID.
3. **API Account ID** *(required)* - Specify the API Account ID. To generate the API Account ID, see [Create API Account ID and Keys](/docs/docusign#create-api-account-id-and-keys).
4. **Account Base URI** *(optional)* - Enter the identifier of the resource to use. To generate the Account Base URI, see [Create API Account ID and Keys](/docs/docusign#create-api-account-id-and-keys).
5. **Integration Key**  *(required)* - Enter the integration key. To generate the Integration Key, see [Create API Account ID and Keys](/docs/docusign#create-api-account-id-and-keys).
6. **Private Key File** *(required)* - Select to upload a private key file. To generate a private key, see [Create API Account ID and Keys](/docs/docusign#create-api-account-id-and-keys).
7. **Fetch DocuSign CLM Licenses** *(optional)* - Enrich users with permission profiles.
8. **Organization ID** - When the 'Fetch DocuSign CLM Licenses' is enabled, add DocuSign Organization ID.

<Callout icon="📘" theme="info">
  Note

  When this option is enabled, the `user_read` scope must be added to authentication scopes.
</Callout>

9. **Verify SSL**  - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.
10. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
11. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
12. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="DocuSignSM" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DocuSignSM.png" />

### Create a Permission Profile in DocuSign

<Callout icon="📘" theme="info">
  Note

  This  is only needed for retrieving SaaS data.
</Callout>

Create a custom permission profile in DocuSign to provide the Axonius account with the least privileges permission.

1. From the account admin console in DocuSign, select the **Settings** tab, and under **Users and Groups**, select **Permission Profiles**.
2. Click **Add Permission Profile**. The **Add Permission Profile** window is displayed.
3. Enter a name for the permission profile.
4. Under the **Admin Permissions** tab, click **Allow Some** and select the following permission levels.

| Permission         | Level of Access |
| ------------------ | --------------- |
| Users and Groups   | View Only       |
| Envelope Sharing   | View & Edit     |
| Document Retention | View & Edit     |
| Account Settings   | View & Edit     |
| Security Settings  | View & Edit     |

5. Under the **Admin Permissions** tab, keep all options as defined by default.

6. Click **Add**.

### Exclude your User Account from 2FA

<Callout icon="📘" theme="info">
  Note

  This is only needed for retrieving SaaS data.
</Callout>

1. Log in with the user account you created for Axonius in DocuSign.

2. Click the user profile icon (avatar), and then click on **Manage Profile**.
   The **My Profile** view is displayed.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-XFZXCPJX.png)

3. From the left navigation menu, click on the **Privacy & Security** menu.

4. Under the **Sign-In Security** section, disable the **Passwordless Login** and the **Two-Step Verification** options.

5. Under the **Device Security** section, disable the **New Device Verification** option.

6. Make sure no **App Password** is generated. If such exists, revoke it.

### Create API Account ID and Keys

**To create the API Account ID, Account Base URI, Integration Key, and Private Key**

<Callout icon="📘" theme="info">
  Note

  Initial consent in DocuSign is required for setup of this adapter, in some of the configurations.
</Callout>

1. Create a DocuSign Developer Account by navigating to [Get your Free Developer Account](https://go.docusign.com/o/sandbox/) and filling-in your details.

2. From the **Settings** tab, under **Integrations**, select **Apps and Keys**.

3. Click **Add App and Integration Key**. The Add Integration Key window is displayed.

4. Click the Copy icon to copy the Integration Key for later use.

5. In **App Name**, specify the name of the app and click **Create App**. The Authentication window is displayed.

6. Under **User Application**, select **No**.

7. Fill in the redirect URI with the following value: `http://localhost/adapters/docusign_adapter`

8. In the **Additional settings** section, under **Allowed HTTP Methods**, select  **GET**.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AllowedHTTPMethods.png)

9. Copy the User ID, API Account ID, and Account Base URI for later use.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DocusingCreds.png)

10. Navigate to your browser and access this URL template (replace the UPPERCASE values with your actual integration key): `https://account-d.docusign.com/oauth/auth?response_type=token&scope=signature&client_id=YOUR_INTEGRATION_KEY&redirect_uri=http://localhost/adapters/docusign_adapter`

11. Follow the prompt to log in.

12. Click **Allow Access** to permit the app to make calls. The browser redirects to the `localhost` URL.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Docusign-Access.png)

13. In the URL in the browser's Address bar, copy the value of the `ACCESS_TOKEN` parameter.
    For example: `https://localhost/adapters/docusign_adapter#access_token=ACCESS_TOKEN&expires_in=28800&token_type=bearer&scope=signature`

14. Using the Access Token, API Account ID, and Account Base URI values that you copied earlier, run this curl command at least 20 times before the `ACCESS_TOKEN` expires.
    Please allow up to thirty minutes for this to register in the Docusign console. A successful output will include a ‘remaining requests’ value that decreases with each run.

Linux/OSX:

```
curl -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -i "ACCOUNT_BASE_URI/restapi/v2.1/accounts/API_ACCOUNT_ID"
```

Windows:

```
curl.exe -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -i "ACCOUNT_BASE_URI/restapi/v2.1/accounts/API_ACCOUNT_ID"
```

<Callout icon="📘" theme="info">
  Note

  You can use the following script to automatically repeat the command. Insert the correct values into the variables at the beginning and run `chmod +x loop_curl.sh`. To execute, use `./loop_curl.sh`).

  ```shell
  #!/bin/bash

  # Define the required variables
  ACCESS_TOKEN="your_access_token_here"
  ACCOUNT_BASE_URI="your_account_base_uri_here"
  API_ACCOUNT_ID="your_api_account_id_here"

  # Run the curl command 25 times
  for i in {1..25}
  do
      curl -H "Content-Type: application/json" -H "Authorization: Bearer $ACCESS_TOKEN" -i "$ACCOUNT_BASE_URI/restapi/v2.1/accounts/$API_ACCOUNT_ID"
      sleep 10 # Sleeping for 10 seconds between requests.
  done
  ```
</Callout>

After the Docusign console reflects the successful connections, the app is approved and you can promote it to production.

14. Promote the App to live:

15. Navigate to **Action > Select Go Live Location**.

16. Choose the relevant production account.

17. After verifying that the new app appears in your DocuSign account, repeat **Steps 2 -6**.

18. Under **Service Integration**, select **Generate RSA** to generate the public and private keys. The RSA Keypair page generates a public key and a private key. Save the values for later use.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Docusign%20-%20GenerateRSA.png)

19. Paste the private key into a .pem file, which you will need to retrieve later. The file must be in a Linux or MAC format with LF as the end of  line sequence. This RSA key is the Private Key file for the Axonius Configuration.

20. In the **Additional settings** section,  **Add URIs**.

21. In the **Redirects URIs** field, enter `https://localhost/adapters/docusign_adapter`.

22. In the  Additional settings section under **Allowed HTTP Methods** select  **GET**, **POST**.

23. The **My Account Information** now shows the User ID,  API Account ID,  and Account Base URI.

24. Copy the User ID, Account ID, and Account Base URI from the ‘live’/production app and paste the values into their corresponding fields in Axonius’s Docusign Adapter Connection configuration.
    ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DocusingCreds.png)

25. Click **Save** or **Save and Fetch**.

26. The adapter will produce an error message containing a URL.
    Follow this URL to perform the final Authentication in a web browser.

Refer to these resources for additional information:
[Getting an Access Token using Auth Code Grant](https://www.youtube.com/watch?v=4cn7Mvmq0Lo\&t=273s)

[How to get an access token with Implicit Grant](https://developers.docusign.com/platform/auth/implicit/implicit-get-token/)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **User Status Filter** - Select a status to filter users by: Active, Closed, or Activation Sent.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in the [User ID](#parameters) must have write permissions in order to fetch SaaS data.

## Troubleshooting

When connecting the adapter the first time, an error message with a link is displayed.
**To resolve the connection issue**

1. Copy the link to a browser and click **Allow**.
2. In the **Host Name or IP Address** parameter, specify: your Account ID at DocuSign followed by docusign.com.
3. Click **Save and Fetch** to reconnect. The adapter is subsequently connected.

## Supported From Version

Supported from version 5.0