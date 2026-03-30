# Source: https://docs.redwoodjs.com/docs/how-to/oauth

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [OAuth]

[Version: 8.8]

On this page

<div>

# OAuth

</div>

If you\'re using an auth provider like [Auth0](/docs/auth/auth0), OAuth login to third party services (GitHub, Google, Facebook) is usually just a setting you can toggle on in your provider\'s dashboard. But if you\'re using [dbAuth](/docs/auth/dbauth) you\'ll only have username/password login to start. But, adding one or more OAuth clients isn\'t hard. This recipe will walk you through it from scratch, adding OAuth login via GitHub.

Alternatively, consider using the [redwoodjs-dbauth-oauth](https://github.com/spoonjoy/redwoodjs-dbauth-oauth) community package. This package streamlines the setup, includes support for multiple providers, and even includes UI components that you can use for making setup even easier.

If you do prefer to set this up manually or are just curious how OAuth and dbAuth can work together, read on!

## Prerequisites[​](#prerequisites "Direct link to Prerequisites") 

This article assumes you have an app set up and are using dbAuth. We\'re going to make use of the dbAuth system to validate that you\'re who you say you are. If you just want to try this code out in a sandbox app, you can create a test blog app from scratch by checking out the [Redwood codebase](https://github.com/redwoodjs/redwood) itself and then running a couple of commands:

``` 
yarn install
yarn build

# typescript
yarn run build:test-project ~/oauth-app

# javascript
yarn run build:test-project ~/oauth-app --javascript
```

That will create a simple blog application at `~/oauth-app`. You\'ll get a login and signup page, which we\'re going to enhance to include a **Login with GitHub** button.

Speaking of GitHub, you\'ll also need a GitHub account so you can create an [OAuth app](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app).

We also assume you\'re familiar with the basics of OAuth and the terminology surrounding it.

## Login Flow[​](#login-flow "Direct link to Login Flow") 

Here\'s the logic flow we\'re going to implement:

1.  User comes to the login page and clicks a **Login with GitHub** button/link.
2.  The link directs the browser to GitHub\'s OAuth process at github.com.
3.  The user logs in with their GitHub credentials and approves our app.
4.  The browser is redirected back to our app, to a new function `/api/src/functions/oauth/oauth.js`.
5.  The function fetches the OAuth **access_token** with a call to GitHub, using the **code** that was included with the redirect from GitHub in the previous step.
6.  When the **access_token** is received, the function then requests the user data from GitHub via another fetch to GitHub\'s API.
7.  The function then checks our database for a user identified by GitHub\'s `id`. If no user is found, the `User` record is created using the info from the fetch in the previous step.
8.  The user data from our own database is used to create the same cookie that dbAuth creates on a successful login.
9.  The browser is redirected back to our site, and the user is now logged in.

## GitHub OAuth App Setup[​](#github-oauth-app-setup "Direct link to GitHub OAuth App Setup") 

In order to allow OAuth login with GitHub, we need to create an OAuth App. The instructions below are for creating one on your personal GitHub account, but if your app lives in a separate organization then you can perform the same steps under the org instead.

First go to your [Settings](https://github.com/settings/profile) and then the [Developer settings](https://github.com/settings/apps) at the bottom left. Finally, click the [OAuth Apps](https://github.com/settings/developers) nav item at left:

![OAuth app settings screenshot](https://user-images.githubusercontent.com/300/245297416-34821cb6-ace0-4a6a-9bf6-4e434d3cefc5.png)

Click [**New OAuth App**](https://github.com/settings/applications/new) and fill it in something like this:

![New OAuth app settings](https://user-images.githubusercontent.com/300/245298106-b35a6abe-6e8c-4ab1-8ab5-7b7e1dcc0a39.png)

The important part is the **Authorization callback URL** which is where GitHub will redirect you back once authenticated (step 4 of the login flow above). This callback URL assumes you\'re using the default function location of `/.redwood/functions`. If you\'ve changed that in your app be sure to change it here as well.

Click **Register application** and then on the screen that follows, click the **Generate a new client secret** button:

![New client secret button](https://user-images.githubusercontent.com/300/245298639-6e08a201-b0db-4df6-975f-592544bdced7.png)

You may be asked to use your 2FA code to verify that you\'re who you say you are, but eventually you should see your new **Client secret**. Copy that, and the **Client ID** above it:

![Client secret](https://user-images.githubusercontent.com/300/245298897-129b5d00-3bed-4d7e-a40e-f4c9cda8a21f.png)

Add those to your app\'s `.env` file (or wherever you\'re managing your secrets). Note that it\'s best to have a different OAuth app on GitHub for each environment you deploy to. Consider this one the **dev** app, and you\'ll create a separate one with a different client ID and secret when you\'re ready to deploy to production:

/.env

``` 
GITHUB_OAUTH_CLIENT_ID=41a08ae238b5aee4121d
GITHUB_OAUTH_CLIENT_SECRET=92e8662e9c562aca8356d45562911542d89450e1
```

We also need to denote what data we want permission to read from GitHub once someone authorizes our app. We\'ll want the user\'s public info, and probably their email address. That\'s only two scopes, and we can add those as another ENV var:

/.env

``` 
GITHUB_OAUTH_CLIENT_ID=41a08ae238b5aee4121d
GITHUB_OAUTH_CLIENT_SECRET=92e8662e9c562aca8356d45562911542d89450e1
GITHUB_OAUTH_SCOPES="read:user user:email"
```

If you wanted access to more GitHub data, you can specify [additional scopes](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) here and they\'ll be listed to the user when they go to authorize your app. You can also change this list in the future, but you\'ll need to log the user out and the next time they click **Login with GitHub** they\'ll be asked to authorize your app again, with a new list of requested scopes.

One more ENV var, this is the same callback URL we told GitHub about. This is used in the link in the **Login with GitHub** button and gives GitHub another chance to verify that you\'re who you say you are: you\'re proving that you know where you\'re supposed to redirect back to:

/.env

``` 
GITHUB_OAUTH_CLIENT_ID=41a08ae238b5aee4121d
GITHUB_OAUTH_CLIENT_SECRET=92e8662e9c562aca8356d45562911542d89450e1
GITHUB_OAUTH_SCOPES="read:user user:email"
GITHUB_OAUTH_REDIRECT_URI="http://localhost:8910/.redwood/functions/oauth/callback"
```

## The Login Button[​](#the-login-button "Direct link to The Login Button") 

This part is pretty easy, we\'re just going to add a link/button to go directly to GitHub to begin the OAuth process:

/web/src/pages/LoginPage/LoginPage.jsx

``` 
<a href=&redirect_uri=$&scope=$`}
  className="mx-auto block w-48 rounded bg-gray-800 px-4 py-2 text-center text-xs font-semibold uppercase tracking-wide text-white">
  Login with GitHub
</a>
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

This example uses Tailwind to style the link to match the rest of the default dbAuth login page

You can put this same link on your signup page as well, since using the OAuth flow will be dual-purpose: it will log the user in if a local user already exists, or it will create the user and then log them in.

We\'re using several of our new ENV vars here, and need to tell Redwood to make them available to the web side during the build process. Add them to the `includeEnvironmentVariables` key in `redwood.toml`:

/redwood.toml

``` 
[web]
  title = "Redwood App"
  port = "$"
  apiUrl = "/.redwood/functions"
  includeEnvironmentVariables = ["GITHUB_OAUTH_CLIENT_ID", "GITHUB_OAUTH_REDIRECT_URI", "GITHUB_OAUTH_SCOPES"]
[api]
  port = "$"
[browser]
  open = true
[notifications]
  versionUpdates = ["latest"]
```

Restart your dev server to pick up the new TOML settings, and your link should appear:

![Login button](https://user-images.githubusercontent.com/300/245899085-0b946a14-cd7c-402a-9d86-b6527fd89c7f.png)

Go ahead and click it, and you should be taken to GitHub to authorize your GitHub login to work with your app. You\'ll see the scopes we requested listed under the **Personal User Data** heading:

![GitHub Oauth Access Page](https://user-images.githubusercontent.com/300/245899872-8ddd7e69-dbfa-4544-ab6f-78fd4ff02da8.png)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

If you get an error here that says \"The redirect_uri MUST match the registered callback URL for this application\" verify that the redirect URL you entered on GitHub and the one you put into the `GITHUB_OAUTH_REDIRECT_URL` ENV var are identical!

Click **authorize** and you should end up seeing some JSON, and an error:

![/oauth function not found](https://user-images.githubusercontent.com/300/245900327-b21a178e-5539-4c6d-a5d6-9bb736100940.png)

That\'s coming from our app because we haven\'t created the `oauth` function that GitHub redirects to. But you\'ll see a `code` in the URL, which means GitHub is happy with our flow so far. Now we need to trade that `code` for an `access_token`. We\'ll do that in our `/oauth` function.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

This nicely formatted JSON comes from the [JSON Viewer](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh) Chrome extension.

## The `/oauth` Function[​](#the-oauth-function "Direct link to the-oauth-function") 

We can have Redwood generate a shell of our new function for us:

``` 
yarn rw g function oauth
```

That will create the function at `/api/src/functions/oauth/oauth.js`. If we retry the **Login with GitHub** button now, we\'ll see the output of that function instead of the error:

![Oauth function responding](https://user-images.githubusercontent.com/300/245903068-760596fa-4139-4d11-b3b3-a90edfbbf496.png)

Now let\'s start filling out this function with the code we need to get the `access_token`.

### Fetching the `access_token`[​](#fetching-the-access_token "Direct link to fetching-the-access_token") 

We told GitHub to redirect to `/oauth/callback` which *appears* like it would be a subdirectory, or child route of our `oauth` function, but in reality everything after `/oauth` just gets shoved into an `event.path` variable that we\'ll need to inspect to make sure it has the proper parts (like `/callback`). We can do that in the `hander()`:

/api/src/functions/oauth/oauth.js

``` 
export const handler = async (event, _context) => 
  }
}

const callback = async (event) => 
}
```

The `callback()` function is where we\'ll actually define the rest of our flow. We can verify this is working by trying a couple of different URLs in the browser and see that `/oauth/callback` returns a 200 and \"ok\" in the body of the page, but anything else returns a 404.

Now we need to make a request to GitHub to trade the `code` for an `access_token`. This is handled by a `fetch`:

/api/src/functions/oauth/oauth.js

``` 
const callback = async (event) =>  = event.queryStringParameters

  const response = await fetch(`https://github.com/login/oauth/access_token`, ,
    body: JSON.stringify(),
  })

  const  = JSON.parse(await response.text())

  if (error) 
  }

  return ),
  }
}
```

First we get the `code` out of the query string variables, then make a POST `fetch()` to GitHub, setting the required JSON body to include several of the ENV vars we\'ve set, as well as the `code` we got from the GitHub redirect. Then we parse the response JSON and just return it in the browser to make sure it worked. If something went wrong (`error` is not `undefined`) then we\'ll output the error message in the body of the page.

Let\'s try it: go back to the login page, click the **Login with GitHub** button and see what happens:

![GitHub OAuth access_token granted](https://user-images.githubusercontent.com/300/245906529-d08f9d6e-4947-4d14-9377-def3645d9c68.png)

You can also verify that the error response works by, for example, removing the `code` key from the `fetch()`, and see GitHub complain:

![GitHub OAuth error](https://user-images.githubusercontent.com/300/245906827-703a4a21-b279-428c-be1c-b73c559a72b3.png)

Great, GitHub has authorized us and now we can get details about the actual user from GitHub.

### Retrieving GitHub User Details[​](#retrieving-github-user-details "Direct link to Retrieving GitHub User Details") 

We need some unique identifier to tie a user in GitHub to a user in our database. The `access_token` we retrieved allows us to make requests to GitHub\'s API and return data for the user that the `access_token` is attached to, up to the limits of the `scopes` we requested. GitHub has a unique user `id` that we can use to tie the two together. Let\'s request that data and dump it to the browser so we can see that the request works.

To keep things straight in our heads, let\'s call our local user `user` and the GitHub user the `providerUser` (since GitHub is \"providing\" the OAuth credentials).

Let\'s make the API call to GitHub\'s user info endpoint and dump the result to the browser:

/api/src/functions/oauth/oauth.js

``` 
const callback = async (event) =>  = event.queryStringParameters

  const response = await fetch(`https://github.com/login/oauth/access_token`, ,
    body: JSON.stringify(),
  })

  const  = JSON.parse(await response.text())

  if (error) 
  }

  try 
  } catch (e) 
  }
}

