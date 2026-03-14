# Source: https://docs.envzero.com/guides/getting-started/getting-started/connect-your-cloud-account.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Your Cloud Account

> Grant env zero permissions to manage resources in your AWS, Azure, or GCP cloud account

env zero applies your infrastructure code to create resources in your own cloud account. It requires only the necessary permissions to manage your cloud resources on your behalf.

This includes permissions to create, update, and delete any type of cloud resource you want env zero to manage.

Here, you will learn how to grant env zero the required permissions.

## Credentials Management

When creating a credential in env zero, it can be assigned to one of two scopes: `Organization` or `Project`.

* **Organization Scope**: When a credential is created via the organization credentials page (Organization Settings > Credentials), it is assigned to the `Organization` scope. This makes it available to all projects within the organization.
* **Project Scope**: When a credential is created via the project credentials page (Project Settings > Credentials), it is assigned to the `Project` scope. This makes it available to that specific project and any of its sub-projects.

All credentials, regardless of scope, are visible on the organization credentials page. To create or update credentials in a specific scope, you must have the `MANAGE_CREDENTIALS` permission at that scope level (organization or project). By default, both `Project Admin` and `Organization Admin` roles include this permission.\
For example, to create or edit credentials in the project "My Project," you need the `MANAGE_CREDENTIALS` permission for that project.

### Use case example

A common reason to scope credentials is to separate access between environments. For instance, if you have distinct development and production projects, you can ensure that users in the development project do not have access to production credentials.

## Amazon Web Services (AWS)

env zero offers three ways for you to connect to your AWS account:

1. Using AWS Assume Role
2. Using IAM user credentials
3. Using [OIDC](/guides/integrations/oidc-integrations/oidc-with-aws)

### Using AWS Assume Role

This role will be assumed by env zero during a deployment.\
It will require all permissions required including `GetAccessKeyInfo`.

#### Create an AWS IAM Role

1. Click on Roles,  then click on Create Role
2. Under type of trusted entity, select AWS Account
3. Under An AWS account ID, select 'An AWS account' and enter `913128560467`.\
   `If you have a self-hosted agent installation you should enter the AWS account ID where the agent is installed`
4. Select Require External ID
5. Enter an External ID. The value must be equal to your Organization ID
6. Click Next:Permissions
7. Select AdministratorAccess or whatever policies are required by your IaC
8. Click Next:Review
9. Enter a name for the role, and click Create Role
10. Click on the role you just created. We will need the `Role ARN` in subsequent steps

<Info>
  **Assume Role Duration**

  To edit the duration of the Assume Role, go to the Created Role screen and locate Maximum Session Duration. Click Edit and select your relevant duration.
</Info>

<Warning>
  When you create the credentials in env zero, please make sure to select the correct duration. It must be equal to or less than the selected duration in AWS.
</Warning>

#### Add your Role ARN and External ID configuration to env zero (via CloudFormation)

You can use the following CloudFormation Template or Terraform HCL to create the AssumeRole

