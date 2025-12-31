# Source: https://docs.redwoodjs.com/docs/cors

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Cross-Origin Resource Sharing]

[Version: 8.8]

On this page

<div>

# CORS

</div>

CORS stands for [Cross Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS). In a nutshell, by default, browsers aren\'t allowed to access resources outside their own domain.

## When you need to worry about CORS[​](#when-you-need-to-worry-about-cors "Direct link to When you need to worry about CORS") 

If your api and web sides are deployed to different domains, you\'ll have to worry about CORS. For example, if your web side is deployed to `example.com` but your api is `api.example.com`. For security reasons your browser will not allow XHR requests (like the kind that the GraphQL client makes) to a domain other than the one currently in the browser\'s address bar.

This will become obvious when you point your browser to your site and see none of your GraphQL data. When you look in the web inspector you\'ll see a message along the lines of:

> ⛔️ Access to fetch [https://api.example.com](https://api.example.com) has been blocked by CORS policy: Response to preflight request doesn\'t pass access control check: No \'Access-Control-Allow-Origin\' header is present on the requested resource.

## Avoiding CORS[​](#avoiding-cors "Direct link to Avoiding CORS") 

Dealing with CORS can complicate your app and make it harder to deploy to new hosts, run in different environments, etc. Is there a way to avoid CORS altogether?

Yes! If you can add a proxy between your web and api sides, all requests will *appear* to be going to and from the same domain (the web side, even though behind the scenes they are forwarded somewhere else). This functionality is included automatically with hosts like [Netlify](https://docs.netlify.com/routing/redirects/rewrites-proxies/#proxy-to-another-service) or [Vercel](https://vercel.com/docs/cli#project-configuration/rewrites). With a host like [Render](https://render-web.onrender.com/docs/deploy-redwood#deployment) you can enable a proxy with a simple config option. Most providers should provide this functionality through a combination of provider-specific config and/or web server configuration.

## GraphQL Config[​](#graphql-config "Direct link to GraphQL Config") 

You\'ll need to add CORS headers to GraphQL responses. You can do this easily enough by adding the `cors` option in `api/src/functions/graphql.js` (or `graphql.ts`):

``` 
export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
+ cors: ,
  onException: () => ,
})
```

Note that the `origin` needs to be a complete URL including the scheme (`https`). This is the domain that requests are allowed to come *from*. In this example we assume the web side is served from `https://www.example.com`. If you have multiple servers that should be allowed to access the api, you can pass an array of them instead:

``` 
cors: ,
```

The proper one will be included in the CORS header depending on where the response came from.

## Authentication Config[​](#authentication-config "Direct link to Authentication Config") 

The following config only applies if you\'re using [dbAuth](/docs/authentication#self-hosted-auth-installation-and-setup), which is Redwood\'s own cookie-based auth system.

You\'ll need to configure several things:

-   Add CORS config for GraphQL
-   Add CORS config for the auth function
-   Cookie config for the auth function
-   Allow sending of credentials in GraphQL XHR requests
-   Allow sending of credentials in auth function requests

Here\'s how you configure each of these:

### GraphQL CORS Config[​](#graphql-cors-config "Direct link to GraphQL CORS Config") 

You\'ll need to add CORS headers to GraphQL responses, and let the browser know to send up cookies with any requests. Add the `cors` option in `api/src/functions/graphql.js` (or `graphql.ts`) with an additional `credentials` property:

``` 
export const handler = createGraphQLHandler( },
  directives,
  sdls,
  services,
+ cors: ,
  onException: () => ,
})
```

`origin` is the domain(s) that requests come *from* (the web side).

### Auth CORS Config[​](#auth-cors-config "Direct link to Auth CORS Config") 

Similar to the `cors` options being sent to GraphQL, you can set similar options in `api/src/functions/auth.js` (or `auth.ts`):

``` 
const authHandler = new DbAuthHandler(event, context, ,
+ cors: ,
  cookie: ,
  forgotPassword: forgotPasswordOptions,
  login: loginOptions,
  resetPassword: resetPasswordOptions,
  signup: signupOptions,
})
```

Just like the GraphQL config, `origin` is the domain(s) that requests come *from* (the web side).

### Cookie Config[​](#cookie-config "Direct link to Cookie Config") 

In order to be able accept cookies from another domain we\'ll need to make a change to the `SameSite` option in `api/src/functions/auth.js` and set it to `None`:

``` 
  cookie: ,
```

### GraphQL XHR Credentials[​](#graphql-xhr-credentials "Direct link to GraphQL XHR Credentials") 

Next we need to tell the GraphQL client to include credentials (the dbAuth cookie) in any requests. This config goes in `web/src/App.`:

``` 
import  from 'src/auth'

const App = () => (
  <FatalErrorBoundary page=>
    <RedwoodProvider titleTemplate="%PageTitle | %AppTitle">
      <AuthProvider type="dbAuth">
        <RedwoodApolloProvider
          useAuth=
          graphQLClientConfig=,
          }}
        >
          <Routes />
        </RedwoodApolloProvider>
      </AuthProvider>
    </RedwoodProvider>
  </FatalErrorBoundary>
)
```

### Auth XHR Credentials[​](#auth-xhr-credentials "Direct link to Auth XHR Credentials") 

Finally, we need to tell dbAuth to include credentials in its own XHR requests. We\'ll do this within `web/src/auth.` when creating the `AuthProvider`:

``` 
import  from '@redwoodjs/auth-dbauth-web'

const dbAuthClient = createDbAuthClient(,
})

export const  = createAuth(dbAuthClient)
```

## Testing CORS Locally[​](#testing-cors-locally "Direct link to Testing CORS Locally") 

If you\'ve made the configuration changes above, `localhost` testing should continue working as normal. But, if you want to make sure your CORS config works without deploying to the internet somewhere, you\'ll need to do some extra work.

### Serving Sides to the Internet[​](#serving-sides-to-the-internet "Direct link to Serving Sides to the Internet") 

First, you need to get the web and api sides to be serving from different hosts. A tool like [ngrok](https://ngrok.com/) or [localhost.run](https://localhost.run/) allows you to serve your local development environment over a real domain to the rest of the internet (on both `http` and `https`).

You\'ll need to start two tunnels, one for the web side (this example assumes ngrok):

``` 
> ngrok http 8910

Session Status  online
Account         Your Name (Plan: Pro)
Version         2.3.40
Region          United States (us)
Web Interface   http://127.0.0.1:4040
Forwarding      http://3c9913de0c00.ngrok.io -> http://localhost:8910
Forwarding      https://3c9913de0c00.ngrok.io -> http://localhost:8910
```

And another for the api side:

``` 
> ngrok http 8911

Session Status  online
Account         Your Name (Plan: Pro)
Version         2.3.40
Region          United States (us)
Web Interface   http://127.0.0.1:4040
Forwarding      http://fb6d701c44b5.ngrok.io -> http://localhost:8911
Forwarding      https://fb6d701c44b5.ngrok.io -> http://localhost:8911
```

Note the two different domains. Copy the `https` domain from the api side because we\'ll need it in a moment. Even if the Redwood dev server isn\'t running you can leave these tunnels running, and when the dev server *does* start, they\'ll just start on those domains again.

### `redwood.toml` Config[​](#redwoodtoml-config "Direct link to redwoodtoml-config") 

You\'ll need to make two changes here:

1.  Bind the server to all network interfaces
2.  Point the web side to the api\'s domain

Normally the dev server only binds to `127.0.0.1` (home sweet home) which means you can only access it from your local machine using `localhost` or `127.0.0.1`. To tell it to bind to all network interfaces, and to be available to the outside world, add this `host` option:

``` 
[web]
  title = "Redwood App"
  port = 8910
  host = '0.0.0.0'
  apiUrl = '/.redwood/functions'
  includeEnvironmentVariables = []
[api]
  port = 8911
[browser]
  open = true
```

We\'ll also need to tell the web side where the api side lives. Update the `apiUrl` to whatever domain your api side is running on (remember the domain you copied from from ngrok):

``` 
[web]
  title = "Redwood App"
  port = 8910
  host = '0.0.0.0'
  apiUrl = 'https://fb6d701c44b5.ngrok.io'
  includeEnvironmentVariables = []
[api]
  port = 8911
[browser]
  open = true
```

Where you get this domain from will depend on how you expose your app to the outside world (this example assumes ngrok).

### Starting the Dev Server[​](#starting-the-dev-server "Direct link to Starting the Dev Server") 

You\'ll need to apply an option when starting the dev server to tell it to accept requests from any host, not just `localhost`:

``` 
rw > yarn dev --fwd="--allowed-hosts all"
```

### Wrapping Up[​](#wrapping-up "Direct link to Wrapping Up") 

Now you should be able to open the web side\'s domain in a browser and use your site as usual. Test that GraphQL requests work, as well as authentication if you are using dbAuth.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/cors.md)