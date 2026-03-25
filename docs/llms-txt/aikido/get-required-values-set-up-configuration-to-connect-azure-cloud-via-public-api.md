# Source: https://help.aikido.dev/cloud-scanning/connect-your-cloud/azure/get-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api.md

# Get Required Values + Set Up Configuration to Connect Azure Cloud via Public API

Log into your [**Azure Portal**](https://portal.azure.com/) and navigate to the **Microsoft Entra ID service** (Formerly known as Azure Active Directory).

Select **App registration**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-53332ba9e377b1992be07aa2b26515a9012923f8%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_7272798b-6ece-4bc5-9e40-df364a5e7a1f.png?alt=media)

Give the application a meaningful name, we need this name later.

Leave the "Supported account types" default: "Accounts in this organizational directory only".

Click "Register"

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-c57ebacda5c9c707705a273faf0d6cc031e393bc%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_a59aca40-8623-4b87-a76b-06ed42ea2ba4.png?alt=media)

You get redirected to the detail page of the newly created application. Here you can find and copy the **Application (client) ID** and the **Directory (tenant) ID**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-5935a87b181e820397a7e063ae13979b9fb52022%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_f919c8fa-39ae-4cb0-9bec-2d25b03306b4.png?alt=media)

At the client credentials field, click "Add a certificate or secret"

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cdec5321abc1ef9cce6200cab6701be1b8fdcece%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_5d15f5a3-597a-473f-87d0-733e9859afaa.png?alt=media)

Click the "New client secret"-button, give a description for the secret and set the expiration date to 2 years (730 days / 24 months)

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-ae12a8e94b9a2412d5f0212702fb9c70fb08ee53%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_d12ff208-e713-46a2-a2a0-c637ff7c9f21.png?alt=media)

Copy the **Secret's Value**

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-3bfeac6592f6a43974cbf9f88e3d1abf6fbc803a%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_4859aaf5-4ea3-4395-afb6-fda023ffdae2.png?alt=media)

Navigate to Subscriptions, Copy the **Subscription ID** of the relevant subscription.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-fa792d5d0c8393c7975be56decc04d127ca41872%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_ba21e769-470f-45ac-8943-e91e79e38637.png?alt=media)

You now have all the required values to add the Azure Cloud via the Public API once the application setup is complete in Azure Portal.

Go to the subscription detail page. Now we need to make sure we grant access to the roles we need.

Click on **"Access Control (IAM)"**.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7791acf5967a0a5744954244877bb936001e7515%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_4b484f3d-1809-4a49-aab8-73b3c23cdcbd.png?alt=media)

Go to the Role assignments tab & Click on **"Add"**, then **"Add role assignment"**.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-916872519ec5da13f9086b2bf83f8dfaf5f00e42%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_0d132105-5281-4e43-a5df-068e79afe0d1.png?alt=media)

In the **"Role"**-list, search and select **"Security Reader"** & Click **"Next"**.

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-82a3673a40308c6313f9983b0895e950176f45d9%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_2db28119-d664-4080-9e28-5871d87b0111.png?alt=media)

Leave the **"Assign access to**"default value.

Click on **"Select Members"**, search for the name of the app registration (e.g. "AikidoSecurity") you created and select it.

Click **"Select"**

Click **"Review + assign"** twice

![](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a51477a198d8514a875bf40686cc16ff0446b8ff%2Fget-required-values-set-up-configuration-to-connect-azure-cloud-via-public-api_c423fb1d-21e0-43ed-b243-f26cf556418a.png?alt=media)

Repeat the role assignment process for the role **"Log Analytics Reader"**.

Now the application has the required roles to do the security scanning. You can now add this cloud using the public API.
