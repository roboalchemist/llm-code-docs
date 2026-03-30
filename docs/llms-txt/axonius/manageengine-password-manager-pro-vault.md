# Source: https://docs.axonius.com/docs/manageengine-password-manager-pro-vault.md

# ManageEngine Password Manager Pro Vault

The ManageEngine Manager Pro integration enables Axonius to securely pull privileged credentials from the **ManageEngine Password Manager Pro Vault**. The integration helps to ensure that privileged credentials are secured in the **ManageEngine Password Manager Pro Vault**, rotated to meet company guidelines and meet complexity requirements.

## Description of Product Integration

Axonius uses the ManageEngine Password Manager Pro Vault HTTP API to fetch credentials from the Vault.
Axonius authenticates to the ManageEngine Password Manager Pro Vault Server token authentication.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your ManageEngine Password Manager Pro Vault Server, you need to:

1. Install and configure **ManageEngine Password Manager Pro Vault**.
2. Enable and configure the **[External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords)**.
3. Configure adapter connection credentials to fetch passwords from ManageEngine Password Manager Pro Vault Server.

## Enable ManageEngine Password Manager Pro Vault Integration

Follow the guidelines in [Enterprise Password Management Settings](/docs/managing-external-passwords#manageengine-password-manager-pro-vault) to enable ManageEngine Password Manager Pro Vault integration and allow Axonius to securely pull privileged credentials from the ManageEngine Password Manager Pro Vault Server.

## Working with  ManageEngine Password Manager Pro Vault

Once the [ManageEngine Password Manager Pro Vault integration is enabled](/docs/managing-external-passwords#manageengine-password-manager-pro-vault) in Axonius, a new ManageEngine Password Manager Pro Vault icon appears in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or fetch the secret from the ManageEngine Password Manager Pro Vault server.

**To fetch the password from ManageEngine Password Manager Pro Vault**

1. In the **Password** field, click the ManageEngine Password Manager Pro Vault icon. If you have configured more than one password manager, click the vault icon ![Vaulticon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and then select **ManageEngine Password Manager Pro Vault** from the dropdown. A **ManageEngine Password Manager Pro** dialog opens.

![ManageEnginePasswordManagerProDialog](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEnginePasswordManagerProDialog.png)

2. In the dialog, specify the following parameters:
   * **Resource Name** *(required)* - The name that uniquely identifies your resource in Password Manager Pro. A resource can be any server, application, network device, or appliance that holds the user accounts and passwords.
   * **Account Name** *(required)* - Your account name in Password Manager Pro.
   * **Reason** *(optional)* - The reason for requesting this specific password.
   * **Ticket ID** *(optional)* - The relevant ticket ID for this specific password request.

3. Click **Fetch**.

   * If the fetch is successful, a green indication is displayed next to the ManageEngine Password Manager Pro Vault icon.  Hovering over the ManageEngine Password Manager Pro Vault icon shows the information that you input.

   ![PasswordManagerProSecretKeyCorrect](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManagerProSecretKeyCorrect.png)

   * If the fetch is unsuccessful, a red indication is displayed next to the ManageEngine Password Manager Pro icon. Hovering over the ManageEngine Password Manager Pro Vault icon shows the error.

   ![PasswordManagerProSecretKeyError](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManagerProSecretKeyError.png)

<Callout icon="📘" theme="info">
  Note

  Typing or deleting any character in the textbox reverts the password field to manual password input.
</Callout>