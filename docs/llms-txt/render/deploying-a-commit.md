# Source: https://render.com/docs/deploying-a-commit.md

# Deploying a specific commit


> *Urgently need to deploy a recent build to revert an error?* See [Rollbacks](rollbacks).

By default, after you connect your [GitHub](github)/[GitLab](gitlab)/[Bitbucket](bitbucket) repository, Render automatically builds and deploys the _latest_ commit from that repository's linked branch. The same is true for your service's [previews](service-previews) and [preview environments](preview-environments).

If you ever want to deploy a _specific_ commit from your branch's history, see options below.

> *Deploying a specific commit disables [*automatic deploys*](/deploys#automatic-git-deploys) for the service.* You can reenable automatic deploys from the service's page in the [Render Dashboard](https://dashboard.render.com).
>
> If you reenable automatic deploys, Render once again automatically deploys the most recent commit for your linked branch.

## Deploying from the dashboard

To manually deploy any commit from your repository, open your service's page in the [Render Dashboard](https://dashboard.render.com) and click *Manual Deploy > Deploy a specific commit*:

[image: Deploying a specific commit in the Render Dashboard]

Select a commit in the modal that appears, then click *Deploy Commit*. Render immediately kicks off a deploy.

## Deploying via webhook

Every Render service has a [deploy hook URL](/deploy-hooks) that you can use to trigger a deploy via an HTTP request. To deploy a specific commit via this hook, include a `ref` query parameter that specifies the commit SHA to deploy:

```bash
# Full commit SHA
https://api.render.com/deploy/srv-XXYYZZ?key=AABBCC&ref=baaa339926cb474b61c1f0e6297b024eaa09ac7d

# Short commit SHA
https://api.render.com/deploy/srv-XXYYZZ?key=AABBCC&ref=baaa339
```

As shown, you can provide either a full or short commit SHA.

A `GET` or `POST` request to the hook URL returns `200 OK` if the provided commit SHA
is valid and a deploy has started. The request returns `404 Not Found` if the SHA is invalid.