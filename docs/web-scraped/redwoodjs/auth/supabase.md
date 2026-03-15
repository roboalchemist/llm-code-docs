# Source: https://docs.redwoodjs.com/docs/auth/supabase

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Authentication](/docs/authentication)
-   [Supabase]

[Version: 8.8]

On this page

<div>

# Supabase Authentication

</div>

To get started, run the setup command:

``` 
yarn rw setup auth supabase
```

This installs all the packages, writes all the files, and makes all the code modifications you need. For a detailed explanation of all the api- and web-side changes that aren\'t exclusive to Supabase, see the top-level [Authentication](/docs/authentication) doc. For now, let\'s focus on Supabase\'s side of things.

## Setup[​](#setup "Direct link to Setup") 

If you don\'t have a Supabase account yet, now\'s the time to make one: navigate to [https://supabase.com](https://supabase.com) and click \"Start your project\" in the top right. Then sign up and create an organization and a project.

While Supabase creates your project, it thoughtfully shows your project\'s API keys. (If the page refreshes while you\'re copying them over, just scroll down a bit and look for \"Connecting to your new project\".) We\'re looking for \"Project URL\" and \"API key\" (the `anon`, `public` one). Copy them into your project\'s `.env` file as `SUPABASE_URL` and `SUPABASE_KEY` respectively.

There\'s one more we need, the \"JWT Secret\", that\'s not here. To get that one, click the cog icon (\"Project Settings\") near the bottom of the nav on the left. Then click \"API\", scroll down a bit, and you should see it---\"JWT Secret\" under \"JWT Settings\". Copy it into your project\'s `.env` file as `SUPABASE_JWT_SECRET`. All together now:

.env

``` 
SUPABASE_URL="..."
SUPABASE_KEY="..."
SUPABASE_JWT_SECRET="..."
```

Lastly, in `redwood.toml`, include `SUPABASE_URL` and `SUPABASE_KEY` in the list of env vars that should be available to the web side:

redwood.toml

``` 
[web]
  # ...
  includeEnvironmentVariables = ["SUPABASE_URL", "SUPABASE_KEY"]
```

## Authentication UI[​](#authentication-ui "Direct link to Authentication UI") 

Supabase doesn\'t redirect to a hosted sign-up page or open a sign-up modal. In a real app, you\'d build a form here, but we\'re going to hardcode an email and password.

### Basic Example[​](#basic-example "Direct link to Basic Example") 

After you sign up, head to your inbox: there should be a confirmation email from Supabase waiting for you.

Click the link, then head back to your app. Once you refresh the page, you should see `` on the page.

Let\'s make sure: if this is a brand new project, generate a home page.

There we\'ll try to sign up by destructuring `signUp` from the `useAuth` hook (import that from `'src/auth'`). We\'ll also destructure and display `isAuthenticated` to see if it worked:

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

## Authentication Reference[​](#authentication-reference "Direct link to Authentication Reference") 

