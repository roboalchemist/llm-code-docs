# Source: https://www.jenkins.io/doc/book/glossary/

Title: Glossary

URL Source: https://www.jenkins.io/doc/book/glossary/

Markdown Content:
[Agent](https://www.jenkins.io/doc/book/using/using-agents/)[](https://www.jenkins.io/doc/book/glossary/#agent)
An agent is typically a machine, or container, which connects to a Jenkins controller and executes tasks when directed by the controller.

Artifact[](https://www.jenkins.io/doc/book/glossary/#artifact)
An immutable file generated during a [Build](https://www.jenkins.io/doc/book/glossary/#build) or [Pipeline](https://www.jenkins.io/doc/book/glossary/#pipeline) run which is **archived** onto the Jenkins [Controller](https://www.jenkins.io/doc/book/glossary/#controller) for later retrieval by users.

Build[](https://www.jenkins.io/doc/book/glossary/#build-1)
[](https://www.jenkins.io/doc/book/glossary/) Result of a single execution of a [job](https://www.jenkins.io/doc/book/glossary/#job)

Cloud[](https://www.jenkins.io/doc/book/glossary/#cloud-1)
[](https://www.jenkins.io/doc/book/glossary/) A System Configuration which provides dynamic [Agent](https://www.jenkins.io/doc/book/glossary/#agent) provisioning and allocation, such as that provided by the [Azure VM Agents](https://plugins.jenkins.io/azure-vm-agents) or [Amazon EC2](https://plugins.jenkins.io/ec2) plugins.

Controller[](https://www.jenkins.io/doc/book/glossary/#controller)
The central, coordinating process which stores configuration, loads plugins, and renders the various user interfaces for Jenkins.

Core[](https://www.jenkins.io/doc/book/glossary/#core)
The primary Jenkins application (`jenkins.war`) which provides the basic web UI, configuration, and foundation upon which [Plugins](https://www.jenkins.io/doc/book/glossary/#plugin) can be built.

Downstream[](https://www.jenkins.io/doc/book/glossary/#downstream-1)
[](https://www.jenkins.io/doc/book/glossary/) A configured [Pipeline](https://www.jenkins.io/doc/book/glossary/#pipeline) or [job](https://www.jenkins.io/doc/book/glossary/#job) which is triggered as part of the execution of a separate Pipeline or Job.

Executor[](https://www.jenkins.io/doc/book/glossary/#executor-1)
[](https://www.jenkins.io/doc/book/glossary/) A slot for execution of work defined by a [Pipeline](https://www.jenkins.io/doc/book/glossary/#pipeline) or [job](https://www.jenkins.io/doc/book/glossary/#job) on a [Node](https://www.jenkins.io/doc/book/glossary/#node). A Node may have zero or more Executors configured which corresponds to how many concurrent Jobs or Pipelines are able to execute on that Node.

Fingerprint[](https://www.jenkins.io/doc/book/glossary/#fingerprint)
A hash considered globally unique to track the usage of an [Artifact](https://www.jenkins.io/doc/book/glossary/#artifact) or other entity across multiple [Pipelines](https://www.jenkins.io/doc/book/glossary/#pipeline) or [jobs](https://www.jenkins.io/doc/book/glossary/#job).

Folder[](https://www.jenkins.io/doc/book/glossary/#folder-1)
[](https://www.jenkins.io/doc/book/glossary/) An organizational container for [Pipelines](https://www.jenkins.io/doc/book/glossary/#pipeline) and/or [jobs](https://www.jenkins.io/doc/book/glossary/#job), similar to folders on a file system.

Item[](https://www.jenkins.io/doc/book/glossary/#item-1)
[](https://www.jenkins.io/doc/book/glossary/) An entity in the web UI corresponding to either a: [Folder](https://www.jenkins.io/doc/book/glossary/#folder), [Pipeline](https://www.jenkins.io/doc/book/glossary/#pipeline), or [job](https://www.jenkins.io/doc/book/glossary/#job).

Jenkins URL[](https://www.jenkins.io/doc/book/glossary/#jenkins-url-1)
[](https://www.jenkins.io/doc/book/glossary/) The main url for the jenkins application, as visited by a user. e.g. [https://ci.jenkins.io/](https://ci.jenkins.io/)

Job[](https://www.jenkins.io/doc/book/glossary/#job-1)
[](https://www.jenkins.io/doc/book/glossary/) A user-configured description of work which Jenkins should perform, such as building a piece of software, etc.

Kubernetes[](https://www.jenkins.io/doc/book/glossary/#kubernetes-1)
[](https://www.jenkins.io/doc/book/glossary/) Kubernetes (K8s) is an open-source system for automating deployment, scaling, and management of containerized applications. See [Installing Jenkins / Kubernetes](https://www.jenkins.io/doc/book/installing/kubernetes/) for more info.

Label[](https://www.jenkins.io/doc/book/glossary/#label-1)
[](https://www.jenkins.io/doc/book/glossary/) User-defined text for grouping [Agents](https://www.jenkins.io/doc/book/glossary/#agent), typically by similar functionality or capability. For example `linux` for Linux-based agents or `docker` for Docker-capable agents.

LTS[](https://www.jenkins.io/doc/book/glossary/#lts)
A long-term support [Release](https://www.jenkins.io/doc/book/glossary/#release) line of Jenkins products, becoming available for downloads every 12 weeks. See [this page](https://www.jenkins.io/download/lts/) for more info.

Master[](https://www.jenkins.io/doc/book/glossary/#master)
A deprecated term, synonymous with [Controller](https://www.jenkins.io/doc/book/glossary/#controller).

[Node](https://www.jenkins.io/doc/book/managing/nodes/)[](https://www.jenkins.io/doc/book/glossary/#node)
A machine which is part of the Jenkins environment and capable of executing [Pipelines](https://www.jenkins.io/doc/book/glossary/#pipeline) or [jobs](https://www.jenkins.io/doc/book/glossary/#job). Both the [Controller](https://www.jenkins.io/doc/book/glossary/#controller) and [Agents](https://www.jenkins.io/doc/book/glossary/#agent) are considered to be Nodes.

Project[](https://www.jenkins.io/doc/book/glossary/#project-1)
[](https://www.jenkins.io/doc/book/glossary/) A deprecated term, synonymous with [job](https://www.jenkins.io/doc/book/glossary/#job).

Pipeline[](https://www.jenkins.io/doc/book/glossary/#pipeline-1)
[](https://www.jenkins.io/doc/book/glossary/) A user-defined model of a continuous delivery pipeline, for more read the [Pipeline chapter](https://www.jenkins.io/doc/book/pipeline/) in this handbook.

Plugin[](https://www.jenkins.io/doc/book/glossary/#plugin)
An extension to Jenkins functionality provided separately from Jenkins [Core](https://www.jenkins.io/doc/book/glossary/#core).

Publisher[](https://www.jenkins.io/doc/book/glossary/#publisher)
Part of a [Build](https://www.jenkins.io/doc/book/glossary/#build) after the completion of all configured [Steps](https://www.jenkins.io/doc/book/glossary/#step) which publishes reports, sends notifications, etc. A publisher may report [Stable](https://www.jenkins.io/doc/book/glossary/#stable) or [Unstable](https://www.jenkins.io/doc/book/glossary/#unstable) result depending on the result of its processing and its configuration. For example, if a JUnit test fails, then the whole JUnit publisher may report the build result as [Unstable](https://www.jenkins.io/doc/book/glossary/#unstable).

Resource Root URL[](https://www.jenkins.io/doc/book/glossary/#resource-root-url-1)
[](https://www.jenkins.io/doc/book/glossary/) A secondary url used to serve potentially untrusted content (especially build artifacts). This url is distinct from the [Jenkins URL](https://www.jenkins.io/doc/book/glossary/#jenkins-url).

Release[](https://www.jenkins.io/doc/book/glossary/#release)
An event, indicating availability of Jenkins distribution products or one of Jenkins plugins. Jenkins products belong either to [LTS](https://www.jenkins.io/doc/book/glossary/#lts) or weekly Release lines.

Stage[](https://www.jenkins.io/doc/book/glossary/#stage)
`stage` is part of Pipeline, and used for defining a conceptually distinct subset of the entire Pipeline, for example: "Build", "Test", and "Deploy", which is used by many plugins to visualize or present Jenkins Pipeline status/progress.

Step[](https://www.jenkins.io/doc/book/glossary/#step)
A single task; fundamentally steps tell Jenkins _what_ to do inside of a [Pipeline](https://www.jenkins.io/doc/book/glossary/#pipeline) or [job](https://www.jenkins.io/doc/book/glossary/#job). See [Pipelines / Getting Started](https://www.jenkins.io/doc/book/pipeline/getting-started/) and [Pipeline / Using a jenkinsfile](https://www.jenkins.io/doc/book/pipeline/jenkinsfile/) for more info.

Trigger[](https://www.jenkins.io/doc/book/glossary/#trigger-1)
[](https://www.jenkins.io/doc/book/glossary/) A criteria for triggering a new [Pipeline](https://www.jenkins.io/doc/book/glossary/#pipeline) run or [job](https://www.jenkins.io/doc/book/glossary/#job).

Update Center[](https://www.jenkins.io/doc/book/glossary/#update-center-1)
[](https://www.jenkins.io/doc/book/glossary/) Hosted inventory of plugins and plugin metadata to enable plugin installation from within Jenkins.

Upstream[](https://www.jenkins.io/doc/book/glossary/#upstream-1)
[](https://www.jenkins.io/doc/book/glossary/) A configured [Pipeline](https://www.jenkins.io/doc/book/glossary/#pipeline) or [job](https://www.jenkins.io/doc/book/glossary/#job) which triggers a separate Pipeline or Job as part of its execution.

View[](https://www.jenkins.io/doc/book/glossary/#view-1)
[](https://www.jenkins.io/doc/book/glossary/) A way of displaying the data of Jenkins in a dashboard style. This is an extensible object, so there are lots of different ways to list [jobs](https://www.jenkins.io/doc/book/glossary/#job), show trends, and analyze data.

Workspace[](https://www.jenkins.io/doc/book/glossary/#workspace-1)
[](https://www.jenkins.io/doc/book/glossary/) A disposable directory on the file system of a [Node](https://www.jenkins.io/doc/book/glossary/#node) where work can be done by a [Pipeline](https://www.jenkins.io/doc/book/glossary/#pipeline) or [job](https://www.jenkins.io/doc/book/glossary/#job). Workspaces are typically left in place after a [Build](https://www.jenkins.io/doc/book/glossary/#build) or [Pipeline](https://www.jenkins.io/doc/book/glossary/#pipeline) run completes unless specific Workspace cleanup policies have been put in place on the Jenkins [Controller](https://www.jenkins.io/doc/book/glossary/#controller).
