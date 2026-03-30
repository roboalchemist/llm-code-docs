# Source: https://docs.axonius.com/docs/manageengine-pam360-vault.md

# ManageEngine PAM360 Vault

The ManageEngine PAM360 integration enables Axonius to securely pull privileged credentials from the **ManageEngine PAM360 Vault**. The integration helps to ensure that privileged credentials are secured in the **ManageEngine PAM360 Vault**, rotated to meet company guidelines and meet complexity requirements.

## Description of Product Integration

Axonius uses the ManageEngine PAM360 Vault HTTP API to fetch credentials from the Vault.
Axonius authenticates to the ManageEngine PAM360 Vault Server token authentication.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your ManageEngine PAM360 Vault Server, you need to:

1. Install and configure **ManageEngine PAM360 Vault**.
2. Enable and configure the **[External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords)**.
3. Configure adapter connection credentials to fetch passwords from ManageEngine PAM360 Vault Server.

## Enable ManageEngine PAM360 Vault Integration

Follow the guidelines in [Enterprise Password Management Settings](/docs/managing-external-passwords#manageengine-pam360-vault) to enable ManageEngine PAM360 Vault integration and allow Axonius to securely pull privileged credentials from the ManageEngine PAM360 Vault Server.

## Working with  ManageEngine PAM360 Vault

Once the [ManageEngine PAM360 Vault integration is enabled](/docs/managing-external-passwords#manageengine-pam360-vault) in Axonius, a new ManageEngine PAM360 Vault icon appears in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or fetch the secret from the ManageEngine PAM360 Vault server.

**To fetch the password from ManageEngine PAM360 Vault**

1. In the **Password** field, click the ManageEngine PAM360 Vault icon. If you have configured more than one password manager, click the vault icon ![Vaulticon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and then select **ManageEngine PAM360 Vault** from the dropdown. A **ManageEngine PAM360** dialog opens.

![PAM360SecretKeyDialog](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PAM360SecretKeyDialog.png)

2. In the dialog, specify the following parameters:
   * **Resource Name** *(required)* - The name that uniquely identifies your resource in PAM360. A resource can be any server, application, network device, or appliance that holds the user accounts and passwords.
   * **Account Name** *(required)* - Your account name in PAM360.
   * **Reason** *(optional)* - The reason for requesting this specific password.
   * **Ticket ID** *(optional)* - The relevant ticket ID for this specific password request.

3. Click **Fetch**.

   * If the fetch is successful, a green indication is displayed next to the ManageEngine PAM360 Vault icon.  Hovering over the ManageEngine PAM360 Vault icon shows the information that you input.

   ![PasswordManagerProSecretKeyCorrect](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManagerProSecretKeyCorrect.png)

   * If the fetch is unsuccessful, a red indication is displayed next to the ManageEngine PAM360 icon. Hovering over the ManageEngine PAM360 Vault icon shows the error.

   ![PasswordManagerProSecretKeyError](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PasswordManagerProSecretKeyError.png)

<Callout icon="📘" theme="info">
  Note

  Typing or deleting any character in the textbox reverts the password field to manual password input.
</Callout>