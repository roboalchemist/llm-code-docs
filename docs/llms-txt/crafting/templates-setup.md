# Source: https://docs.sandboxes.cloud/docs/templates-setup.md

## Setup Templates for Dev Environments

Standardized and replicable development environments is critical for maximizing the team's productivity and minimizing the maintenance overhead. Crafting offers powerful `Template System` for engineering teams define and evolve their dev environments centrally and in a managed way.

### What are templates

On Crafting platform, a `Template` is a pre-set definition of a sandbox setup that is shared within a team and can be used to create sandboxes. Since a `template` is often used to represent the entire app end-to-end, it's also called `app`.

Since a `sandbox` represents a full-fledged end-to-end development environment, including potentially multiple `workspaces`, `containers`, `dependencies`, `resources`, `endpoints`, etc., setting it up from scratch takes a decent amount of effort. A `template` saves the setup effort and makes new sandbox creation according to a common standard as easy as one click.

### Why using templates

In short, the key reason to use templates is for *manageability of dev environments*. For individual developers working on a small side project, templating may be an overkill, but for a team of developers working on an end-to-end product, setting a shared standardized dev environment with template is essential for productivity. Specifically, using templates have following benefits:

* **Robustness**: Whole team is able to share common configurations and if anything broken in the dev environment, it's quickly detected and fixed. If anything breaks in one sandbox, just creating a new one with the template to get a fresh dev environment that is ready to code.
* **Consistent**: Not only the developers have their dev environments consistent with each other, the common dev environments can also be made more consistent with production.
* **Quick onboarding**: New members to the team can get started right away without going through a lengthy environment setup step.
* **Easy to update**: For applying patches and upgrading libraries, there is no need for everyone to update their environments individually. One person makes the update in template, and pushes to everyone using the same template.
* **Collaboration**: Using a common base of setup reduces communication gap and allows team members to share best practices and trouble-shoot easily.

In summary, **the more standardized the dev environment is, the more productive the team is**. Note that Crafting allows each developer apply their own layer of customization on top of shared templates in a repeatable way. For different teams with different dev environments needs, we suggest to use different templates so that each template is best fit for its purpose.

## Outline of this section

In remainder of this section, we go though the steps for setting up a template end-to-end

* [Template builder wizard](https://docs.sandboxes.cloud/docs/template-builder): how to use the template builder wizard provided by Crafting to quickly setup ground work for a template.
* [Standalone sandbox](https://docs.sandboxes.cloud/docs/standalone-sandbox): basics of the `standalone sandbox` we use for building templates, also known as `template builder sandbox`.
* [Setup workspaces](https://docs.sandboxes.cloud/docs/workspaces-setup): steps to setup each dev container (`workspace`) to make it ready to code.
* [Setup containers and dependencies](https://docs.sandboxes.cloud/docs/containers-dependencies-setup): how to setup built-in dependencies such as `Postgres`, `Redis`, `ElasticSearch`, etc., and custom containers to support your services running in `workspaces`.
* [Network configuration and endpoints](https://docs.sandboxes.cloud/docs/network-setup): how to let components in the sandbox communicate with each other and how to access services running in the sandbox from outside via `endpoints`.
* [Integrate resources](https://docs.sandboxes.cloud/docs/resources-setup): how to integrate external resources including per-dev namespaces in Kubernetes cluster and cloud native resources from cloud provider, such as `RDS`, `Lambda`.
* [Checklist and best practices for templates](https://docs.sandboxes.cloud/docs/templates-best-practices): putting everything together and best practices for managing templates.
