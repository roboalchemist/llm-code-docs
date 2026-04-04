# Source: https://docs.airbyte.com/platform/enterprise-flex/external-secrets.md

# External Secret Management

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

This guide provides step-by-step instructions for configuring external secrets management with Airbyte Enterprise Flex. External secrets management allows Airbyte to securely store and manage connection credentials in your cloud provider's secrets manager (AWS Secrets Manager, Azure Key Vault, or Google Cloud Secret Manager) instead of storing them in Airbyte's internal database.

info

External secrets management is available for Airbyte Enterprise Flex customers.

***

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Airbyte organization on an Enterprise Flex plan
* Active account with your chosen cloud provider (AWS, Azure, or GCP)
* Appropriate permissions to create and manage IAM roles/policies or service principals
* Access to your cloud provider's secrets management service

***

## Step 1: Configure Cloud Provider Permissions[​](#step-1-configure-cloud-provider-permissions "Direct link to Step 1: Configure Cloud Provider Permissions")

First, you'll need to create the appropriate permissions in your cloud provider to allow Airbyte to manage secrets.

* AWS
* Azure
* Google Cloud

Follow the [AWS Secret Manager Policy](https://docs.airbyte.com/platform/enterprise-setup/implementation-guide#aws-secret-manager-policy) documentation to create the required IAM policy. This policy ensures Airbyte can create, read, update, and manage secrets while restricting access to only Airbyte-managed secrets.

Follow the [Azure Key Vault Policy](https://docs.airbyte.com/platform/enterprise-setup/implementation-guide#azure-key-vault-policy) documentation to create the required permissions. This policy ensures Airbyte can create, read, update, and manage secrets while restricting access to only Airbyte-managed secrets.

Contact your Airbyte representative for GCP setup guidance and policy documentation.

***

## Step 2: Choose Authentication Method[​](#step-2-choose-authentication-method "Direct link to Step 2: Choose Authentication Method")

The authentication method varies by cloud provider:

* AWS
* Azure
* Google Cloud

AWS supports two authentication methods:

| Method                     | Use Case                                                                     | Security Note                                                   |
| -------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **IAM Role (Recommended)** | Best for EKS deployments or when using IRSA (IAM Roles for Service Accounts) | More secure - no static credentials, uses temporary credentials |
| **Access Key**             | For EC2 instances or non-Kubernetes deployments                              | Requires managing static credentials securely                   |

Azure uses service principal authentication with client credentials:

| Method                                   | Use Case                                                  |
| ---------------------------------------- | --------------------------------------------------------- |
| **Service Principal with Client Secret** | Standard authentication method for Azure Key Vault access |

GCP authentication methods will be provided by your Airbyte representative during setup.

***

## Step 3: Set Up Cloud Provider Authentication[​](#step-3-set-up-cloud-provider-authentication "Direct link to Step 3: Set Up Cloud Provider Authentication")

Follow the instructions for your chosen cloud provider:

* AWS
* Azure
* Google Cloud

Choose one of the following authentication methods:

IAM Role (Recommended)

1. Create an IAM role with a trust relationship to your EKS cluster or service account
   <!-- -->
   * This requires additional coordination with Airbyte and will enable the use of IAM authentication for some AWS-hosted sources
2. Attach the `AirbyteSecretsManagerPolicy` (created in Step 1) to this role
3. Note the Role ARN (e.g., `arn:aws:iam::123456789012:role/AirbyteSecretsRole`)

IAM User with Access Keys

1. Create an IAM user
2. Attach the `AirbyteSecretsManagerPolicy` (created in Step 1) to this user
3. Generate an access key and secret access key for this user
4. Store these credentials securely in a way they can be safely shared with Airbyte

1) **Create an Azure Key Vault** (if you don't already have one)

2) **Create an application in Microsoft Entra ID**

   * This application will act as a service principal for Airbyte to access your Key Vault
   * Navigate to **Microsoft Entra ID** > **App registrations** > **New registration**
   * Name your application (e.g., "Airbyte Secrets Manager")
   * Register the application

3) **Create a client secret for the application**

   * In your application, go to **Manage** > **Certificates & secrets** > **Client secrets**
   * Click **New client secret**
   * Add a description and choose an expiration period
   * Click **Add** and **save the secret value immediately** (it's only shown once)

4) **Assign the Key Vault Secrets Officer role to the application**

   * Navigate to your Azure Key Vault
   * Go to **Access control (IAM)**
   * Click **Add** > **Add role assignment**
   * Under **Role**, select **Key Vault Secrets Officer**
   * Under **Members**, select **User, group, or service principal**
   * Search for and select the application you created
   * Click **Review + assign** to complete the role assignment

5) **Collect the required information**:

   * **Vault URI**: Found in your Key Vault's Overview page (e.g., `https://your-vault-name.vault.azure.net/`)
   * **Tenant ID**: Found in Microsoft Entra ID > Overview
   * **Client ID**: Found in your application's Overview page
   * **Client Secret Value**: The secret value you saved in step 3

Contact your Airbyte representative for detailed GCP setup instructions.

***

## Step 4: Provide Configuration to Airbyte[​](#step-4-provide-configuration-to-airbyte "Direct link to Step 4: Provide Configuration to Airbyte")

Provide Airbyte with the configuration details using the appropriate JSON format for your cloud provider:

* AWS
* Azure
* Google Cloud

IAM Role Example:

```
{
  "auth_type": "IAM_ROLE",
  "roleArn": "arn:aws:iam::123456789012:role/AirbyteSecretsRole",
  "awsRegion": "us-east-1",
  "tagKey": "AirbyteManaged"
}
```

