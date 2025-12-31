# Source: https://docs.redwoodjs.com/docs/how-to/supabase-auth

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Supabase Auth]

[Version: 8.8]

On this page

<div>

# Supabase Auth

</div>

Let\'s call this how to a port of the [Redwood GoTrue Auth how to](/docs/how-to/gotrue-auth) to [Supabase](https://supabase.io/). I won\'t get original style points because I copy-pasted (and updated, for good measure) the original. Why? Because Supabase auth is based on [Netlify GoTrue](https://github.com/netlify/gotrue), an API service for handling user registration and authentication. The Supabase folks build on solid open-source foundations.

Once I connected these dots, the Redwood GoTrue Auth how to became a handy resource as I climbed the auth learning curve (and I started from sea level). Hopefully this Supabase-specific edition will help you climb your own too.

## Time to Cook[​](#time-to-cook "Direct link to Time to Cook") 

In this recipe, we\'ll:

-   Configure a Redwood app with Supabase auth
-   Create a Sign Up form, a Sign In form, and a Sign Out button
-   Add auth links that display the correct buttons based on our auth state

But first, some housekeeping\...

## Prerequisites[​](#prerequisites "Direct link to Prerequisites") 

Before getting started, there are a few steps you should complete:

-   [Create a Redwood app](/docs/tutorial/chapter1/installation)
-   [Create a Supabase account](https://www.supabase.io/)
-   [Go through the Supabase React Quick Start](https://supabase.io/docs/guides/with-react)
-   [Go through the Supabase Redwood Quick Start](https://supabase.io/docs/guides/with-redwoodjs)
-   Fire up a dev server: `yarn redwood dev`

### About the Supabase Quick Starts[​](#about-the-supabase-quick-starts "Direct link to About the Supabase Quick Starts") 

Why the React Quick Start before the Redwood? I found it helpful to first interact directly with the [Supabase Client](https://github.com/supabase/supabase-js). Eventually, you\'ll use the [Redwood Auth wrapper](/docs/authentication#supabase), which provides a level of abstraction and a clean, consistent style. But I needed a couple hours of direct client experimentation to gain comfort in the Redwood one.

So, just this once, I hereby give you permission to fire-up Create React App as you follow-along the Supabase React Quick Start. I worked through it first. Then I worked through the Supabase Redwood Quick start, observing the slight differences. This helped me understand the details that the Redwood wrapper abstracts for us.

> **Auth Alphabet Soup**
>
> If you\'re like me---and I\'m pretty sure I\'m just human---you may find yourself spinning in jumbled auth jargon. Hang in there, you\'ll get your auth ducks lined up eventually.
>
> I\'m proud to tell you that I now know that the Redwood Supabase auth client wraps the Supabase GoTrueJS client, which is a fork of Netlify's GoTrueJS client (which is different from Netlify Identity). And dbAuth is a totally separate auth option. Plus, I\'ll keep it simple and not use RBAC at the moment.
>
> Ahhh! It took me a few weeks to figure this out.

## Back to Redwood[​](#back-to-redwood "Direct link to Back to Redwood") 

Armed with some knowledge and insight from going through the Supabase Quick Starts, let\'s head back to the Redwood app created as part of the prerequisites.

Start by installing the required packages and generating boilerplate for Redwood Auth, all with this simple [CLI command](/docs/cli-commands#setup-auth):

``` 
yarn redwood setup auth supabase
```

By specifying `supabase` as the provider, Redwood automatically added the necessary Supabase config to our app. Let\'s open up `web/src/App.[js/tsx]` and inspect. You should see:

web/src/App.\[js/tsx\]

``` 
import  from '@redwoodjs/web'
import  from '@redwoodjs/web/apollo'

import FatalErrorPage from 'src/pages/FatalErrorPage'
import Routes from 'src/Routes'

import  from './auth'

import './index.css'

const App = () => (
  <FatalErrorBoundary page=>
    <RedwoodProvider titleTemplate="%PageTitle | %AppTitle">
      <AuthProvider>
        <RedwoodApolloProvider useAuth=>
          <Routes />
        </RedwoodApolloProvider>
      </AuthProvider>
    </RedwoodProvider>
  </FatalErrorBoundary>
)

export default App
```

As you can see our AuthProvider is exported from our `web/src/auth.[js/tsx]`, lets take a look at what that looks like:

web/src/auth.\[js/tsx\]

``` 
import  from '@supabase/supabase-js'

import  from '@redwoodjs/auth-supabase-web'

const supabaseClient = createClient(
  process.env.SUPABASE_URL || '',
  process.env.SUPABASE_KEY || ''
)

export const  = createAuth(supabaseClient)
```

Now it\'s time to add the Supabase URL, public API KEY, and JWT SECRET (`SUPABASE_URL`, `SUPABASE_KEY`, and `SUPABASE_JWT_SECRET`) to your `.env` file. You can find these items in your Supabase management console, under **Settings \> API**:

![Supabase console screen shot](https://user-images.githubusercontent.com/43206213/146407575-71ad2c94-8fa6-48d2-a403-d249f75569ea.png)

Here\'s a `.env` example:

``` 
# .env (in your root project directory)

SUPABASE_URL=https://replacewithyoursupabaseurl.supabase.co
SUPABASE_KEY=eyJhb_replace_VCJ9.eyJy_with_your_wfQ.0Abb_anon_key_teLJs
SUPABASE_JWT_SECRET=eyJh_replace_CJ9.eyJy_with_your_NTQwOTB9.MGNZN_JWT_secret_JgErqxj4
```

That\'s (almost) all for configuration.

## Sign Up[​](#sign-up "Direct link to Sign Up") 

Sign Up feels like an appropriate place to start building our interface. Our first iteration won\'t include features like email confirmation or password recovery. To forgo email confirmation, turn off \"Enable email confirmations\" on your Supabase management console, found under `Authentication > Settings`:

![Supabase email confirmation toggle](https://user-images.githubusercontent.com/43206213/147164458-1b6723ef-d7dd-4c7c-b228-73ca4ba7b1ff.png)

*Now* we\'re done with configuration. Back to our app\...

## The Sign Up Page[​](#the-sign-up-page "Direct link to The Sign Up Page") 

Let\'s generate a Sign Up page:

``` 
yarn redwood generate page signup
```

This adds a Sign Up [route](/docs/router) to our routes file and creates a `SignupPage` component.

In the just-generated `SignupPage` component (`web/src/pages/SignupPage/SignupPage.[js/tsx]`), let\'s import some [Redwood Form components](/docs/forms) and make a very basic form:

web/src/pages/SignupPage/SignupPage.\[js/tsx\]

``` 
import  from '@redwoodjs/forms'

const SignupPage = () => 

export default SignupPage
```

Did I mention it was basic? If you want to add some polish, you might find both the [Redwood Form docs](/docs/forms) and the [tutorial section on forms](/docs/tutorial/chapter3/forms) quite useful. For our purposes, let\'s just focus on the functionality.

Now that we have a form interface, we\'re going to want to do something when the user submits it. Let\'s add an `onSubmit` function to our component and pass it as a prop to our Form component:

web/src/pages/SignupPage/SignupPage.\[js/tsx\]

``` 
// ...

const SignupPage = () => 

  return (
    <>
      <h1>Sign Up</h1>
      <Form onSubmit=>
        <TextField name="email" placeholder="email" />
        <PasswordField name="password" placeholder="password" />
        <Submit>Sign Up</Submit>
      </Form>
    </>
  )
}

//...
```

The *something* we need to do is---surprise!---sign up. To do this, we\'ll need a way to communicate with `<AuthProvider />` and the Supabase GoTrue-JS client we passed to it. Look no further than the [`useAuth` hook](/docs/authentication#api), which lets us subscribe to our auth state and its properties. In our case, we\'ll be glad to now have access to `client` and, thusly, our Supabase GoTrue-JS instance and [all of its functions](https://github.com/supabase/supabase-js).

Let\'s import `useAuth` and destructure `client` from it in our component:

web/src/pages/SignupPage/SignupPage.js

``` 
import  from '@redwoodjs/forms'
import  from 'src/auth'

const SignupPage = () =>  = useAuth()
  const onSubmit = (data) => 

  return (
    <>
      <h1>Sign Up</h1>
      <Form onSubmit=>
        <TextField name="email" placeholder="email" />
        <PasswordField name="password" placeholder="password" />
        <Submit>Sign Up</Submit>
      </Form>
    </>
  )
}

export default SignupPage
```

And now we\'ll attempt to create a new user in the `onSubmit` function with [`client.auth.signUp()`](https://supabase.io/docs/reference/javascript/auth-signup) by passing the `email` and `password` values that we captured from our form:

web/src/pages/SignupPage/SignupPage.\[js/tsx\]

``` 
import  from '@redwoodjs/forms'
import  from 'src/auth'

const SignupPage = () =>  = useAuth()

  const onSubmit = async (data) => )
      console.log('response: ', response)
    } catch(error) 
  }

  return (
    <>
      <h1>Sign Up</h1>
      <Form onSubmit=>
        <TextField name="email" placeholder="email" />
        <PasswordField name="password" placeholder="password" />
        <Submit>Sign Up</Submit>
      </Form>
    </>
  )
}
export default SignupPage
```

Presently, our sign up works as is, but simply console-logging the response from `client.auth.signup()` is hardly useful behavior.

Let\'s display errors to the user if there are any. To do this, we\'ll set up `React.useState()` to manage our error state and conditionally render the error message. We\'ll also want to reset the error state at the beginning of every submission with `setError(null)`:

web/src/pages/SignupPage/SignupPage.js

``` 
import  from '@redwoodjs/forms'
import  from 'src/auth'

const SignupPage = () =>  = useAuth()
  const [error, setError] = React.useState(null)

  const onSubmit = async (data) => )
      console.log('response: ', response)
      response?.error?.message && setError(response.error.message)
    } catch(error) 
  }

  return (
    <>
      <h1>Sign Up</h1>
      <Form onSubmit=>
        </p>}
        <TextField name="email" placeholder="email" />
        <PasswordField name="password" placeholder="password" />
        <Submit>Sign Up</Submit>
      </Form>
    </>
  )
}
export default SignupPage
```

> Errors may be returned in two fashions:
>
> 1.  upon promise fulfillment, within the `error` property of the object returned by the promise
> 2.  upon promise rejection, within an error returned by the promise (you can handle this via the `catch` block)

Now we can handle a successful submission. If we sign up without email confirmation, then successful sign up also *signs in* the user. Once they\'ve signed in, we\'ll want to redirect them back to our app.

First, if you haven\'t already, [generate](/docs/cli-commands#generate-page) a homepage:

``` 
yarn redwood generate page home /
```

Let\'s import `routes` and `navigate` from [Redwood Router](/docs/router#navigate) and use them to redirect to the home page upon successful sign up:

web/src/pages/SignupPage/SignupPage.js

``` 
import  from '@redwoodjs/forms'
import  from 'src/auth'
import  from '@redwoodjs/router'

const SignupPage = () =>  = useAuth()
  const [error, setError] = React.useState(null)

  const onSubmit = async (data) => )
      response?.error?.message ? setError(response.error.message) : navigate(routes.home())
    } catch(error) 
  }

  return (
    <>
      <h1>Sign Up</h1>
      <Form onSubmit=>
        </p>}
        <TextField name="email" placeholder="email" />
        <PasswordField name="password" placeholder="password" />
        <Submit>Sign Up</Submit>
      </Form>
    </>
  )
}
export default SignupPage
```

Hoorah! We\'ve just added a sign up page and created a sign up form. We created a function to sign up users and we redirect users to the home page upon successful submission. Let\'s move on to Sign In.

## Sign In[​](#sign-in "Direct link to Sign In") 

Let\'s get right to it. Start by [generating](/docs/cli-commands#generate-page) a sign in page:

``` 
yarn redwood generate page signin
```

Next we\'ll add a basic form with `email` and `password` fields, some error reporting, and a hollow `onSubmit` function:

web/src/pages/SigninPage/SigninPage.\[js/tsx\]

``` 
import  from '@redwoodjs/forms'

const SigninPage = () => 

  return (
    <>
      <h1>Sign In</h1>
      <Form onSubmit=>
        </p>}
        <TextField name="email" placeholder="email" />
        <PasswordField name="password" placeholder="password" />
        <Submit>Sign In</Submit>
      </Form>
    </>
  )
}

export default SigninPage
```

Then we\'ll need to import `useAuth` from `src/auth` and destructure `logIn` so that we can use it in our `onSubmit` function:

web/src/pages/SigninPage/SigninPage.js

``` 
import  from '@redwoodjs/forms'
import  from 'src/auth'

const SigninPage = () =>  = useAuth()
  const [error, setError] = React.useState(null)

  const onSubmit = (data) => 

  return (
    <>
      <h1>Sign In</h1>
      <Form onSubmit=>
        </p>}
        <TextField name="email" placeholder="email" />
        <PasswordField name="password" placeholder="password" />
        <Submit>Sign In</Submit>
      </Form>
    </>
  )
}

export default SigninPage
```

Now we\'ll add `logIn` to our `onSubmit` function. This time we\'ll be passing an object to our function as we\'re using Redwood Auth\'s `logIn` function directly (as opposed to `client`). This object takes an email and password.

web/src/pages/SigninPage/SigninPage.js

``` 
import  from '@redwoodjs/forms'
import  from 'src/auth'

const SigninPage = () =>  = useAuth()
  const [error, setError] = React.useState(null)

  const onSubmit = async (data) => )
      // do something
    } catch(error) 
  }

  return (
    <>
      <h1>Sign In</h1>
      <Form onSubmit=>
        </p>}
        <TextField name="email" placeholder="email" />
        <PasswordField name="password" placeholder="password" />
        <Submit>Sign In</Submit>
      </Form>
    </>
  )
}

export default SigninPage
```

Let\'s redirect our user back to the home page upon a successful login.

In our `SigninPage`, import `navigate` and `routes` from [`@redwoodjs/router`](/docs/router) and add them after awaiting `logIn`:

web/src/pages/SigninPage/SigninPage.js

``` 
import  from '@redwoodjs/forms'
import  from 'src/auth'
import  from '@redwoodjs/router'

const SigninPage = () =>  = useAuth()
  const [error, setError] = React.useState(null)

  const onSubmit = async (data) => )
      response?.error?.message ? setError(response.error.message) : navigate(routes.home())
    } catch(error) 
  }

  return (
    <>
      <h1>Sign In</h1>
      <Form onSubmit=>
        </p>}
        <TextField name="email" placeholder="email" />
        <PasswordField name="password" placeholder="password" />
        <Submit>Sign In</Submit>
      </Form>
    </>
  )
}

export default SigninPage
```

Well done! We\'ve created a sign in page and form that successfully handles sign in.

> The remainder of the how to is the same as the [Netlify GoTrue Auth](/docs/how-to/gotrue-auth) version. This highlights one of the fun benefits of the Redwood Auth wrappers: code specific to a certain auth implementation scheme can live in a few specific spots, as we walked through above. Then, general Redwood Auth functions can be used elsewhere in the app.

## Sign Out[​](#sign-out "Direct link to Sign Out") 

Sign Out is by far the easiest to implement. All we need to do is call `useAuth`\'s `logOut` method.

Let\'s start by [generating a component](/docs/cli-commands#generate-component) to house our Sign Out Button:

``` 
yarn redwood generate component signoutBtn
```

In the `web/src/components/SignoutBtn/SignoutBtn.js` file we just generated, let\'s render a button and add a click handler:

web/src/components/SignoutBtn/SignoutBtn.\[js/tsx\]

``` 
const SignoutBtn = () => 
  return <button onClick=>Sign Out</button>
}

export default SignoutBtn
```

Now let\'s import `useAuth` from `src/auth`. We\'ll destructure its `logOut` method and invoke it in `onClick`:

web/src/components/SignoutBtn/SignoutBtn.\[js/tsx\]

``` 
import  from 'src/auth'

const SignoutBtn = () =>  = useAuth()

  const onClick = () => 
  return <button onClick=>Sign Out</button>
}

export default SignoutBtn
```

This works as is, but because the user may be in a restricted part of your app when they sign out, we should make sure to navigate them away from this page:

web/src/components/SignoutBtn/SignoutBtn.\[js/tsx\]

``` 
import  from 'src/auth'
import  from '@redwoodjs/router'

const SignoutBtn = () =>  = useAuth()

  const onClick = async () => 

  return <button onClick=>Sign Out</button>
}

export default SignoutBtn
```

And that\'s it for Sign Out! Err, of course, we\'re not rendering it anywhere in our app yet. In the next section, well add some navigation that conditionally renders the appropriate sign up, sign in, and sign out buttons based on our authentication state.

## Auth Links[​](#auth-links "Direct link to Auth Links") 

In this section we\'ll implement some auth-related navigation that conditionally renders the correct links and buttons based on the user\'s authentication state:

-   when the user\'s logged out, we should see **Sign Up** and **Sign In**
-   when the user\'s logged in, we should see **Log Out**

Let\'s start by [generating a navigation component](/docs/cli-commands#generate-component):

``` 
yarn redwood generate component navigation
```

This creates `web/src/components/Navigation/Navigation.js`. In that file, let\'s import [the `Link` component and the `routes` object](/docs/router#link-and-named-route-functions) from `@redwoodjs/router`. We\'ll also import [`useAuth`](/docs/authentication#api) since we\'ll need to subscribe to the auth state for our component to decide what to render:

web/src/components/Navigation/Navigation.js

``` 
import  from '@redwoodjs/router'
import  from 'src/auth'

const Navigation = () => 

export default Navigation
```

Let\'s destructure `isAuthenticated` from the `useAuth` hook and use it in some conditionals:

web/src/components/Navigation/Navigation.js

``` 
import  from '@redwoodjs/router'
import  from 'src/auth'

const Navigation = () =>  = useAuth()
  return (
    <nav>
      
    </nav>
  )
}

export default Navigation
```

Because Redwood Auth uses [React\'s Context API](https://reactjs.org/docs/context.html) to manage and broadcast the auth state, we can be confident that `isAuthenticated` will always be up-to-date, even if it changes from within another component in the tree (so long as it\'s a child of `<AuthProvider />`). In our case, when `isAuthenticated` changes, React will auto-magically take care of rendering the appropriate components.

Now let\'s import our sign out button and add it, as well as sign in and sign up links, to the appropriate blocks in the conditional:

web/src/components/Navigation/Navigation.\[js/tsx\]

``` 
import  from '@redwoodjs/router'
import  from 'src/auth'
import SignoutBtn from 'src/components/SignoutBtn/SignoutBtn'

const Navigation = () =>  = useAuth()
  return (
    <nav>
      >Sign Up</Link>
          <Link to=>Sign In</Link>
        </>
      )}
    </nav>
  )
}

export default Navigation
```

We have a working navigation component, but we still need to render it somewhere. Let\'s [generate a layout](/docs/cli-commands#generate-layout) called GlobalLayout:

``` 
yarn redwood generate layout global
```

Then import and render the navigation component in the newly-generated `web/src/layouts/GlobalLayout/GlobalLayout`:

web/src/layouts/GlobalLayout/GlobalLayout.js

``` 
import Navigation from 'src/components/Navigation/Navigation'

const GlobalLayout = () => </main>
    </>
  )
}

export default GlobalLayout
```

Finally, we\'ll wrap each of our generated pages in this `GlobalLayout` component. To do this efficiently, we\'ll update the routes defined in our `web\src\Routes.[js/tsx]` file with the [`Set` component](/docs/router#sets-of-routes):

web/src/Routes.\[js/tsx\]

``` 
import  from '@redwoodjs/router'
import GlobalLayout from 'src/layouts/GlobalLayout/GlobalLayout'

const Routes = () => >
        <Route path="/" page= name="home" />
        <Route path="/signup" page= name="signup" />
        <Route path="/signin" page= name="signin" />
      </Set>
      <Route notfound page= />
    </Router>
  )
}

export default Routes
```

Now we have navigation that renders the correct links and buttons based on our auth state. When the user signs in, they\'ll see a **Sign Out** button. When the user signs out, they\'ll see **Sign Up** and **Sign In** links.

## Wrapping Up[​](#wrapping-up "Direct link to Wrapping Up") 

We\'ve configured Supabase GoTrue Auth with Redwood Auth, created a Sign Up page, a Sign In page, and a Sign Out button, and added auth links to our layout. Nicely done!

As you continue refining your app, the following resources may come in handy:

-   [Redwood Supabase Auth Installation & Setup](/docs/authentication#supabase)
-   [Redwood Auth Playground](https://redwood-playground-auth.netlify.app/supabase)
-   [Redwood Supabase Auth Client Implementation](https://github.com/redwoodjs/redwood/blob/main/packages/auth/src/authClients/supabase.ts)
-   [Supabase GoTrue client implementation](https://github.com/supabase/gotrue-js/blob/d7b334a4283027c65814aa81715ffead262f0bfa/src/GoTrueClient.ts)

Finally, keep the following features in mind (future how to\'s could go deep into any of these):

-   Authentication state changes can be observed via an event listener. The [Supabase Auth playground](https://github.com/redwoodjs/playground-auth/blob/main/web/src/lib/code-samples/supabase.md) shows an example.
-   Authentication options include\...
    -   Passwordless (enter email and get a magic confirmation link)
    -   Third party (via GitHub, Google, etc)
    -   Phone one-time password
    -   Sign in with refresh token (JWTs are a critical part of the auth implementation)

Thanks for tuning in!

> If you spot an error or have trouble completing any part of this recipe, please feel free to open an issue on [Github](https://github.com/redwoodjs/redwoodjs.com) or create a topic on our [community forum](https://community.redwoodjs.com/).

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/supabase-auth.md)