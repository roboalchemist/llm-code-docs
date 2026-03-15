# Source: https://docs.firehydrant.com/docs/google-auth-for-status-pages.md

# Google Auth for Status Pages

With FireHydrant's status pages, you can lock them behind your SSO provider so that only employees or other organization members can access them.

> 🚧 Note:
>
> We currently only support OIDC for SSO-authenticated status pages. In addition, this limits access to anyone in your organization who can login via SSO, not only users with FireHydrant licenses.

## 1. Create Status Page

You'll first want to [set up and configure a status page](https://docs.firehydrant.com/docs/status-page-setup-and-configuration). Once you are on the final "Authentication" step, toggle "Authenticate page" and you can start working through these instructions to lock it behind authentication.

<Image border={false} src="https://files.readme.io/d5b19e4ab6a6c054196cc312b559ef93fd93854194f8ca067391e693d39ec3c8-image.png" />

<br />

## 2. Create Google OIDC Application

> Reference documentation here: [https://developers.google.com/identity/openid-connect/openid-connect](https://developers.google.com/identity/openid-connect/openid-connect)

To create an OIDC application in Google Cloud, please have your admin follow these steps:

1. In a Google Cloud project that your users have access to, go to API and Services > Credentials and click Create credentials.  In the dropdown, choose OAuth Client ID.

   <Image align="center" border={false} src="https://files.readme.io/1ac6e09bb6630d4230e0b3f2026dceb53eb9673c11db1682a46059207241cee0-1.png" />
2. If you have not already done so, the next screen will prompt you to configure the consent screen.  If you’ve done this already, you can skip to step 3.  Otherwise, you can fill in app information, choose your audience (internal), and contact information that will appear on your consent screen.
3. After you set up the consent screen, click on Create OAuth Client.

   <Image align="center" border={false} src="https://files.readme.io/e0ed688b96773c967c3984f7985ec69593129891964f17fe3aef2c054d7fa340-7.png" />
4. In the Application type dropdown, choose Web Application.

   <Image align="center" border={false} src="https://files.readme.io/307f915a6646e80d3b179953291aaee66b98b29907f990685bff5997d88d2f1e-8.png" />
5. In Authorized redirect URIs, add `https://<statuspage hostname>/oauth2/callback` where `<statuspage hostname>` is the DNS name you chose when creating your status page.  Then click Create.

   <Image align="center" border={false} src="https://files.readme.io/16ca284fc97231f9573ffcd67cfe6f491fe993533e68cab8954117c3597add40-9.png" />
6. The following page will be your only chance to get the client secret, so be sure to copy this information before dismissing it!

### 3. Finish Configuration

Once this is complete, you’ll need to gather 3 pieces of information to add authentication to your status page:

1. Issuer URL - For google cloud auth, this will be [https://accounts.google.com/o/oauth2/auth](https://accounts.google.com/o/oauth2/auth)
2. Client ID - This is in the Client ID section shown below.
3. Client Secret - This is in the Client Secret section shown below.

   <Image align="center" border={false} src="https://files.readme.io/57b1eaab14664db48fe963e972068f009cec081e08dfa4a577379fac9ceafd2c-10.png" />

### 4. Publish and Verify

Once the Status Page is showing as verified on the Status Page overview, publish your new status page! When you attempt to access an SSO-locked status page, you should be redirected to your organization's SSO sign-on page.

<Image border={false} src="https://files.readme.io/cf439db615f179d3c0c428a464423b87d715796f1299bb7f8e9241898acc782f-image.png" />

## Next Steps

* Learn how to [use your FireHydrant status page](https://docs.firehydrant.com/docs/status-page-usage)
* Learn more about [Posting Updates](https://docs.firehydrant.com/docs/posting-updates) during incidents