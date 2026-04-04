# Source: https://ngrok.com/docs/integrations/oauth/linkedin-oauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LinkedIn OAuth

> Configure ngrok to authenticate users with LinkedIn OAuth. Create an app in the LinkedIn Developer Portal and set the callback URL.

This guide explains how to create a LinkedIn app and configure ngrok to use LinkedIn OAuth for user authentication.
The steps follow LinkedIn's [OAuth 2.0 setup documentation](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow?tabs=HTTPS1#step-1-configure-your-application) for web applications.

## What you'll need

* A [LinkedIn](https://www.linkedin.com/) account and (optionally) a LinkedIn Page for your app.
* Your ngrok authtoken and an endpoint with the OAuth action in its Traffic Policy.

## Create credentials for ngrok

1. Go to the [LinkedIn Developer Portal](https://developer.linkedin.com/), sign in, click **My apps** in the top menu, and then click **Create app**.

2. Enter **App name**, select a **LinkedIn Page**, enter the **Privacy policy URL**, and then click **Create app**.

3. On the app page, open the **Auth** tab and note the **Client ID** and **Client Secret** values.

4. In the **OAuth 2.0 settings** section, click the pencil icon next to **Authorized redirect URLs**, add `https://idp.ngrok.com/oauth2/callback`, and then click **Update**.

5. Open the **Products** tab and click **Request access** for **Sign In with LinkedIn using OpenID Connect**.

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
            provider: linkedin
            client_id: '{your app''s oauth client id}'
            client_secret: '{your app''s oauth client secret}'
            scopes:
              - r_emailaddress
              - r_liteprofile
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "oauth",
            "config": {
              "provider": "linkedin",
              "client_id": "{your app's oauth client id}",
              "client_secret": "{your app's oauth client secret}",
              "scopes": [
                "r_emailaddress",
                "r_liteprofile"
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

* [Authorization Code Flow](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow)


Built with [Mintlify](https://mintlify.com).