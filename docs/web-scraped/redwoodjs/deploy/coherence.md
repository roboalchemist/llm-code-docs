# Source: https://docs.redwoodjs.com/docs/deploy/coherence

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Deployment](/docs/deployment/index)
-   [GCP or AWS via Coherence]

[Version: 8.8]

On this page

<div>

# Deploy to Coherence

</div>

[Coherence](https://www.withcoherence.com/) delivers automated environments across the full software development lifecycle, without requiring you to glue together your own mess of open source tools to get a world-class develper experience for your team. Coherence is focused on serving startups, who are doing mission-critical work. With one simple configuration, Coherence offers:

-   Cloud-hosted development environments, based on VSCode. Similar to Gitpod or GitHub CodeSpaces
-   Production-ready CI/CD running in your own GCP/AWS account, including: database migration/seeding/snapshot loading, parallelized tests, container building and docker registry management
-   Full-stack branch previews. Vercel/Netlify-like developer experience for arbitrary container apps, including dependencies such as CDN, redis, and database resources
-   Staging and production environment management in your AWS/GCP accounts. Production runs in its own cloud account (AWS) or project (GCP). Integrated secrets management across all environment types with a developer-friendly UI

## Coherence Prerequisites[​](#coherence-prerequisites "Direct link to Coherence Prerequisites") 

To deploy to Coherence, your Redwood project needs to be hosted on GitHub and you must have an [AWS](https://docs.withcoherence.com/docs/overview/aws-deep-dive) or [GCP](https://docs.withcoherence.com/docs/overview/gcp-deep-dive) account.

## Coherence Deploy[​](#coherence-deploy "Direct link to Coherence Deploy") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]Prerender doesn\'t work with Coherence yet

You can see its current status and follow updates here on GitHub: [https://github.com/redwoodjs/redwood/issues/8333](https://github.com/redwoodjs/redwood/issues/8333).

But if you don\'t use prerender, carry on!

If you want to deploy your Redwood project on Coherence, run the setup command:

``` 
yarn rw setup deploy coherence
```

The command will inspect your Prisma config to determine if you\'re using a supported database (at the moment, only `postgres` or `mysql` are supported on Coherence).

Then follow the [Coherence Redwood deploy docs](https://docs.withcoherence.com/docs/configuration/frameworks#redwood-js) for more information, including if you want to set up:

-   a redis server
-   database migration/seeding/snapshot loading
-   cron jobs or async workers
-   object storage using Google Cloud Storage or AWS\'s S3

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/deploy/coherence.md)