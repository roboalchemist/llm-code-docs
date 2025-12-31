# Source: https://docs.redwoodjs.com/docs/how-to/creating-a-background-worker-with-exec-and-faktory

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [Creating a Background Worker with Exec and Faktory]

[Version: 8.8]

On this page

<div>

# Creating a Background Worker with Exec and Faktory

</div>

In this how to, we\'ll use Redwood\'s [exec CLI command](/docs/cli-commands#exec) to create a background worker using [Faktory](https://contribsys.com/faktory/).

At a high level, Faktory is a language-agnostic, persistent background-job server. You can run it [with Docker](https://github.com/contribsys/faktory/wiki/Docker).

We\'ll have to have a way of communicating with the server from our Redwood app. We\'ll use this [node library](https://github.com/jbielick/faktory_worker_node) to send jobs from our Redwood app to our Faktory server.

## Creating the Faktory Worker[​](#creating-the-faktory-worker "Direct link to Creating the Faktory Worker") 

Let\'s create our faktory worker. First, generate the worker script:

``` 
yarn rw g script faktoryWorker
```

We\'ll start by registering a task called `postSignupTask` in our worker:

scripts/faktoryWorker.js

``` 
const  from '$api/src/lib/tasks'
import  from '$api/src/lib/logger'

import faktory from 'faktory-worker'

faktory.register('postSignupTask', async (taskArgs) => )

export default async () => )
    .catch((error) => `)
      process.exit(1)
    })

  worker.on('fail', () => `)
  })
}
```

This won\'t work yet as we haven\'t made `postSignupTask` in `api/src/lib/tasks.js` or set `FAKTORY_URL`. Set `FAKTORY_URL` in `.env` to where your server\'s running.

In `postSignupTask`, we may want to perform operations that need to contact external services, such as sending an email. For this type of work, we typically don\'t want to hold up the request/response cycle and can perform it in the background:

api/src/lib/tasks.js

``` 
export const postSignupTask = async () => ,
  })
}
```

Once we\'ve created our task, we need to call it in the right place. For this task, it makes sense to call it right after the user has completed their signup. This is an example of a Service that\'ll most likely be called via a GraphQL Mutation.

src/services/auth/auth.js

``` 
const faktory = require('faktory-worker')

export const signUp = async () => ).push()
  await client.close()
}
```

That\'s it---we\'re done! Run your Faktory server using Docker and run the worker using `yarn rw exec faktoryWorker`.

If your Faktory server is running and you have set `FAKTORY_URL` correctly, you\'ll see the server pick up the jobs and your worker process the job.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/background-worker.md)