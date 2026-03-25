# Source: https://docs.xano.com/building-backend-features/user-authentication-and-user-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# User Auth & Data

## **Enable Authentication for a Table**

Authentication starts with enabling the function on a table that contains user data. Typically, this would just be your `user` table. You can also enable authentication on multiple tables if you want separate authentication methods for different user groups, such as normal users and administrators.

<Steps>
  <Step title="Click the ⋮ icon in the database table view and choose Settings.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/00310e7c-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=3c1aeca634f40881ee5428e18f93d019" width="20" height="29" data-path="images/00310e7c-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Use the dropdown to enable authentication.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e4a4cbe6-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=96aa4b5f2cd2ed44e4ed7c447ea3cd05" width="500" height="203" data-path="images/e4a4cbe6-image.jpeg" />
    </Frame>
  </Step>
</Steps>

## **Enable Authentication on an API Request**

Once you've enabled authentication on a table, you can use each API endpoint's settings to note whether or not it requires authentication.

When a request is sent to API endpoints that require authentication, an authorization token is sent in the headers of the request, which Xano checks against the table with authentication enabled, before allowing the request to continue.

<Info>
  Still need a primer on the basics of an API? Read more
  [here](/before-you-begin/key-concepts#api).
</Info>

<Steps>
  <Step title="Click … to access the settings of the API you'd like to enable authentication on.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7c32cc03-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=4e9df2ddd3b55b0dfa63d13461886f8e" width="34" height="25" data-path="images/7c32cc03-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Enable authentication for the endpoint in the dropdown.">
    This dropdown will list each table that you have authentication enabled on. Select the table you enabled authentication on.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d2205635-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=4877d4b13210be317275f4313db690c7" width="448" height="149" data-path="images/d2205635-image.jpeg" />
    </Frame>

    Once an API has authentication enabled, it will require an authentication token to be sent in the headers of the request.
  </Step>
</Steps>

## How does authentication work?

Authentication in Xano is powered by industry-standard JWE (JSON Web Encryption) tokens.

Once a token is generated (after login or signup), your app or website will send that token back to Xano for requests that require authentication.

A token is generated using the [**Create Authentication Token**](/the-function-stack/functions/security#create-authentication-token) function, and is typically used in conjunction with a standard login or signup authentication flow.

## Adding Pre-built Authentication Endpoints

<Steps>
  <Step title="Create an API group to hold your authentication endpoints." />

  <Step title="Click '+ Add API Endpoint' and choose Authentication to pick from the pre-built API endpoints.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/534220cf-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=e5e2c2ea833274e65a05db2acf07c49e" width="172" height="45" data-path="images/534220cf-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Choose the API that you'd like to add.">
    * **Login**

      * Accepts an email or username and password, and allows a user to log in

    * **Signup**

      * Accepts user information and creates an account for them

    * **auth/me**

      * Checks an authentication token and returns user information
  </Step>
</Steps>

## Building Sign-up and Login APIs

Below, you can review a **typical** login and signup flow — you are free to modify them to suit your needs. These are the same that Xano can add for you during signup

### Login

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/-vy8_DWVOwkWo8Bt/images/80b400d2-image.jpeg?fit=max&auto=format&n=-vy8_DWVOwkWo8Bt&q=85&s=470964dcbf23216127b0e0da0f6d3fee" width="1208" height="838" data-path="images/80b400d2-image.jpeg" />
</Frame>

<Steps>
  <Step title="Get Record From user">
    First, we need to retrieve the record of the user trying to login.
  </Step>

  <Step title="Precondition: user ≠ null">
    We use a precondition step to check if a user record was returned in step 1.
    If it wasn't, we return an error and halt execution.
  </Step>

  <Step title="Validate Password">
    Because passwords stored in a Xano database are hashed and not human
    readable, we use a Validate Password function to check what the user has
    submitted against the password stored in the database. This function returns
    a `true` or `false` depending on the result.
  </Step>

  <Step title="Precondition: pass_result = true">
    We use another precondition step to check if the password was successfully
    validated. If not, we return an error and halt execution.
  </Step>

  <Step title="Create Authentication Token">
    Finally, all checks are passed, and we create and return the authentication
    token.
  </Step>
</Steps>

### Signup

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/pz6e9Ndbn8i3u8Zz/images/6233c5a8-image.jpeg?fit=max&auto=format&n=pz6e9Ndbn8i3u8Zz&q=85&s=1302682d7c6b2e5a1a7a68454d649f12" width="1205" height="794" data-path="images/6233c5a8-image.jpeg" />
</Frame>

<Steps>
  <Step title="Get Record From user">
    Checks if a user record already exists with the provided information.
  </Step>

  <Step title="Precondition: user = null">
    Checks to see if there is a user record returned in step 1. If so, we halt
    execution and return an error
  </Step>

  <Step title="Add Record In user">
    Add a new record for the user in the `user` table
  </Step>

  <Step title="Create Authentication Token">
    Creates an authentication token to be used in future API requests.
  </Step>
</Steps>

## Extras

The extras payload is an optional setting that allows you to store additional information securely inside the token, such as a user role or other additional information.

<Info>
  When testing endpoints with authentication enabled, the quick token generator
  will not include extras or any other customization present in your login or
  signup endpoints.
</Info>

## Refresh Tokens

Refresh tokens are like spare keys for your online accounts. When a user logs in, they are issued an authentication token. This token eventually expires for security reasons, assuming you've specified an expiry time in your Create Authentication Token functions.

Once this token expires, additional user requests will fail and your frontend would probably redirect them back to the login screen. You can utilize refresh tokens to avoid having your users log in again, while maintaining the shorter expiry that is standard for an authentication token. It's a dance of logic between your backend and frontend to make this work as expected.

Below, you'll find a flowchart that details this process, and an interactive tutorial for how to add refresh token support to your Xano backend.

<Frame>
  <iframe src="https://demo.arcade.software/R4QKSn4i8piWp5ZSIcar?embed&embed_mobile=tab&embed_desktop=inline&show_copy_link=true" title="Adding Refresh Token Support in Xano" frameborder="0" loading="lazy" webkitallowfullscreen mozallowfullscreen allowfullscreen allow="clipboard-write" />
</Frame>

<br />

```mermaid  theme={null}

flowchart TD
    A[User Login] --> B{Valid Credentials?}
    B -->|No| C[Login Failed]
    B -->|Yes| D[Backend Generates Access Token and Refresh Token]
    D --> E[Frontend Stores Both Tokens]

    E --> F[User Makes API Request]
    F --> G[Frontend Sends Access Token]
    G --> H{Auth Token Close to Expiring?}



    H -->|Yes| K[Need New Auth Token]
   H -->|No| I[API Request Successful]
    I --> J[Continue Using App]
    J --> F

    K --> M[Frontend Sends Refresh Token to /refresh Endpoint]
    M --> N{Refresh Token Valid?}

    N -->|No - Expired| O[Redirect to Login]
    O --> A
    N -->|Yes| D





    style D fill:#e1f5fe
    style K fill:#ffebee
    style O fill:#ffebee

```

## Additional Notes

#### Alternative Authentication Headers

If you need to provide a secondary authentication header that takes precedence over the original Xano authentication, you can do so by sending the \*\*X-Xano-Authorization-Only \*\*header along with your requests. This will allow you to move the Xano authentication token to its own header, keeping the original standard **Authorization** header for something else.

You would want to utilize the **X-Xano-Authorization-Only** header if you are sending requests to your Xano APIs from another source that uses the \*\*Authorization \*\*header key for something else on both public and authentication required endpoints that are using the **Authorization** header for something other than Xano authentication.

**Example:**

```sh {1-2} theme={null}
// For a public Xano endpoint that sends an Authorization header
curl "http://localhost:9999/api:elnQNVvy:v1/public_test" \
-H "X-Xano-Authorization-Only: true"

// For a private (authenticated) Xano endpoint that receives an Authorization header
that is not a Xano auth token
curl "http://localhost:9999/api:elnQNVvy:v1/private_test" \
-H "X-Xano-Authorization: Bearer ey...." \
-H "X-Xano-Authorization-Only: true"
```


Built with [Mintlify](https://mintlify.com).