const getProviderUser = async (token) => ` },
  })
  const body = JSON.parse(await response.text())

  return body
}
```

If all went well you should get a ton of juicy data:

![GitHub user output](https://user-images.githubusercontent.com/300/245909925-c984eeb4-f172-46f6-8102-297b72e26bbd.png)

If something went wrong with the fetch you should get a 500 and the error message output in the body. Try setting the `token` in the `Authorization` header to something like `foobar` to verify:

![GitHub API error](https://user-images.githubusercontent.com/300/245910198-2975e90e-9af1-49b1-a41a-81b9269ff71d.png)

Great, we\'ve got the user data, now what do we do with it?

### Database Updates[​](#database-updates "Direct link to Database Updates") 

We\'ve got a bunch of user data that we can use to create a `User` in our own database. But we\'ll want to look up that same user in the future when they log back in. We have a couple of ways we can go about doing this:

1.  Keep our `User` model as-is and create the user in our local database. When the user logs in again, look them by their email address stored in GitHub. **Cons:** If the user changes their email in GitHub we won\'t be able to find them the next time they log in, and we would create a new user.
2.  Keep the `User` model as-is but create the user with the same `id` as the one we get from GitHub. **Cons:** If we keep username/password login, we would need to create new users with an `id` that won\'t ever clash with the ones from GitHub.
3.  Add a column to `User` like `githubId` that stores the GitHub `id` so that we can find the user again the next time they come to login. **Cons:** If we add more providers in the future we\'ll need to keep adding new `*Id` columns for each.
4.  Create a new one-to-many relationship model that stores the GitHub `id` as a single row, tied to the `userId` of the `User` table, and a new row for each ID of any future providers. **Cons:** More complex data structure.

Option #4 will be the most flexible going forward if we ever decide to add more OAuth providers. And if my experience is any indication, everyone always wants more login providers.

So let\'s create a new `Identity` table that stores the name of the provider and the ID in that system. Logically it will look like this:

``` 
┌───────────┐       ┌────────────┐
│   User    │       │  Identity  │
├───────────┤       ├────────────┤
│ id        │•──┐   │ id         │
│ name      │   └──<│ userId     │
│ email     │       │ provider   │
│ ...       │       │ uid        │
└───────────┘       │ ...        │
                    └────────────┘
```

For now `provider` will always be `github` and the `uid` will be the GitHub\'s unique ID. `uid` should be a `String`, because although GitHub\'s ID\'s are integers, not every OAuth provider is guaranteed to use ints.

#### Prisma Schema Updates[​](#prisma-schema-updates "Direct link to Prisma Schema Updates") 

Here\'s the `Identity` model definition:

/api/db/schema.prisma

``` 
model Identity 
```

We\'re also storing the `accessToken` and `scope` that we got back from the last time we retrived them from GitHub, as well as a timestamp for the last time the user logged in. Storing the `scope` is useful because if you ever change them, you may want to notify users that have the previous scope definition to re-login so the new scopes can be authorized.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

There\'s no GraphQL SDL tied to the Identity table, so it is not accessible via our API. But, if you ever did create an SDL and service, be sure that `accessToken` is not in the list of fields exposed publicly!

We\'ll need to add an `identities` relation to the `User` model, and make the previously required `hashedPassword` and `salt` fields optional (since users may want to *only* authenticate via GitHub, they\'ll never get to enter a password):

/api/db/schema.prisma

``` 
model User 
```

Save these as a migration and apply them to the database:

``` 
yarn rw prisma migrate dev
```

Give it a name like \"create identity\". That\'s it for the database. Let\'s return to the `/oauth` function and start working with our new `Identity` model.

### Creating Users and Identities[​](#creating-users-and-identities "Direct link to Creating Users and Identities") 

On a successful GitHub OAuth login we\'ll want to first check and see if a user already exists with the provider info. If so, we can go ahead and log them in. If not, we\'ll need to create it first, then log them in.

Let\'s add some code that returns the user if found, otherwise it creates the user *and* returns it, so that the rest of our code doesn\'t have to care.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

Be sure to import `db` at the top of the file if you haven\'t already!

/api/src/functions/oauth/oauth.js

``` 
import  from 'src/lib/db'

const callback = async (event) =>  = event.queryStringParameters

  const response = await fetch(`https://github.com/login/oauth/access_token`, ,
    body: JSON.stringify(),
  })

  const  = JSON.parse(await response.text())

  if (error) 
  }

  try )
    return 
  } catch (e) 
  }
}

