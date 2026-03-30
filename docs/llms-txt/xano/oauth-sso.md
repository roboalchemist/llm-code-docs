# Source: https://docs.xano.com/building-backend-features/user-authentication-and-user-data/oauth-sso.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OAuth (SSO)

**OAuth** is a security framework that allows you to grant websites or applications access to your information without sharing your password. It acts like a permission slip, letting a service access part of your data from another service on your behalf. For example, you might log into a new app using your Google or Facebook account, and OAuth handles the secure sharing of your data between the services.

## **OAuth vs JWE Token Authentication**

**OAuth** is like giving a valet key to a friend, allowing them limited access to your car. It lets services share your data safely without sharing your password. You're still in control, and you can revoke this access at any time.

**JWE Token Authentication** is more like using a sealed envelope. Your information is encrypted and can only be read by the intended recipient. It ensures data integrity and privacy but doesn't manage who has access like OAuth does. It's great for situations where secure data transmission is key.

## The OAuth Flow

1. **Client Registration**: The client application registers with the OAuth service provider to obtain a client ID and client secret, which are used to identify the application during the OAuth flow.

2. **User Authorization**: The client redirects the user to the authorization server where the user logs in and consents to the application's data access request. This is where the user would see a Google, Facebook, X, or other sign-in option on your frontend.

3. **Authorization Grant**: Once the user signs in and approves access, the authorization server issues an authorization grant to the client, typically in the form of a code sent via a URL query parameter. This would be one of your APIs in Xano that is designed to ingest that authorization.

4. **Access Token Request**: Your Xano API sends a request to the authorization server's token endpoint, including the authorization grant and credentials (client ID and secret), to obtain an access token. Once we've determined that token is valid, it will be traded for a Xano JWE token to proceed with standard authentication methods.

5. **Access Token Response**: The authorization server verifies the request and returns an access token, which the client can use to access protected resources on the user's behalf.

6. **Access Resource**: The client uses the access token to make requests to the resource server, accessing the user's resources as allowed by the token's scope.

## Building OAuth in Xano

<Steps>
  <Step title="Enable Marketplace access in your workspace">
    If you don't see **Marketplace** in your left-hand navigation menu, head to your workspace settings, and click the icon in the top-right corner, and click **Settings**.

    Check the box to **Enable Marketplace**
  </Step>

  <Step title="Access the Marketplace and browse for your OAuth extension of choice">
    Xano provides several prebuilt OAuth flows that you can import from here into your workspace.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/8674243d-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=fc19544a9ee0a3176c1d82d1a1da62c7" width="1500" height="447" data-path="images/8674243d-image.jpeg" />
    </Frame>
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).