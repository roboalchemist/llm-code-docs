# Source: https://render.com/docs/deploy-remix.md

# Deploy a Remix App

[Remix](https://remix.run) is "a full stack web framework that lets you focus on the user interface…to deliver a fast, slick, and resilient user experience." It comes from some well-known developers in the React ecosystem and has been getting more and more attention since its open source debut at the end of 2021.

You can read more about the [philosophy behind Remix](https://remix.run/docs/en/v1/pages/philosophy), including why its creators think it's a big improvement over existing front-end frameworks. But if you want to get started deploying Remix to Render quickly, follow along below.

*Choose which Remix example you want to deploy:*

1. [Just the basics](#just-the-basics) - this example contains the code generated when you run `npx create-remix@latest` and choose JavaScript.
2. [Production Ready](#production-ready) - this contains a slightly modified version of Remix's [Indie Stack](https://github.com/remix-run/indie-stack). It uses TypeScript and includes a PostgreSQL database, the Prisma ORM, unit and end-to-end test scaffolding, and many other features that are useful for a production front-end app.

## Just the Basics

Follow the steps below to deploy your own sample Remix app on Render.

1. [Create your own repository from Render's `remix` template repository](https://github.com/new?template_name=remix&template_owner=render-examples) on GitHub (you may need to log in first).
   - Alternatively, you can [clone the repository](https://github.com/render-examples/remix/) and push your clone to GitLab or Bitbucket.
2. Create a [new Web Service](https://dashboard.render.com/select-repo?type=web) on Render, and give Render permission to access the repository.
3. Use the following values during creation:

|                   |                                                                        |
| ----------------- | ---------------------------------------------------------------------- |
| *Language*      | `Node`                                                                 |
| *Build Command* | `npm ci --production=false && npm run build && npm prune --production` |
| *Start Command* | `npm start`                                                            |

You may select the [*Free Instance Type*](free) if you'd like to try Remix on Render for free. Web Services on the free instance type will spin down after 15 minutes of no activity.

That's it! Your Remix app will be live on your Render URL as soon as the build finishes and the service starts.

## Production Ready

A sample of this app has been [deployed to Render](http://remix-fbnj.onrender.com) for you to check out. Follow the steps below to deploy your own for free.

1. [Create your own repository from Render's `remix-postgres` template repository](https://github.com/new?template_name=remix-postgres&template_owner=render-examples) on GitHub.
   - Alternatively, you can [clone the repository](https://github.com/render-examples/remix-postgres) and push your clone to GitLab or Bitbucket.
2. In the [Render Dashboard](https://dashboard.render.com), click *New* --> *Blueprint* and select your copy of this repository. You may need to connect your GitHub account to Render if you haven't already done so. A Blueprint deploy will use the repository's `render.yaml` to determine what to deploy to Render.
3. Give your *Service Group* a name and click *Apply*.
4. When the database and service have been created, open your service's `.onrender.com` URL in a browser to see your Remix app running on Render. See the README in the GitHub repository for more details about local development, testing, and using the Prisma ORM.