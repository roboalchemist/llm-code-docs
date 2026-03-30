# Source: https://docs.cohere.com/docs/oracle-cloud-infrastructure-oci.mdx

***

title: Cohere on Oracle Cloud Infrastructure (OCI)
slug: docs/oracle-cloud-infrastructure-oci
hidden: false
description: >-
This page describes how to work with Cohere models on Oracle Cloud
Infrastructure (OCI)
image:
type: fileId
value: 'https://files.buildwithfern.com/cohere.docs.buildwithfern.com/8ba30b46486ea7bfab24f3e8856d7411d1b745b26e9026abff3ee62af52ce268/assets/images/f1cc130-cohere_meta_image.jpg'
keywords: 'generative AI, large language models, Oracle Cloud Infrastructure, OCI'
createdAt: 'Mon Feb 22 2024 14:53:59 GMT+0000 (Coordinated Universal Time)'
updatedAt: 'Wed May 31 2024 16:11:36 GMT+0000 (Coordinated Universal Time)'
---------------------------------------------------------------------------

In an effort to make our language-model capabilities more widely available, we've partnered with a few major platforms to create hosted versions of our offerings.

Here, you'll learn how to use Oracle Cloud Infrastructure (OCI) to deploy both the Cohere Command and the Cohere Embed models on the AWS cloud computing platform. The following models are available on OCI:

* Command A Reasoning
* Command A Vision
* Command A
* Command R+ 08-2024
* Command R 08-2024
* Command R+ (retired)
* Command R (retired)
* Command (deprecated)
* Command light (deprecated)
* Embed v4
* Embed English v3
* Embed English v3 light
* Embed Multilingual v3
* Embed Multilingual v3 light
* Rerank v3.5

We also support fine-tuning for Command R (`command-r-04-2024` and `command-r-08-2024`) on OCI.

For the most updated list of available models, see the [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/pretrained-models.htm).

## Working With Cohere Models on OCI

* [Embeddings generation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-embed.htm#playground-embed)

And OCI offers three ways to perform these workloads:

* The console
* The CLI
* The API

In the sections that follow, we'll briefly outline how to use each, and link out to other documentation to fill in any remaining gaps.

### The Console

OCI offers a console through which you can perform many generative AI tasks. It allows you to select your region and the model you wish to use, then pass a prompt to the underlying model, configuring parameters as you wish.

![](https://files.buildwithfern.com/cohere.docs.buildwithfern.com/9aa2a794b51f000832d20fe9bc0619fca2bd2ad26b0983a540d976787d36b558/assets/images/oracle-cloud-infrastructure-oci-1.png)

If you want to use the console for [chat](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-chat.htm), [text generation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-generate.htm#playground-generate), [summarization](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-summarize.htm#playground-summarize), and [embeddings](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-embed.htm#playground-embed), visit those links and select "console."

![](https://files.buildwithfern.com/cohere.docs.buildwithfern.com/121e70d45610e7a1461d59cf071523d4580b319fe38d0868b2731e89de68efe7/assets/images/oracle-cloud-infrastructure-oci-2.png)

### The CLI

With OCI's command line interface (CLI), it's possible to use Cohere models to generate text, get embeddings, or extract information.

![](https://files.buildwithfern.com/cohere.docs.buildwithfern.com/7e85610c9157b08ce77670bee90995c3d86e13e4f54859dbf0a77b944f82c423/assets/images/oracle-cloud-infrastructure-oci-3.png)

If you want to use the console for [text generation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-generate.htm#playground-generate), [summarization](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-summarize.htm#playground-summarize), and [embeddings](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-embed.htm#playground-embed), visit those links and select "CLI."

![](https://files.buildwithfern.com/cohere.docs.buildwithfern.com/b7b63049d41e533c4bd2e3628a01a2c4a1f98e18d5bf0b311a3f7dc09081c07e/assets/images/oracle-cloud-infrastructure-oci-4.png)

### The API

If you're trying to use Cohere models on OCI programmatically -- i.e. as part of software development, or while building an application -- you'll likely want to use the API.

![](https://files.buildwithfern.com/cohere.docs.buildwithfern.com/73b388b30af68734650780290ffe70f806f3e21057e4497988f667a1b7e672e3/assets/images/oracle-cloud-infrastructure-oci-5.png)

If you want to use the console for [text generation](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-generate.htm#playground-generate), [summarization](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-summarize.htm#playground-summarize), and [embeddings](https://docs.oracle.com/en-us/iaas/Content/generative-ai/use-playground-embed.htm#playground-embed), visit those links and select "API."

![](https://files.buildwithfern.com/cohere.docs.buildwithfern.com/0267471ffc16090af14581883b17a61eebabdce4cef3b37b508267e21efd46c4/assets/images/oracle-cloud-infrastructure-oci-6.png)
