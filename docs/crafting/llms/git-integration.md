<!-- Source: https://docs.sandboxes.cloud/docs/git-integration.md -->

# Git Service Integration for Preview

In the [Git Access](https://docs.sandboxes.cloud/docs/git-access) section, we talked about how to let individual developers access git repos for their day-to-day development. Here in this section, we will talk about how to integrate Crafting further into the DevOps workflow to automatically generate preview environment based on each Pull Request. Specifically, we cover:

* [Launch a Sandbox from URL Posted to Pull Request](#launch-a-sandbox-from-url-posted-to-pull-request)
* [Launch a Sandbox Automatically as part of CI process](#launch-a-sandbox-automatically-as-part-of-ci-process)
* [Launch a Sandbox using Github Action](#launch-a-sandbox-using-github-action)

## Launch a Sandbox from URL Posted to Pull Request

A good practice with Crafting Sandbox is for the CI tool to automatically post a URL to each Pull Request. When a developer clicks such a URL, the system will launch a sandbox with the code branch referred in the Pull Request as a preview environment.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/c6677c2-use-case-preview-from-pr.JPG" />

### How to use

**It is recommend to use the[dedicated Github Action](https://github.com/marketplace/actions/sandbox-launch-action) if you only need a URL in Github PR thread**. Please proceed the below approach if the Github Action does not meet your requirement or you need a highly customised behaviour.

To do that, you can modify your CI tool to automatically post a specific URL to each Pull Request. This can be done via your internal CI automation tool (e.g. Jenkins), or by automation tools provided by git repo (e.g., Github action). Just use these tools to post a comment with a specially constructed URL for Crafting, where specific configurations can be put into HTTP query parameters.

Below is an example where the sandbox is provisioned automatically where workspace `frontend` will be set to auto mode, which keeps track of updates in the upstream Git repository.

```http
https://sandboxes.cloud/create?template=frontend&ws_frontend_co_src_version=master&ws_frontend_mode=auto&dep_mysql_snapshot=mysql-snapshot&autolaunch=true
```

For the above URLs, query parameters consists of:

| Breakdown                                       | Descripiton                                                                                                                         |
| :---------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| template=*frontend*                             | `frontend` template will be used for the target sandbox.                                                                            |
| ws\_**frontend**\_co\_**src**\_version=*master* | For the target sandbox, the checkout `src` in workspace `frontend` will use `master` branch as an override.                         |
| ws\_**frontend**\_mode=*auto*                   | For the target sandbox, workspace `frontend` will be set to auto mode, which keeps track of updates in the upstream Git repository. |
| dep\_**mysql**\_snapshot=*mysql-snapshot*       | Dependency `mysql` will use a snapshot called `mysql-snapshot`.                                                                     |
| autolaunch=*true*                               | The target sandbox will be automatically launched.                                                                                  |
| env\_**NODE\_ENV**=*production*                | The target sandbox will apply an environment variable `NODE_ENV=production`                                                         |

In case of a simple workspace setup, the below URL can also to be used to launch a sandbox:

```Text HTTP
https://sandboxes.cloud/create?template=frontend&repo=orgname/reponame&version_spec=develop&mode=auto&autolaunch=true
```

For the above URLs, query parameters consists of:

| Breakdown               | Description                                                                                                                                                           |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| template=*frontend*     | `frontend` template will be used for the target sandbox.                                                                                                              |
| repo=*orgname/reponame* | If the workspace's checkout matches the repo, the target workspace will be selected as further customisation target, such as `version_spec`, `mode` and `autolaunch`. |
| mode=*auto*             | If the workspace's checkout matches the repo, the auto follow mode is turned on.                                                                                      |
| version\_spec=*develop* | If the workspace's checkout matches the repo, `develop` will be used as the override.                                                                                 |
| autolaunch=*true*       | The target sandbox will be automatically launched.                                                                                                                    |

### Supported query parameters

An overview of query parameters and their descriptions are as follows:

| query parameter                      | description                                                                                                                                                                                                                                                                                                                         |
| :----------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| template                             | The template name for target sandbox, if not provided, the first template will be used.                                                                                                                                                                                                                                             |
| flavor                               | The flavor of the template, if not provided, the default flavor will be used.                                                                                                                                                                                                                                                       |
| sandbox\_name                        | The name for the target sandbox, if not provided, a name prefixed with the username will be populated. If an invalid name is specified,  the sandbox might not be created automatically regardless of the value of *autolaunch*                                                                                                     |
| ws\_WORKSPACE\_co\_CHECKOUT\_version | WORKSPACE is the name of target workspace, CHECKOUT represents the path of corresponding checkout in the workspace. The accepted value is *branch name*, *commit number*, etc.                                                                                                                                                      |
| ws\_WORKSPACE\_mode                  | WORKSPACE represents the name of workspace in the target app.                                                                                                                                                                                                                                                                       |
| dep\_DEPENDENCY\_snapshot            | DEPENDENCY represents the name of dependency workload in the target app. The accepted value is the name of a snapshot of which the service type is also aligned with target app.                                                                                                                                                    |
| container\_CONTAINER\_snapshot       | CONTAINER represents the name of the container workload in the target app.  The accepted value is the name of a snapshot that is for container and strictly matches the volumes information.                                                                                                                                        |
| autolaunch                           | Accepted values are true or false. The sandbox will be automatically launched if this is set to true, otherwise, sandbox creation page will only be populated with other provided values. You can omit this flag if you would like to allow another chance to review the settings before launching.                                 |
| env\_ENV\_NAME                       | Inject an environment variable to the launching sandbox.                                                                                                                                                                                                                                                                            |
| repo                                 | This `repo` query parameter can be used to simplify the setup. Instead of use ws\_WORKSPACE\_\* prefixed query parameters, this `repo` query parameter can be used to match any workspace\checkout that uses the same repository. This query parameter are normally used together with `version_spec` and `mode` query parameters. |
| version\_spec                        | Similar to ws\_WORKSPACE\_co\_CHECKOUT\_version, this version\_spec can be used to specify the version spec for the matched workspaces/checkouts by `repo` query parameter. It must be used together with `repo`.                                                                                                                   |
| mode                                 | Similar to ws\_WORKSPACE\_mode, this mode can be used to indicate the auto follow mode for the matched workspace by the `repo` query parameter. It must be used together with `repo`.                                                                                                                                               |

## Launch a Sandbox Automatically as Part of CI Process

Crafting also supports sandboxes to be launched automatically as a Pull Request is generated, without any developer action. To achieve this, following setup is required:

1. Hooks triggered by Pull Request: Your CI pipeline should already have hooks that gets run for each PR, from there, you need to extract which repo's which branch needs to be setup for the preview, and other settings.
2. Script to run Crafting CLI to create sandbox: You need to write a script to run Crafting CLI, which can create a sandbox for a very specific configuration.

For allowing your CI tool to run Crafting CLI, `cs`, we suggest using [Service Account](https://docs.sandboxes.cloud/docs/account-setup#service-account-and-login-token), which supports a token-based login that doesn't require browser. With that, the Crafting CLI can be integrated into any workflow you want.

To create sandbox using CLI with a specific configuration, please check [CLI reference](command-line-tool#sandbox). The basic command is something like this:

```shell
$ cs sandbox create NAME -a TEMPLATE-NAME -D WORKSPACE-NAME/checkout[PATH].version=BRANCH-NAME
```

For example, to create a preview sandbox named `demo-preview-1` based on the `demo` template and use the branch `preview1` for the workspace `dev` checkout `src/demo`. The following command is used.

```shell
$ cs sandbox create demo-preview-1 -a demo -D 'dev/checkout[src/demo].version=preview1'
```

Note that launching a sandbox for every single Pull Request may consume a lot of computational resources. We recommend to set some special flags or naming conventions for launching sandbox without user action.

## Launch a Sandbox using Github Action

Please refer to the [action page in Github marketplace](https://github.com/marketplace/actions/sandbox-launch-action).
