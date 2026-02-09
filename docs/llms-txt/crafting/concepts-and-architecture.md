# Source: https://docs.sandboxes.cloud/docs/concepts-and-architecture.md

# Concepts and Architecture

In this section, we explain some of the core concepts behind Crafting Sandbox and dig deeper on its architecture.

## Core Concepts

#### Sandbox

A `sandbox` is a self-contained development environment. It includes one or multiple `workspaces`, and also `containers`, `dependencies`, `resources`, `endpoints` as needed. These components are grouped together in a sandbox and share the same life-cycle, e.g., creation, suspension, deletion, etc. Each sandbox has its own private network to connect the components in it together.

#### Workspace

A `workspace` is a dev container installed with Linux OS and dev tools, functionally equivalent to a developer VM on cloud. It's the main component that developers interact with because it's where the source code is checked out and where the service being developed runs.

#### Dependency & Container

`Dependencies` and `containers` act as supporting roles in the sandbox. In addition to the service they actively develop on, developers usually need other services which they don't need to modify available as well.  These include standard services like Postgres database, Redis cache, or other specific services running in their own standard containers.

A `dependency` is a well-known standard service like database, cache, etc. Crafting supports a list of commonly used ones like `MySQL`, `Postgres`, `DynamoDB`, `Redis`, `ElasticSearch`, `Memcache`, `RabbitMQ`, etc., with multiple versions each. Users can just specify name and version to make them available conveniently. In addition, users can bring any custom `container` to the sandbox by specifying container tag/image, environment variables, etc. in order to achieve maximum flexibility.

#### Resource

In addition to `dependencies` and `containers`, developers sometimes need to access or provision additional cloud native components for their development, such as AWS lambda function, Kubernetes namespace, etc. These components are physically outside of the sandbox but they need to work closely with components in the sandbox and their life-cycle should be in-sync with the sandbox.

A `resource` represents an external component that can work alongside with the components in the sandbox. Crafting allows the `resource` to be provisioned by Terraform or user-defined custom scripts. The life-cycle of the `resource` is maintained in-sync with the sandbox so that the provisioned external components can be properly created and destroyed.

#### Endpoint

For security, the ports exposed by `workspaces`, `dependencies`, and `containers` are only visible to the internal network in the `sandbox`. An `endpoint` creates an external facing URL serving as the ingress to the sandbox. Traffic to an `endpoint` can be routed to ports on `workspaces`, `dependencies`, and `containers` in the sandbox. Advanced routing rules and authentication can be added to `endpoints`

#### Template

To make the development environments standard and replicable, the specific configuration of a `sandbox` can be saved as a `template` . A `template` defines the specs of components within a sandbox such as `workspaces`, `endpoints`, etc., and users can create sandboxes from any templates they define. Since a `template` is often used to represent the entire app end-to-end, it's also called `app`.

<Image align="center" width="80% " src="https://files.readme.io/be12cfa-Draft.png" />

#### Other concepts

Other concepts like `Secret`, `Snapshot`, `Repo Manifest`, etc. are discussed in detail in other parts of the documents.

## How does Crafting Fit in Your Workflow

<Image align="center" width="80% " src="https://files.readme.io/83a67c7-Frame_90.png" />

As shown above, Crafting is made to assist developers as the dev environments. It does not replace your current source control system or CI/CD pipeline. It typically used *before* the code change (Pull Request) is merged into the main branch.

Crafting is also language/technology agnostic. Based on the operation system and network layer, it does not restrict itself to any particular programming language, framework, or technology. No matter you are frontend engineer working on Javascript, or backend engineer with Java/Go/Python etc. as long as you can set up your environment on a Linux machine, you can take advantage of Crafting.

It can support developers to do full-on-the-cloud development, where developers use Web IDE or Desktop IDE to directly modify the source code in the online workspace. Or it can be used together with local machine in `hybrid mode` by providing an end-to-end context on cloud for the service being worked on locally. In addition, developers can create sandbox per Pull Request to do end-to-end preview of their changes, in a production-like environment.

### Full-on-the-Cloud Development

<Image align="center" width="60% " src="https://files.readme.io/e57706b-concepts-cloud-dev.png" />

For the full-on-cloud development, developers don't need to bother set up and maintain dev environments on their local machine. All they need to install is the browser or remote-capable IDEs, such as VS Code or JetBrains IDEs. They can use them to connect to Crafting Sandbox and edit code remotely on a fully prepared dev environment with Linux OS and all the dev tools.

Advantages of full-on-the-cloud development include:

* The dev environments are standardized and centrally managed, always stable and ready to code.
* Leverage powerful cloud machines without limited by local CPU and memory.
* Library & toolchain updates and security patches are always fresh, no local maintenance.
* Code anywhere, any time, completely portable.
* Linux OS, architecture consistent with production machines.
* Easy for remote collaboration and trouble-shooting.

