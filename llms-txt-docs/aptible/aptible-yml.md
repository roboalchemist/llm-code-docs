# Source: https://www.aptible.com/docs/core-concepts/apps/deploying-apps/releases/aptible-yml.md

# .aptible.yml

In addition to [Configuration variables read by Aptible](/core-concepts/apps/deploying-apps/configuration), Aptible also lets you configure your [Apps](/core-concepts/apps/overview) through a `.aptible.yml` file.

# Location

If you are using [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git), this file must be named `.aptible.yml` and located at the root of your repository.

If you are using [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy), it must be located at `/.aptible/.aptible.yml` in your Docker image. See [Procfiles and `.aptible.yml` with Direct Docker Image Deploy](/core-concepts/apps/deploying-apps/image/deploying-with-docker-image/procfile-aptible-yml-direct-docker-deploy) for more information.

# Structure

This file should be a `yaml` file containing any of the following configuration keys:

## `before_release`

<Warning>For now, this is an alias to `before_deploy`, but should be considered deprecated. If you're still using this key, please update!</Warning>

## `before_deploy`

`before_deploy` should be set to a list, e.g.:

```yaml  theme={null}
before_deploy:
  - command1
  - command2
```

<Warning>If your Docker image has an `ENTRYPOINT`, Aptible will not use a shell to interpret your commands. Instead, the command is split according to shell rules, then simply passed to your Container's ENTRYPOINT as a series of arguments. In this case, using the form `sh -c 'command1 && command2'` or making use of a single wrapper script is required. See [How to define services](/how-to-guides/app-guides/define-services#images-with-an-entrypoint) for additional details.</Warning>

The commands listed under `before_deploy` will run when you deploy your app, either via a `git push` (for [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git)) or using [`aptible deploy`](/reference/aptible-cli/cli-commands/cli-deploy) (for [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy)). However, they will *not* run when you execute [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set), [`aptible restart`](/reference/aptible-cli/cli-commands/cli-restart), etc.

`before_deploy` commands are executed in an isolated ephemeral [Container](/core-concepts/architecture/containers/overview), before new [Release](/core-concepts/apps/deploying-apps/releases/overview) Containers are launched. The commands are executed sequentially in the order that they are listed in the file.

If any of the `before_deploy` commands fail, Release Containers will not be launched and the operation will be rolled back.

This has several key implications:

* Any side effects of your `before_deploy` commands (such as database migrations) are guaranteed to have been completed before new Containers are launched for your app.
* Any changes made to the container filesystem by a `before_deploy` command (such as installing dependencies or pre-compiling assets) will **not** be reflected in the Release Containers. You should usually include such commands in your [Dockerfile](/core-concepts/apps/deploying-apps/image/deploying-with-git/overview) instead.

As such, `before_deploy` commands are ideal for use cases such as:

* Automating database migrations
* Notifying an error tracking system that a new release is being deployed.

<Warning>There is a 30-minute timeout on `before_deploy` tasks. If you need to run something that takes longer, consider using [Ephemeral SSH Sessions](/core-concepts/apps/connecting-to-apps/ssh-sessions).</Warning>

## After Success/Failure Hooks

Aptible provides multiple hook points for you to run custom code when certain operations succeed or fail.

Like `before_deploy`, commands are executed in an isolated ephemeral [Container](/core-concepts/architecture/containers/overview). These commands are executed sequentially in the order that they are listed in the file.

**Success hooks** run after your Release Containers are launched and confirmed to be in good health. **Failure hooks** run if the operation needs to be rolled back.

<Note>Unlike `before_deploy`, command failures in these hooks do not result in the operation being rolled back.</Note>

<Warning>There is a 30-minute timeout on all hooks.</Warning>

The available hooks are:

* `after_deploy_success`
* `after_restart_success`
* `after_configure_success`
* `after_scale_success`
* `after_deploy_failure`
* `after_restart_failure`
* `after_configure_failure`
* `after_scale_failure`

As their names suggest, these hooks run during `deploy`, `restart`, `configure`, and `scale` operations.

In order to update your hooks, you must initiate a deploy with the new hooks added to your .aptible.yml.

Please note that due to their nature, **Failure hooks** are only updated after a successful deploy. This means, for example, that if you currently have an `after_deploy_failure` hook A, and are updating it to B, it will only take effect after the deploy operation completes. If the deploy operation were to fail, then the `after_deploy_failure` hook A would run, not B. In a similar vein, Failure hooks use your **previous** image to run commands, not the current image being deployed. As such, it would not have any new code available to it.
