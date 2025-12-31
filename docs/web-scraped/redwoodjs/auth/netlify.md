# Source: https://docs.redwoodjs.com/docs/auth/netlify

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Authentication](/docs/authentication)
-   [Netlify]

[Version: 8.8]

<div>

# Netlify Identity Authentication

</div>

To get started, run the setup command:

``` 
yarn rw setup auth netlify
```

This installs all the packages, writes all the files, and makes all the code modifications you need. For a detailed explanation of all the api- and web-side changes that aren\'t exclusive to Netlify Identity, see the top-level [Authentication](/docs/authentication) doc. For now let\'s focus on Netlify\'s side of things.

There\'s a catch with Netlify Identity: your app has to be be deployed to Netlify to use it. If this\'s a deal breaker for you, there are [other great auth providers to choose from](/docs/authentication#official-integrations). But here we\'ll assume it\'s not and that your app is already deployed. (If it isn\'t, do that first, then come back. And yes, there\'s a setup command for that: `yarn rw setup deploy netlify`.)

Once you\'ve deployed your app, go to it\'s overview, click \"Integrations\" in the nav at the top, search for Netlify Identity, enable it, and copy the API endpoint in the Identity card. (It should look something like `https://my-redwood-app.netlify.app/.netlify/identity`.)

Let\'s do one more thing while we\'re here to make signing up later a little easier. Right now, if we sign up, we\'ll have to verify our email address. Let\'s forego that feature for the purposes of this doc: click \"Settings and usage\", then scroll down to \"Emails\" and look for \"Confirmation template\". Click \"Edit settings\", tick the box next to \"Allow users to sign up without verifying their email address\", and click \"Save\".

Netlify Identity works a little differently than the other auth providers in that you don\'t have to copy API keys to your project\'s `.env` and `redwood.toml` files. Instead, the first time you use it (by, say, calling `signUp` from `useAuth`), it\'ll ask you for your app\'s API endpoint. So let\'s go ahead and use it: if this is a brand new project, generate a home page. There we\'ll try to sign up by destructuring `signUp` from the `useAuth` hook (import that from `'src/auth'`). We\'ll also destructure and display `isAuthenticated` to see if it worked:

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

Clicking sign up should open a modal; paste the API endpoint you copied earlier there:

![image](https://user-images.githubusercontent.com/32992335/209391973-239d5a12-649f-4e33-9098-cd297034f563.png)

After that, you should see a sign-up modal. Go ahead and sign up:

![image](https://user-images.githubusercontent.com/32992335/209392156-e87a04b8-9ce8-4bc6-bc6b-92a2de8effe3.png)

After you sign up, you should see `` on the page.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/auth/netlify.md)