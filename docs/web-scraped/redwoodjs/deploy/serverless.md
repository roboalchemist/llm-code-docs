# Source: https://docs.redwoodjs.com/docs/deploy/serverless

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Deployment](/docs/deployment/index)
-   [Serverless Framework]

[Version: 8.8]

On this page

<div>

# Deploy to AWS with Serverless Framework

</div>

> ⚠️ **Deprecated** As of Redwood v5, we are deprecating this deploy setup as an \"officially\" supported provider. This means:
>
> -   For projects already using this deploy provider, there will be NO change at this time
> -   Both the associated `setup` and `deploy` commands will remain in the framework as is; when setup is run, there will be a "deprecation" message
> -   We will no longer run CI/CD on the Serverless-AWS deployments, which means we are no longer guaranteeing this deploy works with each new version
> -   We are exploring better options to deploy directly to AWS Lambdas; the current deploy commands will not be removed until we find a replacement
>
> For more details (e.g. why?) and current status, see the Forum post [\"Deprecating support for Serverless Framework Deployments to AWS Lambdas\"](https://community.redwoodjs.com/t/deprecating-support-for-serverless-framework-deployments-to-aws-lambdas/4755/10)

> The following instructions assume you have read the [General Deployment Setup](/docs/deploy/introduction#general-deployment-setup) section above.

Yes, the name is confusing, but Serverless provides a very interesting option---deploy to your own cloud service account and skip the middleman entirely! By default, Serverless just orchestrates starting up services in your cloud provider of choice and pushing your code up to them. Any bill you receive is from your hosting provider (although many offer a generous free tier). You can optionally use the [Serverless Dashboard](https://www.serverless.com/dashboard/) to monitor your deploys and setup CI/CD to automatically deploy when pushing to your repo of choice. If you don\'t setup CI/CD you actually deploy from your development machine (or another designated machine you\'ve setup to do the deployment).

Currently we default to deploying to AWS. We\'d like to add more providers in the future but need help from the community in figuring out what services are equivalent to the ones we\'re using in AWS (Lambda for the api-side and S3/CloudFront for the web-side).

We\'ll handle most of the deployment commands for you, you just need an [AWS account](https://www.serverless.com/framework/docs/providers/aws/guide/credentials#sign-up-for-an-aws-account) and your [access/secret keys](https://www.serverless.com/framework/docs/providers/aws/guide/credentials#create-an-iam-user-and-access-key) before we begin.

## Setup[​](#setup "Direct link to Setup") 

One command will set you up with (almost) everything you need:

``` 
yarn rw setup deploy serverless
```

As you\'ll see mentioned in the post-install instructions, you\'ll need to provide your AWS Access and AWS Secret Access keys. Add those to the designated places in your `.env` file:

``` 
# .env

AWS_ACCESS_KEY_ID=<your-key-here>
AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
```

Make sure you don\'t check `.env` into your repo! It\'s set in `.gitignore` by default, so make sure it stays that way.

## First Deploy[​](#first-deploy "Direct link to First Deploy") 

You\'ll need to add a special flag to the deploy command for your first deploy:

``` 
yarn rw deploy serverless --first-run
```

The first time you deploy your app we\'ll first deploy just the API side. Once it\'s live we can get the URL that it\'s been deployed to and add that as an environment variable `API_URL` so that web side will know what it is during build-time (it needs to know where to send GraphQL and function requests).

Half-way through the first deploy you\'ll be asked if you want to add the API_URL to `.env.production` (which is similar to `.env` but is only used when `NODE_ENV=production`, like when building the web and api sides for deploy). Make sure you say `Y`es at this prompt and then it will continue to deploy the web side.

Once that command completes you should see a message including the URL of your site---open that URL and hopefully everything works as expected!

> **Heads up**
>
> If you\'re getting an error trying to load data from the API side, its possible you\'re still pointing at your local database.
>
> Remember to add a DATABASE_URL env var to your `.env.production` file that is created, pointing at the database you want to use on your deployed site. Since your stack is on AWS, RDS might be a good option, but you might find it easier/quicker to setup databases on other providers too, such as [Railway](https://railway.app/) or [Supabase](https://supabase.com/)

## Subsequent Deploys[​](#subsequent-deploys "Direct link to Subsequent Deploys") 

From now on you can simply run `yarn rw deploy serverless` when you\'re ready to deploy (which will also be much faster).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

Remember, if you add or generate new serverless functions (or endpoints), you\'ll need to update the configuration in your serverless.yml in `./api/serverless.yml`.

By default we only configure the `auth` and `graphql` functions for you.

## Environment Variables[​](#environment-variables "Direct link to Environment Variables") 

For local deployment (meaning you\'re deploying from your own machine, or another that you\'re in control of) you can put any ENV vars that are production-only into `.env.production`. They will override any same-named vars in `.env`. Make sure neither of these files is checked into your code repository!

If you\'re setting up CI/CD and deploying from the Serverless Dashboard, you\'ll need to copy your required ENV vars up to your app on Serverless and then tell it where to get them from. In `api/serverless.yml` and `web/serverless.yml` look for the `provider > environment` section. You\'ll need to list any ENV vars here, using the `$` syntax, which means to get them from the Serverless Dashboard \"parameters\" (which is what they call environment variables, for some strange reason).

There are even more places you can get environment variables from, check out Serverless\'s [Variables documentation](https://www.serverless.com/framework/docs/providers/aws/guide/variables) for more.

## Serverless Dashboard[​](#serverless-dashboard "Direct link to Serverless Dashboard") 

> **Note:** Serverless Dashboard CI/CD does not support projects structured like Redwood, although they\'re working on it. For CD, you\'ll need to use something like GitHub Actions.
>
> It can still be worthwhile to integrate your project with Serverless Dashboard --- you\'ll have features like deploy logs and monitoring, analytics, secret management, and AWS account integration. You can also [authenticate into your Serverless account within a CI context](https://www.serverless.com/framework/docs/guides/cicd/running-in-your-own-cicd). Just remember that if you do use the Dashboard to manage secrets, you\'ll need to use the `$` syntax.

To integrate your site into the Serverless Dashboard, there are two ways:

1.  Run `yarn serverless login` and a browser *should* open asking you to allow permission. However, in our experience, this command will fail nearly 50% of the time complaining about an invalid URL. If it *does* work you can then run `yarn serverless` in both the `api` and `web` directories to link to them an existing app in the Dashboard, or you\'ll be prompted to create a new one. Future deploys will now be monitored on the Dashboard.
2.  You can manually add the `org` and `app` lines in `api/serverless.yml` and `web/serverless.yml`. You\'ll see example ones commented out near the top of the file.

## Environments Besides Production[​](#environments-besides-production "Direct link to Environments Besides Production") 

By default we assume you want to deploy to a production environment, but Serverless lets you deploy anywhere. They call these destinations \"stages\", and in Redwood \"production\" is the default. Check out their [Managing Staging and Environments blog post](https://www.serverless.com/blog/stages-and-environments) for details.

Once configured, just add the stage to your deploy command:

``` 
yarn rw deploy serverless --stage qa
```

## Removing Your Deploy[​](#removing-your-deploy "Direct link to Removing Your Deploy") 

In addition to creating all of the services necessary for your app to run, Serverless can also remove them (which is great when testing to avoid paying for services you\'re no longer using).

You\'ll need to run this command in both the `api` and `web` directories:

``` 
yarn serverless remove --stage production
```

Note that `production` is the default stage when you deploy with `yarn rw serverless deploy` - if you have customized this, you have to use the same stage as you deployed with!

This will take several minutes, so grab your favorite beverage and enjoy your new \$0 monthly bill!

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]Pro tip

If you get tired of typing `serverless` each time, you can use the much shorter `sls` alias: `yarn rw deploy sls`

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting") 

If you happen to see the following error when deploying:

``` 
Error:
No auth.zip file found in the package path you provided.
```

Make sure that the dev server isn\'t running, then retry your deploy.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/deploy/serverless.md)