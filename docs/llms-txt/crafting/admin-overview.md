# Source: https://docs.sandboxes.cloud/docs/admin-overview.md

# Admin Overview

In this chapter, we will talk about how to setup and manage Crafting from an administrator's point of view to boost your engineering team's productivity.

## Best Practices from Adopting Crafting

With Crafting, engineering teams can follow the best practices for managing their development environment more easily. These best practices include:

* Establish a standard repeatable dev environment for each project, shared by every developer
* Manage packages and libraries centrally, upgrading them from one place
* Enable end-to-end testing for each Pull Request in per-developer environments
* Allow developers to create new environment on-demand and dispose them freely
* Develop services in a production-like environment with multiple services running upstream/downstream instead of from single machine
* Manage dev resources centrally, allocate them on-demand, and clean up after use
* Control access to source code and other dev resources, store dev credentials properly

Crafting provides tooling to help achieve these best practices with an emphasis on flexibility and customizability, so each administrator can setup Crafting system best fitting for their usage scenarios.

## Overview of the Setup Process

The setup process varies greatly case by case. It can be as simple as creating an account and providing git access for just simply coding in an online workspace, which takes only a few minutes.

Depending the usage scenario and complexity of your product, it's up to each administrator to decide how much effort is required for setting it up. Typically setting up more automations requires more effort, but at the same time provides better developer experience and improves productivity.

Here is a high level overview of the setup process to provide some guidance on what you need to setup.

* [Account Setup](https://docs.sandboxes.cloud/docs/account-setup): This is for managing accounts on Crafting, and required by everyone to setup.
* [Git Access](https://docs.sandboxes.cloud/docs/git-access): This is for setting git access from Crafting sandbox to your git repository, which is the foundation of many automations and likely required in most teams
* [Setup Templates for Dev Environments](https://docs.sandboxes.cloud/docs/templates-setup): These pages talk about how to create templates to make the dev environment repeatable and optimize the experience. Most teams need to set up one or more templates. There are many topics in this part, some of which could be crucial for best dev experience in your scenario. Depending on your dev environment needs, you may not need to setup everything mentioned in this section, so please choose the relevant components to set up.
* [Git Service Integration for Preview](https://docs.sandboxes.cloud/docs/git-integration): This for further connect Crafting to your GitOps process and allow sandbox created from Pull Request more easily and automated.
* [Advanced Setup](https://docs.sandboxes.cloud/docs/advanced-setup): This includes following advanced setup topics:
  * [Home screen message and sandbox instruction](https://docs.sandboxes.cloud/docs/home-screen-message-and-sandbox-instruction): This help you educate developers in your team about using the sandbox and provide short cuts for them
  * [Secrets for storing dev credentials](https://docs.sandboxes.cloud/docs/secrets): This provides instructions on how to store dev credentials securely.
  * [Endpoint alias and endpoint routing](https://docs.sandboxes.cloud/docs/endpoint-alias): This is helpful for setting up sandbox for third party integration with callbacks and webhooks.
  * [Organizational settings](https://docs.sandboxes.cloud/docs/org-settings): This provides additional settings for you to manage the sandboxes better.
* [Setup for Kubernetes](https://docs.sandboxes.cloud/docs/kubernetes-setup): This is Kubernetes specific setup, which is important if you are using Kubernetes
* [Setup for Cloud Resources](https://docs.sandboxes.cloud/docs/cloud-resources-setup): This is to connect your sandbox with cloud resources from cloud providers such as AWS, GCP, which is important if services in your dev environments uses cloud native resources, such as SQS or Lambda

## System Maintenance

Crafting is designed to minimize the maintenance burden from administrators.

If you are using Crafting SaaS, since it's a fully managed solution, there is zero maintenance effort on your side.

If you are using Crafting Self-Hosted, our *managed self-hosting* solution will do automatic upgrading of the system and node-pool management, with permissions given to us for operating the system in your cloud account. We will also do active monitoring of the system health and respond to issues on the deployed site.