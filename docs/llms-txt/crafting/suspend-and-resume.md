# Source: https://docs.sandboxes.cloud/docs/suspend-and-resume.md

# Suspend and resume

In this page, we talk about an important feature Crafting Sandbox offers, sandbox suspension.

In order to leverage powerful machines for development or running multiple services end-to-end on cloud, it usually requires a lot of computational resources such as CPU and Memory. For saving these resources in the idle time, Crafting platform supports *activity-based auto suspension*. As a user, you may notice your sandbox is suspended after some time of inactivity.

### What are persisted in the sandbox during suspension?

During suspension, the dev containers that runs the workloads in the suspended sandbox is not running on machines to save resources. But unlike production stateless services in containers or some other ephemeral solutions, **all the file system state in the sandbox is saved** on persistent volumes for Crafting Sandbox. It means that you can pick up where you were with all the following parts exactly like they were before sandbox suspension.

* Source code checkout in your workspaces
* Local file system in your workspaces, including your home directly and root file system
* Logs from the services running in all your workspaces
* Files for containers and dependencies, e.g., data in your database services.
* All sandbox configurations

Note that all the in-memory state, however, will not be saved during suspension and all the service processes will be restarted after the sandbox is resumed.

### How to suspend / resume a sandbox?

Like mentioned before, the sandbox is auto-suspended when there is no activity with it. Basically everything that a developer can interact with a sandbox is considered activity, including:

* Web IDE session
* SSH session
* File sync session
* Local desktop IDE connection to the sandbox session
* Endpoint access to the sandbox, from mobile app, web frontend, external API, etc.

The auto-suspension time threshold is 30 minutes idle time if you are using Crafting SaaS. If you are using Crafting Self-hosted, it can be set by your admin.

You can manually suspend a sandbox from the sandbox page

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/e24ef3f-guide-suspend.JPG" />

To resume a suspended sandbox, you can resume it from the sandbox page as well.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/9845954-guide-resume.JPG" />

But in practice, most activities on the sandbox will either automatically resume it or prompt you to resume it in UI.

### Pin a sandbox

Sometimes a sandbox is needed for demo purpose and is meant to have long period of inactivity. For that usage, you can choose to `pin` a sandbox to avoid it being suspended.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/4327822-guide-pin.JPG" />

Given pinned sandbox will always consume computational resources, there is a organizational level setting to control a limit on how many sandboxes can be pinned.

You can also pin a sandbox via a CLI command

```shell
$ cs sandbox [pin|unpin] [SANDBOX-NAME]
```

the `SANDBOX-NAME` can be omitted if the command is run in the sandbox to pin.