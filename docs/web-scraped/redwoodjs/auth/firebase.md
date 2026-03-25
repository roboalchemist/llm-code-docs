# Source: https://docs.redwoodjs.com/docs/auth/firebase

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Authentication](/docs/authentication)
-   [Firebase]

[Version: 8.8]

<div>

# Firebase Authentication

</div>

To get started, run the setup command:

``` 
yarn rw setup auth firebase
```

This installs all the packages, writes all the files, and makes all the code modifications you need. For a detailed explanation of all the api- and web-side changes that aren\'t exclusive to Firebase, see the top-level [Authentication](/docs/authentication) doc. For now, let\'s focus on Firebase\'s side of things.

If you don\'t have a Firebase account yet, now\'s the time to make one: navigate to [https://firebase.google.com](https://firebase.google.com) and click \"Go to console\", sign up, and create a project. After it\'s ready, we\'ll get the API keys.

To get the API keys, we need to add a web app to our project. Click the `</>` icon in main call to action on the dashboard---\"Get started by adding Firebase to your app\". Give your app a nickname, then you should see the API keys. Since we\'re only using Firebase for auth, we only need `apiKey`, `authDomain`, and `projectId`. Copy them into your project\'s `.env` file:

.env

``` 
FIREBASE_API_KEY="..."
FIREBASE_AUTH_DOMAIN="..."
FIREBASE_PROJECT_ID="..."
```

Lastly, include `FIREBASE_API_KEY` and `FIREBASE_AUTH_DOMAIN` in the list of env vars that should be available to the web side (`FIREBASE_PROJECT_ID` is for the api side):

redwood.toml

``` 
[web]
  # ...
  includeEnvironmentVariables = ["FIREBASE_API_KEY", "FIREBASE_AUTH_DOMAIN"]
```

We\'ve hooked up our Firebase app to our Redwood app, but if you try it now, it won\'t work. That\'s because we haven\'t actually enabled auth in our Firebase app yet.

Back to the dashboard one more time: in the nav on the left, click \"Build\", \"Authentication\", and \"Get started\". We\'re going to go with \"Email/Password\" here, but feel free to configure things as you wish. Click \"Email/Password\", enable it, and click \"Save\".

That should be enough; now, things should just work. Let\'s make sure: if this is a brand new project, generate a home page. There we\'ll try to sign up by destructuring `signUp` from the `useAuth` hook (import that from `'src/auth'`). We\'ll also destructure and display `isAuthenticated` to see if it worked:

web/src/pages/HomePage.tsx

``` 
import  from 'src/auth'

const HomePage = () =>  = useAuth()

  return (
    <>
      

      <p>)}</p>
      <button
        onClick=)
        }
      >
        sign up
      </button>
    </>
  )
}
```

\"Email/Password\" says what it means: Firebase doesn\'t redirect to a hosted sign-up page or open a sign-up modal. In a real app, you\'d build a form here, but we\'re going to hardcode an email and password. After you sign up, you should see `` on the page.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/auth/firebase.md)