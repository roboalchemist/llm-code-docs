# Source: https://developers.webflow.com/designer/reference/get-user-id-token.mdx

***

title: Get user ID token
slug: designer/reference/get-user-id-token
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get user ID Token'
'og:description': >-
Retrieves an ID Token for the current user, which provides information on who
is currently using your Designer Extension.
-------------------------------------------

## `webflow.getIdToken()`

Retrieves a [JSON Web Token (JWT)](https://jwt.io) that uniquely identifies the current user of your Designer Extension. This ID token contains encoded user information that can be used for authentication and authorization purposes.

<Card
  title="Authenticating users with the Data API"
  href="/apps/docs/authenticating-users-with-id-tokens"
  icon={
        <>
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Encryption.svg" alt="" className="hidden dark:block" />
            <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Encryption.svg" alt="" className="block dark:hidden" />
        </>
    }
  iconPosition="left"
  iconSize="12"
>
  To decode and verify the token, send a POST request to the [Resolve ID Token endpoint](/data/v2.0.0-beta/reference/token/resolve). The endpoint will return the user's details, which you can use to implement permission-based features or personalized experiences in your extension.

  <br />

  <a href="/apps/docs/authenticating-users-with-id-tokens">
    <button class="cc-primary">Read the guide</button>
  </a>
</Card>

### Syntax

```typescript
webflow.getIdToken(): Promise<string>;
```

### Returns

**Promise\<*String*>**

A Promise that resolves to the value of the ID Token. The ID token will remain valid for 15 minutes.

### Example

```typescript
// Get ID Token
const idToken = await webflow.getIdToken()

// Print ID Token
console.log(idToken)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>
