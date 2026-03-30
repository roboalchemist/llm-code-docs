# Source: https://docs.axonius.com/docs/azure-key-vault.md

# Azure Key Vault Integration

The Azure Key Vault integration enables Axonius to securely pull privileged credentials from the **Azure Key Vault**. The integration helps to ensure that privileged credentials are secured in the **Azure Key Vault**, rotated to meet company guidelines, and meet complexity requirements.

## Description of Product Integration

Axonius uses the Azure Key Vault  to fetch credentials from the Vault. Microsoft Azure Key Vault is a cloud-hosted management service that allows users to encrypt keys and small secrets by using keys that are protected.
Axonius authenticates to the Azure Key Vault Server token authentication.

<Image alt="AzureSecret" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AzureSecret.png" />

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your Azure Key Vault  Server, you need to:

1. Install and configure **Azure Key Vault**
2. Set up permissions for **Azure Key Vault** in Azure
3. Enable and configure the **[external password managers](/docs/managing-external-passwords)** in Axonius.
4. Configure adapter connection credential to fetch passwords from Azure Key Vault Server.

### Creating the Client Secret in Azure

To create the client secret do the following:

1. Select **Azure Active Directory**.
2. From **App registrations** in Azure AD, select your application.
3. Select **Certificates & secrets**.
4. Select **Client secrets** -> **New client secret**. The Client Secret is displayed. Copy it to a safe place.

### **Enabling Permissions in Azure for the Azure Key Vault**

To enable permissions for the vault perform the following:

1. Log in to the Azure Portal
2. Enter in Key vaults
3. Click on a **Key Vault**.
4. Click on **Access policies**.
5. Click **Add Access Policy**.
6. From the drop-down list **Key Permissions**, select **List and Get**.
7. From the drop-down list **Secret Permissions** select **List and Get**.
8. Click **Add**.

## Enable Azure Key Vault Integration

Follow the guidelines in [Managing Enterprise Passwords](/docs/managing-external-passwords#azure-key-vault) to enable Azure Key Vault integration and allow Axonius to securely pull privileged credentials from the Azure Key Vault Server.

## Working with  Azure Key Vault

Once the [Azure Key Vault integration is enabled](/docs/managing-external-passwords#azure-key-vault) in Axonius, a new Azure Key Vault icon will appear in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or to fetch the secret key from Azure Key VaultServer.

<Image alt="KwyVaultinAdapter" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/KwyVaultinAdapter.png" />

To fetch the password from Azure Key Vault:

1. In a password field, click the Azure Key Vault icon.  If you have configured more than one password manager, click the vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select Azure Key Vault from the drop-down. An Azure Key Vault dialog opens.

<Image alt="AzureKeyVAult" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AzureKeyVAult.png" />

2. In the dialog, specify the following parameters:
   1. **Vault name** *(required)* - The name of the vault.

   2. **Secret key** *(required)* - The name of the secret key that you saved for the vault.

3. Click **Fetch**.
   * If the fetch is successful, a green indication is displayed next to the Azure Key Vault icon.

   * If the fetch is unsuccessful, a red indication is displayed next to the Azure Key Vault​  icon. Hovering over the Azure Key Vault icon shows the error.

<Callout icon="📘" theme="info">
  NOTE

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>