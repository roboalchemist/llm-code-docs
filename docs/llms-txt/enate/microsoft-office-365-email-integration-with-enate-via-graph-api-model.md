# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/microsoft-office-365-email-integration-with-enate-via-graph-api-model.md

# Microsoft Office 365 Email Integration with Enate via Graph API model

You can sync Enate to Microsoft Office 365 email boxes and pull emails into Enate without needing to use POP3 or IMAP protocols via Graph API Integration. Read below to find out how to go about this.

## Register with Azure AD <a href="#quickstart-register-an-application-with-the-microsoft-identity-platform" id="quickstart-register-an-application-with-the-microsoft-identity-platform"></a>

To configure integration between Enate and Office 365, each unique Enate instance must be registered with the Microsoft Identity Platform in the Azure AD of the Office 365 tenant to which you need to establish connectivity.

To create the “App Registration” please follow the guide from Microsoft at <https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app>.

When configuring the Enate App Registration the supported account types option should be chosen based on the mailboxes you wish to access. No redirect URI is required.

Once the App Registration is complete you must add credentials and setup permissions.

To add the required permissions follow the guide at <https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#add-permissions-to-access-web-apis>. The only required API permission is an Application permission of Microsoft Graph\Mail.ReadWrite. It is important to select an “Application permission” and not a “Delegated permission”. Be sure to grant admin consent for the permission within the Azure AD tenant.

To create a credential follow the guide at <https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-configure-app-access-web-apis#add-credentials-to-your-web-application>. Enate supports Client Secrets and Certificates.

Finally to restrict the App Registration to only accessing certain mailboxes (strongly recommended) follow the Microsoft guide at <https://docs.microsoft.com/en-us/graph/auth-limit-mailbox-access>

## Add Azure AD Data to Enate

After Azure AD has been configured to grant access, login to Enate Builder as a user with the “Can Edit Shared Configuration” permission.&#x20;

Click the settings cog in the bottom left and open the “Office 365 Integration” pane and enter the details from your Azure AD App Registration.&#x20;

The Tenant ID (aka Directory or Domain) and Application ID is shown on the Overview pane of the Azure AD App Registration; the client secret or certificate (and private key password) are supplied by you to both Azure AD and Enate.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F9VF7nJABH4s97SoAgeFH%2Fimage.png?alt=media\&token=746019b3-bc3c-43d7-a753-db5595324019)

## Integrate with Office 365

You always use shared mailbox.

Click on the Office 365 Integration” pane and select whether you want to authenticate with a certificate (this is the recommended route as it is more secure), or whether you want to authenticate with client secret.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpg6LWUc3pHK4L_bbl%2F-MWpiCqECFb3AdC92KoH%2Fimage.png?alt=media\&token=0b62d108-f1ea-4ca6-8aee-7fc0da22d432)

### Authentication with Certificate (recommended) <a href="#generating-a-certificate" id="generating-a-certificate"></a>

As part of this set up, an Office365 Certificate would need to be generated - Generating a certificate is an activity for your Office365 Administrator to undertake, and is done completely independent of Enate. For your reference we have provided below a SAMPLE of the kind of PowerShell script that can be used to generate such a certificate. It will save the Certificate with the private key (for Enate) to a PFX file and without the private key (for Azure):

```
$pw = Read-Host -Prompt "Please enter a password for the Private Key" -AsSecureString
$name = Read-Host -Prompt "Please enter a name for the Certificate"
Write-Host "Creating Certifcate $Certname" -ForegroundColor Green
$Cert = New-SelfSignedCertificate -certstorelocation cert:\CurrentUser\my -Subject "CN=$name" -KeyExportPolicy Exportable -KeySpec Signature
$desktopPath = [Environment]::GetFolderPath("Desktop")
Write-Host "Exporting Certificate with Private Key to $desktopPath\$name.pfx" -ForegroundColor Green
Export-PfxCertificate -cert $Cert -FilePath $desktopPath\$name.pfx -Password $pw
Write-Host "Exporting Certificate with Public Key only to $desktopPath\$name.cer" -ForegroundColor Green
Export-Certificate -cert $Cert -FilePath $desktopPath\$name.cer
```

Enter the Tenant ID/Domain and the Application ID, select the 'Authentication with Certificate' option, add the certificate file ( Personal Information File, .pfx) and enter the password for the certificate file.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FxElbQ0MAbnlriW7MWKJN%2Fimage.png?alt=media\&token=c84161fa-86e3-402f-a923-c290bf7af231)

Then click to check the connection. Once the connection has been successfully tested, click to save.

You have now successfully configured your Office 365 integration.

### Authentication with Client Secret

To authenticate with client secret code, enter the Tenant ID/Domain and the Application ID, select the 'Authentication with Client Secret' option, add the client secret code (this is generated by the network admin of your company).&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Fxu0zaeHDWgpE77JnQh5K%2Fimage.png?alt=media\&token=c2c08179-a71e-412e-9d8d-cb795d0f7b38)

Then click to check the connection. Once the connection has been successfully tested, click to save.

You have now successfully configured your Office 365 integration.

## Configuring Graph API Mailbox

Once you have successfully configured your Office 365 integration, you can configure your Graph API Mailbox by going to the [Email Connectors](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-connectors-detail) page and selecting to add a Graph API Connector.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FrhF3wnJ2aPExF3zl9NqY%2Fimage.png?alt=media\&token=d9a51a1e-3645-40fa-b531-1f0ab2514a39)

Enter the name and email address of the shared mailbox to be used.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FbjwUjDq3K1Es6TahK3hU%2Fimage.png?alt=media\&token=bcbc2735-46ab-435e-82fb-e0c5b015fcba)

Then click to test the connection. Once the connection has been successfully tested, click to enable the Graph API connector and click to save. Your Graph API connector is now set up.

You can now create different [Email Routes](https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/email-routes) for the Graph API connector if you wish.

If a new email arrives from one of the folders configured in the connector and it matches the folder path specified in the email route and it passes any other routing rules, it will launch the process specified in the route.&#x20;

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FLCqG72wR7bxVw1b0dP8i%2Fimage.png?alt=media\&token=615ae3d1-04e0-422f-ae2e-c06833c6ea14)

If you don't specify the folder path and leave it blank or use a wildcard '\*', emails from any of the the folders configured in the connector will create the process specified in the route, as long as all the other routing rules are matched as well.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FJxaYMh2puV0OmW8Fj1Ce%2Fimage.png?alt=media\&token=c902013c-2f6b-4e0c-b91f-8160864a3f11)
