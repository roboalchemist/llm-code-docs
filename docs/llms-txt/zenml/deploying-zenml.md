# Source: https://docs.zenml.io/user-guides/production-guide/deploying-zenml.md

# Source: https://docs.zenml.io/deploying-zenml/deploying-zenml.md

# Deploy

![ZenML OSS server deployment architecture](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-4a649fec994c2d9608d7ab9c610a5d3864c2ec75%2Foss_simple_deployment.png?alt=media)

Moving your ZenML Server to a production environment offers several benefits over staying local:

1. **Scalability**: Production environments are designed to handle large-scale workloads, allowing your models to process more data and deliver faster results.
2. **Reliability**: Production-grade infrastructure ensures high availability and fault tolerance, minimizing downtime and ensuring consistent performance.
3. **Collaboration**: A shared production environment enables seamless collaboration between team members, making it easier to iterate on models and share insights.

Despite these advantages, transitioning to production can be challenging due to the complexities involved in setting up the needed infrastructure.

## Components

A ZenML deployment consists of multiple infrastructure components:

* [FastAPI server](https://github.com/zenml-io/zenml/tree/main/src/zenml/zen_server) backed with a SQLite or MySQL database
* [Python Client](https://github.com/zenml-io/zenml/tree/main/src/zenml)
* An [open-source companion ReactJS](https://github.com/zenml-io/zenml-dashboard) dashboard
* (Optional) [ZenML Pro API + Database + ZenML Pro dashboard](https://docs.zenml.io/getting-started/system-architectures)

You can read more in-depth about the system architecture of ZenML [here](https://docs.zenml.io/getting-started/system-architectures).\
This documentation page will focus on the components required to deploy ZenML OSS.

<details>

<summary>Details on the ZenML Python Client</summary>

The ZenML client is a Python package that you can install on your machine. It is used to interact with the ZenML server. You can install it using the `pip` command as outlined [here](https://docs.zenml.io/getting-started/installation).

This Python package gives you [the `zenml` command-line interface](https://sdkdocs.zenml.io/latest/cli.html) which you can use to interact with the ZenML server for common tasks like managing stacks, setting up secrets, and so on. It also gives you the general framework that lets you [author and deploy pipelines](https://docs.zenml.io/user-guides/starter-guide) and so forth.

If you want to have more fine-grained control and access to the metadata that ZenML manages, you can use the Python SDK to access the API. This allows you to create your own custom automations and scripts and is the most common way teams access the metadata stored in the ZenML server. The full documentation for the Python SDK can be found [here](https://sdkdocs.zenml.io/latest/). The full HTTP [API documentation](https://docs.zenml.io/api-reference) can also be found by adding the`/doc` suffix to the URL when accessing your deployed ZenML server.

</details>

### Deployment scenarios

When you first get started with ZenML, you have the following architecture on your machine.

![ZenML default local configuration](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-dde266f57e4ad585f3bc8b6b3735f5a4bcd41998%2FScenario1.png?alt=media)

The SQLite database that you can see in this diagram is used to store information about pipelines, pipeline runs, stacks, and other configurations. This default setup allows you to get started and try out the core features, but you won't be able to use cloud-based components like serverless orchestrators and so on.

Users can run the `zenml login --local` command to spin up a local ZenML OSS server to serve the dashboard. For the local OSS server option, the `zenml login --local` command implicitly connects the client to the server. The diagram for this looks as follows:

![ZenML with a local ZenML OSS Server](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-a101ef1823ae0aa896c5a4ecb7bd304d9ef0b9bb%2FScenario2.png?alt=media)

In order to move into production, the ZenML server needs to be deployed somewhere centrally so that the different cloud stack components can read from and write to the server. Additionally, this also allows all your team members to connect to it and share stacks and pipelines.

![ZenML centrally deployed for multiple users](https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-c6661ac5ed59f1c26ad84ef6dfb497dac101a071%2FScenario3.2.png?alt=media)

You connect to your deployed ZenML server using the `zenml login` command, and then you have the full benefits and power of ZenML. You can use all the cloud-based components, your metadata will be stored and synchronized across all the users of the server, and you can leverage features like centralized logs storage and pipeline artifact visualization.

## How to deploy ZenML

Deploying the ZenML Server is a crucial step towards transitioning to a production-grade environment for your machine learning projects. By setting up a deployed ZenML Server instance, you gain access to powerful features, allowing you to use stacks with remote components, centrally track progress, collaborate effectively, and achieve reproducible results.

Currently, there are two main options to access a deployed ZenML server:

1. **Managed deployment:** With [ZenML Pro](https://docs.zenml.io/pro) offering you can utilize a control plane to create ZenML servers, also known as [workspaces](https://docs.zenml.io/pro/core-concepts/workspaces). These workspaces are managed and maintained by ZenML's dedicated team, alleviating the burden of server management from your end. Importantly, your data remains securely within your stack, and ZenML's role is primarily to handle tracking of metadata and server maintenance.
2. **Self-hosted Deployment:** Alternatively, you have the ability to deploy ZenML on your own self-hosted environment. This can be achieved through various methods, including using [Docker](https://docs.zenml.io/deploying-zenml/deploying-zenml/deploy-with-docker), [Helm](https://docs.zenml.io/deploying-zenml/deploying-zenml/deploy-with-helm), or [HuggingFace Spaces](https://docs.zenml.io/deploying-zenml/deploying-zenml/deploy-using-huggingface-spaces). We also offer our Pro version for self-hosted deployments, so you can use our full paid feature set while staying fully in control with an air-gapped solution on your infrastructure.

Both options offer distinct advantages, allowing you to choose the deployment approach that best aligns with your organization's needs and infrastructure preferences. Whichever path you select, ZenML facilitates a seamless and efficient way to take advantage of the ZenML Server and enhance your machine learning workflows for production-level success.

### Options for deploying ZenML

Documentation for the various deployment strategies can be found in the following pages below (in our 'how-to' guides):

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden></th><th data-hidden data-type="content-ref"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><mark style="color:purple;"><strong>Deploying ZenML using ZenML Pro</strong></mark></td><td>Deploying ZenML using ZenML Pro.</td><td><a href="https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-48448fe35ac6c5bff4e03f498b8ac5f9a73f319b%2Fzenml-pro.png?alt=media">zenml-pro.png</a></td><td></td><td></td><td><a href="https://docs.zenml.io/pro/deployments/scenarios/self-hosted-deployment">https://docs.zenml.io/pro/deployments/scenarios/self-hosted-deployment</a></td></tr><tr><td><mark style="color:purple;"><strong>Deploy with Docker</strong></mark></td><td>Deploying ZenML in a Docker container.</td><td><a href="https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-b1f60f21e2fb393bc2ce1fa879b2576ff1ba9b33%2Fdocker.png?alt=media">docker.png</a></td><td></td><td></td><td><a href="deploying-zenml/deploy-with-docker">deploy-with-docker</a></td></tr><tr><td><mark style="color:purple;"><strong>Deploy with Helm</strong></mark></td><td>Deploying ZenML in a Kubernetes cluster with Helm.</td><td><a href="https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-8472d0d0d994ced4e2f3297c115a80943d4c4f08%2Fhelm.png?alt=media">helm.png</a></td><td></td><td></td><td><a href="deploying-zenml/deploy-with-helm">deploy-with-helm</a></td></tr><tr><td><mark style="color:purple;"><strong>Deploy with HuggingFace Spaces</strong></mark></td><td>Deploying ZenML to Hugging Face Spaces.</td><td><a href="https://1640328923-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F5aBlTJNbVDkrxJp7J1J9%2Fuploads%2Fgit-blob-da4344167bb225562e3503f4a0faf6ffcea64d2b%2Fhugging-face.png?alt=media">hugging-face.png</a></td><td></td><td></td><td><a href="deploying-zenml/deploy-using-huggingface-spaces">deploy-using-huggingface-spaces</a></td></tr></tbody></table>

<figure><img src="https://static.scarf.sh/a.png?x-pxid=f0b4f458-0a54-4fcd-aa95-d5ee424815bc" alt="ZenML Scarf"><figcaption></figcaption></figure>
