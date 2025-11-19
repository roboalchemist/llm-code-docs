# Source: https://huggingface.co/docs/hub/xet/index.md

# Source: https://huggingface.co/docs/hub/index.md

# Source: https://huggingface.co/docs/hub/xet/index.md

# Source: https://huggingface.co/docs/hub/index.md

# Hugging Face Hub documentation

The Hugging Face Hub is a platform with over 2M models, 500k datasets, and 1M demo apps (Spaces), all open source and publicly available, in an online platform where people can easily collaborate and build ML together. The Hub works as a central place where anyone can explore, experiment, collaborate, and build technology with Machine Learning. Are you ready to join the path towards open source Machine Learning? 🤗

 Subscriptions &  Plans
PRO subscription
Team & Enterprise Plans
Single Sign-On (SSO)
Audit Logs
Storage Regions
Data Studio for Private datasets
Resource Groups
Advanced Security
Tokens Management
Network Security
Rate Limits

 Repositories
Introduction
Getting Started
Repository Settings
Storage Limits
Storage Backend (Xet)
Pull requests and Discussions
Notifications
Collections
Webhooks
Next Steps
Licenses

     Models
Introduction
The Model Hub
Model Cards
Gated Models
Uploading Models
Downloading Models
Libraries
Tasks
Widgets
Inference API
Download Stats

 Datasets
Introduction
Datasets Overview
Dataset Cards
Gated Datasets
Uploading Datasets
Downloading Datasets
Libraries
Dataset Viewer
Download Stats
Data files Configuration

 Spaces
Introduction
Spaces Overview
Gradio Spaces
Static HTML Spaces
Docker Spaces
ZeroGPU Spaces
Embed your Space
Run with Docker
Reference
Advanced Topics
Sign in with HF

 Other
Organizations
Billing
Security
Moderation
Paper Pages
Search
Digital Object Identifier (DOI)
Hub API Endpoints
Sign in with HF
Contributor Code of Conduct
Content Guidelines

## What's the Hugging Face Hub?

We are helping the community work together towards the goal of advancing Machine Learning 🔥.

The Hugging Face Hub is a platform with over 2M models, 500k datasets, and 1M demos in which people can easily collaborate in their ML workflows. The Hub works as a central place where anyone can share, explore, discover, and experiment with open-source Machine Learning.

No single company, including the Tech Titans, will be able to “solve AI” by themselves – the only way we'll achieve this is by sharing knowledge and resources in a community-centric approach. We are building the largest open-source collection of models, datasets, and demos on the Hugging Face Hub to democratize and advance ML for everyone 🚀.

We encourage you to read the [Code of Conduct](https://huggingface.co/code-of-conduct) and the [Content Guidelines](https://huggingface.co/content-guidelines) to familiarize yourself with the values that we expect our community members to uphold 🤗.

## What can you find on the Hub?

The Hugging Face Hub hosts Git-based repositories, which are version-controlled buckets that can contain all your files. 💾

On it, you'll be able to upload and discover...

- Models: _hosting the latest state-of-the-art models for LLM, text, vision, and audio tasks_
- Datasets: _featuring a wide variety of data for different domains and modalities_
- Spaces: _interactive apps for demonstrating ML models directly in your browser_

The Hub offers **versioning, commit history, diffs, branches, and over a dozen library integrations**! 
All repositories build on [Xet](./xet/index), a new technology to efficiently store Large Files inside Git, intelligently splitting files into unique chunks and accelerating uploads and downloads.

You can learn more about the features that all repositories share in the [**Repositories documentation**](./repositories).

## Models

You can discover and use dozens of thousands of open-source ML models shared by the community. To promote responsible model usage and development, model repos are equipped with [Model Cards](./model-cards) to inform users of each model's limitations and biases. Additional [metadata](./model-cards#model-card-metadata) about info such as their tasks, languages, and evaluation results can be included, with training metrics charts even added if the repository contains [TensorBoard traces](./tensorboard). It's also easy to add an [**inference widget**](./models-widgets) to your model, allowing anyone to play with the model directly in the browser! For programmatic access, a serverless API is provided by [**Inference Providers**](./models-inference).

To upload models to the Hub, or download models and integrate them into your work, explore the [**Models documentation**](./models). You can also choose from [**over a dozen libraries**](./models-libraries) such as 🤗 Transformers, Asteroid, and ESPnet that support the Hub.

## Datasets

The Hub is home to over 500k public datasets in more than 8k languages that can be used for a broad range of tasks across NLP, Computer Vision, and Audio. The Hub makes it simple to find, download, and upload datasets. Datasets are accompanied by extensive documentation in the form of [**Dataset Cards**](./datasets-cards) and [**Data Studio**](./datasets-viewer) to let you explore the data directly in your browser. While many datasets are public, [**organizations**](./organizations) and individuals can create private datasets to comply with licensing or privacy issues. You can learn more about [**Datasets here on the Hugging Face Hub documentation**](./datasets-overview).

The [🤗 `datasets`](https://huggingface.co/docs/datasets/index) library allows you to programmatically interact with the datasets, so you can easily use datasets from the Hub in your projects. With a single line of code, you can access the datasets; even if they are so large they don't fit in your computer, you can use streaming to efficiently access the data.

## Spaces

[Spaces](https://huggingface.co/spaces) is a simple way to host ML demo apps on the Hub. They allow you to build your ML portfolio, showcase your projects at conferences or to stakeholders, and work collaboratively with other people in the ML ecosystem.

We currently support two awesome Python SDKs (**[Gradio](https://gradio.app/)** and **[Streamlit](./spaces-sdks-streamlit)**) that let you build cool apps in a matter of minutes. Users can also create static Spaces, which are simple HTML/CSS/JavaScript pages, or deploy any Docker-based application.

If you need GPU power for your demos, try [**ZeroGPU**](./spaces-zerogpu): it dynamically provides NVIDIA H200 GPUs, in real-time, only when needed.

After you've explored a few Spaces (take a look at our [Space of the Week!](https://huggingface.co/spaces)), dive into the [**Spaces documentation**](./spaces-overview) to learn all about how you can create your own Space. You'll also be able to upgrade your Space to run on a GPU or other accelerated hardware. ⚡️

## Organizations

Companies, universities and non-profits are an essential part of the Hugging Face community! The Hub offers [**Organizations**](./organizations), which can be used to group accounts and manage datasets, models, and Spaces. Educators can also create collaborative organizations for students using [Hugging Face for Classrooms](https://huggingface.co/classrooms). An organization's repositories will be featured on the organization’s page and every member of the organization will have the ability to contribute to the repository. In addition to conveniently grouping all of an organization's work, the Hub allows admins to set roles to [**control access to repositories**](./organizations-security), and manage their organization's [payment method and billing info](https://huggingface.co/pricing). Machine Learning is more fun when collaborating! 🔥

[Explore existing organizations](https://huggingface.co/organizations), create a new organization [here](https://huggingface.co/organizations/new), and then visit the [**Organizations documentation**](./organizations) to learn more.

## Security

The Hugging Face Hub supports security and access control features to give you the peace of mind that your code, models, and data are safe. Visit the [**Security**](./security) section in these docs to learn about:

- User Access Tokens
- Access Control for Organizations
- Signing commits with GPG
- Malware scanning

