# Source: https://render.com/docs/gitlab.md

# Connect GitLab

Render connects with GitLab to deploy your apps and websites automatically on every push to your project. You can connect all your public and private projects on [gitlab.com](https://gitlab.com) to Render and use the *Render for GitLab* integration to create web services, static sites, background workers and more.

You can also use *Render for GitLab* to automatically create Merge Request Preview URLs for your web apps and static sites.

## Setup

1. When you create your first service in the [Render Dashboard](https://dashboard.render.com), you're prompted to connect your Git provider:

   [image: Git Connect]

2. Click *GitLab*. This redirects you to [gitlab.com](https://gitlab.com), where you can authorize Render to access your repositories.

3. You're then redirected back to the Render Dashboard, which now displays a list of your GitLab repos.

You've successfully linked your GitLab account! Whenever you create a new service, select any available repo and click *Connect*. Then complete the remainder of the service creation flow.

> Your GitLab account must have at least *Maintainer* or *Owner* permissions on a project to enable [automatic deploys](/deploys#auto-deploys) for it.

## Merge Request Previews

Render can automatically build and deploy GitLab merge requests if [pull request previews](service-previews) are enabled for your web service. Once enabled, you will see a comment from *Render for GitLab* when your merge request is created. It should look similar to this:

[image: GitLab Merge Request Comment]

Render creates a unique URL for every merge request and builds and deploys the latest changes as they're pushed to the MR. MR servers are automatically deleted when the corresponding MR is merged or closed.

## Git Submodules

Render will read a `.gitmodules` file at the root of your repo and automatically clone all [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) defined in it.

Private submodules are cloned if they are owned by the same GitLab account as the base repository.

## Log in with GitLab

In addition to using GitLab projects to deploy apps, you can also use your [gitlab.com](https://gitlab.com) account to sign up for Render and for subsequent logins. If you already have an account on Render that matches your primary GitLab email, you will be logged into the existing account automatically.

Learn more about [managing login methods](login-settings#managing-login-methods).