# Source: https://www.aptible.com/docs/how-to-guides/app-guides/deploying-docker-image-to-git.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to migrate from deploying via Docker Image to deploying via Git

> Guide for migrating from deploying via Docker Image to deploying via Git

## Overview

Suppose you configured your app to [deploy via Docker Image](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy), i.e., you deployed using [`aptible deploy`](/reference/aptible-cli/cli-commands/cli-deploy) in the past, and you want to switch to [deploying via Git](/how-to-guides/app-guides/deploy-from-git) instead. In that case, you will need to take the following steps:

**Step 1:** Push your git repository to a temporary branch. This action will not trigger a deploy, but we'll use it in just a moment:

```perl  theme={null}
BRANCH="deploy-$(date "+%s")"
git push aptible "master:$BRANCH"
```

**Step 2:** Deploy the temporary branch (using the `--git-commitish` argument), and use an empty string for the `--docker-image` argument to disable deploying via Docker Image.

```perl  theme={null}
aptible deploy --app "$APP_HANDLE" \
        --git-commitish "$BRANCH" \
        --docker-image ""
```

**Step 3:** Use `git push aptible master` for all deploys moving forward.

Please note if your [app](/core-concepts/apps/overview) has [Private Registry Credentials](/core-concepts/apps/overview), Aptible will attempt to log in using these credentials. Unless the app uses a private base image in its Dockerfile, these credentials should not be necessary. To prevent private registry authentication, unset the credentials when deploying:

```perl  theme={null}
aptible deploy --app "$APP_HANDLE" \
        --git-commitish "$BRANCH" \
        --docker-image "" \
        --private-registry-username "" \
        --private-registry-password ""
```

Congratulations! You are now set to deploy via Git.
