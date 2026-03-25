# Source: https://docs.portainer.io/2.33-lts/admin/registries/add.md

# Source: https://docs.portainer.io/2.33-lts/admin/environments/add.md

# Source: https://docs.portainer.io/2.33-lts/admin/user/teams/add.md

# Source: https://docs.portainer.io/2.33-lts/admin/user/add.md

# Source: https://docs.portainer.io/2.33-lts/user/edge/stacks/add.md

# Source: https://docs.portainer.io/2.33-lts/user/aci/containers/add.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/configurations/add.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/networking/ingresses/add.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/applications/add.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/namespaces/add.md

# Source: https://docs.portainer.io/2.33-lts/user/kubernetes/templates/add.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/secrets/add.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/configs/add.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/volumes/add.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/networks/add.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/containers/add.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/services/add.md

# Source: https://docs.portainer.io/2.33-lts/user/docker/stacks/add.md

# Source: https://docs.portainer.io/sts/admin/registries/add.md

# Source: https://docs.portainer.io/sts/admin/environments/add.md

# Source: https://docs.portainer.io/sts/admin/user/teams/add.md

# Source: https://docs.portainer.io/sts/admin/user/add.md

# Source: https://docs.portainer.io/sts/user/edge/stacks/add.md

# Source: https://docs.portainer.io/sts/user/aci/containers/add.md

# Source: https://docs.portainer.io/sts/user/kubernetes/configurations/add.md

# Source: https://docs.portainer.io/sts/user/kubernetes/networking/ingresses/add.md

# Source: https://docs.portainer.io/sts/user/kubernetes/applications/add.md

# Source: https://docs.portainer.io/sts/user/kubernetes/namespaces/add.md

# Source: https://docs.portainer.io/sts/user/kubernetes/templates/add.md

# Source: https://docs.portainer.io/sts/user/docker/secrets/add.md

# Source: https://docs.portainer.io/sts/user/docker/configs/add.md

# Source: https://docs.portainer.io/sts/user/docker/volumes/add.md

# Source: https://docs.portainer.io/sts/user/docker/networks/add.md

# Source: https://docs.portainer.io/sts/user/docker/containers/add.md

# Source: https://docs.portainer.io/sts/user/docker/services/add.md

# Source: https://docs.portainer.io/sts/user/docker/stacks/add.md

# Source: https://docs.portainer.io/admin/registries/add.md

# Source: https://docs.portainer.io/admin/environments/add.md

# Source: https://docs.portainer.io/admin/user/teams/add.md

# Source: https://docs.portainer.io/admin/user/add.md

# Source: https://docs.portainer.io/user/edge/stacks/add.md

# Source: https://docs.portainer.io/user/aci/containers/add.md

# Source: https://docs.portainer.io/user/kubernetes/configurations/add.md

# Source: https://docs.portainer.io/user/kubernetes/networking/ingresses/add.md

# Source: https://docs.portainer.io/user/kubernetes/applications/add.md

# Source: https://docs.portainer.io/user/kubernetes/namespaces/add.md

# Source: https://docs.portainer.io/user/kubernetes/templates/add.md

# Source: https://docs.portainer.io/user/docker/secrets/add.md

# Source: https://docs.portainer.io/user/docker/configs/add.md

# Source: https://docs.portainer.io/user/docker/volumes/add.md

# Source: https://docs.portainer.io/user/docker/networks/add.md

# Source: https://docs.portainer.io/user/docker/containers/add.md

# Source: https://docs.portainer.io/user/docker/services/add.md

# Source: https://docs.portainer.io/user/docker/stacks/add.md

# Add a new stack

There are four ways to deploy a new stack from Portainer:

