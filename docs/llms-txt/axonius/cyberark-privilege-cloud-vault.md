# Source: https://docs.axonius.com/docs/cyberark-privilege-cloud-vault.md

# CyberArk Privilege Cloud Vault

The CyberArk Privilege Cloud Vault integration enables Axonius to securely pull privileged credentials from  **CyberArk Privilege Cloud Vault**. The integration helps to ensure that privileged credentials are secured in  **CyberArk Privilege Cloud Vault**, rotated to meet company guidelines, and meet complexity requirements.

## Description of Product Integration

Axonius uses the [CyberArk Privilege Cloud API](https://docs.cyberark.com/PrivCloud/Latest/en/Content/WebServices/Implementing%20Privileged%20Account%20Security%20Web%20Services%20.htm) to fetch credentials from  CyberArk Privilege Cloud Vault.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your CyberArk Privilege Cloud Vault, you need to:

1. Install and configure **CyberArk Privilege Cloud Vault**.
2. Configure login using [CyberArk](https://docs.cyberark.com/PrivCloud/Latest/en/Content/SDK/CyberArk%20Authentication%20-%20Logon_v10.htm?tocpath=Developers%7CREST%20APIs%7CAuthentication%7CLogon%7C_____1).
3. Have 'read' permissions for the passwords.
4. Enable and configure the **[External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords#cyberark-privilege-cloud-vault)** in Axonius.
5. Configure adapter connection credentials to fetch passwords from CyberArk Privilege Cloud Vault.

## Enable CyberArk Privilege Cloud Vault Integration

Follow the guidelines in [External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords#cyberark-privilege-cloud-vault) to enable CyberArk Privilege Cloud Vault integration and allow Axonius to securely pull privileged credentials from CyberArk Privilege Cloud Vault.

## Working with  CyberArk Privilege Cloud Vault

Once the [CyberArk Privilege Cloud Vault integration is enabled](/docs/managing-external-passwords#cyberark-privilege-cloud-vault) in Axonius, a new CyberArk Privilege Cloud Vault icon will appear in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or to fetch the secret from CyberArk Privilege Cloud Vault. If you have configured more than one domain (tenant) for this vault, a vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) will appear in the password field (same as when you configure more than one password manager).

<Image alt="CyberArk%20PrivCloud" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CyberArk%20PrivCloud.png" />

To fetch the password from CyberArk Privilege Cloud Vault:

1. In a password field, click the CyberArk Privilege Cloud Vault icon. If you have configured more than one password manager (including more than one domain of the CyberArk Privilege Cloud), click the vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select the required CyberArk Privilege Cloud Vault from the drop-down.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChooseVault.png)

A CyberArk Privilege Cloud Vault dialog opens for the selected vault.

<Image align="center" alt="CyberArkValut2" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CyberArkValut2.png" />

2. In the dialog, specify the following parameters:
   1. **Account ID** *(required)* - The account the password belongs to. It uses the endpoints [login](https://docs.cyberark.com/PrivCloud/Latest/en/Content/SDK/CyberArk%20Authentication%20-%20Logon_v10.htm?tocpath=Developers%7CREST%20APIs%7CAuthentication%7CLogon%7C_____1) and [get password](https://docs.cyberark.com/PrivCloud/Latest/en/Content/WebServices/GetPasswordValueV10.htm?tocpath=Developers%7CREST%20APIs%7CAccounts%7CAccount%20actions%7C_____3).

3. Click **Fetch**.
   * If the fetch is successful, a green indication is displayed next to the CyberArk Privilege Cloud Vault icon.  Hovering over the CyberArk Privilege Cloud Vault icon shows the credentials that you input.

   * If the fetch is unsuccessful, a red indication is displayed next to the CyberArk Privilege Cloud Vault icon. Hovering over the Click CyberArk Privilege Cloud Vault icon shows the error.

<Image align="center" alt="CyberArkOnlineValut3" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CyberArkOnlineValut3.png" />

<Callout icon="📘" theme="info">
  Note

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>