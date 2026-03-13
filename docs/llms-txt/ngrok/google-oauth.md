# Source: https://ngrok.com/docs/integrations/oauth/google-oauth.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google OAuth

> Configure ngrok to authenticate users with Google OAuth 2.0. Set up a GCP project, consent screen, and OAuth client.

By default, if you use `"google"` for OAuth in your Traffic Policies without specifying a Google OAuth application, visitors are authenticated using ngrok's managed Google OAuth instance.
Setting up your own Google OAuth application lets you customize authentication in more detail.
This guide walks you through creating a Google OAuth 2.0 application for your ngrok endpoints.

## What you'll need

* A [Google Cloud Platform](https://console.cloud.google.com) account and project.
* Your ngrok authtoken and an endpoint with the OAuth action in its Traffic Policy.

## 1. Build the consent screen

1. Create or select a project in the [Google Cloud Platform Console](https://console.cloud.google.com).
2. Open the project's [OAuth consent screen](https://console.developers.google.com/apis/credentials/consent).
3. Select whether your application is an [internal or external app](https://support.google.com/cloud/answer/6158849?hl=en#public-and-internal).
4. Fill out the application name and support email.
5. Add any additional scopes required by your application and save the full scope URI for later.
   * [Possible scope URIs](https://developers.google.com/identity/protocols/oauth2/scopes)
6. Ensure the `email` and `profile` scopes remain selected.
7. Under **Authorized domains**, add `ngrok.com` and your application homepage domain.
8. Add links to your application homepage and privacy policy.
9. Save the application.
   * Applications that require verification cannot complete the consent screen and are not supported by ngrok.

## 2. Create credentials for ngrok

1. Open [Credentials](https://console.cloud.google.com/apis/credentials) for your project.
2. Click **Create credentials** in the top menu and select **OAuth client ID**.
3. Choose **Web application** from the list of application types.
4. Name your client, set **Authorized redirect URIs** to `https://idp.ngrok.com/oauth2/callback`, and complete the form.
5. Securely store the **Client ID** and **Client secret** from the final screen.

## 3. Update your ngrok endpoint Traffic Policy

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
            provider: google
            client_id: '{your app''s oauth client id}'
            client_secret: '{your app''s oauth client secret}'
            scopes:
              - https://www.googleapis.com/auth/userinfo.profile
              - https://www.googleapis.com/auth/userinfo.email
  ```

  ```json policy.json theme={null}
  {
    "on_http_request": [
      {
        "actions": [
          {
            "type": "oauth",
            "config": {
              "provider": "google",
              "client_id": "{your app's oauth client id}",
              "client_secret": "{your app's oauth client secret}",
              "scopes": [
                "https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/userinfo.email"
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

* [Google OAuth 2.0 Web Server](https://developers.google.com/identity/protocols/oauth2/web-server) (prerequisite steps)
* [GCP Help: Setting up OAuth 2.0](https://support.google.com/cloud/answer/6158849?hl=en)
* [Google OAuth 2.0 workflow](https://developers.google.com/identity/protocols/oauth2)


Built with [Mintlify](https://mintlify.com).