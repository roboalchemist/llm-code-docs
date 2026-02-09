# Source: https://docs.sandboxes.cloud/docs/auto-follow.md

# Auto-follow code branch in sandbox

In this page, we describe how to use the `auto-follow` feature in Crafting sandbox for your development and preview.

Crafting allows developers to turn some workspaces into `AUTO` mode, where it would periodically check the Git repo to see whether there is a new version of the code available for that branch. If so, it would pull the new version of the code to the workspace and rerun hooks for building the code and restarting the service. That way, the service running on the workspace in `AUTO` mode is always up-to-date.

Note that once the workspace is in `AUTO` mode, developers should not edit the code manually there, because all the edit will be discarded and may potentially interfere with the automation. We recommend turning off `AUTO` mode before editing code and debug in the workspace.

### Turn on/off Auto mode for a workspace

To turn on auto mode for an existing sandbox, we can simply turn on the toggle on the workspace from the sandbox page as highlighted follows.

<Image align="center" className="border" border={true} src="https://files.readme.io/72bcfb8-guide-auto-mode.JPG" />

Auto mode can also be controlled via CLI using the following command.

```shell
$ cs mode [auto|manual] -W <SANDBOX/WORKSPACE>
```

The `-W` option is not needed when running the `cs mode` command in the target workspace.

The `AUTO` mode can also be selected for a newly created sandbox, by toggle the switch in the customization page, as shown below

<Image align="center" className="border" border={true} src="https://files.readme.io/432f36f-guide-create-auto.JPG" />

### Use cases for Auto mode

There are several key use cases for Auto mode:

* **To keep PR preview sandbox up-to-date**: With Auto mode, the code in the target workspace will be kept up-to-date for the branch of the PR, which means it would automatically reflect new commits pushed into the branch.
* **To support hybrid development with code sync**: Auto mode can be used to sync code from local machine to cloud workspaces in a more automated way. Please see [Code sync for hybrid development](https://docs.sandboxes.cloud/docs/code-sync) for details.
* **To have a sandbox always following master or staging**: We can turn on Auto mode for all workspaces to let them follow a specific branch such as `master` or `staging`. That way, we have a place for developers to check the latest flow. It's also a reasonable practice to `pin` such sandbox to make it always on.
* **To keep dependencies code up-to-date**: We can turn on the Auto mode to let all other services except the target service we work on follow the master branch. This way, we always get an up-to-date context in our dev environment.