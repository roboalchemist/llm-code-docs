<!-- Source: https://docs.sandboxes.cloud/docs/developer-workflows.md -->

# Developer Workflows

In this section, we walk though the common workflows on Crafting from a developer point of view. This is assuming the proper set up is already done. For more information on sign-on and setup, please take a look at [Quickstart Guide](https://docs.sandboxes.cloud/docs/quick-start) and [Admin Overview](https://docs.sandboxes.cloud/docs/admin-overview), respectively.

## Demo Videos

Below are links to demo videos walking through the common workflows:

[One Click Dev Environments](https://bit.ly/crafting-democ1) (6:17)

* Creating a dev environment (Crafting Sandbox) with frontend and backend up-and-running,
* Develop code in WebIDE as well as desktop IDE connecting to remote container
* Run in local/remote hybrid mode with port forwarding

[Integration Testing & Preview](https://bit.ly/crafting-democ2) (6:01)

* Launch a preview from a PR and run everything end-to-end
* Debug in Crafting Sandbox with code modifications instantly effective
* Swapping a service with the local version and debug using breakpoints with desktop IDE

[Remote Collaboration](https://bit.ly/crafting-democ3) (4:51)

* Pair programming and see your teammates editing code live with Crafting Sandbox
* Work QA team to get a environment which can reproduce test failures
* Work with third party callbacks from Internet and external collaborators

[Crafting for Kubernetes](https://bit.ly/crafting-democ4) (7:17)

* Launch per-developer on-demand production-like Kubernetes deployments with Crafting Sandbox and manage their lifecycles
* Interactively write code and see results immediately without re-launching containers by traffic interception
* Easy setup for your own Kubernetes cluster using your existing config

[Crafting with Cloud Resources](https://bit.ly/crafting-democ5) (5:24)

* Make cloud native serverless services like RDS, SQS and Lambda, work alongside containers
* Setup identity federation to provide developers in Crafting Sandbox with seamless and secure access to your cloud
* On-demand provision cloud resources and manage their lifecycle using Crafting Sandbox

## Main Development Flow

Here we work through a typical workflow for using Crafting in day-to-day development on a high level. For any specific use case, please see the corresponding section for more details, the list of top use cases can be found [here](https://docs.sandboxes.cloud/docs/quick-start#list-of-use-cases), for example, if you are using Kubernetes to orchestrate the services in your app, you can take a look at [Kubernetes Development and Testing](https://docs.sandboxes.cloud/docs/use-case-kubernetes)

To start working on a code change, you can create a dev environment on Crafting. It is up to you to choose to treat the dev environment as *ephemeral* and discard it whenever you are done with the code change, or to stick to an environment and use it for a long term. All your local changes in the environment is persisted.

The dev environments on Crafting is organized as `Sandbox`, which can be constructed on demand according to your predefined template. A sandbox can have one or multiple `Workspaces`, which are dev containers with a standard Ubuntu image and dev tools (You can use your favorite container image as well). Each workspace acts like an online VM and supports you to code for your codebase. Workspaces in the same sandbox are connected by a virtual network, along with other components such as `containers` and `dependencies`, so that services running in different components can work with each other.

To create a sandbox, you can go to our web console and enter the create page. The following shows the components diagram for our demo and the sandbox creation page, with several workspaces, containers, and dependencies.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/4270293-dev-flow-multi-service-diagram.JPG" />

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/15e5136-dev-flow-create.JPG" />

To launch the sandbox, you can just click the **LAUNCH** button on the top right corner and a sandbox will be created. During sandbox creation, Crafting platform *prepares your sandbox to be fully ready for you to develop on*. Based on your setup, it checks out the source code into corresponding workspace folders, installs all the dev packages, builds your code with powerful cloud machines, sets up your database with migrations and seed data, and even runs the services end-to-end for you. The following shows a launched sandbox.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/b4a32b4-dev-flow-sandbox.JPG" />

From here, you can open the Web IDE directly for any workspace to start coding, which also includes a terminal for you access it via command line. The Web IDE is based on the open-source VS code, whose coding experience is as good as native VS code. Given the source code in sandbox is managed by git as a checkout, you can commit your change and push it back to the repo from your workspace directly.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/f07aeb6-dev-flow-web-ide.JPG" />

You can also access the workspace via SSH from your local machine via our command line tool, `cs`.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/2f13bb0-image.png" />

If you prefer to use your desktop version of VS code or JetBrains IDEs, such as IntelliJ, RubyMine, PyCharm, etc., you can also run these locally and connect to sandbox via SSH to directly modify the remote codebase. See more details at [Code with VS Code](https://docs.sandboxes.cloud/docs/code-with-vs-code) and [Code with JetBrains IDEs](https://docs.sandboxes.cloud/docs/code-with-jetbrains-ides)

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/a972f05-dev-flow-ides.JPG" />
