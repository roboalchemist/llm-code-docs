# Source: https://docs.axonius.com/docs/keeper-secrets-manager-integration.md

# Keeper Secrets Manager Integration

The Keeper Secrets Manager integration enables Axonius to securely pull privileged credentials from the **Keeper Secrets Manager**. The integration helps to ensure that privileged credentials are secured in the **Keeper Secrets Manager**, rotated to meet company guidelines, and meet complexity requirements.

## Description of Product Integration

Axonius uses the [Keeper Secrets Manager​ Python SDK](https://docs.keeper.io/secrets-manager/secrets-manager/developer-sdk-library/python-sdk) to fetch credentials from the Vault.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your Keeper Secrets Manager, you need to:

1. Install and configure **Keeper Secrets Manager**
2. Enable and configure the **[External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords)**.
3. Configure adapter connection credential to fetch passwords from Keeper Secrets Manager.

## Enable Keeper Secrets Manager Integration

Follow the guidelines in [Enterprise Password Management Settings](/docs/managing-external-passwords#Keeper-Secrets-Manager) to enable Keeper Secrets Manager integration and allow Axonius to securely pull privileged credentials from the Keeper Secrets Manager.

## Working with  Keeper Secrets Manager

Once the [Keeper Secrets Manager integration is enabled](/docs/managing-external-passwords#Keeper-Secrets-Manager) in Axonius, a new Keeper Secrets Manager icon will appear in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or to fetch the secret from Keeper Secrets Manager.

To fetch the password from Keeper Secrets Manager:

1. In a password field, click the Keeper Secrets Manager icon.  If you have configured more than one password manager, click the vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select Keeper Secrets Manager from the drop-down. A  Keeper Secrets Manager dialog opens.

2. In the dialog, specify the following parameters:
   **Secret Title** *(required)* - The name of the secret.

3. Click **Fetch**.
   * If the fetch is successful, a green indication is displayed next to the  Keeper Secrets Manager icon.  Hovering over the  Keeper Secrets Manager icon shows the secret title you input.

   * If the fetch is unsuccessful, a red indication is displayed next to the  icon. Hovering over the  icon shows the error.

<Callout icon="📘" theme="info">
  NOTE

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>