# Source: https://docs.axonius.com/docs/akeyless-vault-integration.md

# Akeyless Vault Integration

The Akeyless integration enables Axonius to securely pull privileged credentials from the **Akeyless Vault**. The integration helps to ensure that privileged credentials are secured in the **Akeyless Vault**, rotated to meet company guidelines, and meet complexity requirements.

## Description of Product Integration

Axonius uses the Akeyless Vault to fetch credentials from the Vault.
Axonius authenticates to the Akeyless Vault Server token authentication.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your Akeyless Vault Server, you need to:

1. Install and configure **Akeyless Vault**
2. Enable [external password managers](/docs/managing-external-passwords) in Axonius.

<Callout icon="📘" theme="info">
  Note

  The secrets must be created as static secrets.
</Callout>

3. Configure adapter connection credential to fetch passwords from Akeyless Vault Server.

## Enable Akeyless Vault Integration

Follow the guidelines in [Managing External Passwords](/docs/managing-external-passwords#akeyless-vault) to enable Akeyless Vault integration and allow Axonius to securely pull privileged credentials from the Akeyless Vault Server.

## Working with  Akeyless Vault

Once the [Akeyless Vault integration is enabled](/docs/managing-external-passwords#akeyless-vault) in Axonius, a new Akeyless Vault icon will appear in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or to fetch the secret from Akeyless Vault Server.

<Image alt="AkeylessVault" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AkeylessVault.png" />

To fetch the password from Akeyless Vault:

1. In a password field, click the Akeyless Vault icon.  If you have configured more than one password manager, click the vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select Akeyless Vault from the drop-down. An Akeyless Vault password dialog opens.

<Image alt="AkeylessVaultPassword" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AkeylessVaultPassword.png" />

2. In the dialog, specify the following parameters:

   **Secret Name** *(required)* - The name of the secret key that you saved for the Akeyless vault.

3. Click **Fetch**.
   * If the fetch is successful, a green indication is displayed next to the Akeyless Vault icon. Hovering over the  Akeyless Vault icon shows the credentials you input.

   * If the fetch is unsuccessful, a red indication is displayed next to the Akeyless icon. Hovering over the Akeyless Vault icon shows the error.

<Image alt="AkeylessWrong" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AkeylessWrong.png" />

<Callout icon="📘" theme="info">
  NOTE

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>