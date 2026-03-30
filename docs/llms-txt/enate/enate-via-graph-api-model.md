# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/email-mailbox-configuration/enate-via-graph-api-model.md

# Enate via Graph API model

This page includes a step-by-step guide on how to prepare your Azure Active Directory setup for successfully setting up the integration between Enate and Office 365. Here is an outline of the topics that will be covered.&#x20;

1. [Creating a User in Microsoft Azure](#creating-a-user-in-microsoft-azure)
2. [Creating a Shared Mailbox in Azure Active Directory](#creating-a-shared-mailbox-in-azure-active-directory)
3. [Setting up a Mail enabled security group](#id-3.-mail-enabled-security-group)
4. [Creating App registration in Azure Active Directory ](#app-registration-in-azure-active-directory)
5. [Creating Credentials. i.e., Client Secret and Authenticating by Certificate](#creating-credentials).

### **1. Creating a User in Microsoft Azure**&#x20;

Within Azure Active Directory, every user account is granted a default collection of authorisations. The accessibility of a user's account is determined by their user category, role allocations, and possession of specific entities. Azure Active Directory has different types of user accounts, each designed with specific levels of access suited for their expected tasks.

In simpler terms, administrators have the highest access, followed by regular member accounts, and guest users have the most limited access.

Azure Active Directory uses permissions to manage the access rights given to a user or group, implemented through established rules.

1. Access and log in to the Microsoft Azure portal via <https://portal.azure.com>.
2. Beneath "Manage Azure Active Directory," select "View Overview Page."
3. You'll then land on the overview page of your Azure Active Directory tenant. You will need a user account with a global administrator role.
4. Under "Manage," opt for "Users," and subsequently, navigate to the "All Users" tab.
5. Here you can see all user accounts in your Azure Active Directory tenant.
6. Click on the "+" symbol to create a new user account.
7. Two alternatives will be presented: "Create User" or "Invite User." We'll adhere to the default preference to create a fresh user account.
8. Input the user details, including the username, first name, last name, and optionally include the user in existing groups.
9. Scroll downwards to specify the initial password, which the user will employ for their first sign-in.
10. Additionally,  you can include the user into groups or assign Azure AD administrative permissions.
11. Select "Create".

You can adjust user configurations by accessing the user's name and clicking the "Edit" feature.

### **2. Creating a Shared Mailbox in Azure Active Directory**

1. Log into your Microsoft 365 Admin Center.&#x20;
2. Click on the 'Exchange' to access the Exchange Admin Portal.
3. Go to 'Mailboxes' and here click on 'Add shared Mailbox'.
4. Add a 'Display Name' for the shared mailbox and then add an email address and select a domain from the drop down list.
5. You can use the display name as the 'Alias'.
6. Click 'Create'.

After creating the shared mailbox you can add members who can receive, read and reply to the emails sent into that mailbox.

This shared mailbox will be now visible in the list of mailboxes with the RecipientType shown as SharedMailbox.

Two types of permissions are needed for successful operation of a shared mailbox.&#x20;

***Full Access Permission:*** Allows a user to open a mailbox and create and modify items in it.\
\&#xNAN;***Send as Permission**:* Allows other members to send emails from this mailbox.

To enable both, click to select the shared mailbox and under 'Mailbox Permissions' select 'Manage Mailbox Delegation'.

Click on the 'Read and Manage' button and select 'Edit'. Click on 'Add Permissions. Select the users that you want to have Full Access Permission to this mailbox. Hit 'Save'. Then click on 'Close' and then 'Cancel'.

After this click 'Edit' for 'Send as' permissions. Click on 'Add Permissions. Select the users that you want to have Send as permissions to this mailbox.

### **3. Mail Enabled Security Group**

The next thing you'll need to do is the App registration creation and permission restrictions but for these a Mail Enabled security group is a prerequisite. This group can be used to manage permissions, distribute emails, and provide access to various resources within your organization.

1\. Creating a Mail-Enabled Security Group

* In the Exchange Admin Center, go to "Recipients" and click on "Groups."
* Navigate to the "Mail Enabled Security" tab and click "Add a group."
* Choose "Mail Enabled Security" as the group type and click "Next."

2. &#x20;Group Configuration

* Provide a name (e.g., Editors) and optional description for the group.
* Set the email address for the group.
* Configure communication settings based on your requirements.
* Enable owner approval if needed and click "Next."

3. &#x20;Confirmation and Group Creation

* Verify the details and click "Create group" to complete the process.
* Note that it may take some time for the group to appear in your list.

4. &#x20;Adding Members to the Security Group

* Access the group in Exchange Admin Center, click on the group name, and go to the "Members" tab.
* Add members by selecting "View and manage members" and clicking "Add members."

5. &#x20;Sending a Test Message

* Confirm the group's existence in the "Mail Enable Security" tab.
* Send a test email to the group's email address.

6. &#x20;Checking Received Message

* Access the mailbox of a group member to confirm the receipt of the test message.

### **4. App Registration in Azure Active Directory**

To configure integration between Enate and Office 365, each unique Enate instance must be registered with the Microsoft Identity Platform in the Azure AD of the Office 365 tenant to which you need to establish connectivity. <https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app>

#### Create the “App Registration”:

Creating an app registration establishes a  trust between your application and the Microsoft identity platform. This trust is unidirectional, with your application relying on the Microsoft identity platform. Importantly, once the application object is generated, it remains tied to its original tenant and cannot be transferred to different tenants.

Follow these steps for the app registration process:

**1. Sign In -** Log in to the Microsoft Entra admin center with Cloud Application Administrator credentials.

**2. Tenant Selection -** Use the Settings icon to switch to the desired tenant from the Directories + subscriptions menu if you have access to multiple tenants.

**3. App Registrations Location -** Go to Identity > Applications > App registrations and select New registration.

**4. Application Details** Provide a display name for the application, visible during user interactions. The Application (client) ID uniquely identifies the app within the identity platform.

**5. Define Sign-In Audience -** Choose the appropriate account type for the intended audience:

* Accounts in this organizational directory only (Single-tenant).
* Accounts in any organizational directory (Multi-tenant).
* Accounts in any organizational directory and personal Microsoft accounts (Broad audience).
* Personal Microsoft accounts (Exclusive personal accounts).

**6. Redirect URI Field -** Leave the Redirect URI field blank for now; configuration will be done later.

**7. Registration Execution -** Click Register to complete the initial app registration.

**8. Access Application ID -** Visit the Overview pane in the Microsoft Entra admin center to find the Application (client) ID.

{% hint style="info" %}
**Note:** Newly created app registrations are initially hidden. To make the app visible on users' My Apps page, go to Identity > Applications > Enterprise applications, select the app, and toggle Visible to users? to Yes on the Properties page.
{% endhint %}

The client ID is utilized in your application's source code or authentication library for validating security tokens from the Microsoft identity platform.

**Restricting Permissions**

**Testing**&#x20;

### **5. Creating Credentials:**

#### **Generating a Client Secret**

* Log into the [Azure Portal](https://portal.azure.com/) and search for Azure Active Directory
* Select "Azure Active Directory" to navigate to the Azure Active Directory "Overview"
* Click the \[App registrations] button to open the "App Registrations"
* Select your App registration to open its details page
* Click the \[Certificates & secrets] button to display the "Certificates & secrets"
* Select the "Client secrets" tab, if it is not yet selected.
* Click the \[New client secret] button to display the "Add client secret" dialogue.
* Provide a brief description of the secret. This will show up in lists, making it easier to identify later.
* Select a time at which the secret will expire and need to be regenerated.
* Click the \[Add] button to generate the Client Secret and return to the "Certificates & Secrets" value. You should see your newly-generated secret listed here. Copy and save the "Value". You will need it later.

{% hint style="info" %}
IMPORTANT: After you navigate away from this page, there is no way to retrieve the Secret Value. If you do not copy and save it now, you will need to regenerate a Secret. Keep this secret in a safe place - in Azure Key Vault or in a secure folder. If it is compromised, a hacker can access your API with this service identity.
{% endhint %}

**Establishing Certificate-based Authentication**

Establishing authentication through certificates involves a multi-step process. After successfully configuring the entire chain, it's beneficial to disseminate the information for others' convenience.

Reviewing the provided sequence diagram, the initial phase entails the client generating certificates and sharing the public certificate with the server. While utilizing a self-signed certificate suffices for development and testing, it is advisable to employ a CA-signed certificate for production.

Execute the following PowerShell code:

New-SelfSignedCertificate -Subject “CN=CertForMyApp” -CertStoreLocation “Cert:\CurrentUser\My” -KeyExportPolicy Exportable -KeySpec Signature

The initial client step involves generating certificates and sharing the public certificate with the server. For production, prefer a CA-signed certificate over a self-signed one.

Execute the provided PowerShell code to create a self-signed certificate. Note the hex value of the thumbprint for later use.

**Export certificates and keys:**

1. Open "mmc" via the Windows search box.
2. Add "Certificates — Current User" to the selected snap-ins.
3. Locate the created certificate under Personal > Certificate.
4. Right-click on the certificate, select All Tasks > Export.
5. Choose Base-64 encoded X.509 (.CER) format, specify a location and filename, and complete the export.

The exported .CER file is the public certificate to share with the server and upload to Azure AD during app registration.

**Private key extraction:**

1. In the mmc application, right-click on the certificate, select All Tasks > Export.
2. Choose to export the private key, set a password, and complete the export. The private key is in .PFX format.
3. Utilize SSL Converter to convert the .PFX to .PEM format, containing public (.crt) and private (.key) key files.

**Register the app on Azure AD and upload the public certificate:**

1. Follow the steps in the provided link, noting tenant\_id and client\_id.
2. Add a certificate, upload the public certificate (.cer) file, and complete the process.

Initial registration and key exchange are complete. Proceed with the API sequence flow:

1. Retrieve the bearer token from Azure AD.
2. Base64 encode the hex thumbprint using a tool or Python script.
3. Use the encoded thumbprint to create a signed JWT token.

Code for JWT token creation:

Here's a breakdown of the script:

1. **Prompt for Password:**

   ```powershell
   $pw = Read-Host -Prompt "Please enter a password for the Private Key" -AsSecureString
   ```

   This line prompts the user to enter a password securely for the private key and stores it in the variable `$pw` as a secure string.
2. **Prompt for Certificate Name:**

   ```powershell
   $name = Read-Host -Prompt "Please enter a name for the Certificate"
   ```

   This line prompts the user to enter a name for the certificate and stores it in the variable `$name`.
3. **Create Self-Signed Certificate:**

   ```powershell
   Write-Host "Creating Certifcate $Certname" -ForegroundColor Green
   $Cert = New-SelfSignedCertificate -certstorelocation cert:\CurrentUser\my -Subject "CN=$name" -KeyExportPolicy Exportable -KeySpec Signature
   ```

   This section creates a self-signed certificate using the provided name and subject. The certificate is stored in the variable `$Cert`.
4. **Export Certificate with Private Key to PFX:**

   ```powershell
   $desktopPath = [Environment]::GetFolderPath("Desktop")
   Write-Host "Exporting Certificate with Private Key to $desktopPath\$name.pfx" -ForegroundColor Green
   Export-PfxCertificate -cert $Cert -FilePath $desktopPath\$name.pfx -Password $pw
   ```

   This part exports the certificate along with the private key to a PFX file on the user's desktop, using the password entered earlier.
5. **Export Certificate with Public Key Only to CER:**

   ```powershell
   Write-Host "Exporting Certificate with Public Key only to $desktopPath\$name.cer" -ForegroundColor Green
   Export-Certificate -cert $Cert -FilePath $desktopPath\$name.cer
   ```

   Finally, this section exports the certificate with only the public key to a CER file on the user's desktop.

Make sure to handle the generated files securely, especially the PFX file containing the private key, as it requires the password entered during the script execution.

Finally, execute a GET request to "<https://login.microsoftonline.com/\\>\<tenant\_id>/oauth2/token" with the specified parameters to obtain the bearer token for API calls.&#x20;
