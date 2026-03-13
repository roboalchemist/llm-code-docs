# Source: https://ngrok.com/docs/integrations/oauth/twitch-oauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Twitch OAuth

> Configure ngrok to authenticate users with Twitch OAuth. Register an application in the Twitch developer console.

This guide explains how to register a Twitch application and configure ngrok to use Twitch OAuth for user authentication.
The steps follow Twitch's [OAuth 2.0 documentation](https://dev.twitch.tv/docs/authentication/).

## What you'll need

* A [Twitch](https://www.twitch.tv/) account (two-factor authentication enabled for your developer account is recommended).
* Your ngrok authtoken and an endpoint with the OAuth action in its Traffic Policy.

## Create credentials for ngrok

1. Go to the [Twitch developer console](https://dev.twitch.tv/console), sign in, click **Applications** in the left menu, and then click **Register Your Application**.

2. On the **Register Your Application** page, enter a **Name**, set **OAuth Redirect URLs** to `https://idp.ngrok.com/oauth2/callback`, select **Website Integration** in the **Category** selector, and then click **Create**.

<Note>
  **Security:** Enable two-factor authentication for your Twitch account before registering an app.
</Note>

3. On the **Developer Applications** page, click **Manage** for your application.

4. On the application page, click **New Secret** and note the **Client ID** and **Client Secret** values.

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
            provider: twitch
            client_id: '{your app''s oauth client id}'
            client_secret: '{your app''s oauth client secret}'
            scopes:
              - user:read:email
              - openid
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "oauth",
            "config": {
              "provider": "twitch",
              "client_id": "{your app's oauth client id}",
              "client_secret": "{your app's oauth client secret}",
              "scopes": [
                "user:read:email",
                "openid"
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

* [Authentication](https://dev.twitch.tv/docs/authentication/)
* [Registering Your App](https://dev.twitch.tv/docs/authentication/register-app/)


Built with [Mintlify](https://mintlify.com).