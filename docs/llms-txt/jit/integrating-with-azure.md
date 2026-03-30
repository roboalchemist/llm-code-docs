# Source: https://docs.jit.io/docs/integrating-with-azure.md

# Azure Integration

Integrating with Azure

## Overview

Azure integration enables you to scan your Azure cloud infrastructure for [runtime misconfigurations](https://docs.jit.io/docs/scan-runtime-infra#azure-checklist). Integration with multiple concurrent subscriptions is not supported.

Though it does not require the integration steps below, Jit recommends that you also activate the [Scan IaC for Misconfigurations](https://docs.jit.io/docs/scan-iac-for-static-misconfigurations) security requirement for complete infrastructure protection.

## Prerequisites

The following are required before you can proceed with Azure integration

* A subscription to Azure Security.
* Microsoft Defender.

## Steps for integrating with Azure

**To integrate Jit with Microsoft Azure**

1. Create and configure an Azure app using the instructions in [Azure app setup](https://docs.jit.io/docs/integrating-with-azure#azure-app-setup).
2. From the Jit platform, select **Secrets** in the menu bar under **Settings**.
3. Follow the instructions in [Secrets](https://docs.jit.io/docs/secrets#creating-secrets) to create secrets for your Azure client ID and Azure client secret named `azure_client_id`, `azure_client_secret`, and `azure_subscription_ids`, respectively. You must use these exact names.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1614e9c-image.png",
        null,
        "Azure secrets example"
      ],
      "align": "center",
      "border": true,
      "caption": "Azure secrets example"
    }
  ]
}
[/block]

4. Select **Integrations**.
5. Locate the Azure tile and select **integrate-as-code**. You are taken to the `jit-integration.yml` file. Add the information below to this file. If the option to integrate as-code is not available, you may need to manually add`jit-integration.yml` to the repo containing Jit's configuration files.

```yaml jit-integration.yml (example)
azure:
  <integration_id>:
    type: azure_account
    name: "<your account name>"
    auth:
      client_id: "${{ jit_secrets.azure_client_id }}"
      client_secret: "${{ jit_secrets.azure_client_secret }}"
    tenant_id: <your Azure tenant ID>
    subscription_id: "${{ jit_secrets.azure_subscription_ids }}"
```

| Key                 | Value/description                                                                                                                                                                                           |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| azure:              | Integration type. Key must be `azure:`. The Azure integration is nested in this mapping.                                                                                                                    |
| \<integration\_id>: | This key is the name you choose for your Azure integration.                                                                                                                                                 |
| type:               | Enter `azure_account` as shown in the example.                                                                                                                                                              |
| name:               | Enter the name of your Azure account.                                                                                                                                                                       |
| client\_id:         | Enter exactly as shown in the example. To view this information in the Azure console, navigate to **App registrations** > (the app you created in step 1) > **Overview**.                                   |
| client\_secret:     | Enter exactly as shown in the example.                                                                                                                                                                      |
| tenant\_id:         | Enter your Azure tenant ID as shown in the example. To view this information in the Azure console, navigate to **App registrations** > (the app you created in step 1) > **Overview**.                      |
| subscription\_id:   | Enter your Azure subscription ID as shown in the example. To view this information in the Azure console, select your subscription from the *Resources* list on the home page, and then select **Overview**. |

## Azure app setup

### Create an app