const getUser = async () =>  = await findOrCreateUser(providerUser)

  await db.identity.update(,
    data: ,
  })

  return user
}

const findOrCreateUser = async (providerUser) => 
  })

  if (identity) })
    return 
  }

  // identity not found, need to create it and the user
  return await db.$transaction(async (tx) => ,
    }

    const identity = await tx.identity.create(
    })

    return 
  })
}
```

Let\'s break that down.

``` 
const providerUser = await getProviderUser(access_token)
const user = await getUser()
return 
```

After getting the `providerUser` we\'re going to find our local `user`, and then dump the user to the browser to verify.

``` 
const getUser = async () =>  = await getOrCreateUser(providerUser)

  await db.identity.update(,
    data: ,
  })

  return user
}
```

The `getUser()` function is going to return the user, whether it had to be created or not. Either way, the attached identity is updated with the current value for the `access_token` (note the case change, try not to get confused!), as well as the `scope` and `lastLoginAt` timestamp. `findOrCreateUser()` is going to do the heavy lifting:

``` 
const findOrCreateUser = async (providerUser) => ,
  })

  if (identity)  })
    return 
  }

  // ...
}
```

If the user already exists, great! Return it, and the attached `identity` so that we can update the details. If the user doesn\'t exist already:

``` 
const findOrCreateUser = async (providerUser) => ,
    }

    const identity = await tx.identity.create(
    })

    return 
  })
}
```

We create the `user` and the `identity` records inside a transaction so that if something goes wrong, both records fail to create. The error would bubble up to the try/catch inside `callback()`. (The Redwood test project has a required `fullName` field that we fill with the `name` attribute from GitHub.)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

Don\'t forget the `toString()` calls whenever we read or write the `providerUser.id` since we made the `uid` of type `String`.

If everything worked then on clicking **Login with GitHub** we should now see a dump of the actual user from our local database:

![User details](https://user-images.githubusercontent.com/300/245922971-caaeb3ed-9231-4edf-aac5-9ea76b488824.png)

You can take a look in the database and verify that the User and Identity were created. Start up the [Prisma Studio](https://www.prisma.io/studio) (which is already included with Redwood):

``` 
yarn rw prisma studio
```

![Inspecting the Identity record](https://user-images.githubusercontent.com/300/245923393-d61233cc-52d2-4568-858e-9059dfe31bfc.png)

Great! But, if you go back to your homepage, you\'ll find that you\'re not actually logged in. That\'s because we\'re not setting the cookie that dbAuth expects to see to consider you logged in. Let\'s do that, and then our login will be complete!

### Setting the Login Cookie[​](#setting-the-login-cookie "Direct link to Setting the Login Cookie") 

In order to let dbAuth do the work of actually considering us logged in (and handling stuff like reauthentication and logout) we\'ll just set the same cookie that the username/password login system would have if the user logged in with a username and password.

Setting a cookie in the browser is a matter of returning a `Set-Cookie` header in the response from the server. We\'ve been responding with a dump of the user object, but now we\'ll do a real return, including the cookie and a `Location` header to redirect us back to the site.

Don\'t forget the new `CryptoJS` import at the top!

/api/src/functions/oauth/oauth.js

``` 
import CryptoJS from 'crypto-js'
import  from '@redwoodjs/auth-dbauth-api'
import  from 'src/lib/auth'

