# Source: https://docs.anchorbrowser.io/essentials/authenticated-applications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Authenticated Applications (Early Availability)

> Define target websites, configure supported login methods (auth flows), let end-users authenticate via an [Embeddable UI](/essentials/embedding-identity-ui), and create pre-authenticated browser sessions to those websites.

<Warning>
  This feature is currently in **Early Availability**. Contact [**support**](mailto:support@anchorbrowser.io) to enable this feature.
</Warning>

<Steps>
  <Step title="Create an Application">
    <CodeGroup>
      ```javascript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const anchorClient = new Anchorbrowser();

      // Create an application for a target website
      const app = await anchorClient.applications.create({
        name: 'My LinkedIn User',
        source: 'linkedin.com'
      });

      console.log(app.id);
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser()

      # Create an application for a target website
      app = anchor_client.applications.create(
          name="My LinkedIn User",
          source="linkedin.com"
      )

      print(app.id)
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/applications" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{"name": "My LinkedIn User", "source": "linkedin.com"}'
      ```
    </CodeGroup>
  </Step>

  <Step title="Configure Auth Flow for the Application">
    Applications support multiple authentication flows: `username_password`, `authenticator`, and `custom`.

    <CodeGroup>
      ```javascript node.js theme={null}
      await anchorClient.applications.authFlows.create(app.id, {
        name: 'Email Login with authenticator',
        methods: ['username_password', 'authenticator']
      });
      ```

      ```python python theme={null}
      anchor_client.applications.auth_flows.create(
          application_id=app.id,
          name="Email Login with authenticator",
          methods=["username_password", "authenticator"]
      )
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/applications/{app_id}/auth-flows" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{"name": "Email Login with authenticator", "methods": ["username_password", "authenticator"]}'
      ```
    </CodeGroup>
  </Step>

  <Step title="Create Identity">
    Create an identity with credentials for the application.

    <CodeGroup>
      ```javascript node.js theme={null}
      const identity = await anchorClient.identities.create({
        source: 'https://linkedin.com',
        name: 'John Doe',
        credentials: [{
          type: 'username_password',
          username: 'john@example.com',
          password: 'secret'
        }]
      });

      console.log(identity.id);
      ```

      ```python python theme={null}
      identity = anchor_client.identities.create(
          source="https://linkedin.com",
          name="John Doe",
          credentials=[{
              "type": "username_password",
              "username": "john@example.com",
              "password": "secret"
          }]
      )

      print(identity.id)
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/identities" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "source": "https://linkedin.com",
          "name": "John Doe",
          "credentials": [{
            "type": "username_password",
            "username": "john@example.com",
            "password": "secret"
          }]
        }'
      ```
    </CodeGroup>

    <Tip>
      For end-user self-service authentication, use the [Embeddable Identity UI](/essentials/embedding-identity-ui).
    </Tip>
  </Step>

  <Step title="Create Authenticated Sessions">
    Use the identity ID to create an authenticated browser session.

    <CodeGroup>
      ```javascript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const anchorClient = new Anchorbrowser();
      const identityId = "your-identity-id";
      const session = await anchorClient.sessions.create({
          // Recommended settings for authenticated sessions.
          session: {
              proxy: {
                  active: true,
              }
          },
          browser: {
              captcha_solver: {
                  active: true,
              },
              extra_stealth: {
                  active: true,
              }
          },

          // Identity to authenticate with.
          identities: [{ id: identityId }]
      });

      console.log(session.data.id);
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser()
      identity_id = "your-identity-id"
      session = anchor_client.sessions.create(
          # Recommended settings for authenticated sessions.
          session={
              "proxy": {
                  "active": True,
              }
          },
          browser={
              "captcha_solver": {
                  "active": True,
              },
              "extra_stealth": {
                  "active": True,
              }
          },

          # Identity to authenticate with.
          identities=[{"id": identity_id}]
      )

      print(session.data.id)
      ```
    </CodeGroup>
  </Step>
</Steps>

## Related

<CardGroup cols={3}>
  <Card title="Embedding End-User Authentication UI" icon="window" href="/essentials/embedding-identity-ui">
    Embed the authentication flow in your app
  </Card>

  <Card title="Browser Profiles" icon="fingerprint" href="/essentials/authentication-and-identity">
    Alternative approach using browser profiles
  </Card>

  <Card title="API Reference" icon="code" href="/api-reference/applications-early-availability/">
    Applications and Identities endpoints
  </Card>
</CardGroup>
