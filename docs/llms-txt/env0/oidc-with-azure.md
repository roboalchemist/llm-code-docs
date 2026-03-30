# Source: https://docs.envzero.com/guides/integrations/oidc-integrations/oidc-with-azure.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OIDC for Azure

> Connect env zero to Azure using OIDC with an Azure AD App and Federated Credential configuration

This guide is to help you connect to Azure with OIDC, instead of using a Service Principal.

## Overview

This guide will show you how to create an Azure AD App, configure a Federated Credential, and configure env zero to utilize OIDC. The federated credential within the Azure AD app will be configured to accept env zero's OIDC token. Refer to [OIDC Integrations for more background on env zero's OIDC configuration](/guides/integrations/oidc-integrations).

## Azure AD App + Federated Credential

The Azure AD App will be configured with a Federated Credential in order to accept env zero OIDC token.  Using the Azure Portal:

1. Microsoft Entra ID > App registrations > "+ New Registration"
   1. Enter **Name**:  e.g. "env zero OIDC app"
   2. Select **Supported account types** if you're unsure, choose “Single tenant”
   3. Skip **Redirect URI**
   4. **Register** the app.
2. Under the "env zero OIDC app" > "Certificates and Secrets" > "Federated credentials"
   1. “+ Add credential”
   2. Federated Credential Scenario - **Other issuer**
   3. Issuer - `https://login.app.env0.com/`
   4. Subject Identifier - `auth0|xxxxxx` (see the section below on ["Retrieving your Subject Identifier"](/guides/integrations/oidc-integrations/oidc-retrieving-your-subject-identifier))
   5. Name - enter a name (e.g. "env0 OIDC")
   6. Audience - `https://prod.env0.com`
3. For using the Azure Provider in Terraform, we need to specify the following variables:
   1. `ARM_TENANT_ID` - you can find the value in your app registration summary ("env zero OIDC app") under "Directory (tenant) ID"
   2. `ARM_CLIENT_ID` - you can find the value in your app registration summary ("env zero OIDC app") under "Application (client) ID"
   3. `ARM_SUBSCRIPTION_ID` - You can retrieve the Subscription ID from the Azure Subscription, or in a Resource Group that you want to use.

## Azure App AD App Permissions

In order for Terraform to be able to deploy and manage the resources, we need to associate your Azure AD App with your Subscription or Resource Group

1. In this example, I will give the "env zero OIDC app" the "Contributor" role in my "sales-acme-demo" resource group.  This means that env zero will only be able to create and manage resources within this resource group.
2. Go to the Resource Group (”sales-acme-demo”) > Access Control (IAM)
3. Click on “+ Add” > “Add role assignment”\
   <img src="https://mintcdn.com/envzero-b61043c8/t0QBBK-2O7wlTUvX/images/guides/integrations/oidc-integrations/f5afe58-sales-acme-demo_-_microsoft_azure-2022-10-03_at_11.png?fit=max&auto=format&n=t0QBBK-2O7wlTUvX&q=85&s=c6ec8a2f0ac732a6a7fd2d2cc2730190" alt="" width="985" height="344" data-path="images/guides/integrations/oidc-integrations/f5afe58-sales-acme-demo_-_microsoft_azure-2022-10-03_at_11.png" />
4. Select a role (the level of privilege to give to Terraform) - in this case, we choose “Contributor” and hit “Next”
5. Assign access to “User, group, or service principal”
6. Select a member by “+ Select Members”
7. Search for "env zero OIDC app" and hit "Select"
8. Hit "Review + assign"\
   <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/93bb447-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=b4cd3cfbce73b4de3cd4cfac07e1897d" alt="" width="1122" height="491" data-path="images/guides/integrations/oidc-integrations/93bb447-image.png" />

## Configure env0 OIDC Credential

Go to the organization's credentials page and create a new deployment credential. Select `Azure OIDC` type and enter the following fields:

* `Subscription ID` - Azure subscription id
* `Tenant ID` - Azure tenant id
* `Client ID` - Azure client id

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/f50k_bxcw7fbjToJ/images/guides/integrations/oidc-integrations/095b186-image.png?fit=max&auto=format&n=f50k_bxcw7fbjToJ&q=85&s=560b8d1cef597bc957e91f281cd23843" alt="Interface screenshot showing configuration options" width="1126" height="1448" data-path="images/guides/integrations/oidc-integrations/095b186-image.png" />
</Frame>

<Warning>
  Azure Provider Version

  Make sure you use a version of the Azure provider greater than 3.7.0.\
  OIDC did not work for "=3.7.0"
</Warning>

### Assign your Credential in your Project

After creating your Organization Credential - don't forget to go into your Project Settings to use the OIDC credential you just created.

## Deploying to multiple Azure Subscriptions

Sometimes you want to be able to deploy to multiple Azure Subscriptions in one Terraform workspace.  In Terraform / OpenTofu, you can specify multiple azure provider blocks in order to target mutliple subscriptions, see example below:

```go Terraform / OpenTofu (hcl) theme={null}
provider "azurerm" {
  features {}
  use_oidc = true
  //subscription_id = "b48787a1-7145-425f-99af-62cde6c50e31" (optional)
  //env zero will use the subscription ID in defined in the Azure OIDC project credential configuration
}

provider "azurerm" {
  alias = "test"
  features {}
  use_oidc = true
  subscription_id = var.second_subscription
}

variable "second_subscription" {
  type = string
  default = "3ef32f99-33d5-4a4f-bf9c-8a3ebb2b0144"
}

resource "azurerm_resource_group" "example" {
  name     = "env0-example-rg"
  location =  "eastus2"
}

resource "azurerm_resource_group" "second" {
  provider = azurerm.test
  name     = "env0-example-second-rg"
  location =  "eastus2"
}
```

By simply, ensuring that the same App Registration created earlier ("env zero OIDC App") has permissions in the both subscriptions; you can utilize one set of credentials to target multiple subscriptions.

Built with [Mintlify](https://mintlify.com).