Access Key Example:

```
{
  "auth_type": "ACCESS_KEY",
  "awsAccessKey": "AKIAIOSFODNN7EXAMPLE",
  "awsSecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  "awsRegion": "us-west-2",
  "tagKey": "AirbyteManaged"
}
```

Example:

```
{
  "vaultUrl": "https://my-airbyte-vault.vault.azure.net/",
  "tenantId": "12345678-1234-1234-1234-123456789012",
  "clientId": "87654321-4321-4321-4321-210987654321",
  "clientSecret": "your-client-secret-value-here"
}
```

Configuration format will be provided by your Airbyte representative.

***

## Verification Steps[​](#verification-steps "Direct link to Verification Steps")

After providing your configuration to Airbyte:

1. Airbyte will create a test secret in your secrets manager

2. Verify the secret appears in your cloud provider's console:

   <!-- -->

   * **AWS**: Check AWS Secrets Manager in your specified region
   * **Azure**: Check your Azure Key Vault secrets
   * **GCP**: Check Google Cloud Secret Manager

3. Confirm the secret has the appropriate tags or identifiers (e.g., `AirbyteManaged=true` for AWS)

4. All future connection credentials will be stored as secrets in your external secrets manager

***

## Best Practices[​](#best-practices "Direct link to Best Practices")

### General Best Practices[​](#general-best-practices "Direct link to General Best Practices")

* **Use the most secure authentication method** available for your cloud provider and deployment type
* **Use specific tags or naming conventions** to differentiate Airbyte-managed secrets from other secrets
* **Monitor access logs** for your secrets manager (CloudTrail for AWS, Azure Monitor for Azure, Cloud Audit Logs for GCP)
* **Implement least privilege access** - only grant the minimum permissions required
* **Choose a region close to your Airbyte deployment** for better performance and lower latency

### AWS-Specific Best Practices[​](#aws-specific-best-practices "Direct link to AWS-Specific Best Practices")

* **Prefer IAM Roles over Access Keys** for enhanced security
* **Rotate access keys regularly** if using ACCESS\_KEY authentication
* **Restrict policy conditions** to only allow operations on tagged secrets

### Azure-Specific Best Practices[​](#azure-specific-best-practices "Direct link to Azure-Specific Best Practices")

* **Rotate client secrets regularly** before they expire
* **Use Azure Key Vault's built-in logging** to monitor access patterns
* **Consider using managed identities** where possible for additional security

***

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

* AWS
* Azure
* General

**Issue:** "Access Denied" errors when Airbyte tries to access Secrets Manager

**Solution:** Verify the IAM policy is correctly attached and the condition for the `AirbyteManaged` tag is properly configured

**Issue:** Secrets not appearing in AWS Console

**Solution:** Check that the correct AWS region is specified in the configuration

**Issue:** IAM Role authentication not working

**Solution:** Verify the trust relationship is configured correctly and the service account has the proper annotations

**Issue:** Authentication failures when accessing Key Vault

**Solution:** Verify the client secret is correct and has not expired. Check that the service principal has been assigned the Key Vault Secrets Officer role

**Issue:** "Access Denied" errors in Azure Key Vault

**Solution:** Confirm the application has the correct role assignment (Key Vault Secrets Officer) and that the role assignment has propagated (can take a few minutes)

**Issue:** Cannot find the Vault URI

**Solution:** Navigate to your Key Vault in the Azure Portal and copy the Vault URI from the Overview page

**Issue:** Test secret creation fails

**Solution:** Review your cloud provider's audit logs to identify the specific permission issue. Ensure all required permissions from Step 1 are correctly configured

**Issue:** Connection credentials not being stored externally

**Solution:** Verify that external secrets management is enabled for your Airbyte organization and that the configuration was successfully applied

***

## Security Considerations[​](#security-considerations "Direct link to Security Considerations")

* **Never commit credentials to version control** - always use secure methods to share configuration details with Airbyte
* **Regularly review and rotate credentials** - especially client secrets and access keys
* **Enable audit logging** - monitor all access to your secrets manager for suspicious activity
* **Use encryption** - ensure data is encrypted both in transit and at rest (most cloud providers enable this by default)
* **Implement network restrictions** where possible - limit access to your secrets manager to known IP ranges or VPCs
* **Set appropriate secret expiration policies** - configure automatic rotation where supported

***

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

### AWS[​](#aws "Direct link to AWS")

* [AWS Secrets Manager Documentation](https://docs.aws.amazon.com/secretsmanager/)
* [IAM Roles for Service Accounts (IRSA)](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)
* [Airbyte AWS Infrastructure Guide](https://docs.airbyte.com/platform/enterprise-setup/implementation-guide#aws-secret-manager-policy)

### Azure[​](#azure "Direct link to Azure")

* [Azure Key Vault Documentation](https://docs.microsoft.com/azure/key-vault/)
* [Microsoft Entra ID App Registration](https://docs.microsoft.com/azure/active-directory/develop/quickstart-register-app)
* [Airbyte Azure Infrastructure Guide](https://docs.airbyte.com/platform/enterprise-setup/implementation-guide#azure-key-vault-policy)

### GCP[​](#gcp "Direct link to GCP")

* [Google Cloud Secret Manager Documentation](https://cloud.google.com/secret-manager/docs)
* Contact your Airbyte representative for GCP-specific guidance

***

## Support[​](#support "Direct link to Support")

If you encounter issues not covered in this guide, please contact your Airbyte Customer Success representative or reach out to <support@airbyte.com>.
