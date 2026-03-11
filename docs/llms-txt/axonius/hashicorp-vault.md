# Source: https://docs.axonius.com/docs/hashicorp-vault.md

# HashiCorp Vault Integration

The HashiCorp integration enables Axonius to securely pull privileged credentials from the **HashiCorp Vault**. The integration helps to ensure that privileged credentials are secured in the **HashiCorp Vault**, rotated to meet company guidelines, and meet complexity requirements.

## Description of Product Integration

Axonius uses the HashiCorp Vault HTTP API 1 to fetch credentials from the Vault.
Axonius authenticates to the HashiCorp Vault Server  token authentication.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your HashiCorp Vault Server, you need to:

1. Install and configure **HashiCorp Vault**
2. Enable and configure the **[External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords)**.
3. Configure adapter connection credential to fetch passwords from HashiCorp Vault Server.

## Enable HashiCorp Vault Integration

Follow the guidelines in [Enterprise Password Management Settings](/docs/managing-external-passwords#hashicorp-vault) to enable HashiCorp Vault integration and allow Axonius to securely pull privileged credentials from the HashiCorp Vault Server.

## Working with  HashiCorp Vault

Once the [HashiCorp Vault integration is enabled](/docs/managing-external-passwords#hashicorp-vault) in Axonius, a new HashiCorp Vault icon will appear in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or to fetch the secret from HashiCorp Vault Server.

<Image alt="HashiCoprVaultIcon.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HashiCoprVaultIcon.png" />

To fetch the password from HashiCorp Vault:

1. In a password field, click the HashiCorp Vault icon.  If you have configured more than one password manager, click the vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select HashiCorp Vault from the drop-down. A HashiCorp Vault dialog opens.

<Image alt="HashiCoprVaultFetch2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HashiCoprVaultFetch2.png" />

2. In the dialog, specify the following parameters:
   1. **Secret path** *(required)* - The path to the stored secret or the password in the vault.
   2. **Secret Name or Role name** *(required)* - The name of the secret key that you saved for the vault.
   * For example, if you choose the Kv1 secrets engine on your system,

<Image align="center" alt="SecretEngineseg.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SecretEngineseg.png" />

The **secret path** will be the path to the secret, as shown in the screen below; and the **Secret Name**, is the value configured in the HashiCorp vault *key* field.
When working with **Active Directory**, the **Secret path** is the secret path for the “Active Directory” secret engine and **Role name** is the Role name for which you need credentials.

<Image alt="HashconfigEG.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HashconfigEG(2).png" />

When you fill in the credentials, they should look something like this.

<Image alt="HashicorpUpdated" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HashicorpUpdated.png" />

3. Click **Fetch**.

   * If the fetch is successful, a green indication is displayed next to the HashiCorp Vault icon.  Hovering over the HashiCorp Vault icon shows the secret path and secret name or Role name that you input.

   <Image alt="HashicorpSecretgood.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HashicorpSecretgood.png" />

   * If the fetch is unsuccessful, a red indication is displayed next to the HashiCorp icon. Hovering over the HashiCorp Vault icon shows the error.

   <Image alt="HashiCorpSecretFAil.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HashiCorpSecretFAil.png" />

<Callout icon="📘" theme="info">
  NOTE

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>