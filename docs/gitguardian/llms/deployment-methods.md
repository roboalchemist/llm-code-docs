# Source: https://docs.gitguardian.com/honeytoken/deploy-honeytokens/deployment-methods.md

# Deployment methods

> Available methods for deploying honeytokens: automated deployment jobs, manual insertion, and custom scripts via the GitGuardian API.

# Deployment methods

Deploying honeytokens can be accomplished through various methods, each suited to different needs and scenarios:

## Automatically and at scale with Deployment jobs

:::info
Deployment jobs are only available for workspaces under the Business plan.
::: 

Deployment jobs enable the automated deployment of honeytokens into code repositories that are integrated with GitGuardian. For an in-depth exploration of Deployment jobs, please refer to [our detailed page on this topic](../deploy-honeytokens/deployment-jobs).

This approach is highly recommended for broad coverage across numerous repositories, offering an efficient and streamlined process.

## Manually
Manual deployment of honeytokens is always an option. This involves creating a honeytoken from the GitGuardian dashboard, copying the AWS key, and then inserting it into the asset you wish to monitor. Detailed instructions for this process can be found on our [Getting Started](../getting-started.md#create-and-deploy-your-first-honeytoken) page.

This method is particularly useful for assets not under GitGuardian's monitoring or in scenarios where automation is not feasible. It is best suited for situations involving a smaller number of assets.

:::caution
When manually inserting honeytokens into assets not integrated with GitGuardian, it's crucial to assign them distinctive names and descriptions. This way, should the honeytoken be triggered, you'll be able to identify which asset was compromised. We recommend naming the honeytoken after the asset itself and using the description field to provide additional details about its precise location. [Custom tags](../../platform/collaboration-and-sharing/custom-tags) can also be utilized to categorize your honeytokens effectively.
:::

## Via custom scripts leveraging the GitGuardian API

For those with specific needs or seeking greater flexibility, creating custom deployment scripts is a viable option. You can craft scripts that generate honeytokens by leveraging [GitGuardian's Honeytoken API](https://api.gitguardian.com/docs#tag/Honeytokens), insert them into the desired context, and then deploy them to your target assets.

This method offers a high degree of customization and control but requires a significant technical investment from the user. It is a good choice for covering a vast array of assets not supported by GitGuardian's integrations, or if you prefer to dictate the exact context in which your honeytokens are deployed.
