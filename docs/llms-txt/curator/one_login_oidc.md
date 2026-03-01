# Source: https://docs.curator.interworks.com/setup/authentication/one_login_oidc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OneLogin (OIDC)

> A guide to setting up OneLogin as an OpenID Connect (OIDC) provider for Curator.

## OneLogin Setup

1. Go to the Applications page in the Administration area of OneLogin and click "Add App."
2. Enter "oidc" in the search bar and select "OpenId Connect (OIDC)." The vendor should be "OneLogin, Inc."
3. Give the Application a display name like "InterWorks Curator," upload icons if you'd like, and click "Save."
4. In the Application's settings page, navigate to "Configuration" and enter the following for the URL and URI's:
   * **Login URL**: Base Curator URL (i.e. `https://www.curatorexample.com`).
   * **Redirect URI's**: Base Curator URL with `/user/oauth` appended (i.e.
     `https://www.curatorexample.com/user/oauth`). No other URI's should be entered.
   * **Post Logout Redirect URI's**: Base Curator URL (i.e. `https://www.curatorexample.com`). No other URI's should be entered.
5. In the Application's settings page, navigate to "SSO" and set the following:
   * **Application Type**: Set this to "Web."
   * **Token Endpoint - Authentication Method**: Set this to "POST."
6. Save the settings and stay on the "SSO" page. We'll need this info for the Curator-side of the setup.

## Curator Setup

1. Go to the Authentication Settings under Settings > Security in the Curator backend.
2. Choose "OAuth / OpenID Connect" for the Authentication Type.
3. Expand the "Customization" section and enter the following:
   * **OAuth Domain**: Enter the "Issuer URL" from the "SSO" area of the Application's settings in OneLogin. This
     usually ends in `/oidc/2`.
   * **OAuth Client ID**: Enter the "Client ID" from OneLogin.
   * **OAuth Client Secret** Enter the "Client Secret" from OneLogin. You may have to click "Show client secret" in
     OneLogin to see it.
4. Save the settings.

## Users

As users log in via OAuth, user records will automatically be provisioned in Curator. If Curator is connected to an
analytic platform it will sync over details like display name or email at the same time during login. No SCIM necessary!
