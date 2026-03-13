# Source: https://ngrok.com/docs/traffic-policy/actions/oauth.md

# Source: https://ngrok.com/docs/k8s/guides/how-to/oauth.md

# Source: https://ngrok.com/docs/integrations/oauth/oauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Amazon OAuth

> Configure ngrok to authenticate users with Amazon OAuth (Login with Amazon) for websites and apps.

This guide walks you through configuring ngrok to use Amazon OAuth (Login with Amazon) for user authentication.
The steps below follow Amazon's [Register for Login with Amazon](https://developer.amazon.com/docs/login-with-amazon/register-web.html) documentation for websites.

## What you'll need

* Your [Amazon Developer account](https://developer.amazon.com/loginwithamazon/console/site/lwa/overview.html) (sign up if you don't have one).
* Your ngrok authtoken and an endpoint with the OAuth action in its Traffic Policy.

## Create a security profile for ngrok

1. Navigate to the [Login with Amazon](https://developer.amazon.com/loginwithamazon/console/site/lwa/overview.html) portal and sign in with your Amazon Developer credentials.

<Note>
  If you don't have a developer account, you'll need to sign up for a new one.
</Note>

2. Click **Create a New Security Profile**, provide a **Name** and a **Description** for your security profile, enter your application's privacy URL (for example, `https://ngrok.com/privacy`) in the **Consent Privacy Notice URL**, and then click **Save**.

3. Click **Show Client ID and Client Secret** to reveal your **Client ID** and **Client Secret** and make a note of both.

4. Hover over the gear icon of the **Security Profile** you created and then click **Web Settings**.

5. On the **Security Profile** page, click **Edit**, enter `https://idp.ngrok.com/oauth2/callback` in the **Allowed Return URLs** field, and then click **Save**.

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
            provider: amazon
            client_id: '{your app''s oauth client id}'
            client_secret: '{your app''s oauth client secret}'
            scopes:
              - profile
  ```

  ```json policy.json  theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "oauth",
            "config": {
              "provider": "amazon",
              "client_id": "{your app's oauth client id}",
              "client_secret": "{your app's oauth client secret}",
              "scopes": [
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

* [Login with Amazon Documentation](https://developer.amazon.com/docs/login-with-amazon/documentation-overview.html)
* [Login with Amazon for Websites Overview](https://developer.amazon.com/docs/login-with-amazon/web-docs.html)


Built with [Mintlify](https://mintlify.com).