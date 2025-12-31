# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/authenticated-access/setting-up-a-custom-backend.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/authenticated-access/setting-up-a-custom-backend.md

# Source: https://gitbook.com/docs/publishing-documentation/authenticated-access/setting-up-a-custom-backend.md

# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/authenticated-access/setting-up-a-custom-backend.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/authenticated-access/setting-up-a-custom-backend.md

# Source: https://gitbook.com/docs/publishing-documentation/authenticated-access/setting-up-a-custom-backend.md

# Setting up a custom backend

{% hint style="warning" %}
This guide takes you through setting up a protected sign-in screen for your docs. Before going through this guide, make sure you’ve first gone through the process of [enabling authenticated access](https://gitbook.com/docs/publishing-documentation/authenticated-access/enabling-authenticated-access).
{% endhint %}

This guide walks you through setting up a protected sign-in screen for your GitBook documentation site using your own **custom** authentication backend.

{% hint style="info" %}
If you are using one of the authentication providers we support or have an [OpenID Connect](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol) (OIDC) compliant backend, check out our integration guides for a more streamlined setup:\
\
[Auth0](https://gitbook.com/docs/publishing-documentation/authenticated-access/setting-up-auth0) | [Azure AD](https://gitbook.com/docs/publishing-documentation/authenticated-access/setting-up-azure-ad) | [Okta](https://gitbook.com/docs/publishing-documentation/authenticated-access/setting-up-okta) | [AWS Cognito](https://gitbook.com/docs/publishing-documentation/authenticated-access/setting-up-aws-cognito) | [OIDC](https://gitbook.com/docs/publishing-documentation/authenticated-access/setting-up-oidc)
{% endhint %}

### Overview

To setup a custom authentication system for your GitBook site, follow these key steps:

{% stepper %}
{% step %}
[**Create a custom backend to authenticate your users**](#id-1.-create-a-custom-backend-to-authenticate-your-users)

Implement a backend that prompts users to login and authenticate them.
{% endstep %}

{% step %}
[**Sign and pass a JWT token to GitBook**](#id-2.-sign-and-pass-a-jwt-token-to-gitbook)

Create a JWT token and sign it with your site’s private key.
{% endstep %}

{% step %}
[**Configure a fallback URL**](#id-3.-configure-a-fallback-url)

Configure a URL to be used when an unauthenticated visitor access your site.
{% endstep %}

{% step %}
[**Set up multi-tenant authenticated access (optional)**](#id-4.-set-up-multi-tenant-authenticated-access)

Configure your backend to handle authentication across multiple GitBook sites.
{% endstep %}

{% step %}
[**Configure your backend for adaptive content (optional)**](#id-5.-configure-your-backend-for-adaptive-content)

Configure your backend to work with adaptive content in GitBook.
{% endstep %}
{% endstepper %}

### 1. Create a custom backend to authenticate your users

In order to start authenticating users before they can visit your documentation, you’ll need to set up a server that can handle login and authentication of users.

Your backend should:

* Prompt users to log in using your preferred authentication method.
* Validate user credentials and authenticate them.
* Generate and sign a **JSON Web Token (JWT)** upon successful authentication.
* Redirect users to GitBook with the JWT included in the URL.

### 2. Sign and pass a JWT token to GitBook

Once your backend authenticates a user, it must **generate a JWT** and **pass it to GitBook** when **redirecting** them to your site. The token should be signed using the **private key** provided in your site's audience settings after [enabling authenticated access](https://gitbook.com/docs/publishing-documentation/enabling-authenticated-access#enable-authenticated-access).

The following example should demonstrate how a login request handler in your custom backend could look like:

{% code title="index.ts" %}

```typescript
import { Request, Response } from 'express';
import * as jose from 'jose';

import { getUserInfo } from '../services/user-info-service';
import { getFeatureFlags } from '../services/feature-flags-service';

const GITBOOK_VISITOR_SIGNING_KEY = process.env.GITBOOK_VISITOR_SIGNING_KEY!;
const GITBOOK_DOCS_URL = 'https://mycompany.gitbook.io/myspace';

export async function handleAppLoginRequest(req: Request, res: Response) {
    // Your business logic for handling the login request
    // For example, checking credentials and authenticating the user
    //
    // e.g.:
    // const loggedInUser = await authenticateUser(req.body.username, req.body.password);
    
    // Generate a signed JWT
    const gitbookVisitorJWT = await new jose.SignJWT({})
        .setProtectedHeader({ alg: 'HS256' })
        .setIssuedAt()
        .setExpirationTime('2h') // Arbitrary 2-hour expiration
        .sign(new TextEncoder().encode(GITBOOK_VISITOR_SIGNING_KEY));
    
    // Redirect the user to GitBook with the JWT token in the URL
    const redirectURL = `${GITBOOK_DOCS_URL}/?jwt_token=${gitbookVisitorJWT}`;
    res.redirect(redirectURL);
}
```

{% endcode %}

### 3. Configure a fallback URL

The fallback URL is used when an unauthenticated visitor tries to access your protected site. GitBook will then redirect them to this URL.

This URL should point to a handler in your custom backend, where you can prompt them to login, authenticate and then redirect them back to your site with the JWT included in the URL.

For instance, if your login screen is located at `https://example.com/login`, you should include this value as the fallback URL.

You can configure this fallback URL within your site’s audience settings under the "Authenticated access" tab.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FB48PEdMz1tCDf0Q0lo4d%2FScreenshot%202025-03-25%20at%2015.00.08.png?alt=media&#x26;token=e22fe867-e1f6-44f7-8b4f-a868ac620464" alt="A GitBook screenshot showing where to configure a fallback URL"><figcaption><p>Configure a fallback URL</p></figcaption></figure>

When redirecting to the fallback URL, GitBook includes a `location` query parameter to the fallback URL that you can leverage in your handler to redirect the user to the original location of the user:

```javascript
const gitbookVisitorJWT = await new jose.SignJWT({})
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('2h') // Arbitrary 2-hour expiration
    .sign(new TextEncoder().encode(GITBOOK_VISITOR_SIGNING_KEY));
    
// Redirect to the original GitBook docs URL with the JWT included as jwt_token query parameter
// If a location is provided, the user will be redirected back to their original destination
const redirectURL = `${GITBOOK_DOCS_URL}/${req.query.location || ''}?jwt_token=${gitbookVisitorJWT}`;
res.redirect(redirectURL);
```

{% hint style="warning" %}
Because GitBook relies on the `location` search param - you cannot use it in your fallback URL. For example, `https://auth.gitbook.com/?location=something` is not a valid fallback URL.
{% endhint %}

### 4. Set up multi-tenant authenticated access (optional)

If you’re using GitBook as a platform to provide content to your different customers, you probably need to set up multi-tenant authenticated access. Your authentication backend needs to be responsible for handling authentication across multiple different sites. This is possible in GitBook with a few small tweaks to your custom authentication backend code.

#### Adding all tenants to your authentication server

Your authentication backend will need to know the JWT signing keys and the URLs of all the GitBook sites you expect it to handle. If you have two sites in your organization for Customer A and Customer B, you can imagine your authentication code storing such mapping:

```typescript
const CUSTOMER_A = {
  jwtSigningKey: 'aaa-aaa-aaa-aaa',
  url: 'https://mycompany.gitbook.io/customer-a'
};

const CUSTOMER_B = {
  jwtSigningKey: 'bbb-bbb-bbb-bbb',
  url: 'https://mycompany.gitbook.io/customer-b'
};
```

#### Giving your authentication server additional context

When GitBook is unable to authenticate a user's request, it redirects them to the fallback URL. This URL points to your authentication backend, which is responsible for authenticating the user and redirecting them back to the requested content.

To support multiple tenants, your authentication backend needs to know which GitBook site the user is meant to access. This information can be passed in the fallback URL.

So for example, you could setup the fallback URLs for each sites as follow:

<table><thead><tr><th width="150.75390625">GitBook Site</th><th>Fallback URL</th></tr></thead><tbody><tr><td>Customer A site</td><td><code>https://auth-backend.acme.org/login?site=customer-a</code></td></tr><tr><td>Customer B site</td><td><code>https://auth-backend.acme.org/login?site=customer-b</code></td></tr></tbody></table>

Your authentication backend can then check this information and handle the redirection to the correct site accordingly:

```javascript
const customerInfo = req.query.site === 'customer-a' ? CUSTOMER_A : CUSTOMER_B;
  
const gitbookVisitorJWT = await new jose.SignJWT({})
    .setProtectedHeader({ alg: 'HS256' })
    .setIssuedAt()
    .setExpirationTime('2h') // Arbitrary 2-hour expiration
    .sign(new TextEncoder().encode(customerInfo.jwtSigningKey));
    
// Redirect to the original GitBook docs URL with the JWT included as jwt_token query parameter
// If a location is provided, the user will be redirected back to their original destination
const redirectURL = `${customerInfo.url}/${req.query.location || ''}?jwt_token=${gitbookVisitorJWT}`;
res.redirect(redirectURL);
```

### 5. Configure your backend for adaptive content (optional)

{% hint style="warning" %}
This feature is still under development and coming soon to the [Ultimate site plan](https://www.gitbook.com/pricing).&#x20;

Please sign up for the waitlist at <https://www.gitbook.com/#alpha-waitlist>
{% endhint %}

To leverage the Adaptive Content capability in your authenticated access setup, you can include additional user attributes (claims) in the payload of the JWT that your custom backend generates and include in the URL when redirecting the user to the site.

These claims when included in the JWT are used by GitBook to [adapt content](https://gitbook.com/docs/publishing-documentation/adaptive-content/adapting-your-content) dynamically for your site visitors.

Putting it all together, the following code example demonstrates how you could include these claims in the JWT, which can then be used by GitBook to adapt content for your visitors:

{% code title="index.ts" %}

```typescript
import { Request, Response } from 'express';
import * as jose from 'jose';

import { getUserInfo } from '../services/user-info-service';
import { getFeatureFlags } from '../services/feature-flags-service';

const GITBOOK_VISITOR_SIGNING_KEY = process.env.GITBOOK_VISITOR_SIGNING_KEY!;
const GITBOOK_DOCS_URL = 'https://mycompany.gitbook.io/myspace';

export async function handleAppLoginRequest(req: Request, res: Response) {
    // Your business logic for handling the login request
    // For example, checking credentials and authenticating the user
    //
    // e.g.:
    // const loggedInUser = await authenticateUser(req.body.username, req.body.password);
    
    // For the purpose of this example, assume a logged-in user object
    const loggedInUser = { id: '12345' }; // Replace with actual authentication logic

    // Retrieve user information to pass to GitBook
    const userInfo = await getUserInfo(loggedInUser.id);
    
    // Generate a signed JWT and include the user attributes as claims
    const gitbookVisitorClaims = {
        firstName: userInfo.firstName,
        lastName: userInfo.lastName,
        isBetaUser: userInfo.isBetaUser,
        products: userInfo.products.map((product) => product.name),
        featureFlags: await getFeatureFlags({ userId: loggedInUser.id })
    };
    
    const gitbookVisitorJWT = await new jose.SignJWT(gitbookVisitorClaims)
        .setProtectedHeader({ alg: 'HS256' })
        .setIssuedAt()
        .setExpirationTime('2h') // Arbitrary 2-hour expiration
        .sign(new TextEncoder().encode(GITBOOK_VISITOR_SIGNING_KEY));
    
    // Redirect the user to GitBook with the JWT token in the URL
    const redirectURL = `${GITBOOK_DOCS_URL}/?jwt_token=${gitbookVisitorJWT}`;
    res.redirect(redirectURL);
}
```

{% endcode %}

After setting up and configuring the right claims to send to GitBook, head to “[Adapting your content](https://gitbook.com/docs/publishing-documentation/adaptive-content/adapting-your-content)” to continue configuring your site.
