# Source: https://docs.redwoodjs.com/docs/monitoring/sentry

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Monitoring](/docs/monitoring/index)
-   [Sentry]

[Version: 8.8]

On this page

<div>

# Sentry

</div>

**Setup [Sentry](https://sentry.io/welcome/) error and performance monitoring across your Redwood application.**

From your command line, run:

``` 
yarn redwood setup monitoring sentry
```

This command installs and sets up [`@sentry/node`](https://docs.sentry.io/platforms/node/) and [`@sentry/react`](https://docs.sentry.io/platforms/javascript/guides/react/), enabling [Prisma](https://docs.sentry.io/platforms/node/performance/database/opt-in/#prisma-orm-integration) and [Browser](https://docs.sentry.io/platforms/javascript/performance/instrumentation/automatic-instrumentation/) tracing to capture 100% of events. The following sections detail how you may further integrate Sentry in your Redwood application.

## Sentry Envelop Plugin[​](#sentry-envelop-plugin "Direct link to Sentry Envelop Plugin") 

The setup command will install and attempt to setup the [`@envelop/sentry`](https://the-guild.dev/graphql/envelop/plugins/use-sentry) plugin in your application\'s GraphQL handler. If there is a problem installing it, the following can be used to do so manually.

-   JavaScript
-   TypeScript

api/src/functions/graphql.js

``` 
import  from '@envelop/sentry'

import  from '@redwoodjs/graphql-server'

import directives from 'src/directives/**/*.'
import sdls from 'src/graphql/**/*.sdl.'
import services from 'src/services/**/*.'

import 'src/lib/sentry'

...

export const handler = createGraphQLHandler()
```

api/src/functions/graphql.ts

``` 
import  from '@envelop/sentry'

import  from '@redwoodjs/graphql-server'

import directives from 'src/directives/**/*.'
import sdls from 'src/graphql/**/*.sdl.'
import services from 'src/services/**/*.'

import 'src/lib/sentry'

...

export const handler = createGraphQLHandler()
```

## Setting the current user[​](#setting-the-current-user "Direct link to Setting the current user") 

You can associate error and performance events with a unique identity using [`Sentry.setUser`](https://docs.sentry.io/platforms/node/enriching-events/identify-user/). Below is an example of doing so on the API by setting the identity to the user returned by `getCurrentUser`.

-   JavaScript
-   TypeScript

api/src/lib/auth.js

``` 
import Sentry from 'src/lib/sentry'

export const getCurrentUser = async (...) => 
```

api/src/lib/auth.ts

``` 
import Sentry from 'src/lib/sentry'

export const getCurrentUser = async (...) => 
```

Below we set the current user on the web-side from within a [layout](#generate-layout). Note that the `useEffect` dependency array may vary depending on where you place `Sentry.setUser` in your own application.

-   JavaScript
-   TypeScript

web/src/layouts/SentryLayout/SentryLayout.jsx

``` 
import  from 'react'

import  from 'src/lib/auth'
import Sentry from 'src/lib/sentry'

const SentryLayout = () =>  = useAuth()

  useEffect(() => Sentry.setUser(currentUser), [currentUser])

  return <></>
}

export default SentryLayout
```

web/src/layouts/SentryLayout/SentryLayout.tsx

``` 
import React,  from 'react'

import  from 'src/lib/auth'
import Sentry from 'src/lib/sentry'

interface Props 

const SentryLayout = (: Props) =>  = useAuth()

  useEffect(() => Sentry.setUser(currentUser), [currentUser])

  return <></>
}

export default SentryLayout
```

## Capturing exceptions[​](#capturing-exceptions "Direct link to Capturing exceptions") 

You can make use of Sentry to capture exceptions which occur while executing API [Functions](#generate-function).

api/src/functions/foo.

``` 
import Sentry from 'src/lib/sentry'

export const handler = async (event, context) =>  catch (err) 
}
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/monitoring/sentry.md)