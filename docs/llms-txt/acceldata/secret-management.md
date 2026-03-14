# Source: https://docs.acceldata.io/documentation/secret-management.md

# Secret Management

Sensitive information like API keys, passwords, tokens, and cloud credentials are essential for your systems to operate — but storing them insecurely can expose your organization to major risks.

Data Plane requires access to sensitive values such as API keys, passwords, and cloud credentials in order to connect with external systems. To help protect this data, Dataplane supports different ways of **supplying and managing sensitive information**:

- **Environment Variables** – A simple method for passing configuration values to Dataplane at runtime. While convenient, this method is best suited for non-production or controlled environments.
- **AWS Secrets Manager** – A secure, managed service for storing and rotating secrets on AWS.
- **GCP Secret Manager** – A similar managed service for securely storing secrets on Google Cloud.

Note For production environments, it is strongly recommended to use a managed secret store (AWS or GCP) instead of relying solely on environment variables.

## How Data Plane Uses Secrets

At runtime, the Data Plane reads your configured secretmanager.json file and determines where to fetch secrets from (e.g., your environment variables, AWS Secrets Manager, or GCP). The secrets are injected into the services like the analysis engine, crawler, and pipelines during container startup.

This means:

- If you're using environment variables, the services read from env directly.
- If you're using AWS/GCP secret managers, the Data Plane fetches secrets at runtime using the appropriate SDK, based on the config you define.

Think of the secretmanager.json file as a “map” that tells the Data Plane where to fetch credentials from — and how.

## Where to Put Your Secrets

All secrets should be defined in a JSON file. This file tells the system where your secrets live and how to access them securely.

```none
/opt/acceldata/secretmanager.json
```



### Environment Variable-Based Secrets

| **Option** | **Description** | **When to Use** | **How to Configure** | 
| ---- | ---- | ---- | ---- | 
| Environment Variable-Based Secrets | This method allows you to provide credentials and other sensitive information directly via environment variables. It's a simple and lightweight approach, ideal for development, testing, or environments where secrets are securely managed by the operating system or container orchestration layer (like Kubernetes).  While convenient, this method is less secure than dedicated secret managers and should be used cautiously in production scenarios. | Quick testing or dev setups You already manage environment variables manually or through Kubernetes | Add this to /opt/acceldata/secretmanager.json:\n\n\n\n`[{"name": "secret-manager-environment", "type": "APP_ENV_VARIABLE_SECRETS_PROVIDER"}]` | 


### Secret Manager Options

| **Option** | **Description** | **When to Use** | **How to Configure** | 
| ---- | ---- | ---- | ---- | 
| AWS Secrets Manager | AWS Secrets Manager is a fully managed AWS service for storing, rotating, and securely accessing secrets like credentials, tokens, and certificates. | You're running on AWS You need built-in encryption, auditing, or auto-rotation | 1. Create a Secret in AWS Secret Manager. Refer [Create an AWS Secret Manager Secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html).\n2. Add this to /opt/acceldata/secretmanager.json:\n\n\n`[{"name": "secret-manager-aws", "type": "AWS_SECRETS_MANAGER", "details": {"secretName": "<name-of-your-aws-secret>", "accessKey": "<your-access-key>", "secretKey": "<your-secret-key>", "region": "us-east-1" }}]` | 
| GCP Secret Manager | GCP Secret Manager is a Google Cloud service that securely stores secrets and integrates tightly with IAM and GCP-native security features. | You're deploying on GCP You want to use IAM roles and GCP-native security features | 1. Create a Secret in GCP Secret Manager. Refer [Create a secret](https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets). \n2. Download the service account key as a JSON file. \n3. Save the file to: `/opt/acceldata/gcp_`cred.json``\n\n\nNote The file __`/opt/acceldata/gcp_cred.json` is how Data Plane knows how to log in to GCP. It contains your service account credentials so Dataplane can securely fetch secrets from GCP Secret Manager. \n\n\n\n4. Add this to /opt/acceldata/secretmanager.json: \n\n\n`[   {     "name": "secret-manager-gcp",     "type": "GCP_SECRETS_MANAGER",     "details": {       "credentialsFile": "/opt/acceldata/gcp_cred.json",       "projectId": "<your-gcp-project-id>"     }   } ]` | 
| Azure Key Vault | Azure Key Vault is a cloud service from Microsoft that securely stores secrets, keys, and certificates. It integrates with Azure Active Directory (AAD) for secure access management. | You're deploying on Azure You want to leverage AAD roles and native Azure security | 1. Create a Key Vault and Add a Secret Refer to [Create an Azure Key Vault and add a secret](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-portal) using the Azure Portal or CLI. \n2. Register an App in Azure AD \n\n\n- Create an App Registration in Azure Active Directory. \n- Generate a Client Secret and copy the values of: clientId, tenantId, clientSecret\n\n\n3. Grant the App Access to Key Vault \n\n\n- Go to your Key Vault. \n- Under Access Policies, grant the app Secret Get permissions. \n\n\n4. Create the credentials file Save the following JSON as `/opt/acceldata/azure_cred.json`: `{   "clientId": "<your-client-id>",   "tenantId": "<your-tenant-id>",   "clientSecret": "<your-client-secret>" }` \n\n\nNote The file `/opt/acceldata/azure_cred.json` allows the Dataplane to authenticate with Azure and securely access your Key Vault secrets. \n\n\n\n5. Add the following to `/opt/acceldata/secretmanager.json`: \n\n\n`[   {     "name": "secret-manager-azure",     "type": "AZURE_KEY_VAULT",     "details": {       "credentialsFile": "/opt/acceldata/azure_cred.json",       "vaultName": "<your-keyvault-name>"     }   } ]` | 


