# Source: https://docs.axonius.com/docs/thycotic-integration.md

# Delinea Integration

The Delinea integration enables Axonius to securely pull privileged credentials from the **Delinea Secret Server**. The integration ensures that privileged credentials are secured in the Delinea Secret Server, rotated to meet company guidelines, and meet complexity requirements.

## Description of Product Integration

Axonius uses the Secret Server REST API   to fetch credentials from the Delinea Secret Server; refer to [Delinea Documentation.](https://docs.delinea.com/secrets/current/developer-resources#rest_api)
Axonius authenticates to Delinea Secret Server using bearer token authentication.

The integration supports both an on-premise Delinea Secret Server and a cloud instance of Delinea Secret Server.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your Delinea Secret Server, you need to:

1. Install and configure **Delinea Secret Server** or use the Cloud instance of Delinea Secret Server.
2. Enable and configure the **[External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords)** in Axonius.
3. Configure adapter connection credentials to fetch passwords from Delinea Secret Server.

## Enable Delinea Integration

Enable Delinea integration and allow Axonius to securely pull privileged credentials from the Delinea Secret Server.
Follow the guidelines in [Enterprise Password Management Settings](/docs/managing-external-passwords#delinea-secret-server).

## Working with Delinea

Once the [Delinea integration is enabled](/docs/managing-external-passwords#delinea-secret-server) in Axonius, a new Delinea Secret Server icon appears in all password fields when configuring adapters or Enforcement Sets, allowing you to enter a password manually or fetch the secret from Delinea Secret Server.

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(863\).png)

To fetch the password from Delinea Secret Server:

1. In a password field, click the Delinea icon.  If you have configured more than one password manager, click the vault icon ![Vaulticon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select **Delinea Secret Server** from the drop-down. A **Delinea Secret Server** dialog opens.
   ![DelineaSecretServerDialog](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DelineaSecretServerDialog.png)

2. In the dialog, specify the following parameters:
   1. **Secret ID** *(required)* - The secret ID for the password. This secret ID represents a unique identifier for the secret in Delinea.
   2. **Field Name** *(required, default: Password)* - The field name for the password.  This is case sensitive.

3. Click **Fetch**.
   * If the fetch is successful, a green indication is displayed next to the Delinea icon.\
     ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(867\).png)
   * If the fetch is unsuccessful, a red indication is displayed next to the Delinea icon. Hovering over the Delinea Secret Server icon shows the error.
     ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(868\).png)

<Callout icon="📘" theme="info">
  Note

  Typing or deleting any character in the textbox reverts the password field to manual password input.
</Callout>