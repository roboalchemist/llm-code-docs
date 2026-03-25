# Source: https://help.aikido.dev/virtual-machine-scanning/azure/setup-configuration-in-azure.md

# Azure VM Access Configuration

## Entra ID App Registration

Log into your [**Azure Portal**](https://portal.azure.com/) and navigate to the **Microsoft Entra ID service**.

Click on **Add** and select **App registration**

![Azure portal: Add new user, group, enterprise app, or app registration in Default Directory.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-53332ba9e377b1992be07aa2b26515a9012923f8%2Fsetup-configuration-in-azure_e77457d8-318c-4766-947f-86a94c8b0e1a.png?alt=media)

Give the application a meaningful name, we need this name later.

Leave the **Supported account types** default: **Accounts in this organizational directory only**.

Click on **Register**.

![Azure portal screen for registering a new application named "AikidoSecurity" with account type selection.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c57ebacda5c9c707705a273faf0d6cc031e393bc%2Fsetup-configuration-in-azure_4690d5db-e42d-4d8d-93a0-b978333c1364.png?alt=media)

You get redirected to the detail page of the newly created application. Here you can find and copy the **Application (client) ID** and the **Directory (tenant) ID**

![Azure portal showing AikidoSecurity application's client ID and essential overview details.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5568f22ce6811e7894c5b9d23ee50f41c8f45189%2Fsetup-configuration-in-azure_4ce56e1e-0436-430e-8492-e4e85120a1d3.png?alt=media)

At the client credentials field, click "Add a certificate or secret"

![Azure portal displaying AikidoSecurity app overview and client credential configuration options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cdec5321abc1ef9cce6200cab6701be1b8fdcece%2Fsetup-configuration-in-azure_a250622e-201f-4711-a957-e3aba87db480.png?alt=media)

Click the "New client secret"-button, give a description for the secret and set the expiration date to 2 years (730 days / 24 months)

![Creating a new client secret for application authentication in Azure AD.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ae12a8e94b9a2412d5f0212702fb9c70fb08ee53%2Fsetup-configuration-in-azure_121cb5f1-e88a-4223-b42d-a4c8333dc37c.png?alt=media)

Copy the **Secret's Value**

![Azure portal client secret management screen showing secret description, expiry date, and copy option.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-3bfeac6592f6a43974cbf9f88e3d1abf6fbc803a%2Fsetup-configuration-in-azure_bbbbcc21-57d0-4f74-a64a-094a79016cfe.png?alt=media)

You now have all the required values to add the Azure Cloud via the Public API once the application setup is complete in Azure Portal.

## Azure RBAC Role Assignment

Go to the subscription detail page. Now we need to make sure we grant access to the roles we need.

Navigate to **Subscriptions**, find the relevant Subscription for your Virtual Machines

Click on **"Access Control (IAM)"**.

![Azure IAM access control panel for managing roles and permissions in a subscription.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b2955c99d638edfc1240484f19e0fd6b4d896a48%2Fsetup-configuration-in-azure_fd91dcbc-023d-4561-a357-f7baf02fb925.png?alt=media)

Go to the Role assignments tab & Click on **"Add"**, then **"Add role assignment"**.

![Azure portal interface for adding role assignments and managing classic administrators.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-eca053ca98613bc874214d294250d7470f8e62fd%2Fsetup-configuration-in-azure_8065aeb7-37b7-46fb-b253-d4a811d5e136.png?alt=media)

In the **"Role"** tab, search and select **"VM Scanner Operator"** & Click **"Next"**.

![Assigning "VM Scanner Operator" role for disk snapshot security analysis in Azure.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ef0aa96fda730d735d3e08b2cc521330582283c1%2Fsetup-configuration-in-azure_891c0d87-d666-4c75-8199-ed8d65d7bbf2.png?alt=media)

Leave the **"Assign access to**" default value.

Click on **"Select Members"**, search for the name of the app registration (e.g. "AikidoSecurity") you created and select it.

Click **"Select"**

Click **"Review + assign"** twice

![Assigning a role to a member in Azure subscription using Access Control (IAM) settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9c873c11e84698003abd7f45eabc3a7b7283b079%2Fsetup-configuration-in-azure_5ca67420-976c-4fc1-b366-bc67a3920b68.png?alt=media)

Repeat the role assignment process for the role **"Disk Snapshot Contributor"**.

The App Registration now has the required roles to scan your virtual machines.