const callback = async (event) =>  = event.queryStringParameters

  const response = await fetch(`https://github.com/login/oauth/access_token`, ,
    body: JSON.stringify(),
  })

  const  = JSON.parse(await response.text())

  if (error) 
  }

  try )
    const cookie = secureCookie(user)

    return ,
    }
  } catch (e) 
  }
}

const secureCookie = (user) => `,
    'HttpOnly=true',
    'Path=/',
    'SameSite=Lax',
    `Secure=$`,
  ]
  const data = JSON.stringify()

  const encrypted = CryptoJS.AES.encrypt(
    data,
    process.env.SESSION_SECRET
  ).toString()
  //if you're using dbAuth v7.6.2, you have to change the cookie name. You can comment out the line below and make the next line as comment.
  //return [`$=$`, ...cookieAttrs].join('; ')
  return [`session=$`, ...cookieAttrs].join('; ')
}
```

`secureCookie()` takes care of creating the cookie that matches the one set by dbAuth. The attributes that we\'re setting are actually a copy of the ones set in the `authHandler` in `/api/src/functions/auth.js` and you could remove some duplication between the two by exporting the `cookie` object from `auth.js` and then importing it and using it here. We\'ve set the cookie to expire in a year because, let\'s admit it, no one likes having to log back in again.

