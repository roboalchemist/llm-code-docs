# Source: https://trigger.dev/docs/github-integration.md

# GitHub integration

> Automatically deploy your tasks on every push to your GitHub repository.

## How it works

Once you connect a GitHub repository to your project, you can configure tracking branches for the production and staging environments.
Every push to a tracked branch creates a deployment in the corresponding environment. Preview branch deployments are also supported for pull requests.

This eliminates the need to manually run the `trigger.dev deploy` command or set up custom CI/CD workflows.

## Setup

<Steps>
  <Step title="Install our GitHub app">
    Go to your project's settings page and click `Install GitHub app`.
    This will take you to GitHub to authorize the Trigger.dev app for your organization or personal account.
  </Step>

  <Step title="Connect your repository">
    Select a repository to connect to your project.
  </Step>

  <Step title="Configure branch tracking">
    Choose which branches should trigger automatic deployments:

    * **Production**: The branch that deploys to your production environment, e.g., `main`.
    * **Staging**: The branch that deploys to your staging environment.
    * **Preview**: Toggle to enable preview deployments for pull requests
  </Step>

  <Step title="Customize build settings (optional)">
    Configure how your project is built:

    * **Trigger config file**: Path to your `trigger.config.ts` file. By default, we look for it in the root of your repository. The path should be relative to the root of your repository and contain the config file name, e.g., `apps/tasks/trigger.config.ts`.
    * **Install command**: Auto-detected by default, but you can override it if necessary. The command will be run from the root of your repository.
    * **Pre-build command**: Run any commands before building and deploying your project, e.g., `pnpm run prisma:generate`. The command will be run from the root of your repository.
  </Step>
</Steps>

## Branch tracking

Our GitHub integration uses branch tracking to determine when and where to deploy your code.

<img src="https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/git-settings.png?fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=22539316605344f0d461e9132b365161" alt="Trigger.dev project git settings" data-og-width="2128" width="2128" data-og-height="1312" height="1312" data-path="deployment/git-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/git-settings.png?w=280&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=d6e36be08415a61faffca2d42a4f581f 280w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/git-settings.png?w=560&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=56da45f1ba051ae3849c01f1752b3bc8 560w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/git-settings.png?w=840&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=f72bcc7fa00d560bcafec619b1fc987a 840w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/git-settings.png?w=1100&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=984cc0145d10478fa1e4e9383a28be9d 1100w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/git-settings.png?w=1650&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=271094babe4404695f896005a11e9ba9 1650w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/git-settings.png?w=2500&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=46c3892badd5efd5dd1ff6da7bae4e0b 2500w" />

### Production and staging branches

When you connect a repository, the default branch of your repository will be used as the production tracking branch, by default.

When you configure a production or staging branch, every push to that branch will trigger a deployment.
Our build server will install the project dependencies, build your project, and deploy it to the corresponding environment.

If there are multiple consecutive pushes to a tracked branch, the later deployments will be queued until the previous deployment completes.

<Note>
  When you connect a repository, the default branch of your repository will be used as the production tracking branch by default.
  You can change this in the git settings of your project.
</Note>

### Pull requests

By default, pull requests will be deployed to preview branch environments, enabling you to test changes before merging.
When the pull request is merged or closed, the preview branch is automatically archived.

The name of the preview branch matches the branch name of the pull request.

<Note>
  Preview branch deployments require the preview environment to be enabled on your project. Learn more about [preview branches](/deployment/preview-branches).
</Note>

## Disconnecting a repository

You can disconnect a repository at any time from your project git settings. This will stop automatic deployments triggered from GitHub.

## Managing repository access

To add or remove repository access for the Trigger.dev GitHub app, follow the link in the `Connect GitHub repository` modal:

<img src="https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/connect-repo.png?fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=60a5382c08d707000e907b292242f388" alt="Trigger.dev prompt to connect a GitHub repository" data-og-width="2128" width="2128" data-og-height="1312" height="1312" data-path="deployment/connect-repo.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/connect-repo.png?w=280&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=8f66d138ecf9cc56a8ff97d9e484d40f 280w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/connect-repo.png?w=560&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=ac67e6a07bd9e132609c66480b843b2e 560w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/connect-repo.png?w=840&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=5a538fa4904a6fd41fbbaf36e101521f 840w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/connect-repo.png?w=1100&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=06dde82cb6f249a009cc0714dc9eaf73 1100w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/connect-repo.png?w=1650&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=1d4bfea5cfe868c25fa73ce902123470 1650w, https://mintcdn.com/trigger/rYmvd2BT_CpeAo5i/deployment/connect-repo.png?w=2500&fit=max&auto=format&n=rYmvd2BT_CpeAo5i&q=85&s=ffea2ffa393258159c1c60e2686af341 2500w" />

Alternatively, you can follow these steps on GitHub:

1. Go to your GitHub account settings
2. Navigate to **Settings** → **Applications** → **Installed GitHub Apps**
3. Click **Configure** next to `Trigger.dev App`
4. Update repository access under `Repository access`

Changes to repository access will be reflected immediately in your Trigger.dev project settings.

## Environment variables at build time

You can expose environment variables during the build and deployment process by prefixing them with `TRIGGER_BUILD_`.
In the build server, the `TRIGGER_BUILD_` prefix is stripped from the variable name, i.e., `TRIGGER_BUILD_MY_TOKEN` is exposed as `MY_TOKEN`.

Build extensions will also have access to these variables.

<Note>
  Build environment variables only apply to deployments in the environment you set them in.
</Note>

Learn more about managing [environment variables](/deploy-environment-variables).

## Using a private npm registry

If your project uses packages from a private npm registry, you can provide authentication by setting a `TRIGGER_BUILD_NPM_RC` environment variable.

The value should be the contents of your `.npmrc` file including any token credentials, encoded to base64.

### Example

Example `.npmrc` file containing credentials for a private npm registry and a GitHub package registry:

```
//registry.npmjs.org/:_authToken=<YOUR_NPM_TOKEN>
@<YOUR_NAMESPACE>:registry=https://npm.pkg.github.com
//npm.pkg.github.com/:always-auth=true
//npm.pkg.github.com/:_authToken=<YOUR_GITHUB_TOKEN>
```

Encode it to base64:

```bash  theme={null}
# Encode your .npmrc file
cat .npmrc | base64
```

Then, set the `TRIGGER_BUILD_NPM_RC` environment variable in your project settings with the encoded value.

<Note>
  The build server will automatically create a `.npmrc` file in the installation directory based on the content of the `TRIGGER_BUILD_NPM_RC` environment variable.
  This enables the build server to authenticate to your private npm registry.
</Note>
