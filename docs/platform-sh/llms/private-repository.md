# Source: https://docs.upsun.com/development/private-repository.md

# Pull code from a private Git repository

To complete its build, your Upsun project may need to access pieces of code stored in private Git repositories.
Examples include themes, libraries, and modules.
Configure these repositories to grant access to your project.

To grant access to a private Git repository,
add the project's public SSH key to your Git repository's deploy keys.

## 1. Get your project's public key

1. In the Console, open the project you want.
2. Click **Settings Settings**.
3. Under **Project settings**, click **Deploy key**.
4. Click ** Copy**.

![Deploy Key](https://docs.upsun.com/images/management-console/settings-deploy-key.png "0.5")

## 2. Add the key to your repository in your Git provider

* [GitHub deploy key](https://docs.github.com/en/developers/overview/managing-deploy-keys#deploy-keys)
* [GitLab deploy key](https://docs.gitlab.com/ee/user/project/deploy_keys/#grant-project-access-to-a-public-deploy-key)
* [Bitbucket access key](https://support.atlassian.com/bitbucket-cloud/docs/configure-repository-settings/)

If you're only pulling code, the key doesn't need write permissions.

Now your Upsun project can access your private repository via SSH, including to add dependencies.

This means you can access the private repository through links like:
``git@<GIT_PROVIDER>:<PATH_OR_USERNAME>/<REPOSITORY>.git``.
For example, you can clone a repository in your [`build` hook](https://docs.upsun.com../create-apps/hooks/_index.md):

```yaml  {location=".upsun/config.yaml"}
applications:
  <APP_NAME>:
    hooks:
      build: |
        set -e
        git clone git@bitbucket.org:username/module.git
```

You can also use [private repositories as submodules](https://docs.upsun.com/development/submodules.md#use-private-git-repositories).

## Using multiple private GitHub repositories

GitHub requires a separate deploy key for each repository.
To grant your project access to multiple repositories, create an automated user account, known as a machine user, with its own SSH key.

You can then add the machine account as collaborator to specific repositories
or to a team with access to the repositories.

See more information about [machine users on GitHub](https://docs.github.com/en/developers/overview/managing-deploy-keys#machine-users).