Crafting supports following ways to code directly on cloud workspaces:

* SSH on the cloud workspace and use terminal based editor, such as Vim, Emacs, Nano, etc.
* VS Code Web IDE
* VS Code Desktop connecting to remote via SSH
* JetBrains IDEs, such as IntelliJ, RubyMine, PyCharm, GoLand, etc.

### Cloud-and-Local-Hybrid Development

<Image align="center" width="60% " src="https://files.readme.io/1f16189-concepts-hybrid-dev.png" />

For the hybrid development, developers still maintains their local dev environment and uses their favorite local IDE to work on a code base checked out on their local machine. They can run the service they focus on locally as well. But to actually test run their changes, they can have all the heavy-lifting services their service depends on to run on the cloud. That way, they don't need to bother setting up all the services they don't touch locally and the resource usage on their local machine is minimized. Through traffic forwarding, their local machine is virtually replacing the corresponding service on cloud to have an end-to-end flow.

Advantages of full-on-the-cloud development include:

* Developers have near-zero workflow change from their local machine dev experience.
* Heavy dependencies and services are off-load to cloud and no longer consumes local resources.
* Developers can choose to use port forwarding to route traffic between local and cloud to have an end-to-end experience
* Developers can also choose to use code/file sync with remote workspaces to build/run services on cloud workspaces.

### Production-like Preview

Crafting is often used for end-to-end preview in the development workflow. After a code change (e.g., Pull Request) is submitted for review, developers often need to verify how the change behave in an end-to-end production-like environment before merging it in. Crafting lets developers create a whole production-like environment on-demand easily in a resource-efficient manner, so that developers as well as product managers, designers, and QA can preview the change.

Advantages of production-like preview include:

* Developers no need to fight for a shared staging to preview their change end-to-end
* Changes can be reviewed by cross-functional teams early, minimizing iteration cycle
* Easy creation and auto clean up to manage production-like environments
* Leverage existing production config to achieve high fidelity to production

Crafting offers a general support for you to replicate your production environment. Anything you can provision with Terraform or using your script, you can replicate it on Crafting.

* CPU architecture, operating systems, and networks can match your production
* Custom containers can be pulled from your registry
* Special support for running Kubernetes-based apps and services.
* Serverless cloud native resources such as AWS Lambda, SQS, etc. can be allocated on-demand

## Crafting Architecture

Here, we dig a little deeper on Crafting's internal architecture.

<Image align="center" width="80% " src="https://files.readme.io/837d10f-Architecture.png" />

As shown above, Crafting is running in a Kubernetes cluster. It has a control plane with its management services such as API service, reconciler, etc., and a database to store metadata. It manages the nodes (VM hosts) in the machine pool and runs the sandboxes' workloads, e.g., workspaces, dependencies, etc. as containers on the nodes. Workloads in one sandbox can be physically running across multiple nodes, making it very scalable and not limited by per-machine resource constraints. An overlay network is setup by Crafting to connect workloads within a sandbox and ensure isolation between different sandboxes. The overlay network is also responsible for achieving more advanced functionalities such as on-demand traffic routing.

Inside a workload, Crafting uses different setup for different workload types. For example for a dependency, it starts from a container image, with possibly a data snapshot applied on top, and it has process management and logging to support the running service to finally expose a port. For a workspace, where developers use as cloud machine for interactive development, there are more components. It starts from an Linux OS image (default Ubuntu, can be substituted by user), with possibly file system snapshot for user's customization, on organization level or per-developer. Then it's the automation layer to manage the machine's environments, including dev packages, open ports, environment variables, secrets, port-forwardings, checkout management, build system, and process management. On the top layer, it's the source code user checks out and process running based on the source code, as well as IDE backend to support remote coding.

Then the developer uses their local machine to access the workspace, via SSH terminal, Web IDE running in a browser, or desktop IDE connecting to the IDE backend. The developer also manages the sandbox system from the web console, which is supported by Crafting control plane.

### Working with your own Kubernetes cluster

Crafting for Kubernetes allows you to connect existing Kubernetes clusters (not the cluster dedicated to Crafting installation) to the Crafting platform for doing preview and traffic interception, etc. Please see the use [Develop on Kubernetes](https://docs.sandboxes.cloud/docs/kubernetes-dev) for details.

### Working with cloud native serverless resources

Crafting allows developers to access cloud native serverless resources on their cloud providers like AWS and GCP directly from the workspaces. The main issue to establish proper authentication and authorization for such access. Crafting provides solutions like identity federation and stored secrets for users to achieve that. Please see [Develop with cloud resources](https://docs.sandboxes.cloud/docs/cloud-resources-dev) for details.