# Source: https://docs.firehydrant.com/docs/microsoft-entra-for-status-pages.md

# Microsoft Entra for Status Pages

With FireHydrant's status pages, you can lock them behind your SSO provider so that only employees or other organization members can access them.

> 🚧 Note:
>
> We currently only support OIDC for SSO-authenticated status pages. In addition, this limits access to anyone in your organization who can login via SSO, not only users with FireHydrant licenses.

<br />

## 1. Create Status Page

You'll first want to [set up and configure a status page](https://docs.firehydrant.com/docs/status-page-setup-and-configuration). Once you are on the final "Authentication" step, toggle "Authenticate page" and you can start working through these instructions to lock it behind authentication.

<Image border={false} src="https://files.readme.io/d5b19e4ab6a6c054196cc312b559ef93fd93854194f8ca067391e693d39ec3c8-image.png" />

## 2. CreateAzure Active Directory OIDC Application

> Reference documentation here: [https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#register-an-application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#register-an-application)

1. To create an OIDC application in Microsoft Entra, please have your admin follow these steps:
   From the Entra ID > App Registrations page, click New Registration.

   <Image align="center" border={false} src="https://files.readme.io/cf2a7d248e818d8f825c31528333cac0ed40b1a30d85bbbb1bac8f62e8eec16e-1.png" />
2. Add a name for the application, then enter the Redirect URI.  The redirect URI is  `https://<statuspage hostname>/oauth2/callback` where `<statuspage hostname>` is the DNS name you chose when creating your status page.  When you are finished, click Register to create the app.

   <Image align="center" border={false} src="https://files.readme.io/c6911749cbd0ee5187ebfc8990a80c5fc7b7e4c87dd3032e7460d5dc4fdf5583-2.png" />
3. Once the app is registered, you will need to add a secret.  In the Certificates and secrets section, click New Client Secret to add a new secret.  Note that you will only be shown the secret once, so be sure to copy it somewhere immediately so you can enter it in the Firehydrant UI later.

   <Image align="center" border={false} src="https://files.readme.io/d48e84116850bbff86b26b1a0eaac9a73bf9efa232d3ea484d1f57ce2a4dd20e-3.png" />
4. You will also need to add an optional claim.  In the token configuration section, click the Add Optional Claim button.  The token type is ID and the claim is email, as shown below.

   <Image align="center" border={false} src="https://files.readme.io/2e38f3e0c7afa1eb63d6ec76a6f6a28a1d35881fec17888bbdbff8132c570703-4.png" />

### 3. Finish Configuration

Once this is complete, you’ll need to gather 3 pieces of information to add authentication to your status page:

1. Issuer URL - For Microsoft Entra, this is available by clicking on the Endpoints button.  Use the first endpoint, labeled Authority URL (Accounts in this organizational directory only)
2. Client ID - This is labeled as Application (client) ID on the overview page.
3. Client Secret - This was copied from step 3 above when the secret was created.

### 4. Publish and Verify

Once the Status Page is showing as verified on the Status Page overview, publish your new status page! When you attempt to access an SSO-locked status page, you should be redirected to your organization's SSO sign-on page.

<Image border={false} src="https://files.readme.io/cf439db615f179d3c0c428a464423b87d715796f1299bb7f8e9241898acc782f-image.png" />

## Next Steps

* Learn how to [use your FireHydrant status page](https://docs.firehydrant.com/docs/status-page-usage)
* Learn more about [Posting Updates](https://docs.firehydrant.com/docs/posting-updates) during incidents