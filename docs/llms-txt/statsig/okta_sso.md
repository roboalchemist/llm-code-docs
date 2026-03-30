# Source: https://docs.statsig.com/access-management/sso/okta_sso.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Single Sign-On With Okta

## Requirements

* You will need to be the `Admin` of the Statsig Organization you intend to add SSO with Okta to.
* You will need to be the Administrator of the Okta account you want to link.

## Supported Features

Statsig supports the OIDC protocol for SSO with the following flows:

* Service Provider(SP)-Initiated Authentication for Single Sign-On (SSO). This flow is initialized when logging in on the Statsig website.
* Identity Provider(IDP)-Initiated Authentication for SSO. This flow is initialized when launching the Statsig App from Okta.
* Just-In-Time (JIT) provisioning for SSO. Upon successful login for the first time, Statsig automatically provisions an account for the user.

## Configuration

### Adding the Statsig OIDC Application in Okta

1. Navigate to your Okta portal.
2. On your Okta portal, click on `Applications` on the left-hand-column, and click into `Applications` in the dropdown.
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/sso/okta_sso/129780676-c04bd2fb-83ed-4d17-9ae2-4e286f2b3b52.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=ee01b03e1901cdea3afab1f04df4435a" alt="Okta portal navigation highlighting Applications menu" width="286" height="526" data-path="images/access-management/sso/okta_sso/129780676-c04bd2fb-83ed-4d17-9ae2-4e286f2b3b52.png" />
   </Frame>
3. On the Applications page, click on the `Browse App Catalog` button.
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/sso/okta_sso/129780681-c48a6012-a882-475a-bbc9-924ec1391126.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=72a1f00bd73e6158fb7bf42c6e94eaa5" alt="Okta Applications page with Browse App Catalog button" width="685" height="135" data-path="images/access-management/sso/okta_sso/129780681-c48a6012-a882-475a-bbc9-924ec1391126.png" />
   </Frame>
4. On the App Catalog page, use the searchbox to search for Statsig and click on the Statsig OIDC Application.
5. In the Statsig Application, click on the `Add` button.
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/sso/okta_sso/129780685-e6e141c6-8fdf-42f0-8ed6-edc734f4c2a7.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=3d2910c8cf84ef49ed68e34c97a45488" alt="Statsig app listing within Okta catalog showing Add button" width="1047" height="338" data-path="images/access-management/sso/okta_sso/129780685-e6e141c6-8fdf-42f0-8ed6-edc734f4c2a7.png" />
   </Frame>
6. After creating the Statsig OIDC Application in Okta, navigate to the `Sign On` tab in the Application, note the `Client ID` and `Client Secret` fields that will be needed to enable Single Sign-On with OIDC on the Statsig Project. Also note that when adding the Statsig OIDC Application in Okta, the sign-in and sign-out redirect URIs are automatically configured.
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/sso/okta_sso/129780687-bacc68c7-4fb1-4740-bb3e-a7c6b27d006e.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=3cb1d4aa5d7292a35deabca556b607ec" alt="Okta Sign On tab showing Client ID and Client Secret values" width="750" height="983" data-path="images/access-management/sso/okta_sso/129780687-bacc68c7-4fb1-4740-bb3e-a7c6b27d006e.png" />
   </Frame>

Once these steps have been completed, the Statsig OIDC Application in Okta has been successfully configured. Next, you will need to follow the steps [here to enable configuration of SSO on your Statsig Organization](/access-management/sso/overview#in-statsig-console).

## SP-Initiated SSO

1. Navigate to [https://console.statsig.com/sso](https://console.statsig.com/sso)
2. Enter your email address and click on "Authenticate"
3. You will be redirected to authenticate with Okta. If prompted, enter your Okta credentials.
4. Upon successful authentication, you will be redirected and logged in to Statsig.

### Proof Key for Code Exchange (PKCE)

Statsig does not currently support the PKCE Flow, so you will need to turn off the feature in Okta when you enable SSO with Statsig.


Built with [Mintlify](https://mintlify.com).