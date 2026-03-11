# Source: https://docs.axonius.com/docs/gcp-secret-manager.md

# GCP Secret Manager

The GCP Secret Manager integration enables Axonius to securely pull privileged credentials from the **GCP Secret Manager**. The integration ensures that privileged credentials are secured in the GCP Secret Manager, rotated to meet company guidelines, and meet complexity requirements.

## Description of Product Integration

Axonius uses the GCP Secret Manager to fetch credentials from the GCP Secret Manager.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your GCP Secret Manager, you need to:

1. Configure a connection of [Axonius to Google Cloud Platform](/docs/google-cloud-platform-gcp#connect-axonius-to-google-cloud-platform).
2. To fetch secrets from GCP Secrets Manager, you must have the following permissions:   Add to the relevant IAM Principal the following role: Secret Manager Secret Accessor
3. Enable and configure the **[External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords)** in Axonius.
4. Configure adapter connection credential to fetch passwords from GCP Secret Manager.

## Enable GCP Secret Manager Integration

Enable GCP Secret Manager integration and allow to Axonius to securely pull privileged credentials from the GCP Secret Manager.
Following the guidelines in [Enterprise Password Management Settings](/docs/managing-external-passwords#GCP-Secret-Manager).

## Working with GCP Secret Manager

Once the [GCP Secret Manager integration is enabled](/docs/managing-external-passwords#GCP-Secret-Manager) in Axonius, a new GCP Secret Manager icon will appear in all password fields when configuring adapters or Enforcement sets, allowing you to enter a password manually or to fetch the secret from GCP Secret Manager.

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(863\).png)

To fetch the password from GCP Secret Manager:

1. In a password field, click the GCP Secret Manager icon.  If you have configured more than one password manager, click the vault icon ![Vaulticon.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select GCP Secret Manager  from the drop-down. A GCP Secret Manager dialog opens.

![GCPSEcretBox](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GCPSEcretBox.png)

2. In the dialog, specify the following parameters:
   1. **Secret Name** *(required)* - The Secret Name which is created when creating the secret in GCP Secret Manager.
3. Click **Fetch**.
   * If the fetch is successful, a green indication will be displayed next to the GCP icon.

   * If the fetch is unsuccessful, a red indication will be displayed next to the GCP icon. Hovering over the GCP icon  shows the error.

<Callout icon="📘" theme="info">
  Note

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>