# Source: https://ngrok.com/docs/integrations/oauth/microsoft-oauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Microsoft OAuth

> Configure ngrok to authenticate users with Microsoft Entra ID (Azure AD) OAuth. Register an app in the Azure portal.

This guide walks you through registering a Microsoft Entra ID application and configuring ngrok to use it for user authentication.
The steps below follow [Microsoft's app registration documentation](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in the Azure portal.

## What you'll need

* An [Azure](https://portal.azure.com/) account and a tenant (or [create a tenant](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant)).
* Your ngrok authtoken and an endpoint with the OAuth action in its Traffic Policy.

## Register an application

1. Sign in to the [Azure portal](https://portal.azure.com/) and select or create a tenant for your application.
2. Search for **Microsoft Entra ID** and select it.
3. In the left-hand navigation, select **App registrations**.
4. Select **New registration** at the top.
5. Enter a name for your application.
6. ngrok does not support [single-tenant applications](https://learn.microsoft.com/en-us/entra/identity-platform/single-and-multi-tenant-apps).
   Choose one of these supported account types:
   * Accounts in any organizational directory (Any Microsoft Entra directory - Multitenant)
   * Accounts in any organizational directory and personal Microsoft accounts (for example, Skype, Xbox)
7. Under redirect URI, choose **Web** and enter `https://idp.ngrok.com/oauth2/callback`.
8. Click **Register**.

## Configure your application

1. With your application open, select **Overview** in the left-hand navigation.
2. In the top information section, note the **Application (client) ID** for later.
3. Select **API permissions** in the left-hand navigation.
4. Add any additional scopes your application requires and note them for later.
   * Scopes that require application review by Microsoft are unsupported.
   * Scopes that [require admin consent](https://learn.microsoft.com/en-us/entra/identity-platform/permissions-consent-overview#admin-restricted-permissions) prevent tenants' users from authorizing until consent is granted.
5. Ensure `User.Read` or a more permissive scope (for example, `User.Read.All`) is configured for ngrok.
6. Select **Certificates & secrets** in the left-hand navigation.
7. Select **New client secret** at the bottom, name the secret, set an expiration, and click **Add**.
8. Creation is asynchronous.
   When the secret appears, copy the **Value** and store it securely (the value is shown only once).

## Update your ngrok endpoint Traffic Policy

1. Access the [ngrok Dashboard Endpoints page](https://dashboard.ngrok.com/endpoints?sortBy=createdAt\&orderBy=desc) and locate an existing endpoint you'd like to add this to or create a new one.
2. In your traffic policy, add the following configuration:

<Note>
  You may add [any scopes](https://developers.facebook.com/docs/apps/review/login-permissions) that are required by your application with the following caveats.

  * Scopes which require a Facebook [app review](https://developers.facebook.com/docs/apps/review/#app-review) are unsupported.
  * ngrok will enforce that users [accept all permissions](https://developers.facebook.com/docs/facebook-login/handling-declined-permissions#reprompt) before completing authorization.
</Note>

<CodeGroup>
  ```yaml policy.yml theme={null}
  on_http_request:
    - actions:
        - type: oauth
          config:
            provider: microsoft
            client_id: '{your app''s oauth client id}'
            client_secret: '{your app''s oauth client secret}'
            scopes:
              - openid
              - email
              - profile
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "oauth",
            "config": {
              "provider": "microsoft",
              "client_id": "{your app's oauth client id}",
              "client_secret": "{your app's oauth client secret}",
              "scopes": [
                "openid",
                "email",
                "profile"
              ]
            }
          }
        ]
      }
    ]
  }
  ```
</CodeGroup>

Click **Save** to validate and update your traffic policy.

### Configure access control

Optionally, configure access control to your service by only allowing specific users or domains.

<Tabs>
  <Tab title="By Email">
    <CodeGroup>
      ```yaml policy.yml theme={null}
      on_http_request:
        - expressions:
            - '!(actions.ngrok.oauth.identity.email in [''me@example.com''])'
          actions:
            - type: deny
      ```

      ```json policy.json theme={null}
      {
        "on_http_request": [
          {
            "expressions": [
              "!(actions.ngrok.oauth.identity.email in ['me@example.com'])"
            ],
            "actions": [
              {
                "type": "deny"
              }
            ]
          }
        ]
      }
      ```
    </CodeGroup>
  </Tab>

  <Tab title="By Name">
    <CodeGroup>
      ```yaml policy.yml theme={null}
      on_http_request:
        - expressions:
            - '!(actions.ngrok.oauth.identity.name in [''My Name''])'
          actions:
            - type: deny
      ```

      ```json policy.json theme={null}
      {
        "on_http_request": [
          {
            "expressions": [
              "!(actions.ngrok.oauth.identity.name in ['My Name'])"
            ],
            "actions": [
              {
                "type": "deny"
              }
            ]
          }
        ]
      }
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Further resources

* [Creating a Microsoft Entra ID tenant](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant)
* [Permissions and consent](https://learn.microsoft.com/en-us/entra/identity-platform/permissions-consent-overview#admin-restricted-permissions) (restricted permissions)
* [Microsoft Graph User resource type](https://learn.microsoft.com/en-us/graph/api/resources/user) (id, displayName, mail, userPrincipalName)


Built with [Mintlify](https://mintlify.com).