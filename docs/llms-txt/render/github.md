# Source: https://render.com/docs/github.md

# Connect GitHub — Deploy with every push to your linked branch.

Connect your [GitHub](https://github.com) account to Render to start deploying apps and sites using any repo you have access to. Render automatically redeploys your project with every push to your linked branch (you can [disable this](/deploys#disabling-auto-deploys)).

Render can also spin up a [preview instance](service-previews) of your project with every opened pull request to help you validate changes.

## Setup

1. When you create your first service in the [Render Dashboard](https://dashboard.render.com), you're prompted to connect your Git provider:

   [image: Git Connect]

2. Click *GitHub*. This redirects you to GitHub so you can authorize Render to access your repositories.

3. You're then redirected back to the Render Dashboard, which now displays a list of your GitHub repos:

   [image: List of GitHub repos in the Render Dashboard]

You've successfully linked your GitHub account! Whenever you create a new service, select any available repo and click *Connect*. Then complete the remainder of the service creation flow.

## Pull request previews

Render can automatically build and deploy a preview instance of your service for every pull request that's opened against your project.

For details, see [Service previews](service-previews#pull-request-previews-git-backed).

## Git submodules

If your repo defines a `.gitmodules` file at its root, Render automatically reads it and clones all specified [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) as part of your service's build process.

> If your `.gitmodules` file includes _private_ submodules, Render can clone them only if your linked GitHub account has access to the corresponding private repository.

## Log in with GitHub

In addition to deploying projects from GitHub, you can use your GitHub account to log in to the [Render Dashboard](https://dashboard.render.com). If you have an existing Render account that matches your GitHub account's primary email address, Render logs you in to that existing account automatically.

Learn more about [managing login methods](login-settings#managing-login-methods).

## Troubleshooting

If your GitHub deploys aren't working as expected, this might be caused by misconfiguration of Render's GitHub app. For example, it might be configured for the wrong set of repositories, or a repository that was previously public might have been made private.

### Fixing GitHub app permissions

Visit [github.com/apps/render/installations/new](https://github.com/apps/render/installations/new). From here, you can install the app in a new organization or configure an existing installation:

[image: Configure GitHub]

From here, you can check the *Repository access* section to make sure your repository is included.

[image: Selecting connected GitHub repositories]

### Team-specific issues

If the creator of a Render service loses access to that service's connected GitHub repository, it can disrupt deploys for that service. You can update the Git credentials used to deploy a service from the service's *Settings* page in the [Render Dashboard](https://dashboard.render.com):

[image: Git Credentials]

Before you make this change, make sure that the new credentials have access to the service's Git repository.