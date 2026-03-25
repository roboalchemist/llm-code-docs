# Source: https://docs.axonius.com/docs/bitwarden-vault-integration.md

# Bitwarden Vault Integration

The **Bitwarden Vault** integration enables Axonius to securely pull privileged credentials from **Bitwarden Vault**. The integration helps to ensure that privileged credentials are secured in the Bitwarden Vault, rotated to meet company guidelines, and meet complexity requirements.
Axonius uses the [Bitwarden Vault Management API](https://bitwarden.com/help/vault-management-api/).

## Description of Product Integration

**Bitwarden Vault** is a robust, cloud-hosted password manager and secret storage service that uses end-to-end encryption to protect sensitive information. It helps ensure that access to credentials, API keys, and other secrets is strictly controlled and secure.

Axonius authenticates to the Bitwarden Vault using API token-based authentication. This authentication method ensures that the communication between Axonius and Bitwarden Vault is secure, allowing Axonius to retrieve necessary credentials while maintaining the confidentiality of sensitive data. By leveraging Bitwarden Vault’s encrypted storage capabilities, Axonius can manage and access credentials in a compliant and secure manner.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your Bitwarden Vault Server, you need to:

1. Install and configure Bitwarden Vault.
2. Enable and configure the [External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords) in Axonius.
3. Configure adapter connection credential to fetch passwords from Bitwarden Vault Server.

## Enable Bitwarden Vault Integration

Enable Bitwarden Vault integration and allow Axonius to securely pull privileged credentials from the Bitwarden Vault.
Following the guidelines in [External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords#bitwarden-vault)

## Working with Bitwarden Vault

Once the Bitwarden Vault integration is enabled in Axonius, a new Bitwarden Vault icon will appear in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or to fetch the secret from Bitwarden Vault Server.

**To fetch the password from Bitwarden Vault**

1. In a password field, click the Bitwarden Vault icon.  If you have configured more than one password manager, click the vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select Bitwarden Vault from the drop-down. A Bitwarden Vault password dialog opens.

<Image alt="PasswordField" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-PCT7C5KK.png" />

2. In the dialog, specify the following parameter:

   **Name to Search** - The name of the Bitwarden Vault you want to use. You can find it under **Vaults** in your Bitwarden console.

<Image alt="PasswordDialog" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-XZCFO0VX.png" />

3. Click **Fetch**.
   * If the fetch is successful, a green indication is displayed next to the Bitwarden Vault icon. Hovering over the Bitwarden Vault icon shows the credentials you input.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-VNK7ICBS.png)

   * If the fetch is unsuccessful, a red indication is displayed next to the Bitwarden Vault icon. Hovering over the Bitwarden Vault icon shows the error.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-7JJR4RP4.png)

<Callout icon="📘" theme="info">
  Note

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>