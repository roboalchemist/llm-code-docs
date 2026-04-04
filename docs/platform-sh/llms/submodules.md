# Source: https://docs.upsun.com/development/submodules.md

# Use Git submodules

## Clone submodules during deployment

Upsun allows you to use submodules in your Git repository.
They're usually listed in a `.gitmodules` file at the root of your Git repository.
When you push via Git, Upsun tries to clone them automatically.

Say you have a multi-app project that includes the following submodules:

 - A BigFoot app
 - An API Platform v3, Admin component
 - A Gatsby frontend
 - A Mercure Rocks server

To import all the submodules, run the following commands from your multiple application project's root folder:

```bash
touch .gitmodules
git submodule add --name admin https://github.com/platformsh-templates/bigfoot-multiapp-admin.git admin
git submodule add --name api https://github.com/platformsh-templates/bigfoot-multiapp-api.git api
git submodule add --name gatsby https://github.com/platformsh-templates/bigfoot-multiapp-gatsby.git gatsby
git submodule add --name mercure https://github.com/platformsh-templates/bigfoot-multiapp-mercure.git mercure
git add .
git commit -m "Adding submodules for Bigfoot App, API Platform Admin, Gatsby frontend and Mercure Rocks server"
git push
```

Here is an example of a `.gitmodules` file:

```ini
[submodule "admin"]
  path = admin
  url = https://github.com/platformsh-templates/bigfoot-multiapp-admin.git
[submodule "api"]
  path = api
  url = https://github.com/platformsh-templates/bigfoot-multiapp-api.git
[submodule "gatsby"]
  path = gatsby
  url = https://github.com/platformsh-templates/bigfoot-multiapp-gatsby.git
[submodule "mercure"]
  path = mercure
  url = https://github.com/platformsh-templates/bigfoot-multiapp-mercure.git
```

When you run `git push`, you can see the output of the logs:

```bash
  Validating submodules
    Updating submodule ttps://github.com/platformsh-templates/bigfoot-multiapp-admin.git
    Updated submodule https://github.com/platformsh-templates/bigfoot-multiapp-admin.git: 549 references updated.
    Updating submodule ttps://github.com/platformsh-templates/bigfoot-multiapp-api.git
    Updated submodule https://github.com/platformsh-templates/bigfoot-multiapp-api.git: 898 references updated.
    Updating submodule https://github.com/platformsh-templates/bigfoot-multiapp-gatsby.git
    Updated submodule https://github.com/platformsh-templates/bigfoot-multiapp-gatsby.git: 257 references updated.
    Updating submodule https://github.com/platformsh-templates/bigfoot-multiapp-mercure.git
    Updated submodule https://github.com/platformsh-templates/bigfoot-multiapp-mercure.git: 124 references updated.
  ...
```

**Note**: 

If your submodule contains an independent app,
see [how to configure it properly](https://docs.upsun.com/create-apps/multi-app/project-structure.md#split-your-code-source-into-multiple-git-submodule-repositories).

## Update submodules

**Note**: 

To specify which submodule needs to be updated, replace ``[submodule]`` with your submodule path.

**Note**: 

Deploy keys only grant access to a single repository,
which can cause issues when attempting to pull several repositories to the same server.
If your server needs access to multiple repositories, follow these steps:

 - [Create a machine user](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#machine-users)
with access rights to each of the private repositories.
 - Attach the deploy key to your machine user.

## Removing submodules

These steps aren't specific to Upsun, but kept as a reference for Git so that submodules are effectively removed before entering the build process.

1. In your `.gitmodules` and `.git/config` files, delete the information related to the submodule you want to remove.

   ```bash
   git submodule deinit -f path_to_submodule
   ```

2. Stage changes to `.gitmodules`:

    ```bash
    git add .gitmodules
    ```
3. Remove the submodule from the repository (without trailing slash):

    ```bash
    git rm --cached path_to_submodule
    ```

4. Remove the submodule files in `.git` from the repository  (without trailing slash):

    ```bash
    rm -rf .git/modules/path_to_submodule
    ```

5. Commit the changes:

    ```bash
    git commit -m "Removed submodule."
    ```

6. Remove the submodule code locally, now no longer tracked:

    ```bash
    rm -rf path_to_submodule
    ```