<CodeGroup>
  ```yaml CloudFormation(yaml) theme={null}
  AWSTemplateFormatVersion: '2010-09-09'
  Parameters:
    ExternalId:
      Type: String
      Default: external-id
    SessionDuration:
      Type: Number
      Default: 3600
  Resources:
    AssumeRole:
      Type: AWS::IAM::Role
      Properties:
        RoleName: Env0-AssumeRole
        Description: |
          Used by env zero to automate the deployment of Infrastructure from a Version Control System
        AssumeRolePolicyDocument: !Sub |
          {"Version": "2012-10-17",
              "Statement": [
                  {
                      "Effect": "Allow",
                      "Action": "sts:AssumeRole",
                      "Principal": {
                          "AWS": "913128560467"
                      },
                      "Condition": {
                          "StringEquals": {
                              "sts:ExternalId": "${ExternalId}"
                          }
                      }
                  }
              ]
          }
        ManagedPolicyArns:
          - arn:aws:iam::aws:policy/AdministratorAccess
        MaxSessionDuration: !Ref SessionDuration
        Tags:
          - Key: Owner
            Value: env zero
  Outputs:
    ExternalId:
      Value: !Ref ExternalId
      Description: "ExternalID for env zero"
    AssumeRoleArn:
      Value: !GetAtt AssumeRole.Arn
  ```

  ```hcl Terraform (HCL) theme={null}
  terraform {
    required_providers {
      aws = {
        source  = "hashicorp/aws"
        version = "~> 4.36.0"
      }
      env0 = {
        source  = "env0/env0"
        version = ">= 1.15"
      }
    }
  }

  provider "env0" {
    # env zero Provider expects to find the environment variables defined.
    # to create an API key see:  /api-keys
    # ENV0_API_KEY    
    # ENV0_API_SECRET
    # or using tf provider variables
    # api_key = ""
    # api_secret = ""
  }

  provider "aws" {
    region = var.region
  }

  ### VARIABLES

  variable "region" {
    type    = string
    default = "us-east-1"
  }

  variable "assume_role_name" {
    type        = string
    default     = "env0-deployer-role"
    description = "name used for both env zero and AWS"
  }

  variable "managed_policy_arns" {
    type        = list(string)
    default     = ["arn:aws:iam::aws:policy/AdministratorAccess", ]
    description = "list of policy arns to assign to env zero's deployer"
  }

  variable "organization_id" {
    type        = string
    description = "env zero org id found under Organization > Settings"
  }
  ### RESOURCES 

  resource "aws_iam_role" "env0_deployer_role" {
    name = var.assume_role_name

    max_session_duration = 18000 # env zero requirement, 5 hours for SaaS

    # Change to your policy
    managed_policy_arns = var.managed_policy_arns

    # 913128560467 is env0's AWS Account ID
    # see: /guides/getting-started/getting-started/connect-your-cloud-account/#using-aws-assume-role
    assume_role_policy = jsonencode({
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Effect" : "Allow",
          "Principal" : {
            "AWS" : "arn:aws:iam::913128560467:root"
          },
          "Action" : "sts:AssumeRole",
          "Condition" : {
            "StringEquals" : {
              "sts:ExternalId" : "${var.organization_id}"
            }
          }
        }
      ]
    })

    tags = {
      note = "Created through env0 Bootstrap"
    }
  }

  # optional to manage your env0 resources using env0's terraform provider
  resource "env0_aws_credentials" "credentials" {
    name        = aws_iam_role.env0_deployer_role.arn #easier to track in the UI which role exactly is being used
    arn         = aws_iam_role.env0_deployer_role.arn
  }
    
  output "role_arn" {
    value = aws_iam_role.env0_deployer_role.arn
  }
  ```

</CodeGroup>

Next, run the following AWS CLI command to deploy the CloudFormation Stack

```shell  theme={null}
aws cloudformation deploy \
--stack-name assume-role-env0 \
--template-file ./assume-role-env0.yml \
--capabilities CAPABILITY_NAMED_IAM \
--parameter-overrides ExternalId=YOUR_ORGANIZATION_ID SessionDuration=SESSION_DURATION
```

The `RoleArn` will be available in the Outputs tab of your CloudFormation stack.

<Info>
  For security reasons, the ExternalID is resolved on the backend to be your organization ID.
</Info>

#### Add your Role ARN configuration to env0 (via Manual Configuration)

1. Go to the Settings page, and pick the Credentials tab
2. Under Cloud Credentials section, click + Add Credential

<Frame caption="Cloud Credentials">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2856.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=d435a7c52562100d296f5d3311453e75" alt="Cloud Credentials interface showing Add Credential button and credential management options" width="2856" height="854" data-path="images/guides/getting-started/getting-started/2856.png" />
</Frame>

1. Enter a name for the new credential
2. Under Type, pick AWS Assumed Role
3. Under Role ARN, enter your role ARN
4. Note that your External ID is pre-filled with your env0 Organization ID
5. Choose the duration for the deployment's assumed role (make sure it is equal or less than the duration you set in AWS)
6. Click Add
7. Go to the project for which you'd like to use this role, then click Project Settings and click Credentials
8. Pick the credential you would like to use in this project, this project, then click Add

