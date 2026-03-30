# Source: https://docs.sandboxes.cloud/docs/start-a-workspace.md

## Start a Workspace

In this section, we talk about how to start a simple workspace to do some online coding. If you are in a development team, it's likely that your team's admin has already set up the standard development environments into templates. In that case, you should see [Launch a sandbox](https://docs.sandboxes.cloud/docs/launch-a-sandbox) for more information on how you can further customize and launch sandbox.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/8d750c8-user-guide-empty-home.JPG" />

To start a [workspace](https://docs.sandboxes.cloud/docs/concepts-and-architecture#workspace), which is a dev container on cloud where you can code and run your program, you can directly click `Create new Sandbox` from the `Home` page on your web console.

<Image align="center" width="60% " src="https://files.readme.io/769faad-guide-new-workspace.JPG" />

Then, under `Create a Workspace`, you can choose the Git repository URL you want to checkout code and the branch. Optionally you can also also choose a special container image that you want to use for your workspace. By default, it will be based on a standard Ubuntu Linux image. Clicking `Create` will create a new sandbox with a single workspace.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/087e6de-guide-workspace-sandbox.JPG" />

When the sandbox is ready, the source code is checked out into the sandbox and you can click `Open WebIDE` to get into the Web IDE session to edit code. Like shown below, the Web IDE is based on VS code and has a terminal for executing commands.

![Web IDE with VS Code](https://files.readme.io/021353b-guide-workspace-webide.JPG)

You can also quickly modify the sandbox's configuration by clicking `Edit`. In the editing view, you can add more components such as workspaces, containers, dependencies, etc. to your sandbox. For details on editing the config, please see [here](https://docs.sandboxes.cloud/docs/templates-setup)

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/4c1121b-guide-workspace-edit.JPG" />

After editing, you can save the current sandbox configuration as a `template` so that sandbox created in future can use these templates. Or click `Apply` to save the config to the current sandbox. For more information, please see [Standalone sandbox](https://docs.sandboxes.cloud/docs/standalone-sandbox).
