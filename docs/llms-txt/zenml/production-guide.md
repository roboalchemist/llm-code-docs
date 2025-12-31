# Source: https://docs.zenml.io/user-guides/production-guide.md

# Production guide

The ZenML production guide builds upon the [Starter guide](https://docs.zenml.io/user-guides/starter-guide) and is the next step in the MLOps Engineer journey with ZenML. If you're an ML practitioner hoping to implement a proof of concept within your workplace to showcase the importance of MLOps, this is the place for you.

<figure><img src="https://3621652509-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F75OYotLPi8TviSrtZTJZ%2Fuploads%2Fgit-blob-af05c5cdb98d181e65feb849e320eb81b678e2ec%2Fstack_showcase.png?alt=media" alt=""><figcaption><p>ZenML simplifies development of MLOps pipelines that can span multiple production stacks.</p></figcaption></figure>

This guide will focus on shifting gears from running pipelines *locally* on your machine, to running them in *production* in the cloud. We'll cover:

* [Deploying ZenML](https://docs.zenml.io/user-guides/production-guide/deploying-zenml)
* [Understanding stacks](https://docs.zenml.io/user-guides/production-guide/understand-stacks)
* [Connecting remote storage](https://docs.zenml.io/user-guides/production-guide/remote-storage)
* [Orchestrating on the cloud](https://docs.zenml.io/user-guides/production-guide/cloud-orchestration)
* [Configuring the pipeline to scale compute](https://docs.zenml.io/user-guides/production-guide/configure-pipeline)
* [Configure a code repository](https://docs.zenml.io/user-guides/production-guide/connect-code-repository)

Like in the starter guide, make sure you have a Python environment ready and `virtualenv` installed to follow along with ease. As now we are dealing with cloud infrastructure, you'll also want to select one of the major cloud providers (AWS, GCP, Azure), and make sure the respective CLIs are installed and authorized.

By the end, you will have completed an [end-to-end](https://docs.zenml.io/user-guides/production-guide/end-to-end) MLOps project that you can use as inspiration for your own work. Let's get right into it!

{% hint style="info" %}
Throughout this guide, we will be referencing internal ZenML functions and classes, which are more easily discoverable in the [SDK Docs](https://sdkdocs.zenml.io/). Consult the SDK docs if you're ever stuck!
{% endhint %}

<figure><img src="https://static.scarf.sh/a.png?x-pxid=f0b4f458-0a54-4fcd-aa95-d5ee424815bc" alt="ZenML Scarf"><figcaption></figcaption></figure>