You will notice that [Supabase Javascript SDK Auth API](https://supabase.com/docs/reference/javascript/auth-api) reference documentation presents methods to sign in with the various integrations Supabase supports: password, OAuth, IDToken, SSO, etc.

The RedwoodJS implementation of Supabase authentication supports these as well, but within the `logIn` method of the `useAuth` hook.

That means that you will see that Supabase documents sign in with email password as:

``` 
const  = await supabase.auth.signInWithPassword()
```

In RedwoodJS, you will always use `logIn` and pass the necessary credential options and also an `authMethod` to declare how you want to authenticate.

``` 
const  = useAuth()

await logIn()
```

### Sign Up with email and password[​](#sign-up-with-email-and-password "Direct link to Sign Up with email and password") 

Creates a new user.

``` 
const  = useAuth()

await signUp()
```

### Sign Up with email and password and additional user metadata[​](#sign-up-with-email-and-password-and-additional-user-metadata "Direct link to Sign Up with email and password and additional user metadata") 

Creates a new user with additional user metadata.

``` 
const  = useAuth()

await signUp(,
  },
})
```

### Sign Up with email and password and a redirect URL[​](#sign-up-with-email-and-password-and-a-redirect-url "Direct link to Sign Up with email and password and a redirect URL") 

Creates a new user with a redirect URL.

``` 
const  = useAuth()

await signUp(,
})
```

### Sign in a user with email and password[​](#sign-in-a-user-with-email-and-password "Direct link to Sign in a user with email and password") 

Log in an existing user with an email and password or phone and password.

-   Requires either an email and password or a phone number and password.

``` 
const  = useAuth()

await logIn()
```

### Sign in a user through Passwordless/OTP[​](#sign-in-a-user-through-passwordlessotp "Direct link to Sign in a user through Passwordless/OTP") 

Log in a user using magiclink or a one-time password (OTP).

-   Requires either an email or phone number.

-   This method is used for passwordless sign-ins where a OTP is sent to the user\'s email or phone number.

``` 
const  = useAuth()

await logIn(,
})
```

### Sign in a user through OAuth[​](#sign-in-a-user-through-oauth "Direct link to Sign in a user through OAuth") 

Log in an existing user via a third-party provider.

-   This method is used for signing in using a third-party provider.

-   Supabase supports many different [third-party providers](https://supabase.com/docs/guides/auth#providers).

``` 
const  = useAuth()

await logIn()
```

### Sign in a user with IDToken[​](#sign-in-a-user-with-idtoken "Direct link to Sign in a user with IDToken") 

Log in a user using IDToken.

``` 
const  = useAuth()

await logIn()
```

### Sign in a user with SSO[​](#sign-in-a-user-with-sso "Direct link to Sign in a user with SSO") 

Log in a user using IDToken.

``` 
const  = useAuth()

await logIn()
```

### Get Current User[​](#get-current-user "Direct link to Get Current User") 

Gets the content of the current user set by API side authentication.

``` 
const  = useAuth()

<p>)}</p>
```

### Get Current User Metadata[​](#get-current-user-metadata "Direct link to Get Current User Metadata") 

Gets content of the current Supabase user session, i.e., `auth.getSession()`.

``` 
const  = useAuth()

<p>)}</p>
```

### Sign out a user[​](#sign-out-a-user "Direct link to Sign out a user") 

Inside a browser context, signOut() will remove the logged in user from the browser session and log them out - removing all items from localStorage and then trigger a \"SIGNED_OUT\" event.

In order to use the signOut() method, the user needs to be signed in first.

``` 
const  = useAuth()

logOut()
```

### Verify and log in through OTP[​](#verify-and-log-in-through-otp "Direct link to Verify and log in through OTP") 

Log in a user given a User supplied OTP received via mobile.

-   The verifyOtp method takes in different verification types. If a phone number is used, the type can either be sms or phone_change. If an email address is used, the type can be one of the following: signup, magiclink, recovery, invite or email_change.

-   The verification type used should be determined based on the corresponding auth method called before verifyOtp to sign up / sign-in a user.

The RedwoodJS auth provider doesn\'t expose the `veriftyOtp` method from the Supabase SDK directly.

Instead, since you always have access the the Supabase Auth client, you can access any method it exposes.

So, in order to use the `verifyOtp` method, you would:

``` 
const  = useAuth()

useEffect(() =>  = await client.verifyOtp()
}, [client])
```

### Access the Supabase Auth Client[​](#access-the-supabase-auth-client "Direct link to Access the Supabase Auth Client") 

Sometimes you may need to access the Supabase Auth client directly.

``` 
const  = useAuth()
```

You can then use it to work with Supabase sessions, or auth events.

When using in a React component, you\'ll have to put any method that needs an `await` in a `useEffect()`.

### Retrieve a session[​](#retrieve-a-session "Direct link to Retrieve a session") 

Returns the session, refreshing it if necessary. The session returned can be null if the session is not detected which can happen in the event a user is not signed-in or has logged out.

``` 
const  = useAuth()

useEffect(() =>  = await client.getSession()
}, [client])
```

### Listen to auth events[​](#listen-to-auth-events "Direct link to Listen to auth events") 

Receive a notification every time an auth event happens.

-   Types of auth events: `SIGNED_IN`, `SIGNED_OUT`, `TOKEN_REFRESHED`, `USER_UPDATED`, `PASSWORD_RECOVERY`

``` 
const  = useAuth()

useEffect(() => ,
  } = client.onAuthStateChange((event, session) => )

  return () => 
}, [client])
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/auth/supabase.md)