<!-- Source: https://docs.sandboxes.cloud/docs/work-on-a-sandbox.md -->

# Work on a sandbox

When the sandbox is launched and ready, we can start using the sandbox. In this page, we will use the simple multi-service demo app to cover following parts.

* [Run previews](#run-previews)
* [Inspect the workspaces](#inspect-the-workspaces)
* [View logs generated from your services](#view-logs-generated-from-your-services)
* [Use Web IDE to write code or run commands](#use-web-ide-to-write-code-or-run-commands)
* [Rebuild workspace](#rebuild-workspace)

For additional information, please see [Advanced Topics](https://docs.sandboxes.cloud/docs/advanced-topics)

## Run previews

For previewing the code changes you have in the sandbox, you can access the sandbox via `endpoints`. These are the URLs exposed by the sandbox which gets routed to some backend services to run the entire product flow end-to-end. For example, in the demo app, we have two HTTPS endpoints, `app` and `api`, routed to the frontend service (with port 3000) and backend service (with port 3001), respectively. We can hit the `app` endpoint as shown below to run the product flow.

<Image align="center" className="border" border={true} src="https://files.readme.io/38203f1-guide-sandbox-endpoint.jpg" />

After clicking the `app` endpoint, we can see it opens a new page with the sandbox URL `https://app--demo-demo-cloud.sandboxes.run/` and with the code version in the sandbox.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/52fa188-guide-sandbox-preview.jpg" />

Similarly, you can hit the API endpoint from your web frontend, mobile frontend, or command line tools like `curl`

## Inspect the workspaces

You can see the information of each workspaces running in the sandbox by clicking into any workspace. For example, if we click into the backend workspace, we can see it has one repo checkout `demo-jobs-backend`, which is currently on `master` branch, and it's checked out to the path `backend`. It also has two daemon processes running, one open port (`api` port 3001) with the HTTP protocol, and installed with `ruby` version 2.7.2

<Image align="center" className="border" border={true} src="https://files.readme.io/eacd582-guide-workspace-demo-backend.JPG" />

## View logs generated from your services

From here, you can click the page icon to view the logs for specific services or daemon processes.

<Image align="center" className="border" border={true} src="https://files.readme.io/93e167d-guide-workspace-demo-backend-log.JPG" />

For example, below is the log for the rails process.

<Image align="center" className="border" border={true} src="https://files.readme.io/799363a-guide-sandbox-log-viewer.JPG" />

## Use Web IDE to write code or run commands

When you want to go into the workspace to write code or run commands, you can simply open the Web IDE by clicking any of the buttons highlighted below:

<Image align="center" className="border" border={true} src="https://files.readme.io/d1afc1c-guide-sandbox-web-ide.jpg" />

For example, if we open the Web IDE on the frontend, we can see the following window, a VS Code web version opened with a terminal panel.

![Web IDE screenshot](https://files.readme.io/40fad3d-guide-web-ide.JPG)

Here we can directly modify the code (e.g., change the title of the page to `Crafting Jobs.` to something else and it will take effect immediately and we can preview it with the endpoint URL.

The terminal here is in the code checkout directory. Given it's a regular Git checkout, you can do git commands such as `git pull`, `git checkout`, `git commit`, `git push`, etc. directly from here. Or you can run any other command here that you want to execute on this dev container.

## Rebuild workspace

In some cases you may want to wipe clean one of your workspaces (and dependencies or containers as well) to restart it from scratch. You can rebuild it by clicking the rebuild button highlighted below:

<Image align="center" className="border" border={true} src="https://files.readme.io/b814bfc-guide-sandbox-rebuild.jpg" />

Rebuilding the a workspace will clear all the local state. It will checkout the code fresh from the git repo, run the setup and build, and launch the service, all according to what's specified in the template. It basically gives you a fresh state of the workspace as such from a new sandbox. Rebuilding dependencies will remove all the current data and reset it to empty (or with the default data snapshot specified in the template)
