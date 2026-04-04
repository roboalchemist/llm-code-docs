<!-- Source: https://docs.sandboxes.cloud/docs/environment-variables.md -->

# Environment variables (ENV)

This page describes how to use environment variables in Crafting sandbox for your development needs. The outline is as follows:

* [Types of environment variable definitions in sandbox](#types-of-environment-variable-definitions-in-sandbox)
  * [Built-in environment variables](#built-in-environment-variables)
  * [Sandbox-level environment variables](#sandbox-level-environment-variables)
  * [Workspace-level environment variables](#workspace-level-environment-variables)
  * [Environment variables for Repo Manifest](#environment-variables-for-repo-manifest)
  * [User-defined environment for interactive shells](#user-defined-environment-for-interactive-shells)
* [Use Secret in Environment Variables](#use-secret-in-environment-variables)
* [How do environment variables take effect](#how-do-environment-variables-take-effect)
  * [Merge of environment variables](#merge-of-environment-variables)
  * [Override environment variables at sandbox creation](#override-environment-variables-at-sandbox-creation)
  * [When changes are applied to the sandbox](#when-changes-are-applied-to-the-sandbox)
* [Admin guide for environment variables](#admin-guide-for-environment-variables)
  * [Use environment variables for service linking](#use-environment-variables-for-service-linking)
  * [Use Secret to store sensitive information which are used to stored in ENV](#use-secret-to-store-sensitive-information-which-are-used-to-stored-in-env)
  * [How to use direnv](#how-to-use-direnv)
  * [How to use dotenv package for Node.js](#how-to-use-dotenv-package-for-nodejs)

## Types of environment variable definitions in sandbox

Crafting platform supports multiple tiers of environment variables injection/customization in workspaces:

* Built-in environment variables: injected by default for all processes in the workspace;
* Sandbox-level environment variables;
* Workspace-level environment variables;
* User-defined environment for hooks, daemons, jobs in each [checkout](https://docs.sandboxes.cloud/docs/sandbox-definition#checkouts);
* User-defined environment for interactive shells.

#### Built-in environment variables

The following environment variables are injected into workspaces by default:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Variable
      </th>

      <th>
        Value Description
      </th>

      <th>
        Value Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `SANDBOX_SYSTEM_URL`
      </td>

      <td>
        The base URL to access the {user.productName} system. The URL is `<https://sandboxes.cloud`.>
      </td>

      <td>
        `https://sandboxes.cloud`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_SYSTEM_DOMAIN`
      </td>

      <td>
        The domain part of `SANDBOX_SYSTEM_URL`
      </td>

      <td>
        `sandboxes.cloud`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_SYSTEM_DNS_SUFFIX`
      </td>

      <td>
        The suffix for constructing DNS names after `SANDBOX_SYSTEM_DOMAIN`
      </td>

      <td>
        `.sandboxes.cloud`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_ORG`
      </td>

      <td>
        The name of the current organization.
      </td>

      <td>
        `crafting`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_ORG_ID`
      </td>

      <td>
        The ID of the current organization.
      </td>

      <td />
    </tr>

    <tr>
      <td>
        `SANDBOX_NAME`
      </td>

      <td>
        The name of the current Sandbox.
      </td>

      <td>
        `mysandbox`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_ID`
      </td>

      <td>
        The ID of the current Sandbox.
      </td>

      <td />
    </tr>

    <tr>
      <td>
        `SANDBOX_APP`
      </td>

      <td>
        The name of the Template that the Sandbox is created from. It's only available when the Sandbox is created from a Template.
      </td>

      <td>
        `crafting-backend-dev`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_WORKSPACE`
      </td>

      <td>
        The name of the current workspace.
      </td>

      <td>
        `api`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_OWNER_ID`
      </td>

      <td>
        The ID of the Sandbox owner, if available.
      </td>

      <td />
    </tr>

    <tr>
      <td>
        `SANDBOX_OWNER_EMAIL`
      </td>

      <td>
        The email of the Sandbox owner, if available.
      </td>

      <td>
        `demo@crafting.dev`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_OWNER_NAME`
      </td>

      <td>
        The display name of the Sandbox owner, if available.
      </td>

      <td />
    </tr>

    <tr>
      <td>
        `SANDBOX_APP_DOMAIN`
      </td>

      <td>
        The Internet facing DNS domain of the Sandbox. Often, it has the format `${SANDBOX_NAME}-${SANDBOX_ORG}.sandboxes.run`
      </td>

      <td>
        `mysandbox-org.sandboxes.run`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_ENDPOINT_DNS_SUFFIX`
      </td>

      <td>
        The suffix for Internet facing DNS names of endpoints. The complete DNS name of an endpoint can be constructed using `${ENDPOINT_NAME}${SANDBOX_ENDPOINT_DNS_SUFFIX}`
      </td>

      <td>
        `--mysandbox-org.sandboxes.run`
      </td>
    </tr>

    <tr>
      <td>
        `SANDBOX_JOB_ID`
      </td>

      <td>
        The job ID, if the sandbox is created for a job
      </td>

      <td />
    </tr>

    <tr>
      <td>
        `SANDBOX_JOB_EXEC_ID`
      </td>

      <td>
        The job execution ID, if the sandbox is created for a job
      </td>

      <td />
    </tr>

    <tr>
      <td>
        `SANDBOX_POOL_ID`
      </td>

      <td>
        The sandbox Pool ID if the sandbox is currently in the pool
      </td>

      <td />
    </tr>

    <tr>
      <td>
        `__SERVICE_HOST`\
        `__SERVICE_PORT`\
        `*_SERVICE_PORT_<port-name>`
      </td>

      <td>
        Service linking environment variables. See [Use environment variables for service linking](#use-environment-variables-for-service-linking) below.
      </td>

      <td>
        `MYSQL_SERVICE_HOST=mysql`\
        `MYSQL_SERVICE_PORT=3306`\
        `MYSQL_SERVICE_PORT_MYSQL=3306`
      </td>
    </tr>
  </tbody>
</Table>

The built-in environment variables can be used by the code running in the sandbox to choose to use specific config for the sandbox environment.

#### Sandbox-level environment variables

These environment variables are defined in Template as part of [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition) and apply to all the workspaces in the sandbox, affecting shell, IDE, hooks, and daemons/jobs defined in [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest). They are defined in the top-level `env` section in [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition):

```yaml
# These environment variables applies to all workspaces.
env:
- DEV_ENV=development
- APP_URL=https://app${SANDBOX_ENDPOINT_DNS_SUFFIX}  # Expansion is supported
```

#### Workspace-level environment variables

Environment variables can be defined in the `env` section of a workspace in in [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition), which only applies to the workspace. For example:

```yaml
# These environment variables applies to all workspaces.
env:
- DEV_ENV=development
- APP_URL=https://app${SANDBOX_ENDPOINT_DNS_SUFFIX}  # Expansion is supported
workspaces:
- name: frontend
  # These environment variables applies to the workspace only
  env:
  - EXTERNAL_URL=${APP_URL}
```

#### Environment variables for Repo Manifest

[Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest) defines hook scripts, daemons, and jobs per [checkout](https://docs.sandboxes.cloud/docs/sandbox-definition#checkouts). In the manifest, environment variables can be defined to be shared by all hook scripts, daemons, and jobs or for individual commands/scripts. Environment variable expansion is supported in both cases.

Here's an example:

```yaml
env: # Environment variables shared by all hooks, daemons and jobs.
- EXTERNAL_ENDPOINT_NAME=app
- EXTERNAL_URL=https://${EXTERNAL_ENDPOINT_NAME}${SANDBOX_ENDPOINT_DNS_SUFFIX}

hooks:
  build:
    cmd: |
      ./scripts/build.sh
      ./scripts/seed-db.sh
    env:
    - 'DB_SERVER_ADDR=${DB_SERVICE_HOST}:${DB_SERVICE_PORT}'
    - 'APP_URL=${EXTERNAL_URL}'

daemons:
  server:
    run:
      cmd: './scripts/server.sh --app-url=${EXTERNAL_URL}'

jobs:
  post:
    run: 
      cmd: './scripts/post.sh $EXTERNAL_URL'
    schedule: "*/10 * * * *"
```

The `env` section on the top defines the environment variables shared by all the commands defined in the manifest. See [Shared Environment](https://docs.sandboxes.cloud/docs/repo-manifest#shared-environment) for more details. `hooks.build.env` defines the environment variables used by the `build` hook only. See [Run Schema](https://docs.sandboxes.cloud/docs/repo-manifest#run-schema) for more details.

**Note:** The environment variables defined in the [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest) are *ONLY* effective for the commands defined in the manifest. I.e., they are not present in interactive shells such as SSH session or Web IDE session. **For that reason, we recommend to use[Workspace-level environment variables](#workspace-level-environment-variables) in most cases if possible**.

#### Environments in Shell Scripts

> 🚧 Environments Undefined in Shell Scripts
>
> As a common problem, an environment is well-defined when using SSH to access my workspace, but this environment is undefined in my post-checkout, build scripts, neither in the daemon scripts.

Most likely, this is caused by the default `.bashrc` file in the base snapshot which is built from commonly used Linux distributions (like Ubuntu). The file contains the following at the beginning:

```shell Shell
# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *)
        return
        ;;
esac
```

When using SSH, the bash runs in *interactive* mode (unless given special flags), and thus the whole `.bashrc` file is loaded as expected. However, most of the automation/background scripts (like post-checkout, build hooks, daemons etc) ran by bash in *non-interactive* mode, as a result, the content in the `.bashrc` file is skipped by the a few lines described above. As the installation procedure of many tools are appending environment variables (like `PATH`) to `.bashrc`, they are *NOT* effective in background scripts, but works normally in SSH sessions.

**Suggestions**

* Explicitly define important environment variables in the Template or Sandbox definition, at sandbox-level, workspace-level or in the [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest);
* Craft your own `.bashrc` file in the base snapshot `/etc/skel/.bashrc` or `/etc/skel.sandbox/.bashrc` to make it consistent between *interactive* and *non-interactive* modes.

### Use Secret in Environment Variables

The content of a *shared* secret can be extracted into the value of an environment, with prefixing and suffixing whitespaces trimmed. For example:

```yaml
env:
- MY_APP_KEY=key:${secret:app-key}
```

The form `${secret:SECRET-NAME}` can be used to extract the content of the secret into the value. Only organizational secret can be referenced.

### How do environment variables take effect

#### Merge of environment variables

Environment variables are defined in different places for different scopes, and they are merged to generate the final set of environment variables in the following order:

* Built-in environment variables
* Sandbox-level environment variables
* Workspace-level environment variables
* For hooks, daemons, and jobs in Repo manifest only
  * Env defined in top-level `env` section of repo manifest
  * Env defined per hook/daemon/job

The expansion is evaluated immediately when an environment variable is appended to the merging process. Given the following example of a Sandbox Definition:

```yaml
# These environment variables applies to all workspaces.
env:
- DEV_ENV=development
- APP_URL=https://app${SANDBOX_ENDPOINT_DNS_SUFFIX}  # Expansion is supported
workspaces:
- name: frontend
  # These environment variables applies to the workspace only
  env:
  - EXTERNAL_URL=${APP_URL}
  - APP_URL=https://test
```

The final environment variables in a shell of the `frontend` workspace contains (built-in environment variables not listed here):

```shell
DEV_ENV=development
EXTERNAL_URL=https://app--mysandbox-org.sandboxes.run
APP_URL=https://test
```

When `EXTERNAL_URL` is appended, expansion is evaluated immediately, and at that time, `APP_URL` is `<https://app--mysandbox-org.sandboxes.run`>.\
The last `APP_URL=<https://test`> overrides the existing `APP_URL`.

#### Override environment variables at sandbox creation

At sandbox creation time, the creator can further adjust environment variable setting for the sandbox. As shown above, the create can add more ENV definitions to sandbox-level and workspace level.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/c5b6065-guide_create_customize_env.jpg" />

Here, new ENV definitions can be appended at the bottom of existing definitions from the template. The new ENV definitions can expand from the existing definitions, and can re-define the ENV already in the existing definitions.

#### When changes are applied to the sandbox

The environment variables defined above are effective once the workspace is created in a sandbox. However, there may be further changes on the sandbox after creation (e.g. synchronized from a changed Template). Moreover, the change may cause differences in environment variables (e.g. adding workspaces/dependencies affects service linking environment variables, adding/removing packages affects `PATH`). The new changes won't be populated to all existing processes, including WebIDE servers and VS Code remote servers if they are running.\
New processes after the change will pick up new values. Change of [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest) is only effective the next time a command is executed. The running daemons stay with the old environment. Use `cs restart` to restart daemons to use the new environment.

### Admin guide for environment variables

Following best practices are suggestions to team admins for manage environment variables in their team's development environments. They are advanced topics, some of which require further setup in the Template. See [Setup Templates for Dev Environments](https://docs.sandboxes.cloud/docs/templates-setup)

> 🚧 Do not quote values in YAML
>
> When defining environment in sandbox definition, repo manifest etc. Do not put quotes around the value, otherwise the quotes become part of the value.

#### Use environment variables for service linking

*Service linking* (aka *service injection*) is one of the standard service discovery mechanisms that works by injecting environment variables into the container where the service runs in order to discover and communicate with other services. The environment variable name is constructed using the following rules:

* `<service-name>_SERVICE_HOST` specifies the address or hostname of the service.
* `<service-name>_SERVICE_PORT` specifies the port number of the default port of the service (the first exposed port according to [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition)).
* `<service-name>_SERVICE_PORT_<port-name>`: specifies the port number of each exposed port.
* Dashes `-` in `<service-name>` and `<port-name>` are converted to underscores `_`.

Take the below example  [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition):

```yaml
workspaces:
- name: frontend
  ports:
  - name: http
    port: 3000
    protocol: HTTP/TCP
- name: backend
  ports:
  - name: api
    port: 8080
    protocol: HTTP/TCP
  - name: metrics
    port: 9090
    protocol: HTTP/TCP
dependencies:
- name: db
  service_type: mysql
- name: redis
  service_type: redis
```

It will inject the following environment variables in each workspace (both `frontend` and `backend`):

* `FRONTEND_SERVICE_HOST=frontend`
* `FRONTEND_SERVICE_PORT=3000`
* `FRONTEND_SERVICE_PORT_HTTP=3000`
* `BACKEND_SERVICE_HOST=backend`
* `BACKEND_SERVICE_PORT=8080`
* `BACKEND_SERVICE_PORT_API=8080`
* `BACKEND_SERVICE_PORT_METRICS=9090`
* `DB_SERVICE_HOST=db`
* `DB_SERVICE_PORT=3306`
* `DB_SERVICE_PORT_MYSQL=3306`
* `REDIS_SERVICE_HOST=redis`
* `REDIS_SERVICE_PORT=6379`
* `REDIS_SERVICE_PORT_REDIS=6379`

#### Use Secret to store sensitive information which are used to stored in ENV

To conveniently provide environment overrides with sensitive information, place a simple shell script, assigning environment variables into a secret.

For example, to create a secret `db-env` that contains a script defining database access credentials:

```shell
cat <<EOF | cs secret create --shared db-env -f -
export DB_USERNAME=demouser
export DB_PASSWORD='!@#$%^7890'
EOF
```

Append the following line to `~/.bashrc` to load the environment variables:

```shell
. /var/run/sandbox/fs/secrets/shared/db-env
```

Add `.bashrc` to `~/.snapshot/includes.txt` and create a Home Snapshot using `cs snapshot create --home NAME`. Then use this Snapshot in the [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition) for this workspace.

For more information regarding `Secret`, please see [Secrets for storing dev credentials](https://docs.sandboxes.cloud/docs/secrets)

#### How to use direnv

[`direnv`](https://direnv.net) is a powerful tool for terminal users. It intercepts the `cd` command (changing current directory) and updates the current environment variables accordingly if the new *cwd* (current working directory) or its ancestor contains a `.envrc` file. Follow the steps below as an example to setup `direnv` in a workspace:

1. Install `direnv` to the root file system of the workspace (e.g. in `/usr/local/bin`, according to the [document](https://direnv.net/docs/installation.html)).
2. Create a config file `~/.config/direnv/config.toml` with the following content to trust all `.envrc` files under the user's home directory:

```toml
[whitelist]
prefix = [
  "/home",
]
```

3. Append `eval $(direnv hook bash)` into `~/.bashrc` to activate `direnv`.
4. Add `~/.config` and `~/.bashrc` to `~/.snapshot/includes.txt` so they will be included in a home snapshot.
5. Create Base Snapshot using `cs snapshot create NAME`.
6. Create Home Snapshot using `cs snapshot create --home NAME`.
7. Update Template to use these Snapshots for the workspace.
8. Submit `.envrc` files into code base with environment variables.

The next time a new Sandbox is created, inside a workspace, `cd` into a folder containing checked out code will automatically populate the environment variables defined in the `.envrc` file.

#### How to use dotenv package for Node.js

[`dotenv`](https://www.npmjs.com/package/dotenv) is a popular package used in many Node.js projects to populate environment variables from a `.env` file for the current Node.js application. And mostly, the `.env` file contains sensitive information. It's good practice to save the `.env` file as a secret, and load it into the project using a `post-checkout` hook:

1. Create a secret from a `.env` file:

```shell
cat <<EOF | cs secret create --shared env -f -
API_KEY=a46fg78a90eecd
API_SECRET=ZTdmNTUxMWItMTU1NC00ZDNkLWEzNjctODA3ZjA3MmY1OGJiCg==
EOF
```

2. Add to the `post-checkout` hook in [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest):

```yaml
hooks:
  post-checkout:
    cmd: |
      do something ...
      cp -f /var/run/sandbox/fs/secrets/shared/env .env # copy .env from a secret
```

### Troubleshooting

#### Remote Command Execution

This is a very common issue people ran into when running a command remotely using either `cs ssh` or `cs exec` and found some environment variables are not set. However, as they are working in an interactive SSH session, a Web Terminal or a VSCode terminal, everything works fine. The issue may also happen when a *daemon* is defined but failed to run due to missing environment variables.

This is caused by the default `~/.bashrc` template introduced in the Ubuntu or Debian images which skips the whole file in bash's non-interactive mode. This file will contain the following at the beginning:

```shell
# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
```

According to bash's document, commands run using `bash -c COMMAND` will run in non-interactive mode. Specifically, the following commands will run in non-interactive mode:

* `cs ssh COMMAND`
* `cs exec COMMAND`
* The command specified in a *daemon*

For example, when using `ruby` installed by `rbenv` or `rvm`, the environment variables are injected by adding specific lines in `~/.bashrc`, as a result, when run commands like: `cs ssh ruby myapp.rb` or `cs exec ruby myapp.rb` including in a *daemon* with command `ruby myapp.rb` may all fail with something like `ruby not found`, because the lines inserted into `~/.bashrc` is completely ignored in non-interactive bash mode.

On the contrary, when run `cs ssh` (no following command) or `cs exec`, it will just invoke `bash` which will show a prompt and run in interactive mode. As `~/.bashrc` is fully loaded, all environment variables are properly set.

Regarding the solutions, there are multiple options:

1. Force the interactive mode (only applicable with `cs exec`), like:
   1. `cs exec -u 1000 -W sandbox/workspace -- bash -i -c 'COMMAND'`
2. If the lines injected in `~/.bashrc` is simple, just add the same lines before the command;
3. If the lines injected in `~/.bashrc` is complicated:
   1. Move those lines into a separate file like `~/.env`
   2. Replace those lines in `~/.bashrc` with `. .env`
   3. Add `. .env;` before commands to run remotely, like `cs exec -- bash -c '. .env; ruby myapp.rb'`

Specifically for `cs exec`, which runs using the `root` user as default. If you need to load env from the regular `owner` user, the flag `-u 1000` must be specified.
