# Source: https://www.aptible.com/docs/how-to-guides/app-guides/deploy-from-git.md

# How to deploy from Git

> Guide for deploying from Git using Dockerfile Deploy

## **Overview**

With Aptible, you have the option to deploy your code directly from Git using [Dockerfile Deploy](/how-to-guides/app-guides/deploy-from-git). This method involves pushing your source code, including a Dockerfile, to Aptible's Git repository. Aptible will then create a Docker image for you, simplifying the deployment process. This guide will walk you through the steps of using Dockerfile Deploy to deploy your code from Git to Aptible.

## Deploying via the Dashboard

The easiest way to deploy with Dockerfile Deploy within the Aptible Dashboard is by deploying a [template](/getting-started/deploy-starter-template/overview) or [custom code](/getting-started/deploy-custom-code) using the Deploy tool.

## Deploying via the CLI

> ⚠️ Prerequisites: Install the [Aptible CLI](/reference/aptible-cli/cli-commands/overview)

**Step 1: Create an app**

Use the `aptible apps:create` to create an [app](/core-concepts/apps/overview). Note the provided Git Remote. As we advance in this article, we'll refer to it as `$GIT_URL`.

**Step 2: Create a git repository on your local workstation**

Example:

```pl  theme={null}
git init test-dockerfile-deploy
cd test-dockerfile-deploy
```

**Step 3: Add your** [**Dockerfile**](/core-concepts/apps/deploying-apps/image/deploying-with-git/overview) **in the root of the repository**

Example:

```pl  theme={null}
# Declare a base image:
FROM httpd:alpine

# Tell Aptible this app will be accessible over port 80:
EXPOSE 80

# Tell Aptible to run "httpd -f" to start this app:
CMD ["httpd", "-f"]
```

Step 4: Deploy to Aptible:

```pl  theme={null}
# Commit the Dockerfile
git add Dockerfile
git commit -m "Add a Dockerfile"

# This URL is available in the Aptible Dashboard under "Git Remote".
# You got it after creating your app.
git remote add aptible "$GIT_URL"

# Push to Aptible
git push aptible master
```

## Deploying via Terraform

Dockerfile Deploy is not supported by Terraform. Use [Direct Docker Image Deploy](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy) with Terraform instead.
