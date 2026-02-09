# Source: https://docs.sandboxes.cloud/docs/use-case-standardization.md

# Maintainable Dev Environments

In this section, we describe the use case of setting up maintainable dev environments for your development team with Crafting. We will start by a deeper dive into the potential issues of local dev environments and point out the best practices you can achieve with Crafting.

| Issues on Local Machine                                                                                                               | Best Practice with Crafting                                                                                                                                                                                                             |
| :------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CPU architecture and operating system consistency issue](#cpu-architecture-and-operating-system-consistency-issue)                   | [Use standard architecture and dev OS image matching production](#use-standard-architecture-and-dev-os-image-matching-production)                                                                                                       |
| [High overhead and error-prone process in environment setup](#high-overhead-and-error-prone-process-in-environment-setup)             | [Repeatable dev environments, setup on-demand, clean up automatically](#repeatable-dev-environments-setup-on-demand-clean-up-automatically)                                                                                             |
| [Dev environment maintenance and frequent breakage](#dev-environment-maintenance-and-frequent-breakage)                               | [Version controlled update on environments, automatic rollout](#version-controlled-update-on-environments-automatic-rollout)                                                                                                            |
| [Scalability issues in terms of number of services and developers](#scalability-issues-in-terms-of-number-of-services-and-developers) | [Manage multiple types of dev environments with app templates](#manage-multiple-types-of-dev-environments-with-app-templates) [Centralized monitoring and online trouble-shooting](#centralized-monitoring-and-online-trouble-shooting) |

## Issues with local dev environments

As your development team scales, how to make sure the dev environments they use in their day-to-day work maintainable is crucial for their productivity. Since modern software development usually requires developers to piece together several technologies, there are several common pain-points for each engineer relying on local machine for development.

### CPU architecture and operating system consistency issue

The first issue local dev environment faces is related to the consistency between local and production. Even though in production, majority of the cloud services are running by CPUs in x86 architecture on top of Linux operating system, the local machines are much more heterogenous.

Developers commonly uses MacBook Pro with M1 chip, which is arm architecture with a different instruction set than x86. Programs and libraries often have subtle differences in their behavior, which could raise many compatibility issues. In addition, the most commonly used operating system on developers' laptop is actually not Linux. Many of them are using Mac OS and Windows, which could bring more variables and potential issues into the fold.

As a result, there are common issues causing developers unable to run the service they want to code on their local machine, or even worse, have developed features on their local machine, which fail to work in production. Although virtualization and containerization can help to some extent, they are often imperfect and could cause hard-to-reproduce issues. The end solution, is still to have the dev environment consist with production in terms of CPU architecture and operating system.

### High overhead and error-prone process in environment setup

Another common issue for local dev environments is the high overhead in setup. It often takes *hours, days, or sometimes a week* for a new engineer to setup their dev environments on their local machine. The process is often based on some documentation on wiki or in codebase, often outdated and/or littered with assumptions of knowing certain tribal knowledge. As a result, even after a long setup, their local dev environment may still miss some important tweaks, which cause future problems.

Automation scripts and containerization can certainly alleviate the problem, but still requiring the developer to fiddle with their local machine to apply them, and the consistency issue in CPU and OS mentioned above makes it sometimes hard to deal with.

### Dev environment maintenance and frequent breakage

In addition to setup, the maintenance of dev environments is often a troublesome issue. Production system often requires relatively new library versions because of security patch and needed features. When one engineer upgrades a library version and get it to work on his environment, it sometimes breaks everyone else's dev environment. And then everyone needs to stop their work and upgrade their local dev environments following some ad hoc instructions, which may fail to work if the have heterogenous local environment like different OS versions, potentially leading to a cascading upgrade.

That's why developers are usually reluctant to update their dev environments, but that makes their environments more outdated and harder to catch up in the future, resulting in a vicious circle.

### Scalability issues in terms of number of services and developers

If it is still maintainable with a single service/codebase and a small team, dev environments become very difficult to manage with many services and a large team as the company scales.

When there are multiple services to work on, developers with different roles often need to customize their dev environments fitting their roles, making a simple one-dev-image-fits-all approach fail to work. They often need to launch different sets of services and dependencies for their development and have them integrated in a certain way. Consistency issues are naturally introduced when everyone only relies on their local machines.

With a large team of developers, it's also very hard for everyone to follow a standard practice on their local machines without proper guardrails. As a result, developers' dev environment may fail due to some mis-operations. When something went wrong, it's often very difficult for the infra team to diagnose the issue on developer local machine. It's also hard for the infra team monitor the health of dev environments for a large team of engineers.

## Best practices for maintainable dev environments with Crafting

Facing these issues, now let's talk about the best practice Crafting helps to bring to your dev team.

### Use standard architecture and dev OS image matching production

With Crafting, you can easily manage a standard Linux OS image matching the production running on the same CPU architecture like your production machines. Crafting allows you to specify a machine pool in your cloud and use your custom Linux OS image for the dev containers. When all the developers use a homogeneous dev environment align with the production, there is no behavior gaps between development and production, completely resolving the consistency issue.

### Repeatable dev environments, setup on-demand, clean up automatically

Based on Crafting platform, your developers can create new dev environments on-demand with a single click, eliminating the long onboarding time of setting up dev environments for new developers in the team. With the automation supported by Crafting, the dev environments are launched ready-to-code. They are pre-installed with all the necessary dev tools and libraries, and even have the proper background process running for testing your code change.

Developers can easily create multiple dev environments for developing different features, no longer limited by a single dev environment on their local machine. The inactive dev environments are suspended and recycled automatically by the platform, so that there is no dangling environments wasting computing resources.

### Version controlled update on environments, automatic rollout

Regarding upgrading dev environments, Crafting makes it easy by allowing to standardize the process. From dev OS images to versions of dev packages and dependency services, every aspects of dev environments in Crafting is centrally managed and versioned. Any update on any part can be tested first on a sandbox, and saved as a new version of the template for every newly created dev environments to automatically pick up.

Developers no longer need to pay special attention to maintain their dev environments on their local machine, and never need to worry about any environment update will break their local, because they can easily create a new environment with latest updates, which is centrally tested and guaranteed to work properly.

### Manage multiple types of dev environments with templates

For different teams developing different parts of the overall product, Crafting allows different templates to be used to set up their specific dev environments. For example, if team A only need service X, Y, Z to be running for development, they can create their version of the template to only include these services, instead of including everything. Different flavors of the dev environments makes it flexible to support complex apps with many services and teams.

Meanwhile, Crafting allows all the configurations to be managed centrally and composed in parts. This central management allows cross-cutting changes to be made easily for security or compliance reasons.

### Centralized monitoring and online trouble-shooting

Since Crafting centralizes the dev environments on cloud, standard practices and guardrails can be easily implemented by the infra team even facing a large number of developers to work with. There will be less breakage due to local errors, and even if something goes wrong, it's relatively easy for the intra team to hop on the cloud container to see what is the exact problem and fix it.

In addition, the health of everyone's dev environments can be monitored easily on cloud, allowing the infra team to spot problems and react to issues quickly.