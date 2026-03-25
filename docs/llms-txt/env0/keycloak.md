# Source: https://docs.envzero.com/guides/sso-integrations/keycloak.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Keycloak Integration

> Configure Keycloak as a SAML identity provider for env zero organization authentication

## Introduction

This guide will detail the various steps required to integrate Keycloak as a SAML provider for your env zero organization. The current implementation is used for authentication only, where you define your users in your Keycloak to enable them access to your env zero organization.

<Note>
  **Self-Service Configuration Available**: You can configure SAML SSO directly from your organization settings. See [Self-Service SSO Integration](/guides/sso-integrations/self-service-sso) for an overview, or [Self-Service SAML Setup](/guides/sso-integrations/self-service-saml) for step-by-step instructions.
</Note>

## Steps

1. Login to your Keycloak account as an Administrator
2. In the left-side menu click on the `Clients` tab
3. Click on the `Create` button
4. In the Client ID enter `urn:auth0:env0:YOUR_ENV0_ORG_ID`\
   e.g. `urn:auth0:env0:aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`
5. In the Client Protocol dropdown Select `saml`
6. Click on the `Save` button
7. Under the `Settings` tab, in the `Name` enter `env zero`
8. In the `Name ID Format` dropdown select `email`
9. in the `IDP Initiated SSO URL Name` enter `env zero`
10. Open the `Fine Grain SAML Endpoint Configuration` dropdown
11. In the `Assertion Consumer Service POST Binding URL` and in the `Assertion Consumer Service Redirect Binding URL` enter `https://login.app.env0.com/login/callback?connection=YOUR_ENV0_ORG_ID` - e.g. `https://login.app.env0.com/login/callback?connection=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee`
12. Click on the `Save` button at the bottom

<Frame caption="Client Configuration">
  <img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/client_configuration.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=a98d332b5dfefabad725c6d0aa35a040" alt="Keycloak client configuration interface showing SAML settings and authentication options" width="1113" height="891" data-path="images/guides/sso-integrations/client_configuration.png" />
</Frame>

<Frame caption="Client Configuration - Fine Grain SAML Endpoint">
  <img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/client_configuration_-_fine_grain_saml_endpoint.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=c3a21fc042876537e1a2e79bb8e4d25c" alt="Keycloak fine grain SAML endpoint configuration showing advanced SAML settings" width="1097" height="960" data-path="images/guides/sso-integrations/client_configuration_-_fine_grain_saml_endpoint.png" />
</Frame>

## Mappers

1. Click on the `Mappers` tab
2. Click on the `Add Builtin` button
3. Check the `X500 email`, `X500 givenName` and `X500 surname`and click on the `Add selected` button
4. Click on the `Edit` button in the `X500 givenName` and change the `SAML Attribute Name` to be `firstName` and click on the `Save` button
5. Click on the `Edit` button in the `X500 email` and change the `SAML Attribute Name` to be `email`and click on the `Save` button
6. Click on the `Edit` button in the `X500 surname` and change the `SAML Attribute Name` to be `lastName`and click on the `Save` button
7. If you like to also sync your Keycloak groups with env zero you need to click on the `Create` button in the `Mappers` tab
8. Under `Name` enter `groups`
9. In the `Mapper Type` dropdown select `Group list`
10. In the `Group attribute name` enter `groups`
11. In the `Friendly Name` enter `groups`
12. Leave the `SAML Attribute NameFormat` unselected and Make sure the `Single Group Attribute` is switched on
13. You can choose whether to send the full group path.  If you like to get the full group path, switch it on, and the teams in env zero will include the full path of the group, e.g. if you have an `Front end` group inside a `RnD` group the name of the team in env zero will be `/Rnd/Front End`
14. Read more about [Teams syncing with env zero here](/guides/sso-integrations/importing-roles-or-groups-from-your-identity-provider)
15. Click on the `Save` button

<img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/f289642-screenshot_2023-04-13_at_16.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=56039d6698412da10a1cce43c6c6a644" alt="" width="1573" height="225" data-path="images/guides/sso-integrations/f289642-screenshot_2023-04-13_at_16.png" />

## Installation

1. In order to set your SAML inside env zero, navigate to your organization settings and go to the **SSO** tab
2. Click on **SAML** to configure your connection
3. In Keycloak, go to the `Installation` tab
4. In the `Format Option` dropdown select `Mod Auth Mellon Files` and click on the `Download` button
5. Extract the downloaded `keycloak-mod-auth-mellon-sp-config.zip` file
6. Complete the self-service form in env zero with the information from the `idp-metadata.xml` file from the extracted folder

<Frame caption="Download XML file">
  <img src="https://mintcdn.com/envzero-b61043c8/cHWoWZ1iOlL9-IH4/images/guides/sso-integrations/download_xml_file.png?fit=max&auto=format&n=cHWoWZ1iOlL9-IH4&q=85&s=28e4695ddb43c906c47b4172dc73bedf" alt="Keycloak interface showing download XML file option for SAML metadata" width="1054" height="158" data-path="images/guides/sso-integrations/download_xml_file.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