At the end of `callback()` we set the `Set-Cookie` and `Location` headers to send the browser back to the homepage of our app.

Try it out, and as long as you have an indication on your site that a user is logged in, you should see it! In the case of the test project, you\'ll see \"Log Out\" at the right side of the top nav instead of \"Log In\". Try logging out and then back again to test the whole flow from scratch.

## The Complete `/oauth` Function[​](#the-complete-oauth-function "Direct link to the-complete-oauth-function") 

Here\'s the `oauth` function in its entirety:

/api/src/functions/oauth/oauth.js

``` 
import CryptoJS from 'crypto-js'

import  from 'src/lib/db'

export const handler = async (event, _context) => 
  }
}

const callback = async (event) =>  = event.queryStringParameters

  const response = await fetch(`https://github.com/login/oauth/access_token`, ,
    body: JSON.stringify(),
  })

  const  = JSON.parse(await response.text())

  if (error) 
  }

  try )
    const cookie = secureCookie(user)

    return ,
    }
  } catch (e) 
  }
}

const secureCookie = (user) => `,
    'HttpOnly=true',
    'Path=/',
    'SameSite=Lax',
    `Secure=$`,
  ]
  const data = JSON.stringify()

  const encrypted = CryptoJS.AES.encrypt(
    data,
    process.env.SESSION_SECRET
  ).toString()

  return [`session=$`, ...cookieAttrs].join('; ')
}

const getProviderUser = async (token) => ` },
  })
  const body = JSON.parse(await response.text())

  return body
}