<Frame>
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/f8a8d20-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=a4fda8bf8a5d780763c6a36ad698c9d1" alt="Project credentials interface showing how to pick AWS credential for the project" width="524" height="609" data-path="images/guides/getting-started/getting-started/f8a8d20-image.png" />
</Frame>

<Frame caption="Picking AWS credential for the project">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2846.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=ce3b7e9ad49b44c98cd972bdd89d1b19" alt="Project settings interface showing credential selection for AWS assumed role" width="2846" height="634" data-path="images/guides/getting-started/getting-started/2846.png" />
</Frame>

<Info>
  **Change Assumed Role per Environment**

  If you'd like to override the project's Assumed Role and use a different Assumed Role for a specific environment, set the following environment variables:

* A variable called `ENV0_AWS_ROLE_ARN`- set its value to be the role ARN
* A variable called `ENV0_AWS_ROLE_EXTERNAL_ID`- its value to your [Org ID](/guides/admin-guide/organizations/#finding-my-organization-id)

  To customize the duration per environment, create a variable called`ENV0_AWS_ROLE_DURATION`, and set its value to the desired duration in seconds. AWS uses a default value of 3600s (1 hour), while env zero uses a default value of 18000s (5 hours).
</Info>

### Using AWS user credentials

#### Create IAM Role & Permissions

1. To connect your AWS account, you will need to create an IAM user with programmatic access. See [this guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) on how to do that. Make sure you save your **Access Key ID** and **Secret Access Key**.
2. You will need to grant this user the appropriate permissions in order to deploy the resources defined in your IaC code.

#### Add Your Credentials to env zero

1. Go to Settings and click the Credentials tab
2. Under Cloud Credentials, click + Add Credential

<Frame caption="Cloud Credentials">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2856.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=d435a7c52562100d296f5d3311453e75" alt="Cloud Credentials interface showing credential management options" width="2856" height="854" data-path="images/guides/getting-started/getting-started/2856.png" />
</Frame>

1. Enter a name for the new credential
2. Under Type, pick AWS Access Keys
3. Under Access Key ID, enter your Access Key ID
4. Under Secret Access Key, enter the value of your Secret Access Key
5. Click Add

<Warning>
  **Secret Access Key in a Self-Hosted Agent**

  If your organization is managed in a Kubernetes Self-Hosted Agent, you must reference an existing AWS, GCP or Azure secret manager variable instead of typing the actual secret Secret Access Key.

  Read more [here](/guides/admin-guide/self-hosted-kubernetes-agent/#sensitive-secrets)
</Warning>

<Frame caption="AWS Access Keys">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/1024.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=04e1d906ea6b704e24272f2073cd3d0b" alt="AWS Access Keys configuration interface" width="1024" height="1006" data-path="images/guides/getting-started/getting-started/1024.png" />
</Frame>

1. Go to the project for which you'd like to use this role, then go to Project Settings and click Credentials
2. Pick the credential you would like to use in this project, and then click on Save

<Frame caption="Picking AWS credential for the project">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2854.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=ef2042922734c4ed27f53e228d9089e6" alt="Project credentials interface showing AWS credential selection" width="2854" height="638" data-path="images/guides/getting-started/getting-started/2854.png" />
</Frame>

## Google Cloud (GCP)

### Create a Service Account

In order to connect your GCS account, you will need to create a Service Account Key. See this guide on how to create one. Make sure to save the JSON key contents.

### Add Your Credentials to env zero

1. Go to the Settings page and click the Credentials tab
2. Under Cloud Credentials, click + Add Credential

<Frame caption="Cloud Credentials">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2856.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=d435a7c52562100d296f5d3311453e75" alt="Cloud Credentials interface showing credential management options" width="2856" height="854" data-path="images/guides/getting-started/getting-started/2856.png" />
</Frame>

1. Enter a name for the new credential.
2. Under Type, pick Google Cloud Service Account
3. Under Project ID, enter your GCP project name (optional)
4. Under Secret Account Key, copy and paste the JSON key contents directly into the value of this variable
5. Click Add

<Warning>
  **Secret Account Key in a Self-Hosted Agent**

  If your organization is managed in a Kubernetes Self-Hosted Agent, you must reference an existing AWS, GCP or Azure secret manager variable instead of typing the actual secret Secret Account Key.

  Read more [here](/guides/admin-guide/self-hosted-kubernetes-agent/#sensitive-secrets)
</Warning>

<Frame caption="Google Cloud Service Account">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/1024.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=04e1d906ea6b704e24272f2073cd3d0b" alt="AWS Access Keys configuration interface" width="1024" height="1006" data-path="images/guides/getting-started/getting-started/1024.png" />
</Frame>

1. Go to the project for which you'd like to use this role, and then go to Project Settings and click Credentials
2. Pick the credential you would like to use in this project, then click Save

<Frame caption="Picking GCP credential for a project">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2834.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=98dd27705fb02441b9ef9fb5b1a8a060" alt="Project credentials interface showing GCP credential selection" width="2834" height="636" data-path="images/guides/getting-started/getting-started/2834.png" />
</Frame>

## Using OIDC with GCP

See instructions [here](/guides/integrations/oidc-integrations/oidc-with-google-cloud-platform).

## Azure

### Create a Service Principal

In order to access resources a **Service Principal** needs to be created in your Tenant.\
This is easiest to do via the AZ CLI.

1. First, make sure you are logged in:

   ```bash  theme={null}
   az login
   ```

   Follow the instructions to login
2. Once logged in, your subscriptions will be returned:

   ```json5  theme={null}
   [
     {
       "cloudName": "AzureCloud",
       "id": "2d7e700a-8793-45ff-ba0a-9d92d15edf56", // this is your Subscription ID
       "isDefault": "true",
       "name": "Pay-As-You-Go",
       "state": "Enabled",
       "tenantId": "e522969-635a-4327-8807-7f7aac328e82",
       "user": {
         "name": "who@outlook.com",
         "type": "user"
       }
     }
   ]
   ```

3. Next, set your active subscription:

   ```bash  theme={null}
   az account set --subscription="${id}"
   ```

4. Create a Service Principal for env zero to deploy your terraform stack:

   ```bash  theme={null}
   az ad sp create-for-rbac -n "${name-of-your-choice}"
   ```

   This will return the metadata for your Service Principal:

   ```json5  theme={null}
   {
     "appId": "2dc2b1b3-11dd-4eb5-845-84fc-5bda87620cea", // this is your Client ID
     "displayName": "who",
     "name": "http://who",
     "password": "ab735025-151e-4337-b154-b7833d6929a9",  // this is your Client Secret
     "tenant": "5c8c7547-dd3f-4750-a8d9-f2e04e6015ba"     // this is your Tenant ID
   }
   ```

<Warning>
  Make sure the new Service Principal has the necessary permissions. [Learn how to assign a role in Azure.](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal#step-6-select-assignment-type)
</Warning>

### Add Your Credentials to env zero

1. Go to the Settings page, and click on the Credentials tab
2. Under the Cloud Credentials section, click + Add Credential

<Frame caption="Cloud Credentials">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2856.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=d435a7c52562100d296f5d3311453e75" alt="Cloud Credentials interface showing credential management options" width="2856" height="854" data-path="images/guides/getting-started/getting-started/2856.png" />
</Frame>

1. Enter a name for the new credential
2. Under Type, pick Azure Service Principal
3. Under Client ID, enter your service principal app ID
4. Under Client Secret, enter your service principal password
5. Under Subscription ID, enter your subscription ID
6. Under Tenant ID, enter your service principal tenant ID
7. Click Add

<Warning>
  **Client Secret in a Self-Hosted Agent**

  If your organization is managed in a Kubernetes Self-Hosted Agent, you must reference an existing AWS, GCP, or Azure secret manager variable instead of typing the actual secret Client Secret.

  Read more [here](/guides/admin-guide/self-hosted-kubernetes-agent/#sensitive-secrets).
</Warning>

<Frame caption="Azure Service Principal">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/1018.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=a1d381e17450ba8814397be5fa264cfe" alt="Azure Service Principal configuration interface" width="1018" height="1318" data-path="images/guides/getting-started/getting-started/1018.png" />
</Frame>

1. Select the project for which you'd like to use this role, then go to Project Settings and click Credentials
2. Pick the credential you would like to use in this project, then click Save

<Frame caption="Picking Azure credential for project">
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2860.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=6935ce1947f0709cbcffb815df762245" alt="Project credentials interface showing Azure credential selection" width="2860" height="642" data-path="images/guides/getting-started/getting-started/2860.png" />
</Frame>

<Info>
  **Change Credentials per Environment**

  If you'd like to override the project's Credentials and use a different Credentials for a specific environment, set the following environment variables:

  <Info>
    * A variable called `ARM_TENANT_ID`- set its value to be the "service principal tenant ID"
    * A variable called `ARM_SUBSCRIPTION_ID`- set its value to be the "subscription ID"
    * A variable called `ARM_CLIENT_SECRET` - set its value to be the "service principal password"
    * A variable called `ARM_CLIENT_ID` - set its value to be the "service principal app ID"
  </Info>
</Info>

## Using OIDC with Azure

See instructions [here](/guides/integrations/oidc-integrations/oidc-with-azure).

## Oracle Cloud Infrastructure (OCI)

### Create an OCI API Key

To create a personal API Key in OCI:

1. Login to OCI
2. Click on your profile pic, and go to User Settings
3. Under the Resources section, click on API Keys, and the Add API Key
4. When you create an API Key, you will be prompted to download a **Private** RSA Key. Download it and save it for later, you're going to need it
5. Finally, click Save
6. After you create the API key, you'll be prompted with a Configuration file preview. Save it as well

### Add Your Credentials to env zero

1. Go to the Settings page and click the Credentials tab
2. Under Cloud Credentials, click + Add Credential

<Frame>
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2856.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=d435a7c52562100d296f5d3311453e75" alt="Organization credentials interface showing credential management options" width="2856" height="854" data-path="images/guides/getting-started/getting-started/2856.png" />
</Frame>

1. Enter a name for the new credential
2. Under Type, pick OCI API Key
3. Under Tenancy OCID, copy the tenancy from the configuration file preview
4. Under User OCID, copy the user from the configuration file preview
5. Under OCI Region, pick the region that matches the one in the configuration file preview
6. Under API Key Fingerprint, copy the fingerprint from the configuration file preview
7. Under API Key Private Key, copy the private RSA key you downloaded

<Warning>
  When generating a private RSA key via OCI, it's followed by `OCI_API_KEY` after the key ends.\
  Remove that section.
</Warning>

## Other Cloud Providers

If you are using Terraform to manage infrastructure in a different provider than the ones mentioned above, you will need to check the provider’s documentation to understand what authentication options are supported.

Generally, you should be able to use specific environment variables for authorization. Same as all the above options, you'll be able to separate your credentials into projects/environments as you see fit.

## Customizing Cloud Authentication per Environment

Generally, Cloud Credentials are defined per env zero project. These are translated into environment variables at runtime (like AWS\_ACCESS\_KEY\_ID and AWS\_ACCESS\_SECRET\_KEY for AWS). If you'd like to give different credentials to a specific environment, you could simply override the desired environment variables during deployment.

# Kubernetes

env zero applies your IaC to create resources in your own Kubernetes cluster. Here you will learn how to give env zero the required permissions to do just that.

We support major cloud provider managed clusters, as well as a general `kubeconfig` file.

<Tip>
  **Easy Authentication for Terraform and Pulumi**

  While Helm and Kubernetes templates enjoy native support, env zero also enables seamless Kubernetes authentication integration within Terraform and Pulumi templates. These connect to your cluster by automatically creating the `kubeconfig` file in the deployment container.

  Follow our code examples for [Terraform](https://github.com/env0/templates/tree/master/kubernetes/using-terraform) and [Pulumi](https://github.com/env0/templates/tree/master/kubernetes/using-pulumi) for easy configuration.
</Tip>

### Set Up Kubernetes Credential

Navigate into Organization Settings and click Credentials\
Under Deployment Credentials, click + Add Credential

<Frame>
    <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/e6b972d-org_credentials.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=4a265a99594737b9e447192a85743530" alt="Organization credentials interface showing credential management options" width="2090" height="1050" data-path="images/guides/getting-started/getting-started/e6b972d-org_credentials.png" />
</Frame>

Inside the opened modal, select your desired Kubernetes Cluster authentication method.

## Kubeconfig

If you want to allow connection to your custom cluster, you can do so by setting up a `kubeconfig` credential in env zero's UI.

Select the Kubernetes Kubeconfig File credential from the Type dropdown menu and paste your valid`kubeconfig` file.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/1f684ff-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=cac5c184ac281675e39d2d8ebe68a7cb" alt="" width="517" height="620" data-path="images/guides/getting-started/getting-started/1f684ff-image.png" />

<Info>
  **Constraints**

  Your `kubeconfig` hould contain exactly one cluster, context and user. The `current-context` field must be provided, and match the given context.
</Info>

Next, you'll need to associate the created credential with your project.

Under Project Settings, click the Credentials tab. Then, check the Kubernetes checkbox and select the credential you created from the dropdown menu.

<img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/08/05779aa-image.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=827fad77a8de9d0f1f239794ada27e2a" alt="" width="1637" height="548" data-path="images/changelogs/2023/08/05779aa-image.png" />

## AWS EKS

Select the Kubernetes - AWS EKS Configuration credential from the Type dropdown menu, then enter your cluster name and region.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/1749784-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=df7c9f0de182e0d29145b765a64d8487" alt="" width="515" height="524" data-path="images/guides/getting-started/getting-started/1749784-image.png" />

Next, you'll need to associate your EKS credential with your project.

In your Project Settings, click on the Credentials tab. Check the Kubernetes checkbox and select the credential you created from the dropdown menu.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/088e321-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=908cadcf526f3c2d1e2f4a24305f879d" alt="" width="1393" height="328" data-path="images/guides/getting-started/getting-started/088e321-image.png" />

<Info>
  **Credentials**

  In order to access your cluster, you'll also need to set valid [AWS credentials](/guides/getting-started/getting-started/connect-your-cloud-account/#amazon-web-services-aws).
</Info>

## GCP GKE

Select the Kubernetes - GCP GKE Configuration credential from the Type dropdown menu and enter your cluster name and region.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/ad7e32a-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=b5146f106479ce9ac1ae6467576de6e5" alt="" width="516" height="522" data-path="images/guides/getting-started/getting-started/ad7e32a-image.png" />

Next, you'll need to associate the GKE credential with your project.

In your Project Settings, click on the Credentials tab. Then, check the Kubernetes checkbox and select the credential you created from the dropdown menu.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/9fad3e1-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=98849353edd6931dfaf17ca2d33fd506" alt="" width="895" height="327" data-path="images/guides/getting-started/getting-started/9fad3e1-image.png" />

<Info>
  **Credentials**

  In order to access your cluster, you'll also need to set valid [GCP credentials](/guides/getting-started/getting-started/connect-your-cloud-account/#google-cloud-gcp).
</Info>

## Azure AKS

Select the Kubernetes - Azure AKS Configuration credential from the Type dropdown menu and enter your cluster name and resource group.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/054d70f-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=2a26697924bf859578a15aed89c24139" alt="" width="513" height="518" data-path="images/guides/getting-started/getting-started/054d70f-image.png" />

Next, you'll need to associate the AKS credential with your project.

In your Project Settings, click on the Credentials tab. Then, check the Kubernetes checkbox and select the credential you created from the dropdown menu.

<img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/982db9c-image.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=84864488f907ac0db2898d4313ba15bd" alt="" width="895" height="329" data-path="images/guides/getting-started/getting-started/982db9c-image.png" />

<Info>
  **Credentials**

  In order to access your cluster, you'll also need to set valid [Azure credentials](/guides/getting-started/getting-started/connect-your-cloud-account/#azure).
</Info>

Built with [Mintlify](https://mintlify.com).
