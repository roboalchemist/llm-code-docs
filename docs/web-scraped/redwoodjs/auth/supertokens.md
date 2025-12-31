# Source: https://docs.redwoodjs.com/docs/auth/supertokens

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Authentication](/docs/authentication)
-   [SuperTokens]

[Version: 8.8]

On this page

<div>

# SuperTokens Authentication

</div>

To get started, run the setup command:

``` 
yarn rw setup auth supertokens
```

This installs all the packages, writes all the files, and makes all the code modifications you need.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

You may have noticed that in `api/src/functions/auth.ts` there\'s an import from `'supertokens-node/framework/awsLambda'`. This is fine, even if your app isn\'t running in a serverless environment like AWS Lambda. In \"serverful\" environments, Redwood automatically handles the translation between Fastify\'s request and reply objects and functions\' AWS Lambda signature.

For a detailed explanation of all the api- and web-side changes that aren\'t exclusive to SuperTokens, see the top-level [Authentication](/docs/authentication) doc. For now, let\'s focus on SuperTokens\'s side of things.

When you run the setup command it configures your app to support both email+password logins as well as social auth logins (Apple, GitHub and Google). Working with those social auth logins does require quite a few environment variables. And SuperTokens itself needs a couple variables too. Thankfully SuperTokens makes this very easy to setup as they provide values we can use for testing.

# Environment variables

The environment variables have to be added either to your project\'s `.env` file (when running in development environment), or to the environment variables of your hosting provider (when running in production).

## Base setup[​](#base-setup "Direct link to Base setup") 

``` 
SUPERTOKENS_APP_NAME="Redwoodjs App" # this will be used in the email template for password reset or email verification emails.
SUPERTOKENS_JWKS_URL=http://localhost:8910/.redwood/functions/auth/jwt/jwks.json
SUPERTOKENS_CONNECTION_URI=https://try.supertokens.io # set to the correct connection uri
```

## Production setup[​](#production-setup "Direct link to Production setup") 

Assuming that your web side is hosted on `https://myapp.com`:

``` 
SUPERTOKENS_WEBSITE_DOMAIN=https://myapp.com
SUPERTOKENS_JWKS_URL=https://myapp.com/.redwood/functions/auth/jwt/jwks.json
```

## Managed Supertokens service setup[​](#managed-supertokens-service-setup "Direct link to Managed Supertokens service setup") 

``` 
SUPERTOKENS_API_KEY=your-api-key # The value can be omitted when self-hosting Supertokens
```

## Social login setup[​](#social-login-setup "Direct link to Social login setup") 

The following environment variables have to be set up (depending on the social login options):

``` 
SUPERTOKENS_APPLE_CLIENT_ID=4398792-io.supertokens.example.service
SUPERTOKENS_APPLE_SECRET_KEY_ID=7M48Y4RYDL
SUPERTOKENS_APPLE_SECRET_PRIVATE_KEY=-----BEGIN PRIVATE KEY-----\nMIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgu8gXs+XYkqXD6Ala9Sf/iJXzhbwcoG5dMh1OonpdJUmgCgYIKoZIzj0DAQehRANCAASfrvlFbFCYqn3I2zeknYXLwtH30JuOKestDbSfZYxZNMqhF/OzdZFTV0zc5u5s3eN+oCWbnvl0hM+9IW0UlkdA\n-----END PRIVATE KEY-----
SUPERTOKENS_APPLE_SECRET_TEAM_ID=YWQCXGJRJL
SUPERTOKENS_GITHUB_CLIENT_ID=467101b197249757c71f
SUPERTOKENS_GITHUB_CLIENT_SECRET=e97051221f4b6426e8fe8d51486396703012f5bd
SUPERTOKENS_GOOGLE_CLIENT_ID=1060725074195-kmeum4crr01uirfl2op9kd5acmi9jutn.apps.googleusercontent.com
SUPERTOKENS_GOOGLE_CLIENT_SECRET=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
```

## `redwood.toml` setup[​](#redwoodtoml-setup "Direct link to redwoodtoml-setup") 

Make sure to modify `redwood.toml` to pass the required environment variables to the web side:

``` 
[web]
...
includeEnvironmentVariables = [
  'SUPERTOKENS_WEBSITE_DOMAIN',
  'SUPERTOKENS_API_DOMAIN',
  'SUPERTOKENS_API_GATEWAY_PATH',
  'SUPERTOKENS_APP_NAME'
]
```

# Page setup

Let\'s make sure: if this is a brand new project, generate a home page. There we\'ll try to sign up by destructuring `signUp` from the `useAuth` hook (import that from `'src/auth'`). We\'ll also destructure and display `isAuthenticated` to see if it worked:

``` 
yarn rw g page home /
```

web/src/pages/HomePage.tsx

``` 
import  from 'src/auth'

const HomePage = () =>  = useAuth()

  return (
    <>
      

      <p>)}</p>
      <button onClick=>sign up</button>
    </>
  )
}

export default HomePage
```

Clicking sign up should navigate you to `/auth` where SuperToken\'s default login/sign up UI is rendered.

![SuperTokens default UI](https://user-images.githubusercontent.com/30793/215893664-d367eb3d-566e-4541-a01a-5772d95cc9c7.png)

After you sign up, you should be redirected back to your Redwood app, and you should see `` on the page.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting") 

If going to `http://localhost:8910/auth` results in the plain Javascript file being served instead of the expected auth page, rename the `web/src/auth.tsx` file to `web/src/authentication.tsx`, and update the imports (related to [https://github.com/redwoodjs/redwood/issues/9740](https://github.com/redwoodjs/redwood/issues/9740)).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/auth/supertokens.md)