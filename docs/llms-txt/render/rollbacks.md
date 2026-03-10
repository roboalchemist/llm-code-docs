# Source: https://render.com/docs/rollbacks.md

# Rollbacks — Quickly revert your service to a previous deploy.

To revert undesired code changes as quickly as possible, you can *roll back* your service to a previous successful deploy. Render can reuse [build artifacts](#build-retention) from recent deploys, so rollbacks complete much faster than building a new version of your service.

## Triggering a rollback

**Dashboard**

1. In the [Render Dashboard](https://dashboard.render.com), go to your service's *Events* page.

2. In the event list, find a recent successful deploy and click *Rollback*:

   [image: Triggering a rollback in the Render Dashboard]

3. On the confirmation page, click *Rollback to this deploy*.

That's it! Render kicks off a _new_ deploy using the target deploy's build artifact.

**API**

To trigger a rollback via the Render API, use the [Roll back deploy](https://api-docs.render.com/reference/rollback-deploy) endpoint.

> *This endpoint does _not_ disable automatic deploys for the service.*
>
> This means that pushing a new commit to the service's linked branch will trigger a new deploy, which might reintroduce the undesired code change.
>
> You can disable automatic deploys for the service using the [Update service](https://api-docs.render.com/reference/update-service) endpoint. Set the `autoDeploy` parameter to `false`.

## Reenabling automatic deploys

Triggering a rollback in the Render Dashboard automatically disables [autodeploys](/deploys#automatic-git-deploys) for the service. This safeguard prevents new changes from triggering a deploy that might reintroduce the undesired code change.

After you resolve the underlying issue, you can reenable automatic deploys from your service's *Settings* page:

[image: Enabling autodeploys in the Render Dashboard]

> *Rolling back via the Render API does _not_ disable automatic deploys.*
>
> For details, see the *API* tab under [Triggering a rollback](#triggering-a-rollback).

## Build retention

Render retains a fixed number of recent build artifacts for each service, based on your [workspace plan](/pricing). You can only roll back to a particular deploy if its build artifact is still available.

## What's rolled back?

### Service-specific config

When you roll back, Render reuses certain configuration details from the target deploy you selected. Other settings use the service's _current_ configuration.

> *Rolling back does not overwrite any of your service's current configuration settings.*
>
> Render reuses the target deploy's settings _only_ for the rollback. When you next trigger a _standard_ deploy, Render uses the service's current configuration as usual.

🟢 Matches the target deploy

❌ Uses the service's current configuration

🟨 Partially matches the target deploy (details provided)

| Configuration | Matches target deploy |
| --- | --- |
| Start command | 🟢 |
| [Health check path](/deploys#health-checks) | 🟢 |
| Docker command | 🟢 |
| Registry-hosted Docker image | 🟨 [See details below.](#registry-hosted-docker-images) |
| Build artifact | 🟢 |
| Instance count | 🟢 |
| Environment variables | 🟢 |
| Environment groups | 🟨 [See details below.](#environment-groups) |
| Disks | ❌ Disks retain state between all deploys and cannot be rolled back. Separately from rolling back, you can [restore a disk snapshot](disks#disk-snapshots). |
| Instance type | ❌ If the target deploy requires a larger instance type, consider upgrading your instance type before triggering a rollback. |
| Custom domains | ❌ |
| Static site redirects and rewrites | ❌ |
| Static site headers | ❌ |

#### Registry-hosted Docker images

If your service pulls and deploys a [prebuilt Docker image](/deploying-an-image) from a container registry, the rollback uses the same image tag or digest as the target deploy.

As part of the rollback, Render pulls the image again. This has the following implications:

- If the target deploy specified its image with a tag, Render pulls the _latest_ image associated with that tag. This image might differ from the one used in the target deploy.
  - Unlike tags, digests always refer to the exact same image. Using a digest ensures that rollbacks behave more predictably.
- If the specified image is no longer available or reachable in the registry, the rollback fails.

#### Environment groups

[Environment groups](configure-environment-variables#environment-groups) enable sharing configuration across multiple services. Rolling back does _not_ modify any values in an environment group, because other services might also depend on those values.

However, rolling back might modify _which_ environment groups are applied to the service (specifically, if the target deploy used a different set of environment groups from the service's current configuration).

> *Note the following*:
>
> - Because rollbacks skip the build step, any recent changes to environment group variables are not reflected in the build artifact.
> - If the target deploy included an environment group that has since been deleted, the rollback proceeds without it.

### Platform-level config

Rolling back _does not_ revert any changes that Render has made to the underlying platform since the target deploy. For example, if Render has since updated the native runtime for your service's programming language, the rollback uses the updated runtime.