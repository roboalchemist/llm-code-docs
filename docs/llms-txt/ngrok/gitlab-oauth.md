# Source: https://ngrok.com/docs/integrations/oauth/gitlab-oauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GitLab OAuth

> Configure ngrok to authenticate users with GitLab OAuth. Create an app and set the redirect URI and scopes.

This guide shows you how to create a GitLab application and configure ngrok to use GitLab OAuth for user authentication.
The steps below follow GitLab's [OAuth 2.0 setup documentation](https://docs.gitlab.com/ee/integration/oauth_provider.html) for web applications.

## What you'll need

* A [GitLab](https://gitlab.com/) account.
* Your ngrok authtoken and an endpoint with the OAuth action in its Traffic Policy.

## Create an application

1. Open your [GitLab profile page](https://gitlab.com/-/profile) and select **Applications** in the left menu.

<Note>
  **Restricting sign-in:** To limit which users can sign in with GitLab, create the application under one of your groups or as an instance-wide application.
  See [Further resources](#further-resources) for more detail.
</Note>

2. Enter a **Name** for your application and set **Redirect URI** to `https://idp.ngrok.com/oauth2/callback`.

3. In the **Scopes** section, select the scopes appropriate for your app (for example, **openid**, **profile**, and **email**) and then click **Save application**.

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
            provider: gitlab
            client_id: '{your app''s oauth client id}'
            client_secret: '{your app''s oauth client secret}'
            scopes:
              - openid
              - profile
              - email
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "oauth",
            "config": {
              "provider": "gitlab",
              "client_id": "{your app's oauth client id}",
              "client_secret": "{your app's oauth client secret}",
              "scopes": [
                "openid",
                "profile",
                "email"
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

* [Configure GitLab as an OAuth 2.0 authentication identity provider](https://docs.gitlab.com/ee/integration/oauth_provider.html)
* [OAuth 2.0 identity provider API](https://docs.gitlab.com/ee/api/oauth2.html)


Built with [Mintlify](https://mintlify.com).