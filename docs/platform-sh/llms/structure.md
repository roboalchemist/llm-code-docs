# Source: https://docs.upsun.com/learn/overview/structure.md

# Structure


Each environment you deploy on Upsun is built as a set of containers.
Each container is an isolated instance with specific resources.

Each environment has 2 to 4 types of containers, all usually configured from your `.upsun/config.yaml` file.

- One [*router*](#router)
- One or more [*app* containers](#apps)
- Zero or more [*service* containers](#services)
- Zero or more [*worker* containers](#workers)

If you have two app containers, two services (a database and a search engine), and a worker,
requests to your environment might look something like this:

![A user request goes to the router, which sends it to either a Node.js app or a Python app. Each app communicates separately with the database and search services and sends responses to the user. The Node.js app triggers actions in a worker, which communicates separately with the database.](https://docs.upsun.com/images/config-diagrams/structure-diagram.png)

If you have only one app container, your repository might look like this:

```text {no-copy="true"}
project
├── .git
├── .upsun
│   └── config.yaml
└── <YOUR_APP_FILES>
```

## Router

Each environment always has exactly one router.

This router maps incoming requests to the appropriate app container
and provides basic caching of responses, unless configured otherwise.

The router is configured in a `.upsun/config.yaml` file.
If you don't include configuration, a single [default route is deployed](https://docs.upsun.com/define-routes.md#default-route-definition).

Read more about how to [define routes](https://docs.upsun.com/define-routes.md).

## Apps

You always need at least one app container, but you can have more.

App containers run the code you provide via your Git repository.
They handle requests from the outside world and can communicate with other containers within the environment.
Each app container is built from a specific language image with a given version for the language.

To configure your apps, you usually create a single `.upsun/config.yaml` file
and place it in the repository root.

Read more about how to [configure apps](https://docs.upsun.com/create-apps.md).

## Services

You don't need any service containers, but you can add them as you like.

Service containers run predefined code for specific purposes, such as a database or search service.
You don't need to add their code yourself, just set up how your apps communicate with them.

Service containers are configured by the `.upsun/config.yaml` file.

Read more about how to [add services](https://docs.upsun.com/add-services.md).

## Workers

You don't need any worker containers, but you can add them as you like.

Worker containers are copies of an app containers
that have no access to the outside world and can have a different start command.
They're useful for continually running background processes.

Read more about how to [work with workers](https://docs.upsun.com/create-apps/workers.md).

