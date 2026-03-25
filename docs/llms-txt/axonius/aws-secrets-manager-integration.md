# Source: https://docs.axonius.com/docs/aws-secrets-manager-integration.md

# AWS Secrets Manager Integration

The AWS Secrets Manager integration enables Axonius to securely pull privileged credentials from **AWS Secrets Manager**. The integration ensures that privileged credentials are secured in the AWS Secrets Manager, rotated to meet company guidelines, and meet complexity requirements.

## Enable AWS Secrets Manager Integration

Enable AWS Secrets Manager integration and allow to Axonius to securely pull privileged credentials from the AWS Secrets Manager.
Follow the guidelines in [Managing External Passwords](/docs/managing-external-passwords).

## Working with AWS Secrets Manager

Once the [AWS Secrets Manager integration](/docs/managing-external-passwords#aws-secrets-manager) is enabled Axonius, a new AWS Secrets Manager icon will appear in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or to fetch the secret from AWS Secrets Manager.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1331\).png)

To fetch the password from AWS Secrets Manager:

1. In a password field, click the AWS Secrets Manager icon. If you have configured more than one password manager, click the vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select AWS from the drop-down.
   The AWS Secrets Manager dialog opens.

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1330).png" />

2. In the dialog, specify the following parameters:
   1. **Secret name** *(required)* - Specify the secret containing the secret key that you want to retrieve. You can specify either the Amazon Resource Name (ARN) or the friendly name of the secret
   2. **Secret key** *(required, default: Password)* - Specify the unique identifier of the secret that you want to retrieve.
3. Click **Fetch**.
   * If the fetch is successful, a green indication will be displayed next to the AWS Secrets Manager icon.
   * If the fetch is unsuccessful, a red indication will be displayed next to the AWS Secrets Manager icon. Hovering over the AWS Secrets Manager icon will show the error.

<Callout icon="📘" theme="info">
  NOTE

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>