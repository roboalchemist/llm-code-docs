# Source: https://docs.datadoghq.com/cloudcraft/getting-started/connect-azure-account-with-cloudcraft.md

---
title: Connect your Azure Account with Cloudcraft
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Cloudcraft (Standalone) > Getting started > Connect your Azure Account
  with Cloudcraft
---

# Connect your Azure Account with Cloudcraft

This article walks you through connecting your Azure account to Cloudcraft.

## Requirements{% #requirements %}

- A Cloudcraft user with the [Owner or Administrator role](https://docs.datadoghq.com/cloudcraft/account-management/roles-and-permissions/).
- An active [Cloudcraft Pro subscription](https://www.cloudcraft.co/pricing).
- An Azure account with permission to create IAM roles.

## Manage Azure accounts{% #manage-azure-accounts %}

### Add account{% #add-account %}

1. In Cloudcraft, navigate to **User** > **Azure accounts**.
1. At the bottom of the modal, click **Add Azure Account**.
1. The next page provides step-by-step instructions. Click **Select "App registrations" in the left sidebar** to register a new application to interface with Cloudcraft in Azure.
1. On the **App registrations** page in **Azure Active Directory**, click **New registration**.
1. Enter the following information:
   - **Name**: Cloudcraft
   - **Supported account types**: Accounts in this organizational directory only (Single tenant)
   - **Redirect URI**: Leave this field blank.
1. Click **Register**.
1. On the details page of your application, copy the **Application ID** and **Directory ID**.
1. In Cloudcraft, paste the **Application ID** and **Directory ID**, then click **Next**..

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-azure-account-with-cloudcraft/essential-ids-cloudcraft.c98ea4d73c5d5c7c8779dda9e75163c9.png?auto=format"
   alt="Step-by-step instructions for adding an Azure account to Cloudcraft with highlighted Application and Directory ID fields." /%}

#### Create a client secret{% #create-a-client-secret %}

Next, create a client secret to allow the Cloudcraft application to securely identify itself to Azure's authentication services.

**Note**: You can choose your own expiration period for the client secret. Be aware that when the secret expires, you won't be able to scan your Azure account until you register a new secret and update the account in Cloudcraft.

1. On your application page in Azure, under the **Manage** section in the left sidebar, click **Certificates & secrets**.
1. In the **Certificates & secrets** section, **New client secret**.
1. Enter the following information:
   - **Description**: Cloudcraft
   - **Expires**: 730 days (24 months)
1. Click **Add**.
1. Copy the **Value** of your newly created secret.
1. In Cloudcraft, paste the client secret in the **Client secret** field and click **Next**.

#### Create an IAM user for Cloudcraft{% #create-an-iam-user-for-cloudcraft %}

Finally, create an IAM user to allow the Cloudcraft application to read your Azure environment.

1. In Cloudcraft, click **Open your Azure Subscriptions page** link to open the **Subscriptions** page in Azure.
1. Select the subscription you want to use with Cloudcraft.
1. On subscription page, select **Access control (IAM)** in the left sidebar.
1. Click **Add** and select **Add role assignment**. A new page with a list of roles appears.
1. Select **Reader** and click **Next**.
1. On the next page, leave **User, group or service principal** selected and click **Select members**. Search for **Cloudcraft** and select it.
1. Click **Review + assign**.
1. In Cloudcraft, click **Next**.

#### Add subscriptions{% #add-subscriptions %}

Before saving the account, you can optionally configure team access.

1. Click **Team access** and select the teams to share access to the Azure account with. The account will be private and only accessible to you if you skip that step.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-azure-account-with-cloudcraft/share-azure-account.8248769394a6c8590628418b61944e46.png?auto=format"
   alt="Cloudcraft interface showing team sharing options with a dropdown menu for selecting teams to share Azure account access." /%}
Click **Save Account**.
Your Azure account is now ready to use with Cloudcraft.

{% image
   source="https://datadog-docs.imgix.net/images/cloudcraft/getting-started/connect-azure-account-with-cloudcraft/azure-account-added.56ddffcbfe13f6ce598e76b85c9d4bf5.png?auto=format"
   alt="Screenshot of Cloudcraft interface for managing Azure accounts with an account added." /%}

## Edit account{% #edit-account %}

To edit an account, click the gray pencil icon to the left of the account you want to edit. You can change details of the account, such as the name, ARN, and team access.

When you are done, click **Save Account**.

## Remove account{% #remove-account %}

To remove an account, click the trash can icon to the right of the account you want to remove, then click **Remove**.
