# Source: https://docs.axonius.com/docs/1password-connect-server.md

# 1Password Connect Server

The 1Password Connect Server integration enables Axonius to securely pull privileged credentials from the **1Password Connect Server**. The integration helps to ensure that privileged credentials are secured in the **1Password Connect Server**, rotated to meet company guidelines and meet complexity requirements.

## Description of Product Integration

Axonius uses the 1Password Connect Server HTTP API to fetch credentials from the Vault.
Axonius authenticates to the 1Password Connect Server Server token authentication.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your 1Password Connect Server, you need to:

1. Install and configure **1Password Connect Server**.
2. Enable and configure the **[External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords)**.
3. Configure adapter connection credentials to fetch passwords from 1Password Connect Server.

## Enable 1Password Connect Server Integration

Follow the guidelines in [Enterprise Password Management Settings](/docs/managing-external-passwords#1password-connect-server) to enable 1Password Connect Server integration and allow Axonius to securely pull privileged credentials from the 1Password Connect Server.

## Working with  1Password Connect Server

Once the [1Password Connect Server integration is enabled](/docs/managing-external-passwords#1password-connect-server) in Axonius, a new 1password-connect-server icon appears in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or fetch the secret from 1Password Connect Server.

**To fetch the password from 1Password Connect Server**

1. In the **Password** field, click the 1Password Connect Server icon. If you have configured more than one password manager, click the vault icon ![Vaulticon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and then select **1Password Connect Server** from the dropdown. A **1Password Connect Server** dialog opens.

![1PasswordConnectServerdialog](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/1PasswordConnectServerdialog.png)

2. In the dialog, specify the following parameters:
   * **Vault Name** *(required)* - The name of the vault.
   * **Item Name** *(required)* - The name of the item.
   * **Item Type** *(required)* - The type of sandbox credential. Usually *password*. However, you can choose a different sandbox credential, such as *JWT*.

3. Click **Fetch**.
   * If the fetch is successful, a green indication is displayed next to the 1Password Connect Server icon.  Hovering over the 1Password Connect Server icon shows the information that you input.
     ![1PasswordCorrect](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/1PasswordCorrect.png)

   * If the fetch is unsuccessful, a red indication is displayed next to the 1Password Connect Server icon. Hovering over the 1Password Connect Server icon shows the error.
     ![1PasswordConnectServerError](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/1PasswordConnectServerError.png)

<Callout icon="📘" theme="info">
  Note

  Typing or deleting any character in the textbox reverts the password field to manual password input.
</Callout>