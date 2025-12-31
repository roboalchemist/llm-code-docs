# Source: https://docs.redwoodjs.com/docs/auth/auth0

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Authentication](/docs/authentication)
-   [Auth0]

[Version: 8.8]

<div>

# Auth0 Authentication

</div>

To get started, run the setup command:

``` 
yarn rw setup auth auth0
```

This installs all the packages, writes all the files, and makes all the code modifications you need. For a detailed explanation of all the api- and web-side changes that aren\'t exclusive to Auth0, see the top-level [Authentication](/docs/authentication) doc. For now, let\'s focus on Auth0\'s side of things.

If you don\'t have an Auth0 account yet, now\'s the time to make one: navigate to [https://auth0.com](https://auth0.com) and sign up, then create an application. When it asks you to choose an application type, choose SPA (single-page application). Don\'t bother with the the quick start---just click the \"Settings\" tab. We\'ll get some of our application\'s API keys here.

You should see two of the four API keys we need right away: \"Domain\" and \"Client ID\". Copy those over to your project\'s `.env` file as `AUTH0_DOMAIN` and `AUTH0_CLIENT_ID` respectively.

There\'s one more on this page; scroll down to \"Application URIs\" and look for \"Allowed Callback URLs\". With Auth0, when you log in or sign up, it\'ll redirect you to Auth0\'s hosted log-in or sign-up page, then back to your Redwood app. But where in your Redwood app exactly? Auth0 needs to know, and this setting tells it.

We\'ll keep things simple for now and make it \"[http://localhost:8910](http://localhost:8910)\", but feel free to configure it as you wish. Paste \"[http://localhost:8910](http://localhost:8910)\" in the text areas below \"Allowed Callback URLs\", \"Allowed Logout URLs\" and \"Allowed Web Origins\" then click \"Save Changes\" at the bottom of the page. Copy this one over to your project\'s `.env` file too, as `AUTH0_REDIRECT_URI`.

Ok, just one more to go: under \"Applications\" in the nav on the left, click \"APIs\". There should be one there already. We don\'t need to click into it; next to it\'s name (\"Auth0 Management API\" maybe) Auth0 thoughtfully shows what we need, the \"API Audience\". Copy it into your project\'s `.env` file as `AUTH0_AUDIENCE`. All together now:

.env

``` 
AUTH0_DOMAIN="..."
AUTH0_CLIENT_ID="..."
AUTH0_REDIRECT_URI="http://localhost:8910"
AUTH0_AUDIENCE="..."
```

Lastly, include all these env vars in the list of env vars that should be available to the web side in `redwood.toml`:

redwood.toml

``` 
[web]
  # ...
  includeEnvironmentVariables = [
    "AUTH0_DOMAIN",
    "AUTH0_CLIENT_ID",
    "AUTH0_REDIRECT_URI",
    "AUTH0_AUDIENCE",
  ]
```

That should be enough; now, things should just work. Let\'s make sure: if this is a brand new project, generate a home page. There we\'ll try to sign up by destructuring `signUp` from the `useAuth` hook (import that from `'src/auth'`). We\'ll also destructure and display `isAuthenticated` to see if it worked:

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
```

Clicking sign up should redirect you to Auth0:

![image](https://user-images.githubusercontent.com/32992335/209001246-244db949-31f8-42ff-804e-18f3e423ce89.png)

After you sign up, you should be redirected back to your Redwood app, and you should see `` on the page.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/auth/auth0.md)