## Using Multiple Secret Managers

You can use more than one secret manager by adding multiple entries in the same secretmanager.json. This supports hybrid cloud setups or separate secrets for different components.

Suppose your organization has a hybrid cloud architecture:

- Your data processing infrastructure runs on AWS
- Your authentication service is deployed on Azure

You want to:

- Use AWS Secrets Manager to store credentials for your AWS-based Spark jobs
- Use Azure Key Vault to securely store tokens and API keys used by the authentication service

1. Create Secrets in Each Platform:
    1. In AWS Secrets Manager, create a secret named aws-spark-creds
    2. In Azure Key Vault, create a secret named auth-service-token

2. Update your secretmanager.json like this:

```json
[
  {
    "name": "secret-manager-aws",
    "type": "AWS_SECRETS_MANAGER",
    "details": {
      "secretName": "aws-spark-creds",
      "accessKey": "your-access-key",
      "secretKey": "your-secret-key",
      "region": "us-west-2"
    }
  },
  {
    "name": "secret-manager-azure",
    "type": "AZURE_KEY_VAULT",
    "details": {
      "credentialsFile": "/opt/acceldata/azure_cred.json",
      "vaultName": "my-auth-vault"
    }
  }
]
```



3. How It Works at Runtime:
    1. When your Spark job runs, it fetches credentials from AWS Secrets Manager
    2. Meanwhile, your authentication service running on a separate component can access secrets from Azure Key Vault

## Applying the Configuration

Once your secretmanager.json file is ready, follow these steps to apply it to your Dataplane deployment:

**1. Encode the File**

Manually convert both of the following files to **base64**:

- /opt/acceldata/secretmanager.json
- /opt/acceldata/gcp_cred.json (only if you're using GCP Secret Manager)

You'll need these base64 strings in the next steps.

**2. Load it into the existing Kubernetes secret**

Note When you install Acceldata Dataplane, it automatically creates a Kubernetes Secret resource named secret-manager.
If you're using GCP Secret Manager, you'll also need a separate Kubernetes Secret named gcp-cred to store the GCP credentials file.

**Step 1: Add the secretmanager.json to the secret-manager secret**

Open the secret in your default editor:

```bash
kubectl edit secret secret-manager -n <your-namespace>
```



In the data: section of the YAML file, find the secretmanager.json key and replace its value with your base64-encoded string:

```yaml
data:
  secretmanager.json: <your-base64-encoded-json>
```



Save and close the file.

**Step 2 (Only GCP & Azure): Add Credentials to Kubernetes Secrets**

**If you're using GCP, run:**

```bash
kubectl edit secret gcp-cred -n <your-namespace>
```



In the data: section, add or update the following:

```yaml
data:
  gcp_cred.json: <your-base64-encoded-gcp-cred>
```



Replace `<your-base64-encoded-gcp-cred>` with the base64-encoded contents of your GCP service account JSON file.

**If you're using Azure, run:**

```bash
kubectl edit secret azure-cred -n <your-namespace>
```



In the data: section, add or update the following:

```yaml
data:
azure_cred.json: <your-base64-encoded-azure-cred>
```



Replace `<your-base64-encoded-azure-cred>` with the base64-encoded contents of your Azure credential file (typically containing tenant ID, client ID, client secret, and subscription ID).

Save and close the file.

## Deploying the Changes

After updating the JSON file with the encoded secret, restart the data plane services by running the following command:

```bash
kubectl rollout restart deploy -n <your-namespace>
```



Once completed, navigate to the Data Plane's Application Configuration page in the UI to verify that the Secret Manager is properly set up.