const getUser = async () =>  = await findOrCreateUser(providerUser)

  await db.identity.update(,
    data: ,
  })

  return user
}

const findOrCreateUser = async (providerUser) => ,
  })

  if (identity)  })
    return 
  }

  // identity not found, need to create it and the user
  return await db.$transaction(async (tx) => ,
    })

    const identity = await tx.identity.create(,
    })

    return 
  })
}
```

## Enhancements[​](#enhancements "Direct link to Enhancements") 

This is barebones implementation of a single OAuth provider. What can we do to make it better?

### More Providers[​](#more-providers "Direct link to More Providers") 

We hardcoded \"github\" as the provider in a couple of places, as well as hardcoding GitHub\'s API endpoint for fetching user data. That obviously limits this implementation to only support GitHub.

A more flexible version could include the provider as part of the callback URL, and then our code can see that and choose which provider to set and how to get user details. Maybe the OAuth redirect is `/oauth/github/callback` and `/oauth/twitter/callback`. Then parse that out and delegate to a different function altogether, or implement each provider\'s specific info into separate files and `import` them into the `/oauth` function, invoking each as needed.

### Changing User Details[​](#changing-user-details "Direct link to Changing User Details") 

Right now we just copy the user details from GitHub right into our new User object. Maybe we want to give the user a chance to update those details first, or add additional information before saving to the database. One solution could be to create the `Identity` record, but redirect to your real Signup page with the info from GitHub (and the `accessToken`) and prefill the signup fields, giving the user a chance to change or enhance them, adding the `accessToken` to a hidden field. Then when the user submits that form, if the `accessToken` is part of the form, get the user details from GitHub again (so we can get their GitHub `id`) and then create the `Identity` and `User` record as before.

### Better Error Handling[​](#better-error-handling "Direct link to Better Error Handling") 

Right now if an error occurs in the OAuth flow, the browser just stays on the `/oauth/callback` function and sees a plain text error message. A better experience would be to redirect the user back to the login page, with the error message in a query string variable, something like `http://localhost:8910/login?error=Application+not+authorized` Then in the LoginPage, add a `useParams()` to pull out the query variables, and show a toast message if an error is present:

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/web/toast'

const LoginPage = () => 
  }, [params.error])

  return (
    <>
      <Toaster />
      // ...
    </>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/oauth.md)