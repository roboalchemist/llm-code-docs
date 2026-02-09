# Source: https://www.aptible.com/docs/how-to-guides/app-guides/synchronize-config-code-changes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to synchronize configuration and code changes

Updating the [configuration](/core-concepts/apps/deploying-apps/configuration) of your [app](/core-concepts/apps/overview) using [`aptible config:set`](/reference/aptible-cli/cli-commands/cli-config-set) then deploying your app through [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git) or [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) will deploy your app twice:

* Once to apply the [Configuration](/core-concepts/apps/deploying-apps/configuration) changes.
* Once to deploy the new [Image](/core-concepts/apps/deploying-apps/image/overview).

This process may be inconvenient when you need to update your configuration and ship new code that depends on the updated configuration **simultaneously**. To solve this problem, the Aptible CLI lets you deploy and update your app configuration as one atomic operation.

## For Dockerfile Deploy

To synchronize a Configuration change and code release when using [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git):

**Step 1:** Push your code to a new deploy branch on Aptible. Any name will do, as long as it's not `master`, but we recommend giving it a random-ish name like in the example below. Pushing to a branch other than `master` will **not** trigger a deploy on Aptible. However, the new code will be available for future deploys.

```js  theme={null}
BRANCH="deploy-$(date "+%s")"
git push aptible "master:$BRANCH"
```

**Step 2:** Deploy this branch along with the new Configuration variables using the [`aptible deploy`](/reference/aptible-cli/cli-commands/cli-deploy) command:

```js  theme={null}
aptible deploy \
  --app "$APP_HANDLE" \
  --git-commitish "$BRANCH" \
  FOO=BAR QUX=
```

Please note that you can provide some common configuration variables as arguments to CLI commands instead of updating the app configuration. For example, if you need to include [Private Registry Authentication](/core-concepts/apps/overview) credentials to let Aptible pull a source Docker image, you can use this command:

```js  theme={null}
aptible deploy \
  --app "$APP_HANDLE" \
  --git-commitish "$BRANCH" \
  --private-registry-username "$USERNAME" \
  --private-registry-password "$PASSWORD"
```

## For Direct Docker Image Deploy

Please use the [`aptible deploy`](/reference/aptible-cli/cli-commands/cli-deploy) CLI command to deploy your app if you are using [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy). If you are not using `aptible deploy`, please review the [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) instructions. When using `aptible deploy` with Direct Docker Image Deploy, you may append environment variables to the [`aptible deploy`](/reference/aptible-cli/cli-commands/cli-deploy) command:

```js  theme={null}
aptible deploy \
  --app "$APP_HANDLE" \
  --docker-image "$DOCKER_IMAGE" \
  FOO=BAR QUX=
```