| Option                                     | Overview                                                                                                                                 |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [Web editor](#option-1-web-editor)         | Use our web editor to define the services for the stack using a docker-compose format.                                                   |
| [Upload](#option-2-upload)                 | If you have a `stack.yml` file, you can upload it from your computer and use it to deploy the stack.                                     |
| [Git repository](#option-3-git-repository) | You can use a docker-compose format file hosted in a Git repository.                                                                     |
| Custom template                            | If you have created a [custom stack template](https://docs.portainer.io/user/docker/templates/custom), you can deploy using this option. |

## Option 1: Web editor

From the menu select **Stacks**, click **Add stack**, give the stack a descriptive name then select **Web editor**. Use the web editor to define the services.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/7MdJ4fT4M0Vp59kB0eTh/stacks-web-editor-new-1.gif" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
You can search within the web editor at any time by pressing `Ctrl-F` (or `Cmd-F` on Mac).
{% endhint %}

As part of the stack creation you can enable a stack webhook, allowing you to remotely trigger redeployments of the stack from your repository, for example. You can read more on this in our documentation on [stack webhooks](https://docs.portainer.io/user/docker/stacks/webhooks).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/pLr3E59z0srizFibrUUZ/2.15-docker_stack_web_editor_webhook.png" alt=""><figcaption></figcaption></figure>

As an optional step, you can also use the web editor to define environment variables. You can use these to define values in your compose file that would vary between deployments (for example, hostnames, database names, etc).

Environment variables can be set individually within Portainer or you can use **Load variables from .env file** to upload a file containing your environment variables. Environment variables you define (either individually or via a .env file) will be available to use in your compose file using an `environment` definition:

```
environment:
  MY_ENVIRONMENT_VARIABLE: ${MY_ENVIRONMENT_VARIABLE}
```

Alternatively, on Docker Standalone and Podman environments you can add `stack.env` as an `env_file` definition to add all the environment variables that you have defined individually as well as those included in an uploaded .env file:

```
env_file:
  - stack.env
```

**Note:** Using `env_file` to define a file does not work in Docker Swarm due to the lack of `env_file` support in `docker stack deploy` (used on Swarm environments to deploy your stack). On Docker Swarm, you will need to define each environment variable manually.

{% hint style="info" %}
Note the compose file is not changed when environment variables are used - this allows variables to be updated within Portainer without editing the compose file itself. You will still see the `${MY_ENVIRONMENT_VARIABLE}` style entry in the compose file.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/14GwAm1rZRurPvzhWofw/2.15-docker_stack_wed_editor_env_var.png" alt=""><figcaption></figcaption></figure>

You can also select the registries to use when deploying the stack. This is useful when your stack deploys multiple images from different registries that require authentication.

{% hint style="info" %}
By default, all configured registries are used. However, when you have multiple registries from the same provider (like multiple ghcr.io registries), Docker's authentication system may use the wrong credentials during deployment. Explicitly selecting the specific registry ensures the correct credentials are used.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/PlJ0SDdU8VTwHu8GqWRe/2.33-stacks-add-registries.png" alt=""><figcaption></figcaption></figure>

When you're ready, click **Deploy the stack**.

## Option 2: Upload

In Portainer you can create stacks from Compose YML files. To do this, from the menu select **Stacks**, click **Add stack**, then give the stack a descriptive name.

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/0bblMhqQDhzjuM9xj1ZH/stacks-upload-new.gif" alt=""><figcaption></figcaption></figure>

Select **Upload** then select the Compose file from your computer.

As part of the stack creation you can enable a stack webhook, allowing you to remotely trigger redeployments of the stack from your repository, for example. You can read more on this in our documentation on [stack webhooks](https://docs.portainer.io/user/docker/stacks/webhooks).

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/pLr3E59z0srizFibrUUZ/2.15-docker_stack_web_editor_webhook.png" alt=""><figcaption></figcaption></figure>

As an optional step, enter any environment variables. You can use these to define values in your compose file that would vary between deployments (for example, hostnames, database names, etc).

Environment variables can be set individually within Portainer or you can use **Load variables from .env file** to upload a file containing your environment variables. Environment variables you define (either individually or via a .env file) will be available to use in your compose file using an `environment` definition:

```
environment:
  MY_ENVIRONMENT_VARIABLE: ${MY_ENVIRONMENT_VARIABLE}
```

Alternatively, you can add `stack.env` as an `env_file` definition to add all the environment variables that you have defined individually as well as those included in an uploaded .env file:

```
env_file:
  - stack.env
```

{% hint style="info" %}
Note the compose file is not changed when environment variables are used - this allows variables to be updated within Portainer without editing the compose file itself which would take it out of sync with your local copy. You will still see the `${MY_ENVIRONMENT_VARIABLE}` style entry in the compose file.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/8vFUlfGYhZnH4k5mnKsE/2.15-docker_add_stack_upload_env_var.png" alt=""><figcaption></figcaption></figure>

When you're ready click **Deploy the stack**.

## Option 3: Git repository

If your Compose file is hosted in a Git repository, you can deploy from there. From the menu select **Stacks**, click **Add stack**, then give the stack a descriptive name.

{% hint style="warning" %}
When a stack is deployed from Git, Portainer will clone the entire Git repository as part of the deployment process. Ensure you have enough free space to accommodate this.
{% endhint %}

{% hint style="warning" %}
Portainer's Git deployment functionality does not currently support the use of Git submodules. If your repository includes submodules, they will not be pulled as part of the deployment. We [hope to add support](https://github.com/orgs/portainer/discussions/9767) for submodules in a future release.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/M7uZudH76f3XQzieaBmK/stacks-git-new.gif" alt=""><figcaption></figcaption></figure>

Select **Git Repository** then enter information about your Git repo.

{% hint style="info" %}
Any Git-compatible repository should work here. Substitute the details as required.
{% endhint %}

| Field/Option          | Overview                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication        | Toggle this on if your Git repository requires authentication.                                                                                                                                                                                                                                                                                                                                                                                        |
| Git Credentials       | If the **Authentication** toggle is enabled and you have configured [individual](https://docs.portainer.io/account-settings#git-credentials) or [shared](https://docs.portainer.io/admin/settings/credentials/git) Git credentials, you can select them from this dropdown. Shared Git credentials can be identified with the **Shared** tag, and are only available to administrators at present. Leave this field unset to provide new credentials. |
| Authorization type    | Select either **Basic** or **Token** authorization depending on what your Git repository requires. For example, GitHub, GitLab, and Bitbucket Cloud expect Basic Auth, even when using an API or access token.                                                                                                                                                                                                                                        |
| Username              | Enter your Git username.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Personal Access Token | Enter your personal access token or password.                                                                                                                                                                                                                                                                                                                                                                                                         |
| Save credential       | Check this option to save the credentials entered above for future use under the name provided in the **credential name** field.                                                                                                                                                                                                                                                                                                                      |

{% hint style="info" %}
If you have 2FA configured in GitHub, your passcode is your password.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/z3uZr2HPDfrpLSuIWKjh/2.35-stacks-add-git-auth.png" alt=""><figcaption></figcaption></figure>

| Field/Option          | Overview                                                                                                                                                                                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Repository URL        | Enter the repository URL. If you have enabled Authentication above the credentials will be used to access the repository. The below options will be populated by what is found in the repository.                                                                                    |
| Skip TLS verification | Toggle this on to skip the verification of TLS certificates used by your repository. This is useful if your repo uses a self-signed certificate.                                                                                                                                     |
| Repository reference  | Select the reference to use when deploying the stack (for example, the branch).                                                                                                                                                                                                      |
| Compose path          | Enter the path to the Compose file from the root of the repository.                                                                                                                                                                                                                  |
| Additional paths      | Click **Add file** to add additional YAML files to be parsed by the build. This is the equivalent of passing multiple `-f` options to `docker compose`, and abides by the same [merging rules](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/#merging-rules). |
| GitOps updates        | Toggle this on to enable GitOps updates (see below).                                                                                                                                                                                                                                 |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/p1fPRx3nprvXwuIYK8Mh/2.24.0-docker-stacks-add-git.png" alt=""><figcaption></figcaption></figure>

### GitOps updates

Portainer supports automatically updating your stacks deployed from Git repositories. To enable this, toggle on **GitOps updates** and configure your settings.

{% hint style="info" %}
For more detail on how GitOps updates function under the hood, have a look at [this article](https://docs.portainer.io/faqs/troubleshooting/stacks-deployments-and-updates/how-do-automatic-updates-for-stacks-applications-work).
{% endhint %}

| Field/Option   | Overview                                                                                                                                                                                                                                                                            |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mechanism      | Select the method to use when checking for updates:                                                                                                                                                                                                                                 |
|                | <p><strong>Polling:</strong> Periodically poll the Git repository from Portainer to check for updates to the repository.</p><p><strong>Webhook:</strong> Generate a webhook URL to add to your Git repository to trigger the update on demand (for example via GitHub actions).</p> |
| Fetch interval | If **Polling** is selected, how often Portainer will check the Git repository for updates.                                                                                                                                                                                          |
| Webhook        | When **Webhook** is selected, displays the webhook URL to use in your integration. Click **Copy link** to copy the webhook URL to the clipboard.                                                                                                                                    |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/4AskPw1azRdJMQevX1Sy/2.19-stacks-add-git-polling.png" alt=""><figcaption><p>Automatic updates when using polling</p></figcaption></figure>

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/iz1J1LKHTL8WcUueJwT6/2.19-stacks-add-git-webhook.png" alt=""><figcaption><p>Automatic updates when using webhooks</p></figcaption></figure>

| Field/Option       | Overview                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Re-pull image      | <p>Enable this setting to always pull the most recent version of container images when updating the stack. This is equivalent to the <code>--pull=always</code> flag for <code>docker run</code>.<br>This option was previously labeled as <strong>Pull latest image</strong>.</p>                                                                                                                                                                                                                                                                          |
| Force redeployment | <p>Enable this setting to force the redeployment of your stack at the specified interval (or when the webhook is triggered), overwriting any changes that have been made in the local environment, even if there has been no update to the stack in Git. This is useful if you want to ensure that your Git repository is the source of truth for your stacks and are happy with the local stack being replaced.</p><p>If this option is left disabled, automatic updates will only trigger if Portainer detects a change in the remote Git repository.</p> |

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/cPBjSqEdNk4iNExL5Ok5/2.19-stacks-add-git-repull-force.png" alt=""><figcaption></figcaption></figure>

### Relative path volumes

When you toggle **Enable relative path volumes** to on, you are able to specify relative path references in your compose files. Portainer will create the required directory structure and populate the directories with the relevant files from your Git repository.

{% hint style="info" %}
This feature is only available in Portainer Business Edition.
{% endhint %}

On Docker Standalone and Podman environments, specify the path at which you want your files to be created on your host filesystem in the **Local filesystem path** field.

{% hint style="warning" %}
Ensure this directory exists on your local filesystem and is writable.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/AvFdROnyXcwKinZwbtlE/2.17-stacks-add-relativepath.png" alt=""><figcaption></figcaption></figure>

On Docker Swarm environments, specify the path at which you want your files to be created in the Network filesystem path field.

{% hint style="warning" %}
Ensure that this path is available on all of your Docker Swarm nodes and is writable.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/CQ7KAftn6X855td2LoF7/2.17-stacks-add-relativepath-swarm.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
For more detail on how this feature works, have a look at [this article](https://docs.portainer.io/advanced/relative-paths).
{% endhint %}

### Environment variables

As an optional step, you can also set environment variables. You can use these to define values in your compose file that would vary between deployments (for example, hostnames, database names, etc).

Environment variables can be set individually within Portainer or you can use **Load variables from .env file** to upload a file containing your environment variables. Environment variables you define (either individually or via a .env file) will be available to use in your compose file using an `environment` definition:

```
environment:
  MY_ENVIRONMENT_VARIABLE: ${MY_ENVIRONMENT_VARIABLE}
```

Alternatively, you can add `stack.env` as an `env_file` definition to add all the environment variables that you have defined individually as well as those included in an uploaded .env file:

```
env_file:
  - stack.env
```

{% hint style="info" %}
Note the compose file is not changed when environment variables are used - this allows variables to be updated within Portainer without editing the compose file itself which would take it out of sync with the Git repository. You will still see the `${MY_ENVIRONMENT_VARIABLE}` style entry in the compose file.
{% endhint %}

<figure><img src="https://content.gitbook.com/content/xdTQRpMuktD2l0URtOJO/blobs/14GwAm1rZRurPvzhWofw/2.15-docker_stack_wed_editor_env_var.png" alt=""><figcaption></figcaption></figure>

Enter environment variables if required then click **Deploy the stack**.
