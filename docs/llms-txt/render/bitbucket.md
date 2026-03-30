# Source: https://render.com/docs/bitbucket.md

# Connect Bitbucket

Connect your [Bitbucket](https://bitbucket.org/) account to Render to start deploying apps and sites using any repo you have access to. Render automatically redeploys your project with every push to your linked branch (you can [disable this](/deploys#disabling-auto-deploys)).

Render can also spin up a [preview instance](service-previews) of your project with every opened pull request to help you validate changes.

## Setup

1. When you create your first service in the [Render Dashboard](https://dashboard.render.com), you're prompted to connect your Git provider:

   [image: Git Connect]

2. Click *Connect Bitbucket*. This redirects you to Bitbucket so you can authorize Render to access your repositories.

3. You're then redirected back to the Render Dashboard, which now displays a list of your Bitbucket repos:

   [image: List of Bitbucket repos in the Render Dashboard]

You've successfully linked your Bitbucket account! Whenever you create a new service, click the *Connect* button for whichever repo you want to use for that service. Then complete the remainder of the service creation flow.

## Pull request previews

Render can automatically build and deploy a preview instance of your service for every pull request that's opened against your project.

For details, see [Service previews](service-previews#pull-request-previews-git-backed).

## Git submodules

If your repo defines a `.gitmodules` file at its root, Render automatically reads it and clones all specified [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) as part of your service's build process.

> If your `.gitmodules` file includes _private_ submodules, Render can clone them only if your linked Bitbucket account has access to the corresponding private repository.

## Log in with Bitbucket

In addition to deploying projects from Bitbucket, you can use your Bitbucket account to log in to the [Render Dashboard](https://dashboard.render.com). If you have an existing Render account that matches your Bitbucket account's primary email address, Render logs you in to that existing account automatically.

Learn more about [managing login methods](login-settings#managing-login-methods).