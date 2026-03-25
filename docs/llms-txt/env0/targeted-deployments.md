# Source: https://docs.envzero.com/guides/admin-guide/environments/targeted-deployments.md

# Source: https://docs.envzero.com/changelogs/2024/01/targeted-deployments.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🎯 Introducing: Targeted Deployments

> Targeting resources and modules, allows us to pinpoint exactly what needs to be changed, instead of deploying a whole environment. Such selective deployments minimize risks associated with broader changes, ensuring that updates are precise and efficient.
Introducing, Targeted Deployments!
The new 'Targeted Resources' section in our re/deploy flow makes selecting which resources to deploy a breeze.

Targeting resources and modules allows us to pinpoint exactly what needs to be changed instead of deploying a whole environment. Such selective deployments minimize risks associated with broader changes, ensuring that updates are precise and efficient.

Introducing **Targeted Deployments**!

The new 'Targeted Resources' section in our re/deploy flow makes selecting which resources to deploy a breeze.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/01/2d03d71-screenshot_2023-12-25_at_15.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=c69c1c39a8bfeb7c5452df79e496cf4f" alt="Feature demonstration screenshot showing new functionality" width="2618" height="1686" data-path="images/changelogs/2024/01/2d03d71-screenshot_2023-12-25_at_15.png" />
</Frame>

Avid env0 users may know the `ENV0_TERRAFORM_TARGET` [control variable](/guides/admin-guide/additional-controls), but now targeting gets 1st class support -  with easy selection via the UI, and supporting the `targets` field in the API upon creating a deployment.

Contrary to `ENV0_TERRAFORM_TARGET`, targeting resources with the new feature affects only the current deployment.

Read more about it [here](/guides/admin-guide/environments/targeted-deployments).

Built with [Mintlify](https://mintlify.com).
