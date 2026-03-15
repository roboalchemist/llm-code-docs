# Source: https://docs.firehydrant.com/docs/okta-for-status-pages.md

# Okta for Status Pages

With FireHydrant's status pages, you can lock them behind your SSO provider so that only employees or other organization members can access them.

> 🚧 Note:
>
> We currently only support OIDC for SSO-authenticated status pages. In addition, this limits access to anyone in your organization who can login via SSO, not only users with FireHydrant licenses.

## 1. Create Status Page

You'll first want to [set up and configure a status page](https://docs.firehydrant.com/docs/status-page-setup-and-configuration). Once you are on the final "Authentication" step, toggle "Authenticate page" and you can start working through these instructions to lock it behind authentication.

<Image border={false} src="https://files.readme.io/d5b19e4ab6a6c054196cc312b559ef93fd93854194f8ca067391e693d39ec3c8-image.png" />

## 2. Create Okta OIDC Application

> Reference documentation here: [https://help.okta.com/en-us/content/topics/apps/apps\_app\_integration\_wizard\_oidc.htm](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_oidc.htm)

1. In Applications, click Create App Integration.  On the popup that follows, choose OIDC - OpenID Connect as the sign in method and Web Application as the Application Type.  Then click next.

   <Image align="center" border={false} src="https://files.readme.io/a5268e54c1ddd6eabbd759fb9e4f8fc93f6cedee87b2de577f3f0601191aa13a-1.png" />
2. On the next screen, under General Settings, click the checkbox to add the Refresh Token grant type.

   <Image align="center" border={false} src="https://files.readme.io/9516678d83b68f5ab48df7bef7627f5ca050581ce814f212d3333440149da9f7-2.png" />
3. In the Sign-in redirect URIs section, add `https://<statuspage hostname>/oauth2/callback` where `<statuspage hostname>` is the DNS name you chose when creating your status page.

   <Image align="center" border={false} src="https://files.readme.io/5a60c8d0e9b40e2ad927a86cf3aa52bac33de2d490061bfded66c8c14e2c193f-3.png" />
4. Remove any URI in the Sign-out redirect URIs section.
5. Your admin can choose to assign all users or only a limited set, based on your business needs.  Once this is complete, click Save.

### 3. Complete Configuration

Once this is complete, you’ll need to gather 3 pieces of information to add authentication to your status page:

1. Issuer URL - This will be your okta domain.  For example: `https://mycompany.okta.com`
2. Client ID - This is in the general tab for the application you just created in the Client Credentials section.
3. Client Secret - This is in the general tab for the application you just created in the Client Secrets section.  It is hidden by default and you can click the Copy To Clipboard or Reveal buttons to get it.

   <Image align="center" border={false} src="https://files.readme.io/1aa46ec9ee998acd2b88e9b5e58ecf670b4ff61045e4e48e4a52ae6706d6c6fe-4.png" />

### 4. Publish and Verify

Once the Status Page is showing as verified on the Status Page overview, publish your new status page! When you attempt to access an SSO-locked status page, you should be redirected to your organization's SSO sign-on page.

<Image border={false} src="https://files.readme.io/cf439db615f179d3c0c428a464423b87d715796f1299bb7f8e9241898acc782f-image.png" />

## Next Steps

* Learn how to [use your FireHydrant status page](https://docs.firehydrant.com/docs/status-page-usage)
* Learn more about [Posting Updates](https://docs.firehydrant.com/docs/posting-updates) during incidents