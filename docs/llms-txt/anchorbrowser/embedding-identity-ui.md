# Source: https://docs.anchorbrowser.io/essentials/embedding-identity-ui.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Embedding End-User Authentication UI (Early Availability)

> Anchor provides an embeddable identity creation flow that allows end-users to authenticate to third-party websites directly from your application, enabling [authenticated browser sessions](/essentials/authenticated-applications).

<Warning>
  This feature is currently in **Early Availability**. Contact [**support**](mailto:support@anchorbrowser.io) to enable this feature.
</Warning>

## Prerequisites

Before integrating the embedded identity flow, ensure the following are configured:

1. **[Create an Application](/essentials/authenticated-applications)** - Define the target website users will authenticate to via the Anchor Dashboard or API
2. **[Configure Authentication Flows](/essentials/authenticated-applications#configure-auth-flow-for-the-application)** - Set up the supported login methods.

## Overview

<Steps>
  <Step title="Generate a Token">
    Create a one-time token that authorizes the identity creation flow.

    <CodeGroup>
      ```javascript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const anchorClient = new Anchorbrowser();

      // Generate a token for identity creation
      const tokenResponse = await anchorClient.applications.createIdentityToken(
          'your-application-id',
          { callbackUrl: 'https://your-app.com/identity-callback' }
      );

      console.log(tokenResponse.token);
      // Use this token to redirect the user
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser()

      # Generate a token for identity creation
      token_response = anchor_client.applications.create_identity_token(
          application_id="your-application-id",
          callback_url="https://your-app.com/identity-callback"
      )

      print(token_response.token)
      # Use this token to redirect the user
      ```

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/applications/{application_id}/tokens" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "callbackUrl": "https://your-app.com/identity-callback"
        }'
      ```
    </CodeGroup>

    <Warning>
      The `callbackUrl` must use HTTPS. Store the token securely and use it immediately - tokens are single-use and expire
      after 15 minutes.
    </Warning>
  </Step>

  <Step title="Redirect User to Identity Creation">
    Redirect the user to the Anchor identity creation page with the generated token:

    ```
    https://app.anchorbrowser.io/identity/create?token={token}
    ```

    <CodeGroup>
      ```javascript Frontend (React) theme={null}
      function CreateIdentityButton({ token }) {
        const handleClick = () => {
          window.location.href = `https://app.anchorbrowser.io/identity/create?token=${token}`;
        };

        return <button onClick={handleClick}>Connect Your Account</button>;
      }
      ```
    </CodeGroup>

    The user will be guided through the authentication process for the target website configured in the application.
  </Step>

  <Step title="Handle the Callback">
    After the user successfully creates an identity, Anchor redirects them to the `callbackUrl` with the identity ID:

    ```
    https://your-app.com/identity-callback?identityId={identity_id}
    ```

    <CodeGroup>
      ```javascript Express.js theme={null}
      app.get('/identity-callback', async (req, res) => {
        const { identityId } = req.query;

        if (!identityId) {
          return res.status(400).send('Missing identity ID');
        }

        // Store the mapping between the user and the Anchor identity
        await saveUserIdentityMapping(req.user.id, identityId);

        // Optionally, update the identity with an external user ID

        res.redirect('/dashboard?connected=true');
      });
      ```

      ```python Flask theme={null}
      @app.route('/identity-callback')
      def identity_callback():
          identity_id = request.args.get('identityId')

          if not identity_id:
              return 'Missing identity ID', 400

          # Store the mapping between the user and the Anchor identity
          save_user_identity_mapping(current_user.id, identity_id)

          # Optionally, update the identity with an external user ID (See next step)

          return redirect('/dashboard?connected=true')
      ```
    </CodeGroup>
  </Step>

  <Step title="Update Identity Metadata (Optional)">
    Update the identity with additional metadata to maintain a mapping between users and their Anchor identities:

    <CodeGroup>
      ```javascript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const anchorClient = new Anchorbrowser();

      // Update identity with external user ID
      const updatedIdentity = await anchorClient.identities.update('your-identity-id', {
        name: 'User Display Name',
        metadata: {
          externalUserId: 'your-user-id-123',
          plan: 'premium',
          connectedAt: new Date().toISOString(),
        },
      });
      ```

      ```python python theme={null}
      from anchorbrowser import Anchorbrowser

      anchor_client = Anchorbrowser()

      # Update identity with external user ID
      updated_identity = anchor_client.identities.update(
          identity_id='your-identity-id',
          name="User Display Name",
          metadata={
              "externalUserId": "your-user-id-123",
              "plan": "premium",
              "connectedAt": datetime.now().isoformat()
          }
      )
      ```

      ```bash cURL theme={null}
      curl -X PUT "https://api.anchorbrowser.io/v1/identities/{identity_id}" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "name": "User Display Name",
          "metadata": {
            "externalUserId": "your-user-id-123",
            "plan": "premium"
          }
        }'
      ```
    </CodeGroup>
  </Step>

  <Step title="Create Authenticated Sessions">
    Once an identity ID is available, use it to create authenticated browser sessions:

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

      ```bash cURL theme={null}
      curl -X POST "https://api.anchorbrowser.io/v1/sessions" \
        -H "anchor-api-key: YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
        "browser": {
          "captcha_solver": {
            "active": true
          },
          "extra_stealth": {
            "active": true
          }
        },
        "session": {
          "proxy": {
            "active": true
          }
        },
        "identities": [
          {
            "id": "your-identity-id"
          }
        ]
      }'
      ```
    </CodeGroup>

    The browser session will automatically be authenticated to the target website using the stored identity.
  </Step>
</Steps>

## Complete Integration Example

Here's a complete example showing the full flow:

<CodeGroup>
  ```javascript node.js (Express) theme={null}
  import express from 'express';
  import Anchorbrowser from 'anchorbrowser';

  const app = express();
  const anchorClient = new Anchorbrowser();

  const APPLICATION_ID = 'your-application-id';

  // Step 1: Initiate identity creation
  app.post('/api/connect-account', async (req, res) => {
    const userId = req.user.id;

    // Generate token with callback URL
    const tokenResponse = await anchorClient.applications.createIdentityToken(APPLICATION_ID, {
      callbackUrl: `https://your-app.com/api/identity-callback`,
    });

    // Store token-to-user mapping for callback verification
    await storeTokenMapping(tokenResponse.tokenHash, userId);

    // Return redirect URL to frontend
    res.json({
      redirectUrl: `https://app.anchorbrowser.io/identity/create?token=${tokenResponse.token}`,
    });
  });

  // Step 2: Handle callback after identity creation
  app.get('/api/identity-callback', async (req, res) => {
    const { identityId } = req.query;

    // Save identity mapping
    await saveIdentityMapping(req.user.id, identityId);

    // Update identity with external reference
    await anchorClient.identities.update(identityId, {
      metadata: { externalUserId: req.user.id },
    });

    res.redirect('/dashboard?connected=true');
  });

  // Step 3: Use identity in browser sessions
  app.post('/api/run-automation', async (req, res) => {
    const identityId = await getUserIdentity(req.user.id);

    const session = await anchorClient.sessions.create({
      browser: {
        identities: [{ id: identityId }],
      },
    });

    // Run your automation with the authenticated session
    // ...

    res.json({ sessionId: session.id });
  });
  ```

  ```python python (Flask) theme={null}
  from flask import Flask, request, redirect, jsonify
  from anchorbrowser import Anchorbrowser

  app = Flask(__name__)
  anchor_client = Anchorbrowser()

  APPLICATION_ID = "your-application-id"

  # Step 1: Initiate identity creation
  @app.route("/api/connect-account", methods=["POST"])
  def connect_account():
      user_id = request.user.id

      # Generate token with callback URL
      token_response = anchor_client.applications.identities.tokens.create(
          application_id=APPLICATION_ID,
          callback_url="https://your-app.com/api/identity-callback"
      )

      # Store token-to-user mapping for callback verification
      store_token_mapping(token_response.token_hash, user_id)

      # Return redirect URL to frontend
      return jsonify({
          "redirectUrl": f"https://app.anchorbrowser.io/identity/create?token={token_response.token}"
      })

  # Step 2: Handle callback after identity creation
  @app.route("/api/identity-callback")
  def identity_callback():
      identity_id = request.args.get("identityId")

      # Save identity mapping
      save_identity_mapping(request.user.id, identity_id)

      # Update identity with external reference
      anchor_client.identities.update(
          identity_id=identity_id,
          metadata={"externalUserId": request.user.id}
      )

      return redirect("/dashboard?connected=true")

  # Step 3: Use identity in browser sessions
  @app.route("/api/run-automation", methods=["POST"])
  def run_automation():
      identity_id = get_user_identity(request.user.id)

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

      # Run your automation with the authenticated session
      # ...

      return jsonify({"sessionId": session.id})
  ```
</CodeGroup>

## Best Practices

<CardGroup cols={2}>
  <Card title="Secure Token Handling" icon="lock">
    Generate tokens server-side and never expose your API key to the frontend. Tokens are single-use and should be used immediately.
  </Card>

  <Card title="Store Identity Mappings" icon="database">
    Maintain a mapping between your users and their Anchor identity IDs in your database for future session creation.
  </Card>

  <Card title="Use Metadata" icon="tags">
    Store your external user ID in the identity metadata to easily correlate identities with your users.
  </Card>

  <Card title="Handle Errors" icon="triangle-exclamation">
    Implement proper error handling for cases where identity creation fails or the user cancels the flow.
  </Card>
</CardGroup>

## Related Resources

* [Authenticated Applications](/essentials/authenticated-applications) - Define target websites, authentication flows, and create pre-authenticated browser sessions
* [Browser Profiles](/essentials/authentication-and-identity) - Alternative approach using browser profiles
