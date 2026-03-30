# Source: https://tyk.io/docs/tyk-stack/tyk-developer-portal/enterprise-developer-portal/api-access/dynamic-client-registration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic Client Registration

> How to configure Dynamic Client Registration in Tyk developer portal

## Introduction

**Why OAuth2.0 is important**

OAuth 2.0 is a crucial security mechanism for both public and internal APIs, as it provides a secure and standardized way to authenticate and authorize access to protected resources. It enables granular access control and revocation of access when necessary without exposing sensitive login credentials. In short, OAuth 2.0 offers a secure and flexible approach to managing access to APIs.

Implementing an OAuth2.0 provider can be a complex process that involves several technical and security considerations. As such, many API providers choose to use specialized identity providers instead of implementing OAuth2.0 provider themselves.

By using specialized identity providers, API providers can leverage the provider's expertise and infrastructure to manage access to APIs and ensure the security of the authentication process. This also allows API providers to focus on their core business logic and reduce the burden of managing user identities themselves.

**How does Tyk help**

Tyk offers a standard and reliable way to work with identity providers through the Dynamic Client Registration protocol (DCR), which is an [Internet Engineering Task Force](https://www.ietf.org/) protocol that establishes standards for dynamically registering clients with authorization servers.

Tyk Enterprise Developer portal allows API providers to set up a connection with identity providers that support DCR so that API Consumers can use the OAuth2.0 credentials issued by the identity provider to access APIs exposed on the portal.

<br />

## Prerequisites

Before getting starting with configuring the portal, it's required to configure your Identity provider and the Dashboard beforehand.

### Create an initial access token

Before setting up Tyk Enterprise Developer Portal to work with DCR, you need to configure the identity provider. Please refer to the guides for popular providers to create the initial access token for DCR:

* [Gluu](https://gluu.org/docs/gluu-server/4.0/admin-guide/openid-connect#dynamic-client-registration)
* [Curity](https://curity.io/docs/idsvr/latest/token-service-admin-guide/dcr.html)
* [Keycloak](https://github.com/keycloak/keycloak/blob/25.0.6/docs/documentation/securing_apps/topics/client-registration.adoc)
* [Okta](https://developer.okta.com/docs/reference/api/oauth-clients/)

  <Note>
    Whilst many providers require initial access tokens, they are optional. Please refer to your provider documentation to confirm if required.
  </Note>

### Create OAuth2.0 scopes to enforce access control and rate limit

Tyk uses OAuth2.0 scope to enforce access control and rate limit for API Products. Therefore, creating at least two scopes for an API Product and plan is required.

The below example demonstrates how to achieve that with Curity, Keycloak and Okta in the tabs below.

<Tabs>
  <Tab title="Curity">
    1. **Navigate to Profiles → Token Service → Scopes**

       Click `+ New` to create a new scope.

       <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/curity-add-scope.jpg?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=1ca99c6d9b73f56ec83a808d9d58e8e5" alt="Navigate to the Scopes menu" width="3444" height="1606" data-path="img/dashboard/portal-management/enterprise-portal/curity-add-scope.jpg" />

    2. **Give the new scope a name**

       Name the scope **product\_payments** and click `Create`. Repeat to create another scope and give it the name **free\_plan**.

       <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/curity-name-scope-product.jpg?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=a3a4ee5afd435dd1cee981a0530e1f58" alt="Name the scope product_payments" width="1746" height="400" data-path="img/dashboard/portal-management/enterprise-portal/curity-name-scope-product.jpg" />

       <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/curity-name-scope-plan.jpg?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=256598b7b63ed0131c37f88122a1fee4" alt="Name the scope free_plan" width="1744" height="398" data-path="img/dashboard/portal-management/enterprise-portal/curity-name-scope-plan.jpg" />

       The created scopes can now be assigned to OAuth Clients configured, including DCR clients when they are registered.

    **Unauthenticated DCR**

    The Curity Identity Server by default requires a <Tooltip tip="A token that can only be used once">nonce token</Tooltip> with a `dcr` scope to authenticate the DCR endpoint. It obtains this via normal OAuth flows. It is, however, not possible to define an OAuth client\_id and secret in Tyk to obtain such a token. A workaround is to disable authentication of the DCR endpoint in the Curity Identity Server by setting it to use no-authentication.

    <br />

    <Warning>
      **Use in secure environments only**

      When configuring the DCR endpoint in the Curity Identity Server to use `no-authentication`, ensure that the communication between Tyk and the Curity Identity Server is secured so that it is only accessible to Tyk.

      To configure this in the AdminUI of the Curity Identity Server, go to Profiles → Token Service → Dynamic Registration → scroll to the Non-templatized section and set Authentication Method to `no-authentication`.
    </Warning>
  </Tab>

  <Tab title="Keycloak">
    1. **Navigate to the Client scopes menu item**

       <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/step-1-navigate-to-the-client-scopes-menu.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=9667c5d210c1f630a1a6ad082961be9e" alt="Navigate to the Client scopes menu item" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/step-1-navigate-to-the-client-scopes-menu.png" />

    2. **Create a scope for an API Product**

       <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/step-2-create-a-scope-for-an-api-product.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=84ecca70913ed261311550c9819a1895" alt="Create a scope for an API Product" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/step-2-create-a-scope-for-an-api-product.png" />

    3. **Create a scope for a plan**

       <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/step-3-create-a-scope-for-a-plan.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=7fbf9d169829b3453e6d3cb151cf36e8" alt="Create a scope for a plan" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/step-3-create-a-scope-for-a-plan.png" />

       <Note>
         When using Keycloak, ensure that you set the type of the scope to be `Optional`. Default scopes are applied automatically, while optional scopes can be requested by clients on a case-by-case basis to extend the permissions granted by the user. In recent versions of Keycloak this should appear as a dropdown menu option, as shown in the images above. In older releases of Keycloak this may need to be set explicitly in a separate tab, as show on the image below.
       </Note>

    <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/old-keycloak-version-client-scope.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=424b7ca784d7f28a780e3875f50db0a6" alt="Client Scope Assigned Type" width="715" height="245" data-path="img/dashboard/portal-management/enterprise-portal/old-keycloak-version-client-scope.png" />
  </Tab>

  <Tab title="Okta">
    1. **Create an auth server or use the `Default` authorization server**

       Go to Security → API, Edit one of the auth servers and navigate to `Scopes`

       <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/okta-api-page.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=ec0da426ed4fe8ca0396bc045e7fce10" alt="Add or Edit oauth servers in okta" width="1600" height="555" data-path="img/dashboard/portal-management/enterprise-portal/okta-api-page.png" />

    2. **Create a scope for an API Product**

       <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/okta-product-payment.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=ade40380b25d1de2e5cc4f5fa721d74d" alt="Create a scope for an API Product" width="1365" height="1600" data-path="img/dashboard/portal-management/enterprise-portal/okta-product-payment.png" />

    3. **Create a scope for a plan**

       <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/okta-free-plan-scope.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=bed0e97b195f32e844b42d3fb7fa6898" alt="Create a scope for a plan" width="1368" height="1600" data-path="img/dashboard/portal-management/enterprise-portal/okta-free-plan-scope.png" />
  </Tab>
</Tabs>

## Create Tyk policies for an API Product and plan

<Note>
  You can skip this step if you are using Tyk Developer Portal version 1.13.0 or later.
  Go directly to [Configure Tyk Enterprise Developer Portal to work with an identity provider](#configure-tyk-enterprise-developer-portal-to-work-with-an-identity-provider).
</Note>

Navigate to the Tyk Dashboard and create two policies: one for a plan and one for an API Product. Both policies should include only the APIs with JWT authentication that you want to bundle as an API Product.

1. **Create a policy for an API product.**

   <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/create-jwt-policy-for-product.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=697f36fec4141f5539db0c1e31188db2" alt="Create a policy for a product" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/create-jwt-policy-for-product.png" />

2. **Create a policy for a plan.**

   <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/create-jwt-policy-for-plan.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=25b9065c2b0191503e306f4fe8340aa1" alt="Create a policy for a plan" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/create-jwt-policy-for-plan.png" />

### Create the No Operation policy and API

<Note>
  You can skip this step if you are using Tyk Developer Portal version 1.13.0 or later.
  Go directly to [Configure Tyk Enterprise Developer Portal to work with an identity provider](#configure-tyk-enterprise-developer-portal-to-work-with-an-identity-provider).
</Note>

Tyk requires any API that uses the scope to policy mapping to have [a default policy](/basic-config-and-security/security/authentication-authorization/json-web-tokens). Access rights and rate limits defined in the default policy take priority over other policies, including policies for the API Product and plan.

To avoid that, you need to create the No Operation API and policy that won't grant access to the APIs included in the API Product but will satisfy the requirement for a default policy.

1. **Create the No Operation API.**

   Navigate to the `APIs` menu in the Tyk Dashboard:

   <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/navigate-to-the-api-menu-in-the-tyk-dashboard.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=e0ba27efa102cebaea24c9a19f5bda59" alt="Navigate to the API menu in the Tyk Dashboard" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/navigate-to-the-api-menu-in-the-tyk-dashboard.png" />

   Create a new HTTP API:

   <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/create-noop-api.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=97eaacd59b95614bb3f1c3e7344c6542" alt="Create the No Operation API" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/create-noop-api.png" />

   Save it:

   <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/save-the-noop-api.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=ff2b98aa2c3294d5cd66c1989d8427f5" alt="Save the No Operation API" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/save-the-noop-api.png" />

<br />

2. **Create the No Operation policy.**

   Navigate to the `Policies` menu in the Tyk Dashboard:

   <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/navigate-to-the-policies-menu.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=1d885b4ff8bc2bb40fa2f793c5259c4c" alt="Navigate to the policies menu" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/navigate-to-the-policies-menu.png" />

   Create a new policy and select the No Operation API in the `Add API Access Rights` section:

   <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/create-noop-policy.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=3c54211d62cada1bbc1fe23f7c1d31e2" alt="Create the No Operation policy" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/create-noop-policy.png" />

   Configure the No Operation policy and save it:

   <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/save-the-noop-policy.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=e56283840401b44078ee88934a437b7b" alt="Save the No Operation policy" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/save-the-noop-policy.png" />

### Configure scope to policy mapping

<Note>
  You can skip this step if you are using Tyk Developer Portal version 1.13.0 or later.
  Go directly to [Configure Tyk Enterprise Developer Portal to work with an identity provider](#configure-tyk-enterprise-developer-portal-to-work-with-an-identity-provider).
</Note>

To enforce policies for the API Product and plan, you need to configure the scope to policy mapping for each API included in the API Product.
To achieve that, perform the following steps for each API included in the API Product.

1. Navigate to the API.

   <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/navigate-to-the-api.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=611246e0ead404c3cee9a563ab650c6a" alt="Navigate to the API" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/navigate-to-the-api.png" />

2. Select the required JWT signing method. In this example, we use RSA. Leave the `Public key` and `pol` fields blank, they will be filled automatically by the Enterprise portal.

   <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/select-signing-method.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=594b41a6f568e95dafaeec3688ee8645" alt="Select signing method for the API" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/select-signing-method.png" />

3. Select the No Operation policy as the default policy for this API.

   <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/select-the-default-policy.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=c7b82dcba6a239a0f322cbedee84a5f0" alt="Select the default policy for the API" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/select-the-default-policy.png" />

4. Enable scope to policy mapping and specify the value of the JWT claim used to extract scopes in the `Scope name` field (the default value is "scope").

   <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/enable-scope-to-policy-mapping.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=1d7711505227e5e155097c91cc2f2846" alt="Enable scope to policy mapping" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/enable-scope-to-policy-mapping.png" />

5. Add a scope to policy mapping for the product scope. Type the product scope in the `Claim field` and select the product policy.

   <img src="https://mintcdn.com/tyk/wHLHFqRiMZq91WJo/img/dashboard/portal-management/enterprise-portal/add-a-scope-to-policy-mapping-for-the-product-scope.png?fit=max&auto=format&n=wHLHFqRiMZq91WJo&q=85&s=8f2d914d93de4406c890f57829774e14" alt="Add scope to policy mapping for the product scope" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/add-a-scope-to-policy-mapping-for-the-product-scope.png" />

6. Add a scope to policy mapping for the plan scope. Type the plan scope in the `Claim field` and select the plan policy, then save the API.

   <img src="https://mintcdn.com/tyk/wHLHFqRiMZq91WJo/img/dashboard/portal-management/enterprise-portal/add-a-scope-to-policy-mapping-for-the-plan-scope.png?fit=max&auto=format&n=wHLHFqRiMZq91WJo&q=85&s=e6ab034b9d827b9ea0b9401f607a2ec5" alt="Add scope to policy mapping for the plan scope" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/add-a-scope-to-policy-mapping-for-the-plan-scope.png" />

## Configure Tyk Enterprise Developer Portal to work with an identity provider

Set up the portal to work with your IdP.

### Configure the App registration settings

In the portal, navigate to the `OAuth2.0 Providers` menu section. In that section, you need to configure the connection settings to the IdP and define one or more types (configurations) of OAuth 2.0 clients. For instance, you can define two types of OAuth 2.0 clients:

* A confidential client that supports the Client credential grant type for backend integrations;
* A web client that supports the Authorization code grant type for integration with web applications that can't keep the client secret confidential.

Each configuration of OAuth 2.0 client could be associated with one or multiple API Products so that when an API Consumer requests access to an API Product, they can select a client type that is more suitable for their use case.

#### Specify connection setting to your IdP

To connect the portal to the IdP, you need to specify the following settings:

* OIDC well-known configuration URL.
* Initial access token.

First of all, select your IdP from the `Identity provider` dropdown list. Different IdPs have slightly different approaches to DCR implementation, so the portal will use a driver that is specific to your IdP. If your IdP is not present in the dropdown list, select the `Other` option. In that case, the portal will use the most standard implementation of the DCR driver, which implements the DCR flow as defined in the RFC.

Then you need to specify the connection settings: [the initial access token and the well-known endpoint](#create-an-initial-access-token). If your Identity Provider uses certificates that are not trusted, the portal will not work with it by default. To bypass certificate verification, you can select the `SSL secure skip verify` checkbox.

The below example demonstrates how to achieve that with Curity, Keycloak and Okta in the tabs below.

<Tabs>
  <Tab title="Curity">
    <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/curity-oauth-provider.jpg?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=f020c33d683b1e3047e003950761899c" alt="Specify connection setting" width="3448" height="1410" data-path="img/dashboard/portal-management/enterprise-portal/curity-oauth-provider.jpg" />

    Set a **Name**, set the **Identity Provider Type** to `Other`, and the **OIDC well-known configuration URL** aproppriately.
  </Tab>

  <Tab title="Keycloak">
    <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/specify-connection-setting-to-your-idp.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=90caf02d9c6c2174fd2a2e264f7fa19b" alt="Specify connection setting to the IdP" width="1715" height="1170" data-path="img/dashboard/portal-management/enterprise-portal/specify-connection-setting-to-your-idp.png" />
  </Tab>

  <Tab title="Okta">
    <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/specify-connection-setting-to-your-idp-okta.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=396b28a46d405f10c7e39fa703c6e866" alt="Specify connection setting to the IdP" width="1502" height="1272" data-path="img/dashboard/portal-management/enterprise-portal/specify-connection-setting-to-your-idp-okta.png" />

    **OIDC URL**: `{your-domain.com}/oauth2/default/.well-known/openid-configuration`

    **Registration Access Token**: To obtain token, Go to Okta Admin Console → Security → API → Tokens → Create New Token
  </Tab>
</Tabs>

#### Create client configurations

Once the connection settings are specified, you need to create one or multiple types of clients. You might have multiple types of clients that are suitable for different use cases, such as backend integration or web applications.

You need at least one type of client for the DCR flow to work. To add the first client type, scroll down to the `Client Types` section and click on the `Add client type` button.

To configure a client type, you need to specify the following settings:

* **Client type display name.** This name will be displayed to API consumers when they check out API products. Try to make it descriptive and short, so it's easier for API consumers to understand.
* **Description.** A more verbose description of a client type can be provided in this field. By default, we do not display this on the checkout page, but you can customize the respective template and make the description visible to API consumers. Please refer to [the customization section](/portal/customization#) for guidance.
* **Allowed response\_types.** Response types associated with this type of client as per [the OIDC spec](https://openid.net/specs/openid-connect-core-1_0-17.html).
* **Allowed grant\_types.** Grant types that this type of client will support as per [the OIDC spec](https://openid.net/specs/openid-connect-core-1_0-17.html).
* **Token endpoint auth methods.** The token endpoint that will be used by this type of client as per [the OIDC spec](https://openid.net/specs/openid-connect-core-1_0-17.html).
* Additionally, there’s an additional field for Okta: **Okta application type** which defines which type of Okta client should be created. Ignored for all other IdPs.

Please note that your IdP might override some of these settings based on its configuration.

The below example demonstrates how to achieve that with Curity, Keycloak and Okta in the tabs below. After configuring a client type, scroll to the top of the page to save it by clicking on the `SAVE CHANGES` button.

<Tabs>
  <Tab title="Curity">
    <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/curity-client-type.jpg?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=71ba4f1daaad6ab8cfe9b6d5fcc70698" alt="Configure a client type" width="1726" height="1434" data-path="img/dashboard/portal-management/enterprise-portal/curity-client-type.jpg" />
  </Tab>

  <Tab title="Keycloak">
    <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/configure-type-of-client.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=089a770556718839dc51018ca2fe1fad" alt="Configure a client type" width="1715" height="1259" data-path="img/dashboard/portal-management/enterprise-portal/configure-type-of-client.png" />
  </Tab>

  <Tab title="Okta">
    <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/configure-type-of-client-okta.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=b07f4e98cab9d46b8c1d5adbff80d81f" alt="Configure a client type" width="1494" height="1352" data-path="img/dashboard/portal-management/enterprise-portal/configure-type-of-client-okta.png" />

    **For Okta Client Credentials**: allowed response types MUST be token only
  </Tab>
</Tabs>

## Configure API Products and plans for the DCR flow

Once the App registration settings are configured, it is time for the final step: to configure the API Products and plans to work with the DCR flow.

### Configure API Products for the DCR flow

To configure API Products to work with the DCR flow, you need to:

* Enable the DCR flow for the products you want to work with the DCR flow.
* Associate each product with one or multiple types of clients that were created in the previous step.
* Specify scopes for this API Product. Note the portal uses the scope to policy mapping to enforce access control to API Products, so there should be at least one scope.

For achieving this, navigate to the `API Products` menu and select the particular API product you want to use for the DCR flow. Next, go to the ‘App registration configs’ section and enable the ‘Enable dynamic client registration’ checkbox.

After that, specify the scope for this API product. You should have at least one scope that was created in [the Prerequisites for getting started](/tyk-stack/tyk-developer-portal/enterprise-developer-portal/api-access/dynamic-client-registration#prerequisites). If you need to specify more than one scope, you can separate them with spaces.

Finally, select one or multiple types of clients that were created in [the Create client configurations](/tyk-stack/tyk-developer-portal/enterprise-developer-portal/api-access/dynamic-client-registration#create-client-configurations) section of this guide to associate them with that product.

<Tabs>
  <Tab title="Curity">
    <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/curity-enable-product-dcr.jpg?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=aaffa81169aae1acb82686bbe689e83b" alt="Configure an API Product to work with the DCR flow" width="3432" height="1396" data-path="img/dashboard/portal-management/enterprise-portal/curity-enable-product-dcr.jpg" />
  </Tab>

  <Tab title="Keycloak">
    <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/configure-api-products-for-the-dcr-flow.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=44c496d7a44e9c43a1de5645831fa66a" alt="Configure an API Product to work with the DCR flow" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/configure-api-products-for-the-dcr-flow.png" />
  </Tab>

  <Tab title="Okta">
    <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/configure-api-products-for-the-dcr-flow-okta.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=3ddb200b776ac0727098a32600454f04" alt="Configure an API Product to work with the DCR flow" width="1496" height="1192" data-path="img/dashboard/portal-management/enterprise-portal/configure-api-products-for-the-dcr-flow-okta.png" />
  </Tab>
</Tabs>

<br />

<Note>
  From version 1.13.0, you can complete the DCR configuration for a product under the `Dynamic Client Registration` tab in the product's view. Scope to policy mapping for the selected API/s will be automatically configured using the scope defined in the `Scopes` field.

  <img src="https://mintcdn.com/tyk/UiKBFLPkIyNRnItY/img/dashboard/portal-management/enterprise-portal/portal-product-dcr.png?fit=max&auto=format&n=UiKBFLPkIyNRnItY&q=85&s=8e4b9b3156672b42d8447f03a507a641" alt="Add DCR settings" width="3456" height="1978" data-path="img/dashboard/portal-management/enterprise-portal/portal-product-dcr.png" />
</Note>

#### Configure plans for the DCR flow

The last step is to configure the plans you want to use with the DCR flow. To do this, go to the portal's `Plans` menu section and specify the OAuth2.0 scope to use with each plan. You should have at least one scope that was created in [the Prerequisites for getting started](/tyk-stack/tyk-developer-portal/enterprise-developer-portal/api-access/dynamic-client-registration#prerequisites). If you need to specify more than one scope, you can separate them with spaces.

<img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/configure-plan-for-the-dcr-flow.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=31cdc7c78bd4b954cef4251edd5bf694" alt="Configure a plan to work with the DCR flow" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/configure-plan-for-the-dcr-flow.png" />

<br />

<Note>
  From version 1.13.0, you can complete the DCR configuration for a plan under the `Advanced settings (optional)` colapsible section in the plan's view. Scope to policy mapping for the plan will be automatically configured using the scope defined in the `Scopes` field.

  <img src="https://mintcdn.com/tyk/UiKBFLPkIyNRnItY/img/dashboard/portal-management/enterprise-portal/portal-plan-advanced-settings.png?fit=max&auto=format&n=UiKBFLPkIyNRnItY&q=85&s=8f0bc85c1a91bd0f51d731195c6fa115" alt="Add Plan Advanced Settings" width="3456" height="1978" data-path="img/dashboard/portal-management/enterprise-portal/portal-plan-advanced-settings.png" />
</Note>

## Test the DCR flow

To test the DCR flow, you need to perform the following actions:

* Request access to the API product and plan you have selected for the DCR flow as a developer.
* Approve the access request as an admin.
* As a developer, copy the access credentials and obtain an access token.
* As a developer, make an API call to verify the flow's functionality.

### Request access to the API Product

To request access to the DCR enabled API Product:

* Log in as a developer and navigate to the catalog page.
* Select the DCR enabled API Product and add it to the shopping cart (if using cart-based flow) or proceed directly to checkout (if using direct access flow).
* Navigate to the checkout page.
* On the checkout page, select a plan to use with that product, select an existing application, or create a new one. If you plan to build an application that uses the Authorization code grant type, you also need to specify redirect URI of your application in the `Redirect URLs` field. If you have multiple redirect URI, you can separate them with commas.
* Select a client type which is more suitable for your use case in the `Select a client type` section.
* Finally, select the applicable type of client and click on the `Submit request` button.

<img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/request-access-to-the-dcr-enabled-product.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=19198b85755bae03a54ccddd0ee48e61" alt="Request access to the DCR enabled product" width="600" data-path="img/dashboard/portal-management/enterprise-portal/request-access-to-the-dcr-enabled-product.png" />

### Approve the access request

To approve the access request, navigate to the `Access requests` menu in the portal, select the access request and approve it by clicking on the `Approve` button.

<img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/approve-dcr-access-request.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=dd494ce6f2629c379d7f6b877ebc15ae" alt="Approve DCR access request" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/approve-dcr-access-request.png" />

<Note>
  When approving an access request, if the Plan scope is not already present in the API Product's scope mappings the Portal will append it in the scope-to-policy mapping declared in the API definition, mapping it to the Id of the Tyk Dashboard consumption policy that relates to the Plan. This will ensure that when the JWT is presented to Tyk, the Plan will be applied to the session.
</Note>

### Obtain an access token

Once the access request is approved, the developer should receive an email informing them of the approval. Please refer to [the email customization section](/portal/customization/email-notifications) if you wish to change the email template.

As a developer, navigate to the `My Dashboard` section in the developer portal, select the application, and copy the OAuth 2.0 credentials.

<img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/copy-oauth-credentials.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=6bd679b0fa54fcd011ea3ae1d795cb7e" alt="Copy the OAuth2.0 credentials" width="3024" height="1890" data-path="img/dashboard/portal-management/enterprise-portal/copy-oauth-credentials.png" />

Then use the credentials you have copied to obtain an access token. Make sure to include the scopes that are used to enforce access to the API product and plan. Otherwise, the gateway will not authorize the request. Here's an example of to achieve that with `curl`:

```curl  theme={null}
curl --location --request POST 'http://localhost:9999/realms/DCR/protocol/openid-connect/token' \
--header 'Authorization: Basic N2M2NGM2ZTQtM2I0Ny00NTMyLWFlMWEtODM1ZTMyMWY2ZjlkOjNwZGlJSXVxd004Ykp0M0toV0tLZHFIRkZMWkN3THQ0' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'scope=product_payments free_plan' \
--data-urlencode 'grant_type=client_credentials'
```

Since in this example we use the client\_secret\_basic token endpoint authentication method, the credentials must be supplied as a Base64-encoded string: `{client_id}:{client_secret}`.

As a result, you should receive a JWT access token containing the required scopes:

<img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/jwt.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=63bede0ec7aa860b15de94350a25331a" alt="An example of a JWT" width="600" data-path="img/dashboard/portal-management/enterprise-portal/jwt.png" />

### Make an API Call

Finally, use the access token to make an API call and test the flow functionality:

```curl  theme={null}
curl --location --request GET 'http://localhost:8080/payment-api/get' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJUR1ZQd25MWlduaWpNc2taU3lHeHFtYnFDNVlIcW9QUUJYZE4xTmJCRDZjIn0.eyJleHAiOjE2Nzg0NDA2ODksImlhdCI6MTY3ODQ0MDM4OSwianRpIjoiMGYwNTdlYjItODQ5My00ZmM2LTllMzQtZTk0OWUzYWQ2MmI2IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo5OTk5L3JlYWxtcy9EQ1IiLCJzdWIiOiJlNGE3YmFkNy04ZDA4LTQxOTAtODc1Ni1mNTU1ZWQ3Y2JhZjciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiI3YzY0YzZlNC0zYjQ3LTQ1MzItYWUxYS04MzVlMzIxZjZmOWQiLCJzY29wZSI6ImZyZWVfcGxhbiBwcm9kdWN0X3BheW1lbnRzIiwiY2xpZW50SWQiOiI3YzY0YzZlNC0zYjQ3LTQ1MzItYWUxYS04MzVlMzIxZjZmOWQiLCJjbGllbnRIb3N0IjoiMTcyLjE3LjAuMSIsImNsaWVudEFkZHJlc3MiOiIxNzIuMTcuMC4xIn0.WGp9UIqE7CjFhHdaM64b0G2HGP4adaDg3dgc0YVCV9rTDYmri32Djku7PcLiDKyNLCvlQXUm_O2YmwMCLLUHKPGlRmBMG2y-79-T8z5V-qBATbE6uzwPh38p-SYIIDBUZtlMEhnVp049ZqNolUW-n2uB4CTRb0kDosdRnqhiMUFpe-ORwnZB-4BHGRlwWKyjc5Da6CvVczM1a_c5akqurGMFaX9DC81SS-zMXXpQPDpAkvUJBfLYDHEvXWH8JISqYv7ZQSAbOyE4b-EkVAesyHIMDCQ_pzf5Yp2ivM0dOufN9kdG2w_9ToMqJieVyQILJPowEakmEealbNUFQvc5FA'
```

You should receive the following response:

```{.json}  theme={null}
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJUR1ZQd25MWlduaWpNc2taU3lHeHFtYnFDNVlIcW9QUUJYZE4xTmJCRDZjIn0.eyJleHAiOjE2Nzg0NDA2ODksImlhdCI6MTY3ODQ0MDM4OSwianRpIjoiMGYwNTdlYjItODQ5My00ZmM2LTllMzQtZTk0OWUzYWQ2MmI2IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo5OTk5L3JlYWxtcy9EQ1IiLCJzdWIiOiJlNGE3YmFkNy04ZDA4LTQxOTAtODc1Ni1mNTU1ZWQ3Y2JhZjciLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiI3YzY0YzZlNC0zYjQ3LTQ1MzItYWUxYS04MzVlMzIxZjZmOWQiLCJzY29wZSI6ImZyZWVfcGxhbiBwcm9kdWN0X3BheW1lbnRzIiwiY2xpZW50SWQiOiI3YzY0YzZlNC0zYjQ3LTQ1MzItYWUxYS04MzVlMzIxZjZmOWQiLCJjbGllbnRIb3N0IjoiMTcyLjE3LjAuMSIsImNsaWVudEFkZHJlc3MiOiIxNzIuMTcuMC4xIn0.WGp9UIqE7CjFhHdaM64b0G2HGP4adaDg3dgc0YVCV9rTDYmri32Djku7PcLiDKyNLCvlQXUm_O2YmwMCLLUHKPGlRmBMG2y-79-T8z5V-qBATbE6uzwPh38p-SYIIDBUZtlMEhnVp049ZqNolUW-n2uB4CTRb0kDosdRnqhiMUFpe-ORwnZB-4BHGRlwWKyjc5Da6CvVczM1a_c5akqurGMFaX9DC81SS-zMXXpQPDpAkvUJBfLYDHEvXWH8JISqYv7ZQSAbOyE4b-EkVAesyHIMDCQ_pzf5Yp2ivM0dOufN9kdG2w_9ToMqJieVyQILJPowEakmEealbNUFQvc5FA",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.85.0",
  },
  "origin": "XXX.XXX.XXX.XXX, XXX.XXX.XXX.XXX",
  "url": "http://httpbin.org/get"
}
```


Built with [Mintlify](https://mintlify.com).