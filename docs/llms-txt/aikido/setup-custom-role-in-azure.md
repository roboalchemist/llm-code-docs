# Source: https://help.aikido.dev/virtual-machine-scanning/azure/setup-custom-role-in-azure.md

# Setup Custom Role in Azure

This document guides you through creating a new App Registration with client credentials, and a custom RBAC role for Aikido VM scanning.

The credentials will be used by Aikido to make the necessary API requests to scan your Virtual Machines. Access to scan your Virtual Machines will be granted to the App Registration using a custom role.

These permissions are limited to the minimum required for Virtual Machine scanning:

Use the following steps to create

Log into your [**Azure Portal**](https://portal.azure.com/) and navigate to the **Microsoft Entra ID service**.

Click on **Add** and select **App registration**

![Azure Portal: Adding a new app registration under Default Directory Overview.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-53332ba9e377b1992be07aa2b26515a9012923f8%2Fsetup-custom-role-in-azure_ce278464-2951-4d84-877f-6afdae8ed902.png?alt=media)

Give the application a meaningful name, we need this name later.

Leave the **Supported account types** default: **Accounts in this organizational directory only**.

Click on **Register**.

![Registering a new application named "AikidoSecurity" in Microsoft Azure Active Directory.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c57ebacda5c9c707705a273faf0d6cc031e393bc%2Fsetup-custom-role-in-azure_8272b7b3-4bb3-4aec-af7e-437beeaf6095.png?alt=media)

You get redirected to the detail page of the newly created application. Here you can find and copy the **Application (client) ID** and the **Directory (tenant) ID**

![Azure portal displaying AikidoSecurity application overview and client ID information.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5568f22ce6811e7894c5b9d23ee50f41c8f45189%2Fsetup-custom-role-in-azure_f3cb08fa-a0ae-4773-9c9f-6139ef215f3d.png?alt=media)

At the client credentials field, click "Add a certificate or secret"

![Azure portal app registration overview, highlighting "Add a certificate or secret" for client credentials.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cdec5321abc1ef9cce6200cab6701be1b8fdcece%2Fsetup-custom-role-in-azure_5d26a68d-fa9c-4e54-b7ae-90c784fca251.png?alt=media)

Click the "New client secret"-button, give a description for the secret and set the expiration date to 2 years (730 days / 24 months)

![Creating a new client secret for application authentication in Azure Portal.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ae12a8e94b9a2412d5f0212702fb9c70fb08ee53%2Fsetup-custom-role-in-azure_95171d9f-5f07-4498-81dd-3199d5c941ef.png?alt=media)

Copy the **Secret's Value**

![Azure portal showing an active client secret for application authentication with expiration date.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-3bfeac6592f6a43974cbf9f88e3d1abf6fbc803a%2Fsetup-custom-role-in-azure_04e75758-4d58-4f1f-bacd-bac394368b76.png?alt=media)

You now have all the required values to configure VM scanning in Aikido, once the application setup is complete in Azure Portal. Next, we need to make sure we grant the application access for VM scanning.

Navigate to **Subscriptions**, find the relevant Subscription for your Virtual Machines

Click on **"Access Control (IAM)"**.

![Azure IAM portal for managing role assignments, permissions, and access levels on subscriptions.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b2955c99d638edfc1240484f19e0fd6b4d896a48%2Fsetup-custom-role-in-azure_1c719e05-4e24-4386-b2dd-8f82e0bbf7a9.png?alt=media)

Click on the **"Add"** button.

Select **"Add custom role"**

![Azure IAM: Add role assignment, co-administrator, or custom role for subscription access control.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-aeb4986b999c6ce61e50b578d3fe6db986c48602%2Fsetup-custom-role-in-azure_97a45405-cabc-4575-86d3-b35a8b2aac04.png?alt=media)

Go to the **"JSON"** tab and open the editor by clicking on **"Edit"**

![Azure portal interface for creating and downloading a custom role JSON definition.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b42ce582150e0d32a1c902582249dbd0d43bfdd3%2Fsetup-custom-role-in-azure_fa9c2c19-3293-47ef-8456-1812dd0f03a8.png?alt=media)

Copy generated JSON config from the Aikido setup screen, paste it into the editor

Click **"Save"**

![Creating a custom Azure IAM role using JSON permissions template.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-098c1776a2f1e705d99b4983638579eb306256e4%2Fsetup-custom-role-in-azure_bbaca41f-78ff-4e71-80d3-ec6d355db585.png?alt=media)

At the bottom, click **"Review + assign"**, then **"Create"**

![Azure custom role creation: review of permissions and assignable scopes for AikidoVMScanner.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-23a16eb8a6821057f49634dcab226807aac5b99d%2Fsetup-custom-role-in-azure_de6a89f8-a12b-4afd-a892-c92843c530ff.png?alt=media)

Now that the custom role is created, we can assign it to the App Registration we created at the start.

Navigate to **Subscriptions**, find the relevant Subscription for your Virtual Machines

Click on **"Access Control (IAM)"**.

![Azure portal IAM: Manage access roles and permissions for subscription resources.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-b2955c99d638edfc1240484f19e0fd6b4d896a48%2Fsetup-custom-role-in-azure_bcfd2d55-34c9-4434-8f09-502937183174.png?alt=media)

Go to the Role assignments tab & Click on **"Add"**, then **"Add role assignment"**.

![Role assignment menu in Azure portal with options to add or download roles.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-eca053ca98613bc874214d294250d7470f8e62fd%2Fsetup-custom-role-in-azure_4feba3fe-538d-4b7e-b1f7-615bda664244.png?alt=media)

In the **"Role"** tab, search and select the custom role you created (”Aikido VM Scanner”) & Click **"Next"**.

![Assigning the "Aikido VM Scanner" role in Azure for virtual machine access.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7877daccab6719aac65613f877e7813084222060%2Fsetup-custom-role-in-azure_edc34946-a7a6-449d-a0f1-68ec447af894.png?alt=media)

Leave the **"Assign access to"** default value.

Click on **"Select Members"**, search for the name of the app registration (e.g. "AikidoSecurity") you created and select it.

Click **"Select"**

Click **"Review + assign"** twice

![Assigning user, group, or application roles in Azure subscription via role assignment interface.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9c873c11e84698003abd7f45eabc3a7b7283b079%2Fsetup-custom-role-in-azure_4ee31542-c6c9-40da-a557-b264660a458d.png?alt=media)

The App Registration now has the required permissions to scan your Azure Virtual Machines.
