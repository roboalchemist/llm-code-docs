# Source: https://docs.zenml.io/stacks/component-guide.md

# Overview

If you are new to the world of MLOps, it is often daunting to be immediately faced with a sea of tools that seemingly all promise and do the same things. It is useful in this case to try to categorize tools in various groups in order to understand their value in your toolchain in a more precise manner.

## What is a stack?

The [stack](https://docs.zenml.io/user-guides/production-guide/understand-stacks) is a fundamental component of the ZenML framework. Put simply, a stack represents the configuration of the infrastructure and tooling that defines where and how a pipeline executes.

A stack comprises different stack components, where each component is responsible for a specific task. For example, a stack might have a [container registry](https://docs.zenml.io/stacks/container-registries), a [Kubernetes cluster](https://docs.zenml.io/stacks/orchestrators/kubernetes) as an [orchestrator](https://docs.zenml.io/stacks/orchestrators), an [artifact store](https://docs.zenml.io/stacks/artifact-stores), an [experiment tracker](https://docs.zenml.io/stacks/experiment-trackers) like MLflow and so on.

Each pipeline run that you execute with ZenML will require a **stack** and each **stack** will be required to include at least an **orchestrator** and an **artifact store**. Apart from these two, the other components are optional and to be added as your pipeline evolves in MLOps maturity.

## Stacks as a way to organize your execution environment

With ZenML, you can run your pipelines on more than one stacks with ease. This pattern helps you test your code across different environments effortlessly.

This enables a case like this: a data scientist starts experimentation locally on their system and then once they are satisfied, move to a cloud environment on your staging cloud account to test more advanced features of your pipeline. Finally, when all looks good, they can mark the pipeline ready for production and have it run on a production-grade stack in your production cloud account.

![Stacks as a way to organize your execution environment](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-426f4e302d40b2fc34a8ef25df4e01d7f52e7b17%2Fstack_envs.png?alt=media)

Having separate stacks for these environments helps:

* avoid wrongfully deploying your staging pipeline to production
* curb costs by running less powerful resources in staging and testing locally first
* control access to environments by granting permissions for only certain stacks to certain users

## How to manage credentials for your stacks

Most stack components require some form of credentials to interact with the underlying infrastructure. For example, a container registry needs to be authenticated to push and pull images, a Kubernetes cluster needs to be authenticated to deploy models as a web service, and so on.

The preferred way to handle credentials in ZenML is to use [Service Connectors](https://docs.zenml.io/how-to/infrastructure-deployment/auth-management/service-connectors-guide). Service connectors are a powerful feature of ZenML that allow you to abstract away credentials and sensitive information from your team.

![Service Connectors abstract away complexity and implement security best practices](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-634568dfe8cb91b57e7e3a4bfe4026fa6f7c0dee%2FConnectorsDiagram.png?alt=media)

### Recommended roles

Ideally, you would want that only the people who deal with and have direct access to your cloud resources are the ones that are able to create Service Connectors. This is useful for a few reasons:

* **Less chance of credentials leaking**: the more people that have access to your cloud resources, the higher the chance that some of them will be leaked.
* **Instant revocation of compromised credentials**: folks who have direct access to your cloud resources can revoke the credentials instantly if they are compromised, making this a much more secure setup.
* **Easier auditing**: you can have a much easier time auditing and tracking who did what if you have a clear separation between the people who can create Service Connectors (who have direct access to your cloud resources) and those who can only use them.

### Recommended workflow

![Recommended workflow for managing credentials](https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-c8e90bc3e319ac88fa37ba746f061bc3f1119ff6%2Fservice_con_workflow.png?alt=media)

Here's an approach you can take that is a good balance between convenience and security:

* Have a limited set of people that have permissions to create Service Connectors. These are ideally people that have access to your cloud accounts and know what credentials to use.
* You can create one connector for your development or staging environment and let your data scientists use that to register their stack components.
* When you are ready to go to production, you can create another connector with permissions for your production environment and create stacks that use it. This way you can ensure that your production resources are not accidentally used for development or staging.

If you follow this approach, you can keep your data scientists free from the hassle of figuring out the best authentication mechanisms for the different cloud services, having to manage credentials locally, and keep your cloud accounts safe, while still giving them the freedom to run their experiments in the cloud.

{% hint style="info" %}
Please note that restricting permissions for users through roles is a ZenML Pro feature. You can read more about it [here](https://docs.zenml.io/pro/access-management/roles). Sign up for a free trial here: <https://zenml.io/pro>.
{% endhint %}

## How to deploy and manage stacks

Deploying and managing a MLOps stack is tricky.

* Each tool comes with a certain set of requirements. For example, a [Kubeflow installation](https://www.kubeflow.org/docs/started/installing-kubeflow/) will require you to have a Kubernetes cluster, and so would a **Seldon Core deployment**.
* Figuring out the defaults for infra parameters is not easy. Even if you have identified the backing infra that you need for a stack component, setting up reasonable defaults for parameters like instance size, CPU, memory, etc., needs a lot of experimentation to figure out.
* Many times, standard tool installations don't work out of the box. For example, to run a custom pipeline in [Vertex AI](https://cloud.google.com/vertex-ai), it is not enough to just run an imported pipeline. You might also need a custom service account that is configured to perform tasks like reading secrets from your secret store or talking to other GCP services that your pipeline might need.
* Some tools need an additional layer of installations to enable a more secure, production-grade setup. For example, a standard **MLflow tracking server** deployment comes without an authentication frontend which might expose all of your tracking data to the world if deployed as-is.
* All the components that you deploy must have the right permissions to be able to talk to each other. For example, your workloads running in a Kubernetes cluster might require access to the container registry or the code repository, and so on.
* Cleaning up your resources after you're done with your experiments is super important yet very challenging. For example, if your Kubernetes cluster has made use of [Load Balancers](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer), you might still have one lying around in your account even after deleting the cluster, costing you money and frustration.

All of these points make taking your pipelines to production a more difficult task than it should be. We believe that the expertise in setting up these often-complex stacks shouldn't be a prerequisite to running your ML pipelines.

This docs section consists of information that makes it easier to provision, configure, and extend stacks and components in ZenML.

## Stack Components Guide

Here is a full list of all stack components currently supported in ZenML, with a description of the role of that component in the MLOps process:

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Orchestrator</strong></td><td>Orchestrating the runs of your pipeline</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-dd309c171622d6711dff0c0d3dd5a942effd97b7%2Fdeployer.png?alt=media">deployer.png</a></td><td><a href="stack-components/orchestrators">orchestrators</a></td></tr><tr><td><strong>Deployer</strong></td><td>Deploying pipelines as long-running HTTP services</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-dd309c171622d6711dff0c0d3dd5a942effd97b7%2Fdeployer.png?alt=media">deployer.png</a></td><td><a href="stack-components/deployers">deployers</a></td></tr><tr><td><strong>Artifact Store</strong></td><td>Storage for the artifacts created by your pipelines</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-8f674d0dc3437f09ac94a917436c5e9d0d46d462%2Fartifact-store.png?alt=media">artifact-store.png</a></td><td><a href="stack-components/artifact-stores">artifact-stores</a></td></tr><tr><td><strong>Container Registry</strong></td><td>Store for your containers</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-19b1a285e38c198381540bf64c56e6a4e91206c5%2Fcontainer-registry.png?alt=media">container-registry.png</a></td><td><a href="stack-components/container-registries">container-registries</a></td></tr><tr><td><strong>Data Validator</strong></td><td>Data and model validation</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-c3b813ee25445504f6f3a8d25ff6d9b2a508b846%2Fdata-validator.png?alt=media">data-validator.png</a></td><td><a href="stack-components/data-validators">data-validators</a></td></tr><tr><td><strong>Experiment Tracker</strong></td><td>Tracking your ML experiments</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-fd527f9dc6e513c18d058445a8c88a09a84b4fd8%2Fexperiment-tracker.png?alt=media">experiment-tracker.png</a></td><td><a href="stack-components/experiment-trackers">experiment-trackers</a></td></tr><tr><td><strong>Model Deployer</strong></td><td>Services/platforms responsible for online model serving</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-6ef74533ff2936c7d8fde9514689d5af64b79592%2Fmodel-deployer.png?alt=media">model-deployer.png</a></td><td><a href="stack-components/model-deployers">model-deployers</a></td></tr><tr><td><strong>Step Operator</strong></td><td>Execution of individual steps in specialized runtime environments</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-9974f35929eed29cd6f030dd0df5fb96f90b8063%2Fstep-operator.png?alt=media">step-operator.png</a></td><td><a href="stack-components/step-operators">step-operators</a></td></tr><tr><td><strong>Alerter</strong></td><td>Sending alerts through specified channels</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-5c8d0ab2b58a376ff59a7fc29a89d7112645535a%2Falerter.png?alt=media">alerter.png</a></td><td><a href="stack-components/alerters">alerters</a></td></tr><tr><td><strong>Image Builder</strong></td><td>Builds container images.</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-9e79b1fdf7c098e68c1242547a12b452836b08c8%2Fimage-builder.png?alt=media">image-builder.png</a></td><td><a href="stack-components/image-builders">image-builders</a></td></tr><tr><td><strong>Annotator</strong></td><td>Labeling and annotating data</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-000d86bbc9c361e14434bb21daa91feddeedf20d%2Fannotator.png?alt=media">annotator.png</a></td><td><a href="stack-components/annotators">annotators</a></td></tr><tr><td><strong>Model Registry</strong></td><td>Manage and interact with ML Models</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-ec8e81121f64abbcb0b5f1c877873fa0bc2ae70a%2Fmodel-registry.png?alt=media">model-registry.png</a></td><td><a href="stack-components/model-registries">model-registries</a></td></tr><tr><td><strong>Feature Store</strong></td><td>Management of your data/features</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-5d2b54f1d64fe48403f2ce944be6ff9881e14caa%2Ffeature-store.png?alt=media">feature-store.png</a></td><td><a href="stack-components/feature-stores">feature-stores</a></td></tr></tbody></table>

## Custom Implementations

You can take control of how ZenML behaves by creating your own components. This is done by writing custom component `flavors`.

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Component Flavors</strong></td><td>How to write a custom stack component flavor</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-03a423193861bc34995dbcecf576c1dc8cca2dbb%2Fflavors.png?alt=media">flavors.png</a></td><td><a href="https://docs.zenml.io/stacks/contribute/custom-stack-component">https://docs.zenml.io/stacks/contribute/custom-stack-component</a></td></tr><tr><td><strong>Custom orchestrator guide</strong></td><td>Learn how to develop a custom orchestrator</td><td><a href="https://1559531010-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fu4tnWimk4Ev9z09qY15M%2Fuploads%2Fgit-blob-23c39d4845930152e4826c178c5a2fbff3974874%2Fcustom-orchestrator.png?alt=media">custom-orchestrator.png</a></td><td><a href="stack-components/orchestrators/custom">custom</a></td></tr></tbody></table>
