# Source: https://docs.sandboxes.cloud/docs/templates-best-practices.md

# Checklist and best practices for templates

Here, to summarize, we provide a checklist for key points in setting up `Templates` to standardize dev environments for your team on Crafting. Depending on your specific need, you don't necessarily need to have everything in this list, but it's good to check them to find opportunities for optimizing the dev experience.

* \[ ] Setup workspaces with automated source code checkout (instructions [here](https://docs.sandboxes.cloud/docs/workspaces-setup#add-code-checkouts))
* \[ ] Setup libraries and packages needed by the source code, and persist them in snapshots (instructions [here](https://docs.sandboxes.cloud/docs/workspaces-setup#install-required-system-packages) and [here](https://docs.sandboxes.cloud/docs/workspaces-setup#persist-packages-and-libraries-setup-with-snapshots) )
* \[ ] Setup automated build and service launch in workspaces in [Repo Manifest](https://docs.sandboxes.cloud/docs/repo-manifest) (instructions [here](https://docs.sandboxes.cloud/docs/workspaces-setup#build-and-launch-service-and-setup-automation-in-repo-manifest))
* \[ ] If needed, setup environment variables and initialization scripts to further customize the workspace (instructions [here](https://docs.sandboxes.cloud/docs/#setup-environment-variables) and [here](https://docs.sandboxes.cloud/docs/workspaces-setup#initialization-scripts-for-workspace-setup))
* \[ ] Setup dependency services and custom containers to run together with your workspaces, and automate the loading of test dataset (instructions [here](https://docs.sandboxes.cloud/docs/containers-dependencies-setup))
* \[ ] Setup endpoints for external access to the services running in sandbox (instructions [here](https://docs.sandboxes.cloud/docs/network-setup#setup-endpoints))
* \[ ] If needed, setup resources to represent cloud resources or Kubernetes namespaces (instructions [here](https://docs.sandboxes.cloud/docs/resources-setup), [here](https://docs.sandboxes.cloud/docs/cloud-resources-setup), and [here](https://docs.sandboxes.cloud/docs/kubernetes-setup))
* \[ ] If needed, setup `secrets` to manage development credentials (see [here](https://docs.sandboxes.cloud/docs/secrets))
* \[ ] If needed, setup an instruction in mark-down for your team talking about how they can use the sandbox (see [here](https://docs.sandboxes.cloud/docs/home-screen-message-and-sandbox-instruction#sandbox-instructions))

In the remainder of this page, we will discuss some best practices for using templates:

* [Best practice for managing the templates](#best-practice-for-managing-the-templates)
* [Best practice for snapshots](#best-practice-for-snapshots)
  * [Create snapshots using code](#create-snapshots-using-code)
  * [Snapshots naming convention](#snapshots-naming-convention)
  * [Save VS Code settings in snapshots](#save-vs-code-settings-in-snapshots)

### Best practice for managing the templates

For any non-trivial templates, we strongly recommend storing them in source repositories and manage them "config-as-code" in the YAML format. Crafting allows editing the template directly in the YAML format so that pasting an existing YAML config into a template for testing its validity is straightforward. See [Sandbox Definition](https://docs.sandboxes.cloud/docs/sandbox-definition) for the details in how to define a template.

Crafting does not require any particular way to store them but the following practices are good candidates:

* If your code is mono-repo or you have a "main" repo, you could store the template somewhere in there, or
* If you have a separate "dev ops" repo where you store a long of shared configurations, you could store the template there as well, or
* you can create a separate repo just for storing the template.

Given it is more convenient to edit and test template directly on Crafting web console, it's reasonable to iterate quickly without storing it at first for setting up something new. But once it gets to a good shape, it's best practice to store the YAML definition somewhere and enforce a process for updating it.

In addition, the template depends heavily on [Repo Manifests](https://docs.sandboxes.cloud/docs/repo-manifest) to automate build and launch services from the source code. As the name suggests, it's corresponding to a single repo, so naturally we recommend to store them in their corresponding repo. Even though you can directly define them as part of the template, we strongly recommend they are store in the `.sandbox/manifest.yaml` under the repo for long term maintenance.

### Best practice for snapshots

In summary there are four types of snapshots:

* **Base snapshot**: taken from a workspace root filesystem, with home directory (`/home`) excluded; (see [Setup workspaces](https://docs.sandboxes.cloud/docs/workspaces-setup#persist-packages-and-libraries-setup-with-snapshots))
* **Home snapshot**: taken from the home directory of a workspace owner (`/home/owner`) using the include/exclude list explicitly; (see [Setup workspaces](https://docs.sandboxes.cloud/docs/workspaces-setup#persist-packages-and-libraries-setup-with-snapshots))
* **Dependency/Container snapshot**: taken from the data directory of a dependency service, or a persistent volume mounted on container; (see )
* **Personal snapshot**: a snapshot containing personalized configurations and can be applied to the home directory (`/home/owner`) for every workspace in newly created sandboxes. (see [Personalize your sandbox](https://docs.sandboxes.cloud/docs/personalize))

#### Create snapshots using code

To have a more reproducible and manageable process to track what's inside each snapshot, we recommend using a script to create them. In the script, you can run things like `sudo apt install`, etc. to install the things needed. And the script should be checked-in as code for source control.

When an update of snapshot is needed, instead of just adding the packages and re-take the snapshot, you can:

1. Create a workspace without the snapshot;
2. Run the updated scripts (store in source repo with code review) to set files
3. Re-create the snapshot

#### Snapshots naming convention

All snapshots share the same namespace regardless of the type. It's recommend prefixing the snapshot type in the name to avoid conflicts, for example:

* Base Snapshots are named as `base-NAME-REV`.
* Home Snapshots are named as `home-NAME-REV`.
* Dependency Snapshots are named as `SERVICE-TYPE-NAME-REV`.

The `NAME` will be defined based on the purpose of the Snapshot, and `REV` can be anything indicating a revision, for example a date in the format of `YYYYMMDD` or a monotonic version number etc.

Some examples:

* `base-frontend-20211201`
* `base-backend-r1`
* `home-frontend-20211201`
* `mysql-dev-20211201`
* `mysql-test-r2`

If there are multiple sub-teams or sub-projects, a prefix can be added, e.g.

* `project1-base-backend-20211201`
* `team-a-home-backend-2`

Snapshots created for personal use can prefix the user name, e.g.

* `alan-home-backend-1`

#### Save VS Code settings in snapshots

It's helpful to put VS Code settings and extensions in snapshots (home or personal). The system supports VS Code web (in the browser) or desktop VS Code connecting over SSH. And they are using different folders for the settings and extensions. Here's the base folder of different VS Code editions:

* VS Code used in Web IDE: `~/.vscode-remote`
* Microsoft VS Code Desktop: `~/.vscode-server`
* Open Source VS Code Desktop: `~/.vscode-server-oss`

The following subfolders (or files) contain useful configurations that can be put in a snapshot:

* `extensions`: all installed extensions, so the whole folder can be included in a snapshot;
* `data/Machine/settings.json`: the per-machine settings. It can be included in a personal snapshot.

```text ~/.snapshot/includes.txt
.vscode-remote/extensions
.vscode-server/extensions
```

```text ~/.snapshot.personal/includes.txt
.vscode-remote/data/Machine/settings.json
.vscode-server/data/Machine/settings.json
```