1. In the [Azure Portal](https://portal.azure.com/#home), go to **App registrations.**

💡 Can’t find "App registrations"? Go to **Microsoft Entra ID** → **Manage** → **App registrations**.

2. Click  **+ New registration**.
3. Enter a name for the app (e.g., *jit-integration*).
4. Leave the rest of the defaults, then click **Register**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/41dc8a627ac1ed97709cbb391b8afbdaef63b66598b8712a037ed2082dbf9e52-image27.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b79bd51954b0e82005925936866528ae4efc560b9c2f9f9fd7a34f9ec1cb633a-image12.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/80372e41bebdf83a6f71413728dce6bf6df4f4a2d63f31bf2bf05f075a6e45bf-image28.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

### Add API Permissions

1. In your registered app, go to **API permissions** under the **Manage** section.
2. Click **+ Add a permission**.
3. Under **APIs my organization uses**, search for and select **Windows Azure Active Directory**.
4. Select **Delegated permissions**.
5. Expand the permission categories and check the following:
   * `Directory.Read.All`
   * `Group.Read.All`
   * `Policy.Read.All`
   * `User.Read.All`
6. Click **Add permissions**.

Repeat these steps to add:

* `user_impersonation` permission from **Azure Service Management API**.
* `User.Read` permission from **Microsoft Graph API**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a60bf91f88388fb5daa3cbe4a667a3d89478a79b439ec15aa314a6465c0faaef-image10.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/67e0cac2fbb5146e1469705a2917ffd2297b1d0e0212ab05c73148a27572e66e-image29.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

### Create an App Role

1. Select **App roles** from the *Manage* menu.

2. Select **Create app role**.

3. Fill in the fields:
   * **Display name**: Reader (or any meaningful name)
   * **Allowed member types**: Select **Both (Users/Groups + Applications)**
   * **Value**: reader
   * **Description**: e.g. reader app role

4. Check the box **Do you want to enable this app role?**

5. Click **Create**.

[block:image]{"images":[{"image":["https://files.readme.io/454cddc1b432cc1352289dc05c29ab42871d750e6db84aeea28d4bb7ee0cc630-image9.png","",""],"align":"center","sizing":"300px","border":true}]}[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c06ff07a44e25bae3bbbe0f17df40870010c8f4900adc21bfa950bbb2a7b7dea-image19.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

### Create a Client Secret

1. In the registered app, go to **Certificates & secrets** under the **Manage** section.
2. Click **+ New client secret**.
3. Enter a **Description** and select an **Expiration** period.
4. Click **Add**.

⚠️ Important: Copy the Value of the secret now, this is the only time you’ll be able to view it. You’ll need it later when setting up the Azure integration in Jit.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5cda623c61af681d4570c2f34c092e8aaa4170886f90e68a693b3e918e43a4fb-image30.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

### Retrieve Azure Identifiers

1. In your app’s **Overview** tab, copy the following:
   * **Application (client) ID** — used as *azure\_client\_id*
   * **Directory (tenant) ID** — used as *tenant\_id*\
     💡 You’ll use these values when configuring the integration in Jit.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a4137a32954369962e8a70cf1007556a8f76e475b09d21379997a29aa4e8a91b-image17.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

### Assign the App Role to Your Subscription

1. In the Azure Portal, go to **Subscriptions** and select your target subscription.
2. In the **Overview** tab, copy the **Subscription ID**, You will need it later in the integration process.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/9b82169d952d3c8e30804049a7a7b433fa0cbb9c47c73b96b73282523704b315-image14.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/95aeb5aa0779fd239c48248957be2357fb7a4070bed51168634e4ccc11f78447-image15.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

3. Go to **Access control (IAM)**.
4. Click **+ Add → Add role assignment**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/81e2c54a35b470e8b2ce0fd08fb94107a5b3a2ccc3549b19e0a874cac4433e90-image13.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

5. In the **Role** tab, search for the role name you created earlier (e.g., `Reader`) and select it.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d8dcf359b0fcb3eed08c637fd7d47c5ccf21276908bbe4cf16a8a472e17cc7d8-image22.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

6. In the **Members** tab:
   * Click **+ Select members**
   * Search for and select your registered app

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/03f23de8f13866f463450946a09438a3a9169a76d7c1f6a7e33139799782ab04-image5.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

7. Click **Review + assign** to complete the process.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/10349f46a635fbd50a29de0b6d2c11f0d97a406f5d41c295cff397756a933be1-image20.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e9bfa6ba59e269a568e3f10b79c1c12f2917c02459d0600e353e99ddc4f9e315-image31.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/acbbbefaf0ae048101f6169efc3f5d17c0da9044980701d0b75b11e323663474-image8.png",
        "",
        ""
      ],
      "align": "center",
      "border": true
    }
  ]
}
[/block]

## Limitations

Jit currently supports integration with one Azure subscription per tenant.